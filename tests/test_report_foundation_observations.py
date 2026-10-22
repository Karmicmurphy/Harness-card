#!/usr/bin/env python3
"""Read-only monitoring findings must stay visible but not masquerade as CI crashes."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
script = ROOT / "scripts/report_foundation_observations.py"
spec = importlib.util.spec_from_file_location("report_foundation_observations", script)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

refs = {
    "schema_version": "1.0.0", "authority_changed": False,
    "components": [{"role": role, "state": "MATCH" if role != "governance" else "OBSERVED_GOVERNANCE"}
                   for role in ("governance", "factory", "runtime", "salvage", "cockpit")]
}
preview = {"schema_version": "1.0.0", "changes_performed": False,
           "state": "UNKNOWN", "reason": "READ_ONLY_CLOUDFLARE_CREDENTIAL_NOT_CONFIGURED"}


class ReportTests(unittest.TestCase):
    def test_access_unknown_is_valid_evidence_not_a_crashed_job(self):
        r = {**refs, "components": [dict(x) for x in refs["components"]]}
        r["components"][1]["state"] = "UNKNOWN"
        s = module.summarize(r, preview)
        self.assertIn("UNVERIFIED", s)
        self.assertIn("UNKNOWN", s)
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory) / "a.json", Path(directory) / "b.json"
            a.write_text(json.dumps(r), encoding="utf-8")
            b.write_text(json.dumps(preview), encoding="utf-8")
            self.assertEqual(module.main(str(a), str(b)), 0)

    def test_real_drift_and_missing_preview_binding_raise_attention_not_green(self):
        r = {**refs, "components": [dict(x) for x in refs["components"]]}
        r["components"][-1]["state"] = "RECONCILIATION_REQUIRED"
        p = {**preview, "state": "CONFIG_BLOCKED",
             "required_binding_names_missing": ["FOUNDATION_GITHUB_TOKEN"]}
        s = module.summarize(r, p)
        self.assertIn("ATTENTION_REQUIRED", s)
        self.assertIn("FOUNDATION_GITHUB_TOKEN", s)
        self.assertNotIn("CONFIG_RECONCILED_NOT_LIVE_PROOF", s)

    def test_everything_matching_is_still_not_live_proof(self):
        p = {**preview, "state": "CONFIG_READY_RUNTIME_UNPROVEN"}
        s = module.summarize(refs, p)
        self.assertIn("CONFIG_RECONCILED_NOT_LIVE_PROOF", s)
        self.assertIn("It does NOT", s)

    def test_missing_bad_and_corrupt_reports_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory) / "a.json", Path(directory) / "b.json"
            b.write_text(json.dumps(preview), encoding="utf-8")
            self.assertEqual(module.main(str(a), str(b)), 2)
            a.write_text("bad-json", encoding="utf-8")
            self.assertEqual(module.main(str(a), str(b)), 2)
        for bad in (
            {**refs, "components": refs["components"][:-1]},
            {**refs, "authority_changed": True},
            {**refs, "components": [{**v, "state": "MADE_UP"} for v in refs["components"]]},
        ):
            with self.assertRaises(ValueError):
                module.summarize(bad, preview)


if __name__ == "__main__":
    unittest.main()
