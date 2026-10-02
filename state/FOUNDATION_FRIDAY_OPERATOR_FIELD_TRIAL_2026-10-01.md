# FOUNDATION V0 — FRIDAY Operator Field Trial / Incident Closeout

Date: 2026-10-01
Local closeout time: approximately 18:25 America/Chicago
Authority repo: `Karmicmurphy/Harness-card`
Authority branch: `main`
Governing authority revision used by verified continuation capsule: `732378db1eb5a35558627695e1436c3760e7a4ab`

## Outcome

This field trial moved FRIDAY from a local candidate into a remotely exercised operator surface with verified current-state recovery and read-only estate salvage from an Android phone through Codex Remote.

Evidence must remain bounded. This does **not** prove the full phone -> Foundation execution -> Independent Proof -> result-return path.

## Proven wins

### 1. Phone -> Codex Remote -> FRIDAY MCP

The owner successfully reached the registered `friday-owner-node` MCP from Android through Codex Remote.

Observed tool result before recovery:

- server: `friday-foundry-gateway/v0`
- status: `NEEDS_VERIFIED_CAPSULE`
- authority: `RANDY_AND_HARNESS`
- execution_performed: `false`

Evidence state: `PROVEN_REMOTE_PHONE`

### 2. Verified continuation recovery

A real authority conflict was detected between a dirty local reconciliation branch and Harness GitHub `main`.

The system failed closed rather than silently choosing an authority source.

Owner decision: Harness GitHub `main` governs this recovery; the dirty local reconciliation state remains preserved candidate/historical material and was not reset, discarded, merged, or promoted.

The existing continuation-capsule implementation assembled and verified:

- capsule: `vcc:3983583104e956414ddc19093e149213`
- governing Harness revision: `732378db1eb5a35558627695e1436c3760e7a4ab`
- FRIDAY recovery: `RECOVERED`
- trusted: true
- resulting FRIDAY status: `READY`
- authority: `RANDY_AND_HARNESS`
- execution_performed: false

### 3. Read-only estate salvage from the phone

`friday_salvage` succeeded through the registered MCP against real authority and local component fingerprints.

Receipt:

`librarian:821f97b0e7688467a4ddf964`

Observed result:

- verdict: `READY`
- selection_mode: `TARGETED`
- selected_source_yards:
  - `github-karmicmurphy`
  - `local-windows`
- missing_adapter_receipts: []
- executes_work: false
- changes_authority: false
- automatic_promotion: false

Inputs included four Harness files at the recovered authority revision plus fingerprinted local components:

- FRIDAY Gateway
- Estate Librarian
- Continuation Capsule
- Independent Proof

This proves the read-only salvage preflight works with real artifact inputs. It does not prove Foundation execution.

### 4. Certified local FRIDAY -> Foundation -> AIOS -> Independent Proof -> FRIDAY result return

A manually invoked, allowlisted READ fixture completed through the actual local Foundation path and returned a correlated certified result through the registered FRIDAY MCP.

Observed identifiers:

- FRIDAY work order: `friday-work:7fcc12e4d9057ab09819ff2a`
- canonical Foundry job: `job:4ea425916cc72eab71f134af`
- AIOS state: `DONE`
- Independent Proof verdict: `CERTIFIED`
- certificate: `cert:4b8681457665e0e0678d028e97eb2217`

The manually invoked bridge reused the existing grounded intent validator, job compiler, deny-by-default executor, AIOS adapter, and Independent Proof verifier. It accepted only the exact allowlisted READ request and rejected altered or unsupported requests.

Three isolated local candidate files were created:

- `bridge.py`
- `verify_result.py`
- `test_bridge.py`

Validation:

- 17 focused tests passed
  - 7 bridge tests
  - 7 FRIDAY gateway regressions
  - 3 AIOS adapter regressions
- the independent checker ran in an isolated workspace and reported no candidate mutation
- the recovery capsule SHA256 remained unchanged
- existing dirty Foundry files were not edited
- no merge, deployment, promotion, authority change, Cloudflare mutation, or background worker occurred

FRIDAY result return was confirmed by `friday_status`, which remained `READY`, preserved `RANDY_AND_HARNESS`, and exposed the correlated certified result under `read_fixture_result`.

Important boundary: the work order itself remains `QUEUED_FOR_FOUNDATION`. The manually invoked immutable READ fixture executed, but this does **not** establish a live queue consumer or live-job completion semantics. FRIDAY's top-level `execution_performed: false` still describes the gateway layer, not the manually invoked fixture execution.

The immutable result identified `PAGES_BOUNDED_JOB_ROUND_TRIP` as the next unproven gate in the recovered Harness snapshot at `732378db1eb5a35558627695e1436c3760e7a4ab`. This inspection does not prove that gate has passed.

Evidence state: `PROVEN_LOCAL_CERTIFIED_READ_ROUND_TRIP`

