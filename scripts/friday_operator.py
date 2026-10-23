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
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_authority_spine import validate  # noqa: E402
from friday_control_plane import build_status, render_markdown  # noqa: E402
from foundation_state import github_get  # noqa: E402

SCORE_KEYS = ("incident_count", "learned_rule_count",
              "closed_incident_rule_count", "unresolved_incident_prevention_count")
REQUIRED_POLICY_ACTION = "refresh owner-readable machine status"
MAX_REPAIR_ATTEMPTS = 3
HISTORY_FILE = "FRIDAY_OPERATOR_REPAIR_HISTORY.json"
HISTORY_LIMIT = 50
HISTORY_ACTIONS = {"REPAIR_DERIVED_OWNER_STATUS", "TRIAGE_APPROVED_REF_DRIFT",
                   "VERIFY_EXISTING_MACHINE_CONTINUITY", "NONE"}


def repair_with_proof(root: Path, observation: dict | None, *, max_attempts: int = MAX_REPAIR_ATTEMPTS) -> dict:
    """Retry only the known reversible status render; never arbitrary jobs.

    A semantic mismatch is NOT transient: record it and stop. I/O faults are
    retried a bounded number of times; each attempt leaves a sanitized result.
    """
    if not 1 <= max_attempts <= MAX_REPAIR_ATTEMPTS:
        raise ValueError("repair retries must be within the approved limit")
    attempts: list[dict] = []
    for number in range(1, max_attempts + 1):
        try:
            write_status(root, observation)
            score = load_optional_json(root / "state/HARNESS_SCORECARD.json") or {}
            status = load_optional_json(root / "state/FRIDAY_MACHINE_STATUS.json")
            disagreement = score_disagreement(status, score)
            if not disagreement:
                attempts.append({"attempt": number, "result": "PASS_INDEPENDENT_RECHECK"})
                return {"verdict": "PASS_REPAIRED", "attempts": attempts,
                        "remaining_mismatches": [], "stopped_reason": "PROOF_PASSED"}
            attempts.append({"attempt": number, "result": "FAILED_SEMANTIC_RECHECK",
                             "remaining_mismatches": disagreement})
            return {"verdict": "FAILED_REPAIR", "attempts": attempts,
                    "remaining_mismatches": disagreement,
                    "stopped_reason": "NON_RETRYABLE_SEMANTIC_FAILURE"}
        except OSError:
            attempts.append({"attempt": number, "result": "RETRYABLE_LOCAL_IO_FAILURE"})
        except (ValueError, KeyError, TypeError):
            attempts.append({"attempt": number, "result": "BLOCKED_INVALID_STATE"})
            return {"verdict": "FAILED_REPAIR", "attempts": attempts,
                    "remaining_mismatches": [], "stopped_reason": "INVALID_INPUT_NO_RETRY"}
    return {"verdict": "FAILED_REPAIR", "attempts": attempts,
            "remaining_mismatches": [], "stopped_reason": "RETRY_BUDGET_EXHAUSTED"}


def preserve_sanitized_repair_history(root: Path, receipt: dict) -> None:
    """Record outcomes only; never import user requests, secrets or remote content."""
    state = root / "state"
    path = state / HISTORY_FILE
    prior = load_optional_json(path) if path.exists() else None
    if path.exists() and (
        not isinstance(prior, dict)
        or prior.get("schema_version") != "1.0.0"
        or not isinstance(prior.get("runs"), list)
    ):
        raise ValueError("repair history is malformed; refuse to overwrite")
    rows = list((prior or {}).get("runs", []))
    run_id = str(receipt.get("github_run_id", "UNKNOWN"))
    if not re.fullmatch(r"[0-9]{1,24}", run_id):
        raise ValueError("only validated CI run IDs may enter repair history")
    action = receipt.get("action", "NONE")
    if action not in HISTORY_ACTIONS:
        raise ValueError("unrecognized action cannot enter learning history")
    verdict = str(receipt.get("verdict", "UNKNOWN"))
    if not (verdict.startswith(("PASS_", "BLOCKED_", "FAILED_"))):
        raise ValueError("unrecognized outcome cannot enter learning history")
    attempts = receipt.get("repair_attempts", [])
    if not isinstance(attempts, list) or len(attempts) > MAX_REPAIR_ATTEMPTS:
        raise ValueError("invalid bounded attempt count")
    event = {
        "run_id": run_id,
        "action": action,
        "verdict": verdict,
        "attempt_count": len(attempts),
        "attempt_outcomes": [str(a.get("result", "UNKNOWN")) for a in attempts],
        "proof": str(receipt.get("proof", "NONE"))[:100],
        "stopped_reason": str(receipt.get("repair_stop_reason", "NONE"))[:100],
    }
    # A CI rerun is one history identity, not fake repeatability evidence.
    rows = [x for x in rows if isinstance(x, dict) and x.get("run_id") != run_id]
    rows.append(event)
    path.parent.mkdir(parents=True, exist_ok=True)
    staged = path.with_suffix(".friday-tmp")
    staged.write_text(json.dumps({"schema_version": "1.0.0", "privacy": "SANITIZED_CI_OUTCOMES_ONLY",
                                  "runs": rows[-HISTORY_LIMIT:]}, indent=2) + "\n", encoding="utf-8")
    os.replace(staged, path)



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


