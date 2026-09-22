#!/usr/bin/env python3
"""Fail when Harness bootstrap files disagree about current authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    config = load_json("config/harness.json")
    current = load_json("state/CURRENT_PROJECT.json")
    ecosystem = load_json("state/ECOSYSTEM_AUTHORITY_INDEX.json")
    active_order = (ROOT / "state/ACTIVE_WORK_ORDER.md").read_text(encoding="utf-8")
    project_index = (ROOT / "projects/PROJECT_INDEX.md").read_text(encoding="utf-8")

    for path in config.get("bootstrap_files", []):
        if not (ROOT / path).is_file():
            fail(errors, f"missing bootstrap file: {path}")

    active_project = str(current.get("active_project") or "").strip()
    marker = "## PROJECT\n" + active_project
    if not active_project or marker not in active_order:
        fail(errors, "ACTIVE_WORK_ORDER project does not match CURRENT_PROJECT")

    if f"### {active_project}" not in project_index:
        fail(errors, "PROJECT_INDEX does not contain the active project")

    if "PersonalJarvis" in str(current.get("next_action") or ""):
        fail(errors, "current next action illegally depends on PersonalJarvis")

    current_refs = current.get("authority", {})
    ecosystem_refs = {
        item.get("role"): item
        for item in ecosystem.get("active_foundation_v0", {}).get("canonical_refs", [])
    }
    for role in ("factory", "runtime", "salvage", "cockpit"):
        left = current_refs.get(role, {})
        right = ecosystem_refs.get(role, {})
        if left.get("repo") != right.get("repo") or left.get("branch") != right.get("ref"):
            fail(errors, f"authority repo/ref mismatch for {role}")
        if left.get("sha") != right.get("sha"):
            fail(errors, f"authority SHA mismatch for {role}")

    friday = current.get("candidates", {}).get("friday_gateway_v0", {})
    if friday.get("activation") != "NOT_AUTHORIZED":
        fail(errors, "FRIDAY candidate activation must remain NOT_AUTHORIZED")
    if "NOT_THE_LIBRARIAN" not in str(friday.get("relationship") or ""):
        fail(errors, "FRIDAY relationship must explicitly say it is not the librarian")

    result = {
        "verdict": "PASS" if not errors else "FAIL",
        "active_project": active_project,
        "lane": current.get("lane"),
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
