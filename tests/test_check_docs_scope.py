from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_docs  # noqa: E402


class AnchorCompatibilityTests(unittest.TestCase):
    def test_duplicate_headings_get_renderer_style_suffixes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.md"
            path.write_text(
                "```md\n## Hidden\n```\n"
                "## Booking\n## Booking\n"
                "## This'll be a _Helpful_ Section About the Greek Letter Θ!\n"
                "## 需求、範圍\n",
                encoding="utf-8",
            )
            slugs = check_docs._heading_slugs(path)
        self.assertIn("booking", slugs)
        self.assertIn("booking-1", slugs)
        self.assertNotIn("hidden", slugs)
        self.assertIn("thisll-be-a-helpful-section-about-the-greek-letter-θ", slugs)
        self.assertIn("需求範圍", slugs)

    def test_explicit_html_anchor_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "explicit.md"
            path.write_text('<a name="stable-anchor"></a>\n', encoding="utf-8")
            slugs = check_docs._heading_slugs(path)
        self.assertIn("stable-anchor", slugs)


class ProjectScopeLinkTests(unittest.TestCase):
    def test_project_scope_checks_local_file_and_duplicate_anchors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "項目文件" / "source.md"
            target = root / "項目文件" / "target.md"
            source.parent.mkdir(parents=True)
            target.write_text("## Service\n## Service\n", encoding="utf-8")
            source.write_text(
                "[first](target.md#service) [second](target.md#service-1) [bad](target.md#missing)\n",
                encoding="utf-8",
            )
            errors, deferred, checked, anchors = check_docs._check_project_links(
                root, source, (), False
            )
        self.assertEqual(deferred, [])
        self.assertEqual(checked, 3)
        self.assertEqual(anchors, 3)
        self.assertEqual(len(errors), 1)
        self.assertIn("#missing", errors[0])


if __name__ == "__main__":
    unittest.main()
