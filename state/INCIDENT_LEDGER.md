# Incident Ledger

Record expensive failures so the same lesson is not paid for twice.

## Incident template

### INCIDENT
Short memorable name.

- **SYMPTOM:** What was actually observed; no theory yet.
- **EXPECTED:** What should have happened.
- **CURRENT AUTHORITY:** Exact repo / branch / SHA / deploy / device / file / physical state.
- **LAYER:** CONTRACT / AUTHORITY / LOCAL / TEST-CI / DEPLOY / EDGE / APPLICATION / PROVIDER / CUSTOMER / PHYSICAL / CREATIVE
- **FALSE LEADS:** What looked guilty but was not the root cause.
- **ROOT CAUSE:** One sentence, or UNKNOWN.
- **FIX:** Smallest coherent correction.
- **REGRESSION / PREVENTION:** Cheap test, checklist, rule, skill, validator, or harness behavior that catches this next time.
- **REAL-WORLD PROOF:** Evidence the corrected result works in the actual target environment.
- **PREVENTION ARTIFACT:** What durable thing was created because of this incident?
- **BONUS SALVAGE:** Useful code, sound/style, mechanism, workflow, component, or lesson discovered while fixing the failure.
- **VERDICT:** DONE / BLOCKED / FAILED / RETIRED
- **STOP:** Why work stopped instead of continuing to branch or polish.


### INCIDENT
Loop Deck looked done but phone showed old UI

- **SYMPTOM:** The user opened the published Loop Deck on Android and saw the legacy START HERE screen instead of the newly implemented simple PERFORM screen.
- **EXPECTED:** The live phone URL should open directly into the simple PERFORM surface.
- **CURRENT AUTHORITY:** `Karmicmurphy/Ollie_Twis_Holo_workshop` / `main`; current head during audit `134540fc0abf6d64a82111eb5564dd604b57b2b3`; GitHub Pages target `https://karmicmurphy.github.io/Ollie_Twis_Holo_workshop/loop-deck.html`.
- **LAYER:** APPLICATION / DEPLOY / TEST-CI / CONTRACT
- **FALSE LEADS:** Cloudflare, missing plugin, missing implementation.
- **ROOT CAUSE:** Two independent causes: the legacy guide forcibly reopened itself after the simple shell, then the prior service worker continued serving cached application assets.
- **FIX:** Remove guide auto-open; bump asset/cache versions; make script/style/worker fetches network-first with cache fallback.
- **REGRESSION / PREVENTION:** Runtime landing-screen proof is required for UI changes; static file/string tests are insufficient.
- **REAL-WORLD PROOF:** USER_REPORTED_CURRENT success. User explicitly closed the Loop Deck run as a win after using the current live link.
- **PREVENTION ARTIFACT:** Regression test blocking the known guide auto-open plus this incident record.
- **BONUS SALVAGE:** GitHub Pages alone is sufficient for the Loop Deck; Cloudflare is not required for this test path.
- **VERDICT:** DONE
- **STOP:** User reported the current live Loop Deck as a win; remaining feature-quality issues are future work, not blockers to this incident.

### INCIDENT
Harness Card preserved repo state but failed to prevent false completion

- **SYMPTOM:** Repo state and CI were recorded correctly enough to resume work, but the assistant still claimed the UI was effectively ready before the rendered user path was proven.
- **EXPECTED:** Harness Card Proof Gate should prevent any UI/app work from being called done until the target user can open and recognize the implemented artifact.
- **CURRENT AUTHORITY:** `Karmicmurphy/Harness-card` / `main`.
- **LAYER:** CONTRACT / TEST-CI / AUTHORITY
- **FALSE LEADS:** Missing repository, missing project continuity, user setup error.
- **ROOT CAUSE:** Harness Card is a repo-based operating protocol, not an automatically executing runtime guard; its proof rules were applied too weakly and its active project SHA became stale after follow-up patches.
- **FIX:** Treat rendered user path as final authority for UI work; update active authority after every material patch; record deploy target and current evidence honestly.
- **REGRESSION / PREVENTION:** UI DONE rule: repo changed -> deploy complete -> live target loaded -> expected screen verified -> user path exercised -> only then PROVEN_LIVE.
- **REAL-WORLD PROOF:** USER_REPORTED_CURRENT success of the final Loop Deck path, followed by explicit request to treat the run as a win and make the harness learn from it.
- **PREVENTION ARTIFACT:** Incident ledger entry, rendered-authority rule, failure-count rule, self-improvement loop, and UI/app hard gate.
- **BONUS SALVAGE:** Harness Card remains useful for continuity, but it must never be represented as an autonomous plugin or automatic enforcement layer.
- **VERDICT:** DONE
- **STOP:** The harness has now been changed to require the missing live-render and learning gates.


