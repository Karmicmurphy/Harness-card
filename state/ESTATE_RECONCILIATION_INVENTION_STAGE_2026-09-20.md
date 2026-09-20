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
