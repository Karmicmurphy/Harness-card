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