### INCIDENT
Loop Deck failure-cycle closeout

- **SYMPTOM:** Multiple iterations were needed before the user accepted the live Loop Deck as usable.
- **EXPECTED:** One implementation pass should produce a recognizable, usable live artifact without requiring the user to debug the release process.
- **CURRENT AUTHORITY:** Loop Deck repo `Karmicmurphy/Ollie_Twis_Holo_workshop`; Harness Card repo `Karmicmurphy/Harness-card`.
- **LAYER:** APPLICATION / TEST-CI / DEPLOY / EDGE / CONTRACT
- **FALSE LEADS:** Cloudflare requirement, missing plugin, absent implementation.
- **ROOT CAUSE:** Completion was promoted from proxy evidence too early; legacy startup behavior, cache persistence, and insufficient runtime proof were not treated as first-class release risks.
- **FIX:** Remove legacy override, repair cache/update behavior, redeploy, then let the user exercise the live path.
- **REGRESSION / PREVENTION:** UI hard gate, rendered-authority rule, failure-count rule, sibling-failure audit after first live failure, and self-improvement loop.
- **REAL-WORLD PROOF:** USER_REPORTED_CURRENT: user explicitly said to chalk the result up as a win.
- **PREVENTION ARTIFACT:** `SELF_IMPROVEMENT_LOOP.md` plus updated `AGENTS.md` and `OPERATING_CONTRACT.md`.
- **BONUS SALVAGE:** GitHub Pages was sufficient; Cloudflare was unnecessary for this release path.
- **VERDICT:** DONE
- **STOP:** Closeout complete; future Loop Deck feature defects belong to a new work order.


### INCIDENT
Pro Rig autoplay wash and dead controls

- **SYMPTOM:** On Android the page produced an immediate wash/noise texture, while PLAY and other controls appeared to do nothing useful.
- **EXPECTED:** The page should be silent on entry; first user interaction should initialize audio; controls should cause obvious audible and visual changes.
- **CURRENT AUTHORITY:** `Karmicmurphy/Ollie_Twis_Holo_workshop` / `main`, Pro Rig prototype.
- **LAYER:** APPLICATION / MOBILE AUDIO / CONTRACT
- **FALSE LEADS:** Button styling, missing deployment, Cloudflare.
- **ROOT CAUSE:** Tone/WebAudio graph and continuous atmosphere sources were created and started at script evaluation time instead of behind a user gesture; the control model also lacked strong one-control-one-audible-job behavior.
- **FIX:** Lazy-create the entire audio graph on first interaction, silence startup, make deck buttons control stem groups, make scenes/stems/macros auto-start safely, and preserve the wash as an intentional ocean atmosphere stem.
- **REGRESSION / PREVENTION:** Mobile WebAudio prototypes must start silent, initialize inside a user gesture, and every primary control must produce an observable state change plus an audible job.
- **REAL-WORLD PROOF:** PENDING user retest after deploy.
- **PREVENTION ARTIFACT:** Incident rule plus Weird Salvage entry for the accidental ocean wash.
- **BONUS SALVAGE:** The accidental startup wash became a deliberate ocean-atmosphere mechanism.
- **VERDICT:** BLOCKED
- **STOP:** Close only after Android retest confirms silence on load and working controls.


### INCIDENT
Android treated as compatibility instead of architecture

