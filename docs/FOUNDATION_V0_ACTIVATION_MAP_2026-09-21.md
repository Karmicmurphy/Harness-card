# Foundation V0 Activation Map — 2026-09-21

Status: **INTEGRATION / PROOF — NOT END-TO-END FUNCTIONAL**

Purpose: one current checklist for turning the existing repository estate into the first functional human-owned software factory without creating another framework.

This file does not replace live project authority. Repositories and device-local truth outrank this map.

## Foundation roles

| Layer | Authority | Current role | Current state |
|---|---|---|---|
| Human authority | Randy | final irreversible/publish/deploy/spend decisions | ACTIVE |
| Governance | Karmicmurphy/Harness-card | recover truth, scope work, set proof/approval boundaries | ACTIVE |
| Cockpit | Karmicmurphy/Ollie_Twis_Holo_workshop | human job/artifact surface, receipts, returned results | GITHUB PHASE 1A PROVEN IN TEST; LOCAL WINDOWS STATE UNRECONCILED |
| Factory | Karmicmurphy/temporal-capability-foundry | typed jobs, Builder, evidence, evaluation, promotion/rollback | DETERMINISTIC REAL-REPOSITORY BUILDER PROVEN IN TEST; MODEL PATCH LANE OPTIONAL |
| Runtime | Karmicmurphy/Untethered-AIOS | bounded processes, capability grants, path scopes, audit | FOUNDRY JOB CORRELATION / SCOPES / TICK-LIMIT WAKE PROVEN IN TEST |
| Salvage | Karmicmurphy/digital-scrapyard-autopilot | Artifact Compass/Salvage/Rights/Recombination/Adaptive Pass | VERIFIED GREEN |
| Independent inspection | CERT-RIVER contract lineage + minimal current certifier | rerun exact claim outside Builder, certify/reject/quarantine | CONTRACT RECOVERED; CURRENT EXECUTABLE LANE MISSING |

## One important simplification

**Do not make a local LLM the gate for activating deterministic factory plumbing.**

The first foundation proof should separate:

1. **Builder plumbing proof** — real repository, deterministic/no-model repair, automatic retest, honest receipt.
2. **Patch-brain proof** — optional replaceable model proposes a narrow patch.

If the deterministic real-repository Builder proof is green, Foundry -> AIOS wiring may proceed while Qwen/Granite/other patch-brains are benchmarked separately.

The model is compute, not authority and not the control plane.

## Existing identity pieces — reuse, do not invent

Foundry already owns:
- `job_id` in `contracts/job/job.schema.json`;
- `evidence_id + job_id` in `contracts/evidence/evidence.schema.json`;
- `proof_id + target_id` in `contracts/proof/proof.schema.json`.

Workshop already has job IDs and receipt storage.

AIOS already has `pid`, `ProcessRecord.metadata`, and hash-addressed audit receipts.

### Foundation correlation rule

Use **Foundry `job_id` as the cross-repo correlation key** for Foundry-governed work.

Do not create a second global job ID.

Required mappings:
- Workshop job/artifact -> `foundry_job_id`;
- AIOS `ProcessRecord.metadata["foundry_job_id"]`;
- AIOS audit receipt detail -> `foundry_job_id`;
- Foundry evidence already uses `job_id`;
- independent proof details -> `foundry_job_id` plus exact target hash/id;
- Workshop returned artifact/receipt -> `foundry_job_id`.

Local IDs remain local:
- Workshop job ID stays Workshop-local;
- AIOS pid stays runtime-local;
- proof target stays exact candidate/hash;
- Foundry job ID ties the chain together.

## Connection matrix

### Harness -> all
**Link type:** policy/document authority only.
**Code adapter required:** NO.
**Fix:** keep authority maps current; do not turn Harness into a service.

### Scrapyard -> Harness / Foundry
**Link type:** method/registry reuse.
**Code adapter required:** NO for Foundation V0.
**Current:** Adaptive Pass Rule verified green.
**Fix:** Rights Gate and warehouse dispositions must travel with salvaged candidates; no license laundering by snippets.

### Workshop -> Foundry
**Link type:** thin job-envelope adapter.
**Code adapter required:** YES, but after local Workshop/GitHub reconciliation for the final cockpit.
**Reuse:** Foundry CompiledJob contract rather than inventing a new job model.
**Minimum mapping:** project/artifact refs, goal, constraints, risk/approval posture, acceptance tests, `foundry_job_id`.
**Do not:** make Workshop promotion/proof authority.

