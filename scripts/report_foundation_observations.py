#!/usr/bin/env python3
"""Validate scheduled read-only observations and summarize findings without false CI failures.

A remote UNKNOWN or reviewed-ref drift is an observation, not a script crash.
Bad/missing/malformed evidence is a real workflow failure. Never promote authority.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import sys

ROLES = {"governance", "factory", "runtime", "salvage", "cockpit"}
REF_STATES = {"MATCH", "OBSERVED_GOVERNANCE", "RECONCILIATION_REQUIRED", "UNKNOWN"}
PREVIEW_STATES = {"UNKNOWN", "CONFIG_BLOCKED", "CONFIG_READY_RUNTIME_UNPROVEN"}


def summarize(refs: dict, preview: dict) -> str:
    if not isinstance(refs, dict) or refs.get("schema_version") != "1.0.0":
        raise ValueError("invalid repository observation envelope")
    rows = refs.get("components")
    if not isinstance(rows, list) or len(rows) != len(ROLES):
        raise ValueError("missing/extra repository observation rows")
    if any(not isinstance(row, dict) for row in rows):
        raise ValueError("malformed repository observation row")
    if {row.get("role") for row in rows} != ROLES:
        raise ValueError("duplicate or unknown repository role")
    if any(row.get("state") not in REF_STATES for row in rows):
        raise ValueError("unknown repository observation state")
    if refs.get("authority_changed") is not False:
        raise ValueError("observer cannot change authority")
    if not isinstance(preview, dict) or preview.get("schema_version") != "1.0.0":
        raise ValueError("invalid Preview observation envelope")
    if preview.get("changes_performed") is not False:
        raise ValueError("Preview inspection cannot change resources")
    if preview.get("state") not in PREVIEW_STATES:
        raise ValueError("unknown Preview observation state")

    unknown = any(row["state"] == "UNKNOWN" for row in rows) or preview["state"] == "UNKNOWN"
    drift = any(row["state"] == "RECONCILIATION_REQUIRED" for row in rows)
    blocked = preview["state"] == "CONFIG_BLOCKED"
    disposition = (
        "ATTENTION_REQUIRED" if drift or blocked
        else "UNVERIFIED" if unknown
        else "CONFIG_RECONCILED_NOT_LIVE_PROOF"
    )
    lines = [
        "# Foundation read-only observation receipt", "",
        f"**Disposition: {disposition}**", "",
        "GitHub workflow success means the observer and report ran correctly. "
        "It does NOT mean approved refs, Cloudflare Preview, or live FRIDAY are healthy.", "",
        "| Component | Observed state |",
        "|---|---|",
    ]
    for row in rows:
        lines.append(f"| {row['role']} | {row['state']} |")
    lines.extend([
        "", f"**Pages Preview:** {preview['state']}",
        "",
        "Remote access gaps remain UNKNOWN; branch movement needs review, never automatic repinning. "
        "Do not equate deployment/configuration proof with a working Android-to-FRIDAY job.",
        "",
    ])
    if preview["state"] == "UNKNOWN":
        lines.insert(-2, f"Preview access reason: {preview.get('reason', 'UNKNOWN')}")
    if preview["state"] == "CONFIG_BLOCKED":
        missing = preview.get("required_binding_names_missing", [])
        if not isinstance(missing, list) or any(not isinstance(n, str) for n in missing):
            raise ValueError("malformed Preview binding summary")
        lines.insert(-2, "Missing Preview binding *names* (never values): " + ", ".join(missing or ["UNKNOWN"]))
    return "\n".join(lines)


def main(ref_path: str, preview_path: str) -> int:
    try:
        refs = json.loads(Path(ref_path).read_text(encoding="utf-8"))
        preview = json.loads(Path(preview_path).read_text(encoding="utf-8"))
        receipt = summarize(refs, preview)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"OBSERVATION_RECEIPT_INVALID: {exc}", file=sys.stderr)
        return 2
    print(receipt)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(receipt + "\n")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: report_foundation_observations.py REFS_JSON PREVIEW_JSON")
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
