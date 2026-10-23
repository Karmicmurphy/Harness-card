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
            old, old_inspect = module.validate, module.inspect_approved_ref_delta
            try:
                module.validate = lambda _: []
                module.inspect_approved_ref_delta = lambda *_: {
                    "verdict": "PASS_DELTA_INSPECTED_REQUIRES_REVIEW",
                    "changed_files": ["test.py"], "no_auto_promotion": True,
                }
                result = module.operate(root, observation)
            finally:
                module.validate, module.inspect_approved_ref_delta = old, old_inspect
            self.assertEqual(result["verdict"], "PASS_DELTA_INSPECTED_REQUIRES_REVIEW")
            self.assertEqual(result["inspected_delta"]["changed_files"], ["test.py"])
            self.assertFalse(result["authority_changed"])
            self.assertEqual(result["changed_paths"], [])

    def test_actual_approved_ref_comparison_and_fail_closed_guards(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            canonical = {"authority": {"cockpit": {"repo": "example/cockpit", "sha": "a" * 40}}}
            (root / "state/CURRENT_PROJECT.json").write_text(json.dumps(canonical))
            row = {"role": "cockpit", "repo": "example/cockpit",
                   "approved_sha": "a" * 40, "observed_sha": "b" * 40,
                   "state": "RECONCILIATION_REQUIRED"}
            seen = []
            def remote(path):
                seen.append(path)
                return {"ahead_by": 1, "behind_by": 0, "files": [{"filename": "readme.md"}]}
            decision = {"role": "cockpit"}
            result = module.inspect_approved_ref_delta(root, {"components": [row]}, decision, get=remote)
            self.assertEqual(result["verdict"], "PASS_DELTA_INSPECTED_REQUIRES_REVIEW")
            self.assertEqual(result["changed_files"], ["readme.md"])
            self.assertIn("compare/" + "a" * 40 + "..." + "b" * 40, seen[0])
            altered = {**row, "observed_sha": "NOT_A_SHA"}
            bad = module.inspect_approved_ref_delta(root, {"components": [altered]}, decision, get=remote)
            self.assertEqual(bad["verdict"], "BLOCKED_UNVERIFIED_REFS")
            mismatch = module.inspect_approved_ref_delta(root, {"components": [{**row, "repo": "wrong/name"}]}, decision, get=remote)
            self.assertEqual(mismatch["verdict"], "BLOCKED_AUTHORITY_MISMATCH")
            def fail(_):
                raise ValueError("provider down")
            offline = module.inspect_approved_ref_delta(root, {"components": [row]}, decision, get=fail)
            self.assertEqual(offline["verdict"], "BLOCKED_REMOTE_DELTA_UNAVAILABLE")

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

    def test_transient_io_retry_then_independent_verified_repair(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            called = []
            original = module.write_status
            try:
                def intermittent(root, observation):
                    called.append(len(called) + 1)
                    if len(called) < 3:
                        raise OSError("temporary local filesystem error")
                    (root / "state/FRIDAY_MACHINE_STATUS.json").write_text(json.dumps(STATUS))
                module.write_status = intermittent
                proof = module.repair_with_proof(root, None)
            finally:
                module.write_status = original
            self.assertEqual(len(called), 3)
            self.assertEqual(proof["verdict"], "PASS_REPAIRED")
            self.assertEqual([x["result"] for x in proof["attempts"]],
                             ["RETRYABLE_LOCAL_IO_FAILURE"] * 2 + ["PASS_INDEPENDENT_RECHECK"])
            self.assertEqual(proof["stopped_reason"], "PROOF_PASSED")

    def test_semantic_failure_does_not_waste_retry_budget(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            called = []
            original = module.write_status
            try:
                def inconsistent(root, observation):
                    called.append(1)
                    (root / "state/FRIDAY_MACHINE_STATUS.json").write_text(
                        json.dumps({"self_improvement": {"incident_count": -1}}))
                module.write_status = inconsistent
                proof = module.repair_with_proof(root, None)
            finally:
                module.write_status = original
            self.assertEqual(len(called), 1)
            self.assertEqual(proof["verdict"], "FAILED_REPAIR")
            self.assertEqual(proof["stopped_reason"], "NON_RETRYABLE_SEMANTIC_FAILURE")
            self.assertIn("incident_count", proof["remaining_mismatches"])

    def test_io_budget_exhaustion_does_not_claim_success(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            original = module.write_status
            try:
                module.write_status = lambda *_: (_ for _ in ()).throw(OSError("full filesystem"))
                proof = module.repair_with_proof(root, None)
            finally:
                module.write_status = original
            self.assertEqual(proof["verdict"], "FAILED_REPAIR")
            self.assertEqual(proof["stopped_reason"], "RETRY_BUDGET_EXHAUSTED")
            self.assertEqual(len(proof["attempts"]), 3)
            with self.assertRaises(ValueError):
                module.repair_with_proof(root, None, max_attempts=4)

    def test_sanitized_deduplicated_bounded_learning_history(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            entry = {"github_run_id": "123", "action": "REPAIR_DERIVED_OWNER_STATUS",
                     "verdict": "PASS_REPAIRED", "proof": "INDEPENDENT_SCORE_STATUS_RECHECK",
                     "repair_attempts": [{"attempt": 1, "result": "PASS_INDEPENDENT_RECHECK"}],
                     "repair_stop_reason": "PROOF_PASSED",
                     "raw_owner_request": "sensitive content not for recording"}
            module.preserve_sanitized_repair_history(root, entry)
            module.preserve_sanitized_repair_history(root, entry)
            path = root / "state/FRIDAY_OPERATOR_REPAIR_HISTORY.json"
            record = json.loads(path.read_text())
            self.assertEqual(len(record["runs"]), 1)
            self.assertNotIn("sensitive content", path.read_text())
            self.assertEqual(record["runs"][0]["attempt_count"], 1)
            for i in range(50):
                module.preserve_sanitized_repair_history(root, {
                    **entry, "github_run_id": str(200 + i),
                })
            record = json.loads(path.read_text())
            self.assertEqual(len(record["runs"]), 50)
            with self.assertRaises(ValueError):
                module.preserve_sanitized_repair_history(root, {**entry, "github_run_id": "LOCAL_TEST"})
            with self.assertRaises(ValueError):
                module.preserve_sanitized_repair_history(root, {**entry, "action": "DEPLOY"})

    def test_disabled_policy_blocks_even_status_repair(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root, status=None, policy={"mode": "OFF", "automatic_actions": []})
            self.assertEqual(module.pick_action(root, None)["action"], "BLOCKED_POLICY")

if __name__ == "__main__":
    unittest.main()
