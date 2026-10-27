"""The public Harness route must not consume or expose private THY continuity."""
import json
import unittest
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

    def test_public_skill_never_contains_private_data_or_media(self):
        text = SKILL.read_text(encoding="utf-8").lower()
        for prohibited in (
            "libfile_", "file_00000000", "cdn.creativeclaw.co",
            "http://", "https://", "rnoxon", "cheryl",
            "april 13", "10:54", "c50648c8-",
        ):
            self.assertNotIn(prohibited, text)
        for p in ROOT.glob("skills/thy-continuity-recovery/**/*"):
            if p.is_file():
                self.assertNotIn(p.suffix.lower(), (".mp4", ".wav", ".mp3", ".png", ".jpg"))

if __name__ == "__main__":
    unittest.main()
