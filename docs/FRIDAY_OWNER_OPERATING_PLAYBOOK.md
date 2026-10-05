# FRIDAY Owner Operating Playbook

**Date:** 2026-10-05  
**Status:** OWNER / OPERATOR PLAYBOOK — NON-AUTHORITATIVE  
**Authority:** NONE  
**Implementation authorization:** NONE  
**Machine mutation authorization:** NONE  
**Purpose:** Help Randy operate the current Foundation / FRIDAY system without needing technical vocabulary, without losing the active goal, and without turning every useful idea into active architecture.

> This file is a human operating guide. It is subordinate to `state/CURRENT_PROJECT.json`, the active work order, Harness authority/policy, immutable approved refs, receipts, and proof. If this file conflicts with canonical Harness state, canonical Harness state wins.

---

# 1. The one-sentence operating model

> **Talk to FRIDAY / Control Room to decide what is wanted; use research only when evidence is missing; use Codex only after the work is bounded; let Harness/GitHub record what survived proof; stop when the Goal is actually satisfied.**

The owner does **not** need to know the technical name for a problem before the machine can help.

Valid owner inputs include:

- "This doesn't make fucking sense."
- "Where the fuck were we?"
- "Don't drift."
- "I think we're doing the same shit again."
- "I have an idea."
- "I want this to work from my phone."

The system's job is to translate ordinary human intent into a bounded technical task without requiring the owner to conduct the internal machinery.

---

# 2. What FRIDAY is

Current working product definition:

> **Foundation is the machinery. FRIDAY is the relationship between the owner and the machinery.**

Operational definition:

> **FRIDAY turns nonlinear human intent into continuous, bounded, verified action without losing the ideas, the evidence, the owner, or the plot.**

FRIDAY is **not**:

- a model;
- GPT itself;
- Codex;
- Workshop alone;
- Foundry alone;
- a therapist;
- a clone of Randy;
- a separate personality;
- a reason to create another architecture.

Models are replaceable workers. Authority remains outside the model.

---

# 3. Source-of-truth hierarchy

When sources disagree, use this order:

1. **Canonical Harness authority and approved immutable refs**
2. **Receipts / independent proof / directly verified live state**
3. **Current repository source at the exact relevant ref**
4. **Current bounded work-order evidence**
5. **Research and operator playbooks such as this file**
6. **Chat summaries / handoffs / remembered state**
7. **Model inference or confidence**

Rules:

- Chat is not authority.
- Work research is not authority.
- Codex output is not authority.
- A green build is not automatically live proof.
- Branch movement is not promotion.
- Memory is not verified state.
- A candidate is not Canon.

---

# 4. The five stations the owner uses

Until FRIDAY automatically routes work, use these human-visible stations.

## A. CONTROL ROOM — normal ChatGPT conversation

**Use for:**

- deciding what is actually wanted;
- recovering where work left off;
- keeping the active Goal visible;
- evaluating research;
- reviewing Codex results;
- deciding whether a branch is active or parked;
- architectural judgment before code is touched;
- translating technical language into behavior.

**Default:** use a strong general reasoning model at normal/medium effort.

**Escalate to highest available reasoning effort when:**

- deciding architecture;
- auditing the machine;
- reconciling contradictory evidence;
- determining whether an idea deserves implementation;
- reviewing a root-of-trust or authority change.

**Control Room rule:**

> Never let the current conversation replace the persistent Goal.

---

## B. RESEARCH LAB — ChatGPT Work / deep research workspace

**Use for:**

- multi-source research;
- current frontier AI research;
- comparing papers, frameworks, standards, products, or implementations;
- large file/repository surveys;
- substantial evidence packets;
- questions where current external evidence materially matters.

Use the strongest available research/reasoning model when the question is difficult enough to justify it.

**Research Lab never mutates machine authority directly.**

It returns an evidence packet to Control Room.

### Research evidence packet

```text
QUESTION
What were we trying to determine?

SUPPORTED FINDINGS
What survived source checking?

UNVERIFIED / REJECTED
What did not survive?

MACHINE RELEVANCE
What actually changes our understanding of Foundation / FRIDAY?

RECOMMENDATION
KEEP / TEST / DEFER / REJECT

PARKED
Interesting findings that do not change the active Goal.
```

Research stops when enough evidence exists to make the current decision.

---

## C. BUILDER — Codex

**Use for:**

- repository inspection tied to a bounded task;
- code changes;
- workflow repair;
- tests;
- refactors whose scope and completion condition are already known;
- producing candidate branches / diffs / receipts.

**Do not open Codex to figure out what the product should be.**

Control Room defines the work first.

### Required Codex work-order format

