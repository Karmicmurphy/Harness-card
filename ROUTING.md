# Automatic Routing

The user should not need to name internal skills. Route automatically from situation to mechanism.

## Always-on gates

1. Recover intent.
2. Establish current truth when project state matters.
3. Lock one lane.
4. Prevent unnecessary broadening.
5. Require proof before promotion.
6. Close explicitly.


## Executable skill resolution

Before applying a named skill, resolve it through `config/skill_registry.json` (or `python scripts/resolve_skill.py <skill>`). The resolver establishes one canonical repo/path/ref and whether the skill is procedural, conditional, executable, or only mapped. Do not silently substitute a stale duplicate from another repo.

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


### FRIDAY Provider Release (GitHub/Cloudflare)\nUse when the owner asks to publish an existing app, repair a deployment, or verify whether changes actually reached production. Resolve `friday-provider-release` through the canonical registry, use current provider evidence and `scripts/provider_release_gate.py`, and keep deployment authorization separate from live phone proof.\n\n### Business Operator Harness
Use automatically for business/commercialization work when the user wants to turn a product, service, skill, or idea into a functioning business or asks how to distribute, sell, price, automate, or prove demand.

Canonical skill:
`skills/business-operator-harness/SKILL.md`

Default behavior:
- do not require the user to already know business/marketing vocabulary;
- run demand, market, offer, pricing, trust, distribution, automation, operations, measurement, and experiment passes;
- route to Market Want Board, Artifact Compass, Artifact Salvage, Cost & Complexity Challenge, Thought Economy, Owner Interruption Minimizer, and Proof Gate as needed;
- treat no social following/no personal brand as a design constraint, not a blocker;
- prefer proof-first, low-owner-burden distribution;
- do not call a working product a proven business without transaction/acquisition evidence.

Trigger phrases include:
- “Business build mode”;
- “help me make money with this”;
- “how do I get this out there?”;
- “I don't know business”;
- “how do I sell this?”;
- “automate the business”;
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


### COILSIDE field-app win and owner-language recovery

When the owner mentions **COILSIDE**, **WTF Stupid Simple** (the field app), Sean's shared notes, Jesse's timesheet, the Cloudflare Access 403/D1 repair, or asks FRIDAY to learn from the field-app win:

- Load `state/COILSIDE_FIELD_WIN_HANDOFF_2026-10-15.md` **on demand**. Do not add this external app to the current Foundation active work order.
- Interpret emphatic/plainspoken language as an outcome constraint and urgency cue, not blanket technical authorization. Distinguish two participants from three work/pay categories; public app entry from privately paired messages; successful deployment from phone-to-phone proof.
- Recover verified Cloudflare/GitHub state first. If the Chat connector cannot perform a provider write, diagnose that connector's scope and consider an owner-confirmed provider-native action (Agent Lee) without making the owner wander through dashboard pages. Independently inspect the result.
- Never assume a stored issue automatically changes FRIDAY's runtime. Honor the authority hierarchy and route this evidence only when the problem is relevant.
- Protect local Android records: no cache clearing or profile switching before owner backup. Next unproven app gate is actual owner ↔ Sean notes and timecard save/reload/recovery, **not** another database or Worker architecture pass.

### Phone-only FRIDAY / no reliable PC

Trigger when the owner says they cannot access their PC, are operating only from Android, or asks FRIDAY to continue work despite missing local equipment.

- Load `config/owner_access_profile.json` and `state/FRIDAY_PHONE_ONLY_RECOVERY_2026-10-15.md`; recover live Harness authority and provider state before acting.
- Treat **Android as the primary operating environment**, not a degraded afterthought. Do repo, CI and provider actions through connected tools with bounded receipts. Never require a Windows launcher, local shell, past local files, or manually pasted secret tokens to make ordinary progress.
- Protect local-only authority and owner data. Inaccessible private Workshop files are UNKNOWN/UNAVAILABLE, **not** reconstructed, lost, or silently copied into GitHub.
- **Never revive an old phone/Pages gate from this router.** Recover the *current* single active gate from `state/CURRENT_PROJECT.json` (and verify the derived `state/ACTIVE_WORK_ORDER.md`) before directing work. Pages Preview and the Android end-to-end round trip are **parked** until explicitly reprioritized.\n- Preserve existing owner/provider gates for protected actions: no production changes, secret transfers, spending, broad permissions, or live dispatch without exact authorization and proof. Repo-only FRIDAY maintenance may continue within the current bounded operator policy.
- Minimize owner interruption. One phone action at a time only when the tools cannot cross an unavoidable gate, and retain a restart receipt.
- The owner need not explain their personal circumstances or housing situation to use this route. No sensitive details go in this public repository.
