"""Core entry compatibility and the boundary with configurable on-demand records."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from workflow_support import document_template_plan, generation_plan


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


if __name__ == '__main__':
    unittest.main()
