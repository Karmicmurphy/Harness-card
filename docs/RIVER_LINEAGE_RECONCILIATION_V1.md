# River Lineage Reconciliation — V1

Date: 2026-09-20

Status: **RECOVERED ARCHIVED PROOF LINEAGE — RECONCILED, NOT CURRENT RUNTIME AUTHORITY**

This file answers the question that kept getting lost:

> What did CERT-RIVER / PRISM-RIVER / RiverKernel actually contain, and what role is still missing after Foundry, AIOS, Workshop, and Harness?

## Recovery result

CERT-RIVER was not merely a name or a future architecture sketch.

The recovered Library artifact `FlashRiver_Phase12_Harness_Skills_Questions_Extraction.md` records a source package:

`FlashRiver_CERT-RIVER_phase12_certified_lineage_clean_working_memory(2).zip`

SHA-256:

`74d16ddf7769b03d816d32b6aa9bec5c7a8d74ea125d0d1a0600ee633194f2bb`

The extraction reports **607 files**, including:

- 110 Markdown files;
- 213 JSON files;
- 35 Python files;
- 84 text files;
- 21 PDFs;
- 10 HTML files;
- 7 ZIPs.

That is strong evidence of a real proof-system lineage, not just a chat concept.

The exact ZIP itself was not surfaced as a directly readable Library item in this pass, so this remains **archived lineage evidence**, not current executable authority.

## Primary proof artifacts recovered by hash

The Phase-12 extraction pins these important files:

- `PROJECT_STATE.md` — `2a9a66199844bd296ce1070d8cbeedb1075dfd44cc53d0513db62835584d1e96`
- `RESTART_PACKET.md` — `0b4dfc94d784aa5fa237de2e85c270834394e0380b55e7912429f0d2adc31953`
- `MANIFEST.json` — `a7bb4d4a907fe4b394d76718d4f9f2a37e452f443d2d58d9a1d813323f1c937a`
- `PHASE8_POLICY_GATE_SKETCH.md` — `6c12fd5c14c6575924483159fb3067de9fc2ed004cf587648bd1bc5c2813e998`
- `PHASE9_LEGAL_EXECUTION_SURFACE_ROUTING_REVIEW.md` — `c50d3662493b0ce5b89f472404a72e71277b5faf41a1345ca625224465368ad1`
- `PHASE10A_PROOF_MODE_UI_BOUNDARY_MAP.md` — `42400656ea387d964ea700319e871e4aed4f305875d2aae1aac3bd385fddc988`
- `PHASE11B_TINY_MULTI_STEP_PIPELINE_PROOF_PLAN.md` — `0b612fcbf12b6ad36427373002671f6f719eab342bda487c5a3e38d7d6651e56`
- `PHASE11E_PROOF_FAILURE_REPAIR_AUDIT.md` — `710ef935d8267bf8b74525aa1068a477f938f4657ba87b81fa4753a65050ad37`
- `PHASE11F_COMPARATOR_REPAIR_AND_PIPELINE_PROOF_RERUN.md` — `633b00531187f6935a7008563665361cb078b40aeefb8a449b7ef1a61de885dc`
- `PHASE12_CERTIFIED_LINEAGE_CONSOLIDATION_AUDIT.md` — `4afb5286433d307be1804499c59f858a5c2d3cd80e7bf295043eac96828d78ef`
- `PHASE5_THREE_CONTRACT_KERNEL_ACCEPTANCE_AUDIT.md` — `a54df871c31ee24b860a6bfaa5f1918b5cc313272b5cbd8cb42778e958cd4cd5`

## What River uniquely contributed

The unique value is **not another AI agent framework**.

It is the independent proof/certification contract:

```text
claim
+ exact provider/implementation
+ exact fixture/input boundary
+ exact comparator
+ receipts
+ trace
+ proof debt
-> independent proof
-> CERTIFIED / REJECTED / QUARANTINED
-> exact certificate boundary
-> no-broadening audit
```

Recovered River laws include:

- prove actual file access before reasoning;
- certify claims, not whole tools;
- no certificate broader than the exact proof;
- no-certificate-no-use;
- failure stops and quarantines instead of being hand-waved;
- classify failure before repair;
- make the smallest lawful repair;
- rerun the exact proof;
- cached proof is lawful only with a complete dirty-key basis;
- UI/metadata may display proof facts but cannot become enforcement;
- receipt, trace, and certificate are different things;
- working-memory files are continuation truth.

