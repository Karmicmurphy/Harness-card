#!/usr/bin/env python3
"""FRIDAY artifact-compass diagnostics: evidence-only, bounded and deduplicated."""
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("radar", ROOT / "scripts/friday_diagnostics.py")
radar = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(radar)
operator_spec = importlib.util.spec_from_file_location("friday_operator", ROOT / "scripts/friday_operator.py")
op = importlib.util.module_from_spec(operator_spec)
assert operator_spec.loader is not None
operator_spec.loader.exec_module(op)
A, B, C = ("a"*40, "b"*40, "c"*40)


def canonical():
    return {"work_order": {"gate_id": "FRIDAY_BOUNDED_OPERATOR_LOOP"}, "authority": {
        role: {"repo": f"Karmicmurphy/{role}", "branch": "main", "sha": A}
        for role in radar.ROLES
    }}


def observation(roles=("factory",)):
    return {"schema_version": "1.0.0", "components": [
        {"role": role, "repo": f"Karmicmurphy/{role}", "approved_sha": A,
         "observed_sha": B, "state": "RECONCILIATION_REQUIRED"}
        for role in roles
    ]}


def receipt(role="factory", verdict="PASS_DELTA_INSPECTED_REQUIRES_REVIEW"):
    return {"action": "TRIAGE_APPROVED_REF_DRIFT",
            "verdict": verdict, "decision": {"role": role, "repo": f"Karmicmurphy/{role}"},
            "inspected_delta": {"approved_sha": A, "observed_sha": B, "changed_files": ["src/safe.py"],
                                "no_auto_promotion": True}}


