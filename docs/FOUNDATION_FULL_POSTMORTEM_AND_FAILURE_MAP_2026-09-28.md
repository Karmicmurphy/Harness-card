# Foundation V0 — Full Postmortem, Failure Map, and Anti-Repeat Contract

Date: 2026-09-28
Status: DURABLE POSTMORTEM / NON-AUTHORITATIVE ANALYSIS

> Canonical authority still lives in `state/CURRENT_PROJECT.json`, `state/ACTIVE_WORK_ORDER.md`, `OPERATING_CONTRACT.md`, and `ROUTING.md`. This file explains how the project got here, why it repeatedly looped, what can still fail, and what the finished system is actually supposed to let the owner do.

---

# Executive answer

Foundation V0 is not supposed to be another chatbot, another repo, another operating system, or another agent framework.

It is supposed to become a **human-owned continuity and software-work factory** where the owner can speak naturally once, from a simple phone-facing Workshop/Open Door, and the machine handles the technical translation, current-state recovery, bounded execution, proof, and return path without forcing the owner to know which repo, model, skill, workflow, service, branch, or deployment owns the task.

The intended normal loop is:

```text
OWNER SAYS WHAT HE WANTS
-> WORKSHOP / OPEN DOOR PRESERVES THE RAW SIGNAL
-> HARNESS RECOVERS CURRENT AUTHORITY + RULES
-> FOUNDRY COMPILES ONE BOUNDED JOB
-> AIOS CORRELATES/RUNS THE BOUNDED PROCESS
-> BUILDER/TOOLS DO THE WORK
-> INDEPENDENT PROOF CHECKS THE RESULT
-> ONE RECEIPT RETURNS UNDER THE SAME job_id
-> WORKSHOP SHOWS WHAT HAPPENED AND WHAT NEEDS OWNER REVIEW
-> HARNESS LEARNS ONLY FROM VERIFIED OUTCOMES
```

The owner should **not** have to choose Luna vs Sol vs Astra, find the right repository, name a workflow, remember a SHA, understand GitHub Actions, know Cloudflare routing, or rebuild project context every new chat.

That is the real product.

The project has taken too long because the pieces were often individually improved faster than the connections between them, while authority/state lived on several surfaces at once. New sessions repeatedly rediscovered old work, followed stale handoffs, mistook tests for live proof, introduced alternate architectures before closing the current gate, or proved fixed fixtures without proving the actual owner path.

This was primarily a **continuity, integration, and evidence-discipline failure**, not a lack-of-code failure.

---

# 1. How this project came to exist

## 1.1 The original problem was continuity, not software

The durable origin is simple:

- useful work was scattered across chats, repos, drives, folders, devices, archives, notes, music, images, and experiments;
- AI could help intensely inside one session but often lost the working relationship when the chat, model, app, context window, repo, or tool changed;
- every restart pushed reconstruction work back onto the human;
- repeated reconstruction caused duplicated effort, stale assumptions, lost decisions, fake finishes, and momentum loss.

The governing insight became:

> The model is replaceable. The working relationship is not.

From that came the desire for a layer that preserves:

- what the owner meant;
- what changed;
- what was accepted/rejected;
- what was proven/failed;
- where authority lives;
- what deserves continuity;
- what should retire;
- what can proceed automatically;
- what still requires owner judgment.

## 1.2 The behavior existed before the names

The project did not begin as one clean architecture. It grew from recurring behaviors:

- search before rebuilding;
- salvage mechanisms from old work;
- compare candidates;
- preserve provenance;
- prove before promoting;
- keep the owner above irreversible decisions;
- convert repeated reasoning into cheaper deterministic machinery.

Those behaviors later received names:

- Harness Card
- Artifact Compass
- Artifact Salvage / Deep-Sea Salvage
- Digital Scrapyard
- Temporal Capability Foundry
- AIOS
- Independent Proof / CERT
- Workshop / TWIS / Open Door
- Thought Economy / Capability Downshift
- Rights Gate / Proof Gate

The naming helped specialization but also created a new failure mode: the names could look like separate products instead of mechanisms serving one owner loop.

---

# 2. What Foundation V0 actually is now

## 2.1 Current role split

The intended split is:

