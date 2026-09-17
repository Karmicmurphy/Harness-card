# Harness Card

Harness Card is the canonical operating harness for how AI systems work with Randy across projects.

It is **not** a project repo and it does not own project code. It owns the rules for understanding intent, recovering current truth, selecting skills, controlling scope, proving work, recording failures, and closing work cleanly.

## Manual trigger

Say: **Use Harness Card.**

Expected behavior:
1. Read `AGENTS.md` and `OPERATING_CONTRACT.md`.
2. Recover the actual job from the full relevant context, not only the latest sentence.
3. Resolve the active project from `projects/PROJECT_INDEX.md` and `state/CURRENT_PROJECT.json`.
4. Verify current authority in the actual project repo/device/deploy before making claims.
5. Load only the skills required for the job.
6. Execute one bounded work order.
7. Prove the result.
8. Record meaningful corrections, incidents, decisions, or closeout evidence.
9. Stop when the defined condition is met.

## Core loop

**INTENT -> CURRENT TRUTH -> PROFESSIONAL FRAME -> SKILL ROUTE -> ONE MOVE -> PROOF -> LEARN -> CLOSE**

## Repository boundaries

Harness Card may store:
- operating rules;
- routing logic;
- project pointers and non-sensitive state;
- work-order templates;
- incident and release templates;
- reusable skills or pointers to canonical skill sources;
- schemas and validation rules.

Harness Card should not become:
- a dump of every chat;
- a copy of every project repo;
- a giant personal-memory file;
- a place for secrets, credentials, API keys, private health/legal/financial details, or other sensitive material;
- a roadmap generator that creates work without a proven need.

## Status

Version: **0.1.0**

State: **FOUNDATION / IMPLEMENTED_UNPROVEN**

The harness becomes PROVEN only after it successfully resumes and completes real work across at least two separate projects without requiring Randy to manually restate process rules.