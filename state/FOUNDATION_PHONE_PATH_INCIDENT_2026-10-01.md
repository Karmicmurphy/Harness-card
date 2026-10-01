# Foundation phone-path incident — 2026-10-01

Status: ACTIVE INCIDENT / REPO-SIDE REPAIR PROVEN IN CI / LIVE PREVIEW NOT YET PROVEN

## Locked outcome

Android owner action -> authenticated current Workshop Preview -> bounded Foundation job -> Independent Proof -> correlated result visible on Android under one Foundation job identity.

Production is out of scope. No new infrastructure is required.

## Observed failure sequence

1. Preview configuration appeared complete in the provider dashboard.
2. Android repeatedly returned `BLOCKED: PHONE_JOBS_DISABLED`.
3. A successful deployment retry of Workshop commit `0f2f6de0a1b9712592295c50eef4f609fc482baf` did not change the symptom.
4. Provider build logs reported a root Wrangler configuration and showed only the three legacy `TWIS_*` variables.
5. Repository inspection proved root `wrangler.jsonc` contained exactly those legacy variables and omitted the Foundation phone-path configuration.
6. Commit `003684535b17f99fe61d687f4e05500479704113` removed the conflicting root Pages Wrangler config from the Preview branch.
7. CI then failed because two stale Python contracts still required that obsolete file; 65 tests passed and 2 stale tests failed.
8. Commit `a99b13340c82ac79d7dc7ac883ab202f46770456` repaired those stale contracts.
9. GitHub run `36818221673` then produced a red failure with zero jobs from an unrelated Worker workflow, creating misleading failure noise.
10. Commit `029ce359b5833f654151a5ba3e4235404d949a54` repaired that unrelated workflow validation problem.
11. Workshop CI run `36818614766` passed the full repository-side suite, including contracts, API tests, static Pages build, and Pages Functions compilation.
12. The live Preview runtime after the configuration-authority repair remains unproven. The Android round trip remains open.

## Primary root cause

Split configuration authority / configuration drift.

The provider dashboard and repository Pages configuration described different runtime environments. Debugging initially trusted visible dashboard state without first proving which configuration source the deployed runtime consumed.

## Secondary failure classes

- Stale CI contracts encoded the obsolete configuration mechanism instead of the intended behavior.
- An unrelated zero-job workflow failure looked like application failure evidence.
- Repository changes were at times described as fixed before live runtime proof existed.
- Manual retry/check work was pushed to the owner before available repository and CI evidence had been exhausted.

## Failure-cycle accounting

At least four user-visible failure cycles are directly evidenced in this recovery sequence:

1. phone remained disabled after provider configuration;
2. phone remained disabled after deployment retry;
3. the configuration-authority repair triggered stale-contract CI failure;
4. the next repair triggered an unrelated zero-job workflow failure notification.

Earlier cycles existed, but an exact total is not reconstructed here. Do not invent one.

## Permanent rules

1. Provider configuration authority must be proven, not assumed.
2. Compare provider-reported build/runtime bindings against the expected runtime contract before asking the owner to re-enter settings.
3. Keep Pages and Worker configuration authority explicitly separate.
4. A zero-job Actions failure is workflow validation until proven otherwise.
5. Tests should assert intended behavior, not obsolete configuration-file shape.
6. Configuration-authority changes require a fresh deployment generation and live verification.
7. Green CI is PROVEN_IN_TEST only; target-device/provider proof is required for PROVEN_LIVE.
8. Owner interruption is a cost: exhaust current-session repo, logs, CI, and provider-access tools first.
9. After one live failure, inspect sibling failure modes in the same layer before another release attempt.
10. Public incident records must not contain private account data or credentials.

## Current evidence

Workshop repaired head at green CI proof: `029ce359b5833f654151a5ba3e4235404d949a54`.

Workshop CI run `36818614766`: SUCCESS.

Repository side: PROVEN_IN_TEST.

Current live Preview runtime: UNKNOWN until provider live state is inspected.

Android bounded round trip: BLOCKED / NOT PROVEN LIVE.

## Closure condition

Close only after the current authenticated Preview accepts the approved bounded action and returns the correlated Independent Proof result to Android under the same Foundation job identity.