| Role | System | Owns | Must not own |
|---|---|---|---|
| Governance / continuity | Harness-card | current project state, routing, authority, proof requirements, recovery, durable lessons | runtime, coding, certification |
| Human cockpit | Ollie_Twis_Holo_workshop | arrival, owner interaction, artifacts, status, receipts | global authority, self-certification, auto-activation |
| Factory | temporal-capability-foundry | job identity, compilation, Builder policy, evidence, proof integration, promotion/rollback contracts | human cockpit, global governance |
| Runtime | Untethered-AIOS | bounded process lifecycle, runtime correlation, grants/audit primitives | Builder semantics, global authority |
| Salvage/research | digital-scrapyard-autopilot | source recovery, rights, mechanism extraction, candidate discovery | runtime authority, proof authority |
| Independent verifier | Independent Proof / CERT lane | verifies the actual claim independently of the executor | execution, owner approval |
| Permanent authority | Owner | irreversible decisions, approval, value judgments | routine orchestration burden |

This division is sound. The failure was not primarily that these roles were wrong; it was that their state, wiring, and proof levels repeatedly drifted apart.

## 2.2 Current canonical state

At the time of this postmortem, Harness records Foundation V0 as:

- project: `FOUNDATION V0 — HUMAN-OWNED SOFTWARE FACTORY`
- evidence: `PARTIALLY_PROVEN`
- lane: `INTEGRATION REPAIR / PHONE RESULT RETURN`
- active gate: `PAGES_BOUNDED_JOB_ROUND_TRIP`

Approved component refs recorded by Harness include:

- Foundry `software-builder-v0` at `e0e14e689b1d3a3bda1356276975b4b34f1b615e`
- AIOS `main` at `8a954439af2b15b00f7c961d83552772b382fd1f`
- Salvage `main` at `a059a27ef2bd662827a51da44dd8efb8863d634c`
- Workshop approved pin `1785ed1405e769a17ec22066dc1e27a40dbf153b`, while the observed Workshop branch has advanced beyond that pin and requires review before promotion

The bounded Foundry workflow has already demonstrated a certified fixed fixture and correlated identity in GitHub Actions. What remains unproven is the actual owner-facing phone round trip through the existing Workshop/Pages surface.

---

# 3. The intended finished user experience

When Foundation V0 is actually finished for its first useful job class, the owner should be able to do this:

1. Open Workshop/Open Door from Android.
2. Say or type the job in ordinary language.
3. See that the request was received under one visible job identity.
4. Leave the internal routing to the machine.
5. See clear state: submitted, pending, running, proof pending, passed, failed, or rejected.
6. Receive an understandable result.
7. Open the proof/receipt without hunting through GitHub.
8. Be asked only for a real owner decision when necessary.
9. Retry safely without creating contradictory hidden outcomes.
10. Return later and recover the same job/history without reconstructing the project.
11. Start a new chat/model/session without explaining the entire machine again.
12. Have failures become durable prevention so the same class of failure is less likely to recur.

For later job classes, the same outer loop should support more than the original fixed proof fixture, but each class must be promoted separately through evidence.

The owner should **not** need to:

- pick the repo;
- pick the skill;
- pick the model;
- pick the agent;
- pick the execution host;
- know the current SHA;
- know GitHub Actions syntax;
- know Cloudflare internals;
- run terminal commands for normal work;
- manually copy proof from one system to another;
- remember which old handoff is current;
- decide whether a stale document is authoritative;
- sit through another architecture rewrite because one transport link is missing.

---

# 4. Chronology of the major architecture shifts

This project became difficult partly because the target was refined while implementation was already moving.

## Phase A — continuity/recovery problem

Initial emphasis:

- preserve useful context across AI sessions/tools;
- recover prior work before rebuilding;
- salvage mechanisms from old projects;
- make current truth outrank remembered truth.

Useful result:

- Harness/authority ideas;
- Artifact Compass/Salvage concepts;
- provenance and proof thinking.

Failure mode introduced:

- many valuable concepts developed before one narrow end-to-end product path was locked.

## Phase B — bounded software factory

The architecture hardened into:

```text
Harness -> Foundry -> AIOS -> Builder -> Independent Proof -> Human review
```

Important progress:

- bounded jobs;
- job IDs;
- deterministic fixtures;
- Builder policy;
- independent certification;
- no automatic activation.

Failure mode introduced:

- subsystem proof began to look emotionally like machine completion even though Workshop/owner arrival was not connected.

