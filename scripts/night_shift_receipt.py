#!/usr/bin/env python3
"""Render an honest read-only FRIDAY Night Shift CI receipt from step outcomes and status.

Green tests and reconciled remote authority are independent facts. This helper is
a reporting surface, not an authority promotion, job dispatcher or provider client.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Mapping

CHECK_KEYS = (
    ("Authority guard", "AUTHORITY_RESULT"),
    ("Continuity projection", "CONTINUITY_RESULT"),
    ("Full Harness regression", "REGRESSION_RESULT"),
    ("Remote-ref observation (read-only)", "OBSERVATION_RESULT"),
    ("FRIDAY control-plane test", "CONTROL_PLANE_RESULT"),
    ("Owner status rendering", "RENDER_RESULT"),
    ("Rendered-status validation", "VALIDATION_RESULT"),
)
REMOTE_LABEL = "Remote-ref observation (read-only)"
VALID_REMOTE = {"RECONCILIATION_REQUIRED", "PARTIAL_UNKNOWN", "CURRENTLY_RECONCILED", "NOT_SUPPLIED"}


def safe_status(path: Path) -> dict[str, Any] | None:
    """Fail closed for absent, malformed or unrecognized generated status."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return None
    if not isinstance(data, dict):
        return None
    return data


def report(checks: Mapping[str, str], status: dict[str, Any] | None) -> dict[str, Any]:
    required = [key for key, _ in CHECK_KEYS if key != REMOTE_LABEL]
    passed = all(checks.get(key) == "success" for key in required)
    remote = (status or {}).get("remote_authority_observation") or {}
    state = remote.get("state") if isinstance(remote, dict) else None
    if state not in VALID_REMOTE or checks.get(REMOTE_LABEL) != "success":
        # A failed observation cannot prove a stale generated status is current.
        state = "UNKNOWN"
    if not passed or status is None:
        verdict = "FAILED_OR_INCOMPLETE"
    elif state == "RECONCILIATION_REQUIRED":
        verdict = "TESTS_PASS__RECONCILIATION_REQUIRED"
    elif state in {"PARTIAL_UNKNOWN", "NOT_SUPPLIED", "UNKNOWN"}:
        verdict = "TESTS_PASS__REMOTE_UNVERIFIED"
    else:
        verdict = "TESTS_PASS__CURRENTLY_RECONCILED"
    gate = (status or {}).get("current_gate") or {}
    blockers = (status or {}).get("blockers") or {}
    return {
        "verdict": verdict,
        "remote_state": state,
        "reconciliation_required": remote.get("reconciliation_required", 0) if isinstance(remote, dict) else 0,
        "remote_unknown": remote.get("unknown", 0) if isinstance(remote, dict) else 0,
        "active_gate": gate.get("gate_id", "UNKNOWN") if isinstance(gate, dict) else "UNKNOWN",
        "owner_gates": len(blockers.get("owner_gate", [])) if isinstance(blockers, dict) else 0,
    }


def render(checks: Mapping[str, str], status: dict[str, Any] | None, env: Mapping[str, str]) -> str:
    result = report(checks, status)
    repo = env.get("GITHUB_REPOSITORY", "UNKNOWN")
    run_id = env.get("GITHUB_RUN_ID", "UNKNOWN")
    sha = env.get("GITHUB_SHA", "UNKNOWN")
    lines = [
        "# FRIDAY Night Shift - GitHub verification receipt",
        "",
        f"- **Verdict:** {result['verdict']}",
        f"- **Repository SHA:** {sha}",
        f"- **Run:** https://github.com/{repo}/actions/runs/{run_id}",
        f"- **Trigger:** {env.get('GITHUB_EVENT_NAME', 'UNKNOWN')}",
        "- **Production writes / secrets / live job dispatch:** NONE",
        "- **Reference changes:** observed only, not promoted",
        "- **Runtime proof:** NOT CLAIMED",
        f"- **Remote authority:** {result['remote_state']}",
        f"- **Remote refs needing reconciliation:** {result['reconciliation_required']}",
        f"- **Remote refs unknown:** {result['remote_unknown']}",
        f"- **Canonical next gate:** {result['active_gate']}",
        f"- **Owner-gated blockers still open:** {result['owner_gates']}",
        "",
        "## Checks",
        "",
    ]
    lines.extend(f"- **{name}:** {checks.get(name, 'missing')}" for name, _ in CHECK_KEYS)
    lines.extend(["", "## Next step", ""])
    if result["verdict"] == "FAILED_OR_INCOMPLETE":
        lines.append("Inspect the first failing GitHub job step. Repair that layer only; do not promote any authority.")
    elif result["remote_state"] == "RECONCILIATION_REQUIRED":
        lines.append("Tests passed, but approved versus observed refs diverged. Inspect receipts; NEVER auto-promote a branch SHA.")
    elif result["remote_state"] != "CURRENTLY_RECONCILED":
        lines.append("Tests passed; remote authority is partly unknown/not supplied. Recheck with correct read access before action.")
    else:
        lines.append("Tests and observed remote refs agree; stay at the canonical owner gate. No live proof or auto-dispatch implied.")
    if checks.get(REMOTE_LABEL) != "success":
        lines.append("Remote observation step itself did not succeed; provider/repo reachability remains UNKNOWN.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    env = os.environ
    checks = {name: env.get(key, "missing") for name, key in CHECK_KEYS}
    status = safe_status(Path("state/FRIDAY_MACHINE_STATUS.json"))
    output = render(checks, status, env)
    Path("night-shift").mkdir(exist_ok=True)
    Path("night-shift/receipt.md").write_text(output, encoding="utf-8")
    summary = env.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
