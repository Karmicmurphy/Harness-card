# Authority Spine Guard V0 — Receipt

Status: **PROVEN_IN_TEST**

Date: 2026-09-22

## Failure class repaired

Harness continuity surfaces had drifted apart:

- `state/CURRENT_PROJECT.json` named **FOUNDATION V0 — HUMAN-OWNED SOFTWARE FACTORY** as active.
- `state/ACTIVE_WORK_ORDER.md` still named the separate TWIS sonic project as active.
- `projects/PROJECT_INDEX.md` did not contain the active Foundation project.
- `state/ECOSYSTEM_AUTHORITY_INDEX.json` carried older Foundation authority pointers.

That contradiction could make a fresh agent resume the wrong job and force Randy to reconstruct context manually.

## Candidate repair

Branch: `authority-spine-guard-v0`

Draft PR: #4

The candidate:

1. aligns the human-readable active work order with `CURRENT_PROJECT.json`;
2. adds a machine-readable `state/ACTIVE_WORK_ORDER.json`;
3. adds the active Foundation project to `projects/PROJECT_INDEX.md`;
4. reconciles active Foundation canonical refs in `ECOSYSTEM_AUTHORITY_INDEX.json`;
5. adds `scripts/check_authority_spine.py`, a standard-library-only fail-closed validator;
6. adds regression tests that intentionally create stale work-order and stale authority-pointer drift;
7. runs the guard in GitHub Actions whenever Harness state or the guard surfaces change.

## Proof

GitHub Actions run: `35696712845`

Commit under proof: `322ba5f6e06a6ba27817d7ec6b33edeab15b9153`

Result: **SUCCESS**

Job: `authority-spine`

Proof checks:
- live candidate continuity surfaces agree;
- deliberate active-work-order drift is detected;
- deliberate Foundation authority SHA drift is detected.

A later documentation-only receipt commit may advance the branch head without invalidating the code/test proof above.

## Boundary

This repair does not:

- merge the PR;
- deploy or activate Foundation;
- publish;
- spend money;
- delete data;
- grant permissions;
- broaden FRIDAY authority;
- claim the owner-device PersonalJarvis -> FRIDAY field trial has passed.

That field trial remains the first real-world unproven gate.

## Outcome

The machine now has a candidate **continuity interlock**: if its main "where am I / what am I doing / what authority is current" surfaces disagree, CI fails instead of silently letting a future worker choose stale context.
