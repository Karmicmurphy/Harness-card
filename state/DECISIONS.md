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
