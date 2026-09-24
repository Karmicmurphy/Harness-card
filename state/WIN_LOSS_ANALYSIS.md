# Win / Loss Analysis

> AUTO-GENERATED. Do not hand-edit.

- Incidents: **12**
- Wins: **6**
- Losses: **0**
- Blocked/open: **6**
- User-facing failure cycles: **6**
- Weird salvage items: **2**

## 1. Loop Deck looked done but phone showed old UI

- **Outcome:** DONE
- **What went wrong:** The user opened the published Loop Deck on Android and saw the legacy START HERE screen instead of the newly implemented simple PERFORM screen.
- **Why it failed:** Two independent causes: the legacy guide forcibly reopened itself after the simple shell, then the prior service worker continued serving cached application assets.
- **What changed:** Remove guide auto-open; bump asset/cache versions; make script/style/worker fetches network-first with cache fallback.
- **Why the corrected path won:** USER_REPORTED_CURRENT success. User explicitly closed the Loop Deck run as a win after using the current live link.
- **Permanent lesson:** Runtime landing-screen proof is required for UI changes; static file/string tests are insufficient.

## 2. Harness Card preserved repo state but failed to prevent false completion

- **Outcome:** DONE
- **What went wrong:** Repo state and CI were recorded correctly enough to resume work, but the assistant still claimed the UI was effectively ready before the rendered user path was proven.
- **Why it failed:** Harness Card is a repo-based operating protocol, not an automatically executing runtime guard; its proof rules were applied too weakly and its active project SHA became stale after follow-up patches.
- **What changed:** Treat rendered user path as final authority for UI work; update active authority after every material patch; record deploy target and current evidence honestly.
- **Why the corrected path won:** USER_REPORTED_CURRENT success of the final Loop Deck path, followed by explicit request to treat the run as a win and make the harness learn from it.
- **Permanent lesson:** UI DONE rule: repo changed -> deploy complete -> live target loaded -> expected screen verified -> user path exercised -> only then PROVEN_LIVE.

## 3. Loop Deck failure-cycle closeout

- **Outcome:** DONE
- **What went wrong:** Multiple iterations were needed before the user accepted the live Loop Deck as usable.
- **Why it failed:** Completion was promoted from proxy evidence too early; legacy startup behavior, cache persistence, and insufficient runtime proof were not treated as first-class release risks.
- **What changed:** Remove legacy override, repair cache/update behavior, redeploy, then let the user exercise the live path.
- **Why the corrected path won:** USER_REPORTED_CURRENT: user explicitly said to chalk the result up as a win.
- **Permanent lesson:** UI hard gate, rendered-authority rule, failure-count rule, sibling-failure audit after first live failure, and self-improvement loop.

## 4. Pro Rig autoplay wash and dead controls

- **Outcome:** BLOCKED
- **What went wrong:** On Android the page produced an immediate wash/noise texture, while PLAY and other controls appeared to do nothing useful.
- **Why it failed:** Tone/WebAudio graph and continuous atmosphere sources were created and started at script evaluation time instead of behind a user gesture; the control model also lacked strong one-control-one-audible-job behavior.
- **What changed:** Lazy-create the entire audio graph on first interaction, silence startup, make deck buttons control stem groups, make scenes/stems/macros auto-start safely, and preserve the wash as an intentional ocean atmosphere stem.
- **Why the corrected path won:** PENDING user retest after deploy.
- **Permanent lesson:** Mobile WebAudio prototypes must start silent, initialize inside a user gesture, and every primary control must produce an observable state change plus an audible job.

## 5. Android treated as compatibility instead of architecture

- **Outcome:** BLOCKED
- **What went wrong:** A phone-first audio prototype was built before Android/WebAudio interaction constraints were verified, causing autoplay-style behavior and non-obvious control response on the actual device.
- **Why it failed:** The implementation started from desired features and desktop-like assumptions instead of first proving the target environment and the human interaction path.
- **What changed:** Add mandatory Environment + Human Interaction Preflight, assumption stop rule, interaction contract, and acceptance tests.
- **Why the corrected path won:** PENDING future project where the harness performs preflight before first build and avoids this failure class.
- **Permanent lesson:** Known device/runtime constraints are architecture. No material platform assumption may pass silently into implementation.

## 6. Controls work but the music still sounds like a browser synth experiment

- **Outcome:** BLOCKED
- **What went wrong:** Android screen recording shows the Pro Rig controls responding and state changing, but the audible result still does not resemble a professional amphitheater DJ performance. The user correctly described it as a browser synth experiment rather than a finished musical instrument.
- **Why it failed:** We repeatedly translated "sound like a professional amphitheater DJ set" into interface features and browser-synth mechanisms without first creating a sonic acceptance contract or sourcing/proving professional-grade musical content. We optimized interaction before sound quality.
- **What changed:** Freeze UI growth. Define a sonic reference contract first: genre/energy target, drum quality, bass movement, harmonic language, melody behavior, vocal role, transitions, dynamics, loudness, stereo space, and what a 30-second successful performance must sound like. Then Artifact Compass/Salvage real open/permissive musical engines, samples, stems, effects, and arrangement mechanisms against that contract before implementation.
- **Why the corrected path won:** USER_REPORTED_CURRENT: interaction works on Android, but sonic quality target is not met. This is direct target-device evidence.
- **Permanent lesson:** For music products, "controls work" is interaction proof only. No music build may be promoted until an audible reference-path test passes. Build musical content/arrangement/mix first, then expose controls. Require a SONIC_ACCEPTANCE.md before implementation.

