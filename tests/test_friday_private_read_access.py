#!/usr/bin/env python3
"""Ensure FRIDAY's private-repo reader is granted only to trusted CI steps.

GitHub's repository-scoped default GITHUB_TOKEN cannot monitor another private
repository. Repo-scoped secret is intentionally NOT used on pull_request jobs.
No token value is ever read by this test.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
FRIDAY = ROOT / ".github/workflows/friday-control-plane.yml"
LEARNER = ROOT / ".github/workflows/self-improve.yml"
TRUSTED = "GH_TOKEN: ${{ github.event_name != 'pull_request' && secrets.FOUNDATION_READ_TOKEN || github.token }}"
MAIN_ONLY = "GH_TOKEN: ${{ secrets.FOUNDATION_READ_TOKEN || github.token }}"


def step(code: str, name: str) -> str:
    prefix = "      - name: " + name + "\n"
    if prefix not in code:
        raise AssertionError("Missing workflow step: " + name)
    section = code.split(prefix, 1)[1]
    if "\n      - name: " in section:
        section = section.split("\n      - name: ", 1)[0]
    return section


class ScopedPrivateAccessTests(unittest.TestCase):
    def test_observe_and_compare_share_same_narrow_credential(self):
        data = FRIDAY.read_text()
        for name in ("Observe approved refs without promotion",
                     "FRIDAY chooses and executes one allowed machine-maintenance action"):
            with self.subTest(step=name):
                section = step(data, name)
                self.assertIn(TRUSTED, section)
                self.assertIn("env:", section)
        writer = step(data, "Commit refreshed owner view on main only")
        self.assertIn("if: github.event_name != 'pull_request'", writer)
        self.assertIn(MAIN_ONLY, writer)
        self.assertIn("python scripts/friday_operator.py", writer)
        self.assertIn("python scripts/foundation_state.py observe", writer)

    def test_learner_keeps_private_token_away_from_prs(self):
        data = LEARNER.read_text()
        self.assertIn(TRUSTED, step(data, "Refresh FRIDAY machine status from this learning pass"))
        writer = step(data, "Commit self-rewrite outputs")
        self.assertIn("github.event_name != 'pull_request'", writer)
        self.assertIn(MAIN_ONLY, writer)

    def test_tokens_only_use_named_read_secret_or_scoped_repo_fallback(self):
        combined = FRIDAY.read_text() + LEARNER.read_text()
        gh_lines = [s.strip() for s in combined.splitlines() if s.strip().startswith("GH_TOKEN:")]
        self.assertEqual(len(gh_lines), 5)
        self.assertTrue(all(v in (TRUSTED, MAIN_ONLY) for v in gh_lines))
        self.assertNotIn("secrets.GITHUB_PAT", combined)
        self.assertNotIn("GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}", combined)


if __name__ == "__main__":
    unittest.main()
