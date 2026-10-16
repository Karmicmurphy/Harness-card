#!/usr/bin/env python3
"""Night Shift must never call remote drift a fully green machine."""
from pathlib import Path
import importlib.util
import json
import tempfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "night_shift_receipt", ROOT / "scripts/night_shift_receipt.py"
)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

checks = {name: "success" for name, _ in module.CHECK_KEYS}
base = {
    "remote_authority_observation": {
        "state": "RECONCILIATION_REQUIRED",
        "reconciliation_required": 1,
        "unknown": 2,
    },
    "current_gate": {"gate_id": "PAGES_BOUNDED_JOB_ROUND_TRIP"},
    "blockers": {"owner_gate": ["PREVIEW_SECRET_BINDING_MISSING"]},
}
proof = module.report(checks, base)
assert proof["verdict"] == "TESTS_PASS__RECONCILIATION_REQUIRED", proof
assert proof["reconciliation_required"] == 1
assert proof["remote_unknown"] == 2
assert proof["owner_gates"] == 1

text = module.render(checks, base, {
    "GITHUB_REPOSITORY": "example/harness",
    "GITHUB_RUN_ID": "123",
    "GITHUB_SHA": "abc",
    "GITHUB_EVENT_NAME": "schedule",
})
assert "TESTS_PASS__RECONCILIATION_REQUIRED" in text
assert "NEVER auto-promote a branch SHA" in text
assert "PAGES_BOUNDED_JOB_ROUND_TRIP" in text
assert "Runtime proof:** NOT CLAIMED" in text

for state, expected in [
    ("PARTIAL_UNKNOWN", "TESTS_PASS__REMOTE_UNVERIFIED"),
    ("NOT_SUPPLIED", "TESTS_PASS__REMOTE_UNVERIFIED"),
    ("CURRENTLY_RECONCILED", "TESTS_PASS__CURRENTLY_RECONCILED"),
    ("UNEXPECTED", "TESTS_PASS__REMOTE_UNVERIFIED"),
]:
    candidate = {**base, "remote_authority_observation": {"state": state}}
    assert module.report(checks, candidate)["verdict"] == expected, state

bad = {**checks, "Full Harness regression": "failure"}
assert module.report(bad, base)["verdict"] == "FAILED_OR_INCOMPLETE"
assert module.report(checks, None)["verdict"] == "FAILED_OR_INCOMPLETE"
assert module.report(checks, {"remote_authority_observation": {}})["verdict"] == "TESTS_PASS__REMOTE_UNVERIFIED"

with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "status.json"
    assert module.safe_status(path) is None
    path.write_text("nope", encoding="utf-8")
    assert module.safe_status(path) is None
    path.write_text(json.dumps(base), encoding="utf-8")
    assert module.safe_status(path) == base

print("FRIDAY Night Shift honest receipt PASS")