class RadarTests(unittest.TestCase):
    def test_observation_outage_preserves_exhaustion_and_triage(self):
        for final in (radar.FAILED_READ, radar.TERMINAL_TRIAGED):
            with self.subTest(final=final):
                rows=radar.candidates(canonical(),observation(),{'items':[]})
                rows[0].update(state=final,read_attempts=3,
                    proof_verdict='PASS_DELTA_INSPECTED_REQUIRES_REVIEW' if final==radar.TERMINAL_TRIAGED else None)
                outage=radar.candidates(canonical(),None,{'items':rows})
                self.assertIsNone(outage[0]['observed_sha'])
                self.assertEqual(outage[0]['read_attempts'],3)
                returned=radar.candidates(canonical(),observation(),{'items':outage})
                self.assertEqual(returned[0]['state'],final)
                self.assertEqual(returned[0]['read_attempts'],3)
                self.assertIsNone(radar.pick_untriaged(returned))
                if final==radar.FAILED_READ:
                    self.assertEqual(returned[0]['next_method'],'STOP_REQUIRES_OWNER_REVIEW')
                    self.assertEqual(returned[0]['candidate_disposition'],'DEFER')

    def test_dated_protocols_route_to_live_friday_gate_not_parked_phone(self):
        night = (ROOT / "docs/FRIDAY_NIGHT_SHIFT_PROTOCOL.md").read_text(encoding="utf-8")
        spine = (ROOT / "docs/FRIDAY_AUTOMATION_SPINE.md").read_text(encoding="utf-8")
        self.assertNotIn("The canonical Foundation next gate is still `PAGES_BOUNDED_JOB_ROUND_TRIP`", night)
        self.assertIn("FRIDAY_BOUNDED_OPERATOR_LOOP", night)
        self.assertIn("Android/phone and Cloudflare Pages Preview remain parked", night)
        self.assertIn("state/CURRENT_PROJECT.json", spine)
        self.assertIn("state/FRIDAY_MAINTENANCE_QUEUE.json", spine)
        self.assertIn("NOT GENERAL LIVE FRIDAY", spine)

    def test_first_new_drift_then_verified_same_sha_is_not_repeated(self):
        with TemporaryDirectory() as d:
            root = Path(d)
            (root/"state").mkdir()
            (root/"state/CURRENT_PROJECT.json").write_text(json.dumps(canonical()))
            first = radar.build_queue(root, observation(("factory", "runtime")), receipt())
            self.assertEqual(first["items"][0]["state"], radar.TERMINAL_TRIAGED)
            self.assertEqual(first["items"][0]["next_method"], "NO_AUTOMATIC_ACTION_REQUIRES_REVIEW")
            self.assertEqual(first["items"][0]["candidate_disposition"], "REVIEW")
            self.assertEqual(first["items"][1]["state"], radar.PENDING)
            self.assertEqual(first["summary"]["triaged_for_review"], 1)
            self.assertEqual(first["summary"]["pending"], 1)
            radar.write_queue(root, first)
            following = radar.build_queue(root, observation(("factory", "runtime")), {})
            pick = radar.pick_untriaged(following["items"])
            self.assertEqual(pick["role"], "runtime")
            radar.write_queue(root, following)
            latest = radar.build_queue(root, observation(("factory", "runtime")), receipt("runtime"))
            self.assertEqual(latest["summary"]["triaged_for_review"], 2)
            self.assertIsNone(radar.pick_untriaged(latest["items"]))

    def test_new_commit_invalidates_prior_review_without_automatic_promotion(self):
        with TemporaryDirectory() as d:
            root=Path(d);(root/"state").mkdir()
            (root/"state/CURRENT_PROJECT.json").write_text(json.dumps(canonical()))
            radar.write_queue(root, radar.build_queue(root, observation(), receipt()))
            obs=observation()
            obs["components"][0]["observed_sha"]=C
            new=radar.build_queue(root, obs, {})
            self.assertEqual(new["items"][0]["state"], radar.PENDING)
            self.assertEqual(new["items"][0]["read_attempts"], 0)
            self.assertEqual(new["items"][0]["observed_sha"], C)
            self.assertEqual(new["items"][0]["owner_gate"], "NO_AUTO_REPIN_OR_MERGE")

    def test_unknown_and_untrusted_rows_stop_no_permission_bypass(self):
        for tamper in ({"state":"UNKNOWN","observed_sha":None},
                       {"repo":"untrusted/other"}, {"approved_sha":B},
                       {"observed_sha":"invalid"}):
            with self.subTest(tamper=tamper):
                obs=observation()
                obs["components"][0].update(tamper)
                rows=radar.candidates(canonical(), obs, radar.load_queue(Path("/nonexistent-friday-diagnostics-fixture")))
                self.assertEqual(rows[0]["state"], radar.ACCESS)
                self.assertEqual(rows[0]["next_method"], "STOP_NEEDS_AUTHORIZED_READ")

    def test_failed_comparison_retry_budget_3_and_stop(self):
        with TemporaryDirectory() as d:
            root=Path(d);(root/"state").mkdir()
            (root/"state/CURRENT_PROJECT.json").write_text(json.dumps(canonical()))
            for n in range(3):
                queue=radar.build_queue(root, observation(), receipt(verdict="BLOCKED_REMOTE_DELTA_UNAVAILABLE"))
                radar.write_queue(root, queue)
                self.assertEqual(queue["items"][0]["read_attempts"], n+1)
            self.assertEqual(queue["summary"]["read_attempts_exhausted"],1)
            self.assertEqual(queue["items"][0]["next_method"], "STOP_REQUIRES_OWNER_REVIEW")
            self.assertEqual(queue["items"][0]["candidate_disposition"], "DEFER")
            self.assertIsNone(radar.pick_untriaged(queue["items"]))
            again=radar.build_queue(root,observation(),{})
            self.assertEqual(again["items"][0]["read_attempts"],3)

    def test_mismatched_receipt_cannot_fake_triaged(self):
        with TemporaryDirectory() as d:
            root=Path(d);(root/"state").mkdir()
            (root/"state/CURRENT_PROJECT.json").write_text(json.dumps(canonical()))
            bad=receipt();bad["inspected_delta"]["observed_sha"]=C
            q=radar.build_queue(root,observation(),bad)
            self.assertEqual(q["items"][0]["state"], radar.FAILED_READ)
            self.assertEqual(q["items"][0]["proof_verdict"],None)

    def test_corrupt_queue_refuses_overwrite_and_observer_duplicates_rejected(self):
        with TemporaryDirectory() as d:
            root=Path(d);(root/"state").mkdir()
            (root/"state/CURRENT_PROJECT.json").write_text(json.dumps(canonical()))
            path=root/"state/FRIDAY_MAINTENANCE_QUEUE.json"
            path.write_text("{broken")
            with self.assertRaises(radar.InvalidQueue):
                radar.build_queue(root,observation(),{})
            self.assertEqual(path.read_text(),"{broken")
            path.unlink()
            obs=observation(("factory","factory"))
            with self.assertRaises(radar.InvalidQueue):
                radar.build_queue(root,obs,{})

    def test_operator_chooses_next_unique_item_not_perpetual_same_diff(self):
        with TemporaryDirectory() as d:
            root=Path(d)
            (root/"state").mkdir()
            (root/"config").mkdir()
            (root/"state/CURRENT_PROJECT.json").write_text(json.dumps(canonical()))
            (root/"state/HARNESS_SCORECARD.json").write_text(json.dumps({
                "incident_count":1, "learned_rule_count":1, "closed_incident_rule_count":1,
                "unresolved_incident_prevention_count":0,
            }))
            score=json.loads((root/"state/HARNESS_SCORECARD.json").read_text())
            (root/"state/FRIDAY_MACHINE_STATUS.json").write_text(json.dumps({"self_improvement":score}))
            (root/"config/friday_automation_policy.json").write_text(json.dumps({
                "mode":"AUTOMATE_UNTIL_OWNER_GATE",
                "automatic_actions":["refresh owner-readable machine status"]
            }))
            obs=observation(("factory","runtime"))
            self.assertEqual(op.pick_action(root,obs)["role"],"factory")
            radar.write_queue(root,radar.build_queue(root,obs,receipt()))
            self.assertEqual(op.pick_action(root,obs)["role"],"runtime")
            radar.write_queue(root,radar.build_queue(root,obs,receipt("runtime")))
            self.assertEqual(op.pick_action(root,obs)["action"],"VERIFY_EXISTING_MACHINE_CONTINUITY")
            self.assertNotIn("deploy",json.dumps(radar.load_queue(root/"state/FRIDAY_MAINTENANCE_QUEUE.json")).lower())


if __name__=="__main__":
    unittest.main()