### Foundry -> Software Builder
**Link type:** existing internal capability.
**Current:** **PROVEN_IN_TEST** for deterministic real-repository plumbing.
**Proof:** run `35611616345`.
**Verified:** real pinned repo baseline, injected failure, bounded worker edit, automatic passing retest, honest worker-authored `files_changed`, no test edits.
**Model lane:** sanitized action-attempt diagnostics are implemented; local patch models remain replaceable optional compute.

### Foundry -> AIOS
**Link type:** bounded runtime adapter.
**Current:** **PROVEN_IN_TEST**.
**Proof:** run `35612271813` against AIOS `8a954439af2b15b00f7c961d83552772b382fd1f`.
**Verified:** Foundry job correlation, allowed scoped call, out-of-scope denial, terminal result, correlated audit receipts, tick-limit evidence, terminal cancellation.
**Non-goals preserved:** no deploy, promotion, certification, or permanent-agent authority.

### AIOS -> Foundry
**Link type:** same adapter return side.
**Current:** **PROVEN_IN_TEST** for runtime result/audit correlation.
**Rule:** runtime success remains evidence, not certification.

### Foundry -> Independent Proof
**Link type:** exact claim/fixture/candidate handoff.
**Code adapter/runtime required:** YES.
**First:** bounded recovery checkpoint for usable archived CERT-RIVER primitives.
**If recovery does not produce a current executable certifier:** build the smallest independent verifier.
**Verifier V0 must:** pin target/hash, rerun exact acceptance outside Builder, verify forbidden files/policy conditions, emit CERTIFIED/REJECTED/QUARANTINED with bounded scope.
**Do not:** let Builder self-certify.

### Independent Proof -> Foundry promotion
**Link type:** certificate consumption.
**Code change/verification required:** YES.
**Fix:** verify promotion requires the expected independent proof for capabilities that declare it; never translate ordinary passing tests into a certificate.

### Foundry -> Workshop result return
**Link type:** artifact/evidence presentation.
**Code adapter required:** YES after local Workshop reconciliation.
**Return:** result artifact/diff, Builder receipt, AIOS runtime receipt, independent proof verdict/debt, status.
**Human gate:** deploy/publish/permanent/destructive/spend stays Randy-controlled.

## Cog order

### Cog 0 — Truth and continuity
State: **MOSTLY DONE**
- boundary map exists;
- estate map exists;
- warehouse exists;
- Adaptive Pass Rule exists and CI is green;
- Workshop Phase 1A GitHub proof is recorded;
- stale 10/12-step Builder story removed.

Remaining:
- keep one activation map current;
- reconcile local Windows Workshop to GitHub before final cockpit wiring.

### Cog 1 — Deterministic real-repository Builder
State: **PROVEN_IN_TEST** — run `35611616345`
Acceptance:
- pinned real repository starts green;
- deliberate implementation fault makes target tests fail;
- deterministic/no-model engine performs one bounded implementation repair through Builder tools;
- Builder automatically retests;
- targeted test passes;
- no tests edited;
- receipt attributes only worker-authored changes;
- no deploy/publish.

This proves factory plumbing without depending on a model.

### Cog 1B — Patch-brain diagnostics/bake-off
State: **DIAGNOSTICS IMPLEMENTED / OPTIONAL PARALLEL LANE**
Latest Qwen proof `35595297143`: red; failure observed, target preloaded, `files_changed=[]`, blocked after 3 model turns.

Next:
- expose action attempts/rejections;
- rerun once;
- if socket issue -> smallest socket repair;
- if model issue -> bounded bake-off.

Candidate order:
1. NO MODEL / structural rule;
2. Qwen2.5-Coder 0.5B;
3. Qwen2.5-Coder 1.5B baseline;
4. Granite 350M;
5. SmolLM2 360M;
6. other permissive candidates only if they earn a pass;
7. Liquid only after Rights Gate clears exact terms.

Winner is per job class, not global.

### Cog 2 — Foundry -> AIOS Wake Adapter V0
State: **PROVEN_IN_TEST** — run `35612271813`.
Acceptance:
- exact Foundry job ID enters AIOS;
- only declared grants/path scopes are available;
- worker cannot escape workspace or call ungranted capability;
- tick/resource bound terminates cleanly;
- AIOS returns result + audit evidence linked to job ID.

