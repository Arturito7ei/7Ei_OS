"""[radar-desc] Description column is required in scan, hub, and dashboard tables."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from radar_columns import fmt_desc, insert_description_column, repo_key_from_cell  # noqa: E402
from scan import render_report  # noqa: E402


class TestFmtDesc(unittest.TestCase):
    def test_empty_is_em_dash(self):
        self.assertEqual(fmt_desc({}), "—")
        self.assertEqual(fmt_desc({"description": None}), "—")
        self.assertEqual(fmt_desc(None), "—")

    def test_pipe_and_newline_are_safe(self):
        self.assertEqual(fmt_desc({"description": "a|b\nc"}), "a/b c")

    def test_truncate_ends_with_ellipsis(self):
        out = fmt_desc({"description": "x" * 200}, limit=40)
        self.assertTrue(out.endswith("…"))
        self.assertEqual(len(out), 40)


class TestInsertDescriptionColumn(unittest.TestCase):
    def test_inserts_after_repo_before_why(self):
        rows = [
            ["Verdict", "Repo", "Why"],
            ["Trial", "[yetone/magpie](https://github.com/yetone/magpie)", "Local BYOK"],
        ]
        out = insert_description_column(rows, {"yetone/magpie": "Menu-bar + local gateway"})
        self.assertEqual(out[0], ["Verdict", "Repo", "Description", "Why"])
        self.assertEqual(out[1][2], "Menu-bar + local gateway")
        self.assertEqual(out[1][3], "Local BYOK")

    def test_leaves_existing_description_untouched(self):
        rows = [
            ["Verdict", "Repo", "Description", "Why"],
            ["Trial", "[acme/foo](https://github.com/acme/foo)", "Curated blurb", "Because"],
        ]
        out = insert_description_column(rows, {"acme/foo": "GitHub blurb"})
        self.assertEqual(out, rows)

    def test_repo_key_from_markdown_link(self):
        self.assertEqual(
            repo_key_from_cell("[yetone/magpie](https://github.com/yetone/magpie)"),
            "yetone/magpie",
        )


class TestRenderReport(unittest.TestCase):
    def test_scan_tables_include_description_after_repo(self):
        repos = [
            {
                "full_name": "acme/foo",
                "html_url": "https://github.com/acme/foo",
                "description": "Local gateway for agents",
                "stargazers_count": 100,
                "stars_per_day": 10.0,
                "age_days": 10.0,
                "language": "Go",
                "_track": "ai",
            }
        ]
        prev = {"acme/foo": {"stargazers_count": 50}}
        report = render_report(repos, prev, {"ai": {"label": "AI / LLM"}})
        self.assertIn("| Repo | Description | Δ stars |", report)
        self.assertIn("| Repo | Description | ⭐/day |", report)
        self.assertIn("Local gateway for agents", report)


if __name__ == "__main__":
    unittest.main()
