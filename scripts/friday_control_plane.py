#!/usr/bin/env python3
"""Build FRIDAY's owner-readable automation/control-plane status from canonical state.

This script does not promote authority, execute live work, read secret values, or mutate
other repositories. It turns existing Harness evidence into one deterministic owner view.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state"
CONFIG = ROOT / "config"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def owner_access_profile(root: Path) -> dict[str, Any]:
    """Non-sensitive owner interaction environment; never an authorization grant."""
    profile = load_json(root / "config/owner_access_profile.json")
    if profile.get("schema_version") != "1.0.0":
        raise ValueError("unsupported owner access profile version")
    if profile.get("mode") != "PHONE_ONLY":
        raise ValueError("unsupported owner access mode")
    if profile.get("platform") != "ANDROID_PHONE" or profile.get("pc_required") is not False:
        raise ValueError("phone-only profile cannot require PC")
    return profile


def split_blockers(blockers: list[str], markers: list[str]) -> tuple[list[str], list[str]]:
    owner: list[str] = []
    automatic: list[str] = []
    upper_markers = [m.upper() for m in markers]
    for blocker in blockers:
        upper = blocker.upper()
        if any(marker in upper for marker in upper_markers):
            owner.append(blocker)
        else:
            automatic.append(blocker)
    return owner, automatic


def observation_summary(observation: dict[str, Any] | None) -> dict[str, Any]:
    if not observation:
        return {
            "state": "NOT_SUPPLIED",
            "match": 0,
            "reconciliation_required": 0,
            "unknown": 0,
            "components": [],
        }
    rows = observation.get("components", [])
    # A successful HTTP/observation step with zero usable component rows
    # is not evidence that the approved remote revisions match.
    if not isinstance(rows, list) or not rows:
        return {
            "state": "NOT_SUPPLIED",
            "observed_at": observation.get("observed_at"),
            "match": 0,
            "reconciliation_required": 0,
            "unknown": 0,
            "components": [],
        }
    if any(not isinstance(row, dict) for row in rows):
        return {
            "state": "PARTIAL_UNKNOWN",
            "observed_at": observation.get("observed_at"),
            "match": 0,
            "reconciliation_required": 0,
            "unknown": len(rows),
            "components": rows,
        }
    expected_roles = {"governance", "factory", "runtime", "salvage", "cockpit"}
    observed_roles = [row.get("role") for row in rows]
    # Missing or duplicate roles and unexpected enum values cannot prove all
    # canonical sources are reconciled, even if every reported row says MATCH.
    missing = expected_roles - set(role for role in observed_roles if isinstance(role, str))
    duplicate_count = len(observed_roles) - len(set(str(role) for role in observed_roles))
    states = [str(row.get("state", "UNKNOWN")) for row in rows]
    allowed = {"MATCH", "OBSERVED_GOVERNANCE", "RECONCILIATION_REQUIRED", "UNKNOWN"}
    reconciliation = sum(state == "RECONCILIATION_REQUIRED" for state in states)
    unknown = sum(state not in allowed or state == "UNKNOWN" for state in states) + len(missing) + duplicate_count
    match = sum(state in {"MATCH", "OBSERVED_GOVERNANCE"} for state in states)
    if reconciliation:
        state = "RECONCILIATION_REQUIRED"
    elif unknown:
        state = "PARTIAL_UNKNOWN"
    else:
        state = "CURRENTLY_RECONCILED"
    return {
        "state": state,
        "observed_at": observation.get("observed_at"),
        "match": match,
        "reconciliation_required": reconciliation,
        "unknown": unknown,
        "components": rows,
    }


def learning_summary(learning: dict[str, Any]) -> dict[str, Any]:
    rows = learning.get("candidates", [])
    allowed = {"CANDIDATE", "PROVEN", "REJECTED", "RETIRED"}
    bad = [row.get("id", "UNKNOWN") for row in rows if row.get("status") not in allowed]
    if bad:
        raise ValueError(f"invalid learning candidate status: {', '.join(bad)}")
    counts = {status: 0 for status in sorted(allowed)}
    for row in rows:
        counts[row["status"]] += 1
    return {
        "scope": "DURABLE_SANITIZED_HARNESS_INPUTS_NOT_RAW_CHAT",
        "candidate_count": len(rows),
        "status_counts": counts,
        "proven_rules_eligible": counts["PROVEN"],
    }


def automation_surface(root: Path) -> dict[str, bool]:
    required = {
        "authority_guard": root / ".github/workflows/authority-spine-guard.yml",
        "self_improvement_worker": root / ".github/workflows/self-improve.yml",
        "drift_observer": root / ".github/workflows/foundation-observe.yml",
        "continuity_renderer": root / "scripts/foundation_state.py",
        "automation_policy": root / "config/friday_automation_policy.json",
        "learning_inbox": root / "state/LEARNING_CANDIDATES.json",
        "constraint_breaker": root / "skills/constraint-breaker-lab/SKILL.md",
    }
    return {name: path.exists() for name, path in required.items()}


def choose_next_action(remote_state: str, automatic_blockers: list[str], owner_blockers: list[str]) -> str:
    if remote_state == "RECONCILIATION_REQUIRED":
        return "RECONCILE_REMOTE_STATE_BEFORE_MUTATION"
    if automatic_blockers:
        return "AUTOMATE_BOUNDED_BLOCKER_REPAIR_AND_PROOF"
    if owner_blockers:
        return "STOP_AT_OWNER_GATE_WITH_PRECISE_REQUEST"
    return "RUN_NEXT_BOUNDED_PROOF"


def delivery_readiness(current: dict[str, Any], owner_blockers: list[str], operator_receipt: dict | None = None) -> dict[str, str]:
    """Describe the owner's real path; never infer delivery from CI or installed files."""
    gate = current.get("work_order", {}).get("gate_id")
    evidence = current.get("evidence_state")
    if gate == "FRIDAY_BOUNDED_OPERATOR_LOOP":
        r = operator_receipt or {}
        proven = (
            r.get("operator") == "FRIDAY_BOUNDED_HARNESS_OPERATOR"
            and r.get("scope") == "EXISTING_HARNESS_MAINTENANCE_ONLY"
            and str(r.get("verdict", "")).startswith("PASS_")
            and bool(r.get("github_run_id"))
            and r.get("github_run_id") != "LOCAL_TEST"
            and all(r.get(flag) is False for flag in
                    ("authority_changed", "other_repo_changed", "production_changed",
                     "secret_values_accessed", "live_external_job_dispatched"))
        )
        return {
            "state": "BOUNDED_OPERATOR_RUN_PROVEN" if proven else "OPERATOR_RUN_RECEIPT_PENDING",
            "proof": "CI_BOUNDED_OPERATOR_ONLY_NOT_GENERAL_FRIDAY_MCP" if proven else "FIRST_REAL_OPERATOR_RUN_NOT_YET_PROVEN",
            "one_next_owner_action": "None for preauthorized safe machine maintenance; consequential external actions still need applicable approval.",
            "machine_next_action": "Continue the existing FRIDAY operator action/verification/learning loop and independently review receipts.",
        }
    if gate == "PAGES_BOUNDED_JOB_ROUND_TRIP":
        if any("PREVIEW_FOUNDATION_GITHUB_TOKEN_AND_FOUNDATION_OWNER_SUB_ABSENT" in b for b in owner_blockers):
            return {
                "state": "BLOCKED_PREVIEW_CREDENTIALS",
                "proof": "ANDROID_TO_FOUNDRY_TO_PHONE_NOT_PROVEN",
                "one_next_owner_action": "Securely configure the two existing protected Preview bindings in Cloudflare; do not put values in Chat or GitHub.",
                "machine_next_action": "After bindings are verified, inspect a fresh exact-source Preview deployment and owner authentication before requesting fixture dispatch.",
            }
        if owner_blockers:
            return {
                "state": "BLOCKED_OWNER_GATE",
                "proof": "ANDROID_TO_FOUNDRY_TO_PHONE_NOT_PROVEN",
                "one_next_owner_action": "Resolve only the currently authorized owner gate recorded in CURRENT_PROJECT; do not bypass it.",
                "machine_next_action": "Resume the bounded phone proof after independent readiness checks.",
            }
        return {
            "state": "PHONE_PROOF_REQUIRED",
            "proof": "ANDROID_TO_FOUNDRY_TO_PHONE_NOT_PROVEN",
            "one_next_owner_action": "No new owner task until the existing bounded proof requires an explicit approval.",
            "machine_next_action": "Verify the exact-source deployed app and correlated proof on Android; do not assume deployment equals success.",
        }
    if evidence == "PROVEN_LIVE":
        return {
            "state": "RECORDED_LIVE_PROOF_REVERIFY_ON_CHANGE",
            "proof": "CANONICAL_EVIDENCE_ONLY",
            "one_next_owner_action": "None unless the current job requires approval.",
            "machine_next_action": "Recheck runtime proof when the code, deployment, or target device changes.",
        }
    return {
        "state": "USER_PATH_NOT_PROVEN",
        "proof": "CANONICAL_EVIDENCE_ONLY",
        "one_next_owner_action": "Only the exact owner approval required by the active work order.",
        "machine_next_action": "Prove the existing user path before calling the machine operational.",
    }