def inspect_approved_ref_delta(root: Path, observation: dict | None, decision: dict, get=github_get) -> dict:
    """Read actual GitHub compare metadata for ONE approved vs observed ref.

    No code checkout, branch update, production action, or automatic SHA promotion.
    Fail closed if the observation does not match Harness authority.
    """
    current = load_optional_json(root / "state/CURRENT_PROJECT.json") or {}
    role = decision.get("role")
    canonical = (current.get("authority") or {}).get(role, {})
    row = next((r for r in (observation or {}).get("components", [])
                if isinstance(r, dict) and r.get("role") == role), None)
    if not row or row.get("repo") != canonical.get("repo"):
        return {"verdict": "BLOCKED_AUTHORITY_MISMATCH"}
    approved, observed = row.get("approved_sha"), row.get("observed_sha")
    if approved != canonical.get("sha") or not all(
        isinstance(s, str) and re.fullmatch(r"[0-9a-f]{40}", s)
        for s in (approved, observed)
    ):
        return {"verdict": "BLOCKED_UNVERIFIED_REFS"}
    try:
        response = get(f"{canonical['repo']}/compare/{approved}...{observed}")
        if not isinstance(response, dict) or not isinstance(response.get("files"), list):
            raise ValueError("GitHub compare not complete")
        files = response["files"]
        if len(files) > 300 or any(not isinstance(x, dict) or not isinstance(x.get("filename"), str)
                                   for x in files):
            raise ValueError("GitHub compare files invalid or truncated")
        return {
            "verdict": "PASS_DELTA_INSPECTED_REQUIRES_REVIEW",
            "ahead_by": response.get("ahead_by"),
            "behind_by": response.get("behind_by"),
            "changed_files": [x["filename"] for x in files],
            "approved_sha": approved,
            "observed_sha": observed,
            "files_inspected_count": len(files),
            "no_auto_promotion": True,
        }
    except (OSError, ValueError, KeyError, TypeError):
        return {"verdict": "BLOCKED_REMOTE_DELTA_UNAVAILABLE", "no_auto_promotion": True}


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
        "github_run_id": os.environ.get("GITHUB_RUN_ID", "LOCAL_TEST"),
        "github_source_sha": os.environ.get("GITHUB_SHA", "LOCAL_TEST"),
        "github_event": os.environ.get("GITHUB_EVENT_NAME", "LOCAL_TEST"),
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
        proof = repair_with_proof(root, observation)
        receipt.update(action=action, changed_paths=[
            "state/FRIDAY_MACHINE_STATUS.json", "state/FRIDAY_MACHINE_STATUS.md"],
            proof="INDEPENDENT_SCORE_STATUS_RECHECK",
            verdict=proof["verdict"], repair_attempts=proof["attempts"],
            repair_stop_reason=proof["stopped_reason"],
            remaining_mismatches=proof["remaining_mismatches"],
            next_action=("Continue scheduled safe verification"
                         if proof["verdict"] == "PASS_REPAIRED"
                         else "Stop after bounded attempts; review exact failing render/proof before changing implementation"))
    elif action == "TRIAGE_APPROVED_REF_DRIFT":
        # A new head is candidate evidence, never permission to change authority.
        delta = inspect_approved_ref_delta(root, observation, decision)
        receipt.update(action=action, verdict=delta["verdict"],
                       proof="READ_ONLY_GITHUB_COMPARE_OF_EXACT_CANONICAL_VS_BRANCH_REFS",
                       changed_paths=[],
                       inspected_delta=delta,
                       next_action="Use this exact delta as evidence for one scoped candidate decision; never silently merge or repin")
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
    # Preserve the exact machine-owned action receipt in canonical Harness history
    # on the existing GitHub main-branch status-writer run only.
    if os.environ.get("GITHUB_REF") == "refs/heads/main" and os.environ.get("GITHUB_ACTIONS") == "true":
        (ROOT / "state/FRIDAY_OPERATOR_LAST_RUN.json").write_text(
            json.dumps(result, indent=2) + "\n", encoding="utf-8"
        )
        preserve_sanitized_repair_history(ROOT, result)

    print(f"FRIDAY operator: {result['verdict']} | {result['action']}")
    return 0 if result["verdict"].startswith("PASS_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
