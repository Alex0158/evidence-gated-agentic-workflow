"""Core entry compatibility and the boundary with configurable on-demand records."""
import copy
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from create_document import main as create_document_main
from workflow_support import document_template_plan, generation_plan


class PartialWriteFile:
    """Persist a prefix to a real file, then fail the write operation."""

    def __init__(self, wrapped, prefix_length=10):
        self.wrapped = wrapped
        self.prefix_length = prefix_length

    def __enter__(self):
        self.wrapped.__enter__()
        return self

    def __exit__(self, exc_type, exc, traceback):
        return self.wrapped.__exit__(exc_type, exc, traceback)

    def __getattr__(self, name):
        return getattr(self.wrapped, name)

    def write(self, value):
        self.wrapped.write(value[:self.prefix_length])
        self.wrapped.flush()
        raise OSError('synthetic write failure after persisted bytes')


class CoreDocumentPathTests(unittest.TestCase):
    def setUp(self):
        self.binding = json.loads((ROOT / '.workflow/project.json').read_text(encoding='utf-8'))

    def test_default_entries_accept_declaration_reordering(self):
        expected = copy.deepcopy(self.binding['generated_documents'])
        self.binding['generated_documents'].reverse()
        actual = generation_plan(ROOT, self.binding)
        self.assertEqual({s['role']: s['target'] for s in actual},
                         {s['role']: s['target'] for s in expected})

    def test_each_core_entry_rejects_renaming(self):
        for index in range(len(self.binding['generated_documents'])):
            with self.subTest(role=self.binding['generated_documents'][index]['role']):
                changed = copy.deepcopy(self.binding)
                spec = changed['generated_documents'][index]
                spec['target'] = str(Path(spec['target']).with_name('different-entry.md'))
                with self.assertRaisesRegex(ValueError, 'Core document target is fixed'):
                    generation_plan(ROOT, changed)

    def test_core_paths_cannot_be_swapped_between_roles(self):
        specs = self.binding['generated_documents']
        specs[0]['target'], specs[1]['target'] = specs[1]['target'], specs[0]['target']
        with self.assertRaisesRegex(ValueError, 'Core document target is fixed'):
            generation_plan(ROOT, self.binding)

    def test_core_entry_requires_its_canonical_spelling(self):
        spec = self.binding['generated_documents'][0]
        parent, name = spec['target'].rsplit('/', 1)
        spec['target'] = parent + '/./' + name
        with self.assertRaisesRegex(ValueError, 'Core document target is fixed'):
            generation_plan(ROOT, self.binding)

    def test_optional_record_destination_remains_configurable(self):
        task = next(s for s in self.binding['document_templates'] if s['id'] == 'task')
        task['target_directory'] = '項目文件/05-工作與交付紀錄/任務'
        generation_plan(ROOT, self.binding)
        actual = document_template_plan(ROOT, self.binding)
        self.assertEqual(next(s for s in actual if s['id'] == 'task')['target_directory'],
                         task['target_directory'])

    def make_synthetic_project(self):
        root = Path(tempfile.mkdtemp(prefix='document-receipt-regression-'))
        (root / '.workflow').mkdir()
        (root / '文件模板').mkdir()
        binding = copy.deepcopy(self.binding)
        binding['project'].update({'mode': 'PROJECT', 'name': 'Synthetic Receipt Project'})
        (root / '.workflow/project.json').write_text(
            json.dumps(binding, ensure_ascii=False), encoding='utf-8'
        )
        template = next(spec['template'] for spec in binding['document_templates']
                        if spec['id'] == 'task')
        (root / template).write_text(
            '# {{PROJECT_NAME}}\n\nSynthetic receipt regression payload.\n',
            encoding='utf-8',
        )
        target = root / '項目文件/05-工作與交付紀錄/Receipt regression.md'
        return root, target

    def run_create_document(self, root, target, *, open_fault=None, read_fault=None):
        output = io.StringIO()
        argv = ['create_document.py', '--template', 'task', '--filename', 'Receipt regression']
        patches = [
            patch('create_document.package_root', return_value=root),
            patch.object(sys, 'argv', argv),
        ]
        if open_fault is not None:
            patches.append(patch.object(Path, 'open', open_fault))
        if read_fault is not None:
            patches.append(patch.object(Path, 'read_bytes', read_fault))
        with contextlib.ExitStack() as stack:
            for active_patch in patches:
                stack.enter_context(active_patch)
            stack.enter_context(contextlib.redirect_stdout(output))
            exit_code = create_document_main()
        return exit_code, json.loads(output.getvalue())

    def test_post_open_write_failure_reports_retained_partial_file(self):
        root, target = self.make_synthetic_project()
        real_open = Path.open

        def fail_after_persisting_prefix(path, mode='r', *args, **kwargs):
            if path == target and mode == 'x':
                return PartialWriteFile(real_open(path, mode, *args, **kwargs))
            return real_open(path, mode, *args, **kwargs)

        exit_code, receipt = self.run_create_document(
            root, target, open_fault=fail_after_persisting_prefix
        )
        self.assertEqual(exit_code, 2)
        self.assertEqual(receipt['status'], 'PARTIAL_RETAINED')
        self.assertIs(receipt['created'], True)
        self.assertEqual(receipt['path'], '項目文件/05-工作與交付紀錄/Receipt regression.md')
        self.assertIn('synthetic write failure', receipt['reason'])
        self.assertIn('Inspect the retained file', receipt['recovery'])
        self.assertNotEqual(receipt['status'], 'DRAFT_CREATED')
        self.assertTrue(target.is_file())
        self.assertEqual(target.read_bytes(), b'# Syntheti')

    def test_readback_failure_reports_retained_complete_file_as_unverified(self):
        root, target = self.make_synthetic_project()
        real_read_bytes = Path.read_bytes

        def fail_target_readback(path):
            if path == target:
                raise OSError('synthetic readback failure')
            return real_read_bytes(path)

        exit_code, receipt = self.run_create_document(
            root, target, read_fault=fail_target_readback
        )
        expected = (
            '# Synthetic Receipt Project\n\nSynthetic receipt regression payload.\n'
        ).encode('utf-8')
        self.assertEqual(exit_code, 2)
        self.assertEqual(receipt['status'], 'PARTIAL_RETAINED')
        self.assertIs(receipt['created'], True)
        self.assertEqual(receipt['path'], '項目文件/05-工作與交付紀錄/Receipt regression.md')
        self.assertIn('synthetic readback failure', receipt['reason'])
        self.assertIn('Inspect the retained file', receipt['recovery'])
        self.assertNotEqual(receipt['status'], 'DRAFT_CREATED')
        self.assertTrue(target.is_file())
        self.assertEqual(target.read_bytes(), expected)

    def test_pre_open_existing_target_remains_refused_and_unchanged(self):
        root, target = self.make_synthetic_project()
        target.parent.mkdir(parents=True)
        original = b'existing user content\n'
        target.write_bytes(original)

        exit_code, receipt = self.run_create_document(root, target)

        self.assertEqual(exit_code, 2)
        self.assertEqual(receipt['status'], 'REFUSED')
        self.assertIs(receipt['created'], False)
        self.assertEqual(target.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
