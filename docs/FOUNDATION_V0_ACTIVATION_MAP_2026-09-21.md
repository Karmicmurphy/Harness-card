# Foundation V0 Activation Map — 2026-09-21

Status: **FOUNDATION CORE V0 OPERATIONAL_IN_TEST — HUMAN REVIEW GATED**

Live repository/device truth outranks this map.

## What is functional now

The direct Foundation core can run one bounded software repair job without a model:

```text
human-specified exact patch job
-> Foundry job identity
-> AIOS process/job correlation
-> Software Builder bounded edit + automatic retest
-> Independent Proof V0
-> CERTIFIED / REJECTED / QUARANTINED
-> human review
```

Normal software jobs do **not** enter capability promotion automatically.

Successful normal jobs end at:

`CERTIFIED_AWAITING_HUMAN_REVIEW`

No merge, deploy, publish, activation, spending, deletion, permission expansion, or model-weight change occurs automatically.

## Proven core evidence

- Deterministic Builder: run `35611616345`
- Foundry -> AIOS wake: run `35612271813`
- Independent Proof V0: run `35620771601`
- Certificate-required promotion gate: run `35620968656`
- Foundation core composition: run `35627936077`
- Strict Python-bytecode proof integrity: run `35627957323`
- Human-operated exact-patch runner on real pinned AIOS: run `35628459336`

Human-runner proof head:

`b84db3579ff7d62095c40b6c2a8830fec7557e11`

Current Foundry authority:

`Karmicmurphy/temporal-capability-foundry@software-builder-v0`

Authority head at this update:

`32c8a292d9d753a79a163a470dd5873e98e87dcb`

## Human-operated runner

Implementation:

`scripts/run_foundation_exact_patch_job.py`

Documentation:

`docs/FOUNDATION_CORE_V0.md`

Example:

`examples/foundation_exact_patch_job.example.json`

V0 intentionally supports:
- existing candidate Git checkout;
- separate trusted Untethered-AIOS checkout;
- exact replacement patches;
- Python standard-library unittest acceptance;
- Builder workspace/command policy;
- independent exact-claim certification;
- human review stop.

This is deliberately narrow. New patch types or command families must earn support through proof.

## Proof-integrity rule

Builder test commands and Independent Proof acceptance commands use isolated `PYTHONPYCACHEPREFIX` directories.

Reason: CPython can otherwise reuse stale timestamp/size-valid bytecode after a same-size source repair.

Independent Proof excludes only derived Python bytecode (`__pycache__`, `.pyc`, `.pyo`) from changed-path authority and still records those paths in evidence.

Other unexpected files still count.

## Known proof debt

AIOS currently provides process lifecycle and `foundry_job_id` correlation around the Builder job.

Builder's own proven workspace/command policy still mediates Builder file/test operations; every Builder tool call is **not** currently routed through AIOS CapabilityGrant.

Do not claim otherwise.

Per-tool AIOS mediation may be considered later only if its extra security/recovery value earns the complexity.

## Human-owned improvement mode

Foundation improvement is **not self-evolving AI**.

After repeated real proven jobs:

```text
successful traces
-> repeated pattern
-> candidate RULE / SCRIPT / WORKER / tiny model
-> regression evidence
-> Independent Proof
-> certificate-aware promotion assessment
-> AWAITING_HUMAN_APPROVAL
-> Randy decides
-> separate explicit activation
```

The core itself forces human approval to remain absent during automated assessment.

It cannot approve Randy's decision for him.

A proposed improvement should reduce something measurable:
- model calls;
- latency;
- CPU/RAM;
- cost;
- owner intervention;
- ambiguity;
- failure rate;
- proof debt.

More code, models, or agents is not itself improvement.

## Workshop

Workshop is now a **front-end integration task**, not a blocker for the core engine.

GitHub Foundation branch:

`Karmicmurphy/Ollie_Twis_Holo_workshop@living-workshop-main-build`

GitHub Phase 1A is proven in test.

Randy's local Windows Workshop may be newer and remains private/local authority until reconciled.

Remaining Workshop work:
1. reconcile local Windows Workshop with the GitHub Foundation branch;
2. build thin Workshop -> Foundry job submission;
3. store `foundry_job_id` beside Workshop-local IDs;
4. display Builder evidence, AIOS runtime evidence, independent certificate, proof debt, and human-required action;
5. never let Workshop self-certify or auto-activate.

## Cross-repo identity

Use Foundry `job_id` as the machine-wide correlation key for Foundry-governed work.

Do not create another global ID.

## Next field boundary

The core is **OPERATIONAL_IN_TEST**, not yet PROVEN_LIVE on Randy's Windows machine.

The next strongest evidence is the first real local bounded job through the human-operated runner.

That local job should end at human review, not autonomous merge/deploy/activation.

Workshop reconciliation can proceed in parallel.

## Later continuity work

Estate delta checker remains useful but non-blocking:
- compare recorded authority heads to live heads;
- flag stale pointers/status contradictions;
- never auto-promote.

## Do not reopen

Do not redo Builder, AIOS wake, Independent Proof, or certificate promotion architecture unless new evidence invalidates their current proofs.

Build/use the smallest complete machine first.