## Phase C — Workshop/Open Door arrival

The target shifted toward:

```text
human signal -> Workshop/Open Door -> Foundry compile -> execution -> proof -> Workshop result
```

Important progress:

- human-signal representation;
- compile-job path;
- loopback Foundry bridge;
- Workshop receipt/storage concepts;
- one visible owner surface became the goal.

Failure discovered:

- Workshop and Foundry were still not actually connected through the full executable path;
- some capabilities compiled but were not dispatchable/executable;
- proof did not return to the Workshop under one owner-visible identity.

## Phase D — phone-first/cloud doorway

Windows-local-first thinking was reduced because an always-on owner PC is a poor prerequisite for a phone control surface.

The architecture converged toward:

```text
Android -> Cloudflare Pages Workshop -> authenticated Pages Function -> GitHub dispatcher -> pinned Foundry -> AIOS/Builder/Proof -> receipt -> Pages/phone
```

Important correction:

- Cloudflare is a doorway/field shell, not authority;
- Windows remains private/local authority and source yard where needed;
- GitHub runner is ephemeral execution transport;
- `job_id` is execution identity;
- `workflow_run_id` is transport identity.

Failure mode introduced:

- Cloudflare Worker, D1, Workers AI, Access, standalone Worker, and other infrastructure options were repeatedly explored as if they might solve the missing integration by themselves.

## Phase E — cohesion repair

A major repair finally named the real systemic problem:

- components advanced on different surfaces;
- stale files kept sending new sessions backward;
- old SHAs/blockers survived newer proofs;
- generated state could agree with itself while being stale against live repos;
- one work order mixed multiple unrelated stop conditions.

This led to:

- `CURRENT_PROJECT.json` as the canonical current project source;
- generated `ACTIVE_WORK_ORDER.md` and related projections;
- authority guard improvements;
- observed vs approved vs candidate refs;
- explicit one-next-gate discipline.

This is the most important continuity repair so far.

---

# 5. What has gone wrong — complete failure taxonomy

## 5.1 Authority fragmentation

### Symptom
Different chats/docs/repos/local folders each appeared to describe the current system.

### Root problem
There was no single enforced source that every later session had to recover before acting.

### Consequences
- stale SHAs became instructions;
- obsolete blockers survived after fixes;
- already-proven work was rebuilt;
- branch advancement was mistaken for approved authority;
- local Windows state and remote GitHub state could diverge.

### Prevention
- `state/CURRENT_PROJECT.json` is canonical for active Foundation state;
- derived files must be generated/validated from it;
- live repo/device truth outranks historical docs;
- observed branch movement never auto-promotes authority.

---

## 5.2 Handoff decay

### Symptom
A correct handoff became wrong because the repo changed after it was written.

### Root problem
Static prose was used as if it were live state.

### Consequences
- new sessions resumed from yesterday's problem;
- old “next steps” reopened closed gates;
- repeated “start over” behavior.

### Prevention
Every handoff must contain:
- creation date;
- source SHAs;
- evidence level;
- invalidation rule;
- pointer to canonical live state;
- explicit “historical if live state differs” language.

A handoff without an invalidation rule is historical narrative, not control state.

---

## 5.3 Subsystem proof mistaken for machine proof

### Symptom
Tests passed, a workflow ran, or a receipt existed, so the project sounded “done.”

### Root problem
Evidence levels were not consistently tied to the owner path.

### Consequences
- repeated fake finishes;
- owner opened the real interface and discovered the gap;
- trust eroded even when individual components were genuinely good.

### Prevention
Use the evidence ladder strictly:

```text
CLAIMED
IMPLEMENTED_UNPROVEN
PARTIALLY_PROVEN
PROVEN_IN_TEST
PROVEN_LIVE
```

For user-facing flows, rendered behavior on the target device outranks source, unit tests, build output, deployment status, and mockups.

---

## 5.4 Fixed-fixture proof overgeneralized

### Symptom
A deterministic `aios-path-containment` fixture proved the engine path, then the language drifted toward “the machine can do jobs.”

### Root problem
A proof for one job class was treated as proof of arbitrary work.

### Consequences
- natural-language coding appeared closer than it was;
- later sessions tried to extend before the bounded phone path itself was live.

### Prevention
Evidence must always name the exact proven job class and scope.

