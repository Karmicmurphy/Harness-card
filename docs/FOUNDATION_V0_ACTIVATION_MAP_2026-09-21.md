# Foundation V0 Activation Map — 2026-09-21

Status: **INTEGRATION / PROOF — COGS 1 THROUGH 4 PROVEN IN TEST; NOT YET END-TO-END FUNCTIONAL**

Live repo/device truth outranks this map.

## Current chain

```text
Randy
-> Workshop
-> Harness
-> Foundry
-> AIOS
-> Independent Proof
-> Foundry Promotion / Activation
-> Workshop
-> Randy
```

Digital Scrapyard remains the salvage / rights / research / recombination department beside this chain.

## Canonical refs

- Governance: `Karmicmurphy/Harness-card@main`
- Factory: `Karmicmurphy/temporal-capability-foundry@software-builder-v0`
  - authority head: `cd4bae186250eaf5bb49d10c8257869921ad38ea`
  - latest functional proof head: `c25eaac464968ae5d1654affc9e75318b03acff9`
- Runtime: `Karmicmurphy/Untethered-AIOS@8a954439af2b15b00f7c961d83552772b382fd1f`
- Salvage: `Karmicmurphy/digital-scrapyard-autopilot@028f1a9559a7f198d73e7042d18b9c8343f64729`
- Cockpit GitHub candidate: `Karmicmurphy/Ollie_Twis_Holo_workshop@living-workshop-main-build`
  - head: `29deb23f917199b09b17d6b87a2f33c40657ea79`
  - local Windows Workshop remains private authority pending reconciliation.

## Identity rule

Use **Foundry `job_id`** as the cross-repo correlation key.

- Workshop keeps its own IDs and stores `foundry_job_id`.
- AIOS keeps its PID and stores `ProcessRecord.metadata["foundry_job_id"]`.
- AIOS audit evidence carries `foundry_job_id`.
- Foundry evidence already keys by `job_id`.
- Independent proof binds `foundry_job_id` + exact `claim_id` + exact candidate hash.

Do not create another global job ID.

## Proven cogs

### Cog 1 — Deterministic real-repository Builder
**PROVEN_IN_TEST**

Proof run: `35611616345`

Verified:
- pinned real repo baseline green;
- deliberate failure injected;
- failing test observed;
- declared repair target preloaded;
- bounded worker edit through Builder tools;
- automatic retest passed;
- no test edits;
- honest worker-authored `files_changed`;
- no deploy/publish.

### Cog 1B — Patch-brain diagnostics
**DIAGNOSTICS IMPLEMENTED / OPTIONAL LANE**

Qwen diagnostic run: `35611616512`

Result: **failure / non-blocking**.

Sanitized action-attempt diagnostics exist. Local patch models remain replaceable compute and do not gate Foundation activation.

### Cog 2 — Foundry -> AIOS Wake Adapter V0
**PROVEN_IN_TEST**

Proof run: `35612271813`

Pinned AIOS: `8a954439af2b15b00f7c961d83552772b382fd1f`

Verified:
- Foundry job correlation into AIOS;
- scoped capability allow;
- out-of-scope denial;
- correlated audit evidence;
- terminal result;
- tick-limit evidence;
- tick-limited process cancellation;
- no certification/promotion broadening.

### Cog 3 — Independent Proof V0
**PROVEN_IN_TEST**

Proof run: `35620771601`

Proof head: `c9fdad6e41ed6ffad6f34ec1b7f079b0c9439cd9`

Verifier: `independent-proof-v0.2`

Verified:
- exact candidate hash pinning;
- changed-path boundary;
- forbidden-path quarantine;
- disallowed-command quarantine;
- proof-execution mutation quarantine;
- normal untracked runtime artifacts do not falsely trigger quarantine;
- exact passing candidate -> `CERTIFIED`;
- exact failing candidate -> `REJECTED`;
- integrity/policy violation -> `QUARANTINED`;
- certifier cannot edit/deploy/promote/activate/broaden claim.

### Cog 4 — Promotion certificate-consumption gate
**PROVEN_IN_TEST**

Test run: `35620968656`

Proof head: `c25eaac464968ae5d1654affc9e75318b03acff9`

When policy requires independent certification:
- missing certificate -> promotion BLOCKED;
- `REJECTED` -> BLOCKED;
- `QUARANTINED` -> BLOCKED;
- `CERTIFIED` must match expected `foundry_job_id`;
- `CERTIFIED` must match expected `claim_id`;
- activation still requires an APPROVED promotion assessment;
- `auto_activate=false` remains enforced.

## Remaining cogs

### Cog 5 — Workshop local/GitHub reconciliation
**NEXT / OWNER-DEVICE DEPENDENT**

Need:
- compare authoritative local Windows Workshop with `living-workshop-main-build`;
- identify newer/local-only files;
- record intentional differences;
- keep secrets, private DBs, personal archives, credentials, and raw private data out of GitHub;
- establish which code snapshot is safe to wire.

Do not assume GitHub is newer than the local Workshop.

### Cog 6 — Workshop -> Foundry handoff / result return
**MISSING AFTER COG 5**

Reuse existing contracts. Do not create a second job architecture.

Minimum submission:
- goal;
- project/artifact reference;
- constraints;
- risk / approval posture;
- acceptance tests.

Foundry returns / correlates:
- `job_id`;
- Builder receipt;
- AIOS runtime evidence;
- independent certificate;
- proof debt;
- promotion/activation state;
- changed files / result artifact.

Workshop stores `foundry_job_id` beside its local records and displays proven/unproven state without self-certifying.

### Cog 7 — Estate delta checker
**MISSING / NOT FIRST-MACHINE BLOCKER**

Purpose:
- compare recorded repo/branch heads with live heads;
- flag stale SHAs/status contradictions;
- never auto-promote.

### Cog 8 — Capability Downshift
**DEFER UNTIL COGS 5–6 COMPLETE**

Allowed path:

```text
successful trace
-> repeated pattern
-> candidate rule/script/worker/tiny model
-> regression test
-> independent proof
-> promotion
-> human-controlled activation
```

Improvement must reduce measurable burden such as model calls, latency, cost, CPU/RAM, owner intervention, ambiguity, failure rate, or proof debt.

More agents/models/code is not automatically improvement.

## First functional-machine definition

Foundation V0 becomes end-to-end functional when one real bounded software job can travel:

```text
Workshop intake
-> Foundry job_id
-> AIOS bounded wake
-> Builder
-> automatic test evidence
-> Independent Proof
-> certificate-aware promotion
-> Workshop result surface
-> Randy irreversible-action gate
```

and every transition can answer:
- exact job?
- exact artifact/hash?
- exact permissions?
- exact changed files?
- exact tests?
- exact independent proof?
- exact remaining debt?
- exact human-required action?

## Current next move

**Cog 5 first: reconcile the authoritative local Windows Workshop with the GitHub Foundation branch.**

Then immediately build **Cog 6: the smallest Workshop -> Foundry job/result adapter**.

Do not reopen Cogs 1–4 unless new evidence breaks their proofs.
