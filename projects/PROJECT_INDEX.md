# Project Index

Harness Card does not own project code. It points to the authoritative project location and records only non-sensitive continuity data.

## Entry format

### Project name
- **Purpose:**
- **Authority repo/path/device:**
- **Default branch:**
- **Live/deploy target:**
- **Current evidence state:** CLAIMED / IMPLEMENTED_UNPROVEN / PARTIALLY_PROVEN / PROVEN_IN_TEST / PROVEN_LIVE / FAILED / BLOCKED / RETIRED
- **Current work order:**
- **Last verified:**
- **Do not restart / locked exclusions:**
- **Notes:**

## Rules

- Verify live authority before updating a project to a stronger evidence state.
- Historical handoffs and chat summaries are evidence, not authority.
- Do not duplicate the project's source code here.
- Do not place sensitive/private material in this public repo.
- If authority is ambiguous, run context harvesting before building.


### FOUNDATION V0 — HUMAN-OWNED SOFTWARE FACTORY
- **Purpose:** Recover current truth, salvage before rebuild, route the smallest necessary capability, build bounded candidates, prove them independently, and return human-owned receipts/approval requests.
- **Authority repo/path/device:** Governance `Karmicmurphy/Harness-card@main`; factory `Karmicmurphy/temporal-capability-foundry@software-builder-v0`; runtime `Karmicmurphy/Untethered-AIOS@main`; salvage `Karmicmurphy/digital-scrapyard-autopilot@main`; cockpit `Karmicmurphy/Ollie_Twis_Holo_workshop@living-workshop-main-build`.
- **Default branch:** See `state/CURRENT_PROJECT.json`; that file is the current machine-readable authority.
- **Live/deploy target:** No live product/deploy target is governing this lane. Current work is deterministic discovery over the recovered estate.
- **Current evidence state:** PROVEN_IN_TEST core; Missing Gear Collision V0 PROVEN_IN_TEST on the real estate capability map. PersonalJarvis / FRIDAY is SHELVED_BY_OWNER.
- **Current work order:** `state/ACTIVE_WORK_ORDER.json` and `state/ACTIVE_WORK_ORDER.md`, both required to agree with `state/CURRENT_PROJECT.json`.
- **Last verified:** 2026-09-22.
- **Do not restart / locked exclusions:** Do not route back into PersonalJarvis / FRIDAY without a new explicit owner decision. Do not rebuild proven Builder/AIOS/Independent Proof primitives without invalidating evidence. Do not treat collision ranking as proof of novelty.
- **Notes:** Current lane is estate discovery: surface non-obvious combinations, falsify the strongest lead cheaply, and keep Foundation infrastructure in the background unless needed. TWIS Loop Deck / Pro Rig, First3 Local, Coilside, Terri Tax, and commerce/product lanes remain separate unless an exact primitive is explicitly reconciled and promoted.


### TWIS LOOP DECK
- **Purpose:** Phone-first local looper/groovebox with a simple one-screen performance shell over the existing V2 audio engine.
- **Authority repo/path/device:** `Karmicmurphy/Ollie_Twis_Holo_workshop` · `app/loop-deck.html`
- **Default branch:** `main`
- **Live/deploy target:** UNKNOWN / not re-verified during this work order
- **Current evidence state:** PROVEN_IN_TEST
- **Current work order:** Prove the merged simple performance shell on the target Android phone through the real user path.
- **Last verified:** 2026-09-18T00:14:00Z · main `7e60194c36a5542b7c8bbcfcf229dc9732d03928`
- **Do not restart / locked exclusions:** Do not rebuild the audio engine. Keep the advanced V2 screens as the engine room; simple PERFORM is the default human surface.
- **Notes:** Simple shell includes eight musical-role toggles, Deep Melodic House starter pack, Energy macro, real Ghost catch, real Fuck It + undo, custom local sounds, session save/load, OPFS persistence, and Advanced escape hatch. CI/static tests passed; phone-live proof remains.