Example:

`PROVEN_IN_TEST: EXACT_PATCH_FIXTURE_ONLY`

is not equivalent to:

`PROVEN_LIVE: ARBITRARY_NATURAL_LANGUAGE_SOFTWARE_JOB`.

---

## 5.5 Arrival disconnected from execution

### Symptom
Workshop/Open Door could accept input, but the request did not reliably become a real executable Foundry job with a returned proof receipt.

### Root problem
The front door and factory evolved separately.

### Consequences
- bridge code existed without complete transport;
- `compile-job` could produce identity without generic dispatch;
- UI could suggest capability not connected to runtime.

### Prevention
The owner path must be treated as one contract, not separate frontend/backend tasks.

No arrival feature is “working” until it has:

```text
input -> accepted identity -> dispatch -> execution -> proof -> result retrieval -> owner display
```

---

## 5.6 Correlation identity confusion

### Symptom
Different systems had signal IDs, intent IDs, job IDs, process IDs, GitHub workflow run IDs, receipt IDs, artifact IDs.

### Root problem
Transport identity and semantic job identity were not always clearly separated.

### Consequences
- difficult debugging;
- duplicate outcomes;
- uncertainty about whether proof belongs to the initiating request.

### Prevention
- one canonical `job_id` across the owner-visible execution/proof lifecycle;
- `workflow_run_id` is transport metadata only;
- preserve signal/intent IDs only as lineage;
- every receipt/proof must bind to the canonical `job_id` and source revision.

---

## 5.7 Retry/idempotency risk

### Symptom
A phone action, browser retry, network timeout, refresh, or duplicate dispatch can submit the same work more than once.

### Root problem
Distributed systems naturally retry, while early flows were designed around happy-path single execution.

### Possible consequence
- conflicting receipts;
- double work;
- one failed and one passed run under confusing identities;
- accidental side effects once jobs become less fixture-like.

### Prevention
- explicit idempotency key using job/attempt semantics;
- immutable attempt history;
- safe dedupe before side effects;
- concurrency grouping where appropriate;
- never overwrite prior outcome silently.

---

## 5.8 Executor grading itself

### Symptom
The same code that performs work can be tempted to label itself successful based on its own checks.

### Root problem
Convenience collapses execution and verification.

### Consequence
False confidence and self-certification.

### Prevention
Independent Proof remains structurally separate. Builder tests are evidence; independent proof is the certification gate. Owner approval remains above both.

---

## 5.9 Model/agent architecture churn

### Symptom
Luna/Sol/Astra, Friday/Jarvis, local Qwen/Llama/Liquid models, agent swarms, producer/foreman/judge roles, and other intelligent layers repeatedly entered the discussion before the base transport loop was closed.

### Root problem
Interesting intelligence options were allowed to become architecture before being necessary to the current stop condition.

### Consequences
- moving goalposts;
- new abstractions;
- more state to govern;
- harder completion.

### Prevention
Models are workers, not authority.

Routing belongs inside already-bounded job contracts after the baseline round trip is proven.

Prefer:

```text
deterministic routine -> cheap model -> stronger model -> human
```

only when evidence justifies escalation.

---

## 5.10 Infrastructure rabbit holes

### Symptom
Cloudflare Workers, Pages, D1, Workers AI, AI Gateway, standalone orchestration, Kaggle/free compute, quantum resources, local always-on servers, and other infrastructure repeatedly became possible “solutions.”

### Root problem
A missing narrow integration link was reframed as a platform problem.

### Consequences
- architectural resets;
- credential work before product proof;
- additional deployment surfaces;
- more failure modes.

### Prevention
Cost & Complexity Challenge before infrastructure.

Ask:

1. Does the current stop condition require this?
2. Is there already an existing component that does enough?
3. Does this remove a proven bottleneck or merely create options?
4. Can it be added later behind a stable contract?

If not required, park it.

---

## 5.11 Local Windows authority ambiguity

### Symptom
Workshop documentation said local Windows was private authority while GitHub was code backup/deploy source, yet remote agents often only saw GitHub.

### Root problem
The highest-value local state was not always available to the agent doing the planning.

### Consequences
- risk of overwriting newer local work;
- repeated reconciliation stalls;
- source-yard inventories mistaken for proof of local contents;
- confusing statements about what “the current Workshop” meant.

