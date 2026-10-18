#!/usr/bin/env python3
"""FRIDAY's bounded machine operator: choose one allowed action, execute it, verify, receipt.

This is a deterministic execution controller for the EXISTING Harness scheduler.
It is not an LLM, a replacement for the local FRIDAY MCP, or permission to deploy,
spend, change approvals, access secrets, or rewrite other repositories.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_authority_spine import validate  # noqa: E402
from friday_control_plane import build_status, render_markdown  # noqa: E402

SCORE_KEYS = ("incident_count", "learned_rule_count",
              "closed_incident_rule_count", "unresolved_incident_prevention_count")
REQUIRED_POLICY_ACTION = "refresh owner-readable machine status"


def load_optional_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except (OSError, ValueError, UnicodeError):
        return None


def score_disagreement(status: dict | None, score: dict) -> list[str]:
    seen = (status or {}).get("self_improvement") or {}
    return [k for k in SCORE_KEYS if seen.get(k) != score.get(k)]


def pick_action(root: Path, observation: dict | None) -> dict:
    """Choose from the fixed local action menu, never from free-form text."""
    score = load_optional_json(root / "state/HARNESS_SCORECARD.json")
    status = load_optional_json(root / "state/FRIDAY_MACHINE_STATUS.json")
    policy = load_optional_json(root / "config/friday_automation_policy.json")
    if not (score and policy):
        return {"action": "BLOCKED_MISSING_CANONICAL_INPUT", "reason": "Missing scorecard or operating policy"}
    if policy.get("mode") != "AUTOMATE_UNTIL_OWNER_GATE" or REQUIRED_POLICY_ACTION not in policy.get("automatic_actions", []):
        return {"action": "BLOCKED_POLICY", "reason": "Automatic owner-view maintenance not authorized"}
    mismatch = score_disagreement(status, score)
    if mismatch:
        return {"action": "REPAIR_DERIVED_OWNER_STATUS", "fields": mismatch}
    rows = (observation or {}).get("components")
    if isinstance(rows, list):
        drift = next((r for r in rows if isinstance(r, dict) and r.get("state") == "RECONCILIATION_REQUIRED"), None)
        if drift:
            return {"action": "TRIAGE_APPROVED_REF_DRIFT",
                    "role": drift.get("role", "UNKNOWN"), "repo": drift.get("repo", "UNKNOWN")}
    return {"action": "VERIFY_EXISTING_MACHINE_CONTINUITY",
            "reason": "No allowed repair is required based on the available evidence"}


def write_status(root: Path, observation: dict | None) -> None:
    state = root / "state"
    status = build_status(root, observation)
    md = render_markdown(status)
    # Only generated view files; never rewrite CURRENT_PROJECT, pinned refs, or ledgers.
    for name, body in (("FRIDAY_MACHINE_STATUS.json", json.dumps(status, indent=2, ensure_ascii=False) + "\n"),
                       ("FRIDAY_MACHINE_STATUS.md", md)):
        target = state / name
        tmp = state / (name + ".friday-tmp")
        tmp.write_text(body, encoding="utf-8")
        os.replace(tmp, target)


def operate(root: Path = ROOT, observation: dict | None = None) -> dict:
    receipt = {
        "schema_version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operator": "FRIDAY_BOUNDED_HARNESS_OPERATOR",
        "scope": "EXISTING_HARNESS_MAINTENANCE_ONLY",
        "authority_changed": False,
        "other_repo_changed": False,
        "production_changed": False,
        "secret_values_accessed": False,
        "live_external_job_dispatched": False,
    }
    errors = validate(root)
    if errors:
        receipt.update(verdict="BLOCKED_AUTHORITY", action="NONE", details=errors[:8],
                       next_action="Repair canonical authority/projection discrepancy before action")
        return receipt
    decision = pick_action(root, observation)
    receipt["decision"] = decision
    action = decision["action"]
    if action.startswith("BLOCKED"):
        receipt.update(verdict=action, action="NONE", proof="FAIL_CLOSED")
    elif action == "REPAIR_DERIVED_OWNER_STATUS":
        write_status(root, observation)
        score = load_optional_json(root / "state/HARNESS_SCORECARD.json") or {}
        status = load_optional_json(root / "state/FRIDAY_MACHINE_STATUS.json")
        disagreement = score_disagreement(status, score)
        receipt.update(action=action, changed_paths=[
            "state/FRIDAY_MACHINE_STATUS.json", "state/FRIDAY_MACHINE_STATUS.md"],
            proof="INDEPENDENT_SCORE_STATUS_RECHECK",
            verdict="PASS_REPAIRED" if not disagreement else "FAILED_REPAIR",
            remaining_mismatches=disagreement)
    elif action == "TRIAGE_APPROVED_REF_DRIFT":
        # A new head is candidate evidence, never permission to change authority.
        receipt.update(action=action, verdict="PASS_TRIAGED_REQUIRES_REVIEW",
                       proof="OBSERVED_REF_MISMATCH_WITH_CANONICAL_AUTHORITY",
                       changed_paths=[],
                       next_action="Review the exact approved-vs-observed delta through existing GitHub tools; no silent merge or repin")
    else:
        # The authority validator has already run, not just a status file check.
        receipt.update(action=action, verdict="PASS_VALIDATED_NO_SAFE_CHANGE",
                       proof="AUTHORITY_SPINE_VALIDATION", changed_paths=[],
                       next_action="Continue the existing approved work order within its owner gates")
    return receipt


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--observation", type=Path)
    p.add_argument("--receipt", type=Path, default=Path("friday-operator/receipt.json"))
    args = p.parse_args()
    observation = load_optional_json(args.observation) if args.observation else None
    result = operate(ROOT, observation)
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"FRIDAY operator: {result['verdict']} | {result['action']}")
    return 0 if result["verdict"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
