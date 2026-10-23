#!/usr/bin/env python3
"""Fail-closed, no-network FRIDAY maintenance radar for the EXISTING daily operator.

This is a diagnostics/approval queue, not a general code editor, issue bot or
permission to promote a moving branch. All input evidence comes from the
canonical Harness and the read-only observer. Learn only exact verified refs.
"""
from __future__ import annotations

import json
from pathlib import Path
import re

SCHEMA = "1.0.0"
ROLES = ("factory", "runtime", "salvage", "cockpit")
SHA_RE = re.compile(r"^[a-f0-9]{40}$")
ROLE_SKILLS = {
    "factory": ["artifact-compass", "proof-gate", "rights-gate"],
    "runtime": ["artifact-compass", "proof-gate"],
    "salvage": ["artifact-salvage", "rights-gate", "proof-gate"],
    "cockpit": ["project-context-harvester", "proof-gate"],
}
TERMINAL_TRIAGED = "TRIAGED_REVIEW_REQUIRED"
PENDING = "UNTRIAGED_READ_ONLY"
FAILED_READ = "READ_PROOF_FAILED"
ACCESS = "UNKNOWN_READ_ACCESS"
MATCH = "MATCH"
MAX_READ_ATTEMPTS = 3


class InvalidQueue(ValueError):
    """Do not overwrite malformed state or count its claims as evidence."""


def is_sha(value):
    return isinstance(value, str) and SHA_RE.fullmatch(value) is not None


def load_queue(path: Path) -> dict:
    if not path.exists():
        return {"schema_version": SCHEMA, "scope": "APPROVED_REFS_READ_ONLY", "items": []}
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise InvalidQueue("Existing FRIDAY queue is unreadable; preserve it for review") from exc
    if (not isinstance(raw, dict) or raw.get("schema_version") != SCHEMA
            or raw.get("scope") != "APPROVED_REFS_READ_ONLY"
            or not isinstance(raw.get("items"), list)
            or len(raw["items"]) > len(ROLES)):
        raise InvalidQueue("Existing queue does not match approved schema")
    seen = set()
    for row in raw["items"]:
        if not isinstance(row, dict):
            raise InvalidQueue("Queue record is not an object")
        role = row.get("role")
        if role not in ROLES or role in seen:
            raise InvalidQueue("Queue contains duplicate/unrecognized role")
        seen.add(role)
        if row.get("state") not in (TERMINAL_TRIAGED, PENDING, FAILED_READ, ACCESS, MATCH):
            raise InvalidQueue("Queue record state is invalid")
        if row.get("approved_sha") is not None and not is_sha(row["approved_sha"]):
            raise InvalidQueue("Queue contains invalid approved SHA")
        if row.get("observed_sha") is not None and not is_sha(row["observed_sha"]):
            raise InvalidQueue("Queue contains invalid observed SHA")
        attempts = row.get("read_attempts")
        if type(attempts) is not int or attempts < 0 or attempts > MAX_READ_ATTEMPTS:
            raise InvalidQueue("Queue contains invalid read attempts")
        if row.get("state") == TERMINAL_TRIAGED and not (
            is_sha(row.get("approved_sha")) and is_sha(row.get("observed_sha"))
            and row.get("proof_verdict") == "PASS_DELTA_INSPECTED_REQUIRES_REVIEW"
        ):
            raise InvalidQueue("Review-complete entry lacks exact verified refs")
    return raw


def candidates(authority: dict, observation: dict | None, old: dict) -> list[dict]:
    refs = (authority or {}).get("authority")
    if not isinstance(refs, dict):
        raise InvalidQueue("Canonical authority missing")
    observed_rows = (observation or {}).get("components", [])
    if not isinstance(observed_rows, list):
        raise InvalidQueue("Remote observation is malformed")
    by_role = {}
    for item in observed_rows:
        if not isinstance(item, dict) or not isinstance(item.get("role"), str):
            raise InvalidQueue("Remote observation contains invalid row")
        if item["role"] in by_role:
            raise InvalidQueue("Duplicated remote role cannot prove anything")
        by_role[item["role"]] = item

    previous = {r["role"]: r for r in old["items"]}
    result = []
    for role in ROLES:
        canonical = refs.get(role)
        if not isinstance(canonical, dict) or not is_sha(canonical.get("sha")):
            raise InvalidQueue("Missing approved immutable source for " + role)
        repo, approved = canonical.get("repo"), canonical["sha"]
        if not isinstance(repo, str) or not repo.startswith("Karmicmurphy/"):
            raise InvalidQueue("Invalid canonical repository for " + role)
        observed = by_role.get(role)
        state, sha, evidence = ACCESS, None, "Remote source not observed"
        if observed is not None:
            if observed.get("repo") != repo or observed.get("approved_sha") != approved:
                # Data mismatch cannot be treated as drift of a trusted ref.
                state, sha, evidence = ACCESS, None, "Observer disagrees with canonical identity"
            elif observed.get("state") == "MATCH" and observed.get("observed_sha") == approved:
                state, sha, evidence = MATCH, approved, "Exactly matched approved commit"
            elif observed.get("state") == "RECONCILIATION_REQUIRED" and is_sha(observed.get("observed_sha")):
                state, sha, evidence = PENDING, observed["observed_sha"], "Observed branch ahead/different: proof required"
            else:
                state, sha, evidence = ACCESS, None, "UNKNOWN or malformed remote evidence"
        prior = previous.get(role)
        attempts = 0
        verdict = None
        if (prior and prior.get("repo") == repo and prior.get("approved_sha") == approved
                and prior.get("observed_sha") == sha and state == PENDING):
            old_state = prior["state"]
            attempts = prior["read_attempts"]
            if old_state == TERMINAL_TRIAGED:
                state, verdict = TERMINAL_TRIAGED, "PASS_DELTA_INSPECTED_REQUIRES_REVIEW"
            elif old_state == FAILED_READ:
                state = FAILED_READ
        result.append({
            "role": role, "repo": repo, "approved_sha": approved, "observed_sha": sha,
            "state": state, "read_attempts": attempts, "proof_verdict": verdict,
            "evidence": evidence, "next_method": (
                "NO_AUTOMATIC_ACTION_REQUIRES_REVIEW" if state == TERMINAL_TRIAGED
                else "VERIFY_EXACT_GITHUB_COMPARE" if state in (PENDING, FAILED_READ)
                else "STOP_NEEDS_AUTHORIZED_READ" if state == ACCESS
                else "MONITOR"),
            "candidate_disposition": "REVIEW" if state == TERMINAL_TRIAGED else (
                "TEST" if state in (PENDING, FAILED_READ) else "DEFER"),
            "skill_routes": ROLE_SKILLS[role],
            "owner_gate": "NO_AUTO_REPIN_OR_MERGE",
        })
    return result


