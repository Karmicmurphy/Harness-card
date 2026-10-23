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

## Truthful Night Shift results (drift is not a clean machine)

The machine can have **green regression tests while its remote authority is still mismatched or unknown**. The run receipt now has distinct meanings:

- `TESTS_PASS__CURRENTLY_RECONCILED`: repository checks passed, remote refs supplied by the observation report agree with pinned refs. **Not** live phone-job proof.
- `TESTS_PASS__RECONCILIATION_REQUIRED`: checks passed but at least one current remote ref differs from the approved pin; investigate before any mutation and **never** auto-repin.
- `TESTS_PASS__REMOTE_UNVERIFIED`: checks passed but some remote refs are UNKNOWN, observation is missing, or its state is unrecognized. Private access errors do not equal confirmed drift or confirmed health.
- `FAILED_OR_INCOMPLETE`: required tests or generated status failed/are missing. Preserve this verdict in the always-run receipt even though the Actions workflow is red.

Receipt generation is pure reporting in `scripts/night_shift_receipt.py`, with regressions in `tests/test_night_shift_receipt.py`. The receipt includes the current canonical gate and count of owner-gated blockers so green CI is not mistaken for an operational FRIDAY. It does not read secret values, modify refs, write to another repository, or dispatch jobs.

## Meaning of a green run

- **PROVEN_IN_TEST:** Repository authority, test contracts, deterministic learning, and owner-status rendering succeeded at one commit.
- **NOT PROVEN_LIVE:** A phone sent a Foundry job, received a correlated receipt, or edited any real end-user artifact.
- **Not a freshness guarantee:** Scheduled runs can be delayed or disabled by GitHub; latest world/AI research is not performed by these regression tests.

The canonical Foundation next gate is resolved **live** from `state/CURRENT_PROJECT.json`, never from this dated protocol. As of October 23, 2026 it is `FRIDAY_BOUNDED_OPERATOR_LOOP`: keep the scheduled Harness/Foundry proof and diagnostics loop operating, and pursue only the bounded authorization/recovery test recorded in the current work order. **Android/phone and Cloudflare Pages Preview remain parked**, including their prior protected bindings; no credential copying or live job dispatch. The current [diagnostic queue](../state/FRIDAY_MAINTENANCE_QUEUE.json) remembers exact inspected source revisions. A reviewed branch delta is not an approved SHA or code repair.

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
