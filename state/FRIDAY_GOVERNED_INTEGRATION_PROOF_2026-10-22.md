# FRIDAY governed Foundry → AIOS integration proof — 2026-10-22

> **2026-10-22 postscript:** The candidate described below was subsequently merged **only into the Foundry development branch** at `7ceaad7a82dcedc85f8c23cf88bea4bef05ee9ca`; both exact post-merge CI checks [guarded proof](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/39885548352) and [unit](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/39885548353) passed. The dated pre-merge descriptions below are retained for evidence chronology, not current status. No canonical factory authority repin or live FRIDAY assertion follows from this merge.

**Current evidence: PROVEN_IN_TEST, not PROVEN_LIVE. Candidate only.** This is a dated observation receipt, not a new canonical work order, merge authorization, runtime activation, owner authentication, or general FRIDAY capability.

## Exact links and identities

- Work order: [Harness Issue #47](https://github.com/Karmicmurphy/Harness-card/issues/47).
- Candidate: [Foundry PR #35](https://github.com/Karmicmurphy/temporal-capability-foundry/pull/35) on `candidate/friday-governed-foundry-aios-proof-2026-10-22`, targeting existing `software-builder-v0`. **Unmerged / draft**.
- Green guarded real composition run: [GitHub Actions #39879548240](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/39879548240) — **SUCCESS**.
- Green complete Foundry unit suite: [GitHub Actions #39879548114](https://github.com/Karmicmurphy/temporal-capability-foundry/actions/runs/39879548114) — **SUCCESS**.
- Receipt artifact: `friday-governed-bounded-proof` in run 39879548240 (GitHub artifact ID **12469967203**), contains `friday-governed-integration-proof-receipt.json` and original `foundation-core-v0-proof-receipt.json`. This is a GitHub-hosted artifact, not an invented local file.
- Original core receipt SHA-256 (computed in the successful CI job): `c07f533f74b6416ed7ff792266915c1d8f2dbe928a95fc8b91db26803c3fc62a`.
- Immutable Harness inspection source: `b39200af892a3060a0488406f7d065c5b7582501` (`state/CURRENT_PROJECT.json`).
- Harness-approved exact AIOS runtime tested: `8a954439af2b15b00f7c961d83552772b382fd1f`, not the later documentation-only main advancement.
- Foundry candidate PR head tested: `8d85c6af6f36f10964dbf9298ffafc0d1e9a3a5e`.

## What actually ran

Existing `scripts/run_foundation_core_v0_proof.py` was reused *unchanged*. It clones the approved public AIOS repo in a disposable temp checkout, executes baseline tests, introduces a known path-containment fault in an allowed source file, routes deterministic repair via the existing Foundry Software Builder and actual AIOS Kernel, retests the repaired artifact and obtains the existing independent proof certificate. The upstream core returns **PROVEN_IN_TEST**, not automatic promotion.

The new gated wrapper verified immutable public Harness checkout SHA and the ACTIVE `FRIDAY_BOUNDED_OPERATOR_LOOP` work order; enforced the matching approved AIOS source identity; invalidated any stale local core result; checked correlated Foundry job, AIOS runtime, Builder and certificate job identities; checked failure/repair/retest evidence, exact changed-file scope, `CERTIFIED` independent proof, and explicit **awaiting human approval / no activation**. It stored a digest of the original core receipt and a narrow `BOUNDED_EXISTING_FOUNDRY_AIOS_COMPOSITION_NOT_GENERAL_FRIDAY` verdict.

Eight focused negative/positive tests passed (mismatched identity/gate, missing/counterfeit receipts, escaped write scope, bad job IDs, missing retest, false certificate, fabricated model/deploy claims, bypassed approval). Full Foundry CI passed. The guarded workflow preserved both receipts and used only read permissions, no model/API service, no secrets, and no production or phone actions.

## Why this does not finish FRIDAY

- This is a **deterministic CI repair fixture**, not an arbitrary owner language request, authenticated fresh live authority, durable dispatcher, general-model reasoning or a running resident assistant.
- It does not prove a persistent loop that survives process crashes or delivers exactly-once external effects.
- It does not prove the real Windows Workshop host, local private materials, authenticated Android/Pages round trip, Cloudflare Preview, general FRIDAY MCP endpoint, or a live external task.
- This does not approve Foundry PR #31 or #34, change Harness pins, merge Foundry #21, increase GitHub Actions permissions, transfer protected secrets, or authorize deployment.
- GitHub CI evidence is scoped to the tested exact commit and its uploaded receipts; rerun if source or policy changes.

## Disposition

- **KEEP:** Existing Foundry Foundation Core, AIOS Kernel, independent certificate, Harness gate and Artifact Compass/Proof Gate machinery. No new framework or scheduler.
- **PROVEN_IN_TEST:** One bounded real cross-repo Foundation execution under pinned Harness governance at Foundry PR #35.
- **REVIEW before any merge:** The minimal PR #35 (candidate/test-only), and independently PRs #31/#34 only if they close a remaining verified gap. Merge to a working branch is not canonical promotion.
- **NEXT REQUIRED PROOF:** A FRIDAY owner-intent-to-allowlisted-job path (including recovery/retry, authorization, and receipt preservation) under *fresh* authority, first in a disposable isolated runner. No production or local-host dependency. The current canonical block `GENERAL_FREEFORM_FRIDAY_RUNTIME_AND_CONNECTED_LOCAL_MACHINE_NOT_YET_PROVEN` remains valid.
- **PARKED:** Phone / Pages Preview integration and local Windows source-yards, per owner prioritization.

**Stop:** This bounded verification work order has met its `PROVEN_IN_TEST` acceptance threshold. Do not escalate it to `PROVEN_LIVE` or unrestricted autonomy without independent real user-path proof.