- **SYMPTOM:** A phone-first audio prototype was built before Android/WebAudio interaction constraints were verified, causing autoplay-style behavior and non-obvious control response on the actual device.
- **EXPECTED:** The known Android target should have shaped initialization, interaction, feedback, and proof before implementation.
- **CURRENT AUTHORITY:** Harness Card operating rules plus TWIS Pro Rig Android test.
- **LAYER:** CONTRACT / APPLICATION / MOBILE AUDIO
- **FALSE LEADS:** Styling, deployment platform, missing features.
- **ROOT CAUSE:** The implementation started from desired features and desktop-like assumptions instead of first proving the target environment and the human interaction path.
- **FIX:** Add mandatory Environment + Human Interaction Preflight, assumption stop rule, interaction contract, and acceptance tests.
- **REGRESSION / PREVENTION:** Known device/runtime constraints are architecture. No material platform assumption may pass silently into implementation.
- **REAL-WORLD PROOF:** PENDING future project where the harness performs preflight before first build and avoids this failure class.
- **PREVENTION ARTIFACT:** AGENTS preflight, Environment Contract, routing trigger, and acceptance Tests K-M.
- **BONUS SALVAGE:** The failed mobile behavior produced the intentional ocean-atmosphere layer and a reusable mobile-audio release pattern.
- **VERDICT:** BLOCKED
- **STOP:** Close when a future target-device build demonstrates preflight prevented a comparable runtime mismatch.


### INCIDENT
Controls work but the music still sounds like a browser synth experiment

- **SYMPTOM:** Android screen recording shows the Pro Rig controls responding and state changing, but the audible result still does not resemble a professional amphitheater DJ performance. The user correctly described it as a browser synth experiment rather than a finished musical instrument.
- **EXPECTED:** Pressing PLAY should immediately produce a coherent, polished deep-melodic live-set foundation with convincing drums, bass, harmony, melodic phrasing, atmosphere, vocals, transitions, and mix/master behavior. Subsequent controls should reshape that music rather than merely trigger simple synthesis events.
- **CURRENT AUTHORITY:** `Karmicmurphy/Ollie_Twis_Holo_workshop` / `main` / `43bc7f67b3988b56dcd6987594e0a84160e0041f`; GitHub Pages `/pro-rig.html`; Android screen recording supplied by user on 2026-09-18.
- **LAYER:** CREATIVE / APPLICATION / CONTRACT
- **FALSE LEADS:** Android itself, button wiring, deployment, transport state, UI responsiveness.
- **ROOT CAUSE:** We repeatedly translated "sound like a professional amphitheater DJ set" into interface features and browser-synth mechanisms without first creating a sonic acceptance contract or sourcing/proving professional-grade musical content. We optimized interaction before sound quality.
- **FIX:** Freeze UI growth. Define a sonic reference contract first: genre/energy target, drum quality, bass movement, harmonic language, melody behavior, vocal role, transitions, dynamics, loudness, stereo space, and what a 30-second successful performance must sound like. Then Artifact Compass/Salvage real open/permissive musical engines, samples, stems, effects, and arrangement mechanisms against that contract before implementation.
- **REGRESSION / PREVENTION:** For music products, "controls work" is interaction proof only. No music build may be promoted until an audible reference-path test passes. Build musical content/arrangement/mix first, then expose controls. Require a SONIC_ACCEPTANCE.md before implementation.
- **REAL-WORLD PROOF:** USER_REPORTED_CURRENT: interaction works on Android, but sonic quality target is not met. This is direct target-device evidence.
- **PREVENTION ARTIFACT:** This incident record; next work order must create a sonic acceptance contract before further code changes.
- **BONUS SALVAGE:** The current V3 interaction surface, gesture-safe audio startup, scene/stem control model, and ocean-atmosphere mechanism are reusable once connected to better musical material.
- **VERDICT:** BLOCKED
- **STOP:** Do not add more UI or synth features until the sonic target and source-material strategy are proven.


### INCIDENT
Pro Rig prototype was treated as product progress before sonic proof

- **SYMPTOM:** Multiple Pro Rig iterations added professional-looking controls and technically valid audio behavior while the user still heard toy/browser-synth output.
- **EXPECTED:** The governing success criterion should have been audible professional musical quality first, with UI/control progress secondary.
- **CURRENT AUTHORITY:** TWIS Pro Rig history through V3 and Android screen-recording evidence.
- **LAYER:** CREATIVE / CONTRACT / APPLICATION
- **FALSE LEADS:** More buttons, more synth voices, more scene labels, more visual resemblance to professional decks.
- **ROOT CAUSE:** Product intent was repeatedly translated into implementation nouns instead of the user's actual outcome: perform convincing finished-sounding music without needing producer knowledge.
- **FIX:** Create and enforce a sonic acceptance contract; require a blind 30-second musical pass before UI growth or professional-sound claims.
- **REGRESSION / PREVENTION:** For creative tools, define the perceptual/output acceptance test before selecting implementation mechanisms.
- **REAL-WORLD PROOF:** USER_REPORTED_CURRENT: prior versions failed the sonic target despite working controls.
- **PREVENTION ARTIFACT:** SONIC_ACCEPTANCE.md and V4 five-pass Compass/Salvage record.
- **BONUS SALVAGE:** Existing phone interaction and scene-control concepts remain reusable.
- **VERDICT:** BLOCKED
- **STOP:** Close after a live V4 listen meets the sonic contract on target devices.


