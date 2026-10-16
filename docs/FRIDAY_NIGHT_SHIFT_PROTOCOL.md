# FRIDAY Night Shift — unattended GitHub verification protocol

**Purpose:** Keep the existing FRIDAY/Harness ecosystem verifiable and recoverable while the owner is away, using GitHub Actions only. No new agent, no Cloudflare dependency, no new front door.

**Operating rule:** Recover authority → run existing checks → render current status → preserve a receipt → stop. Night Shift verifies and detects drift; it does **not** self-authorize implementation, deployment, secret access, spending, or promotion of SHA pins.

## What actually runs

The existing `.github/workflows/friday-control-plane.yml` already has a daily GitHub Actions schedule (12:37 UTC; GitHub scheduling is best effort), manual dispatch, and scoped PR/main change triggers. This change **extends that same workflow**, rather than adding competing schedulers.

Night Shift now runs:
1. Canonical authority spine guard and generated continuity check.
2. Existing read-only observation of approved remote refs. Private inaccessibility is UNKNOWN, not failure-proof or permission to repin.
3. The full *present* Harness test inventory: `tests.test_authority_spine`, `tests.test_foundation_state`, `tests.test_skill_registry`, `tests/test_self_improve.py`, `tests/test_learning_intake.py`, and `tests/test_friday_control_plane.py`.
4. A regeneration of the owner-readable FRIDAY status with the existing control-plane script, with generated test mutations cleared before it.
5. An always-created Markdown run receipt and GitHub step summary, including commit, run URL, per-gate outcome, explicit limits, and first-failure recovery rule.
6. The existing Actions artifact upload, even on failure. The status and receipt may be absent if an early gate failed; the run and earlier step logs are still the evidence. On success, the existing authorized status writeback on main remains unchanged.

The run uses the runner's checked-out repository and existing policy only. It cannot see the owner's local PC artifacts or magically run private deployments. If a check fails, the workflow stays red and **does not automatically change source code** to silence the error.

## Meaning of a green run

- **PROVEN_IN_TEST:** Repository authority, test contracts, deterministic learning, and owner-status rendering succeeded at one commit.
- **NOT PROVEN_LIVE:** A phone sent a Foundry job, received a correlated receipt, or edited any real end-user artifact.
- **Not a freshness guarantee:** Scheduled runs can be delayed or disabled by GitHub; latest world/AI research is not performed by these regression tests.

The canonical Foundation next gate is still `PAGES_BOUNDED_JOB_ROUND_TRIP`. Preview authorization secrets remain a named blocker; do not copy Production secrets or launch the job to force a green result.

## Allowed next actions for an interactive owner session

When the user says `Use Harness Card and continue` after a Night Shift run:
- read the latest workflow receipt and latest canonical `state/FRIDAY_MACHINE_STATUS.md`;
- isolate a failing CI/regression and repair one specific layer on a candidate branch with tests;
- merge only an ordinary scoped change after its own proof and applicable gates;
- keep unrelated security, payments, identity, personal records, live fixture dispatch and provider production under their established owner permissions.

No automatic mass dependency update or AI industry chasing is licensed by this protocol. Each real upgrade requires a concrete justified outcome, evidence, cost/security assessment where relevant, and a bounded diff.

## Owner interruption budget

Default to no phone taps, no questions, no manual GitHub clicking, and no requirement for a PC. This is appropriate for safe CI/repository work; some operations remain owner-gated by the existing `OPERATING_CONTRACT.md`, `config/friday_automation_policy.json`, and `state/CURRENT_PROJECT.json`.

## Evidence checkpoint

This protocol modifies an **existing** scheduled verification workflow, not a live autonomous FRIDAY instance. The highest proof comes from an actual GitHub Actions run using this revision. Claim no scheduled production behavior until such a run exists. When resuming, link the workflow run ID, commit SHA, and checked steps.