def build_status(root: Path = ROOT, observation: dict[str, Any] | None = None) -> dict[str, Any]:
    current = load_json(root / "state/CURRENT_PROJECT.json")
    score = load_json(root / "state/HARNESS_SCORECARD.json")
    policy = load_json(root / "config/friday_automation_policy.json")
    learning = load_json(root / "state/LEARNING_CANDIDATES.json")
    access = owner_access_profile(root)

    work = current["work_order"]
    owner_blockers, automatic_blockers = split_blockers(
        list(work.get("blockers", [])), list(policy.get("owner_gate_markers", []))
    )
    remote = observation_summary(observation)
    surface = automation_surface(root)
    surface_ready = all(surface.values())
    next_action = choose_next_action(remote["state"], automatic_blockers, owner_blockers)

    try:
        operator_receipt = load_json(root / "state/FRIDAY_OPERATOR_LAST_RUN.json")
    except (OSError, ValueError):
        operator_receipt = None
    delivery = delivery_readiness(current, owner_blockers, operator_receipt)

    generated_candidates = learning_summary(learning)
    generated_at = (
        remote.get("observed_at")
        or score.get("generated_at")
        or datetime.now(timezone.utc).isoformat()
    )

    return {
        "schema_version": "1.0.0",
        "generated_at": generated_at,
        "active_project": current.get("active_project"),
        "evidence_state": current.get("evidence_state"),
        "lane": current.get("lane"),
        "machine_state": "READY_FOR_BOUNDED_AUTOMATION" if surface_ready else "AUTOMATION_SPINE_INCOMPLETE",
        "delivery_readiness": delivery,
        "operator_last_run": {
            "action": (operator_receipt or {}).get("action", "NOT_RUN"),
            "verdict": (operator_receipt or {}).get("verdict", "NOT_RUN"),
            "github_run_id": (operator_receipt or {}).get("github_run_id", "UNKNOWN"),
            "receipt_path": "state/FRIDAY_OPERATOR_LAST_RUN.json" if operator_receipt else None,
        },
        "automation_mode": policy.get("mode"),
        "owner_access": {
            "recent_continuity_path": "state/FRIDAY_RECENT_CONTINUITY_2026-10-18.md" if (root / "state/FRIDAY_RECENT_CONTINUITY_2026-10-18.md").is_file() else None,
            "recent_continuity_state": "FILE_PRESENT_RUNTIME_INGESTION_UNPROVEN" if (root / "state/FRIDAY_RECENT_CONTINUITY_2026-10-18.md").is_file() else "UNAVAILABLE",
            "mode": access["mode"],
            "platform": access["platform"],
            "pc_required": access["pc_required"],
            "source": access["source"],
            "resume_path": "state/FRIDAY_PHONE_ONLY_RECOVERY_2026-10-15.md",
        },
        "automation_surface": surface,
        "current_gate": {
            "gate_id": work.get("gate_id"),
            "status": work.get("status"),
            "stop_condition": work.get("stop_condition"),
            "canonical_next_action": current.get("next_action"),
        },
        "blockers": {
            "automatic": automatic_blockers,
            "owner_gate": owner_blockers,
            "owner_attention_required": bool(owner_blockers),
        },
        "remote_authority_observation": remote,
        "learning": generated_candidates,
        "self_improvement": {
            "incident_count": score.get("incident_count"),
            "learned_rule_count": score.get("learned_rule_count"),
            "closed_incident_rule_count": score.get("closed_incident_rule_count"),
            "unresolved_incident_prevention_count": score.get("unresolved_incident_prevention_count"),
            "weird_salvage_count": score.get("weird_salvage_count"),
            "friday_operator_outcomes": score.get("friday_operator_learning"),
            "learning_contract": "PROVEN generalized candidates may join generated rules; raw private chat is not automatically ingested.",
        },
        "policy": {
            "automatic_actions": policy.get("automatic_actions", []),
            "owner_gate_actions": policy.get("owner_gate_actions", []),
            "never_automatic": policy.get("never_automatic", []),
        },
        "next_machine_action": next_action,
        "owner_view": {
            "working": [name for name, ok in surface.items() if ok],
            "missing": [name for name, ok in surface.items() if not ok],
            "what_friday_is_doing": next_action,
            "what_friday_needs_from_owner": owner_blockers,
        },
    }


