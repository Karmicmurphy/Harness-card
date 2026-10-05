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
    states = [str(row.get("state", "UNKNOWN")) for row in rows]
    reconciliation = sum(s == "RECONCILIATION_REQUIRED" for s in states)
    unknown = sum(s == "UNKNOWN" for s in states)
    match = sum(s in {"MATCH", "OBSERVED_GOVERNANCE"} for s in states)
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


def build_status(root: Path = ROOT, observation: dict[str, Any] | None = None) -> dict[str, Any]:
    current = load_json(root / "state/CURRENT_PROJECT.json")
    score = load_json(root / "state/HARNESS_SCORECARD.json")
    policy = load_json(root / "config/friday_automation_policy.json")
    learning = load_json(root / "state/LEARNING_CANDIDATES.json")

    work = current["work_order"]
    owner_blockers, automatic_blockers = split_blockers(
        list(work.get("blockers", [])), list(policy.get("owner_gate_markers", []))
    )
    remote = observation_summary(observation)
    surface = automation_surface(root)
    surface_ready = all(surface.values())
    next_action = choose_next_action(remote["state"], automatic_blockers, owner_blockers)

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
        "automation_mode": policy.get("mode"),
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
            "weird_salvage_count": score.get("weird_salvage_count"),
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
        f"- **Project:** {status['active_project']}",
        f"- **Evidence:** {status['evidence_state']}",
        f"- **Lane:** {status['lane']}",
        f"- **Automation:** {status['automation_mode']}",
        f"- **Remote state:** {remote['state']}",
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
        f"- Durable learned rules: **{status['self_improvement']['learned_rule_count']}**",
        f"- Weird salvage items: **{status['self_improvement']['weird_salvage_count']}**",
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
