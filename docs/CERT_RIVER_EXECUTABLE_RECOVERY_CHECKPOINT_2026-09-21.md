# CERT-RIVER Executable Recovery Checkpoint — 2026-09-21

Status: **BOUNDED RECOVERY COMPLETE — CURRENT EXECUTABLE CERTIFIER NOT RECOVERED**

## Purpose

Satisfy the Foundation V0 recover-before-rebuild gate before implementing Cog 3.

This checkpoint searched for reusable executable CERT-RIVER / independent-certifier primitives without allowing archive archaeology to become an indefinite blocker.

## Direction 1 — Current canonical estate / code search

Searched live Foundation authorities and account-wide GitHub code for:
- CERT-RIVER;
- CERTIFIED / QUARANTINED;
- proof debt;
- certificate / quarantine / proof;
- certifier.

Recovered:
- Harness River lineage reconciliation and exact contract;
- Foundry proof/evidence/lifecycle machinery;
- AIOS receipt/trace/certificate **skill**;
- Workshop FlashRiver archive/intake/review surfaces;
- Scrapyard Proof Gate method.

Result: **no current executable independent certifier located.**

## Direction 2 — Repository trees / historical branches

Inspected:
- Harness main;
- Foundry software-builder-v0;
- AIOS main;
- historical AIOS prep/successor SHAs;
- Workshop main / living-workshop-main-build / audit-reconcile;
- Scrapyard main.

Relevant historical executable code recovered:
- AIOS `RiverBlackboard` — shared bounded work-state coordinator;
- Workshop `flashriver_intake.py` — archive intake/staging;
- AIOS audit/receipt schemas.

These are useful primitives but **not independent claim certifiers**.

The recovered AIOS Receipt / Trace / Certificate Harness is a method/contract, not a runtime certifier.

The Workshop source-archive metadata explicitly keeps raw/nested FlashRiver source packages local/private. The exact 607-file Phase-12 ZIP remains hash-pinned lineage evidence but is not accessible as current executable source in the live GitHub estate.

## Adaptive-pass verdict

Pass 1 found contract/method surfaces but no executable certifier.

Pass 2 changed source direction into historical repository trees and recovered adjacent mechanisms, but still no certifier implementation.

A third search pass is lower-value than building/testing the already-recovered minimal contract.

**TEST BEATS SEARCH.**

## Recovery verdict

`EXECUTABLE_NOT_RECOVERED_BOUNDED_RECOVERY_COMPLETE`

This does **not** claim the historical package never contained executable certification code.

It means no current usable executable certifier was recovered from the accessible estate after the bounded recovery checkpoint.

## Clean reimplementation authorization boundary

Foundation V0 may now implement the **smallest independent verifier** consistent with the recovered River contract:

Input:
- `foundry_job_id`;
- exact claim ID/text;
- exact candidate path/reference;
- expected candidate hash;
- exact acceptance command(s);
- allowed/forbidden changed paths;
- proof debt.

Required behavior:
- run outside SoftwareBuilder;
- isolate the proof workspace;
- independently recompute candidate hash;
- verify changed-path boundary;
- run only allowlisted exact acceptance commands;
- detect proof-induced mutation;
- emit exactly CERTIFIED / REJECTED / QUARANTINED;
- preserve exact certificate boundary, proof debt, trace/evidence;
- never edit candidate source, deploy, promote, activate, or broaden the claim.

No larger proof framework is authorized by this checkpoint.
