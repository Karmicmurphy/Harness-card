# Active Work Order

## TARGET
Close the TWIS LOOP DECK release run and convert its failures into reusable Harness Card behavior.

## CURRENT TRUTH
- USER_REPORTED_CURRENT: The live Loop Deck is accepted by the user as a win.
- VERIFIED_CURRENT: GitHub Pages is the deploy path used for this release.
- VERIFIED_CURRENT: Harness Card now contains a self-improvement loop, rendered-authority rule, UI/app hard gate, and failure-count rule.
- VERIFIED_CURRENT: Three user-facing failure cycles occurred before acceptance, plus one internal CI-caught implementation failure.

## DO NOT
- Do not reopen Loop Deck feature work inside this closeout.
- Do not call remaining feature-quality issues part of this completed release unless the user creates a new work order.
- Do not reduce the lessons back to chat-only memory.

## LANE
CLOSEOUT

## PROFESSIONAL FRAME
Release retrospective + reliability engineering.

## ONE MOVE
Record the failure count, root causes, successful corrections, and permanent harness changes.

## PROOF
Harness Card files contain the generalized rules and incident closeout, and current project state records the user-reported live win.

## STOP
DONE when the retrospective and durable harness updates are committed.

## PARKING LOT
Ghost first-use hardening, stricter bar-boundary toggles, deeper session persistence, harmonic pack refinement, PWA identity cleanup, and other Loop Deck feature improvements.
