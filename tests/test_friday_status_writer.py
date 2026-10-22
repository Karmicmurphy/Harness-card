#!/usr/bin/env python3
"""Generated status publishing must be syntactically valid and fail closed on unsafe drift."""
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/friday-control-plane.yml"


class WriterContractTests(unittest.TestCase):
    def test_replay_script_is_valid_bash_and_scoped_to_generated_state(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("      - name: Commit refreshed owner view on main only", workflow)
        tail = workflow.split("      - name: Commit refreshed owner view on main only", 1)[1]
        block = tail.split("        run: |\n", 1)[1]
        # The publisher is the workflow's final step; shell indentation is ten spaces.
        lines = [line[10:] if line.startswith("          ") else line for line in block.splitlines()]
        script = "\n".join(lines) + "\n"
        result = subprocess.run(["bash", "-n"], input=script, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('git diff --name-only "$GITHUB_SHA" origin/main', script)
        self.assertIn('git reset --hard origin/main', script)
        self.assertIn('python scripts/check_authority_spine.py', script)
        self.assertIn('python scripts/foundation_state.py observe', script)
        self.assertIn('python scripts/friday_operator.py', script)
        self.assertIn('Refusing to replay FRIDAY output onto unreviewed source/authority changes', script)
        # Refuse to rebase any unknown new source, work order or permission settings.
        self.assertNotIn('state/CURRENT_PROJECT.json|', script)
        self.assertNotIn('scripts/friday_operator.py|', script)


if __name__ == "__main__":
    unittest.main()