```text
GOAL
What exact outcome is required?

TARGET
Which repo / branch / files may be touched?

PROBLEM
What exact defect or missing behavior is being addressed?

DONE WHEN
What observable evidence proves success?

DO NOT
What must not change?

PROOF
Which tests / receipts / live checks must exist?

OWNER GATES
What requires explicit human approval?
```

If the task cannot be written this narrowly, it is not ready for Codex.

---

## D. AUTHORITY — GitHub + Harness

GitHub/Harness records what the machine actually accepts.

This includes:

- current project;
- approved immutable refs;
- active gate;
- evidence state;
- work-order status;
- receipts;
- proven learning;
- owner gates.

A model can propose a change.

Only the accepted evidence path can promote the result.

---

## E. PRIVATE DESK — Word / local private documents

**Use for:**

- full personal profile;
- private life history;
- long-form private thinking;
- sensitive notes;
- narrative drafts;
- material that should not be public machine governance.

**Never use a private Word document as parallel machine authority.**

The machine only needs compact non-sensitive operating rules derived from private material where they are genuinely useful.

---

# 5. Current model-routing rule

Model names change over time, so this section is descriptive rather than permanent authority.

## Normal reasoning

Use the normal strong ChatGPT reasoning model at medium effort for:

- planning;
- explanation;
- ordinary technical reasoning;
- goal recovery;
- result review.

## High reasoning

Use the highest practical reasoning effort/model for:

- architecture decisions;
- forensic audits;
- root-of-trust changes;
- cross-repo contradictions;
- difficult falsification/challenge passes.

## Codex

Use Codex only after a bounded work order exists.

Use a normal coding/reasoning model for small, clear repairs.

Use the strongest coding/reasoning model for hard cross-file or cross-repo work.

**Stronger model does not mean broader authority.**

## Mechanism ladder

Before escalating model intelligence, ask:

```text
Can deterministic code / existing tooling do it?
        ↓ no
Is there an existing proven skill/capability?
        ↓ no
Can proven capabilities be combined?
        ↓ no
Can a cheaper/smaller model do it safely?
        ↓ no
Use stronger general reasoning.
        ↓ still insufficient
Use heavy frontier / multi-agent search only if the problem earns it.
```

---

# 6. Every meaningful task gets one Goal Contract

The Goal Contract is the software form of:

> **DON'T DRIFT.**

Minimum structure:

```text
GOAL
What does Randy actually want?

DONE WHEN
What observable evidence means the Goal is satisfied?

CONSTRAINTS
What must not be broken, changed, exposed, spent, published, or assumed?

CURRENT STATE
Where are we actually now?

VERIFIED FACTS
What is supported by evidence?

UNKNOWNS
What still needs evidence?

ACTIVE BRANCH
What are we working on right now?

PARKED BRANCHES
Useful ideas not currently active.

NEXT MOVE
One bounded action that reduces uncertainty or advances the Goal.

OWNER GATES
Only decisions the owner actually has to make.

STOP CONDITIONS
When research / debugging / building must stop.

RESULT
What happened and where is the proof?
```

A Goal should get a stable identifier when it spans tools/sessions.

Example:

`GOAL-2026-10-05-FOUNDATION-01`

Research, Codex work orders, PRs, receipts, and proof should point back to the same Goal where practical.

---

# 7. Capture broadly. Execute narrowly.

The owner's associative thinking is not a defect to eliminate.

FRIDAY should preserve useful branches without letting them steal the active target.

Working rule:

- **Randy generates broadly.**
- **FRIDAY preserves broadly.**
- **Harness authorizes narrowly.**
- **Foundry builds narrowly.**
- **AIOS executes narrowly.**
- **Proof judges narrowly.**

### Parking rule

When a side idea appears:

1. capture it;
2. label it `PARKED` unless it materially changes the active Goal;
3. record why it might matter;
4. return to the active Goal.

Do not create a PR, architecture change, new repo, or new active work order merely to avoid forgetting an idea.

---

# 8. What "don't drift" means operationally

When the owner says:

> **Don't drift.**

The system should reconstruct this, in order:

1. **ACTIVE GOAL** — what are we trying to accomplish?
2. **DONE CONDITION** — what would actually close it?
3. **CURRENT VERIFIED STATE** — where are we really?
4. **ACTIVE BRANCH** — what are we working on right now?
5. **PARKED BRANCHES** — what ideas are preserved but inactive?
6. **NEXT MOVE** — one bounded action.

Do not respond to "don't drift" by creating more architecture.

---

# 9. Interaction adaptation without psychological authority

FRIDAY may react to observable interaction conditions.

Examples:

