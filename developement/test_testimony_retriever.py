#!/usr/bin/env python3
"""
Tests for the shipped Grok Build testimony skill retriever.

Drives the real entry point under .grok/skills/testimony/testimony_retriever.py
(not a reimplementation). Run from repo root:

  python3 -m unittest developement.test_testimony_retriever -v
"""
from __future__ import annotations

import importlib.util
import os
import re
import subprocess
import sys
import tempfile
import unittest

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROK_RETRIEVER = os.path.join(
    WORKSPACE_DIR, ".grok", "skills", "testimony", "testimony_retriever.py"
)
GROK_SKILL_MD = os.path.join(
    WORKSPACE_DIR, ".grok", "skills", "testimony", "SKILL.md"
)
GROK_COMMAND = os.path.join(WORKSPACE_DIR, ".grok", "commands", "testimony.md")
GROK_DATA = os.path.join(
    WORKSPACE_DIR, ".grok", "skills", "testimony", "data", "testimonies.json"
)
BIBLEMATE_ORCH = os.path.join(
    WORKSPACE_DIR, ".grok", "skills", "biblemate", "biblemate_orchestrator.py"
)
BIBLEMATE_SUPER_ORCH = os.path.join(
    WORKSPACE_DIR,
    ".grok",
    "skills",
    "biblemate-super",
    "biblemate_super_orchestrator.py",
)


