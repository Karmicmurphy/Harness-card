# FRIDAY Automation Spine

Status: CANDIDATE / ISOLATED  
Target: make the existing Foundation/Harness machine operable as one automated system before adding more product capability.

## Owner outcome

Randy should not have to remember repository roles, compare SHAs, translate normal speech into engineering prompts, manually run repeated checks, or reconstruct what FRIDAY learned.

The normal owner view should answer four questions:

1. What is working?
2. What is blocked?
3. What is FRIDAY doing automatically?
4. What, if anything, genuinely needs Randy?

## Control loop

`RECOVER -> VALIDATE -> OBSERVE -> CLASSIFY -> AUTOMATE -> TEST -> PROVE -> LEARN -> RENDER -> STOP/CONTINUE`

### Recover
Load canonical Harness authority, current work order, generated learned rules, skill registry, and automation policy.

### Validate
Fail closed when authority, projections, policy, or learning inputs are malformed or stale.

### Observe
Read approved remote refs without promoting branch movement. Unknown access remains UNKNOWN.

### Classify
Separate blockers into:
- automatic bounded work;
- owner-gated work.

### Automate
FRIDAY may automatically perform policy-approved deterministic/reversible work, tests, candidate comparisons, isolated candidate preparation, status refresh, and learning-index maintenance.

### Test / prove
Candidate implementation is not capability. Tests do not become live proof. Existing Harness evidence states remain authoritative.

### Learn
The existing self-improvement worker continues to learn from incidents and weird salvage. `workers/learning_intake.py` adds a sanitized generalized candidate lane. Raw private chat is deliberately not copied into the public Harness.

Only learning candidates marked `PROVEN` with non-pending evidence are eligible to appear as generated operating rules.

### Render
`scripts/friday_control_plane.py` produces the owner-readable machine status from canonical state. It does not become a competing source of authority.

## Automation authority

`config/friday_automation_policy.json` is the machine-readable policy.

Default mode: `AUTOMATE_UNTIL_OWNER_GATE`.

The policy deliberately separates owner authority from owner labor. Randy should not be asked to perform machine work merely because he retains authority over sensitive decisions.

## Creative problem solving

`constraint-breaker-lab` is the routed capability for situations where the current implementation works in principle but is too slow, expensive, heavy, fragile, manual, or hardware-constrained.

It changes the question from:

`How do we optimize this implementation?`

to:

`What outcome is required, which assumptions are optional, and what cheaper mechanism can prove the same outcome?`

Its loop is:

`OUTCOME -> CONSTRAINT -> ASSUMPTIONS -> INVERT -> SEARCH -> RECOMBINE -> TEST -> ATTACK FAVORITE -> KEEP WINNER -> DOWNSHIFT`

## What this candidate does not authorize

This automation-spine candidate does not:
- promote any Foundation component SHA;
- change the current Pages/Preview authorization;
- read or restore secret values;
- dispatch the live bounded fixture;
- alter Production;
- merge itself;
- claim the machine is PROVEN_LIVE.

## Proof required before promotion

1. Pull-request checks pass.
2. Existing authority-spine and continuity checks still pass.
3. Sanitized learning intake passes and does not promote the pending constraint-inversion lesson.
4. FRIDAY control-plane status builds deterministically from current canonical state.
5. The generated owner view correctly identifies current owner-gated blockers without mutating Foundation authority.
6. No protected current work is changed.

## After promotion

Once this spine is proven and merged, the next architectural work should attach existing Foundry candidate-building/testing mechanisms behind this policy rather than inventing another front door.

The automation spine becomes the control layer; existing repos keep their specialized roles.
