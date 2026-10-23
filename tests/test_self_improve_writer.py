#!/usr/bin/env python3
"""Learning publisher must replay only generated state and check shell syntax."""
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/self-improve.yml"


class LearningWriterTests(unittest.TestCase):
    def test_collision_rebuild_is_shell_valid_and_fail_closed(self):
        raw = WORKFLOW.read_text(encoding="utf-8")
        block = raw.split("      - name: Commit self-rewrite outputs\n", 1)[1]
        block = block.split("        run: |\n", 1)[1]
        block = block.split("      - name: Fail if the self-improvement run lost\n", 1)[0]
        lines = [s[10:] if s.startswith("          ") else s
                 for s in block.splitlines()]
        script = "\n".join(lines) + "\n"
        proc = subprocess.run(["bash", "-n"], input=script, text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn('git diff --name-only "$GITHUB_SHA" origin/main', script)
        self.assertIn("Refusing to rebuild learning over unreviewed code or canonical authority changes", script)
        self.assertIn("git reset --hard origin/main", script)
        self.assertIn("python scripts/check_authority_spine.py", script)
        self.assertIn("python scripts/foundation_state.py check", script)
        self.assertIn("python workers/self_improve.py", script)
        self.assertIn("python workers/learning_intake.py", script)
        self.assertIn("python scripts/friday_control_plane.py build", script)
        self.assertIn("friday_operator_outcomes", script)
        self.assertNotIn("state/CURRENT_PROJECT.json|", script)
        self.assertNotIn("workers/self_improve.py|", script)
        self.assertIn("if: always() && github.event_name != 'pull_request'", raw)


if __name__ == "__main__":
    unittest.main()
