"""Hub nav includes Local models + Free model APIs tabs."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from generate_research_hub import (  # noqa: E402
    page_shell,
    render_free_apis,
    render_index,
    render_local_models,
    render_week_report,
)
from model_catalogs import FREE_APIS, LOCAL_MODELS, LOCAL_RUNTIMES  # noqa: E402


class TestHubNav(unittest.TestCase):
    def test_root_nav_has_catalog_tabs(self):
        html = page_shell("Weekly Research Hub", "home", "<p>x</p>", ["2026-10-02"])
        self.assertIn('href="local-models.html"', html)
        self.assertIn('href="free-apis.html"', html)
        self.assertIn(">Local models</a>", html)
        self.assertIn(">Free model APIs</a>", html)
        self.assertIn('href="reports/2026-10-02.html"', html)

    def test_nested_report_nav_uses_parent_prefix(self):
        html = page_shell("Week of 2026-10-02", "2026-10-02", "<p>x</p>", ["2026-10-02"], nested=True)
        self.assertIn('href="../local-models.html"', html)
        self.assertIn('href="../free-apis.html"', html)
        self.assertIn('href="../index.html"', html)
        self.assertIn('href="../radar.html"', html)
        self.assertIn('href="../reports/2026-10-02.html"', html)
        self.assertNotIn('href="local-models.html"', html)

    def test_index_cards_link_catalogs(self):
        html = render_index(["2026-10-02"], "2026-10-02")
        self.assertIn('href="local-models.html"', html)
        self.assertIn('href="free-apis.html"', html)

    def test_week_report_is_nested(self):
        html = render_week_report("2026-10-02", "# Scan\n", None, ["2026-10-02"])
        self.assertIn('href="../local-models.html"', html)


class TestCatalogPages(unittest.TestCase):
    def test_local_models_page_links(self):
        html = render_local_models([])
        self.assertIn("class=\"active\">Local models</a>", html)
        self.assertIn("https://github.com/ggml-org/llama.cpp", html)
        self.assertIn("https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive", html)
        self.assertIn("https://ollama.com/library/llama3.2", html)
        for item in LOCAL_RUNTIMES + LOCAL_MODELS:
            self.assertIn(item["url"], html, msg=item["name"])
            self.assertIn(item["description"][:40], html)

    def test_free_apis_page_links(self):
        html = render_free_apis([])
        self.assertIn("class=\"active\">Free model APIs</a>", html)
        self.assertIn("https://console.groq.com/docs/models", html)
        self.assertIn("https://openrouter.ai/thinkingmachines/inkling:free", html)
        self.assertIn("Adopt none of these as org-default", html)
        for item in FREE_APIS:
            self.assertIn(item["url"], html, msg=item["name"])


class TestHubGenerateWritesTabs(unittest.TestCase):
    def test_main_writes_catalog_html(self):
        from generate_research_hub import DASHBOARD_SRC, main

        if not DASHBOARD_SRC.exists():
            self.skipTest("radar dashboard missing")
        with tempfile.TemporaryDirectory() as tmp:
            research = Path(tmp) / "research"
            research.mkdir()
            (research / "GITHUB_RISING_RADAR_2026_10_02.md").write_text("# Scan\n")
            out = Path(tmp) / "docs"
            old_argv = sys.argv
            sys.argv = [
                "generate_research_hub.py",
                "--research-dir",
                str(research),
                "--output-dir",
                str(out),
            ]
            try:
                main()
            finally:
                sys.argv = old_argv
            self.assertTrue((out / "local-models.html").is_file())
            self.assertTrue((out / "free-apis.html").is_file())
            home = (out / "index.html").read_text()
            self.assertIn("Local models", home)
            self.assertIn("Free model APIs", home)


if __name__ == "__main__":
    unittest.main()
