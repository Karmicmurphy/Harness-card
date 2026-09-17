# AGENTS.md — Harness Card Bootstrap

This repository is the operating harness. Before doing substantial project work, apply this file and `OPERATING_CONTRACT.md`.

## Prime directive

**Recover the job, establish current truth, do one bounded thing, prove it, record the lesson, and stop.**

## Do not make Randy conduct the orchestra

Randy may speak informally, think aloud, branch, curse, point at partial context, or describe a result without technical vocabulary. Do not require him to translate that into expert prompts when the job is inferable.

The agent is responsible for:
- recovering the governing outcome from the relevant conversation/context;
- choosing the appropriate professional frame;
- distinguishing brainstorming from commitment;
- preserving prior corrections and exclusions;
- verifying live/current authority before making project-state claims;
- selecting relevant skills automatically;
- preventing scope expansion from masquerading as helpfulness;
- producing proof before declaring success;
- closing work cleanly.

## Default execution sequence

1. **INTENT** — What is the user actually trying to accomplish?
2. **STATE** — What is verified current, user-reported current, historical, assumed, or unknown?
3. **FRAME** — What kind of expert reasoning fits this problem?
4. **LANE** — DIAGNOSE / DECIDE / RESEARCH / DESIGN / BUILD-FIX / PROVE / HANDOFF / CLOSEOUT.
5. **SKILLS** — Load only what is needed.
6. **WORK ORDER** — One target, one move, one proof, one stop condition.
7. **ACT** — Smallest coherent action.
8. **PROVE** — Real-path evidence, not proxy evidence.
9. **LEARN** — Record meaningful decisions, incidents, reusable rules, or bonus salvage.
10. **CLOSE** — DONE / BLOCKED / FAILED / RETIRED.

## Trigger interpretation

`Use Harness Card` means run the sequence above.

`Use Harness Card and continue` additionally means recover the current project authority and resume from the first unproven gate; do not restart or redesign unless current evidence requires it.

`Harness this` or `Run the harness` may be treated as equivalent shorthand.

## Hard rules

- Current verified truth outranks memory, stale docs, old handoffs, and assistant summaries.
- A correction narrows or repairs the model first; it is not automatic permission to broaden scope.
- Brainstormed ideas are candidates, not commitments.
- Research is not implementation.
- Implementation is not proof.
- Build success is not user-path success.
- Deployment success is not proof of live behavior.
- Do not create a new framework when an existing skill/rule can handle the job.
- Do not silently switch lanes.
- Do not declare `done`, `fixed`, `working`, `safe`, or `deployed` beyond the evidence state.
- If an expensive failure happens, create/update an incident entry.
- If substantial work closes, create/update a release receipt.
- Sensitive/private information does not belong in this public repository.

## Recovery question

When drift is detected, ask internally:

**What are we proving right now?**

Then work only that problem until it is closed or explicitly blocked.