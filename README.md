# Harness Card

Harness Card is the canonical operating harness for how AI systems work with Randy across projects.

It is **not** a project repo and it does not own project code. It owns the rules for understanding intent, recovering current truth, selecting skills, controlling scope, proving work, recording failures, and closing work cleanly.

## Manual trigger

Say: **Use Harness Card.**

For interactive software work, say: **Chat build mode.**

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

`Chat build mode` additionally loads `skills/chat-software-harness/SKILL.md` and keeps ordinary interactive Chat as the software command center when its available tools can perform the work. Code alone is not a reason to route the job into Codex, Work, Astra, or another agent.

## Core loop

**INTENT -> CURRENT TRUTH -> PROFESSIONAL FRAME -> SKILL ROUTE -> ONE MOVE -> PROOF -> LEARN -> CLOSE**

## Durable system lineage

For cross-project lineage, whole-estate salvage, the origin of the system, and the long-running architecture Randy has been building across repos, files, connected apps, and project generations, read:

1. `docs/ORIGIN_STORY.md`
2. `docs/SYSTEM_LINEAGE_START_HERE.md`
3. `docs/FIVE_YEAR_ARTIFACT_SALVAGE_MASTER_CONTEXT.md`
4. `state/ESTATE_COVERAGE_LEDGER.md`
5. `docs/ECOSYSTEM_RECOVERY_MASTER_CONTEXT_2026-09-19.md`
6. `state/ECOSYSTEM_AUTHORITY_INDEX.json`

`docs/ORIGIN_STORY.md` explains why this system exists, who the human behind it is in working terms, what he does and does not want from AI, and what future AI systems must not misunderstand.

The other lineage files preserve the non-sensitive architectural realization, reusable mechanism map, source-yard coverage, and current direction so future AI systems do not require Randy to re-explain years of work.

These files are **lineage/context**, not live authority. Current truth still comes from the active project repo/device/deploy.

Before creating a new core mechanism, apply the global **RECOVER BEFORE REBUILD** rule in `state/DECISIONS.md`: search ChatGPT Library/files, live project/GitHub authority, and prior lineage first; only then widen to public web research.

## Repository boundaries

Harness Card may store:
- operating rules;
- routing logic;
- project pointers and non-sensitive state;
- work-order templates;
- incident and release templates;
- reusable skills or pointers to canonical skill sources;
- schemas and validation rules;
- non-sensitive cross-project lineage and architecture context needed to prevent repeated rediscovery.

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