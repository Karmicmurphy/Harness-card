# Estate Reconciliation -> Invention Stage

Date: 2026-09-20

Status: **PLANNING / RECONCILIATION — BOUNDED IMPLEMENTATION ALLOWED**

## Purpose

This state note exists so future AI sessions do not confuse the current cross-project work with a finished architecture.

Randy is still deciding the final shape of the larger system. The immediate job is to recover and reconcile the existing estate well enough that invention can proceed from verified capabilities instead of memory, duplicate work, or repo-by-repo guessing.

This file is a **current workstream marker**, not a new architecture authority.

## Existing recovery authority

Do not create replacement recovery systems before reading the existing sources:

1. `docs/SYSTEM_LINEAGE_START_HERE.md`
2. `docs/FIVE_YEAR_ARTIFACT_SALVAGE_MASTER_CONTEXT.md`
3. `state/ESTATE_COVERAGE_LEDGER.md`
4. `docs/ECOSYSTEM_RECOVERY_MASTER_CONTEXT_2026-09-19.md`
5. `state/ECOSYSTEM_AUTHORITY_INDEX.json`
6. `state/DECISIONS.md` — especially **RECOVER BEFORE REBUILD**

Live project truth still comes from the relevant project repo/branch/device/deploy.

## Capability map now exists

First capability-first reconciliation artifacts:

- `state/ESTATE_CAPABILITY_MAP_V1.json` — machine-readable capability/authority/overlap/invention map.
- `docs/ESTATE_CAPABILITY_MAP_V1.md` — human-readable reconciliation and first invention candidates.
- `state/RIVER_LINEAGE_RECONCILIATION_V1.json` / `docs/RIVER_LINEAGE_RECONCILIATION_V1.md` — recovered CERT-RIVER / PRISM-RIVER / RiverKernel contract reconciliation.
- `state/SYSTEM_BOUNDARY_MAP_V1.json` / `docs/SYSTEM_BOUNDARY_MAP_V1.md` — live cross-project ownership, handoff, receipt-semantics, missing-interface, and next-proof map.
- `state/FRANKENSTEIN_WAREHOUSE_V0.json` / `docs/FIVE_PASS_FOUNDATION_SALVAGE_2026-09-21.md` — five-pass Artifact Compass/Salvage/Rights/Recombination result: deterministic-first foundation, external candidate registry, legal dispositions, and current build sequence.

Use these as an extension of the existing recovery chain, not as replacement authority. Reverify live project truth before making current-state claims.

Current V1 findings include:

- Workshop already contains the human-facing artifact/engine cockpit primitives;
- Foundry already contains the typed capability lifecycle and bounded Software Builder;
- AIOS already contains reusable scheduler/process/capability-grant/audit primitives;
- Digital Scrapyard already contains the canonical salvage/rights/recombination method suite;
- CERT-RIVER / PRISM-RIVER / RiverKernel remain the major unresolved independent-certification lineage;
- the Software Builder has moved past the old 10/12-step-budget hypothesis. Deterministic controls now own the failing test, declared target preload, post-edit retest, and change provenance; the live unresolved gate is one real schema-constrained narrow patch through the local model socket.

Boundary reconciliation still identifies **Foundry -> AIOS Builder Wake Adapter V0** as the first missing cross-repo runtime interface, but the adapter remains deferred until the narrower Builder repair proof is green. The active Builder direction is **deterministic-first / Agentless-style**: localize and preload mechanically, ask the model only for a bounded patch, retest mechanically, and keep proof separate. Do not resurrect the 10->12 step-budget experiment; it was disproven and is historical only.

The Digital Scrapyard now carries an active shared `skills/salvage-suite/ADAPTIVE_PASS_RULE.md`. Future research depth is evidence-adaptive: passes must earn passes, two directionally different low-yield passes trigger saturation, and bounded testing replaces searching when it will reduce more uncertainty.

## Current direction

The working direction is:

`recover estate -> reconcile overlaps -> map capabilities -> identify missing interfaces -> generate invention candidates -> prove bounded candidates -> promote only what earns authority`

The system should eventually answer without Randy reconstructing history:

- What do I already have?
- Where is it?
- What actually works?
- What failed but contains reusable parts?
- What overlaps or supersedes what?
- What can be recombined?
- What paid capability can be replaced with existing low-cost/free/local parts?
- What new thing can be built from capabilities already owned?

## Planning-stage rule

The final architecture is **not locked**.

Planning may continue as new evidence is recovered.

However, planning status is **not a freeze on useful implementation**.

Bounded implementation is allowed when it:

- improves recovery, indexing, lineage, capability discovery, proof, or handoff quality;
- extends an existing canonical mechanism instead of creating a parallel framework;
- is reversible and narrowly scoped;
- does not silently promote a hypothesis into architecture authority;
- leaves evidence of what changed and why;
- respects project boundaries and current live authority.

Examples of allowed work during this stage:

- correcting stale authority pointers;
- extending the estate/capability index;
- adding machine-readable capability metadata;
- reconciling duplicated proof/certification mechanisms;
- improving restart/handoff pointers;
- adding small adapters between already-proven components;
- writing tests/validators that prevent rediscovery or false completion.

Examples that require stronger evidence before implementation:

- creating a new core framework;
- replacing Harness Card, Foundry, AIOS, CERT-RIVER/PRISM-RIVER, or Workshop authority;
- merging whole projects;
- deleting duplicate/failed artifacts before lineage is understood;
- granting autonomous deploy/spend/delete authority;
- locking a final "self-improving AI" architecture before the estate is reconciled.

## Important recovered overlap

Existing proof/certification, routing, execution, learning, and salvage mechanisms overlap across:

- CERT-RIVER / PRISM-RIVER / RiverKernel lineage;
- Harness Card;
- Temporal Capability Foundry;
- Untethered AIOS;
- Digital Scrapyard salvage suite;
- Twis Holo Workshop.

Therefore the next job is **reconciliation and reuse**, not another parallel system.

## Current practical target

The immediate cross-project target is to make the estate legible enough that AI does not require Randy to remember repository names, old chats, branches, or buried mechanisms.

After that, begin the invention pass:

> **What useful capability or product can be produced by recombining verified parts Randy already owns?**

Candidates are allowed to be unusual, playful, cheap, local-first, or commercially useful. Surprise is welcome; surprise authority is not.

## Relationship to active project state

`state/CURRENT_PROJECT.json` and `state/ACTIVE_WORK_ORDER.md` may still point to a specific active product/project such as TWIS Loop Deck.

That is not a contradiction.

This file records a **cross-project estate workstream** that can coexist with a specific active project. It does not replace project-specific authority.

## Exit condition

This planning/reconciliation stage can advance when:

1. major current repos and recovered historical lineages are represented in the estate authority map;
2. overlapping core mechanisms are classified as authority / reusable primitive / historical / superseded / unresolved;
3. a usable capability map exists;
4. future sessions can recover the estate without Randy manually naming buried work;
5. at least one invention candidate is produced from recovered capabilities rather than from a blank-slate design.

Until then, report this workstream as:

**PLANNING / RECONCILIATION — BOUNDED IMPLEMENTATION ALLOWED**