## Reconciliation with live systems

### Foundry

Foundry now owns the integrated capability lifecycle:

`intent -> job -> execution -> evaluation -> learning candidate -> promotion -> activation -> rollback`

That should stay.

Foundry evaluation is **development/evaluation feedback**, not automatically an independent certificate.

Foundry promotion decides whether a candidate is eligible to become active. A River-style certificate can become one evidence gate when independent proof is required.

### Software Builder

Builder owns:

`inspect -> edit -> test -> failure -> repair -> retest -> receipt`

Builder must be allowed to run its own development tests.

It should **not issue its own final independent certificate**.

The recovered River pattern strongly supports Randy’s instinct:

> Builder builds. Independent certifier verifies.

### Untethered AIOS

AIOS owns reusable process/scheduler/capability/audit primitives:

- process lifecycle;
- explicit grants;
- path scopes;
- child grant subsets;
- bounded ticks;
- runtime audit receipts.

Those are execution controls, not certificates.

An AIOS audit receipt can support a proof, but a process receipt does not mean the claim is certified.

### Workshop

Workshop owns the human-facing artifact/engine surface.

Its Receipt Ledger stores action/artifact evidence. Its MCP/security gates constrain tool use.

Workshop is also the natural future place to **display**:

- candidate;
- proof running;
- certified;
- rejected;
- quarantined;
- proof debt;
- trace/receipt links.

But the UI must never infer or issue certification itself.

### Harness Card

Harness remains cross-project operating authority:

- recover current truth;
- scope work;
- route skills;
- prevent drift;
- require proof;
- preserve decisions.

PRISM-RIVER’s policy/proof-routing concepts should inform bounded proof/use routing. They should not become a second global Harness.

## Receipt semantics must stay separate

Do not make one giant generic “receipt.”

Current useful distinction:

- **AIOS receipt** — runtime/process/capability audit event.
- **Workshop receipt** — human-facing artifact/action record.
- **Foundry receipt** — capability lifecycle/evaluation/promotion/activation evidence.
- **CERT-RIVER trace** — detailed proof execution path.
- **CERT-RIVER certificate** — bounded independent decision about one exact claim.

That separation is a feature, not duplication.

## One River mechanism Foundry should salvage later

**Dirty-key proof honesty.**

Foundry already requires repeatability for promotion, but River is more precise about cached/replayed proof.

A valid proof replay should eventually bind at least:

- provider/model/implementation;
- fixture/input;
- expected output;
- comparator;
- proof engine;
- dependency/runtime versions;
- boundary-affecting code.

If one changes, a cached certificate cannot silently survive.

Do not implement this globally yet. Carry it into the Builder-to-CERT proof design.

## Candidate independent-certifier contract

This is a recovered **contract candidate**, not permission to build a new framework.

Input:

- exact claim;
- content-pinned candidate;
- exact fixture;
- exact acceptance comparator;
- Builder/development receipt;
- declared proof debt.

Process:

1. prove access/hashes;
2. create clean isolated state;
3. run the exact acceptance proof;
4. capture trace and receipts;
5. classify any failure;
6. quarantine on ambiguity/failure;
7. run no-broadening audit.

Output:

- `CERTIFIED | REJECTED | QUARANTINED`;
- exact certificate boundary;
- proof debt;
- trace/receipt references;
- dirty-key basis when replay is allowed.

The certifier does **not** edit code, deploy, promote, activate, or broaden a claim.

## Reconciliation verdict

We do **not** need to invent another proof architecture.

We already have the design lineage for the independent proof side, and live systems now cover much of the execution/storage side.

The remaining job is smaller:

```text
Software Builder candidate receipt
        |
        v
small Builder-to-CERT adapter
        |
        v
recovered River proof contract
        |
        v
independent clean rerun
        |
        v
CERTIFIED / REJECTED / QUARANTINED
        |
        v
Foundry promotion gate may consume certificate as evidence
```

Do not implement that adapter until either:

1. the exact archived CERT-RIVER implementation primitives are recovered; or
2. recovery proves those implementation files unavailable and a smallest clean reimplementation is justified.

## Current status

**RIVER LINEAGE: RECOVERED AND RECONCILED**

**CURRENT EXECUTABLE CERTIFIER: NOT YET VERIFIED**

That distinction must remain explicit.
