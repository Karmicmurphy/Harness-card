# Harness Card Self-Improvement Loop

## Purpose

Turn costly project failures into permanent operating improvements so the same class of mistake becomes less likely on future work.

## Loop

`OBSERVE -> CLASSIFY -> ROOT CAUSE -> FIX -> PROVE -> GENERALIZE -> GUARD -> RECORD -> REUSE`

### 1. OBSERVE
Capture what the user actually saw or experienced.

### 2. CLASSIFY
Name the failing layer: contract, authority, local state, test/CI, deploy, cache/edge, application, provider, customer, physical, or creative.

### 3. ROOT CAUSE
Separate the actual cause from attractive false leads.

### 4. FIX
Apply the smallest coherent correction.

### 5. PROVE
Repeat the same real path that failed. Proxy evidence cannot close the incident.

### 6. GENERALIZE
Ask: what broader rule would have prevented this class of failure?

### 7. GUARD
Create the cheapest durable guardrail: test, validator, checklist, state field, routing rule, or hard contract rule.

### 8. RECORD
Update incident ledger, current authority, active work order, and release receipt when applicable.

### 9. REUSE
Automatically apply the learned guardrail to future projects with the same failure shape.

## Loop Deck lesson set

The Loop Deck run established these durable rules:

- UI source code existing is not equivalent to the intended screen winning at runtime.
- A successful deploy is not equivalent to fresh assets reaching a previously installed/cached phone.
- Service workers require explicit cache-version and update strategy proof.
- Legacy modules can override new UI after startup; startup-settled state must be checked.
- A polished mockup must remain visibly separate from implementation proof.
- Current-project authority must be updated after every material fix, not only at initial implementation.
- User-reported live success is valid real-world evidence when clearly labeled as user-reported.
- One user-facing failure should trigger inspection for sibling failures before another redeploy.

## Closeout question

Before closing any substantial task, ask:

**What did this project teach the harness that the next project should get for free?**
