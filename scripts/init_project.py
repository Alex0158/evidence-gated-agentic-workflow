"""Generate a draft project in this clone, without overwriting product content."""
import argparse
from datetime import datetime, timezone
import json
import os
import uuid
from workflow_support import bounded_path, digest, generation_plan, package_root, read_binding, rebase_links

def initialize(root, name):
    if not name or len(name) > 80 or not all(c.isalnum() or c in ' -_' for c in name):
        raise ValueError('Project name must be 1..80 letters/numbers/spaces/dashes/underscores')
    config_path, original, config = read_binding(root)
    project = config['project']
    if project.get('mode') != 'TEMPLATE' or project.get('name') is not None or project.get('id') is not None:
        raise ValueError('Already initialized/customized; existing project is preserved')
    if set(project) != {'name', 'id', 'mode', 'readiness'} or project.get('readiness') != 'NOT_DECLARED':
        raise ValueError('Customized project fields/readiness require owner adoption; nothing overwritten')
    if any(config['commands'].get(k) is not None for k in ('product_build', 'product_test', 'product_run')):
        raise ValueError('Product runner already bound; preserve existing configuration')
    plan = generation_plan(root, config)
    targets = [bounded_path(root, spec['target']) for spec in plan]
    receipt = bounded_path(root, '.workflow/init-receipt.json')
    backup = bounded_path(root, '.workflow/init-config-before.json')
    instance = bounded_path(root, '.workflow/instance.json')
    candidate = bounded_path(root, '.workflow/init-candidate-' + str(uuid.uuid4()) + '.json')
    for p in targets + [receipt, backup, instance, candidate]:
        if p.exists():
            raise ValueError('Existing target must be preserved: ' + str(p.relative_to(root)))
    for relative in ('項目文件/01-產品需求', '項目文件/02-業務規格', '項目文件/03-系統設計'):
        p = bounded_path(root, relative)
        if p.exists() and (not p.is_dir() or any(p.iterdir())):
            raise ValueError('Existing product content must be preserved: ' + relative)
    prepared = []
    for spec, target in zip(plan, targets):
        source = bounded_path(root, spec['template'])
        text = source.read_text(encoding='utf-8')
        text = text.replace('{{PROJECT_NAME}}', name)
        text = rebase_links(text, source, target, root)
        prepared.append((source, target, text))
    if config_path.read_bytes() != original:
        raise ValueError('Binding changed during preflight; nothing written')
    config['project'] = {'name': name, 'id': str(uuid.uuid4()), 'mode': 'PROJECT', 'readiness': 'NOT_DECLARED'}
    revised = (json.dumps(config, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    created = []
    planned_hashes = {str(target.relative_to(root)): digest(body.encode('utf-8')) for _, target, body in prepared}
    planned_hashes.update({str(backup.relative_to(root)): digest(original), str(candidate.relative_to(root)): digest(revised), str(instance.relative_to(root)): digest(revised)})
    # All product targets were preflighted before the first write. Exclusive opens refuse races.
    try:
        with backup.open('xb') as f:
            created.append(str(backup.relative_to(root)))
            f.write(original)
        for _, target, text in prepared:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('x', encoding='utf-8') as f:
                created.append(str(target.relative_to(root)))
                f.write(text)
        if config_path.read_bytes() != original:
            raise ValueError('Binding changed; retain generated drafts and reconcile manually')
        # Publish a complete instance with no-overwrite semantics. The base is never modified.
        with candidate.open('xb') as f:
            created.append(str(candidate.relative_to(root)))
            f.write(revised)
            f.flush()
            os.fsync(f.fileno())
        if config_path.read_bytes() != original:
            raise ValueError('Template binding changed; drafts retained, activation refused')
        os.link(candidate, instance)
        created.append(str(instance.relative_to(root)))
        result = {
            'status': 'DRAFT_INITIALIZED', 'project_name': name,
            'time_utc': datetime.now(timezone.utc).isoformat(),
            'binding_template_sha256': digest(original), 'binding_after_sha256': digest(revised),
            'active_binding': '.workflow/instance.json', 'template_binding_unchanged': config_path.read_bytes() == original,
            'created': created, 'requirements_approved': False, 'product_tests': 'NOT_RUN',
            'template_sources': {str(s.relative_to(root)): digest(s.read_bytes()) for s, _, _ in prepared},
            'generated_sha256': {str(t.relative_to(root)): digest(t.read_bytes()) for _, t, _ in prepared},
        }
        with receipt.open('x', encoding='utf-8') as f:
            created.append(str(receipt.relative_to(root)))
            json.dump(result, f, ensure_ascii=False, indent=2)
            f.write('\n')
        return result
    except Exception as exc:
        partial = bounded_path(root, '.workflow/init-partial-' + str(uuid.uuid4()) + '.json')
        with partial.open('x', encoding='utf-8') as f:
            json.dump({'status':'PARTIAL_RETAINED','created':created,'planned_sha256':planned_hashes,'cause':str(exc),'template_binding_unchanged':config_path.read_bytes()==original,'active_binding_published':instance.exists(),'recovery':'Compare retained files to planned hashes and base backup; adopt/reconcile explicitly in a fresh destination. No reset/cleanup/forced retry.'},f,ensure_ascii=False,indent=2)
            f.write('\n')
        raise ValueError('Partial initialization retained; no cleanup performed. Created=' + repr(created) + '; cause=' + str(exc)) from exc

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-name', required=True)
    args = parser.parse_args()
    try:
        result = initialize(package_root(), args.project_name)
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps({'status': 'REFUSED', 'reason': str(exc), 'cleanup': 'NONE'}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