## Incidents / losses / friction

### Incident A — Local command helper setup-refresh failure

**SYMPTOM:** Codex default sandbox execution failed with `helper_unknown_error: setup refresh had errors` while FRIDAY MCP remained callable.

**EXPECTED:** Codex should be able to inspect authoritative local files without blocking continuation recovery.

**LAYER:** LOCAL / TOOLING

**ROOT CAUSE:** Unproven. Codex/sandbox-service processes responded, but the setup-refresh failure remained unresolved.

**FIX / WORKAROUND:** Use the explicitly approved execution path outside the sandbox for read-only commands and file inspection.

**PROOF:** `cd` succeeded and `AGENTS.md` was read from the FRIDAY Owner Node repository. FRIDAY MCP status continued to work.

**VERDICT:** BLOCKED root cause / WORKAROUND PROVEN

**LEARNING:** A broken default sandbox is not evidence that FRIDAY or the host is unavailable. Classify the failing layer before redesigning or rebuilding.

### Incident B — Authority conflict stopped capsule recovery

**SYMPTOM:** Dirty local `CURRENT_PROJECT.json` on `codex/foundation-state-reconciliation-v0` disagreed with Harness GitHub `main` about approved Foundry SHA, Workshop SHA, and active path.

**EXPECTED:** Recovery must identify one governing authority without silently discarding material local edits.

**LAYER:** AUTHORITY / CONTRACT

**ROOT CAUSE:** A preserved dirty local reconciliation candidate contained uncommitted authority edits that had not been promoted to governing Harness authority.

**FIX:** Apply Harness bleed-control rule: GitHub `main` remains governing authority; local branch remains candidate/historical material until explicitly reconciled and promoted.

**PROOF:** Capsule verified and FRIDAY reached `READY` while dirty local reconciliation state remained untouched.

**VERDICT:** DONE

**LEARNING:** Current governing authority must be explicit. Dirty local authority-like edits are evidence, not authority, unless promoted.

### Incident C — Codex/FRIDAY MCP transport closed after restart attempt

**SYMPTOM:** MCP discovery still succeeded, but fresh `friday_status` calls returned `Transport closed`.

**EXPECTED:** FRIDAY should remain reachable after a Codex restart/reconnect cycle.

**LAYER:** LOCAL / TRANSPORT / OPERATOR

**FALSE LEAD:** FRIDAY state corruption.

**ROOT CAUSE:** The active Codex/MCP transport was stale/closed. FRIDAY's verified capsule and recovered state remained intact.

**FIRST REPAIR ATTEMPT:** A graceful restart was requested, but Codex did not fully quit and remained running. The transport did not recover.

**WORKING REPAIR:** Use Codex's actual Quit/Exit action so the application/session fully terminates, reopen Codex, then call `friday_status`.

**REAL-WORLD PROOF:** After full Quit/Exit and reopen, `friday_status` succeeded and returned:

- status: `READY`
- authority: `RANDY_AND_HARNESS`
- execution_performed: false
- work_orders: []
- approval_requests: []
- recovery state: recovered/trusted
- capsule unchanged: `vcc:3983583104e956414ddc19093e149213`

**VERDICT:** DONE

**LEARNING:** `Transport closed` must be diagnosed as a transport/process lifecycle problem before touching FRIDAY state. Preserve recovery state; do not rebuild the gateway or capsule. A window-close is not equivalent to a verified process exit.

### Incident D — Single remote doorway exposed owner-stranding risk

**SYMPTOM:** Restarting Codex while the owner was away from the laptop risked losing the only proven remote operator channel.

**EXPECTED:** Recovery of the operator surface should not require the owner to be physically present at the host.

**LAYER:** ARCHITECTURE / OPERATIONS

**ROOT CAUSE:** Management-plane access depended too heavily on the same Codex process/session used as the work-plane operator.

**FIX STATUS:** Candidate only. Created `candidate/friday-host-recovery-v0` and draft Harness PR #15 with a fail-closed Windows host-recovery kit.

Candidate functions:

- `preflight`
- `status`
- `recover-codex`
- `recover-remote`

Candidate detects:

- Windows OpenSSH / `sshd`
- Tailscale
- `cloudflared`
- Codex CLI
- Codex process state
- Codex remote-control capability

Candidate explicitly avoids public-port changes, force-kill, Foundation execution, and authority mutation.

**REAL-WORLD PROOF:** NOT RUN on host.

**VERDICT:** BLOCKED pending host proof

**LEARNING:** Separate management plane from work plane. Codex/FRIDAY/Foundation work must not own the only channel capable of restoring Codex/FRIDAY/Foundation access.

### Incident E — FRIDAY accepted work but had no live queue consumer

