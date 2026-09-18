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