### Prevention
Separate three questions:

1. **Source authority** — where private/current source is allowed to live.
2. **Deploy authority** — what exact commit is deployed.
3. **Observed remote state** — what an agent can currently verify.

Never infer local equivalence from GitHub.
Never require Windows to be an always-on runtime just because it is private source authority.

---

## 5.12 Repo contamination / wrong-root risk

### Symptom
At least one Foundry/local workflow resolved into or near an unrelated parent Git root with large unrelated staged/deletion state.

### Root problem
Folder identity and Git root identity were not established before mutation.

### Consequences
- catastrophic accidental commit/deletion risk;
- source history confusion;
- false diff/reconciliation results.

### Prevention
Before modifying local repos:

- resolve absolute workspace path;
- resolve `git rev-parse --show-toplevel`;
- verify expected remote;
- verify branch;
- inspect dirty status;
- fail closed if identity differs from expected;
- never flatten nested independent Git histories without explicit decision.

---

## 5.13 Generated-state self-consistency without external truth

### Symptom
Generated Harness files could agree with each other while all being stale relative to live repos.

### Root problem
Validation tested internal projection consistency but not enough external observation.

### Consequences
A clean authority check could still represent yesterday.

### Prevention
Two separate checks:

- **projection integrity:** all derived files match canonical state;
- **observation drift:** approved refs compared read-only against named live branches/deploys.

UNKNOWN must remain UNKNOWN when access is unavailable.

---

## 5.14 Learning loop silently learning nothing

### Symptom
Incident ledger contained real failures while generated Harness scorecard showed zero incidents/rules.

### Root problem
Parser bug plus weak semantic guard.

### Consequences
The very mechanism designed to stop repeated failures could report success while ingesting nothing.

### Prevention already added
- fail closed on populated-ledger/zero-record contradiction;
- semantic assertions;
- self-improvement regressions in authority guard;
- scheduled learner rejection of zero-output false success.

General lesson:
A “learning system” needs measurable learning output, not just a successful workflow status.

---

## 5.15 Skill routing ambiguity

### Symptom
Harness referred to skills living elsewhere without one machine-readable canonical resolver.

### Root problem
Names were treated as enough identity.

### Consequences
Different agents could use different copies/versions.

### Prevention already added
- canonical `skill_registry.json`;
- resolver;
- explicit executable/procedural/mapped classification;
- pinned source authority.

General lesson:
Every named mechanism needs an address, version/ref, capability level, and authority class.

---

## 5.16 Candidate/active confusion

### Symptom
Open PRs, later branch heads, test-passing candidates, experiments, and shelved systems were repeatedly spoken about near active architecture.

### Root problem
Existence, evidence, and activation were not always separated in language.

### Consequences
- Friday/Jarvis candidates resurfaced;
- coding-engine candidates sounded merged;
- observed Workshop advancement risked becoming authority merely because it was newer.

### Prevention
Every component/ref must be one of:

- observed
- candidate
- approved
- active
- shelved
- retired
- rejected

“Newer” is not a promotion rule.

---

## 5.17 Documentation multiplying faster than closure

### Symptom
Many handoffs, maps, audits, prompts, state documents, recovery reports, and project descriptions accumulated.

### Root problem
Documentation was repeatedly used to compensate for missing executable continuity.

### Consequences
- more things to reconcile;
- uncertainty about which file to read;
- apparent progress without reducing owner burden.

### Prevention
Documentation has only four legitimate roles:

1. canonical machine-readable authority;
2. generated human view of that authority;
3. durable postmortem/origin context;
4. archived historical evidence.

Anything else should justify why it exists or be retired.

---

## 5.18 New-chat amnesia

### Symptom
A new AI session did not know what the machine was, what had passed, or what to do next.

### Root problem
Continuity depended on chat history instead of recoverable project state.

### Consequences
This recreated the original problem the project was invented to solve.

### Prevention
A new competent agent should be able to recover the current work by reading only:

1. `state/START_HERE_FOR_CODE.md`
2. `state/CURRENT_PROJECT.json`
3. `state/ACTIVE_WORK_ORDER.md`
4. `OPERATING_CONTRACT.md`
5. `ROUTING.md`

and then verifying live repo/device state where required.

If a new session still needs a 100-message explanation, continuity is not fixed.

---

# 6. Murphy's Law risk register — what can and will go wrong if unguarded

