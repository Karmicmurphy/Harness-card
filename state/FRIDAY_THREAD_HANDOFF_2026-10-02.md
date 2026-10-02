# FOUNDATION V0 — FRIDAY Thread Handoff

Date: 2026-10-02
Local time: approximately 00:12 America/Chicago
Purpose: clean thread/window handoff so the owner does not have to reconstruct current state.

## Governing authority

- Repo: `Karmicmurphy/Harness-card`
- Branch: `main`
- Authority model: `RANDY_AND_HARNESS`
- Verified continuation capsule: `vcc:3983583104e956414ddc19093e149213`
- Recovered authority revision used by the current durable READ fixture: `732378db1eb5a35558627695e1436c3760e7a4ab`
- Current FRIDAY status: `READY`
- Recovery: `RECOVERED`, trusted

Do not silently replace governing Harness authority with dirty/local candidate state. Branch advancement is observation, not promotion.

## What is now proven

### 1. Phone -> Codex Remote -> FRIDAY MCP

Android phone can reach the registered `friday-owner-node` MCP through Codex Remote.

Observed repeatedly:

- FRIDAY MCP connected
- `status: READY`
- `authority: RANDY_AND_HARNESS`
- recovery trusted
- no pending approvals

### 2. FRIDAY recovery survives client restart/reconnect

A stale MCP transport previously returned `Transport closed`. Full Codex Quit/Exit + reopen restored the transport without changing FRIDAY recovery state or capsule.

Lesson: transport failure is not state failure.

### 3. Read-only estate salvage works remotely

`friday_salvage` succeeded against real GitHub + local source yards.

Receipt:

`librarian:821f97b0e7688467a4ddf964`

Result was `READY`, targeted, no execution, no authority change, no automatic promotion.

### 4. FRIDAY can accept a bounded READ work order

Work order:

`friday-work:7fcc12e4d9057ab09819ff2a`

Initial status was `QUEUED_FOR_FOUNDATION`.

This exposed the missing queue-to-execution bridge; acceptance alone was not treated as execution.

### 5. Local certified READ round trip works through the real execution spine

A manually invoked candidate bridge reused existing Foundation components:

- grounded intent validation
- Foundry job compilation
- deny-by-default execution
- AIOS adapter
- Independent Proof

Correlated identifiers:

- FRIDAY work order: `friday-work:7fcc12e4d9057ab09819ff2a`
- Foundry job: `job:4ea425916cc72eab71f134af`
- AIOS state: `DONE`
- Independent Proof verdict: `CERTIFIED`
- certificate: `cert:4b8681457665e0e0678d028e97eb2217`

The immutable result identified:

`PAGES_BOUNDED_JOB_ROUND_TRIP`

as the next unproven gate in the recovered snapshot at `732378db1eb5a35558627695e1436c3760e7a4ab`.

### 6. Durable READ lifecycle was implemented locally

The exact READ fixture was turned into a small manual durable READ operator inside the existing FRIDAY MCP candidate.

Behavior now proven locally:

- original request preserved
- request hash preserved
- work-order bytes preserved
- recovery capsule preserved
- lifecycle events/results stored separately
- lifecycle supports `ACCEPTED`, `RUNNING`, `BLOCKED`, `FAILED`, `CERTIFIED`
- duplicate submission returns the preserved certified result without rerunning
- fresh server process recovers the result without rerunning
- unsupported/altered requests fail closed
- conflicting authority blocks without execution
- interrupted/tampered attempts fail closed

Focused validation reported 36 passing tests. One unrelated historical execution test hit Windows SQLite temporary-file cleanup `WinError 32`; that code was not changed.

No background worker, database, new framework, merge, deployment, promotion, authority change, or Cloudflare change was introduced.

### 7. Durable READ operator is proven from the phone

After refreshing the Codex/FRIDAY MCP connection, the phone-visible tool set included the new durable READ lifecycle.

From Android through Codex Remote, `friday_run_read` was invoked for the existing immutable READ request and returned the preserved certified result:

- status: `CERTIFIED`
- cached: `true`
- execution performed this call: `false`
- authority changed: `false`
- activation performed: `false`
- work order: `friday-work:7fcc12e4d9057ab09819ff2a`
- job: `job:4ea425916cc72eab71f134af`
- certificate: `cert:4b8681457665e0e0678d028e97eb2217`
- result: `PAGES_BOUNDED_JOB_ROUND_TRIP`
- scope: `IMMUTABLE_READ_FIXTURE_ONLY`
- source revision: `732378db1eb5a35558627695e1436c3760e7a4ab`

The existing receipt was recovered without rerunning the worker.

Evidence state: `PROVEN_REMOTE_PHONE_DURABLE_READ_RECOVERY`

