# FOUNDATION V0 — START HERE FOR CODE

This file is an operator handoff, not a second authority source.

Canonical state remains:
- `state/CURRENT_PROJECT.json`
- `state/ACTIVE_WORK_ORDER.md`
- `OPERATING_CONTRACT.md`
- `ROUTING.md`

If this file conflicts with those canonical files, follow the canonical files.

## What this project actually is

**FOUNDATION V0 — HUMAN-OWNED SOFTWARE FACTORY**

It is not one app and it is not one repository. It is a governed machine composed of several existing repositories with distinct roles:

- **Harness-card** — governance, routing, authority, state, promotion rules, learning guardrails.
- **temporal-capability-foundry** — bounded software factory / job execution / compilation path.
- **Untethered-AIOS** — runtime execution layer.
- **digital-scrapyard-autopilot** — salvage and source-recovery tooling; not the runtime.
- **Ollie_Twis_Holo_workshop** — Workshop / cockpit / phone-facing operator surface.
- **Independent Proof** — certification/verdict lane that must remain separate from the executor.

Separate projects such as Spatial Cognitive Territory, Rusty Phasewire / Pro Rig, Coilside, First3 Local, commerce branches, and other experiments are not Foundation authority unless explicitly promoted through Harness.

## Current overall state

**Status: ACTIVE**  
**Evidence state: PARTIALLY_PROVEN**  
**Current lane: INTEGRATION REPAIR / PHONE RESULT RETURN**

The core problem is no longer “build the engine.” Major components already exist and several internal/bounded flows are proven in CI.

The machine is not yet proven end to end from the owner’s phone.

The reason this has dragged on is primarily continuity and integration drift: individual parts advanced on different repos/branches while older work orders and handoffs kept sending later sessions backward or treating already-built components as missing. The 2026-09-27 cohesion repair explicitly identified this as a continuity/integration failure, not evidence that the engine should be replaced.

Do not start another architecture.

## Approved Foundation refs

Use the canonical refs in `state/CURRENT_PROJECT.json` as authority.

Current approved refs recorded there:

- Governance: `Karmicmurphy/Harness-card` / `main`
- Factory: `Karmicmurphy/temporal-capability-foundry` / `software-builder-v0` / `e0e14e689b1d3a3bda1356276975b4b34f1b615e`
- Runtime: `Karmicmurphy/Untethered-AIOS` / `main` / `8a954439af2b15b00f7c961d83552772b382fd1f`
- Salvage: `Karmicmurphy/digital-scrapyard-autopilot` / `main` / `a059a27ef2bd662827a51da44dd8efb8863d634c`
- Cockpit: `Karmicmurphy/Ollie_Twis_Holo_workshop` / `living-workshop-main-build` / approved `1785ed1405e769a17ec22066dc1e27a40dbf153b`

Observed Workshop branch head is newer than the approved cockpit pin. Advancement alone is **not** promotion. Review the delta before changing the approved SHA.

## What is already proven

Do not rebuild these just because another session cannot immediately see them.

1. Foundation core exists and is operational in test.
2. Open Door compile-job path has been proven in test and merged.
3. Unified job correlation through AIOS -> builder -> proof has been proven in test and merged.
4. The bounded Foundry phone-job runner exists.
5. Foundry default-branch dispatcher exists and is pinned to the approved Foundry SHA.
6. Unknown fixture rejection before execution has already been demonstrated.
7. Independent Proof produced a certified verdict on the approved bounded fixture.
8. One remote GitHub run already produced a correlated job identity and certified receipt for `aios-path-containment`.

Important limitation: that proof was a PR-triggered / GitHub workflow proof. It was **not** a real phone-originated Workshop round trip.

## The actual missing integration

The next gate is exactly:

`PAGES_BOUNDED_JOB_ROUND_TRIP`

The observed Workshop/Pages branch still lacks the complete bounded-job dispatch and receipt-return path needed for the phone flow.

Known remaining gaps in canonical state:

- `PAGES_DISPATCH_AND_RECEIPT_ROUTES_NOT_IMPLEMENTED_IN_OBSERVED_BRANCH`
- `AUTHENTICATED_PAGES_DEPLOYMENT_NOT_VERIFIED`
- `ARBITRARY_NATURAL_LANGUAGE_TO_CERTIFIED_RESULT_NOT_PROVEN`

The third item is **not** a prerequisite for the bounded phone round trip. General natural-language coding is later work.

## What must happen next

Do this in order.

### 1. Establish the real local workspace

This Code session is attached to the owner’s Windows computer.

Find the existing local copies of the Foundation repos. Do not create replacement repos. Do not move/delete anything until you know what is authoritative.

Workshop documentation says local Windows is private authority and GitHub may be behind local. Therefore compare the local Workshop tree against the GitHub `living-workshop-main-build` branch before modifying Workshop.