def render_markdown(status: dict[str, Any]) -> str:
    gate = status["current_gate"]
    blockers = status["blockers"]
    remote = status["remote_authority_observation"]
    lines = [
        "# FRIDAY Machine Status",
        "",
        "> AUTO-GENERATED from canonical Harness state. This is the owner view; canonical authority remains in CURRENT_PROJECT.json.",
        "",
        f"- **Machine:** {status['machine_state']}",
        f"- **Active machine execution:** {status['delivery_readiness']['state']} (separate from installed scripts)",
        f"- **Project:** {status['active_project']}",
        f"- **Evidence:** {status['evidence_state']}",
        f"- **Lane:** {status['lane']}",
        f"- **Automation:** {status['automation_mode']}",
        f"- **Remote state:** {remote['state']}",
        f"- **Owner environment:** {status['owner_access']['mode']} / {status['owner_access']['platform']}",
        "- **PC required:** NO",
        "",
        "## Phone-only operation",
        "",
        "The owner currently operates from Android without dependable PC access. Use connected Chat tools, GitHub, and provider reads/writes within existing owner gates. Keep local-only Workshop files UNKNOWN/UNAVAILABLE; never invent them.",
        "Read [phone-only recovery](FRIDAY_PHONE_ONLY_RECOVERY_2026-10-15.md) when resuming from a phone.",
        "Read [the Oct 15-18 recent continuation](FRIDAY_RECENT_CONTINUITY_2026-10-18.md) **when present**, then verify current provider evidence. A file pointer does not prove a live FRIDAY process consumed it." if status["owner_access"].get("recent_continuity_path") else "Recent continuation capsule unavailable; do not claim it was loaded.",
        "Minimize owner interruption: ask for one exact Android action only when tools cannot cross a genuine permission or real-device proof boundary.",
        "",
        "## What actually works vs. what is still blocked",
        "",
        "Installed scripts or green checks alone never prove operator execution or a working live FRIDAY MCP.",
        f"- **Last bounded FRIDAY action:** {status['operator_last_run']['action']}",
        f"- **Last bounded action verdict:** {status['operator_last_run']['verdict']}",
        f"- **Operator receipt:** {status['operator_last_run']['receipt_path'] or 'NOT YET RECORDED'}",
        f"- **Live-path evidence:** {status['delivery_readiness']['proof']}",
        f"- **Exact owner gate:** {status['delivery_readiness']['one_next_owner_action']}",
        f"- **FRIDAY's next permitted machine move:** {status['delivery_readiness']['machine_next_action']}",
        "",
                "## What FRIDAY is proving now",
        "",
        f"**{gate['gate_id']}** — {gate['status']}",
        "",
        gate["canonical_next_action"] or "No canonical next action recorded.",
        "",
        "## What FRIDAY can handle automatically",
        "",
    ]
    for item in blockers["automatic"]:
        lines.append(f"- {item}")
    if not blockers["automatic"]:
        lines.append("- No current blocker is classified as automatic repair work.")
    lines += ["", "## What actually needs Randy", ""]
    for item in blockers["owner_gate"]:
        lines.append(f"- {item}")
    if not blockers["owner_gate"]:
        lines.append("- Nothing at the current gate.")
    lines += [
        "",
        "## Learning",
        "",
        f"- Documented prevention rules (closed + unresolved): **{status['self_improvement']['learned_rule_count']}**",
        f"- Rules from closed incidents: **{status['self_improvement']['closed_incident_rule_count'] if status['self_improvement']['closed_incident_rule_count'] is not None else 'UNKNOWN UNTIL LEARNER REFRESH'}**",
        f"- Unresolved prevention candidates (not proven fixes): **{status['self_improvement']['unresolved_incident_prevention_count'] if status['self_improvement']['unresolved_incident_prevention_count'] is not None else 'UNKNOWN UNTIL LEARNER REFRESH'}**",
        f"- Weird salvage items: **{status['self_improvement']['weird_salvage_count']}**",
        f"- Bounded FRIDAY operator outcomes (sanitized distinct runs): **{(status['self_improvement'].get('friday_operator_outcomes') or {}).get('runs', 'AWAITING LEARNING RUN')}**",
        f"- Independently verified derived-status fixes: **{(status['self_improvement'].get('friday_operator_outcomes') or {}).get('repaired_runs', 'AWAITING LEARNING RUN')}**",
        f"- Recovered local retry sequences: **{(status['self_improvement'].get('friday_operator_outcomes') or {}).get('retry_recovered_runs', 'AWAITING LEARNING RUN')}**",
        f"- Repair failures requiring review: **{(status['self_improvement'].get('friday_operator_outcomes') or {}).get('failed_repairs', 'AWAITING LEARNING RUN')}**",
        f"- New generalized learning candidates: **{status['learning']['candidate_count']}**",
        f"- Proven candidate rules eligible for promotion: **{status['learning']['proven_rules_eligible']}**",
        "- Raw private chat is not copied automatically into the public Harness.",
        "",
        "## Next machine move",
        "",
        f"**{status['next_machine_action']}**",
        "",
        "## Stop condition",
        "",
        gate["stop_condition"] or "No stop condition recorded.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "status"))
    parser.add_argument("--observation", type=Path)
    args = parser.parse_args()

    observation = None
    if args.observation and args.observation.exists() and args.observation.stat().st_size:
        observation = load_json(args.observation)

    status = build_status(ROOT, observation)
    rendered = render_markdown(status)
    if args.command == "status":
        print(rendered, end="")
        return 0

    (STATE / "FRIDAY_MACHINE_STATUS.json").write_text(
        json.dumps(status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (STATE / "FRIDAY_MACHINE_STATUS.md").write_text(rendered, encoding="utf-8")
    print("FRIDAY control-plane status refreshed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
