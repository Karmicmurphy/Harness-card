import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/provider_release_gate.py"
SPEC = importlib.util.spec_from_file_location("provider_release_gate", SCRIPT)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(module)
SHA = "2e07e429c9174d6ea99503e357476c37f8c5b241"


def packet():
    return {
        "target": {"repo": "Karmicmurphy/coilside", "branch": "main", "sha": SHA,
                   "service": "coilside", "environment": "production",
                   "required_bindings": ["COILSIDE_DB", "ASSETS"]},
        "authorization": {"production_approved": True},
        "ci": {"sha": SHA, "conclusion": "success", "run_url": "https://github.com/Karmicmurphy/coilside/actions/runs/1"},
        "deployment": {"sha": SHA, "status": "success", "service": "coilside",
                       "environment": "production", "id": "deploy-1", "traffic_percent": 100,
                       "bindings": ["COILSIDE_DB", "ASSETS"]},
    }


class GateTests(unittest.TestCase):
    def test_deployed_is_not_live(self):
        r = module.evaluate(packet())
        self.assertEqual(r["evidence_level"], "DEPLOYMENT_CONFIRMED")
        self.assertEqual(r["verdict"], "PARTIALLY_PROVEN")

    def test_wrong_commit_fails_closed(self):
        p = packet(); p["deployment"]["sha"] = "1" * 40
        self.assertEqual(module.evaluate(p)["reason"], "DEPLOY_SHA_UNKNOWN_OR_MISMATCH")

    def test_ci_wrong_sha_fails_closed(self):
        p = packet(); p["ci"]["sha"] = "1" * 40
        self.assertEqual(module.evaluate(p)["reason"], "CI_SHA_UNKNOWN_OR_MISMATCH")

    def test_failed_ci(self):
        p = packet(); p["ci"]["conclusion"] = "failure"
        self.assertEqual(module.evaluate(p)["verdict"], "FAILED")

    def test_missing_owner_approval(self):
        p = packet(); p["authorization"]["production_approved"] = False
        self.assertEqual(module.evaluate(p)["reason"], "PRODUCTION_OWNER_GATE")

    def test_missing_binding(self):
        p = packet(); p["deployment"]["bindings"] = ["ASSETS"]
        self.assertEqual(module.evaluate(p)["reason"], "REQUIRED_BINDINGS_MISSING")

    def test_partial_traffic(self):
        p = packet(); p["deployment"]["traffic_percent"] = 90
        self.assertEqual(module.evaluate(p)["reason"], "TRAFFIC_NOT_100_PERCENT")

    def test_access_edge_denial_does_not_count_as_live(self):
        p = packet(); p["live"] = {"http_status": 403, "sha": SHA}
        self.assertEqual(module.evaluate(p)["reason"], "LIVE_AUTH_OR_EDGE_DENIED")

    def test_phone_path_incomplete(self):
        p = packet(); p["live"] = {"http_status": 200, "sha": SHA, "expected_screen_visible": True}
        self.assertEqual(module.evaluate(p)["reason"], "LIVE_ACTION_NOT_PROVEN")

    def test_complete_proof_still_needs_independent_review(self):
        p = packet(); p["live"] = {"http_status": 200, "sha": SHA,
                                  "expected_screen_visible": True, "primary_action_verified": True,
                                  "device": "android", "proof_ref": "verified-session/receipt-1"}
        r = module.evaluate(p)
        self.assertEqual(r["verdict"], "READY_FOR_INDEPENDENT_REVIEW")
        self.assertNotEqual(r["evidence_level"], "PROVEN_LIVE")

    def test_no_secrets_in_receipt(self):
        p = packet(); p["arbitrary_secret"] = "should-never-print"
        p["deployment"]["api_token"] = "should-never-print"
        self.assertNotIn("should-never-print", str(module.evaluate(p)))

    def test_bad_sha_rejected(self):
        p = packet(); p["target"]["sha"] = "main"
        with self.assertRaises(ValueError): module.evaluate(p)


if __name__ == "__main__":
    unittest.main()
