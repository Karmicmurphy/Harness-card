# Auto-Generated Learned Rules

> MACHINE-WRITTEN from the Incident Ledger. Preventive advice from unresolved incidents is kept but never represented as a verified fix.

## Closed-incident learned rules

An incident marked DONE contributed the following prevention rules. Its recorded proof applies only to the stated scope; this does not imply every downstream app is working.

### LR-001 — Loop Deck looked done but phone showed old UI
- **Incident closure:** DONE
- **Root cause learned:** Two independent causes: the legacy guide forcibly reopened itself after the simple shell, then the prior service worker continued serving cached application assets.
- **Rule:** Runtime landing-screen proof is required for UI changes; static file/string tests are insufficient.
- **Evidence:** USER_REPORTED_CURRENT success. User explicitly closed the Loop Deck run as a win after using the current live link.

### LR-002 — Harness Card preserved repo state but failed to prevent false completion
- **Incident closure:** DONE
- **Root cause learned:** Harness Card is a repo-based operating protocol, not an automatically executing runtime guard; its proof rules were applied too weakly and its active project SHA became stale after follow-up patches.
- **Rule:** UI DONE rule: repo changed -> deploy complete -> live target loaded -> expected screen verified -> user path exercised -> only then PROVEN_LIVE.
- **Evidence:** USER_REPORTED_CURRENT success of the final Loop Deck path, followed by explicit request to treat the run as a win and make the harness learn from it.

### LR-003 — Loop Deck failure-cycle closeout
- **Incident closure:** DONE
- **Root cause learned:** Completion was promoted from proxy evidence too early; legacy startup behavior, cache persistence, and insufficient runtime proof were not treated as first-class release risks.
- **Rule:** UI hard gate, rendered-authority rule, failure-count rule, sibling-failure audit after first live failure, and self-improvement loop.
- **Evidence:** USER_REPORTED_CURRENT: user explicitly said to chalk the result up as a win.

### LR-008 — Pro Rig V4 first CI pass hit stale V3 contract
- **Incident closure:** DONE
- **Root cause learned:** The implementation replaced the V3 entry script without updating the old V3-specific contract before the first CI run.
- **Rule:** Version replacement checklist must inspect tests that pin old entrypoints before first push/merge.
- **Evidence:** PROVEN_IN_TEST: corrected V4 SHA `34c486f5e5a7b8dc3033568972063e5e64925b09` passed Workshop CI and Static Contract; merged main SHA `d5527703b348b65956ea4ac8a1792cc02326480f` also passed Workshop CI, Static Contract, remote sample reachability, and static build.

### LR-010 — Harness scorecard stale during first Chat Software Harness field trial
- **Incident closure:** DONE
- **Root cause learned:** The self-improvement worker used double-escaped Markdown regexes, so it parsed zero incidents from a populated ledger; the workflow validated headings rather than semantic counts, allowing the empty result to be recorded as a WIN.
- **Rule:** A field-trial closeout must compare generated scorecard authority/counts against canonical state before trusting the scorecard.
- **Evidence:** PROVEN_ON_MAIN 2026-09-24: repaired self-improvement run regenerated 12 incidents, 12 learned rules, 6 user-facing failure cycles, and current Foundry/Workshop authority in `state/HARNESS_SCORECARD.json`.

### LR-011 — Split Pro Rig / Loop Deck engine architecture
- **Incident closure:** DONE
- **Root cause learned:** The product evolved as two independently functioning prototypes instead of one shared musical core.
- **Rule:** Contract tests assert Pro Rig no longer loads the legacy Tone runtime and both surfaces depend on the shared Loop Core.
- **Evidence:** PROVEN_LIVE_BROWSER: merged main CI passes and deployed automation run `c000d5c8-bdaa-4e03-b68d-078c05d062a9` exercised the unified Pro Rig and advanced Loop workstation successfully.

### LR-012 — Advanced mode opened a hidden non-existent page
- **Incident closure:** DONE
- **Root cause learned:** `advanced()` activated a non-existent `perform` page instead of the actual `loop` page.
- **Rule:** Unified browser proof explicitly requires ADVANCED to reveal eight loop rows, record controls, and import control.
- **Evidence:** PROVEN_LIVE_BROWSER on deployed main; advanced workstation opened correctly in automation run `c000d5c8-bdaa-4e03-b68d-078c05d062a9`.


## Provisional prevention rules — original incident still unresolved

These are protective hypotheses/checks from BLOCKED, FAILED, OPEN or RETIRED incidents. Use them to prevent harm, but do not claim the incident was fixed, the rule proven, or the target device validated.

### LR-004 — Pro Rig autoplay wash and dead controls
- **Incident closure:** BLOCKED — NOT VERIFIED AS FIXED
- **Root cause learned:** Tone/WebAudio graph and continuous atmosphere sources were created and started at script evaluation time instead of behind a user gesture; the control model also lacked strong one-control-one-audible-job behavior.
- **Provisional prevention:** Mobile WebAudio prototypes must start silent, initialize inside a user gesture, and every primary control must produce an observable state change plus an audible job.
- **Evidence:** PENDING user retest after deploy.

### LR-005 — Android treated as compatibility instead of architecture
- **Incident closure:** BLOCKED — NOT VERIFIED AS FIXED
- **Root cause learned:** The implementation started from desired features and desktop-like assumptions instead of first proving the target environment and the human interaction path.
- **Provisional prevention:** Known device/runtime constraints are architecture. No material platform assumption may pass silently into implementation.
- **Evidence:** PENDING future project where the harness performs preflight before first build and avoids this failure class.