## 7. Pro Rig prototype was treated as product progress before sonic proof

- **Outcome:** BLOCKED
- **What went wrong:** Multiple Pro Rig iterations added professional-looking controls and technically valid audio behavior while the user still heard toy/browser-synth output.
- **Why it failed:** Product intent was repeatedly translated into implementation nouns instead of the user's actual outcome: perform convincing finished-sounding music without needing producer knowledge.
- **What changed:** Create and enforce a sonic acceptance contract; require a blind 30-second musical pass before UI growth or professional-sound claims.
- **Why the corrected path won:** USER_REPORTED_CURRENT: prior versions failed the sonic target despite working controls.
- **Permanent lesson:** For creative tools, define the perceptual/output acceptance test before selecting implementation mechanisms.

## 8. Pro Rig V4 first CI pass hit stale V3 contract

- **Outcome:** DONE
- **What went wrong:** V4 JavaScript syntax and remote sample reachability passed, but Python contract collection failed because an older test still required the V3 script name.
- **Why it failed:** The implementation replaced the V3 entry script without updating the old V3-specific contract before the first CI run.
- **What changed:** Update the historical Amphitheater contract to assert V4 wiring and current engine behavior.
- **Why the corrected path won:** PROVEN_IN_TEST: corrected V4 SHA `34c486f5e5a7b8dc3033568972063e5e64925b09` passed Workshop CI and Static Contract; merged main SHA `d5527703b348b65956ea4ac8a1792cc02326480f` also passed Workshop CI, Static Contract, remote sample reachability, and static build.
- **Permanent lesson:** Version replacement checklist must inspect tests that pin old entrypoints before first push/merge.

## 9. Cross-device claim outran PC proof

- **Outcome:** BLOCKED
- **What went wrong:** The project goal expanded to "same rig on phone and PC," but only Android interaction had direct user proof.
- **Why it failed:** Shared web technology was treated as implied cross-device proof rather than an implementation strategy requiring separate runtime verification.
- **What changed:** Same code path plus desktop and Android live-path proof; add runtime diagnostics and fallback audio assets.
- **Why the corrected path won:** PENDING.
- **Permanent lesson:** Any "works on phone and PC" claim requires separate target-device evidence records.

## 10. Harness scorecard stale during first Chat Software Harness field trial

- **Outcome:** BLOCKED
- **What went wrong:** `state/HARNESS_SCORECARD.json` still reported TWIS LOOP DECK at old SHA `134540fc0abf6d64a82111eb5564dd604b57b2b3`, zero incidents, zero wins, and zero losses while the Incident Ledger and current authority already contained active TWIS Pro Rig V4 work and multiple incidents.
- **Why it failed:** UNKNOWN; either the self-improvement generator has not rerun after current changes or its parser/generation path is not ingesting the current ledger/state correctly.
- **What changed:** Treat the scorecard as stale derived data until its generation path is rerun and verified against CURRENT_PROJECT + INCIDENT_LEDGER.
- **Why the corrected path won:** PENDING scorecard regeneration/verification.
- **Permanent lesson:** A field-trial closeout must compare generated scorecard authority/counts against canonical state before trusting the scorecard.

## 11. Split Pro Rig / Loop Deck engine architecture

- **Outcome:** DONE
- **What went wrong:** Pro Rig and Loop Deck behaved as separate applications with separate timing/audio ownership, causing repeated divergence between performance controls and looping capability.
- **Why it failed:** The product evolved as two independently functioning prototypes instead of one shared musical core.
- **What changed:** Introduce `twis-loop-core.js`, make Loop Deck V2 own the shared AudioContext-backed transport, convert Pro Rig into `loop-deck.html?mode=pro`, and route scenes/live FX through the same engine.
- **Why the corrected path won:** PROVEN_LIVE_BROWSER: merged main CI passes and deployed automation run `c000d5c8-bdaa-4e03-b68d-078c05d062a9` exercised the unified Pro Rig and advanced Loop workstation successfully.
- **Permanent lesson:** Contract tests assert Pro Rig no longer loads the legacy Tone runtime and both surfaces depend on the shared Loop Core.

## 12. Advanced mode opened a hidden non-existent page

- **Outcome:** DONE
- **What went wrong:** Unified browser proof timed out because clicking ADVANCED left `#ldLoops` hidden.
- **Why it failed:** `advanced()` activated a non-existent `perform` page instead of the actual `loop` page.
- **What changed:** Route ADVANCED to `data-page="loop"` and its matching tab.
- **Why the corrected path won:** PROVEN_LIVE_BROWSER on deployed main; advanced workstation opened correctly in automation run `c000d5c8-bdaa-4e03-b68d-078c05d062a9`.
- **Permanent lesson:** Unified browser proof explicitly requires ADVANCED to reveal eight loop rows, record controls, and import control.
