# FRIDAY bounded intent → real AIOS → receipt / replay proof — 2026-10-23

**Status: PROVEN_IN_TEST ONLY.** A fixed, safe *owner-style example request* executed through the existing Foundry intent compiler, job compiler, deny-by-default execution reconciliation, real AIOS Kernel, Software Builder and independent Proof. This is not an authenticated real owner command, persistent FRIDAY service, general language routing or exactly-once distributed runtime.

## Exact verified state

- [Foundry PR #36](https://github.com/Karmicmurphy/temporal-capability-foundry/pull/36) **merged** on `software-builder-v0` at development commit `58ef07c46c71943b313ae36298fece54281046ad`.
- [Real intent / kernel / independent proof / replay test](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/40007468407) **PASSED** on merged commit.
- [Earlier Harness-governed Foundry→AIOS proof](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/40007468443) **PASSED** on same merged commit.
- [Full Foundry test suite](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/40007468380) **PASSED** on same merged commit.
- [Pre-merge proof](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/40007280164) passed 8 focused positive/negative tests and exercised real process flow. It uploaded artifact `friday-intent-bounded-verified-receipt`, GitHub Actions artifact ID `12524722024`.
- On that verified pre-merge run: `intent:41219de437536ac51725d32f` → `job:ef9d94554501a166d08bedb2`, core `CERTIFIED_AWAITING_HUMAN_REVIEW`, certificate verdict `CERTIFIED`, Builder `PROVEN_IN_TEST`, replay `REUSED_CERTIFIED_RECEIPT_WITHOUT_SECOND_EXECUTION`. The run freshly observed public Harness head `30027847da4eab91a32b823e6ae1c3c82e210a6d` and checked unchanged approved AIOS runtime `8a954439af2b15b00f7c961d83552772b382fd1f`.
- First candidate CI run identified a missed sentence-final “only” constraint; no test execution occurred on that failed run. The request was updated to contain a recognized explicit `only ` constraint and revalidated without removing negative checks.

## What the test actually does

1. Clones the **current public** Harness main into temporary storage, reads its current `CURRENT_PROJECT.json`, verifies governance, active `FRIDAY_BOUNDED_OPERATOR_LOOP`, approved AIOS SHA, Foundry branch and still-open general runtime blocker. It records the observed main head. This is a source read, **not owner authentication**.
2. Clones the exact Harness-approved executable AIOS revision into a **disposable** Git workspace; asserts its identity and passes baseline tests.
3. Accepts exactly this test sentence: “Repair only the isolated AIOS path-containment test fixture.” Foundry's existing `prepare_intent` / `validate_interpretation` retains the explicit limit; `compile_job` emits a stable job identity; `reconcile_compiled_job` admits the single allowlisted `software_builder.repair` route with no privileges.
4. Injects a deliberately known failing path-containment fixture, then routes its **compiled job ID**, real AIOS Kernel, existing Builder and independent Proof to restore the exact code and retest. The certificate, Builder, runtime and Foundry records must share a job ID.
5. Requires status `CERTIFIED_AWAITING_HUMAN_REVIEW`, independent `CERTIFIED` exact source-byte identity, only the approved file changed, no activation and no deployment.
6. A **temporary local** JSON ledger records the attempt before execution. Identical replay returns the original certified receipt with no second execution; conflicting input, bad receipt or in-progress/uncertain attempt fail closed instead of being blindly rerun. This ledger does **not** prove safe recovery after arbitrary power loss, corrupted disks, two concurrent hosts, or externally visible effects.

## Honest boundaries / outstanding gate

- **Already proven:** one fixed request flows into a real compiled Foundry→AIOS job with an independently certified output, correlation and safe in-process/post-process-object replay on the same ephemeral workspace.
- **Still UNPROVEN:** user-authenticated fresh authority, general natural-language intention parsing, externally supplied jobs, reliable concurrent submit/durable idempotency across separate runners and crashes, resident service, human-facing success, and physical Windows/phone/Cloudflare delivery.
- **No approvals granted:** The Factory canonical SHA `e0e14e689b1d3a3bda1356276975b4b34f1b615e` has **not** been changed. Development branch advancement is not production approval. No credentials, production deployment, live dispatch, subscriptions, paid API or private local work were used.
- **Parked by owner:** phone/Android integration and Cloudflare Preview remain out of scope.

## One next proof — no expansion

Prove **freshly authorized owner request admission and durable duplicate handling across two separate process invocations** for the same isolated allowlisted job, using existing Harness policy and repo machinery. Include denial of unauthenticated/expired approval, changed source SHA, malformed receipt, uncertain in-flight process, and cross-process double-submission. If that path requires a token, identity claim, new public endpoint or broader permissions, **stop at that owner gate**; do not invent or copy a secret. Then evaluate whether a narrow live request path can safely be supported.

The current general runtime blocker stays open. This is a dated evidence report, not canonical promotion or a replacement work order.
