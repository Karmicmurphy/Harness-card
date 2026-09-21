# Cross-Project System Boundary Map — V1

Date: 2026-09-20

Status: **RECONCILED WORKING BOUNDARY — NOT FINAL ARCHITECTURE AUTHORITY**

This map answers one narrow question: **who owns what, what may hand off to what, and what is actually missing?**

Live project truth outranks this file. Harness policy governs the work; this file does not create a new framework.

## 1. Role boundaries

| System | Owns | Does not own |
|---|---|---|
| **Harness Card** | Cross-project recovery, scope, policy, proof requirements, decision continuity, anti-drift | Runtime execution, coding, scheduling, certification implementation, artifact UI |
| **Twis Holo Workshop** | Human-facing artifact/engine cockpit, selected handoff packets, artifact return, human review, Workshop receipts | Global policy, capability promotion, independent certification, unrestricted runtime authority |
| **Temporal Capability Foundry** | Typed job/capability lifecycle, bounded Software Builder, evaluation, learning candidate, promotion, activation, rollback | Human cockpit, global governance, general scheduler authority, independent self-certification |
| **Untethered AIOS** | Bounded process lifecycle, cooperative scheduling, explicit capability grants/path scopes, runtime audit receipts | Global governance, Builder semantics, capability promotion, independent certification |
| **Digital Scrapyard** | Canonical salvage/rights/recombination/proof-gate method suite | Runtime scheduler, Builder execution, global proof authority, artifact cockpit |
| **CERT-RIVER / PRISM-RIVER / RiverKernel lineage** | Independent claim-proof/certificate discipline, quarantine, no-broadening, dirty-key honesty | Current live runtime authority; current executable certifier is not yet verified |

## 2. The working execution chain

For a future software-building path, the clean layering is:

```text
Randy / human authority
        |
        v
Harness scope + policy + proof requirement
        |
        v
Workshop selected artifact / handoff packet
        |
        v
Foundry typed job / Software Builder
        |
        v
AIOS bounded wake/schedule/grants  [MISSING ADAPTER; DO NOT BUILD YET]
        |
        v
Foundry development receipt/evaluation
        |
        v
Independent CERT-RIVER-style proof [EXECUTABLE CERTIFIER NOT VERIFIED]
        |
        v
Foundry promotion/activation may consume certificate as evidence
        |
        v
Workshop displays returned artifact + receipt + proof state
        |
        v
Randy decides permanent/destructive/publish/deploy actions
```

This is layering, not a requirement that every Workshop engine go through Foundry or AIOS. The chain above applies when the capability is a Foundry-governed software/capability build.

## 3. Explicit handoff contracts

### Harness -> everything
**Type:** governance constraint, not RPC.

Carries:
- recovered current truth;
- bounded target;
- allowed authority;
- proof requirement;
- stop/approval conditions.

Do **not** build a Harness service merely to make this machine-readable unless repeated evidence requires one.

### Workshop -> Foundry
**Current state:** conceptually compatible, **shared machine envelope not yet verified**.

Workshop already has:
- human-selected handoff packet;
- adapter boundary;
- artifact return;
- receipt rule.

Foundry already has:
- typed job/capability lifecycle;
- bounded Builder job input;
- explicit workspace/command policy.

**Missing:** a small shared handoff envelope if/when Workshop becomes the live Builder cockpit.

**Blocker:** GitHub Workshop may lag Randy's authoritative local Windows Workshop. Do not wire this adapter against stale Workshop state.

### Scrapyard -> Harness / Foundry
**Current state:** no new runtime adapter required.

Scrapyard is the canonical method source for:
- Artifact Compass;
- Artifact Salvage;
- Deep-Sea Salvage;
- Rights Gate;
- Recombination Forge;
- Proof Gate;
- Cost & Complexity Challenge;
- Thought Economy;
- Capability Downshift;
- Project Context Harvester;
- Rabbit-Hole Governor.

Foundry already has provenance-first salvage intake/registry. Harness may invoke the methods during work. Do not duplicate the skill suite.

### Foundry -> AIOS
**Current state:** **first genuine missing runtime interface**.

Needed contract:
- exact Foundry job/candidate identity;
- exact candidate workspace;
- explicit capability grants;
- allowed path scopes;
- max ticks/resource bound;
- worker entry point;
- return status/result;
- AIOS audit receipts linked back to Foundry evidence.

**Do not implement yet.** Builder must first earn a green real failure->repair->retest proof without weakening its gates.

### AIOS -> Foundry
**Current state:** same missing adapter, return side.

