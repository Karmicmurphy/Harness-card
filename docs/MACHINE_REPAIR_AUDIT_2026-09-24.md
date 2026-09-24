# Machine Repair Audit — 2026-09-24

Status: ACTIVE REPAIR / EVIDENCE-DRIVEN

## Governing outcome

The owner should be able to speak naturally once. The machine must carry the integration burden from arrival to a bounded, evidence-backed outcome without requiring the owner to know which repo, skill, service, module, or category owns the problem.

Target loop:

```text
HUMAN SIGNAL
-> ARRIVAL
-> HARNESS / AUTHORITY
-> CANONICAL SKILL + CAPABILITY ROUTING
-> ESTATE / RECOVERY / SALVAGE
-> FOUNDRY
-> AIOS / BOUNDED EXECUTION
-> INDEPENDENT PROOF
-> WORKSHOP RESULT
-> LEARNING
-> UPDATED HARNESS
```

## Verified defects found in this audit

### 1. Harness learning ingestion was broken

Observed:
- `state/INCIDENT_LEDGER.md` contains multiple real incidents.
- generated `state/HARNESS_SCORECARD.json` reported zero incidents and zero learned rules.

Root cause:
- regex literals in `workers/self_improve.py` were double-escaped and did not match the Markdown ledger.
- the scheduled workflow only checked generated file headings, so empty learning could be recorded as a WIN.
- `tests/test_self_improve.py` existed but was not part of the PR authority guard.

Repair:
- corrected parser regexes;
- added fail-closed checks when populated ledgers recover zero records;
- strengthened semantic assertions;
- added self-improvement and skill-registry regressions to the PR guard;
- changed the scheduled learner to reject zero-incident / zero-rule output.

Evidence:
- Harness PR #9 branch CI executed `Harness self-improvement worker PASS`;
- canonical skill registry tests also passed.

### 2. Skill routing depended on agent interpretation

Observed:
- Harness routed to skills that canonically live in Digital Scrapyard;
- there was no machine-readable resolver establishing exactly which repo/path/ref a routed skill means.

Repair:
- added `config/skill_registry.json`;
- added `scripts/resolve_skill.py`;
- classified skills as procedural / conditional / executable / mapped-not-implemented;
- pinned external suite authority to the current Scrapyard SHA;
- ROUTING now requires canonical skill resolution before use.

Evidence:
- resolver regressions pass, including unknown-skill failure.

### 3. There was no explicit human-signal arrival contract

Observed:
- Foundry had a Human Intent Compiler, but intake began too close to technical intent/taxonomy for the desired owner experience.

Repair:
- added `foundry.human_signal`;
- preserves raw language and explicit constraints before taxonomy;
- requires grounded evidence phrases for semantic interpretation;
- explicitly forbids intake-time diagnosis/category lock;
- leaves unknowns as unknowns;
- added `tcf compile-human-signal`.

Evidence:
- Foundry PR #24 passed 171 tests and was merged into `software-builder-v0` at `3bb8e0d073f4bdda2af414340633a95b0e182887`.

### 4. Workshop and Foundry were not actually wired

Observed:
- current Workshop branch had no `foundry_job_id` or direct Foundry transport;
- Foundation authority already identified Workshop->Foundry integration as unfinished.

Repair in progress:
- added loopback-only Foundry HTTP service with `/health`, `/v1/human-signal`, and `/v1/route-intelligence`;
- added Workshop loopback Foundry bridge;
- added Workshop `/api/foundry/human-signal`;
- Foundry signal identity may be recorded in Workshop receipts.

Security boundary:
- no shell execution;
- no public binding;
- no remote Foundry endpoint;
- no automatic promotion or activation.

### 5. Local Windows remained a mapped-but-inaccessible source yard

Observed:
- estate map/queue was proven, but local Windows bytes were still the highest-value blocked source.

Repair in progress:
- added read-only source-yard inventory to Workshop;
- files may be hashed for duplicate/lineage detection without being copied;
- ZIP/TAR members are listed without extraction;
- secret-like/browser credential paths use existing skip policy;
- skipped directories are pruned before traversal;
- optional inventory manifests remain in local Workshop project storage.

Security boundary:
- inventory does not execute files;
- inventory does not extract archives;
- inventory does not upload source contents;
- inventory is local companion functionality.

## What is now substantially better

- governance has a deterministic skill-address layer;
- learning can no longer silently learn nothing from a populated ledger;
- rough human language has an explicit first-class arrival representation;
- Foundry has a loopback service surface;
- Workshop has a real transport boundary to Foundry;
- Workshop has a read-only adapter for the major blocked local source yard.

## Still not proven / do not overclaim

### A. Full natural-language-to-completed-job vertical slice
Not yet PROVEN_LIVE.

Current arrival can reach Foundry, but a rough human signal is not yet automatically:
- semantically interpreted;
- routed through canonical Harness skills;
- compiled into the correct Foundry job;
- executed via AIOS;
- independently certified;
- returned to Workshop under one visible correlation identity.

### B. Real Windows field trial
The source-yard inventory code must be exercised on Randy's actual Windows machine before calling Windows estate access PROVEN_LIVE.

### C. Human-facing Open Door UI
The Workshop API bridge exists, but the main human-facing surface still needs one simple input path that hides internal subsystem names.

### D. Learning closure
After Harness PR #9 merges, the scheduled/self-triggered learner must regenerate nonzero scorecard/rules on `main`. That generated state is the live proof of the repaired learning loop.

### E. Authority reconciliation
After Foundry and Workshop promotion, Harness authority SHAs must be updated to their new live heads before the repair work can close.

## Anti-reinvention decision

Do not create:
- another OS;
- another giant agent framework;
- another new repo for the arrival layer;
- a second skill suite;
- a second proof engine;
- a separate memory platform.

Repair the existing stack by completing its transmissions.

## New owner-level acceptance rule

A subsystem test is not a machine test.

The machine is only PROVEN_LIVE for a job class when:

```text
owner speaks naturally
-> machine preserves the signal
-> current authority is recovered
-> needed skills/capabilities resolve automatically
-> required sources are accessed
-> bounded work executes
-> independent proof evaluates the actual claim
-> Workshop returns an understandable result
-> owner is interrupted only for a genuine owner gate
-> learning/state updates prevent paying for the same failure again
```

## Core principle

**The human explains the problem once. The machine carries the integration burden.**
