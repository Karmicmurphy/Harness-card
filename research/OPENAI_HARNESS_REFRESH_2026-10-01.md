# OpenAI harness refresh — 2026-10-01

Purpose: Artifact Compass / Artifact Salvage pass over current OpenAI developer guidance that materially affects Harness Card, phone-first software work, skills, and long-running agent workflows.

This is research evidence, not automatic authority. Only the specific lessons promoted into Harness rules/skills are active.

## Sources reviewed

### OpenAI Developers — Rethinking skills and prompts for GPT-6 Astra
Published 2026-09-11.

https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

Relevant findings:

- Skill descriptions should be short and precise about when they apply.
- Too many broad skills create context pressure and routing ambiguity.
- Progressive disclosure is preferred: keep root skill material small and route to supporting references/scripts only when needed.
- `AGENTS.md` should point to contextual documentation instead of forcing a full documentation load before every edit.
- Old guardrails/instructions should be revisited when newer models make them redundant or over-constraining.
- Completion conditions should be explicit; capable agents may otherwise stop at a first implementation when the real task includes running, inspecting, repairing, and proving the result.

Harness adoption:

- Chat Software Harness 1.1 adds a Context discipline section.
- Provider/deployment debugging moved into a targeted reference file rather than bloating the root skill.
- Fast bootstrap now selects only needed skills/references.
- Proof language explicitly separates patched, CI green, deployed, and fixed.

### OpenAI Developers — Mastering remote engineering work from your phone
Published 2026-06-23.

https://developers.openai.com/blog/mastering-codex-remote-for-engineering

Relevant findings:

- Treat the phone as the control plane, not as a tiny desktop terminal.
- The execution environment should remain where the repository, credentials, simulator, or runtime belongs.
- Durable goals should describe the completion condition across implementation, tests, review, and cleanup.
- Use steering only when current work is heading in the wrong direction; queue unrelated follow-up work.
- Keep permissions narrow and explicit.
- Mobile engineering works best when owner decisions are separated from mechanical execution.

Harness adoption:

- Reinforces the existing Android-primary control-surface direction.
- New owner-interruption rule treats manual owner diagnostics as a cost and keeps repository/provider inspection in Chat where tools allow it.
- Provider deploy reference requires a single boundary-crossing owner action only when tooling cannot inspect the remaining state.

### OpenAI Developers — Testing Agent Skills Systematically with Evals
Published 2026-01-22.

https://developers.openai.com/blog/eval-skills

Relevant findings:

- Skill quality should be tested, not judged by feel.
- Useful skill evals separate outcome goals, process goals, style goals, and efficiency goals.
- A practical eval is prompt -> captured run/trace/artifacts -> deterministic and rubric checks -> comparable score.
- Efficiency/thrash should be measured alongside correctness.

Harness adoption:

- Foundation incident now records owner-interruption waste and repeated failure cycles, not only final correctness.
- Future Chat Software Harness eval should score: correct skill/rule selection, number of unnecessary owner actions, repeated retries without new evidence, proof-level accuracy, and final user-path result.

### OpenAI — Introducing the Agents API
Published 2026-09-10.

https://openai.com/index/introducing-the-agents-api/

Relevant findings:

- The Agents API exposes the managed harness/infrastructure behind Codex for long-running agents.
- It supports hosted or partner execution environments and explicit capability directories for skills.
- The underlying Codex harness is open-source, making its orchestration patterns inspectable.

Harness adoption / decision:

- No migration is required for the current Foundation phone gate.
- Agents API is a future candidate for bounded autonomous work only when it removes a real missing execution capability.
- Do not introduce it merely because it is newer; current Chat + GitHub + Cloudflare path remains the smallest architecture for this incident.

### OpenAI Developers — OpenAI Developers plugin
Current documentation checked 2026-10-01.

https://developers.openai.com/learn/developers-codex-plugin

Relevant findings:

- The OpenAI Developers plugin packages current OpenAI platform guidance and developer skills.
- It includes OpenAI API Platform access, OpenAI Docs MCP, API key setup guidance, and Agents SDK workflows.

Harness adoption / recommendation:

- The plugin is useful as a current-documentation source for future OpenAI API/Agents work.
- It is not required to finish the Cloudflare phone-path incident.

### OpenAI product guidance — plugins, Work, and apps
Current product documentation checked 2026-10-01.

Relevant findings:

- Plugins package skills, connected apps, and reusable workflows across ChatGPT and Codex.
- Apps remain the underlying external-service connections.
- ChatGPT Work is appropriate for longer multi-step web/app work when a cloud browser/computer environment is specifically needed.

Harness adoption:

- Continue to prefer current-session direct tools for bounded repo/debug work.
- Add a plugin or Work only when it closes a concrete capability gap; do not route software work away from Chat by default.

## Artifact Salvage verdict

Keep and strengthen:

- live authority recovery;
- repair loop;
- proof-state ladder;
- state writeback;
- explicit stop conditions;
- target-device proof;
- salvage before rebuild.

Refactor:

- broad always-read instruction stacks -> contextual references;
- provider debugging -> dedicated progressive-disclosure reference;
- vague completion -> explicit user-path closure;
- correctness-only learning -> include efficiency/owner-interruption metrics.

Do not add now:

- Agents API migration;
- new agent swarm;
- new model router;
- another deployment provider;
- new infrastructure for the current phone gate.

## New eval targets for Chat Software Harness

A future repeatable field eval should check:

1. Did Chat recover the correct active project/branch without asking the owner to restate it?
2. Did it inspect live authority before proposing a fix?
3. Did it identify the failing layer before modifying code?
4. Did it inspect sibling failure modes after the first user-visible failure?
5. Did it avoid unnecessary owner/manual actions?
6. Did it distinguish zero-job workflow validation from application failure?
7. Did it distinguish PROVEN_IN_TEST from PROVEN_LIVE?
8. Did it write back incident learning and current state?
9. Did it stop at the locked outcome instead of broadening architecture?
10. Did the actual target user path work?

## Bottom line

The strongest current OpenAI guidance supports a *smaller, more selective, more evidence-driven* Harness Card: short routing instructions, progressive disclosure, explicit completion, eval-backed skills, and a phone-as-control-plane workflow. The 2026-10-01 Foundation incident confirms that the biggest practical gap was not missing architecture; it was failing to prove configuration authority and runtime truth before repeated retries.
