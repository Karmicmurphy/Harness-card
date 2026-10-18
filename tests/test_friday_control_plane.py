#!/usr/bin/env python3
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "friday_control_plane", ROOT / "scripts" / "friday_control_plane.py"
)
module = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(module)

owner, automatic = module.split_blockers(
    ["CACHE_STALE", "LIVE_JOB_REQUIRES_EXPLICIT_APPROVAL", "SECRET_BINDING_MISSING"],
    ["EXPLICIT_APPROVAL", "SECRET"],
)
assert owner == ["LIVE_JOB_REQUIRES_EXPLICIT_APPROVAL", "SECRET_BINDING_MISSING"]
assert automatic == ["CACHE_STALE"]
assert module.choose_next_action("RECONCILIATION_REQUIRED", [], []) == "RECONCILE_REMOTE_STATE_BEFORE_MUTATION"
assert module.choose_next_action("CURRENTLY_RECONCILED", ["X"], []) == "AUTOMATE_BOUNDED_BLOCKER_REPAIR_AND_PROOF"
assert module.choose_next_action("CURRENTLY_RECONCILED", [], ["Y"]) == "STOP_AT_OWNER_GATE_WITH_PRECISE_REQUEST"
assert module.choose_next_action("CURRENTLY_RECONCILED", [], []) == "RUN_NEXT_BOUNDED_PROOF"

status = module.build_status(ROOT, None)
assert status["machine_state"] == "READY_FOR_BOUNDED_AUTOMATION", status
assert status["automation_mode"] == "AUTOMATE_UNTIL_OWNER_GATE", status
# A file-backed automation spine is not a live FRIDAY phone path.
assert status["delivery_readiness"]["state"] in ("OPERATOR_RUN_RECEIPT_PENDING", "BOUNDED_OPERATOR_RUN_PROVEN"), status
assert status["current_gate"]["gate_id"] == "FRIDAY_BOUNDED_OPERATOR_LOOP", status
assert "OPERATOR" in status["delivery_readiness"]["proof"], status
assert "preauthorized safe machine maintenance" in status["delivery_readiness"]["one_next_owner_action"]
assert "Active machine execution" in module.render_markdown(status)

assert status["owner_access"]["mode"] == "PHONE_ONLY", status
assert status["owner_access"]["platform"] == "ANDROID_PHONE", status
assert status["owner_access"]["pc_required"] is False, status
assert status["owner_access"]["resume_path"] == "state/FRIDAY_PHONE_ONLY_RECOVERY_2026-10-15.md", status
assert status["owner_access"]["recent_continuity_path"] == "state/FRIDAY_RECENT_CONTINUITY_2026-10-18.md", status
assert status["owner_access"]["recent_continuity_state"] == "FILE_PRESENT_RUNTIME_INGESTION_UNPROVEN", status
assert module.owner_access_profile(ROOT)["source"] == "OWNER_REPORTED_CURRENT"
assert status["learning"]["candidate_count"] >= 1, status
assert "closed_incident_rule_count" in status["self_improvement"]
assert "unresolved_incident_prevention_count" in status["self_improvement"]
assert "Unresolved prevention candidates" in module.render_markdown(status)

assert status["blockers"]["owner_attention_required"] is True, status
rendered = module.render_markdown(status)
assert "FRIDAY Machine Status" in rendered
assert "What actually needs Randy" in rendered
assert "Phone-only operation" in rendered
assert "PC required:** NO" in rendered
# A successful observation must cover every canonical repo; empty/partial output
# must never be labelled fully reconciled.
roles = ("governance", "factory", "runtime", "salvage", "cockpit")
complete = {"components": [{"role": role, "state": "MATCH"} for role in roles]}
assert module.observation_summary(complete)["state"] == "CURRENTLY_RECONCILED"
assert module.observation_summary({"components": []})["state"] == "NOT_SUPPLIED"
partial = module.observation_summary({"components": [{"role": "governance", "state": "MATCH"}]})
assert partial["state"] == "PARTIAL_UNKNOWN" and partial["unknown"] == 4, partial
bad_enum = {"components": [{"role": role, "state": "UNEXPECTED" if role == "salvage" else "MATCH"} for role in roles]}
assert module.observation_summary(bad_enum)["state"] == "PARTIAL_UNKNOWN"
duplicate = {"components": [{"role": "governance", "state": "MATCH"} for _ in roles]}
assert module.observation_summary(duplicate)["state"] == "PARTIAL_UNKNOWN"
drift = {"components": [{"role": role, "state": "RECONCILIATION_REQUIRED" if role == "cockpit" else "MATCH"} for role in roles]}
assert module.observation_summary(drift)["state"] == "RECONCILIATION_REQUIRED"

# A completed fixture is a separate evidence dimension from the observer output.
from copy import deepcopy
resolved = deepcopy(module.load_json(ROOT / "state/CURRENT_PROJECT.json"))
resolved["work_order"]["blockers"] = []
resolved["work_order"]["gate_id"] = "PAGES_BOUNDED_JOB_ROUND_TRIP"
no_blockers = module.delivery_readiness(resolved, [])
assert no_blockers["state"] == "PHONE_PROOF_REQUIRED", no_blockers
resolved["work_order"]["gate_id"] = "OTHER_GATE"
assert module.delivery_readiness(resolved, [])["state"] == "USER_PATH_NOT_PROVEN"
resolved["evidence_state"] = "PROVEN_LIVE"
assert module.delivery_readiness(resolved, [])["state"] == "RECORDED_LIVE_PROOF_REVERIFY_ON_CHANGE"

operator = module.load_json(ROOT / "state/CURRENT_PROJECT.json")
receipt = {"operator": "FRIDAY_BOUNDED_HARNESS_OPERATOR",
           "scope": "EXISTING_HARNESS_MAINTENANCE_ONLY",
           "verdict": "PASS_VALIDATED_NO_SAFE_CHANGE", "github_run_id": "123",
           "authority_changed": False, "other_repo_changed": False,
           "production_changed": False, "secret_values_accessed": False,
           "live_external_job_dispatched": False}
assert module.delivery_readiness(operator, [], receipt)["state"] == "BOUNDED_OPERATOR_RUN_PROVEN"
assert module.delivery_readiness(operator, [], {**receipt, "production_changed": True})["state"] == "OPERATOR_RUN_RECEIPT_PENDING"
assert module.delivery_readiness(operator, [], {**receipt, "github_run_id": "LOCAL_TEST"})["state"] == "OPERATOR_RUN_RECEIPT_PENDING"

print("FRIDAY control plane PASS")
