"""Create an on-demand project record from its registered template without overwriting."""
import argparse
import hashlib
import json
from pathlib import PurePosixPath
from workflow_support import bounded_path, document_template_plan, package_root, read_binding, rebase_links

MAX_NAME_LENGTH = 120
_CAPTURED_FAILURES = (OSError, ValueError, KeyError, TypeError)


class PartialDocumentCreationError(Exception):
    """A new target was exclusively opened, but its contents could not be verified."""

    def __init__(self, path, cause):
        self.receipt = {
            'status': 'PARTIAL_RETAINED',
            'created': True,
            'path': path,
            'reason': f'{type(cause).__name__}: {cause}',
            'recovery': (
                'Inspect the retained file and compare it with the registered template '
                'and active binding. Reconcile it explicitly before continuing; do not '
                'assume it is a complete draft or retry the same filename.'
            ),
        }
        super().__init__(self.receipt['reason'])


def create_document(root, template_id, filename):
    binding_path, binding_bytes, data = read_binding(root)
    if data['project'].get('mode') != 'PROJECT':
        raise ValueError('Initialize the project before creating an on-demand document')
    project_name = data['project'].get('name')
    if not isinstance(project_name, str) or not project_name:
        raise ValueError('Active project binding has no project name')
    allowed_chars = lambda value: value.isalnum() or value in ' ._-'
    if (not filename or filename in {'.', '..'} or filename.startswith('.') or len(filename) > MAX_NAME_LENGTH
            or filename.strip() != filename or '/' in filename or chr(92) in filename
            or chr(0) in filename or not all(allowed_chars(c) for c in filename)):
        raise ValueError('Use one filename (letters, numbers, spaces, dots, dashes or underscores; max 120)')
    final_name = filename if filename.casefold().endswith('.md') else filename + '.md'
    selected = next((spec for spec in document_template_plan(root, data) if spec['id'] == template_id), None)
    if selected is None:
        raise ValueError('Template ID is not registered in the active binding')
    source = bounded_path(root, selected['template'])
    target_directory = bounded_path(root, selected['target_directory'])
    target = bounded_path(root, (PurePosixPath(selected['target_directory']) / final_name).as_posix())
    if not source.is_file():
        raise ValueError('Registered template is missing')
    if target_directory.exists() and not target_directory.is_dir():
        raise ValueError('Registered destination is not a directory')
    if target.exists():
        raise ValueError('Target exists; existing content is preserved')
    rendered = rebase_links(
        source.read_text(encoding='utf-8').replace('{{PROJECT_NAME}}', project_name),
        source, target, root,
    )
    if binding_path.read_bytes() != binding_bytes:
        raise ValueError('Active binding changed during preflight; no document written')
    target.parent.mkdir(parents=True, exist_ok=True)
    output = target.open('x', encoding='utf-8')
    try:
        with output:
            output.write(rendered)
        saved = target.read_bytes()
        binding_unchanged = binding_path.read_bytes() == binding_bytes
        template_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    except _CAPTURED_FAILURES as exc:
        raise PartialDocumentCreationError(target.relative_to(root).as_posix(), exc) from exc
    return {
        'status': 'DRAFT_CREATED' if binding_unchanged else 'DRAFT_CREATED_BINDING_CHANGED_REVIEW',
        'template_id': template_id,
        'path': target.relative_to(root).as_posix(),
        'template_sha256': template_hash,
        'document_sha256': hashlib.sha256(saved).hexdigest(),
        'active_binding_unchanged': binding_unchanged,
        'project_readiness': data['project'].get('readiness', 'NOT_DECLARED'),
        'product_execution': 'NOT_RUN',
    }

def main():
    root = package_root()
    try:
        _, _, data = read_binding(root)
        choices = sorted(spec['id'] for spec in document_template_plan(root, data))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'REFUSED', 'reason': str(exc), 'created': False}, ensure_ascii=False))
        return 2
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template', choices=choices, required=True)
    parser.add_argument('--filename', required=True, help='One new Markdown filename; existing targets are never replaced')
    args = parser.parse_args()
    try:
        result = create_document(root, args.template, args.filename)
    except PartialDocumentCreationError as exc:
        print(json.dumps(exc.receipt, ensure_ascii=False))
        return 2
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'REFUSED', 'reason': str(exc), 'created': False}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
