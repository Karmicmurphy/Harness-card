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