Record:
- local repo paths
- current branches
- HEAD SHAs
- dirty/uncommitted changes
- untracked files
- nested Git roots
- anything secret/private that must not be committed

If there is no clean parent workspace, create only a workspace/container folder for Code. Do not turn that parent folder into a new competing architecture or authority repo.

### 2. Reconcile Workshop local vs GitHub

Preserve legitimate local work.

Classify meaningful differences as:
- LOCAL_NEWER_KEEP
- GITHUB_NEWER_KEEP
- SAME
- CONFLICT_REVIEW
- GENERATED_OR_DISPOSABLE
- SECRET_PRIVATE_DO_NOT_COMMIT

Do not overwrite the local Workshop with GitHub wholesale.
Do not commit secrets, tokens, databases, cookies, browser profiles, private archives, or runtime state.
Do not force-push uncertain history.

### 3. Finish the bounded phone round trip

Use the existing architecture and existing Foundry dispatcher.

Required path:

PHONE
-> WORKSHOP / OPEN DOOR
-> one canonical job_id
-> approved Foundry bounded job
-> AIOS / execution
-> Independent Proof
-> correlated receipt
-> WORKSHOP / PHONE
-> human review
-> Harness learning only after proof

The same job identity must survive dispatch, execution, proof, receipt, and display. GitHub `workflow_run_id` is transport identity, not a replacement for the Foundation `job_id`.

### 4. Add only the missing Pages boundary

Use the existing Cloudflare Pages / Pages Functions direction already selected by the project state.

Do not add another queue, D1 database, Worker architecture, orchestration framework, or Cloudflare migration just to finish this gate.

The phone UI must show at minimum:
- SUBMITTED
- PENDING
- RUNNING
- PASSED
- FAILED
- REJECTED
- proof/receipt location

Reload/status recovery must work.
Duplicate dispatch must be safe/idempotent.
Unknown fixtures must be rejected before execution.

### 5. Prove the real end-to-end path

Do not call DONE from local tests or an isolated Actions run.

Prove:

**Approved success**
- authenticated owner action originates in Workshop on phone-facing path
- approved `aios-path-containment` job dispatches
- same job_id propagates end to end
- execution occurs
- Independent Proof returns verdict
- correlated receipt returns to Workshop
- Workshop shows PASSED and proof

**Forbidden/unknown input**
- rejected before execution
- visible as rejected
- cannot be recorded as success

**Controlled failure**
- visible as FAILED
- no false proof/promotion

**Retry / duplicate dispatch**
- no silent contradictory outcomes
- attempt history/correlation remains intact

Record exact deployment URL, workflow run URL/ID, job_id, commit SHAs, proof verdict, receipt artifact, and human-review state.

## Definition of done for the current gate

The current gate is DONE only when:

1. Owner opens the existing Workshop on Android.
2. Owner authenticates.
3. Owner starts the approved bounded fixture.
4. Workshop displays progress.
5. The request reaches the existing Foundry dispatcher pinned to approved authority.
6. Execution occurs.
7. Independent Proof evaluates it.
8. The same Foundation job_id returns with the exact correlated receipt.
9. Workshop displays the result/proof after normal use and reload/status recovery.
10. Unknown and failed jobs cannot become success.
11. No automatic activation occurs.
12. Evidence is recorded back into Harness only after proof.

Until this passes, Foundation remains `PARTIALLY_PROVEN`.

## Do not waste time on these before the current gate passes

Parked / later work:
- arbitrary natural-language coding beyond the approved bounded fixture
- broad model relay work
- Luna/Sol/Astra routing upgrades
- quantum/free-compute experiments
- another orchestration framework
- broad salvage/re-inventory
- Spatial repairs
- music / Pro Rig
- commerce lanes
- Cloudflare `cf` CLI migration
- another Worker/D1/queue architecture

Foundry PR #31 already contains a coding-engine candidate. Review it after the bounded phone round trip instead of reinventing general coding.

## Rules for Code / Astra / agents

- Start from canonical Harness state, not chat memory.
- Inspect before modifying.
- Use sub-agents if useful, but keep one lead agent accountable for the final truth.
- Reuse existing components before creating anything new.
- Make small, reversible commits.
- No force push over uncertain history.
- No automatic authority promotion.
- No secret/private data in public source.
- No claiming capabilities from scaffolding alone.
- Executor does not certify itself.
- Models may propose; Foundry validates; Independent Proof verifies; owner approves.
- If blocked, identify the exact blocked step and one concrete owner action. Do not return a vague list of possibilities.

## Why Harness is the starting repo

Harness is the governance and continuity spine. It answers:
- what project is active
- which repos/refs are authority
- what is proven vs merely observed/candidate
- what the one active gate is
- what is parked
- what may be promoted

Do not treat Harness as the place all code must physically live. It is the authority/index for the multi-repo Foundation machine.

## First commandment for the next session

**Do not restart the project. Resume the one active gate from `state/ACTIVE_WORK_ORDER.md`.**