## Important proof boundary

The current certificate is limited to one immutable READ fixture captured from the recovered Harness snapshot.

It does **not** prove:

- arbitrary natural-language -> certified result
- fresh/current authority READs
- unattended/background execution
- a general FRIDAY queue consumer
- live Workshop/Cloudflare execution
- `PAGES_BOUNDED_JOB_ROUND_TRIP`
- production deployment
- cloud execution as FRIDAY's default worker

Do not broaden the claim.

## Local FRIDAY candidate state

Current work was performed in the local FRIDAY owner-node candidate, not by promoting old historical PRs.

Relevant current local candidate additions include the durable READ bridge/lifecycle implementation and focused tests. Earlier isolated bridge candidate files included:

- `bridge.py`
- `verify_result.py`
- `test_bridge.py`

The live registered MCP now exposes/returns the durable READ lifecycle, including `friday_run_read`.

Do not assume GitHub contains every current local FRIDAY candidate file. Inspect the live local candidate before modifying or rebuilding it.

## Existing historical/candidate material to preserve

- Foundry PR #24–#28: arrival validation, job compilation, execution/proof lineage
- Foundry PR #31: trusted coding-engine candidate; later work, not a READ prerequisite
- Foundry PR #32/#33: cloud dispatch/correlation candidates; open/unmerged
- Harness PR #15: `candidate/friday-host-recovery-v0`, draft fail-closed host recovery kit; not host-proven
- Estate Librarian / PR #23 material: deterministic source-yard/authority composition candidate
- PersonalJarvis warehouse: salvage patterns only, not architecture authority

Do not merge/promote any of these merely to make a demo pass.

## Known incidents / learned rules from this run

1. `Transport closed` was a Codex/MCP lifecycle problem, not FRIDAY state corruption.
2. Dirty local authority-like edits are candidate evidence, not governing authority.
3. Work-order acceptance is not execution.
4. Queue persistence is not proof; completion requires correlated execution + Independent Proof.
5. Reuse the existing Foundation execution spine before creating new orchestration infrastructure.
6. Prompt burden belongs in Harness/FRIDAY, not the owner.
7. Management-plane recovery must not depend solely on the work-plane process.
8. Fixture proof remains fixture-bounded.
9. Duplicate READ requests must recover preserved certified evidence instead of silently rerunning or overwriting it.

## Current official Harness work order

`state/ACTIVE_WORK_ORDER.md` remains the canonical generated work order and currently names:

`PAGES_BOUNDED_JOB_ROUND_TRIP`

as the one next gate.

Do not hand-edit generated `ACTIVE_WORK_ORDER.md`; its source is `state/CURRENT_PROJECT.json`.

## Best resume move in a new thread

Before changing code, recover current truth and avoid relying only on the frozen fixture result.

Recommended first action:

1. Call `friday_status` to confirm FRIDAY is still `READY` and recovery is trusted.
2. Inspect whether the current durable READ operator can safely support a **fresh bounded authority read** without weakening the immutable fixture guarantees.
3. If fresh authority READ is not yet supported, make that the smallest next candidate capability.
4. Use the fresh bounded read to verify whether `PAGES_BOUNDED_JOB_ROUND_TRIP` is still the true current blocker.
5. Only then continue the Pages/Workshop round-trip work if current authority still says it is next.

Do not restart architecture discussion unless the current code proves a structural blocker.

## Owner interaction rule

WTF SIMPLE.

The owner should be able to give short natural-language intent. Recover authority, choose the necessary skills/tools, inspect/salvage first, do the bounded work, prove it, record the lesson, and stop.

Do not make the owner re-explain repos, SHAs, proof plumbing, prior incidents, or architecture unless a real unresolved authority/approval boundary requires it.

## Stop / safety boundaries

Without explicit owner approval, do not:

- merge
- deploy
- publish
- activate
- spend
- change permissions/security
- delete
- reset dirty local work
- promote candidates to authority
- broaden execution capability

Models may propose. Deterministic machinery validates/routes/executes within bounded capability. Independent Proof verifies. Randy retains consequential approval.

## Related durable records

- `state/FOUNDATION_FRIDAY_OPERATOR_FIELD_TRIAL_2026-10-01.md`
- `state/FRIDAY_REMOTE_DURABLE_READ_PROOF_2026-10-01.md`
- `state/ACTIVE_WORK_ORDER.md`
- `state/CURRENT_PROJECT.json`
- `state/AUTOGENERATED_RULES.md`

## Resume sentence

If a new thread needs one instruction, use:

> Recover current Foundation/FRIDAY state from Harness main and continue from `state/FRIDAY_THREAD_HANDOFF_2026-10-02.md`. Follow Harness. Do not redesign. Verify the current next gate before changing anything.
