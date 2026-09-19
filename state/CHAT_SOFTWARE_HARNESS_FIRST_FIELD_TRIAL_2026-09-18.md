# Chat Software Harness — First Field Trial

Date: 2026-09-18
Project: TWIS Pro Rig V4 / Loop Deck
Harness skill: `skills/chat-software-harness/SKILL.md`
Project repo: `Karmicmurphy/Ollie_Twis_Holo_workshop`
Final project SHA at this checkpoint: `b9f0484e6673f79ce81bca74c770ee8b089d34cf`
Evidence state: PROVEN_IN_TEST
Live sonic/device proof: PENDING

## What the harness was asked to do

Resume the existing Pro Rig work in ordinary Chat, recover current authority without making Randy restate the project, use relevant Harness Card rules/skills automatically, debug the current implementation, keep the same app usable on phone and PC, improve the sound path, record failures, and continue until the next genuinely unproven gate.

## Wins

1. **Authority recovered without restart**
   - Loaded Harness Card authority and the live Workshop repo.
   - Resumed from the current unproven gate instead of rebuilding from scratch.

2. **Stayed in Chat instead of delegating by default**
   - Repository inspection, branching, edits, CI inspection, PR creation, merge, and state writeback were all performed from interactive Chat.

3. **Salvage-before-build worked**
   - Existing Loop Deck import/loop subsystem was preserved.
   - V4 reused the proven timing/control ideas instead of replacing the whole product.

4. **Evidence language stayed bounded**
   - V4 was kept at IMPLEMENTED_UNPROVEN / PROVEN_IN_TEST rather than being called PROVEN_LIVE before real device/listening proof.

5. **Repair loop worked on a stale regression**
   - First V4 CI failed because a V3-specific contract still pinned the old script.
   - The failure was inspected, classified as TEST-CI/CONTRACT, repaired narrowly, and rerun to green.

6. **Repair loop worked on browser proof**
   - First Playwright proof failed when external sample CDN requests returned HTTP 400.
   - The test was corrected so external sample failure is accepted only when the product reaches the explicit FALLBACK OK state.
   - Desktop-size and Pixel-size Chromium paths then passed.

7. **Proof got materially stronger**
   - The project now has automated runtime proof for silent entry, PLAY, running AudioContext, BREAK, VOCAL HIT, BUILD, ECHO, WASH, and STOP at desktop and phone-sized Chromium dimensions.

8. **State was written back**
   - Harness Card CURRENT_PROJECT and ACTIVE_WORK_ORDER were updated as the project advanced.

## Failures / catches

### F1 — Stale V3 contract survived into V4
- Layer: TEST-CI / CONTRACT.
- Result: first V4 CI failed.
- Cause: implementation entrypoint changed before old version-specific contract was updated.
- Fix: update contract to current V4 entrypoint and behavior.
- Outcome: corrected branch and main CI passed.
- Classification: INTERNAL CAUGHT FAILURE.

### F2 — Browser proof initially treated recoverable external CDN failure as product failure
- Layer: TEST-CI / EDGE.
- Result: first Playwright run failed on external sample HTTP 400 responses.
- Cause: proof harness did not distinguish local/runtime errors from optional remote asset failures even though the product had an explicit fallback path.
- Fix: local/runtime failures remain fatal; remote sample failures are logged and accepted only if the app reports READY or FALLBACK OK and the interaction path remains functional.
- Outcome: browser proof passed on desktop and phone-sized Chromium.
- Classification: INTERNAL CAUGHT FAILURE.

### F3 — Harness scorecard is stale and did not reflect current incidents
- Layer: HARNESS / AUTHORITY / LEARNING.
- Result: `state/HARNESS_SCORECARD.json` still reported the old Loop Deck authority, zero incidents, zero wins, and zero losses despite multiple recorded incident entries and the active Pro Rig V4 work.
- Cause: UNKNOWN at this checkpoint; generated scorecard did not refresh or parse current state.
- Fix: record this as a Harness Card incident and require the self-improvement/scorecard path to be checked before treating generated metrics as authority.
- Outcome: PENDING.
- Classification: HARNESS FAILURE DISCOVERED BY FIRST FIELD TRIAL.

### F4 — Irrelevant Cloudflare workflow continues to fail
- Layer: TEST-CI / PROVIDER NOISE.
- Result: Cloudflare worker workflow reports failure while GitHub Pages is the actual release path for Pro Rig.
- Cause: non-authoritative workflow remains active for this repo.
- Fix: do not use it as Pro Rig release authority; classify or scope it later rather than letting it create false project-failure signals.
- Outcome: product CI and Static Contract remain green.
- Classification: NON-BLOCKING CI NOISE.

## User-facing failures during this first harness run

None after the harness skill was explicitly activated.

The previous V3 sonic failure and earlier Android failures predate this first formal skill field trial and remain recorded separately in the Incident Ledger.

## Current proof boundary

PROVEN_IN_TEST:
- V4 source/contract tests pass.
- remote sample URLs are checked.
- deterministic fallback path exists.
- desktop Chromium browser interaction path passes.
- Pixel-sized Chromium browser interaction path passes.

NOT YET PROVEN_LIVE:
- actual Android V4 listen/use;
- actual PC V4 listen/use;
- user's sonic acceptance of the V4 result.

## First-trial verdict

**PARTIAL WIN / PROVEN_IN_TEST.**

The Chat Software Harness performed its intended command-center role on its first project trial: authority recovery, direct execution, bounded repairs, stronger proof, and durable state writeback all worked.

It is not yet globally PROVEN because the skill's own success condition requires at least two distinct projects, and this project still has real-device/sonic proof gates open.

## Next gate

Use the deployed V4 on a real Android phone and a real PC. Record exact pass/fail evidence. Fix only the layer that actually fails.
