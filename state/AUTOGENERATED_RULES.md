# Auto-Generated Learned Rules

> MACHINE-WRITTEN from the Incident Ledger.

## Active learned rules

### LR-001 — Loop Deck looked done but phone showed old UI
- **Root cause learned:** Two independent causes: the legacy guide forcibly reopened itself after the simple shell, then the prior service worker continued serving cached application assets.
- **Rule:** Runtime landing-screen proof is required for UI changes; static file/string tests are insufficient.
- **Evidence:** USER_REPORTED_CURRENT success. User explicitly closed the Loop Deck run as a win after using the current live link.

### LR-002 — Harness Card preserved repo state but failed to prevent false completion
- **Root cause learned:** Harness Card is a repo-based operating protocol, not an automatically executing runtime guard; its proof rules were applied too weakly and its active project SHA became stale after follow-up patches.
- **Rule:** UI DONE rule: repo changed -> deploy complete -> live target loaded -> expected screen verified -> user path exercised -> only then PROVEN_LIVE.
- **Evidence:** USER_REPORTED_CURRENT success of the final Loop Deck path, followed by explicit request to treat the run as a win and make the harness learn from it.

### LR-003 — Loop Deck failure-cycle closeout
- **Root cause learned:** Completion was promoted from proxy evidence too early; legacy startup behavior, cache persistence, and insufficient runtime proof were not treated as first-class release risks.
- **Rule:** UI hard gate, rendered-authority rule, failure-count rule, sibling-failure audit after first live failure, and self-improvement loop.
- **Evidence:** USER_REPORTED_CURRENT: user explicitly said to chalk the result up as a win.

### LR-004 — Pro Rig autoplay wash and dead controls
- **Root cause learned:** Tone/WebAudio graph and continuous atmosphere sources were created and started at script evaluation time instead of behind a user gesture; the control model also lacked strong one-control-one-audible-job behavior.
- **Rule:** Mobile WebAudio prototypes must start silent, initialize inside a user gesture, and every primary control must produce an observable state change plus an audible job.
- **Evidence:** PENDING user retest after deploy.

### LR-005 — Android treated as compatibility instead of architecture
- **Root cause learned:** The implementation started from desired features and desktop-like assumptions instead of first proving the target environment and the human interaction path.
- **Rule:** Known device/runtime constraints are architecture. No material platform assumption may pass silently into implementation.
- **Evidence:** PENDING future project where the harness performs preflight before first build and avoids this failure class.

### LR-006 — Controls work but the music still sounds like a browser synth experiment
- **Root cause learned:** We repeatedly translated "sound like a professional amphitheater DJ set" into interface features and browser-synth mechanisms without first creating a sonic acceptance contract or sourcing/proving professional-grade musical content. We optimized interaction before sound quality.
- **Rule:** For music products, "controls work" is interaction proof only. No music build may be promoted until an audible reference-path test passes. Build musical content/arrangement/mix first, then expose controls. Require a SONIC_ACCEPTANCE.md before implementation.
- **Evidence:** USER_REPORTED_CURRENT: interaction works on Android, but sonic quality target is not met. This is direct target-device evidence.

### LR-007 — Pro Rig prototype was treated as product progress before sonic proof
- **Root cause learned:** Product intent was repeatedly translated into implementation nouns instead of the user's actual outcome: perform convincing finished-sounding music without needing producer knowledge.
- **Rule:** For creative tools, define the perceptual/output acceptance test before selecting implementation mechanisms.
- **Evidence:** USER_REPORTED_CURRENT: prior versions failed the sonic target despite working controls.

### LR-008 — Pro Rig V4 first CI pass hit stale V3 contract
- **Root cause learned:** The implementation replaced the V3 entry script without updating the old V3-specific contract before the first CI run.
- **Rule:** Version replacement checklist must inspect tests that pin old entrypoints before first push/merge.
- **Evidence:** PROVEN_IN_TEST: corrected V4 SHA `34c486f5e5a7b8dc3033568972063e5e64925b09` passed Workshop CI and Static Contract; merged main SHA `d5527703b348b65956ea4ac8a1792cc02326480f` also passed Workshop CI, Static Contract, remote sample reachability, and static build.

### LR-009 — Cross-device claim outran PC proof
- **Root cause learned:** Shared web technology was treated as implied cross-device proof rather than an implementation strategy requiring separate runtime verification.
- **Rule:** Any "works on phone and PC" claim requires separate target-device evidence records.
- **Evidence:** PENDING.

### LR-010 — Harness scorecard stale during first Chat Software Harness field trial
- **Root cause learned:** UNKNOWN; either the self-improvement generator has not rerun after current changes or its parser/generation path is not ingesting the current ledger/state correctly.
- **Rule:** A field-trial closeout must compare generated scorecard authority/counts against canonical state before trusting the scorecard.
- **Evidence:** PENDING scorecard regeneration/verification.

### LR-011 — Split Pro Rig / Loop Deck engine architecture
- **Root cause learned:** The product evolved as two independently functioning prototypes instead of one shared musical core.
- **Rule:** Contract tests assert Pro Rig no longer loads the legacy Tone runtime and both surfaces depend on the shared Loop Core.
- **Evidence:** PROVEN_LIVE_BROWSER: merged main CI passes and deployed automation run `c000d5c8-bdaa-4e03-b68d-078c05d062a9` exercised the unified Pro Rig and advanced Loop workstation successfully.

### LR-012 — Advanced mode opened a hidden non-existent page
- **Root cause learned:** `advanced()` activated a non-existent `perform` page instead of the actual `loop` page.
- **Rule:** Unified browser proof explicitly requires ADVANCED to reveal eight loop rows, record controls, and import control.
- **Evidence:** PROVEN_LIVE_BROWSER on deployed main; advanced workstation opened correctly in automation run `c000d5c8-bdaa-4e03-b68d-078c05d062a9`.


## Repeated-layer escalations

- **APPLICATION repeated 9 times:** inspect sibling failure modes before another release touching this layer.
- **DEPLOY repeated 2 times:** inspect sibling failure modes before another release touching this layer.
- **TEST-CI repeated 6 times:** inspect sibling failure modes before another release touching this layer.
- **CONTRACT repeated 10 times:** inspect sibling failure modes before another release touching this layer.
- **AUTHORITY repeated 2 times:** inspect sibling failure modes before another release touching this layer.
- **MOBILE AUDIO repeated 2 times:** inspect sibling failure modes before another release touching this layer.
- **CREATIVE repeated 2 times:** inspect sibling failure modes before another release touching this layer.

## Non-negotiable promotion rule

Generated rules may strengthen proof and quality requirements. They may not remove privacy/safety boundaries, erase incident history, silently change the user's locked outcome, or promote proxy evidence to PROVEN_LIVE.
