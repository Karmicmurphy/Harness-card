#!/usr/bin/env python3
"""Bounded FRIDAY operator decision/action tests; no provider or production calls."""
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "friday_operator.py"
spec = importlib.util.spec_from_file_location("friday_operator", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

SCORE = {"incident_count": 14, "learned_rule_count": 14,
         "closed_incident_rule_count": 7, "unresolved_incident_prevention_count": 7}
POLICY = {"mode": "AUTOMATE_UNTIL_OWNER_GATE",
          "automatic_actions": ["refresh owner-readable machine status"]}
STATUS = {"self_improvement": SCORE.copy()}

def fixture(root: Path, status=STATUS, policy=POLICY):
    state = root / "state"
    state.mkdir(parents=True)
    config = root / "config"
    config.mkdir(parents=True)
    (state / "HARNESS_SCORECARD.json").write_text(json.dumps(SCORE))
    if status is not None:
        (state / "FRIDAY_MACHINE_STATUS.json").write_text(json.dumps(status))
    (config / "friday_automation_policy.json").write_text(json.dumps(policy))


class OperatorTests(unittest.TestCase):
    def test_mismatch_triggers_bounded_repair(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root, status={"self_improvement": {"learned_rule_count": 13}})
            self.assertEqual(module.pick_action(root, None)["action"], "REPAIR_DERIVED_OWNER_STATUS")
            orig_validate, orig_write = module.validate, module.write_status
            try:
                module.validate = lambda _: []
                def safe_write(root, observation):
                    (root / "state/FRIDAY_MACHINE_STATUS.json").write_text(
                        json.dumps(STATUS))
                    (root / "state/FRIDAY_MACHINE_STATUS.md").write_text("FRIDAY")
                module.write_status = safe_write
                receipt = module.operate(root, None)
            finally:
                module.validate, module.write_status = orig_validate, orig_write
            self.assertEqual(receipt["verdict"], "PASS_REPAIRED")
            self.assertEqual(receipt["remaining_mismatches"], [])
            self.assertFalse(receipt["authority_changed"])
            self.assertFalse(receipt["production_changed"])

    def test_existing_refs_divergence_is_triage_not_auto_promotion(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            observation = {"components": [{"role": "cockpit", "repo": "example/cockpit",
                                            "state": "RECONCILIATION_REQUIRED"}]}
            plan = module.pick_action(root, observation)
            self.assertEqual(plan["action"], "TRIAGE_APPROVED_REF_DRIFT")
            old = module.validate
            try:
                module.validate = lambda _: []
                result = module.operate(root, observation)
            finally:
                module.validate = old
            self.assertEqual(result["verdict"], "PASS_TRIAGED_REQUIRES_REVIEW")
            self.assertFalse(result["authority_changed"])
            self.assertEqual(result["changed_paths"], [])

    def test_missing_observation_does_not_claim_proof(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            self.assertEqual(module.pick_action(root, None)["action"], "VERIFY_EXISTING_MACHINE_CONTINUITY")

    def test_authority_disagreement_stops_before_write(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root, status={"self_improvement": {}})
            original = module.validate
            try:
                module.validate = lambda _: ["CANONICAL PROJECTION DISAGREES"]
                receipt = module.operate(root)
            finally:
                module.validate = original
            self.assertEqual(receipt["verdict"], "BLOCKED_AUTHORITY")
            self.assertEqual(receipt["action"], "NONE")
            self.assertFalse(receipt["secret_values_accessed"])

    def test_disabled_policy_blocks_even_status_repair(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root, status=None, policy={"mode": "OFF", "automatic_actions": []})
            self.assertEqual(module.pick_action(root, None)["action"], "BLOCKED_POLICY")

if __name__ == "__main__":
    unittest.main()
