#!/usr/bin/env python3
"""Fail closed when Harness continuity surfaces disagree.

This is intentionally boring. It uses only the Python standard library and
checks the small set of files that agents are expected to trust when resuming
work. If these pointers disagree, the machine must stop and repair authority
before planning or building.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROLE_KEYS = {
    "governance": ("repo", "branch"),
    "factory": ("repo", "branch", "sha"),
    "runtime": ("repo", "branch", "sha"),
    "salvage": ("repo", "branch", "sha"),
    "cockpit": ("repo", "branch", "sha"),
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _canonical_refs(current: dict[str, Any]) -> dict[str, dict[str, Any]]:
    refs: dict[str, dict[str, Any]] = {}
    for role, keys in ROLE_KEYS.items():
        src = current["authority"][role]
        entry: dict[str, Any] = {"role": role}
        for key in keys:
            if key in src:
                entry["ref" if key == "branch" else key] = src[key]
        refs[role] = entry
    return refs


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    state = root / "state"
    current = load_json(state / "CURRENT_PROJECT.json")
    active = load_json(state / "ACTIVE_WORK_ORDER.json")
    ecosystem = load_json(state / "ECOSYSTEM_AUTHORITY_INDEX.json")

    if active.get("source_project_state_path") != "state/CURRENT_PROJECT.json":
        errors.append("ACTIVE_WORK_ORDER.json must point to state/CURRENT_PROJECT.json")

    for key in ("active_project", "lane", "next_action"):
        if active.get(key) != current.get(key):
            errors.append(
                f"ACTIVE_WORK_ORDER.json {key!r} disagrees with CURRENT_PROJECT.json"
            )

    if active.get("evidence_state") != current.get("evidence_state"):
        errors.append(
            "ACTIVE_WORK_ORDER.json evidence_state disagrees with CURRENT_PROJECT.json"
        )

    project_index = (root / "projects" / "PROJECT_INDEX.md").read_text(encoding="utf-8")
    required_heading = f"### {current['active_project']}"
    if required_heading not in project_index:
        errors.append(
            f"PROJECT_INDEX.md is missing active project heading: {required_heading}"
        )

    active_md = (state / "ACTIVE_WORK_ORDER.md").read_text(encoding="utf-8")
    if f"Project: `{current['active_project']}`" not in active_md:
        errors.append("ACTIVE_WORK_ORDER.md does not name CURRENT_PROJECT active_project")
    if "State source: `state/CURRENT_PROJECT.json`" not in active_md:
        errors.append("ACTIVE_WORK_ORDER.md does not declare CURRENT_PROJECT as state source")

    foundation = ecosystem.get("active_foundation_v0")
    if not isinstance(foundation, dict):
        errors.append("ECOSYSTEM_AUTHORITY_INDEX.json missing active_foundation_v0")
    else:
        actual = {
            item.get("role"): item
            for item in foundation.get("canonical_refs", [])
            if isinstance(item, dict) and item.get("role")
        }
        expected = _canonical_refs(current)
        for role, exp in expected.items():
            got = actual.get(role)
            if got is None:
                errors.append(f"ECOSYSTEM authority missing canonical role {role}")
                continue
            for key, value in exp.items():
                if got.get(key) != value:
                    errors.append(
                        f"ECOSYSTEM authority {role}.{key}={got.get(key)!r} "
                        f"but CURRENT_PROJECT says {value!r}"
                    )

        if foundation.get("next") != current.get("next_action"):
            errors.append(
                "ECOSYSTEM active_foundation_v0.next disagrees with CURRENT_PROJECT.next_action"
            )

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("AUTHORITY_SPINE: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("AUTHORITY_SPINE: PASS")
    print("Current project, active work order, project index, and ecosystem pointers agree.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
