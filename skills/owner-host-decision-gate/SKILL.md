---
name: owner-host-decision-gate
version: 0.1.0
status: candidate
---
# Owner Host Decision Gate

**When to use:** Before a permanent OS-dependent service, disk/storage plan, Windows account/DPAPI/Task Scheduler installation, Linux systemd/UID migration, or whenever the owner says current implementation ignores an earlier platform plan.

## Mechanism
1. Recover actual prior owner choices with **date, target, alternatives, and evidence source**. Distinguish the owner decision from assistant suggestions, experiments and stale handoffs. If competing choices exist, show them; never manufacture one permanent preference.
2. Separate the **currently authorized proof target** from the **eventual operating-system destination**. Compare Windows-resident, Linux external/live, Linux dual boot, WSL and fallback only when relevant and grounded.
3. Verify current source, host, disk and backup state rather than assuming a cloud repository can inspect the private PC. Keep a custody record for each artifact.
4. Build a portability table: host-neutral request/response/receipt, Windows-specific SID/DPAPI/Scheduler/NTFS, Linux-specific user/systemd/permissions/credential storage, path and index migration, test and rollback.
5. Recommend one smallest non-destructive evidence-producing step. Stop for a genuine new owner choice, secret, destructive disk change, or broadened authority. Do not silently change CURRENT_PROJECT, active work order, branch pins, original Workshop or deployment.
6. Report outcome with **IMPLEMENTED / PROVEN_IN_TEST / PROVIDER_VERIFIED / PROVEN_OWNER_LIVE / UNKNOWN**, exact evidence references, and next bounded gate. A generated diagram, percent bar or test count cannot prove a live user path.
7. Treat this skill as a **proposed deterministic checklist**, not self-activated runtime learning. Promotion demands owner review and later correlated evidence that an authorized agent applied it.

## Specific regressions to prevent
- Windows-specific installation selected without asking whether it is a short proof or permanent destination.
- A staged-disabled preflight rejects its own safe state.
- Elevated provisioning attempted with no stage-specific logging and no verified rollback.
- Previous assistant recommendation presented as owner approval.
- A prior local index or CI test presented as authenticated FRIDAY-to-PC proof.
- User made to repeat already recorded approvals or reconstruct source locations.

## Output
A dated host decision record, a scope and permissions matrix, a migration/fallback comparison when needed, and one real current gate. If the owner has not decided, state **DECISION PENDING**.
