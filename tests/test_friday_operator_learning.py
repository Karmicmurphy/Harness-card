#!/usr/bin/env python3
"""Safe FRIDAY operator learning: evidence, never broad automatic self-promotion."""
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "workers" / "self_improve.py"
spec = importlib.util.spec_from_file_location("worker_learner", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def event(run_id, verdict="PASS_REPAIRED", outcomes=None):
    outcomes = outcomes if outcomes is not None else ["PASS_INDEPENDENT_RECHECK"]
    return {"run_id": str(run_id), "action": "REPAIR_DERIVED_OWNER_STATUS",
            "verdict": verdict, "attempt_count": len(outcomes), "attempt_outcomes": outcomes,
            "proof": "INDEPENDENT_SCORE_STATUS_RECHECK", "stopped_reason": "PROOF_PASSED"}


class LearningFromRetriesTests(unittest.TestCase):
    def write(self, root, rows, *, privacy="SANITIZED_CI_OUTCOMES_ONLY"):
        (root / "FRIDAY_OPERATOR_REPAIR_HISTORY.json").write_text(json.dumps({
            "schema_version": "1.0.0", "privacy": privacy, "runs": rows,
        }))

    def test_no_history_never_claims_proof(self):
        with TemporaryDirectory() as td:
            result = module.operator_outcome_summary(Path(td))
            self.assertEqual(result["runs"], 0)
            self.assertFalse(result["verified_repeatable_repair"])

    def test_one_verified_repair_is_not_repeatable_proof(self):
        with TemporaryDirectory() as td:
            root = Path(td)
            self.write(root, [event(101)])
            result = module.operator_outcome_summary(root)
            self.assertEqual(result["repaired_runs"], 1)
            self.assertFalse(result["verified_repeatable_repair"])

    def test_two_independent_repairs_are_repeatable_only_for_status(self):
        with TemporaryDirectory() as td:
            root = Path(td)
            self.write(root, [event(101), event(102, outcomes=[
                "RETRYABLE_LOCAL_IO_FAILURE", "PASS_INDEPENDENT_RECHECK"
            ])])
            result = module.operator_outcome_summary(root)
            self.assertEqual(result["runs"], 2)
            self.assertEqual(result["repaired_runs"], 2)
            self.assertEqual(result["retry_recovered_runs"], 1)
            self.assertTrue(result["verified_repeatable_repair"])

    def test_failure_is_not_a_success(self):
        with TemporaryDirectory() as td:
            root = Path(td)
            self.write(root, [event(101), event(102, verdict="FAILED_REPAIR",
                       outcomes=["RETRYABLE_LOCAL_IO_FAILURE"] * 3)])
            result = module.operator_outcome_summary(root)
            self.assertEqual(result["repaired_runs"], 1)
            self.assertEqual(result["failed_repairs"], 1)
            self.assertFalse(result["verified_repeatable_repair"])

    def test_reject_corrupt_history_unknown_event_and_duplicate_run(self):
        with TemporaryDirectory() as td:
            root = Path(td)
            for rows, privacy in [
                ([event(1), event(1)], "SANITIZED_CI_OUTCOMES_ONLY"),
                ([event(1)], "RAW_USER_CHAT"),
                ([{**event(1), "action": "DEPLOY"}], "SANITIZED_CI_OUTCOMES_ONLY"),
                ([{**event(1), "attempt_count": 4}], "SANITIZED_CI_OUTCOMES_ONLY"),
                ([{**event(1), "attempt_outcomes": ["MAGIC"]}], "SANITIZED_CI_OUTCOMES_ONLY"),
                ([{**event(1), "proof": "CLAIM_NOT_INDEPENDENT"}], "SANITIZED_CI_OUTCOMES_ONLY"),
            ]:
                with self.subTest(rows=rows, privacy=privacy):
                    self.write(root, rows, privacy=privacy)
                    if rows[0].get("proof") == "CLAIM_NOT_INDEPENDENT":
                        result = module.operator_outcome_summary(root)
                        self.assertFalse(result["verified_repeatable_repair"])
                        self.assertEqual(result["repaired_runs"], 0)
                    else:
                        with self.assertRaises(ValueError):
                            module.operator_outcome_summary(root)


if __name__ == "__main__":
    unittest.main()
