# Project Index

Harness Card does not own project code. It points to the authoritative project location and records only non-sensitive continuity data.

## Entry format

### Project name
- **Purpose:**
- **Authority refs:**
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
- Do not duplicate exact active component SHAs here; `state/CURRENT_PROJECT.json` owns the active immutable refs.
- Do not duplicate the project's source code here.
- Do not place sensitive/private material in this public repo.
- If authority is ambiguous, run context harvesting before building.


### FOUNDATION V0 — HUMAN-OWNED SOFTWARE FACTORY
- **Purpose:** Accept ordinary human signal, recover current truth, route canonical skills/capabilities, salvage before rebuild, execute bounded work, prove it independently, and return an understandable human-owned result without making the owner conduct the internal machinery.
- **Authority refs:** See `state/CURRENT_PROJECT.json`. That file alone owns the current approved component branches and immutable SHAs; this index must not duplicate them.
- **Default branch:** See `state/CURRENT_PROJECT.json`.
- **Live/deploy target:** Existing Cloudflare Pages Workshop as the phone-facing field doorway, with private/local Windows Workshop preserved as separate private authority where applicable. The active target is the bounded Android phone round trip, not a Windows-only vertical slice.
- **Current evidence state:** PARTIALLY_PROVEN. Foundation core execution/correlation/proof are proven in test and a real bounded candidate dispatch has carried one Foundation job identity through Foundry -> AIOS -> Builder -> Independent Proof -> correlated receipt. The complete authenticated Android Workshop -> Pages -> dispatch -> proof -> Workshop return is not yet PROVEN_LIVE.
- **Current work order:** `PAGES_BOUNDED_JOB_ROUND_TRIP`; canonical detail is generated into `state/ACTIVE_WORK_ORDER.json` and `state/ACTIVE_WORK_ORDER.md` from `state/CURRENT_PROJECT.json`.
- **Last verified:** 2026-09-29 for repository/phone-gate continuity; account-side Cloudflare values remain subject to live re-verification.
- **Do not restart / locked exclusions:** Do not build another OS, skill suite, proof engine, agent framework, standalone Workshop Worker, D1/queue orchestration layer, or model-routing expansion while the bounded phone gate remains open. Do not reopen PersonalJarvis / FRIDAY without a new explicit owner decision. Do not promote subsystem CI or candidate PR success to whole-machine PROVEN_LIVE.
- **Notes:** Current Cloudflare/phone state is preserved in `state/CLOUDFLARE_PHONE_GATE_HANDOFF_2026-09-29.md`. Candidate Foundry and Workshop changes remain review candidates until canonical Harness authority explicitly promotes them. Finish the bounded owner path before arbitrary natural-language coding or optional upgrades.


### TWIS LOOP DECK
- **Purpose:** Phone-first local looper/groovebox with a simple one-screen performance shell over the existing V2 audio engine.
- **Authority repo/path/device:** `Karmicmurphy/Ollie_Twis_Holo_workshop` · `app/loop-deck.html`
- **Default branch:** `main`
- **Live/deploy target:** UNKNOWN / not re-verified during this work order
- **Current evidence state:** PROVEN_IN_TEST
- **Current work order:** Prove the merged simple performance shell on the target Android phone through the real user path.
- **Last verified:** 2026-09-18T00:14:00Z · historical main ref retained in its own project history, not Foundation authority
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