- owner explicitly says "I'm lost";
- owner explicitly says "don't drift";
- repeated correction of the same misunderstanding;
- too many simultaneously active branches;
- repeated question with no new evidence;
- explicit excitement;
- explicit frustration;
- current action contradicts original Goal.

Permitted adaptation:

- shorten explanation;
- reconstruct state;
- reduce jargon;
- park side branches;
- ask/return one next action;
- distinguish candidate from proof;
- challenge premature promotion.

Not permitted:

- changing factual truth based on emotion;
- diagnosing the owner;
- promoting a personality interpretation into authority;
- building separate Scooter/Randy/Ollie agents;
- storing private emotional history in public Harness.

---

# 10. Stop conditions

The machine must know when to stop.

## Research stops when

- enough evidence exists to make the current decision;
- new sources stop changing the answer;
- the remaining uncertainty does not affect the active Goal;
- the research budget/limit is reached.

## Debugging stops when

- the Goal's acceptance test passes;
- the attempt budget is reached;
- the same failure repeats without uncertainty decreasing;
- an owner gate is reached.

## Architecture exploration stops when

- an existing component already owns the responsibility;
- the new idea is interesting but not required by the active Goal;
- a bounded local repair is sufficient;
- no falsifying evidence justifies a rebuild.

## Conversation stops when

- the question is answered;
- the owner has one clear next move;
- more explanation would add detail but not change action.

## Improvement stops when

- the candidate fails to outperform the incumbent;
- held-out or non-regression tests fail;
- proof is insufficient;
- the change exceeds its authorized scope.

---

# 11. Learning contract

Never use:

```text
failure -> rule
```

Use:

```text
OBSERVED FAILURE
    ↓
TRACE / RECEIPT
    ↓
GENERALIZED NON-SENSITIVE CANDIDATE LESSON
    ↓
TURN LESSON INTO AN EVAL / TEST
    ↓
PROPOSE SMALLEST CHANGE
    ↓
ISOLATED CANDIDATE
    ↓
KNOWN TESTS + HELD-OUT / NON-REGRESSION TESTS
    ↓
INDEPENDENT PROOF
    ↓
PROMOTE OR REJECT
```

Only proven generalized learning may become operating law.

Raw chat is not learning authority.

Emotional intensity is not proof.

Repeated wording is not proof.

Model confidence is not proof.

---

# 12. Three memory planes

Do not create one giant FRIDAY memory.

## EVIDENCE MEMORY

Preserve what actually happened:

- receipts;
- commits;
- test results;
- files;
- user-reported facts with provenance;
- verified external evidence.

Evidence is not silently rewritten by later interpretation.

## WORKING STATE

Preserve what is happening now:

- active Goal;
- active branch;
- blockers;
- parked ideas;
- next action;
- temporary context.

## PROVEN LEARNING

Preserve only reusable lessons that survived the learning contract.

No raw-chat rule promotion.

No private-life dump.

No inference promoted as fact.

---

# 13. Daily owner workflow

Use this until FRIDAY automates it.

```text
RANDY
  │
  ▼
CONTROL ROOM
"What am I trying to accomplish?"
  │
  ├── simple question ─────────► solve here
  │
  ├── evidence missing ────────► RESEARCH LAB
  │                               │
  │                               ▼
  │                         evidence packet
  │                               │
  ├───────────────────────────────┘
  │
  ├── code/change required ─────► CODEX
  │                               │
  │                               ▼
  │                         candidate + tests
  │                               │
  ▼                               │
CONTROL ROOM ◄────────────────────┘
  │
  │ compare result to GOAL
  ▼
HARNESS / PROOF
  │
  ├── FAIL ─► one next bounded move
  │
  └── PASS
       │
       ▼
CLOSE GOAL
record result
park discoveries
start next Goal only intentionally
```

---

# 14. Current build program

This is the research-derived build order. It is a plan, not automatic authority.

## PHASE 0 — Repair the truth machine

Before adding new FRIDAY capability:

1. fail closed if self-improvement proof/validation fails;
2. prevent unproven incidents from becoming active learned rules;
3. converge on one canonical learning/promotion path;
4. remove or clearly demote stale files that call themselves current;
5. reconcile stale FRIDAY wording and duplicate status surfaces;
6. strengthen repository enforcement around authority where practical.

**Exit condition:**

> No path can promote authority or learned behavior while bypassing Foundation's own proof policy.

---

## PHASE 1 — Make Goal continuity real

Finish the Goal Contract using existing Harness state mechanisms rather than creating another architecture.

Prove:

- active Goal survives session/restart;
- side ideas remain parked;
- current verified state can be reconstructed;
- one next action is recoverable;
- owner does not have to restate the entire problem.

**Exit proof:**

Start one Goal, deliberately create several side branches, interrupt/restart, and recover the same Goal plus its parked branches without re-explanation.

