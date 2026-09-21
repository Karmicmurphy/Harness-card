# Foundation V0 — Current Work/Build Prompt

Use Harness Card. BUILD / RECONCILIATION MODE.

You are resuming Randy's **Foundation V0 — Human-Owned Software Factory**.

Do not redesign the architecture. Do not ask Randy to reconstruct history. Recover live repository truth first. Live repo/device evidence outranks this prompt.

## Canonical Foundation authorities

- Governance: `Karmicmurphy/Harness-card@main`
- Factory/Builder: `Karmicmurphy/temporal-capability-foundry@software-builder-v0`
- Runtime: `Karmicmurphy/Untethered-AIOS@main`
- Salvage: `Karmicmurphy/digital-scrapyard-autopilot@main`
- Cockpit: `Karmicmurphy/Ollie_Twis_Holo_workshop@living-workshop-main-build`

Anything outside these refs is SALVAGE / QUARANTINE / SEPARATE PROJECT until explicitly reconciled and promoted.

Read first in Harness:
- `state/CURRENT_PROJECT.json`
- `docs/FOUNDATION_V0_ACTIVATION_MAP_2026-09-21.md`
- `state/FOUNDATION_V0_ACTIVATION_MAP_2026-09-21.json`
- `docs/SYSTEM_BOUNDARY_MAP_V1.md`
- `state/SYSTEM_BOUNDARY_MAP_V1.json`
- `state/ESTATE_CAPABILITY_MAP_V1.json`
- `docs/RIVER_LINEAGE_RECONCILIATION_V1.md`
- `state/RIVER_LINEAGE_RECONCILIATION_V1.json`

Read in Foundry:
- `state/SOFTWARE_BUILDER_V0_AUTHORITY.json`
- `src/foundry/software_builder.py`
- `src/foundry/aios_adapter.py`
- `contracts/software_builder_receipt.schema.json`
- `scripts/run_software_builder_deterministic_proof.py`
- `scripts/run_foundry_aios_wake_proof.py`

## Current proven Foundation state

### Cog 1 — deterministic real-repository Builder
**PROVEN_IN_TEST**

Proof run: `35611616345`

Verified:
- pinned real Untethered-AIOS baseline green;
- deliberate implementation fault produced failing tests;
- actual SoftwareBuilder preloaded the repair target;
- deterministic/no-model engine used the same Builder action boundary as model engines;
- Builder made one worker-authored source edit;
- automatic retest passed;
- no tests were edited;
- receipt had no remaining proof gates.

### Cog 1B — model patch-brain lane
**OPTIONAL / NON-BLOCKING**

Sanitized action-attempt diagnostics are implemented.

Local models are replaceable compute, not control-plane authority.

Do not increase model turn budgets blindly. Diagnose/bake-off later using the Adaptive Pass Rule if this lane still matters.

### Cog 2 — Foundry -> AIOS Wake Adapter V0
**PROVEN_IN_TEST**

Proof run: `35612271813`

Pinned AIOS: `8a954439af2b15b00f7c961d83552772b382fd1f`

Verified:
- Foundry `job_id` correlates AIOS process/audit evidence;
- declared scoped capability works inside candidate workspace;
- out-of-scope capability is denied and audited;
- terminal runtime result returns to Foundry;
- tick-limit evidence carries the job correlation;
- tick-limited process is cancelled to terminal state;
- no certification, promotion or deploy authority was granted.

Do not redo Cogs 1 or 2 unless live evidence shows regression.

## CURRENT WORK LANE — COG 3

### Independent Proof / CERT-RIVER lane

First perform one **bounded recovery checkpoint** for usable executable CERT-RIVER primitives.

Search the internal estate before writing replacement code:
- Harness River lineage files;
- canonical Foundation repos;
- historical branches/repos only as SALVAGE;
- exact proof/certificate/quarantine mechanisms.

Use the Adaptive Pass Rule. Do not perform indefinite archaeology.

