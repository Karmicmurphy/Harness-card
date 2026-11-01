"""The public Harness route must not consume or expose private THY continuity."""
import json
import unittest
import subprocess
import sys
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "thy-continuity-recovery" / "SKILL.md"

class THYContinuityRecoveryTests(unittest.TestCase):
    def test_registered_under_existing_harness_source(self):
        registry = json.loads((ROOT / "config" / "skill_registry.json").read_text(encoding="utf-8"))
        entry = registry["skills"]["thy-continuity-recovery"]
        self.assertEqual(entry, {
            "source": "harness_local",
            "path": "skills/thy-continuity-recovery/SKILL.md",
            "kind": "PROCEDURAL_CONDITIONAL",
        })
        self.assertEqual(registry["sources"]["harness_local"]["repo"], "Karmicmurphy/Harness-card")

    def test_creative_lane_stays_separate_and_no_fake_success(self):
        text = SKILL.read_text(encoding="utf-8")
        routing = (ROOT / "ROUTING.md").read_text(encoding="utf-8")
        for fragment in (
            "independent creative project", "private ChatGPT Library",
            "THY_Episode_001_The_Noise_Inside_FIRST_CUT_v2.mp4",
            "BLOCKED_BY_LIBRARY_ACCESS", "does not", "no",
        ):
            self.assertIn(fragment.lower(), text.lower())
        self.assertIn("THY Continuity Recovery", routing)
        self.assertIn("Do not", routing)

    def test_real_cli_resolves_conditional_pointer_without_invoking_media(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/resolve_skill.py"), "thy-continuity-recovery"],
            cwd=ROOT, capture_output=True, text=True, timeout=10, check=True,
        )
        pointer = json.loads(result.stdout)
        self.assertEqual(pointer["kind"], "PROCEDURAL_CONDITIONAL")
        self.assertEqual(pointer["repo"], "Karmicmurphy/Harness-card")
        self.assertEqual(pointer["path"], "skills/thy-continuity-recovery/SKILL.md")

    def test_guard_rejects_private_reference_in_companion_document_without_echo(self):
        document = ROOT / "docs/THY_CONTINUITY_RECOVERY_ROUTING_2026-10-26.md"
        read_text = Path.read_text
        synthetic = "libfile_" + "SYNTHETIC_ONLY"
        def injected(path, *args, **kwargs):
            text = read_text(path, *args, **kwargs)
            return text + "\n" + synthetic if path == document else text
        with patch.object(Path, "read_text", injected):
            result = unittest.TestResult()
            type(self)("test_public_skill_never_contains_private_data_or_media").run(result)
        self.assertEqual(len(result.failures), 1)
        self.assertNotIn(synthetic, result.failures[0][1])

    def assert_public_text_safe(self, text):
        text = text.lower()
        for prohibited in (
            "libfile_", "file_00000000", "cdn.creativeclaw.co",
            "rnoxon", "cheryl",
            "april 13", "10:54", "c50648c8-",
        ):
            self.assertFalse(prohibited in text, "private-reference pattern in public adapter")

    def test_public_skill_never_contains_private_data_or_media(self):
        for path in (
            SKILL,
            ROOT / "ROUTING.md",
            ROOT / "config/skill_registry.json",
            ROOT / "skills/SKILL_SOURCES.md",
            ROOT / "docs/THY_CONTINUITY_RECOVERY_ROUTING_2026-10-26.md",
        ):
            # Error messages deliberately omit scanned contents and matched data.
            with self.subTest(path=path.relative_to(ROOT)):
                self.assert_public_text_safe(path.read_text(encoding="utf-8"))
        for scheme in ("http://", "https://"):
            self.assertFalse(scheme in SKILL.read_text(encoding="utf-8").lower(),
                             "URL in public recovery skill")
        for p in ROOT.glob("skills/thy-continuity-recovery/**/*"):
            if p.is_file():
                self.assertNotIn(p.suffix.lower(), (".mp4", ".wav", ".mp3", ".png", ".jpg"))

if __name__ == "__main__":
    unittest.main()
