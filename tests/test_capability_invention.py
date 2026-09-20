import unittest
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "workers"))
import capability_invention as ci

class CapabilityInventionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = ci.load_map(ROOT / "state" / "CAPABILITY_MAP.json")
    def test_map_has_unique_ids(self):
        ids=[c["id"] for c in self.data["capabilities"]]
        self.assertEqual(len(ids), len(set(ids)))
    def test_finds_execution_kernel_overlap(self):
        result=ci.answer("bounded execution kernel with recovery", self.data)
        self.assertEqual(result["verdict"], "OWNED_OVERLAP")
        self.assertEqual(result["matches"][0]["id"], "execution.bounded")
    def test_finds_artifact_compass_lineage(self):
        result=ci.answer("artifact compass discovery salvage", self.data)
        self.assertIn(result["verdict"], {"OWNED","OWNED_OVERLAP"})
        self.assertEqual(result["matches"][0]["id"], "research.temporal_compass")
    def test_software_builder_resume_not_redesign(self):
        result=ci.answer("software builder coding worker", self.data)
        self.assertEqual(result["matches"][0]["id"], "software.builder")
        self.assertEqual(result["action"], "RESUME_DONT_REDESIGN")
    def test_unknown_request_does_not_invent_automatically(self):
        result=ci.answer("quantum pineapple telemetry", self.data)
        self.assertEqual(result["verdict"], "POSSIBLE_GAP")
        self.assertEqual(result["action"], "RECOVER_MORE_BEFORE_INVENTING")

if __name__ == "__main__":
    unittest.main()