**SYMPTOM:** `friday_submit_work_order` accepted and persisted the READ request as `QUEUED_FOR_FOUNDATION`, but inspection found no live queue consumer or completed-result retrieval path in the registered gateway.

**EXPECTED:** A bounded accepted work order should correlate to a canonical Foundry job, execute through the compatible bounded path, receive Independent Proof, and return the result to FRIDAY.

**LAYER:** ARCHITECTURE / EXECUTION / CONTRACT

**ROOT CAUSE:** The FRIDAY gateway intentionally persisted work orders but had no capability-checked bridge from FRIDAY work-order IDs into the existing Foundry/AIOS/proof machinery.

**FIX STATUS:** Candidate proof implemented locally as an isolated manually invoked READ bridge. The bridge reuses existing Foundation components rather than adding a new queue framework, worker service, database, or background daemon.

**REAL-WORLD PROOF:** `PROVEN_LOCAL_CERTIFIED_READ_ROUND_TRIP` for the exact immutable allowlisted READ fixture; see Proven Win 4.

**VERDICT:** PARTIALLY DONE — candidate bridge proof complete; live queue consumer / production handoff remains unproven.

**LEARNING:** Work-order acceptance is not execution. Persisted queue state must never be promoted to job completion without correlated execution and Independent Proof. Reuse the existing execution spine before creating new orchestration infrastructure.

## Current proven FRIDAY boundary

Proven:

1. Android phone -> Codex Remote -> registered FRIDAY MCP.
2. FRIDAY can report its state remotely.
3. Verified continuation capsule can reconcile current governing authority and recover FRIDAY to `READY`.
4. Authority conflict fails closed.
5. `friday_salvage` can run targeted, read-only estate preflight against real GitHub + local artifact inputs.
6. A stale/closed Codex MCP transport can be recovered by full Quit/Exit + reopen without changing FRIDAY recovery state.
7. `friday_submit_work_order` can accept and persist a bounded READ work order through the remote operator path.
8. An isolated, manually invoked, exact-allowlist READ bridge can correlate FRIDAY work order -> Foundry job -> real AIOS execution -> Independent Proof -> FRIDAY result return.
9. The focused certified round trip preserved the recovery capsule and governing authority and failed closed on altered/unsupported requests.

Not yet proven:

1. A live FRIDAY queue consumer automatically handing accepted work into Foundry/AIOS.
2. A live/non-fixture arbitrary natural-language -> certified result path.
3. `PAGES_BOUNDED_JOB_ROUND_TRIP`: authenticated phone dispatch of the approved bounded fixture followed by the exact correlated Independent Proof receipt returning to the phone.
4. Host recovery candidate on the actual Windows machine.
5. Independent out-of-band management path.
6. Cloud execution as FRIDAY's default worker.
7. Full Workshop phone dispatch path; historical Cloudflare lane remains separately bounded and must not be inferred from the local certified FRIDAY fixture.

## Durable operating rules extracted

1. **Transport is not state.** `Transport closed` does not invalidate a verified FRIDAY capsule or authority state.
2. **Classify before repair.** Distinguish Codex transport, FRIDAY process, sandbox/helper, authority, and Foundation execution layers before modifying anything.
3. **Preserve verified state through operator restart.** Do not rebuild FRIDAY merely because the Codex client/session restarted.
4. **Authority outranks local candidate edits.** Dirty or local authority-like artifacts remain candidate evidence until explicitly promoted.
5. **Management plane must be independent.** The work-plane operator must not be the only means to restore the operator.
6. **Owner interruption is a defect signal.** Prefer self-recovery, read-only inspection, and deterministic proof before asking the owner for manual diagnostics.
7. **Prompt burden belongs in the harness.** Once authority, operating rules, and tool contracts are durable, the owner's normal request should be short natural-language intent; FRIDAY/Harness must recover context and choose the bounded next move.
8. **Queue acceptance is not execution.** `QUEUED_FOR_FOUNDATION` proves persistence only; completion requires a correlated canonical job, execution result, and Independent Proof.
9. **Reuse the execution spine.** Before creating orchestration infrastructure, combine the existing intent validator, compiler, AIOS adapter, and proof machinery through the smallest capability-checked bridge.
10. **Fixture proof stays fixture-bounded.** A certified immutable local READ fixture does not prove arbitrary natural language, automatic queue consumption, cloud dispatch, or the live Pages path.

## Next safe proof

The next governing unproven gate identified by the certified immutable READ fixture is `PAGES_BOUNDED_JOB_ROUND_TRIP`.

Treat that gate separately from the local FRIDAY bridge proof. Do not infer that local certified execution resolves Cloudflare/Workshop blockers. The required live proof remains authenticated phone dispatch of the approved bounded Foundation fixture followed by return of the exact correlated Independent Proof receipt.

Stop before mutation, promotion, merge, deployment, authority change, or security-permission change unless a separately authorized work order explicitly crosses that boundary.