def pick_untriaged(items: list[dict]) -> dict | None:
    for row in items:
        if row["state"] in (PENDING, FAILED_READ) and row["read_attempts"] < MAX_READ_ATTEMPTS:
            return row
    return None


def ingest_receipt(items: list[dict], receipt: dict) -> None:
    if receipt.get("action") != "TRIAGE_APPROVED_REF_DRIFT":
        return
    delta = receipt.get("inspected_delta")
    decision = receipt.get("decision")
    if not isinstance(delta, dict) or not isinstance(decision, dict):
        return
    role = decision.get("role")
    row = next((r for r in items if r["role"] == role), None)
    if row is None or row["state"] not in (PENDING, FAILED_READ):
        return
    if (not is_sha(row["observed_sha"]) or delta.get("approved_sha") != row["approved_sha"]
            or delta.get("observed_sha") != row["observed_sha"]):
        # Do not trust a mismatched or incomplete proof.
        row["state"] = FAILED_READ
        row["read_attempts"] = min(MAX_READ_ATTEMPTS, row["read_attempts"] + 1)
        row["evidence"] = "Comparison lacked exact approved and observed identities"
        return
    row["read_attempts"] = min(MAX_READ_ATTEMPTS, row["read_attempts"] + 1)
    if (receipt.get("verdict") == "PASS_DELTA_INSPECTED_REQUIRES_REVIEW"
            and delta.get("no_auto_promotion") is True
            and isinstance(delta.get("changed_files"), list)):
        row["state"] = TERMINAL_TRIAGED
        row["proof_verdict"] = receipt["verdict"]
        row["evidence"] = "Exact remote compare inspected; candidate held for review"
    else:
        row["state"] = FAILED_READ
        row["evidence"] = "Bounded compare attempt failed; no permission to promote"


def build_queue(root: Path, observation: dict | None, receipt: dict) -> dict:
    old = load_queue(root / "state/FRIDAY_MAINTENANCE_QUEUE.json")
    authority = json.loads((root / "state/CURRENT_PROJECT.json").read_text(encoding="utf-8"))
    if authority.get("work_order", {}).get("gate_id") != "FRIDAY_BOUNDED_OPERATOR_LOOP":
        raise InvalidQueue("Current work order does not authorize this queue")
    rows = candidates(authority, observation, old)
    ingest_receipt(rows, receipt)
    return {"schema_version": SCHEMA, "scope": "APPROVED_REFS_READ_ONLY",
            "evidence_state": "DIAGNOSTIC_NOT_LIVE_EXECUTION",
            "authority_gate": "FRIDAY_BOUNDED_OPERATOR_LOOP",
            "items": rows,
            "summary": {
                "pending": sum(x["state"] in (PENDING, FAILED_READ) for x in rows),
                "triaged_for_review": sum(x["state"] == TERMINAL_TRIAGED for x in rows),
                "unknown_access": sum(x["state"] == ACCESS for x in rows),
                "matched": sum(x["state"] == MATCH for x in rows),
                "read_attempts_exhausted": sum(x["state"] == FAILED_READ and x["read_attempts"] >= MAX_READ_ATTEMPTS for x in rows),
            },
            "salvage_contract": {
                "use_registered_skills": ["artifact-compass", "artifact-salvage", "rights-gate", "proof-gate"],
                "no_source_install_or_import": True,
                "proof_before_any_upgrade": True,
                "parked_phone_and_preview": True,
            },
        }


def write_queue(root: Path, queue: dict) -> None:
    target = root / "state/FRIDAY_MAINTENANCE_QUEUE.json"
    stage = target.with_suffix(".friday-tmp")
    stage.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    stage.replace(target)
