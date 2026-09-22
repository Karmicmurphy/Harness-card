# Decisions and Corrections

This file stores durable, non-sensitive decisions that future agents should not force Randy to repeat.

## Entry format

### YYYY-MM-DD — Short decision name
- **Type:** TARGET / STATE / CONSTRAINT / EVIDENCE / SCOPE / NAMING / OTHER
- **Decision or correction:**
- **Why it matters:**
- **Applies to:** global harness / named project
- **Authority/evidence:**
- **Reopen condition:** what new evidence would justify revisiting this?

## Rules

- A correction repairs the model first; it does not automatically broaden scope.
- Do not reopen settled decisions without new evidence or explicit user request.
- Do not put sensitive personal information in this public repo.

### 2026-09-19 — Recover before rebuild
- **Type:** CONSTRAINT / EVIDENCE / SCOPE
- **Decision or correction:** Before inventing, researching publicly, or building a new core mechanism, first recover existing work from ChatGPT Library/files, live GitHub/project authority, and prior lineage/context. Public web research comes after internal recovery.
- **Why it matters:** Repeated work has rebuilt or renamed mechanisms that already existed across CERT-RIVER, PRISM-RIVER, FlashRiver, RiverKernel, Untethered AIOS, Harness Card, Digital Scrapyard, Twis Holo Workshop, and related archives. Randy must not be required to remember which repo/file/chat contains the existing mechanism.
- **Applies to:** global harness / all projects
- **Authority/evidence:** `docs/ECOSYSTEM_RECOVERY_MASTER_CONTEXT_2026-09-19.md`; `state/ECOSYSTEM_AUTHORITY_INDEX.json`; `docs/FIVE_YEAR_ARTIFACT_SALVAGE_MASTER_CONTEXT.md`; Master Thread Salvage V2 Library package.
- **Reopen condition:** Only if a newer verified authority index replaces this recovery rule with an equal-or-stronger automatic recovery mechanism.

### 2026-09-21 — Foundation project-bleed containment
- **Type:** SCOPE / AUTHORITY / CONSTRAINT
- **Decision or correction:** Foundation V0 may be changed only from repo/branch authorities explicitly named in the current Foundation authority/activation files. Any other chat, Codex workspace, branch, PR, archive, repo, or product is treated as SALVAGE, QUARANTINE, or SEPARATE PROJECT until live evidence is reconciled and the primitive is explicitly promoted into Foundation authority.
- **Why it matters:** Work from Loop Deck / Pro Rig, First3 Local, Digital Scrap Forge, Coilside, older AIOS successor branches, Codex scratch work, and other projects has bled across chats and created false current state. Randy must not be required to remember which conversation or workspace a mechanism came from.
- **Applies to:** Foundation V0 / global harness recovery
- **Authority/evidence:** `state/CURRENT_PROJECT.json`; `docs/FOUNDATION_V0_ACTIVATION_MAP_2026-09-21.md`; `state/FOUNDATION_V0_ACTIVATION_MAP_2026-09-21.json`; live repo/branch heads.
- **Reopen condition:** Only when a candidate artifact/branch passes recovery, provenance/rights classification, and a bounded proof showing why it belongs in the Foundation authority chain.


### 2026-09-21 — Foundation improvement is human-owned, not self-evolving
- **Type:** TARGET / CONSTRAINT / AUTHORITY
- **Decision or correction:** Foundation V0 may use successful traces to propose cheaper reusable capability through Capability Downshift, but it does not autonomously rewrite, promote, activate, deploy, publish, spend, delete, expand permissions, or change governance. Ordinary jobs end at certified human review. Reusable-capability proposals end at human approval, and activation remains a separate explicit action.
- **Why it matters:** The intended system is a human-owned software factory that can become more efficient from proven experience, not a self-evolving AI. Keeping ordinary work separate from capability promotion prevents useful job execution from being confused with changes to the factory itself.
- **Applies to:** Foundation V0 / global language when describing Foundation improvement
- **Authority/evidence:** `temporal-capability-foundry/src/foundry/foundation_core.py`; human runner proof run `35628459336`; certificate-aware promotion proof run `35620968656`; `docs/FOUNDATION_CORE_V0.md`.
- **Reopen condition:** Only if Randy explicitly changes the human-approval boundary and a separate safety/proof design is approved.


### 2026-09-22 — PersonalJarvis / FRIDAY shelved; discovery lane takes priority
- **Type:** TARGET / SCOPE / STATE
- **Decision or correction:** PersonalJarvis and FRIDAY are not the current goal and must not be presented as the next step. Their unmerged candidate work is preserved only as salvage/reference. The active lane is deterministic estate discovery: collide recovered mechanisms, surface non-obvious cross-domain fits, then falsify the strongest lead cheaply.
- **Why it matters:** Repeatedly steering the project toward assistant integration was not aligned with the owner's actual goal and consumed attention without answering the deeper discovery question.
- **Applies to:** Foundation V0 / Digital Scrapyard / global harness routing
- **Authority/evidence:** Owner correction on 2026-09-22; Foundry PR #22 closed unmerged; Digital Scrapyard Missing Gear Collision Engine merged at `c5d06aabf54d9187a8478047eda5393d8be68673`; proof runs `35700359307` and `35700359308`.
- **Reopen condition:** Only on a new explicit owner decision to make PersonalJarvis / FRIDAY active again.


### 2026-09-22 — Missing Gear novelty gate exposed atomization gap
- **Type:** EVIDENCE / TARGET / CONSTRAINT
- **Decision or correction:** Known overlaps, existing lanes, status labels, mode, evidence state, cost, priority, and rights metadata are context only and cannot earn Missing Gear novelty points. After enforcing that rule and typing the PersonalJarvis warehouse intake, the combined estate+warehouse run loaded 36 artifacts, produced 7 scored collisions, and produced zero cross-domain survivors; all seven were within the single richly typed PersonalJarvis source.
- **Why it matters:** The collision engine is no longer mainly fooled by labels. The limiting factor is now representation quality: most source yards are mapped at project/capability level rather than decomposed into provenance-backed typed mechanisms, inputs, outputs, and interfaces.
- **Applies to:** Estate discovery / Digital Scrapyard / Foundation discovery lane
- **Authority/evidence:** Digital Scrapyard main `75d83feeb566d19e58b00d43404a640c67930787`; PR #23; proof runs `35730332924` and `35730333270`.
- **Reopen condition:** Revisit only if a later multi-source typed-atom run shows that metadata suppression removed genuinely useful discovery evidence or a stronger typed representation replaces this rule.
