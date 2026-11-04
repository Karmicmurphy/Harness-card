# FRIDAY Phase Five — host-OS drift and provisioning incident
Recorded 2026-11-03. **Status: review candidate, not an authority change, not PROVEN LIVE.**

## The product objective
One authenticated FRIDAY/Workshop owner request must retrieve permitted local **read-only inventory** evidence, return a correlated independently verified receipt, reject unauthorized/replayed requests, recover safely, and respect durable owner-disable. Harness main at 6d66dac has active FRIDAY_PERSISTENT_OWNER_INVENTORY_READ and evidence PARTIALLY_PROVEN. No live owner-to-Windows success has been established.

## Evidence ladder / current local gate
| Event | Evidence source | Verdict |
| --- | --- | --- |
| Harness authority | GitHub source read | Active, partial proof |
| Foundry/AIOS bounded job and disposable Task Scheduler | CI and Codex test reports | PROVEN IN TEST only |
| Staged-disabled Python host preflight | Codex report | 17 focused tests passed; untested under permanent identity |
| Per-user DPAPI key initializer | Codex report | Tested with disposable identity only |
| First UAC permanent provisioning attempt | Codex report | Exit 1; rollback reported successful, original failing stage not captured |
| No permanent account, task, credential, listener after failed run | Codex follow-up | Reported; verify ACL and rights restoration independently |
| Cloudflare Pages Access and tunnel | Provider read | Protective front door exists; inventory route unconnected |
| Authenticated FRIDAY-to-real-Windows query and receipt | No final evidence | NOT PROVEN |

The reason for the Windows installer failure is UNKNOWN. Do not assign it to a Windows setting, DPAPI, SID, ACL, Scheduler or execution policy without stage-level evidence. Stage/error-code capture was added **after** the failed run, so cannot explain that run retroactively.

## What we got wrong and the recovery rule
1. **Host destination drift.** A Windows-specific acceptance task was mistaken for a permanent decision to run AIOS on Windows. Owner's earlier plans varied across time: Windows-preserving Mint XFCE dual boot (May–July), external-Linux-first with protected Windows fallback (August), Windows-resident AIOS layout (late August), and phone-first/PC-optional runtime (September). November owner reopened Linux-first. These are historical alternatives, **not** one settled timeless choice. Before costly platform-specific installation, reconcile owner’s intended destination with the immediate active proof task and ask for an explicit choice only when necessary. Do not silently repin or rewrite Harness.
2. **Preflight versus activation.** Staged-disabled readiness had accidentally required enabled state; corrected preflight needs to prove disabled readiness without binding listener or reading inventory. Normal startup must still refuse disabled state. Test these two paths separately.
3. **Installer observability before elevation.** An elevated transactional installer was run before stage/code diagnostics identified the failing operation. Require redacted, stage-stamped diagnostics, idempotence and tested rollback before initiating UAC. Check account, task, credential, ACL and user-right restoration.
4. **Component proof was mistaken for owner success.** Static Pages, successful CI, local index, Access 302 login, and green concept diagrams are not live inventory retrieval. Use SOURCE / TEST / PROVIDER / OWNER-LIVE / UNKNOWN per arrow with cited receipt; remove invented progress percentages.
5. **Indices were conflated.** Workshop SQLite/FTS5 artifact search, separate Windows Universal Inventory, and Artifact Compass discovery skills are different sources. Require an explicit read-only search contract that states which index, freshness, coverage, and live-file-check evidence.
6. **Owner became integration manager.** Repetitive reports, branch/workspace drift, scattered file locations, and regenerated prompts forced owner to rebuild context. Persist exact actor, branch, source SHA, cwd, environment, authority, evidence, next step and stop gate. Continue authorized steps without repeat approval.
7. **AIOS existence was conflated with resident OS.** Untethered-AIOS contains experimental Python runtime and test evidence. No verified installed bootable Linux environment or permanent AIOS host exists in the accessible evidence. Windows SID, DPAPI, NTFS ACL and Scheduler implementation would require a distinct host adapter for Linux; do not promise drop-in migration.
8. **A stored lesson is not a learned behavior.** Documentation/PR does not prove FRIDAY read, used, tested or promoted it. Preserve as REVIEW CANDIDATE until verified runtime consumption and regression evidence.

## Decision still owed
A. Finish bounded Windows inventory proof then migrate if the owner decides; or
B. pause new Windows-only hardening and first create an owner-approved, non-destructive Linux-first migration plan (Mint live/external test, Windows recovery, portability/credential changes).

**No OS decision is made by this document.** No partition edits, image restoration, account installation, credential migration, production ingress, PR merge, canonical source-pins or authority change are permitted by this documentation task.

## Scope and custody
This document is intentionally sanitized for the **public** Harness repository. The detailed owner conversation, diagrams and earlier local incident reports belong in private owner storage, not public main. Windows private checkpoint is unavailable to GitHub connector. Previous Phase Five incident/learning proposals should be read and linked rather than overwritten; avoid duplicate learning-rule IDs.

**Next review action:** compare to existing learning candidates, approve/adjust the documented prevention skill, choose operating-system destination explicitly when appropriate, and keep live proof NOT PROVEN until correlated real owner evidence arrives.