If a current usable executable certifier is recovered:
- reuse/adapt it behind the recovered exact-claim certificate contract;
- preserve provenance and rights;
- prove the adapter independently.

If bounded recovery does **not** yield a current usable executable certifier:
build the smallest independent verifier.

Minimum independent verifier input:
- `foundry_job_id`;
- exact claim ID and claim text;
- candidate path/reference;
- exact candidate content hash;
- exact fixture/workspace;
- deterministic acceptance command(s);
- forbidden-file policy;
- proof debt declared before execution.

Minimum behavior:
1. operate outside SoftwareBuilder;
2. independently recompute/verify the candidate hash;
3. independently rerun exact acceptance;
4. verify forbidden-file/policy conditions;
5. record evidence/trace references;
6. emit exactly one bounded verdict:
   - CERTIFIED
   - REJECTED
   - QUARANTINED
7. preserve proof debt;
8. never deploy, promote, publish or broaden one claim into whole-tool certification.

Builder test success is not certification.
AIOS runtime success is not certification.
A receipt is not automatically a certificate.

## NEXT AFTER COG 3 GREEN — COG 4

Verify Foundry promotion/activation consumes independent proof where certification is required.

For certificate-required capabilities:

```text
NO CERTIFICATE -> NO ACTIVATION
REJECTED -> NO ACTIVATION
QUARANTINED -> NO ACTIVATION
CERTIFIED -> may become promotion evidence, not automatic activation
```

Rollback must remain available.

## THEN

Cog 5:
- reconcile authoritative local Windows Workshop with GitHub Foundation branch;
- protect private DBs, secrets, credentials and personal archives.

Cog 6:
- thin Workshop <-> Foundry handoff/result-return adapter;
- reuse Foundry `job_id`;
- show Builder evidence + AIOS evidence + independent proof + proof debt + Randy-required action.

Cog 7:
- estate delta checker; flag stale authority, never auto-promote.

Cog 8:
- Capability Downshift candidate loop only after Cogs 1-6 work end-to-end.

## Side-project isolation

Loop Deck / Pro Rig, First3 Local, Digital Scrap Forge product/payment branches, Coilside, Terri Tax, and other side projects are not Foundation authority.

A side-project lesson becomes global only after salvage, scope/rights/evidence review, proof, and explicit promotion.

## Adaptive research

Use Digital Scrapyard `skills/salvage-suite/ADAPTIVE_PASS_RULE.md`.

PASSES MUST EARN PASSES.

If a bounded test teaches more than another search pass: TEST BEATS SEARCH.

## Truth labels

Use:
PLANNED / INSPECTED / CHANGED / COMMITTED / TESTED / PROVEN_IN_TEST / DEPLOYED / PROVEN_LIVE / BLOCKED / UNVERIFIED.

Never collapse them.

## Safe autonomous work

You may inspect, make branch-local code fixes, run tests, repair failing tests, build proof harnesses/adapters, and update non-sensitive authority records.

Stop for Randy before production deploy, public publish, destructive deletion, spending, secrets, irreversible external state, or changing human approval boundaries.

## Startup action

Return a compact live table:

```text
COMPONENT | REF | LIVE SHA | TEST/PROOF STATE | STALE AUTHORITY? | NEXT ACTION
```

Check Harness, Foundry, AIOS, Scrapyard, and Workshop Foundation branch.

Then proceed directly into Cog 3. Do not wait for Randy unless a genuine human-authority gate is required.

## Closeout

Before ending, persist exact:
- repos/branches/SHAs;
- commits;
- files changed;
- workflow run IDs;
- tests and proof results;
- blockers;
- current Cog;
- next bounded action;
- any uncommitted/unpushed work.

The next session must resume without Randy reconstructing anything.

**Recover live truth. Do not redo proven Cogs. Finish Cog 3, prove it, update authority, then move to the next earned Cog.**