### INCIDENT
Pro Rig V4 first CI pass hit stale V3 contract

- **SYMPTOM:** V4 JavaScript syntax and remote sample reachability passed, but Python contract collection failed because an older test still required the V3 script name.
- **EXPECTED:** A new version should update/retire version-specific regression assertions as part of the same bounded change.
- **CURRENT AUTHORITY:** Workshop branch `feature/pro-rig-v4-cross-device-sonic`; failing run 35414841606.
- **LAYER:** TEST-CI / CONTRACT
- **FALSE LEADS:** V4 engine syntax, sample CDN reachability, audio code.
- **ROOT CAUSE:** The implementation replaced the V3 entry script without updating the old V3-specific contract before the first CI run.
- **FIX:** Update the historical Amphitheater contract to assert V4 wiring and current engine behavior.
- **REGRESSION / PREVENTION:** Version replacement checklist must inspect tests that pin old entrypoints before first push/merge.
- **REAL-WORLD PROOF:** PROVEN_IN_TEST: corrected V4 SHA `34c486f5e5a7b8dc3033568972063e5e64925b09` passed Workshop CI and Static Contract; merged main SHA `d5527703b348b65956ea4ac8a1792cc02326480f` also passed Workshop CI, Static Contract, remote sample reachability, and static build.
- **PREVENTION ARTIFACT:** Updated contract test plus this incident.
- **BONUS SALVAGE:** CI correctly caught stale test authority before merge.
- **VERDICT:** DONE
- **STOP:** Corrected contracts passed on branch and main.


### INCIDENT
Cross-device claim outran PC proof

- **SYMPTOM:** The project goal expanded to "same rig on phone and PC," but only Android interaction had direct user proof.
- **EXPECTED:** Cross-device support must be proven on at least one target phone browser and one target desktop browser before being called working everywhere.
- **CURRENT AUTHORITY:** V4 branch targets one responsive web app; Android prior evidence exists; desktop live evidence is not yet recorded.
- **LAYER:** CONTRACT / APPLICATION / TEST-CI
- **FALSE LEADS:** Responsive CSS or a shared URL alone proving cross-device behavior.
- **ROOT CAUSE:** Shared web technology was treated as implied cross-device proof rather than an implementation strategy requiring separate runtime verification.
- **FIX:** Same code path plus desktop and Android live-path proof; add runtime diagnostics and fallback audio assets.
- **REGRESSION / PREVENTION:** Any "works on phone and PC" claim requires separate target-device evidence records.
- **REAL-WORLD PROOF:** PENDING.
- **PREVENTION ARTIFACT:** V4 diagnostics and cross-device work-order proof gate.
- **BONUS SALVAGE:** One web codebase remains the right architecture if both device proofs pass.
- **VERDICT:** BLOCKED
- **STOP:** Close only after both phone and PC paths are exercised.


### INCIDENT
Harness scorecard stale during first Chat Software Harness field trial

