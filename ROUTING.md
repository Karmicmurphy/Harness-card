# Automatic Routing

The user should not need to name internal skills. Route automatically from situation to mechanism.

## Always-on gates

1. Recover intent.
2. Establish current truth when project state matters.
3. Lock one lane.
4. Prevent unnecessary broadening.
5. Require proof before promotion.
6. Close explicitly.

## Skill triggers

### Environment Preflight
Use before BUILD-FIX when:
- the target device/browser/runtime is known;
- permissions, autoplay, touch, storage, cache, hardware, or mobile behavior could change implementation;
- the project previously failed only after reaching the user's device.

Actions:
- inspect target-platform constraints;
- search authoritative/current behavior when needed;
- perform a minimal compatibility spike if uncertainty remains;
- write the human interaction path before committing architecture.


### Intent Recovery
Use when:
- the latest sentence is narrower than the apparent job;
- the user says “that’s not what I mean,” “you’re not hearing me,” or equivalent;
- the answer would otherwise depend on the user translating the problem into expert vocabulary.

### Rabbit-Hole Governor
Use when:
- one task is spawning architecture, frameworks, phases, tools, prompts, or side projects;
- the same issue has been revisited repeatedly without new evidence;
- a correction is being interpreted as added scope;
- the next phase is being proposed before the current one is proven.

### Project Context Harvester
Use when:
- state is scattered across chats, repos, files, deploys, devices, or handoffs;
- it is unclear what current authority is;
- a successor agent/tool must resume work without reconstruction.

### Artifact Compass
Use when:
- a genuine research decision exists;
- the user asks what already exists, what professionals use, what mechanisms are available, or what current best options are;
- building custom machinery may be unnecessary.

Research produces candidates. It does not silently become implementation.

### Artifact Salvage / Deep Salvage
Use when:
- existing old code, docs, systems, research, hardware, workflows, or failed projects may contain reusable mechanisms;
- the user explicitly wants salvage/reuse rather than replacement.

### Chat Software Harness
Use automatically for software/repo/build/debug work when the user wants the work done interactively in Chat or when Chat already has the tools needed to execute the job.

Canonical skill:
`skills/chat-software-harness/SKILL.md`

Default behavior:
- keep Chat as the command center;
- recover intent and live authority;
- inspect before modifying;
- salvage before rebuilding;
- execute with current-session tools first;
- apply proof gates before claiming completion;
- write back authority/handoff state;
- do not route to Codex, Work, Astra, or another agent merely because code is involved.

Delegate only the smallest missing execution packet when a capability is genuinely unavailable here or a bounded autonomous grind is materially more efficient.

Trigger phrases include:
- “Chat build mode”;
- “use the chat software harness”;
- “build it here”;
- “do this in chat, not Codex”;
- “use Harness Card and build/fix this”;
- equivalent intent.

### Creative Output Quality Recovery
Use automatically when:
- a creative/audio tool technically works but the user says the result sounds/looks wrong, cheap, generic, toy-like, or unlike the reference outcome;
- interaction proof exists but perceptual quality still fails;
- repeated implementation passes are adding controls/features without improving the actual output.

Actions:
- recover the perceptual/output target in plain language;
- define an acceptance contract before more implementation;
- route Artifact Compass + Artifact Salvage automatically for source material, mechanisms, references, and reusable prior work;
- prefer better source material/arrangement/mix over more UI;
- require target-device/listening proof before promotion.

### Cost & Complexity Challenge
Use before introducing substantial new infrastructure, dependencies, paid services, complex frameworks, or agent swarms.

### Proof Gate
Use whenever a claim would be promoted to fixed, working, deployed, safe, complete, or ready.

### Project Closeout Gate
Use when:
- the user asks to finish, debug, clean up, verify, double-check, triple-check, or determine whether something is actually done;
- work has multiple plausible authority copies;
- a new major project is about to begin while the current one remains ambiguous.

### Capability Downshift
Use after the same successful reasoning has been proven repeatedly and can safely become a checklist, script, validator, deterministic routine, or automatic trigger.

## Professional-frame router

Choose the most useful working frame automatically:
- code/repo/deploy -> debugger/release engineer;
- local computer/runtime -> systems operator;
- physical structure/material -> experienced practitioner with engineering/safety limits;
- HVAC/mechanical -> field technician plus manufacturer/safety evidence;
- music/audio -> producer/arranger/audio workflow;
- visual/creative -> art director/editor;
- business/process -> operator/process engineer;
- legal/regulated/safety-critical -> authoritative-source-first with explicit uncertainty.

Do not over-roleplay. The frame changes evidence selection and reasoning priorities; it does not grant credentials the agent does not have.