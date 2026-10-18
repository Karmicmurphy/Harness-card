#!/usr/bin/env python3
"""Evaluate provider release evidence; never deploy, authenticate or certify live by itself.

Input is a SANITIZED observation packet assembled from current GitHub, provider,
route and owner-device evidence. This script neither requests nor reads credentials.
Its strongest verdict means the packet is ready for independent live-proof review.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SHA = re.compile(r"^[0-9a-f]{40}$")


def evaluate(packet: dict[str, Any]) -> dict[str, Any]:
    target = packet.get("target")
    if not isinstance(target, dict):
        raise ValueError("target must be an object")
    required = ("repo", "branch", "sha", "service", "environment")
    if any(not isinstance(target.get(k), str) or not target[k].strip() for k in required):
        raise ValueError("target must specify repo, branch, sha, service, environment")
    if not SHA.fullmatch(target["sha"]):
        raise ValueError("target.sha must be a full 40-character Git SHA")
    if target["environment"] not in {"preview", "production"}:
        raise ValueError("environment must be preview or production")
    bindings = target.get("required_bindings", [])
    if not isinstance(bindings, list) or any(not isinstance(x, str) for x in bindings):
        raise ValueError("required_bindings must be a list of names")

    # Only emit allowlisted, non-sensitive details. Never reproduce unknown input.
    report: dict[str, Any] = {
        "target": {k: target[k] for k in required},
        "evidence_level": "NOT_PROVEN",
        "verdict": "BLOCKED",
        "reason": "CI_NOT_VERIFIED",
        "next_action": "Read the current GitHub CI conclusion for the exact target SHA.",
        "requires_independent_live_review": True,
    }

    def mark(level: str, verdict: str, reason: str, action: str) -> dict[str, Any]:
        report.update(evidence_level=level, verdict=verdict, reason=reason, next_action=action)
        return report

    auth = packet.get("authorization") or {}
    if target["environment"] == "production" and auth.get("production_approved") is not True:
        return mark("NOT_PROVEN", "BLOCKED", "PRODUCTION_OWNER_GATE", "Obtain explicit owner authorization for this production target.")

    ci = packet.get("ci") or {}
    if ci.get("sha") != target["sha"]:
        return mark("NOT_PROVEN", "BLOCKED", "CI_SHA_UNKNOWN_OR_MISMATCH", "Verify CI against the requested commit, not a moving branch.")
    if ci.get("conclusion") == "failure":
        return mark("FAILED", "FAILED", "CI_FAILED", "Repair the failing job and rerun CI for this commit.")
    if ci.get("conclusion") != "success" or not ci.get("run_url"):
        return report
    report["ci_run_url"] = ci["run_url"] if isinstance(ci["run_url"], str) and ci["run_url"].startswith("https://github.com/") else "NOT_SUPPLIED"
    report.update(evidence_level="PROVEN_IN_TEST", reason="CI_PASSED", next_action="Inspect the provider deployment for the exact commit.")

    deploy = packet.get("deployment") or {}
    if not deploy:
        return report
    if deploy.get("sha") != target["sha"]:
        return mark("PROVEN_IN_TEST", "BLOCKED", "DEPLOY_SHA_UNKNOWN_OR_MISMATCH", "Match the provider deployment to the approved commit.")
    if deploy.get("status") == "failure":
        return mark("PROVEN_IN_TEST", "FAILED", "DEPLOY_FAILED", "Inspect deploy logs; preserve the last working production version.")
    if (deploy.get("status") != "success" or deploy.get("service") != target["service"]
            or deploy.get("environment") != target["environment"] or not deploy.get("id")):
        return mark("PROVEN_IN_TEST", "BLOCKED", "DEPLOY_NOT_CONFIRMED", "Check provider deployment ID, target service and environment.")
    if target["environment"] == "production" and deploy.get("traffic_percent") != 100:
        return mark("PROVEN_IN_TEST", "BLOCKED", "TRAFFIC_NOT_100_PERCENT", "Check production traffic allocation before claiming an updated app.")
    deployed_bindings = deploy.get("bindings", [])
    if not isinstance(deployed_bindings, list) or not set(bindings).issubset(set(str(x) for x in deployed_bindings)):
        return mark("PROVEN_IN_TEST", "BLOCKED", "REQUIRED_BINDINGS_MISSING", "Restore the approved environment bindings without exposing secret values.")
    report["deployment_id"] = str(deploy["id"])
    report.update(evidence_level="DEPLOYMENT_CONFIRMED", verdict="PARTIALLY_PROVEN",
                  reason="LIVE_USER_PATH_NOT_VERIFIED",
                  next_action="Verify the actual target route, screen and primary action on the target device.")

    live = packet.get("live") or {}
    if not live:
        return report
    if live.get("http_status") in {401, 403}:
        return mark("DEPLOYMENT_CONFIRMED", "BLOCKED", "LIVE_AUTH_OR_EDGE_DENIED", "Use an authorized owner session to verify the route; do not bypass Access.")
    if live.get("http_status") != 200 or live.get("sha") != target["sha"]:
        return mark("DEPLOYMENT_CONFIRMED", "BLOCKED", "LIVE_ROUTE_OR_VERSION_NOT_VERIFIED", "Resolve the route/version mismatch and recheck after caches settle.")
    if not live.get("expected_screen_visible") or not live.get("primary_action_verified"):
        return mark("DEPLOYMENT_CONFIRMED", "PARTIALLY_PROVEN", "LIVE_ACTION_NOT_PROVEN", "Test the requested control and observe its real result.")
    if live.get("device") not in {"android", "desktop_browser", "ios"} or not live.get("proof_ref"):
        return mark("DEPLOYMENT_CONFIRMED", "PARTIALLY_PROVEN", "LIVE_PROOF_IDENTITY_MISSING", "Record target device and independently reviewable proof reference.")
    report["live_proof_ref"] = str(live["proof_ref"])
    return mark("CANDIDATE_LIVE_PROOF_PACKET", "READY_FOR_INDEPENDENT_REVIEW",
                "LIVE_EVIDENCE_PACKET_COMPLETE",
                "Independently verify the supplied provider and device evidence before declaring PROVEN_LIVE.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence", type=Path, help="Path to sanitized current evidence JSON")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text(encoding="utf-8"))
    report = evaluate(data)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["verdict"] == "READY_FOR_INDEPENDENT_REVIEW" else 1


if __name__ == "__main__":
    raise SystemExit(main())
