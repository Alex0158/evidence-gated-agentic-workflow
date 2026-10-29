"""Static scaffold/link/entry checks, never product execution or approval."""
import argparse
import json
import re
from urllib.parse import unquote, urlsplit
from workflow_support import LINK, bounded_path, document_template_plan, generation_plan, local_links, package_root, read_binding, without_fences

REQUIRED = (
    'AGENTS.md', 'README.md', '項目文件/README.md',
    '項目文件/00-協作與執行/README.md',
    '項目文件/00-協作與執行/項目工程入口.md',
    '項目文件/00-協作與執行/規則與標準/工作規則與標準.md',
    '項目文件/00-協作與執行/Runbooks/啟動項目.md',
    '項目文件/00-協作與執行/Runbooks/任務登記與分流.md',
    '項目文件/00-協作與執行/Runbooks/調查與分析.md',
    '項目文件/00-協作與執行/Runbooks/開發與變更.md',
    '項目文件/00-協作與執行/Runbooks/修復缺陷.md',
    '項目文件/00-協作與執行/Runbooks/規格驅動開發.md',
    '項目文件/00-協作與執行/Runbooks/測試驅動開發.md',
    '項目文件/00-協作與執行/Runbooks/驗證功能.md',
    '項目文件/00-協作與執行/Runbooks/版本交付.md',
    '文件模板/產品骨架範本.md', '文件模板/模組與功能規格範本.md',
    '文件模板/業務流程範本.md', '文件模板/技術設計與契約範本.md',
    '文件模板/決策範本.md', '文件模板/工作任務範本.md',
    '文件模板/驗證紀錄範本.md', '文件模板/交付紀錄範本.md',
    'scripts/init_project.py', 'scripts/create_document.py', 'scripts/check_docs.py', 'scripts/workflow_support.py',
)

def _anchor_slug(value):
    value = unquote(value).strip().lower()
    value = ''.join(char for char in value if char.isalnum() or char in ' -')
    value = re.sub(r'\s+', '-', value)
    return re.sub(r'-+', '-', value).strip('-')


def _heading_slugs(path):
    text = without_fences(path.read_text(encoding='utf-8'))
    slugs, occurrences = set(), {}
    for match in re.finditer(r'^\s*#{1,6}\s+(.+?)\s*$', text, re.MULTILINE):
        base = _anchor_slug(match.group(1).strip().rstrip('#').strip())
        if not base:
            continue
        suffix = occurrences.get(base, 0)
        slugs.add(base if suffix == 0 else f'{base}-{suffix}')
        occurrences[base] = suffix + 1
    for anchor in re.findall(r'<(?:a|span)\b[^>]*\b(?:name|id)=["\']([^"\']+)["\']', text, re.IGNORECASE):
        slugs.add(anchor)
        slugs.add(_anchor_slug(anchor))
    return slugs


def _check_project_links(root, path, generated, template):
    errors, deferred, checked, anchors_checked = [], [], 0, 0
    text = path.read_text(encoding='utf-8')
    for match in LINK.finditer(without_fences(text)):
        original = match.group(1).strip('<>')
        split = urlsplit(original)
        if split.scheme or split.netloc:
            continue
        checked += 1
        target = path if not split.path else bounded_path(root, unquote(split.path), path.parent)
        if not target.exists():
            target_rel = target.relative_to(root).as_posix()
            if template and target_rel in generated:
                deferred.append(target_rel)
            else:
                errors.append(path.relative_to(root).as_posix() + ': unresolved ' + original)
            continue
        if split.fragment:
            anchors_checked += 1
            if _anchor_slug(split.fragment) not in _heading_slugs(target):
                errors.append(path.relative_to(root).as_posix() + ': unresolved anchor ' + original)
    return errors, deferred, checked, anchors_checked


def check(root, project_docs=False):
    errors, deferred, commands = [], [], {}
    try:
        _, _, config = read_binding(root)
        optional_templates = document_template_plan(root, config)
    except (OSError, ValueError, KeyError) as exc:
        return {'status': 'FAIL', 'errors': ['Binding: ' + str(exc)], 'product_execution': 'NOT_RUN'}
    template = config['project']['mode'] == 'TEMPLATE'
    generated = tuple(spec['target'] for spec in generation_plan(root, config))
    for relative in REQUIRED + (() if template else generated):
        try:
            p = bounded_path(root, relative)
            if not p.is_file():
                errors.append('Missing artifact: ' + relative)
        except ValueError as exc:
            errors.append(relative + ': ' + str(exc))
    links_checked = 0
    files = [root / p for p in REQUIRED if p.endswith('.md')]
    files += [root / p for p in generated if (root / p).is_file()]
    if project_docs:
        files += sorted((root / '項目文件').rglob('*.md'))
    files = list(dict.fromkeys(files))
    anchors_checked = project_docs
    for path in files:
        try:
            path = bounded_path(root, path.relative_to(root))
            if not path.is_file():
                continue
            text = path.read_text(encoding='utf-8')
            if path.relative_to(root).as_posix() in generated and '{{PROJECT_NAME}}' in text:
                errors.append('Unfilled project-name token: ' + path.relative_to(root).as_posix())
            if project_docs:
                link_errors, link_deferred, checked, checked_anchors = _check_project_links(root, path, generated, template)
                errors.extend(link_errors)
                deferred.extend(link_deferred)
                links_checked += checked
                anchors_checked = True if checked_anchors or anchors_checked else anchors_checked
            else:
                for original, relative in local_links(text):
                    links_checked += 1
                    target = bounded_path(root, relative, path.parent)
                    if not target.exists():
                        target_rel = target.relative_to(root).as_posix()
                        if template and target_rel in generated:
                            deferred.append(target_rel)
                        else:
                            errors.append(path.relative_to(root).as_posix() + ': unresolved ' + original)
        except (OSError, ValueError) as exc:
            errors.append(str(path.relative_to(root)) + ': ' + str(exc))
    for name, spec in config['commands'].items():
        if spec is None:
            commands[name] = 'NO_RUNNER'
            continue
        try:
            if not isinstance(spec, dict) or not isinstance(spec.get('argv'), list) or not spec['argv']:
                raise ValueError('Invalid argv/entry binding')
            entry = bounded_path(root, spec['entry'])
            if not entry.is_file():
                raise ValueError('Native entry is absent')
            commands[name] = 'ENTRY_EXISTS_NOT_EXECUTED'
        except (ValueError, KeyError, TypeError) as exc:
            errors.append('Command ' + name + ': ' + str(exc))
    return {
        'status': 'PASS' if not errors else 'FAIL', 'claim': 'FRAMEWORK_STATIC_CHECKED',
        'project_mode': config['project']['mode'], 'product_readiness': config['project'].get('readiness', 'NOT_DECLARED'),
        'errors': errors, 'deferred_generated_paths': sorted(set(deferred)),
        'local_file_links_checked': links_checked, 'anchors_checked': anchors_checked, 'external_links_fetched': False,
        'project_docs_scope': '項目文件/**/*.md' if project_docs else 'required_and_generated_only',
        'commands': commands, 'requirements_approved': 'NOT_DETERMINED',
        'on_demand_template_ids': sorted(spec['id'] for spec in optional_templates),
        'on_demand_documents_created': False,
        'product_execution': 'NOT_RUN', 'runtime_proven': False,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-docs', action='store_true', help='check all Markdown under 項目文件, including local anchors')
    args = parser.parse_args()
    result = check(package_root(), project_docs=args.project_docs)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'PASS' else 1

if __name__ == '__main__':
    raise SystemExit(main())
