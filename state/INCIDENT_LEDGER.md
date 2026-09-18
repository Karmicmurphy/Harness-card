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
- **REAL-WORLD PROOF:** PENDING. User has not yet shown the corrected simple PERFORM surface on the target Android phone after cache-fix deployment.
- **PREVENTION ARTIFACT:** Regression test blocking the known guide auto-open plus this incident record.
- **BONUS SALVAGE:** GitHub Pages alone is sufficient for the Loop Deck; Cloudflare is not required for this test path.
- **VERDICT:** BLOCKED
- **STOP:** Stop promotion to PROVEN_LIVE until a phone screenshot/interaction proves the corrected landing surface.

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
- **REAL-WORLD PROOF:** PENDING.
- **PREVENTION ARTIFACT:** Incident ledger entry and corrected active work order.
- **BONUS SALVAGE:** Harness Card remains useful for continuity, but it must never be represented as an autonomous plugin or automatic enforcement layer.
- **VERDICT:** BLOCKED
- **STOP:** Stop calling the harness successful for UI proof until it enforces/records the live-render gate.
