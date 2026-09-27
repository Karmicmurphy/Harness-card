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
- **Purpose:** Accept ordinary human signal, recover current truth, route canonical skills/capabilities, salvage before rebuild, execute bounded work, prove it independently, and return an understandable human-owned result without making the owner conduct the internal machinery.
- **Authority repo/path/device:** Governance `Karmicmurphy/Harness-card@main`; factory `Karmicmurphy/temporal-capability-foundry@software-builder-v0` at `3bb8e0d073f4bdda2af414340633a95b0e182887`; runtime `Karmicmurphy/Untethered-AIOS@main`; salvage `Karmicmurphy/digital-scrapyard-autopilot@main`; cockpit `Karmicmurphy/Ollie_Twis_Holo_workshop@living-workshop-main-build` at `f083c699d0dbf1837a8f207a53bcb243abc06be2`.
- **Default branch:** See `state/CURRENT_PROJECT.json`; that file is the current machine-readable authority.
- **Live/deploy target:** Owner's local Windows Workshop + loopback Foundry service. Live field proof is still pending.
- **Current evidence state:** FOUNDATION_CORE_V0_OPERATIONAL_IN_TEST; HUMAN_SIGNAL_ARRIVAL_V0_PROVEN_IN_TEST_AND_MERGED; WORKSHOP_FOUNDRY_LOOPBACK_BRIDGE_V0_PROVEN_IN_TEST_AND_MERGED; LOCAL_SOURCE_YARD_INVENTORY_V1_PROVEN_IN_TEST; LIVE_WINDOWS_VERTICAL_SLICE_NOT_YET_PROVEN.
- **Current work order:** `state/ACTIVE_WORK_ORDER.json` and `state/ACTIVE_WORK_ORDER.md`, both required to agree with `state/CURRENT_PROJECT.json`.
- **Last verified:** 2026-09-24.
- **Do not restart / locked exclusions:** Do not build another OS, skill suite, proof engine, or agent framework. Do not reopen PersonalJarvis / FRIDAY without a new explicit owner decision. Do not promote subsystem CI to whole-machine PROVEN_LIVE.
- **Notes:** The highest-value next evidence is no longer more blind cloud discovery. It is a live Windows vertical slice proving Workshop -> Foundry arrival, bounded local source-yard inventory, and then one shared correlation identity through Foundry -> AIOS -> Independent Proof -> Workshop.


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


### SALVAGE FOUNDRY — MECHANISM SALVAGE AND EVOLUTION RESEARCH
- **Purpose:** Turn historical and current engineering artifacts into traceable mechanism cards keyed by function and constraint; recombine and test candidates; compare challengers against incumbents; independently prove results; preserve rollback; and accumulate Wisdom so the machine reuses proven mechanisms and progressively downshifts repeatable AI work into cheaper deterministic capabilities.
- **Authority repo/path/device:** Governance/handover `Karmicmurphy/Harness-card@main` at `docs/SALVAGE_FOUNDRY_RESEARCH_HANDOVER_2026-09-27.md`; canonical salvage primitives in `Karmicmurphy/digital-scrapyard-autopilot@main`; experiment factory in `Karmicmurphy/temporal-capability-foundry@software-builder-v0`; runtime `Karmicmurphy/Untethered-AIOS@main`.
- **Default branch:** Harness `main`; downstream authority remains whatever `state/CURRENT_PROJECT.json` approves when this project is explicitly promoted to active work.
- **Live/deploy target:** NONE for research handover. V0 target is a bounded disposable incumbent/challenger experiment through existing Foundry -> AIOS -> Independent Proof, not a public deployment.
- **Current evidence state:** PARTIALLY_PROVEN — constituent mechanisms already exist/prove independently (Harness deterministic learning, Artifact Compass/Salvage, Missing Gear, Foundry/AIOS/Independent Proof), but the integrated Mechanism Card -> challenger -> certificate -> Wisdom loop is NOT_YET_PROVEN.
- **Current work order:** QUEUED. Canonical handover: `docs/SALVAGE_FOUNDRY_RESEARCH_HANDOVER_2026-09-27.md`. When owner explicitly selects/promotes this project, execute the V0 implementation order from that handover rather than restarting research from chat history.
- **Last verified:** 2026-09-27.
- **Do not restart / locked exclusions:** Do not create another OS, agent framework, proof engine, or Salvage Foundry monolith. Do not re-import PersonalJarvis wholesale. Do not give AI workers promotion authority. Do not allow candidates to edit their own proof/authority boundary. Do not add autonomous crawling, broad deployment, spending, or a large UI before V0 proves second-run improvement.
- **Notes:** Research reached working saturation under the Adaptive Pass Rule. The main missing gear is a general `Mechanism Card -> incumbent/challenger -> independent certificate -> promotion/rollback -> Wisdom` loop. This project is intentionally queued so it does not displace the currently active Foundation work order unless the owner explicitly promotes it.