#!/usr/bin/env python3
"""Read-only Pages Preview onboarding gate. Does not change authority or secrets."""
from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("FOUNDATION_GITHUB_TOKEN", "FOUNDATION_OWNER_SUB")
PROJECT = "ollie-twis-holo-workshop"


def inspect(project: dict, deployments: list, current: dict) -> dict:
    candidate = current["candidates"]["pages_bounded_fixture_promotion"]
    expected_repo = candidate["repo"]
    expected_commit = candidate["sha"]
    approved_branch = candidate["branch"]
    source = project.get("source", {}).get("config", {})
    found_repo = f"{source.get('owner', '')}/{source.get('repo_name', '')}"
    vars_ = project.get("deployment_configs", {}).get("preview", {}).get("env_vars", {})
    # Never emit variable values, even if the provider starts returning them.
    present = sorted(set(REQUIRED).intersection(vars_))
    missing = sorted(set(REQUIRED).difference(vars_))
    matches = [d for d in deployments if
               d.get("environment") == "preview" and
               d.get("deployment_trigger", {}).get("metadata", {}).get("commit_hash") == expected_commit and
               d.get("deployment_trigger", {}).get("metadata", {}).get("branch") == approved_branch and
               d.get("latest_stage", {}).get("status") == "success"]
    reasons = []
    if found_repo != expected_repo:
        reasons.append("SOURCE_REPOSITORY_MISMATCH")
    if missing:
        reasons.append("MISSING_PREVIEW_BINDINGS")
    if not matches:
        reasons.append("APPROVED_PREVIEW_DEPLOYMENT_NOT_VERIFIED")
    return {
        "project": PROJECT,
        "expected_repository": expected_repo,
        "observed_repository": found_repo,
        "approved_preview_branch": approved_branch,
        "approved_preview_commit": expected_commit,
        "matching_successful_preview_deployments": [d["id"] for d in matches if d.get("id")],
        "required_binding_names_present": present,
        "required_binding_names_missing": missing,
        "state": "CONFIG_BLOCKED" if reasons else "CONFIG_READY_RUNTIME_UNPROVEN",
        "reasons": reasons,
        "runtime_authenticated_phone_proof": "NOT_CHECKED",
        "authorization_changed": False,
        "secrets_read_or_exported": False,
    }


def cloudflare_get(account: str, resource: str, token: str):
    req = Request(
        f"https://api.cloudflare.com/client/v4/accounts/{account}/{resource}",
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json",
                 "User-Agent": "Harness-onboarding-readonly"},
    )
    with urlopen(req, timeout=15) as response:
        body = json.load(response)
    if not body.get("success"):
        raise ValueError("Cloudflare API returned unsuccessful response")
    return body["result"]


def run(current: dict, account: str | None, token: str | None, get=cloudflare_get) -> dict:
    report = {"schema_version": "1.0.0",
              "observed_at": datetime.now(timezone.utc).isoformat(),
              "scope": "READ_ONLY_PREVIEW_CONFIGURATION_NOT_LIVE_PROOF",
              "changes_performed": False}
    if not (account and token):
        report.update(state="UNKNOWN", reason="READ_ONLY_CLOUDFLARE_CREDENTIAL_NOT_CONFIGURED")
        return report
    try:
        project = get(account, f"pages/projects/{PROJECT}", token)
        deployments = get(account, f"pages/projects/{PROJECT}/deployments", token)
        report.update(inspect(project, deployments, current))
    except (HTTPError, URLError, TimeoutError, OSError, ValueError, KeyError, TypeError):
        report.update(state="UNKNOWN", reason="CLOUDFLARE_EVIDENCE_UNAVAILABLE_OR_INVALID")
    return report


def main() -> int:
    current = json.loads((ROOT / "state/CURRENT_PROJECT.json").read_text(encoding="utf-8"))
    report = run(current, os.environ.get("CLOUDFLARE_ACCOUNT_ID"),
                 os.environ.get("CLOUDFLARE_READ_TOKEN"))
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["state"] == "CONFIG_READY_RUNTIME_UNPROVEN" else 1


if __name__ == "__main__":
    sys.exit(main())
