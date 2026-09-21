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

Read in Foundry:
- `state/SOFTWARE_BUILDER_V0_AUTHORITY.json`
- `src/foundry/software_builder.py`
- `contracts/software_builder_receipt.schema.json`
- `scripts/run_software_builder_deterministic_proof.py`
- `scripts/run_software_builder_ollama_proof.py`
- `tests/test_software_builder.py`

## Non-negotiable design law

Deterministic machinery before model intelligence.

Models are replaceable compute, not authority.

Use Foundry `job_id` as the cross-repo correlation key.

Proof before promotion. Human authority before irreversible action.

## Startup action

Return a compact live table:

```text
COMPONENT | REF | LIVE SHA | TEST/PROOF STATE | STALE AUTHORITY? | NEXT ACTION
```

Check Harness, Foundry, AIOS, Scrapyard, and Workshop Foundation branch.

Then proceed without waiting unless a human-authority gate is required.

## Current work lane

### Cog 1A — Builder action diagnostics

Builder receipts should record sanitized action-attempt evidence:
- attempt number
- action kind
- target path
- action/schema shape validity
- policy accepted/rejected
- tool result
- replace_exact matched yes/no
- rejection classification
- short sanitized error

Do not store full patch payloads or secrets merely for diagnostics.

Verify the current branch actually contains this contract and that unit CI is green.

### Cog 1B — deterministic real-repository Builder proof

This is the Foundation activation gate if it is not already green.

Pinned source:
`Karmicmurphy/Untethered-AIOS@17a717e556a639d450551d7cf3b9a77d6a1b459e`

The proof must:
1. establish green baseline;
2. inject the known temporary path-containment fault into `src/untethered_aios/capabilities.py`;
3. observe failing target tests;
4. use actual `SoftwareBuilder`;
5. preload the declared repair target;
6. use a deterministic/no-model engine through the same Builder action boundary used by model engines;
7. apply one bounded repair through Builder tools;
8. automatically rerun the target tests;
9. pass;
10. edit no tests;
11. honestly record only worker-authored file changes;
12. emit a machine-readable receipt.

Do not direct-edit the repair outside Builder.

If Cog 1B is green, update authority and move immediately to Cog 2. Do not restart architecture review.

### Model patch lane

The Qwen/Ollama lane is optional compute, not the Foundation control plane.

Use the new action-attempt diagnostics to classify its exact failures.

Do not increase turn budgets blindly.

If model/socket diagnosis is still unresolved, use the Adaptive Pass Rule and a bounded tiny-model bake-off later. It must not block deterministic runtime integration.

## Cog 2 — Foundry -> AIOS Wake Adapter V0

Build only after deterministic Builder proof is green.

Input:
- `foundry_job_id`
- exact candidate workspace
- worker entry point
- explicit CapabilityGrant set
- path scopes
- max ticks/resource bounds
- Builder policy

AIOS must place `foundry_job_id` in `ProcessRecord.metadata` and runtime audit evidence.

Return:
- pid
- terminal ProcessState
- result/error
- denials
- tick/resource termination
- audit receipts linked to Foundry job

Foundry converts runtime truth into evidence.

AIOS success is not certification.

## Cog 3 — independent proof

First perform bounded recovery for usable CERT-RIVER primitives.

If a current executable certifier cannot be recovered within that bounded pass, implement the smallest independent verifier that:
- runs outside Builder;
- pins exact candidate/hash and fixture;
- reruns acceptance;
- checks forbidden-file/policy conditions;
- emits CERTIFIED / REJECTED / QUARANTINED for one exact claim;
- records proof debt;
- cannot deploy or promote.

## Cog 4 onward

Then:
- verify Foundry promotion consumes required independent proof;
- reconcile local Windows Workshop vs GitHub Foundation branch;
- build thin Workshop <-> Foundry handoff/result return;
- add estate delta checker;
- only after Cogs 1-6 work, enable Capability Downshift candidate loop.

## Side-project isolation

Loop Deck / Pro Rig, First3 Local, Digital Scrap Forge product branches, Coilside, Terri Tax, and other side projects are not Foundation authority.

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

## Closeout

Before ending, persist exact:
- repos/branches/SHAs
- commits
- files changed
- workflow run IDs
- tests and proof results
- blockers
- current Cog
- next bounded action
- any uncommitted/unpushed work

The next session must resume without Randy reconstructing anything.

**Recover live truth, finish the current Cog, prove it, update authority, then continue to the next earned Cog.**