---

## PHASE 2 — Finish the bounded phone round trip

Return to the existing `PAGES_BOUNDED_JOB_ROUND_TRIP` gate after Phase 0 makes the control plane trustworthy.

Prove:

- authenticated owner action from phone;
- only the approved bounded fixture runs;
- exact job identity survives;
- Foundry / AIOS / Independent Proof correlation survives;
- reload/status recovery works;
- denial path works;
- retries do not silently duplicate work;
- understandable proof returns to phone.

Do not expand to arbitrary natural-language coding until this works.

---

## PHASE 3 — Proven memory

Implement only:

- evidence memory;
- working state;
- proven learning.

Prove questions such as:

- "Why did we decide this?"
- "What failed last time?"
- "What evidence supports this state?"

Responses must return provenance rather than invented recollection.

---

## PHASE 4 — Capability reuse

Operationalize the existing mechanism ladder:

- deterministic tool;
- proven skill;
- capability combination;
- cheap model;
- stronger model;
- heavy search only when earned.

Scrapyard answers:

> **Do we already have something that can do this?**

Foundry only builds when reuse is insufficient.

---

## PHASE 5 — Real learning loop

Convert proven failures into evals before changing behavior.

Candidate improvements must beat the incumbent and pass non-regression / held-out evaluation before promotion.

---

## PHASE 6 — Owner-compatible interaction

Encode only compact stable operating preferences such as:

- truth before reassurance;
- constructive criticism over flattery;
- behavior before jargon;
- one next move when overloaded;
- preserve side ideas without changing the active target;
- do not make the owner operate infrastructure unnecessarily;
- do not confuse excitement with proof;
- do not repeat questions whose answers are already known.

Do not build a psychological model of the owner.

---

## PHASE 7 — Replay / modular evolution later

Only after receipts and learning are trustworthy:

- receipt replay;
- policy comparison against historical evidence;
- modular harness improvement;
- hidden / held-out evaluation;
- candidate genealogy;
- limited self-modification inside the proof cage.

Do not begin here.

---

# 15. Immediate next build target

The next implementation target after this playbook is **not** another FRIDAY feature.

It is:

> **PHASE 0 — repair the Harness truth/learning plane.**

First bounded work order should address:

1. self-improvement publishing despite failed proof/validation;
2. unproven incident lessons entering active generated rules.

Scope should remain Harness-only unless evidence proves another repo is required.

---

# 16. Things the owner should not do anymore

- Do not open Codex with "make FRIDAY better."
- Do not create a new Foundation chat for every side idea.
- Do not let research directly become implementation.
- Do not let Codex choose architecture while coding.
- Do not put the full private personal profile into public Harness.
- Do not let Word become parallel machine truth.
- Do not merge because a model says the result looks good.
- Do not promote an idea because it is exciting.
- Do not keep researching after enough evidence exists to decide.
- Do not create another FRIDAY.
- Do not rebuild Foundation because one subsystem needs repair.
- Do not confuse preservation with promotion.

---

# 17. Definition of FRIDAY V1 done

FRIDAY V1 is real when the owner can say from the normal front door:

> **"Friday, I want to accomplish X."**

and the system can:

1. establish the Goal and DONE condition;
2. preserve it durably;
3. recover relevant evidence/history;
4. check existing capabilities before building;
5. select the cheapest sufficient mechanism;
6. execute reversible bounded work automatically;
7. stop only at real owner gates;
8. survive interruption/restart;
9. preserve side discoveries without changing the Goal;
10. independently verify completion;
11. learn only through proven evals;
12. return an understandable result and proof;
13. later answer "Where were we?" without requiring a handoff novel.

A good final response looks conceptually like:

```text
DONE
Here is what happened.
Here is the proof.
Here are the two useful side discoveries I parked instead of letting them derail the Goal.
```

---

# 18. The pocket version

If everything else is too much, use this:

## TALK
Start in Control Room.

## GOAL
State what you want and what DONE means.

## PARK
Capture side ideas; do not activate them automatically.

## RESEARCH
Only when evidence is missing.

## CODEX
Only after the task is bounded.

## PROOF
The model does not certify itself.

## HARNESS
Records what survived.

## STOP
When DONE is proven, stop.

---

# 19. Change policy for this playbook

This file may evolve as the owner workflow becomes clearer, but it should stay small enough to be usable.

Changes should be made only when:

- repeated real use exposes a missing operating rule;
- the product/tool landscape changes enough to make routing advice stale;
- a proven Foundation mechanism replaces a manual step in this guide.

Do not expand this file merely because a new idea is interesting.

When FRIDAY eventually performs these decisions automatically, this playbook should shrink rather than grow.
