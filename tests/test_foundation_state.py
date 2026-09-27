import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("foundation_state", ROOT / "scripts/foundation_state.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ContinuityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ("state", "config", "docs", "projects"):
            shutil.copytree(ROOT / folder, self.root / folder)
        self.current = MODULE.load(self.root / "state/CURRENT_PROJECT.json")

    def test_generated_files_agree(self):
        self.assertEqual(MODULE.projection_errors(self.root, self.current), [])

    def test_stale_markdown_next_step_is_detected(self):
        p = self.root / "state/ACTIVE_WORK_ORDER.md"
        p.write_text(p.read_text() + "\nRestart Windows before doing anything.\n")
        self.assertTrue(any("ACTIVE_WORK_ORDER.md" in e for e in MODULE.projection_errors(self.root, self.current)))

    def test_old_build_prompt_is_detected(self):
        p = self.root / "docs/FOUNDATION_V0_CURRENT_WORK_PROMPT.md"
        p.write_text("Resume Cog 3; rebuild Independent Proof")
        self.assertTrue(any("CURRENT_WORK_PROMPT" in e for e in MODULE.projection_errors(self.root, self.current)))

    def test_date_and_blocker_drift_are_detected(self):
        p = self.root / "state/ACTIVE_WORK_ORDER.json"
        d = json.loads(p.read_text())
        d.update(updated_at="2020-01-01", blockers=["OLD_WINDOWS_GATE"])
        p.write_text(json.dumps(d))
        self.assertTrue(any("ACTIVE_WORK_ORDER.json" in e for e in MODULE.projection_errors(self.root, self.current)))

    def test_invalid_evidence_enum_is_rejected(self):
        self.current["evidence_state"] = "PROVEN_EVERYWHERE_PROBABLY"
        self.assertTrue(any("evidence_state" in e for e in MODULE.contract_errors(self.root, self.current)))

    def test_short_sha_is_rejected(self):
        self.current["authority"]["factory"]["sha"] = "deadbeef"
        self.assertTrue(any("full SHA" in e for e in MODULE.contract_errors(self.root, self.current)))

    def test_missing_gate_is_rejected(self):
        self.current["work_order"].pop("gate_id")
        self.assertTrue(any("gate_id" in e for e in MODULE.contract_errors(self.root, self.current)))

    def test_missing_projection_is_detected(self):
        (self.root / "state/ACTIVE_WORK_ORDER.md").unlink()
        self.assertTrue(MODULE.projection_errors(self.root, self.current))

    def test_projection_preserves_unrelated_ecosystem_records(self):
        before = MODULE.load(self.root / "state/ECOSYSTEM_AUTHORITY_INDEX.json")
        projected = json.loads(MODULE.projections(self.root, self.current)["state/ECOSYSTEM_AUTHORITY_INDEX.json"])
        for key in before:
            if key != "active_foundation_v0":
                self.assertEqual(before[key], projected[key])
        self.assertEqual(before["active_foundation_v0"]["quarantine_examples"], projected["active_foundation_v0"]["quarantine_examples"])

    def test_sync_does_not_promote_observed_cockpit_sha(self):
        before = copy.deepcopy(self.current)
        MODULE.projections(self.root, self.current)
        self.assertEqual(self.current, before)
        self.assertEqual(self.current["authority"]["cockpit"]["sha"], "1785ed1405e769a17ec22066dc1e27a40dbf153b")

    def fake_get(self, path):
        for ref in self.current["authority"].values():
            if path.startswith(ref["repo"] + "/"):
                sha = ref.get("sha", "a" * 40)
                return {"commit": {"sha": sha}} if "/branches/" in path else {"sha": sha}
        raise AssertionError(path)

    def test_matching_refs_are_not_live_proof(self):
        report = MODULE.observe(self.current, self.fake_get)
        self.assertTrue(all(r["state"] in ("MATCH", "OBSERVED_GOVERNANCE") for r in report["components"]))
        self.assertIn("NOT_RUNTIME_OR_DEPLOY_PROOF", report["scope"])
        self.assertFalse(report["authority_changed"])

    def test_remote_advancement_requests_reconciliation_without_mutation(self):
        before = copy.deepcopy(self.current)
        def get(path):
            if "Ollie_Twis_Holo_workshop/branches/" in path:
                return {"commit": {"sha": "b" * 40}}
            return self.fake_get(path)
        report = MODULE.observe(self.current, get)
        self.assertEqual(report["components"][-1]["state"], "RECONCILIATION_REQUIRED")
        self.assertEqual(before, self.current)

    def test_private_or_missing_repo_is_unknown_not_missing_or_passed(self):
        for code in (401, 403, 404, 429, 500):
            with self.subTest(code=code):
                def get(path):
                    raise HTTPError("https://api.github.com", code, "unavailable", {}, None)
                rows = MODULE.observe(self.current, get)["components"]
                self.assertTrue(all(r["state"] == "UNKNOWN" for r in rows))

    def test_approved_pin_must_exist_even_if_branch_matches(self):
        def get(path):
            if "/commits/" in path:
                raise HTTPError("https://api.github.com", 404, "missing", {}, None)
            return self.fake_get(path)
        rows = MODULE.observe(self.current, get)["components"]
        self.assertTrue(all(r["state"] == "UNKNOWN" for r in rows if r["approved_sha"]))

    def test_malformed_remote_response_is_unknown(self):
        rows = MODULE.observe(self.current, lambda path: {})["components"]
        self.assertTrue(all(r["state"] == "UNKNOWN" for r in rows))

    def test_authority_digest_changes_when_a_pin_changes(self):
        before = MODULE.authority_digest(self.current)
        self.current["authority"]["factory"]["sha"] = "b" * 40
        self.assertNotEqual(before, MODULE.authority_digest(self.current))


if __name__ == "__main__":
    unittest.main()