This section assumes that every dependency eventually fails, every network eventually retries, every token eventually expires, every branch eventually drifts, and every human eventually returns after forgetting the implementation details.

## Critical risks

### R1 — Duplicate dispatch
Cause: double tap, network retry, refresh, client timeout.
Impact: duplicate work or conflicting receipts.
Guard: idempotency key + immutable attempts + concurrency control.

### R2 — Proof belongs to wrong request
Cause: transport IDs mixed with semantic IDs.
Impact: false certification.
Guard: receipt/proof structurally binds canonical `job_id`, source SHA, fixture/job class, and attempt.

### R3 — GitHub artifact expires
Cause: retention and workflow cleanup.
Impact: historical receipt/proof link becomes dead.
Guard: persist the durable receipt/proof summary somewhere governed before artifact expiration; treat artifact URLs as evidence transport, not permanent memory.

### R4 — Branch moves after approval
Cause: normal development.
Impact: deployed/executed code differs from approved code.
Guard: dispatch exact approved SHA; observe branch separately.

### R5 — Token expires/revokes/loses scope
Cause: security rotation, account change.
Impact: phone dispatch or result retrieval breaks.
Guard: explicit BLOCKED credential state, health check, minimum-scoped service credential, no silent fallback to weaker security.

### R6 — Cloudflare route/deploy changes
Cause: Pages/Functions config drift.
Impact: UI loads while API route fails, or preview works but production fails.
Guard: deployment receipt + route smoke test + authenticated target-device proof.

### R7 — Access/authentication passes browser but fails API
Cause: headers/session assumptions.
Impact: owner sees login but dispatch cannot authenticate correctly.
Guard: test the actual authenticated POST/GET owner path, not only 302/login page behavior.

### R8 — Executor passes its own test but independent proof fails
Cause: narrow Builder tests.
Impact: misleading success state.
Guard: UI cannot show PASSED until independent proof result binds to job.

### R9 — Independent proof unavailable
Cause: workflow failure, dependency outage.
Impact: work exists but cannot be certified.
Guard: terminal state `PROOF_PENDING`/`BLOCKED`, never implicit success.

### R10 — UI cache/service worker serves old code
Cause: browser cache/PWA behavior.
Impact: owner interacts with stale frontend against newer backend.
Guard: version display, cache-busting/reload strategy, deployed SHA visible in operator view.

### R11 — Local source newer than GitHub
Cause: unsynced Windows work.
Impact: remote agent modifies obsolete assumptions.
Guard: local-vs-GitHub reconciliation before source-authoritative Workshop changes.

### R12 — Local repository identity wrong
Cause: nested repo/parent root/path confusion.
Impact: accidental unrelated commits/deletes.
Guard: workspace identity fail-closed checks before mutation.

### R13 — Workflow concurrency creates race
Cause: two runs same job/ref.
Impact: contradictory states.
Guard: concurrency group based on canonical job/attempt policy; never cancel a run if cancellation would erase required history without recording it.

### R14 — Receipt schema changes
Cause: later upgrade.
Impact: old UI cannot read new receipt or old receipts become unreadable.
Guard: schema versioning + backwards-compatible reader or explicit migration.

### R15 — New model invents architecture
Cause: model sees incomplete context and optimizes locally.
Impact: another Worker, repo, agent framework, memory layer, or database.
Guard: Rabbit-Hole Governor + one active gate + architecture-change burden of proof.

### R16 — “Helpful” cleanup deletes historical evidence
Cause: repo tidy-up.
Impact: provenance loss.
Guard: retirement/archive, not unexplained deletion; provenance-preserving cleanup.

### R17 — Private data enters public repo
Cause: local source-yard/recovery automation.
Impact: irreversible privacy/security incident.
Guard: public Harness contains pointers/state only; secret/private source paths excluded; no raw local archives/transcripts/databases.

### R18 — Salvage candidate becomes active without rights/proof
Cause: useful artifact found in old/public source.
Impact: legal/security/quality contamination.
Guard: Rights Gate -> security/dependency/cost -> bounded test -> independent proof -> explicit promotion.

### R19 — Model cost spirals
Cause: agent swarms/retries/large models.
Impact: wasted money/time.
Guard: deterministic-first, explicit model budgets, escalation rules, hard stop after repeated identical failure.

