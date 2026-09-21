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

### Foundry -> independent proof / CERT-RIVER lineage
**Current state:** contract reconciled; executable current certifier not yet verified.

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

**Recovery rule:** first perform a bounded recovery checkpoint for the archived CERT-RIVER implementation because recovered proven machinery outranks reinvention. If exact usable primitives are recovered, reuse them behind this contract.

**Stop rule:** archive recovery may not become an indefinite blocker. If the bounded recovery checkpoint cannot recover a current executable certifier, build the smallest independent proof lane from the reconciled contract: pin candidate/hash, rerun acceptance outside Builder, verify forbidden-file/policy conditions, and issue a bounded certificate verdict. Do not broaden that lane into another framework.

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

The original 10-step and 12-step hypotheses are superseded by later evidence.

Verified sequence on Foundry branch `software-builder-v0`:
- real Ollama/Qwen connectivity works;
- the pinned Untethered-AIOS baseline is green before deliberate fault injection;
- the worker owns the initial failing test gate;
- the worker now owns automatic post-edit retesting;
- declared repair targets are preloaded deterministically before a model repair turn;
- the normal Foundry unit suite is green for those deterministic controls;
- a later proof exposed malformed/truncated free-form JSON from the coding model, not a missing scheduler or a reason to widen model authority;
- receipt provenance also required correction so pre-existing dirty workspace files are not falsely attributed as worker-authored edits.

The active experiment replaces loose model action JSON with a schema-constrained **narrow repair action** while retaining the same failing fixture, immutable tests, bounded workspace, and automatic retest.

Therefore the current model-patch blocker is **why three schema-constrained repair turns produced no accepted worker edit**. That is now a patch-brain/socket problem, not a reason to block deterministic factory plumbing.

## 7. Immediate bounded move

Split the proof into two independent questions:

1. **Foundation plumbing control:** prove the same pinned real-repository failure -> repair -> automatic retest loop with a deterministic/no-model repair engine.
2. **Patch-brain lane:** instrument each model action attempt/rejection, then decide whether to repair the socket or run the tiny-model bake-off.

Do not let a flaky replaceable model become the gate for scheduler/permission integration. The model is compute, not the control plane.

The Digital Scrapyard adaptive pass rule is now the discovery-depth authority:
`skills/salvage-suite/ADAPTIVE_PASS_RULE.md`.

## 8. First interface to build after green proof

If the deterministic real-repository Builder control becomes green, the first bounded interface candidate is:

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
-> deterministic/no-model real-repository Builder control
-> Foundry-to-AIOS wake adapter
-> independent proof/certifier lane
-> Workshop cockpit integration after local authority reconciliation
-> patch-brain bake-off as a replaceable capability lane
-> Capability Downshift only from repeated proven traces
```
