# Cross-Project System Boundary Map — V1

Date: 2026-09-21

Status: **RECONCILED WORKING BOUNDARY — COGS 1–4 PROVEN IN TEST**

Live repo/device truth outranks this file.

## Ownership

| System | Owns | Does not own |
|---|---|---|
| Harness Card | recovery, scope, policy, proof requirements, continuity | runtime, coding, scheduling, certifier implementation |
| Workshop | human artifact/job cockpit, returned artifacts, human review | global governance, promotion, independent certification |
| Foundry | typed jobs, Builder, evidence, evaluation, promotion, activation, rollback | human cockpit, global scheduler, self-certification |
| AIOS | bounded process lifecycle, grants/path scopes, scheduling, runtime audit | governance, Builder semantics, promotion, certification |
| Scrapyard | salvage, rights, recombination, adaptive research methods | runtime scheduler, Builder, certifier runtime |
| Independent Proof V0 / CERT-RIVER lineage | exact-claim proof discipline, certificate, quarantine, no-broadening | editing, deploy, promotion, activation |

## Proven execution spine

```text
Foundry job_id
-> AIOS bounded wake/grants
-> Builder deterministic repair/test
-> Foundry development evidence
-> Independent Proof V0
-> certificate-aware Foundry promotion gate
```

Proven runs:
- Builder: `35611616345`
- Foundry -> AIOS wake: `35612271813`
- Independent Proof V0: `35620771601`
- Certificate-required promotion gate: `35620968656`

## Receipt semantics remain separate

- Workshop receipt = human-facing artifact/action record.
- AIOS receipt = runtime/process/capability audit.
- Foundry receipt = development/evaluation/promotion/activation evidence.
- Independent proof trace = exact verifier execution path.
- Independent certificate = bounded verdict on one exact claim.

Do not collapse these into one receipt type.

## Independent proof boundary

Current implementation: `temporal-capability-foundry/src/foundry/independent_proof.py`

Verifier: `independent-proof-v0.2`

It pins exact candidate bytes/hash and claim boundary, reruns acceptance outside Builder, enforces changed/forbidden path policy, distinguishes `CERTIFIED`, `REJECTED`, and `QUARANTINED`, records proof debt, and has no edit/deploy/promote/activate/broaden authority.

Foundry promotion can now require an exact `CERTIFIED` certificate bound to the expected `foundry_job_id` and `claim_id`. Missing, rejected, quarantined, or mismatched certificates block promotion.

## Current missing interface

### Workshop -> Foundry
**State:** BLOCKED ON LOCAL WORKSHOP RECONCILIATION.

GitHub Foundation branch:
`Karmicmurphy/Ollie_Twis_Holo_workshop@living-workshop-main-build`

GitHub Phase 1A is proven in test, but Randy's local Windows Workshop may be newer and remains local/private authority until reconciled.

After reconciliation, build one thin adapter only:
- Workshop goal/project/artifact refs/constraints/risk/acceptance;
- Foundry creates/uses `job_id`;
- Workshop stores `foundry_job_id`;
- return Builder receipt, AIOS audit, independent certificate, proof debt, promotion/activation state, result artifact/diff.

Workshop must not issue certification.

## Forbidden bypasses

1. Builder does not self-certify.
2. AIOS runtime success does not equal certification or promotion.
3. Workshop does not certify.
4. Scrapyard Proof Gate is a method, not the certifier runtime.
5. Models do not control deploy/publish/promotion.
6. No new scheduler, global job ID, AI OS, proof DB, or agent framework without hard evidence.
7. Randy retains irreversible-action authority.

## Current blocker

**Cog 5: reconcile local Windows Workshop against the GitHub Foundation branch.**

Then:

**Cog 6: build and prove the smallest Workshop -> Foundry job/result adapter.**

Do not reopen Cogs 1–4 unless new evidence breaks their proofs.