### R20 — Repeated failure becomes repeated prompting instead of a regression
Cause: closeout skipped.
Impact: same pain returns.
Guard: material incident cannot close until it leaves a durable rule/test/validator/proof gate/routing fix.

---

# 7. External engineering checks that reinforce the current design

The project-specific lessons align with ordinary distributed/software reliability principles:

- GitHub Actions workflows can run concurrently by default; explicit concurrency/idempotency policy is required where duplicate work can conflict.
- GitHub workflow artifacts are useful for transporting proof but are retention-bound and should not be treated as permanent historical authority.
- Cloudflare Pages Functions are a legitimate thin authenticated server-side boundary without requiring a dedicated always-on server, which supports the current “doorway, not authority” design.
- deployment success is not the same as target-device/route success; the real authenticated owner path still requires proof.

These are not reasons to add more infrastructure. They are reasons to harden the narrow path already selected.

---

# 8. The anti-repeat contract

The following rules should be treated as hard operational law for Foundation V0.

## Rule 1 — One active gate
Only one Foundation stop condition is active at a time.

New research, models, salvaged mechanisms, UI ideas, infrastructure, or side products go to PARKED/CANDIDATE unless they directly unblock the active gate.

## Rule 2 — One canonical current-state source
`state/CURRENT_PROJECT.json` owns current project state.

Human-readable work orders are projections, not competing authority.

## Rule 3 — Live truth beats memory
If repo/device/deploy state can be inspected, inspect it.

Historical conversation memory is context, never stronger than verified current truth.

## Rule 4 — Exact evidence scope
Every proof statement names:

- job class;
- environment;
- source SHA;
- test/live level;
- what was NOT proven.

## Rule 5 — No architecture changes during closure
A missing route does not authorize a new platform.

Architecture changes require evidence that the current contract cannot satisfy the locked outcome.

## Rule 6 — Salvage before rebuild
Before inventing a new subsystem, search current repos/history/candidates for an existing mechanism.

## Rule 7 — Candidates do not become authority automatically
Branch movement, newer code, a passing PR, a discovered artifact, or a clever model output is not promotion.

## Rule 8 — One canonical job identity
One owner-visible `job_id` survives arrival, execution, proof, receipt, display, retry history, and learning.

## Rule 9 — Proof is independent
The executor cannot be the final certifier.

## Rule 10 — Human authority remains above activation
Certified means ready for owner review unless a later explicitly approved job class permits a narrower automatic action.

## Rule 11 — Every material failure pays rent
If a failure costs meaningful owner time, it must produce durable prevention.

## Rule 12 — Closure before upgrade
The first bounded phone round trip must be PROVEN_LIVE before model routing, broad natural-language coding, new compute brokers, or broader self-improvement becomes active work.

---

# 9. Definition of DONE for the current gate

`PAGES_BOUNDED_JOB_ROUND_TRIP` is DONE only when all of the following are true in the real owner path:

1. Owner opens existing Workshop on Android.
2. Owner authenticates through the existing boundary.
3. Owner starts the approved bounded `aios-path-containment` job from Workshop.
4. Workshop assigns/preserves one canonical `job_id` according to the approved contract.
5. Existing dispatcher invokes the pinned Foundry implementation.
6. Foundry/AIOS/Builder perform the real bounded execution.
7. Independent Proof returns its verdict.
8. The exact correlated receipt returns to Workshop.
9. Phone UI shows state and proof clearly.
10. Refresh/reload can recover state.
11. Unknown/forbidden job is rejected before execution.
12. Controlled failure does not appear as success.
13. Duplicate/retry behavior is deterministic and auditable.
14. Deployed source SHA, workflow run ID, job ID, proof verdict, and human-review state are recorded.
15. Harness updates only after proof, without silently advancing unrelated authority.

Nothing short of that is completion of the current gate.

---

# 10. What happens after the current gate is proven

The next work must be incremental, not another redesign.

## Mandatory after-proof hardening

- durable receipt retention independent of expiring transient artifact URLs;
- job/attempt idempotency/concurrency policy;
- clear operator recovery after timeout/reload;
- health/status visibility for auth, dispatch, workflow, proof, and result retrieval;
- target-device cache/version visibility;
- documented credential/permission failure state;
- regression covering the real bounded round trip where practical.

## Then, and only then, capability expansion

