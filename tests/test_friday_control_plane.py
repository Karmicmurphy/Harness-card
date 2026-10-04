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
assert status["learning"]["candidate_count"] >= 1, status
assert status["blockers"]["owner_attention_required"] is True, status
rendered = module.render_markdown(status)
assert "FRIDAY Machine Status" in rendered
assert "What actually needs Randy" in rendered
print("FRIDAY control plane PASS")
