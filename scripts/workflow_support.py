"""Read-only boundary and Markdown helpers for the isolated prototype."""
from pathlib import Path
import hashlib
import json
import os
import re
import sys
from urllib.parse import quote, unquote, urlsplit

# Stable bootstrap entry contract. Binding declarations must match these paths;
# project detail can be split behind the entries without moving the entries.
CORE_DOCUMENT_TARGETS = {
    'product': '項目文件/01-產品需求/產品骨架.md',
    'business': '項目文件/02-業務規格/業務模組/規格草稿.md',
    'technical': '項目文件/03-系統設計/系統設計草稿.md',
}
DOCUMENT_ROLES = set(CORE_DOCUMENT_TARGETS)
DOCUMENT_TEMPLATE_IDS = {'business-flow', 'decision', 'task', 'verification', 'delivery'}
LINK = re.compile(r'(?<!!)\[[^\]\n]+\]\((<[^>]+>|[^)\s]+)(?:\s+"[^"]*")?\)')

def digest(data):
    return hashlib.sha256(data).hexdigest()

def package_root():
    if sys.version_info < (3, 11):
        raise ValueError('Prototype requires Python 3.11 or later')
    here = Path(__file__).absolute()
    root = here.parent.parent
    if any(p.is_symlink() for p in (here, here.parent, root)):
        raise ValueError('Symlink package/script root is not supported')
    return root

def bounded_path(root, relative, origin=None):
    """Resolve local relative references without reading through symlinks."""
    root = root.absolute()
    value = unquote(relative.as_posix() if isinstance(relative, Path) else str(relative))
    if not value or Path(value).is_absolute() or '\\' in value:
        raise ValueError('Expected a nonempty portable relative path')
    current = (origin or root).absolute()
    if not current.is_relative_to(root) or root.is_symlink():
        raise ValueError('Origin/root is outside the declared package boundary')
    for part in Path(value).parts:
        if part == '.':
            continue
        current = current.parent if part == '..' else current / part
        if not current.is_relative_to(root):
            raise ValueError('Path escapes the declared package root')
        if current.is_symlink():
            raise ValueError('Symlink path requires explicit owner review')
    return current

def read_binding(root):
    path = bounded_path(root, '.workflow/project.json')
    instance = bounded_path(root, '.workflow/instance.json')
    if instance.exists():
        path = instance
    raw = path.read_bytes()
    data = json.loads(raw)
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise ValueError('Unknown binding schema')
    generation_plan(root, data)
    if not isinstance(data.get('project'), dict) or data['project'].get('mode') not in ('TEMPLATE', 'PROJECT'):
        raise ValueError('Unknown project mode')
    if not isinstance(data.get('commands'), dict):
        raise ValueError('Invalid command binding')
    return path, raw, data

def generation_plan(root, data):
    """Validate template sources and the fixed core-entry contract before any write."""
    specs = data.get('generated_documents')
    if not isinstance(specs, list) or len(specs) != 3:
        raise ValueError('Invalid generated document contract')
    roles, targets = set(), set()
    for spec in specs:
        if not isinstance(spec, dict) or spec.get('role') not in DOCUMENT_ROLES:
            raise ValueError('Unknown document role')
        role = spec['role']
        if role in roles:
            raise ValueError('Duplicate document role')
        roles.add(role)
        if spec.get('target') != CORE_DOCUMENT_TARGETS[role]:
            raise ValueError('Core document target is fixed for ' + role + ': '
                             + CORE_DOCUMENT_TARGETS[role]
                             + '. Preserve existing content; reconcile the entry explicitly.')
        source = bounded_path(root, spec.get('template', ''))
        target = bounded_path(root, spec.get('target', ''))
        if not source.is_relative_to(root/'文件模板') or source.suffix != '.md':
            raise ValueError('Template source is outside the declared template family')
        if not target.is_relative_to(root/'項目文件') or target.suffix != '.md' or target.is_relative_to(root/'項目文件/00-協作與執行'):
            raise ValueError('Generated target is outside product-document scope')
        if target in targets:
            raise ValueError('Duplicate generated target')
        targets.add(target)
    return specs

def document_template_plan(root, data):
    """Validate optional project documents and their owner destinations."""
    specs = data.get('document_templates')
    if not isinstance(specs, list) or len(specs) != len(DOCUMENT_TEMPLATE_IDS):
        raise ValueError('Invalid on-demand document template contract')
    seen_ids, seen_sources = set(), set()
    for spec in specs:
        if not isinstance(spec, dict) or spec.get('id') not in DOCUMENT_TEMPLATE_IDS:
            raise ValueError('Unknown document template ID')
        if spec['id'] in seen_ids:
            raise ValueError('Duplicate document template ID')
        seen_ids.add(spec['id'])
        source = bounded_path(root, spec.get('template', ''))
        target_dir = bounded_path(root, spec.get('target_directory', ''))
        if not source.is_relative_to(root/'文件模板') or source.suffix != '.md' or source in seen_sources:
            raise ValueError('Template source is outside the declared template family or is duplicated')
        if not target_dir.is_relative_to(root/'項目文件') or target_dir == root/'項目文件' or target_dir.is_relative_to(root/'項目文件/00-協作與執行'):
            raise ValueError('On-demand documents must be created under product-document owners')
        seen_sources.add(source)
    if seen_ids != DOCUMENT_TEMPLATE_IDS:
        raise ValueError('Incomplete on-demand document template registry')
    return specs

def without_fences(markdown):
    result = []
    fence = None
    for line in markdown.splitlines(keepends=True):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            char = marker[1][0]
            if fence is None:
                fence = char
            elif fence == char:
                fence = None
            result.append('\n')
        elif fence is None:
            result.append(line)
        else:
            result.append('\n')
    return ''.join(result)

def local_links(markdown):
    for match in LINK.finditer(without_fences(markdown)):
        value = match[1].strip('<>')
        split = urlsplit(value)
        if split.scheme or split.netloc or not split.path:
            continue
        yield value, split.path

def rebase_links(markdown, source, destination, root):
    """Only rebase real local links; examples in fenced code stay untouched."""
    def replace(match):
        original = match[1]
        split = urlsplit(original.strip('<>'))
        if split.scheme or split.netloc or not split.path:
            return match[0]
        target = bounded_path(root, split.path, source.parent)
        if not target.exists():
            raise ValueError('Template has an unresolved local link: ' + original)
        rel = quote(Path(os.path.relpath(target, destination.parent)).as_posix(), safe='/-._~')
        new = rel + ('?' + split.query if split.query else '') + ('#' + split.fragment if split.fragment else '')
        if original.startswith('<'):
            new = '<' + new + '>'
        return match[0].replace(original, new, 1)
    result, fence = [], None
    for line in markdown.splitlines(keepends=True):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            char = marker[1][0]
            if fence is None:
                fence = char
            elif fence == char:
                fence = None
            result.append(line)
        else:
            result.append(line if fence else LINK.sub(replace, line))
    return ''.join(result)