### Cog 3 — Independent Proof Lane V0
State: **NEXT / MISSING**
Acceptance:
- executes outside Builder;
- pins exact target/hash and acceptance fixture;
- checks forbidden file touches and deterministic policy conditions;
- reruns acceptance;
- outputs CERTIFIED / REJECTED / QUARANTINED for one exact claim;
- cannot deploy or promote.

### Cog 4 — Promotion consumption gate
State: **PARTIAL / VERIFY**
Acceptance:
- Foundry promotion reads independent verdict where required;
- no certificate -> no activation for certificate-required capability;
- rejection/quarantine blocks activation;
- rollback remains available.

### Cog 5 — Workshop/local reconciliation
State: **OPEN**
Acceptance:
- authoritative Windows Workshop compared file-by-file with GitHub branch;
- intentional differences recorded;
- current local code synchronized or explicitly retained local-only;
- private databases/secrets/raw personal data remain out of GitHub.

### Cog 6 — Workshop -> Foundry / result return
State: **MISSING**
Acceptance:
- Workshop submits a Foundry-compatible job using existing contract;
- returned evidence is understandable from the cockpit;
- all records share Foundry job ID;
- user sees changed / works / does not work / proven / unproven;
- human remains final deploy/publish gate.

### Cog 7 — Estate delta updater
State: **MISSING BUT NOT BLOCKING FIRST MACHINE**
Purpose: stop authority maps from rotting.
Minimum:
- read declared repo/branch heads;
- compare to last recorded authority;
- flag stale pointers/status contradictions;
- never promote automatically.

### Cog 8 — Capability Downshift / learning loop
State: **DO NOT ACTIVATE UNTIL COGS 1-6 WORK**
Allowed evolution:
```text
successful trace
-> repeated pattern
-> candidate rule/script/worker/tiny model
-> regression test
-> independent proof
-> human-controlled promotion
```

Improvement must reduce at least one measurable burden:
- model calls;
- latency;
- CPU/RAM/cost;
- owner intervention;
- ambiguity;
- failure rate;
- proof debt.

More agents/models/code alone is not improvement.

## Parts available now

### Already owned and suitable for foundation
- Foundry typed job/evidence/proof contracts;
- Foundry Builder bounded workspace/tools/automatic retest;
- AIOS process states/tick bounds/grants/audit;
- Workshop artifact revisions/receipts/history/capsules;
- Scrapyard Artifact Compass/Salvage/Rights/Recombination/Adaptive Pass;
- Harness governance/recovery/boundary maps.

### Warehouse candidates — acquire only when a cog needs them
- ast-grep — structural localization/rewrite, MIT;
- Tree-sitter — parsing/symbol localization, MIT;
- Agentless / mini-SWE-agent atoms — loop/reference, MIT;
- SWE-bench concepts — repair benchmark, MIT;
- BitNet runtime/embedding candidates — MIT;
- Qwen/Granite/SmolLM permissive tiny-model candidates;
- NASA/LLNL component/interface/monitoring patterns per Rights Gate.

Do **not** install/vendor every candidate now. A warehouse is useful because parts stay on the shelf until a test earns them.

## Definition of first functional machine

Foundation V0 is functional when one real bounded software job can travel:

```text
Workshop or direct Foundry intake
-> Foundry job_id + scope/acceptance
-> AIOS bounded wake/grants
-> Builder deterministic tools + optional patch brain
-> automatic tests
-> Foundry development evidence
-> independent proof
-> Foundry activation decision
-> Workshop/result surface
-> Randy final irreversible decision
```

and every transition can answer:
- what exact job is this?
- what code/artifact was touched?
- who/what performed the action?
- what permissions existed?
- what tests ran?
- what independently proved the claim?
- what remains unproven?
- what requires Randy?

## Current first move

**Cog 3: perform one bounded recovery checkpoint for usable executable CERT-RIVER primitives.**

If that bounded recovery does not yield a current usable independent certifier, implement the smallest verifier that pins the exact claim/candidate/hash/fixture, reruns acceptance outside Builder, checks forbidden-file/policy conditions, and emits only CERTIFIED / REJECTED / QUARANTINED with proof debt.

The model patch-brain lane may continue in parallel but does not block Foundation integration.