Candidate sequence:

1. review existing natural-language coding candidate rather than reinventing it;
2. add model routing inside bounded jobs using cost/complexity rules;
3. expand Artifact Compass/Salvage candidate discovery;
4. promote new job classes one by one with exact evidence;
5. downshift repeated proven reasoning into deterministic routines;
6. keep Windows/private source access optional and bounded rather than an always-on dependency.

---

# 11. What Foundation V0 must never become

Do not let the project drift into:

- an omniscient memory diary;
- a surveillance archive;
- an autonomous owner replacement;
- a giant monorepo because multiple repos feel inconvenient;
- a permanent agent swarm;
- a model-specific architecture;
- a Cloudflare-specific architecture;
- a GitHub-Actions-specific architecture;
- a Windows-always-on architecture;
- a museum that preserves every failed experiment forever;
- an endless research project with no owner-visible product path;
- a system where documentation is mistaken for execution;
- a system where tests are mistaken for owner experience;
- a system where “newer” is mistaken for “approved.”

The contracts should remain portable enough that model, provider, host, and UI can change without forcing the human to reconstruct the working relationship.

---

# 12. The simplest possible description for future agents

If a future model has only one minute to understand Foundation V0, tell it this:

> Randy should be able to tell one simple phone-facing Workshop what he wants. Harness recovers current truth and rules. Foundry turns the request into one bounded job. AIOS correlates the execution. Builder/tools do the work. Independent Proof verifies it. One receipt comes back under one job ID. Randy decides anything irreversible. Proven failures become permanent prevention. Models, hosts, skills, and providers are replaceable implementation details.

If the proposed work does not move that loop forward or strengthen its reliability, it is probably not the active Foundation job.

---

# 13. Why this project felt endless

The owner has repeatedly experienced a contradiction:

- a lot of real work exists;
- many individual mechanisms are genuinely proven;
- every new audit finds more evidence;
- yet the simple thing the owner expects to do is still not available end to end.

That creates the feeling that the project is constantly “90% done” while never becoming usable.

The technical explanation is that progress accumulated **horizontally across components** while completion requires **vertical proof through the owner path**.

A hundred more component improvements will not substitute for one proven vertical slice.

The project stops feeling endless when the development unit changes from:

> improve a component

into:

> close one owner-visible job class end to end, freeze its contract, then move to the next.

---

# 14. Final diagnosis

Foundation V0 did not fail because the idea was incoherent.

The core idea has actually become clearer over time:

- preserve useful continuity;
- recover current truth;
- salvage before rebuilding;
- bound execution;
- separate execution from proof;
- keep irreversible authority human;
- make complexity disappear behind a simple owner interface;
- turn expensive repeated lessons into durable cheaper machinery.

The project failed repeatedly at **finishing discipline**:

- too many authority surfaces;
- too many stale handoffs;
- too many candidate ideas near active scope;
- too much subsystem proof described near system proof;
- too much architecture exploration before closure;
- insufficiently enforced end-to-end owner-path testing;
- insufficient durable state recovery between sessions.

Those are fixable.

The correct response is not another architecture.

It is to enforce the continuity rules already earned, close the current phone round trip, and make every future expansion prove itself through the same vertical discipline.

---

# 15. Durable source index for this postmortem

Primary live sources used for reconstruction:

- `docs/ORIGIN_STORY.md`
- `OPERATING_CONTRACT.md`
- `ROUTING.md`
- `state/CURRENT_PROJECT.json`
- `state/ACTIVE_WORK_ORDER.md`
- `docs/MACHINE_REPAIR_AUDIT_2026-09-24.md`
- `docs/FOUNDATION_COHESION_REPAIR_2026-09-27.md`
- `docs/SYSTEM_BOUNDARY_MAP_V1.md`
- current repo/branch observations recorded in Harness state
- historical project handoffs and prior Foundation reconstruction work

When any historical statement conflicts with live verified repo/device/deploy state, live verified state wins.

---

# Final rule

> Do not make Randy pay the same integration tax twice.

A failure is not fully closed until the system can explain:

- what broke;
- why it broke;
- which layer owned the break;
- which false leads consumed time;
- what smallest fix closed it;
- how the real owner path proved the fix;
- what durable guard prevents the same class of failure from returning.

That is the standard Foundation V0 was built to enforce on itself.