AIOS should return:
- process terminal state;
- result payload;
- capability-call audit receipts;
- denial/failure evidence;
- tick/resource termination evidence.

An AIOS receipt is runtime evidence, **not** a capability certificate.

### Foundry -> CERT-RIVER
**Current state:** contract reconciled, implementation blocked.

Input candidate:
- exact claim;
- content-pinned implementation;
- exact fixture;
- comparator/acceptance criteria;
- Builder/development receipt;
- declared proof debt.

Output:
- CERTIFIED / REJECTED / QUARANTINED;
- exact certificate boundary;
- trace/receipt references;
- proof debt;
- dirty-key basis when replay is lawful.

**Blocker:** exact archived executable CERT-RIVER primitives are not yet recovered as current code. Do not reimplement before recovery proves them unavailable.

### Foundry -> Workshop
**Current state:** generic artifact/receipt return exists conceptually; no shared cross-repo schema verified.

Workshop may display:
- candidate;
- proof running;
- certified;
- rejected;
- quarantined;
- proof debt;
- receipt/trace links.

Workshop must never infer or issue certification.

## 4. Receipt semantics — keep separate

- **Workshop receipt:** human-facing artifact/action record.
- **AIOS receipt:** runtime/process/capability audit.
- **Foundry receipt:** development/evaluation/promotion/activation evidence.
- **CERT-RIVER trace:** exact independent proof path.
- **CERT-RIVER certificate:** bounded decision on one exact claim.

Do not collapse these into one generic receipt type.

## 5. Forbidden bypasses

1. Workshop must not self-certify an engine or candidate.
2. Software Builder must not issue its own independent certificate.
3. AIOS process success must not equal Foundry promotion.
4. Foundry evaluation must not silently equal CERT-RIVER certification.
5. Scrapyard Proof Gate must not be relabeled as an executable certifier.
6. AIOS must not become a second global Harness.
7. Workshop must not bypass explicit human approval for publish/deploy/destructive/spend actions.
8. No new scheduler, proof database, agent framework, AI OS, or promotion engine is justified by this reconciliation.

## 6. Current blocker before interface work

The real Software Builder proof on Foundry branch `software-builder-v0` reached the bounded repair path against pinned Untethered-AIOS.

Observed in GitHub Actions run `35522934878`:
- Foundry unit tests: green;
- Ollama installed and reachable;
- model: `qwen2.5-coder:1.5b-instruct`;
- pinned AIOS baseline was green before fault injection;
- worker-owned initial failing test gate observed the injected path-containment failure;
- the Builder inspected `src/untethered_aios/capabilities.py`;
- the Builder changed that implementation file;
- tests were not edited;
- no passing retest was observed before `max_steps=10` was exhausted.

Therefore the current blocker is **loop-step efficiency / proof budget**, not missing model connectivity and not a reason to redesign the Builder.

## 7. Immediate bounded move

Run one minimal experiment before touching Builder architecture:

1. change only the proof harness `max_steps` from **10 to 12**;
2. keep the same pinned AIOS commit;
3. keep `repair_limit=2`;
4. keep the same required initial failing test;
5. keep tests immutable;
6. keep the same acceptance gate;
7. rerun the real Ollama proof.

Why 12: after an implementation edit, the minimum remaining useful actions are **retest + final**. Two extra action slots test the step-budget hypothesis without loosening any proof or repair gate.

If 12 still fails, do **not** blindly raise it again. Instrument/recover the action history and fix the smallest repeated-action cause before another policy change.

## 8. First interface to build after green proof

If the 12-step proof becomes green, the first bounded interface candidate is:

**Foundry -> AIOS Builder Wake Adapter V0**

It should do only this:

```text
Foundry job
+ candidate workspace
+ explicit grants/path scopes
+ tick/resource bound
-> AIOS process
-> Software Builder invocation
-> terminal state + runtime audit receipts
-> Foundry evidence
```

No autonomous deployment. No permanent agent. No new scheduler. No certification.

## 9. Deferred interfaces

- Workshop -> Foundry shared handoff envelope: wait until local Workshop authority is reconciled with GitHub.
- Builder -> CERT adapter: wait until exact CERT-RIVER implementation recovery is complete or proven unavailable.
- Workshop proof-state UI: wait until certificate producer/consumer contracts exist.

## 10. Verdict

The estate does **not** currently need another architecture layer.

The immediate sequence is:

```text
boundary map
-> 12-step Builder proof experiment
-> green real failure/repair/retest evidence
-> Foundry-to-AIOS wake adapter
-> independent certification recovery/adapter
-> Workshop cockpit integration after local authority reconciliation
```