### LR-006 — Controls work but the music still sounds like a browser synth experiment
- **Incident closure:** BLOCKED — NOT VERIFIED AS FIXED
- **Root cause learned:** We repeatedly translated "sound like a professional amphitheater DJ set" into interface features and browser-synth mechanisms without first creating a sonic acceptance contract or sourcing/proving professional-grade musical content. We optimized interaction before sound quality.
- **Provisional prevention:** For music products, "controls work" is interaction proof only. No music build may be promoted until an audible reference-path test passes. Build musical content/arrangement/mix first, then expose controls. Require a SONIC_ACCEPTANCE.md before implementation.
- **Evidence:** USER_REPORTED_CURRENT: interaction works on Android, but sonic quality target is not met. This is direct target-device evidence.

### LR-007 — Pro Rig prototype was treated as product progress before sonic proof
- **Incident closure:** BLOCKED — NOT VERIFIED AS FIXED
- **Root cause learned:** Product intent was repeatedly translated into implementation nouns instead of the user's actual outcome: perform convincing finished-sounding music without needing producer knowledge.
- **Provisional prevention:** For creative tools, define the perceptual/output acceptance test before selecting implementation mechanisms.
- **Evidence:** USER_REPORTED_CURRENT: prior versions failed the sonic target despite working controls.

### LR-009 — Cross-device claim outran PC proof
- **Incident closure:** BLOCKED — NOT VERIFIED AS FIXED
- **Root cause learned:** Shared web technology was treated as implied cross-device proof rather than an implementation strategy requiring separate runtime verification.
- **Provisional prevention:** Any "works on phone and PC" claim requires separate target-device evidence records.
- **Evidence:** PENDING.

### LR-013 — Foundation restart files disagreed and sent work back to completed stages
- **Incident closure:** BLOCKED — NOT VERIFIED AS FIXED
- **Root cause learned:** Independent editable status copies; Markdown guard verified only headings; no branch observation job; unrelated inventory and runtime finish lines were coupled.
- **Provisional prevention:** Stale work-order prose and build prompts fail the same guard as stale JSON. Access failures remain UNKNOWN. Branch advancement never silently replaces approved pins.
- **Evidence:** Local regression and guard proof only; corrected instructions not yet field-proven in a later session. Whole phone path remains unproven.

### LR-014 — COILSIDE field app recovery — public Access, cloud D1 and two-person owner intent
- **Incident closure:** OPEN — NOT VERIFIED AS FIXED
- **Root cause learned:** Shared Access include/action mismatch, provider-tool capability mismatch, and expansion away from owner-locked no-sign-in/two-person outcome. Some user-visible retries arose from speculative mobile guidance.
- **Provisional prevention:** Target Android and owner-language translation; provider-action fallback; policy shared-reach inspection; separate work-pay category from account; source/CI/deploy/runtime/binding/user-path ladder; backup before touching local data.
- **Evidence:** **INFRASTRUCTURE WIN VERIFIED:** public home, dedicated D1 with three tables, `COILSIDE_DB` live binding and deployment, PR #5 and PR #6 merged. **NOT YET USER-PATH PROVEN:** owner ↔ Sean cross-phone notes, edited/reloaded Android timecards and restore.

### LR-015 — Scheduled Foundation monitor reported expected access gaps as nightly workflow crashes
- **Incident closure:** BLOCKED — NOT VERIFIED AS FIXED
- **Root cause learned:** The scheduled observation scripts intentionally returned exit 1 for UNKNOWN / RECONCILIATION_REQUIRED / CONFIG_BLOCKED, and the workflow escalated those *findings* into failing jobs. GitHub Actions' repo-scoped token cannot resolve two private components; Cloudflare read-only env inputs are absent. These genuine monitoring access limitations do not establish a core runtime crash.
- **Provisional prevention:** Distinguish observation failure *states* from observer *execution* failure. A green observation job certifies the reporting machinery only. Missing/malformed reports must still fail CI; never make UNKNOWN look like reconciled/live.
- **Evidence:** PROVEN_IN_GITHUB_PR_CI: Authority Spine Guard 39862496405 and read-only observer 39862496340 both passed, and the observer preserved real UNKNOWN/drift facts. First post-merge scheduled run remains PENDING; no Android/general FRIDAY runtime proof.


## Repeated-layer escalations

- **APPLICATION repeated 10 times:** inspect sibling failure modes before another release touching this layer.
- **DEPLOY repeated 2 times:** inspect sibling failure modes before another release touching this layer.
- **TEST-CI repeated 7 times:** inspect sibling failure modes before another release touching this layer.
- **CONTRACT repeated 12 times:** inspect sibling failure modes before another release touching this layer.
- **AUTHORITY repeated 3 times:** inspect sibling failure modes before another release touching this layer.
- **MOBILE AUDIO repeated 2 times:** inspect sibling failure modes before another release touching this layer.
- **CREATIVE repeated 2 times:** inspect sibling failure modes before another release touching this layer.
- **PROVIDER ACCESS repeated 2 times:** inspect sibling failure modes before another release touching this layer.

## FRIDAY operator retry evidence — sanitized scheduled CI only

- Observed independent CI run identities: 1
- Verified bounded repairs: 0
- Recovered local I/O retry sequences: 0
- Failed repairs awaiting review: 0
- **PROVISIONAL:** Do not call status repair repeatable until two distinct CI runs independently verify it.

## Non-negotiable promotion rule

Generated rules may strengthen proof and quality requirements. They may not remove privacy/safety boundaries, erase incident history, silently change the user's locked outcome, or promote proxy evidence to PROVEN_LIVE.

<!-- FRIDAY_LEARNING_CANDIDATES_START -->

## Proven generalized learning candidates

- No proven generalized learning candidates yet.
<!-- FRIDAY_LEARNING_CANDIDATES_END -->