def _load_retriever_module():
    """Import the shipped Grok retriever as a module for unit-level checks."""
    spec = importlib.util.spec_from_file_location(
        "grok_testimony_retriever", GROK_RETRIEVER
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


class TestTestimonyArtifacts(unittest.TestCase):
    def test_skill_and_command_exist(self):
        self.assertTrue(os.path.isfile(GROK_SKILL_MD), "Grok testimony SKILL.md missing")
        self.assertTrue(os.path.isfile(GROK_COMMAND), "Grok /testimony command missing")
        self.assertTrue(os.path.isfile(GROK_RETRIEVER), "Grok testimony retriever missing")
        self.assertTrue(os.path.isfile(GROK_DATA), "Grok testimonies.json missing")

    def test_skill_requires_real_sources_and_grok_paths(self):
        with open(GROK_SKILL_MD, "r", encoding="utf-8") as f:
            text = f.read()
        self.assertIn(".grok/skills/testimony/testimony_retriever.py", text)
        self.assertIn(".grok/skills/bible/bible_retriever.py", text)
        self.assertNotIn(".claude/skills/testimony", text)
        self.assertNotIn(".agents/skills/testimony", text)
        lower = text.lower()
        self.assertIn("never fabricate", lower)
        self.assertIn("real", lower)
        self.assertTrue(
            "web_search" in text or "web_fetch" in text or "open_page" in text,
            "Grok skill should reference Grok web tools",
        )
        self.assertNotIn("`search_web`", text)
        self.assertNotIn("`read_url_content`", text)
        self.assertIn("biblemate/", text)
        self.assertIn("testimony_", text)

    def test_command_persona_and_real_rule(self):
        with open(GROK_COMMAND, "r", encoding="utf-8") as f:
            text = f.read()
        self.assertIn(".grok/agents.md", text)
        self.assertIn("Passionate Evangelist", text)
        self.assertIn("never fake or fabricated", text.lower())
        self.assertIn("fact-check", text.lower())


class TestTestimonyRetrieverCLI(unittest.TestCase):
    def test_match_george_muller_writes_biblemate_file(self):
        """Drive the real CLI; assert structured output and matching save file."""
        before = set(
            f
            for f in os.listdir(os.path.join(WORKSPACE_DIR, "biblemate"))
            if f.endswith(".md") and "_testimony_" in f
        ) if os.path.isdir(os.path.join(WORKSPACE_DIR, "biblemate")) else set()

        proc = subprocess.run(
            [sys.executable, GROK_RETRIEVER, "George Muller"],
            cwd=WORKSPACE_DIR,
            capture_output=True,
            text=True,
            timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = proc.stdout
        self.assertIn("Real Testimony:", out)
        self.assertRegex(out, r"M[uü]ller|Muller", re.I)
        self.assertIn("## The Testimony Story", out)
        self.assertIn("## Historical Context & Biography", out)
        self.assertIn("## Verification & Sources", out)
        self.assertIn("Study output saved to: biblemate/", out)

        save_line = [
            line for line in out.splitlines() if line.startswith("Study output saved to:")
        ]
        self.assertTrue(save_line, "missing save path line")
        rel = save_line[0].split("Study output saved to:", 1)[1].strip()
        abs_path = os.path.join(WORKSPACE_DIR, rel)
        self.assertTrue(os.path.isfile(abs_path), f"expected file {abs_path}")
        with open(abs_path, "r", encoding="utf-8") as f:
            body = f.read()
        # File body must match the narrative printed to stdout (minus footer)
        narrative = out.split("\n---\n")[0].rstrip()
        self.assertEqual(body.rstrip(), narrative)
        self.assertIn("_testimony_", os.path.basename(abs_path))

        after = set(
            f
            for f in os.listdir(os.path.join(WORKSPACE_DIR, "biblemate"))
            if f.endswith(".md") and "_testimony_" in f
        )
        self.assertTrue(after - before or os.path.basename(abs_path) in after)

    def test_match_corrie_ten_boom(self):
        proc = subprocess.run(
            [sys.executable, GROK_RETRIEVER, "Corrie ten Boom"],
            cwd=WORKSPACE_DIR,
            capture_output=True,
            text=True,
            timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Corrie", proc.stdout)
        self.assertIn("## Verification & Sources", proc.stdout)
        self.assertIn("Study output saved to: biblemate/", proc.stdout)

    def test_no_match_does_not_fabricate(self):
        proc = subprocess.run(
            [sys.executable, GROK_RETRIEVER, "xyzzy_nonexistent_person_qwerty_999"],
            cwd=WORKSPACE_DIR,
            capture_output=True,
            text=True,
            timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("No direct matching testimony found", proc.stdout)
        self.assertIn("Do not fabricate a testimony", proc.stdout)
        self.assertNotIn("## The Testimony Story", proc.stdout)


class TestTestimonyRetrieverLogic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_retriever_module()

    def test_load_and_search_known_entry(self):
        testimonies = self.mod.load_testimonies(GROK_DATA)
        self.assertGreaterEqual(len(testimonies), 1)
        matches = self.mod.search_testimonies(testimonies, "forgiveness camp")
        self.assertTrue(matches, "expected at least one thematic match")
        md = self.mod.format_testimony_markdown(matches[0])
        self.assertIn("## Verification & Sources", md)
        self.assertIn("http", md.lower())

    def test_format_includes_required_sections(self):
        testimonies = self.mod.load_testimonies(GROK_DATA)
        md = self.mod.format_testimony_markdown(testimonies[0])
        for section in (
            "# Real Testimony:",
            "## The Testimony Story",
            "## Historical Context & Biography",
            "## Theological & Biblical Themes",
            "## Verification & Sources",
        ):
            self.assertIn(section, md)


class TestOrchestratorDiscoversTestimony(unittest.TestCase):
    def test_biblemate_list_skills_includes_testimony(self):
        proc = subprocess.run(
            [sys.executable, BIBLEMATE_ORCH, "--list-skills"],
            cwd=WORKSPACE_DIR,
            capture_output=True,
            text=True,
            timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertRegex(proc.stdout, r"(?m)^\- \*\*testimony\*\*:")

    def test_biblemate_super_list_skills_includes_testimony(self):
        proc = subprocess.run(
            [sys.executable, BIBLEMATE_SUPER_ORCH, "--list-skills"],
            cwd=WORKSPACE_DIR,
            capture_output=True,
            text=True,
            timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertRegex(proc.stdout, r"(?m)^\- \*\*testimony\*\*:")

    def test_minimum_coverage_includes_testimony(self):
        for path in (BIBLEMATE_ORCH, BIBLEMATE_SUPER_ORCH):
            with open(path, "r", encoding="utf-8") as f:
                src = f.read()
            self.assertIn('"testimony"', src)
            self.assertIn('"testimony": 1000', src)


if __name__ == "__main__":
    unittest.main()
