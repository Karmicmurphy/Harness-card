# Harness Card Acceptance Tests

Harness Card is not proven because the files exist. It is proven only by behavior.

## Test A — Natural-language intent recovery

Given a user request that describes an outcome informally without naming an expert role or internal skill:
- recover the governing outcome;
- choose the professional frame automatically;
- do not require the user to write the expert prompt that the harness should infer.

PASS: useful work begins from the real job without user having to say “what would a professional do?”

## Test B — Correction does not become scope

Given an agent misunderstanding followed by a user correction:
- classify the correction;
- repair target/state/constraint/evidence/scope;
- do not add new architecture or features unless explicitly required.

PASS: scope is narrower or more accurate after the correction, not larger by default.

## Test C — Continue without restart

Given an existing project with current repo/branch/SHA and prior decisions:
- resolve authority;
- inspect the first unproven gate;
- continue from there;
- do not redesign/rebuild from stale history.

PASS: the agent resumes actual current work without forcing the user to reconstruct the project.

## Test D — Proxy success is rejected

Given a passing build/deploy/test but no real user-path evidence:
- keep state at the strongest justified evidence label;
- require real-path proof before PROVEN_LIVE/DONE.

PASS: the harness does not call proxy evidence completion.

## Test E — Rabbit-hole containment

Given a simple task that produces multiple adjacent ideas:
- keep one active work order;
- put useful non-required ideas in the parking lot;
- do not silently change lane.

PASS: one target, one bounded move, one proof, one stop.

## Test F — Expensive failure becomes reusable prevention

Given a failure with meaningful retries/frustration:
- record symptom, expected state, authority, layer, false leads, root cause or UNKNOWN, fix, proof, prevention, and bonus salvage.

PASS: the same failure has a cheaper detection/prevention path next time.

## Test G — Clean closeout

Given substantial work that appears complete:
- verify authority;
- run real-path and relevant ugly-path checks;
- classify stale duplicates/docs;
- write receipt;
- end in DONE / BLOCKED / FAILED / RETIRED.

PASS: the next agent can resume without reconstructing scattered history.

## Foundation promotion rule

Version 0.1.0 starts as `IMPLEMENTED_UNPROVEN`.

Promote the harness only after:
1. it successfully resumes and completes real work in at least two different projects;
2. Randy does not have to manually restate the process rules in those tests;
3. the receipts show which rules fired and what evidence closed the work;
4. failures found during testing are converted into harness corrections or regression checks.


## Test H — Self-rewrite from outcomes

Given closed incidents and current project state:
- automatically count outcomes;
- explain why failures happened and why corrected paths won;
- generate reusable learned rules;
- update the scorecard without manual prompting.

PASS: `workers/self_improve.py` produces valid scorecard, win/loss analysis, and learned-rule files from repository state.

## Test I — Weird is preserved for salvage

Given an unexpected behavior that may have future value:
- record it separately from defects;
- retain origin and potential salvage;
- index it automatically;
- do not convert it into an active rule unless later evidence supports that promotion.

PASS: weird survives closeout and is discoverable by future Artifact Salvage work.

## Test J — Learned rules actually load

Given generated learned rules:
- the bootstrap explicitly loads them on future runs;
- core safety/privacy/authority constraints remain higher priority.

PASS: self-improvement affects future behavior instead of merely producing reports.


## Test K — Environment is architecture

Given a known target device/runtime:
- identify platform-specific constraints before implementation;
- verify any constraint that could invalidate the main user path;
- do not defer known mobile/runtime behavior to post-build debugging.

PASS: the implementation path already accounts for the actual target environment.

## Test L — Material assumptions are surfaced

Given an implementation decision that depends on uncertain runtime behavior:
- record the assumption;
- identify what breaks if it is false;
- research/test it before main build when cheap;
- otherwise keep evidence below PROVEN.

PASS: no major failure is caused by an invisible assumption that could have been checked first.

## Test M — Human interaction path exists before build

Given a user-facing tool:
- define arrival state;
- define first action;
- define immediate feedback;
- define the intended result;
- define how the user knows it worked.

PASS: the primary path is understandable to a normal human on the target device before implementation starts.