- **SYMPTOM:** `state/HARNESS_SCORECARD.json` still reported TWIS LOOP DECK at old SHA `134540fc0abf6d64a82111eb5564dd604b57b2b3`, zero incidents, zero wins, and zero losses while the Incident Ledger and current authority already contained active TWIS Pro Rig V4 work and multiple incidents.
- **EXPECTED:** Generated scorecard should reflect current authority and summarize recorded outcomes closely enough to be trusted as a derived view.
- **CURRENT AUTHORITY:** `Karmicmurphy/Harness-card` / `main`; first formal Chat Software Harness field trial.
- **LAYER:** AUTHORITY / LEARNING / HARNESS
- **FALSE LEADS:** Missing incidents, missing project state, user failure to request a refresh.
- **ROOT CAUSE:** The self-improvement worker used double-escaped Markdown regexes, so it parsed zero incidents from a populated ledger; the workflow validated headings rather than semantic counts, allowing the empty result to be recorded as a WIN.
- **FIX:** Correct the ledger parser, fail closed when populated ledgers recover zero records, run the real self-improvement regression in CI, require nonzero semantic counts, and regenerate derived state from current authority.
- **REGRESSION / PREVENTION:** A field-trial closeout must compare generated scorecard authority/counts against canonical state before trusting the scorecard.
- **REAL-WORLD PROOF:** PROVEN_ON_MAIN 2026-09-24: repaired self-improvement run regenerated 12 incidents, 12 learned rules, 6 user-facing failure cycles, and current Foundry/Workshop authority in `state/HARNESS_SCORECARD.json`.
- **PREVENTION ARTIFACT:** Corrected parser, fail-closed semantic validation, `tests/test_self_improve.py` in the PR guard, and regenerated scorecard/rules on main.
- **BONUS SALVAGE:** The mismatch itself is a useful Fresh-Brain/Doctor check: derived state must reconcile with canonical state.
- **VERDICT:** DONE
- **STOP:** The generated scorecard now reconciles with the populated Incident Ledger and current authority; future mismatches are guarded by CI.


### INCIDENT
Split Pro Rig / Loop Deck engine architecture

- **SYMPTOM:** Pro Rig and Loop Deck behaved as separate applications with separate timing/audio ownership, causing repeated divergence between performance controls and looping capability.
- **EXPECTED:** One workstation should have one authoritative transport and one audio engine with multiple UI surfaces.
- **CURRENT AUTHORITY:** `Karmicmurphy/Ollie_Twis_Holo_workshop` / `main` / `f39db751c41cfe9d909fa50efe5d19afa73b3d5d`.
- **LAYER:** APPLICATION / CONTRACT / ARCHITECTURE
- **FALSE LEADS:** More Pro Rig UI work, more Tone.js patching, separate Loop Deck and Pro Rig deployments.
- **ROOT CAUSE:** The product evolved as two independently functioning prototypes instead of one shared musical core.
- **FIX:** Introduce `twis-loop-core.js`, make Loop Deck V2 own the shared AudioContext-backed transport, convert Pro Rig into `loop-deck.html?mode=pro`, and route scenes/live FX through the same engine.
- **REGRESSION / PREVENTION:** Contract tests assert Pro Rig no longer loads the legacy Tone runtime and both surfaces depend on the shared Loop Core.
- **REAL-WORLD PROOF:** PROVEN_LIVE_BROWSER: merged main CI passes and deployed automation run `c000d5c8-bdaa-4e03-b68d-078c05d062a9` exercised the unified Pro Rig and advanced Loop workstation successfully.
- **PREVENTION ARTIFACT:** Shared Loop Core, deterministic Loop Core tests, unified browser proof, ADR bundle.
- **BONUS SALVAGE:** Existing OPFS, recorder worklet, sound rack, Simple Perform UI, Pro Rig scene/FX semantics, and advanced loop workstation were preserved instead of rewritten.
- **VERDICT:** DONE
- **STOP:** One-engine architecture is live and regression-protected.


### INCIDENT
Advanced mode opened a hidden non-existent page

- **SYMPTOM:** Unified browser proof timed out because clicking ADVANCED left `#ldLoops` hidden.
- **EXPECTED:** ADVANCED should reveal the real advanced loop workstation.
- **CURRENT AUTHORITY:** PR #14 branch before merge.
- **LAYER:** APPLICATION / TEST-CI
- **FALSE LEADS:** Audio engine, loop rows, Playwright visibility behavior.
- **ROOT CAUSE:** `advanced()` activated a non-existent `perform` page instead of the actual `loop` page.
- **FIX:** Route ADVANCED to `data-page="loop"` and its matching tab.
- **REGRESSION / PREVENTION:** Unified browser proof explicitly requires ADVANCED to reveal eight loop rows, record controls, and import control.
- **REAL-WORLD PROOF:** PROVEN_LIVE_BROWSER on deployed main; advanced workstation opened correctly in automation run `c000d5c8-bdaa-4e03-b68d-078c05d062a9`.
- **PREVENTION ARTIFACT:** Browser regression in `tests/pro_rig_browser_smoke.mjs`.
- **BONUS SALVAGE:** Existing advanced Loop Deck page required no rewrite.
- **VERDICT:** DONE
- **STOP:** Deployed proof passed.
