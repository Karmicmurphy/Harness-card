# Cross-Project System Boundary Map — V1

Date: 2026-09-21

Status: **FOUNDATION CORE V0 OPERATIONAL_IN_TEST**

Live repo/device truth outranks this file.

## Current usable core

```text
human bounded job
-> Foundry job_id
-> AIOS process/job correlation
-> Software Builder policy + repair/test
-> Independent Proof V0
-> CERTIFIED / REJECTED / QUARANTINED
-> human review
```

Real human-operated runner proof:
- run `35628459336`
- proof head `b84db3579ff7d62095c40b6c2a8830fec7557e11`
- result: success
- normal terminal state: `CERTIFIED_AWAITING_HUMAN_REVIEW`
- model required: false
- auto activation/deploy/publish/spend: false

## Ownership

| System | Owns | Does not own |
|---|---|---|
| Harness | recovery, scope, policy, proof requirements, continuity | runtime/coding/certifier |
| Foundry | job identity, Builder, evidence, independent proof, promotion/activation/rollback | human cockpit, global governance |
| AIOS | process lifecycle, runtime correlation, grants/audit primitives | Builder semantics, promotion, certification |
| Workshop | human-facing cockpit/artifacts/receipts | certification, promotion, global authority |
| Scrapyard | salvage/rights/recombination/adaptive research methods | runtime/certifier |
| Randy | irreversible and permanent decisions | delegated automatic approval |

## Important runtime truth

Builder's own proven workspace/command policy currently mediates Builder file/test operations.

AIOS wraps the Builder process for lifecycle and `foundry_job_id` correlation, but does **not** currently mediate every Builder tool call through AIOS CapabilityGrant.

That is explicit proof debt, not hidden architecture.

## Proof integrity

Builder tests and Independent Proof acceptance use isolated Python bytecode caches.

Strict proof-integrity run:
`35627957323`

Derived bytecode artifacts are recorded but excluded from changed-path authority. Other unexpected changes still count.

## Ordinary work vs factory improvement

Ordinary software work ends at certified human review.

Capability improvement is opt-in and separate:

```text
repeated proven traces
-> candidate cheaper capability
-> regression evidence
-> independent certificate
-> promotion assessment
-> human approval
-> separate explicit activation
```

This is human-owned Capability Downshift, not self-evolving AI.

## Workshop status

Workshop is no longer a blocker for the core engine.

It remains the desired human-facing front end.

Open work:
1. reconcile Randy's authoritative local Windows Workshop with `living-workshop-main-build`;
2. add a thin front-end adapter to the proven Foundation core;
3. store/display `foundry_job_id`, Builder evidence, AIOS evidence, certificate, proof debt, and human-required action;
4. never let Workshop self-certify or auto-activate.

## Current field boundary

**Next strongest evidence:** run the first real bounded local job on Randy's machine through the human-operated exact-patch runner.

The result must stop at human review.

Do not reopen the core architecture unless new proof invalidates it.
