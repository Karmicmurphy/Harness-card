import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class WorkflowImplementationTests(unittest.TestCase):
    def test_tracking_is_not_execution_authority(self):
        state = json.loads((ROOT / "state/FOUNDATION_WORKFLOW_IMPLEMENTATION.json").read_text(encoding="utf-8"))
        self.assertFalse(state["grants_execution"])
        self.assertFalse(state["canonical_pins_changed"])
        self.assertEqual(state["execution_authority"], "state/CURRENT_PROJECT.json")
        self.assertEqual(len(state["components"]), 5)
        self.assertEqual(state["commissioning"]["state"], "BLOCKED")
        self.assertEqual(state["commissioning"]["original_request"], "request-first-001")
        allowed = {"PROVEN_IN_TEST", "IMPLEMENTED_UNPROVEN", "PARTIALLY_PROVEN", "PLANNED", "BLOCKED"}
        for item in state["workstreams"]:
            self.assertIn(item["state"], allowed)
            self.assertTrue(item.get("limits") or item.get("gate"))

    def test_bootstrap_and_contract_find_one_specification(self):
        state = json.loads((ROOT / "state/FOUNDATION_WORKFLOW_IMPLEMENTATION.json").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / state["specification"]).is_file())
        for path in ("AGENTS.md", "OPERATING_CONTRACT.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            self.assertIn(state["specification"], text)
            self.assertIn("state/FOUNDATION_WORKFLOW_IMPLEMENTATION.json", text)


if __name__ == "__main__":
    unittest.main()
