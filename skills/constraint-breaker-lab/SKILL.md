# Constraint Breaker Lab

name: constraint-breaker-lab
version: 0.1.0
status: CANDIDATE
canonical_repo: Karmicmurphy/Harness-card
canonical_path: skills/constraint-breaker-lab/SKILL.md

## Purpose

Use when a desired capability technically works or is understood, but latency, hardware, memory, cost, bandwidth, dependency mass, reliability, complexity, or owner effort makes the current implementation unacceptable.

The job is not to optimize the current implementation by reflex. The job is to recover the required outcome, expose hidden assumptions, invert them, search sideways and backward for alternate mechanisms, and run the cheapest experiment that can falsify the current favorite.

## Trigger

Route here when any of these are true:
- a working mechanism is too slow, too heavy, too expensive, too fragile, or too manual;
- the obvious solution requires hardware or a subscription the owner does not want;
- repeated tuning of the same implementation produces little gain;
- the problem statement has silently become identical to the current implementation;
- the owner asks for an outside-the-box, workaround, old-tech, cross-domain, or radically simpler path.

## Core loop

`OUTCOME -> CONSTRAINT -> ASSUMPTIONS -> INVERT -> SEARCH -> RECOMBINE -> TEST -> ATTACK FAVORITE -> KEEP WINNER -> DOWNSHIFT`

### 1. OUTCOME
State what must actually happen without naming the current mechanism.

Example: `FRIDAY answers conversationally by voice.`
Not: `Make Kokoro run faster.`

### 2. CONSTRAINT
Use measured evidence when possible.

Name the actual bottleneck: startup, warm latency, RAM, CPU instruction set, bandwidth, cost, owner steps, provider gate, or another specific limit.

### 3. ASSUMPTIONS
List implementation choices currently being treated as requirements.

Typical hidden assumptions:
- one engine must do the whole job;
- every result must be generated live;
- the highest-quality path must handle trivial work;
- a modern neural method must beat an old deterministic method;
- one device must perform every stage;
- a model must solve something a cache, grammar, table, DSP routine, state machine, or compiler can solve;
- a hardware limitation automatically implies a hardware purchase.

### 4. INVERT
For every material assumption, ask the opposite.

Examples:
- generate every time -> generate once and reuse;
- one engine -> route between specialized gears;
- general recognizer -> restricted grammar for known commands;
- local-only compute -> reuse already-owned nearby compute if policy permits;
- neural -> deterministic, compiled, cached, indexed, or signal-processing mechanism;
- newest technology -> archived, embedded, industrial, accessibility, telephony, game, aerospace, or DSP ancestor.

### 5. SEARCH
Route only the needed existing skills:
- `artifact-compass` for mechanism classes;
- `deep-sea-salvage` for historical, obscure, constrained-system, or abandoned mechanisms;
- `artifact-salvage` for extracting a useful atom without importing a platform;
- `cost-complexity-challenge` before accepting heavy or paid machinery;
- `recombination-forge` when multiple partial mechanisms can form the answer;
- `rights-gate` before code reuse;
- `thought-economy` when repeated intelligence should become deterministic;
- `capability-downshift` after a repeated win is proven.

Use the suite Adaptive Pass Rule. Research stops when a bounded experiment will buy down more uncertainty than another pass.

### 6. RECOMBINE
Prefer a system of small gears when one giant mechanism is wasteful.

A valid result may intentionally use different mechanisms for:
- wake/attention;
- routing;
- familiar commands;
- novel language;
- cached responses;
- dynamic responses;
- local work;
- remote or stronger work.

### 7. TEST
Run the smallest discriminating bake-off against the same input and acceptance metric.

Measure only what affects the decision, for example:
- cold startup;
- warm latency;
- CPU/RAM peak;
- accuracy on the owner's real phrases;
- dependency size;
- recurring cost;
- number of owner steps;
- rollback difficulty.

Do not redesign before the bake-off.

### 8. ATTACK FAVORITE
Before promotion, deliberately try to disprove the leading candidate.

Check:
- hidden hardware assumptions;
- weak or irrelevant benchmarks;
- maintenance state;
- license/rights;
- security and privacy costs;
- dependency explosion;
- regressions on the actual owner path;
- whether an even simpler mechanism already wins.

### 9. KEEP WINNER
Promote only on evidence. Reject attractive losers explicitly so they do not return as zombie ideas.

### 10. DOWNSHIFT
A proven workaround should reduce future compute and owner effort.

Convert repeated wins into the cheapest adequate durable form: policy, cache, script, compiled asset, lookup table, tiny model, validator, benchmark, test, or routing rule.

## Hardware-purchase gate

A hardware limitation does not authorize a hardware purchase until software architecture, caching, decomposition, reuse, existing hardware, and lightweight alternatives have been measured or ruled out proportionately.

## Automation coupling

When `config/friday_automation_policy.json` is present:
- automatic candidate exploration stays bounded and reversible;
- tests and benchmarks may run automatically where already authorized;
- secrets, permission broadening, spending, destructive actions, public/production activation, and unapproved live side effects remain owner gates;
- every automated experiment must leave a receipt sufficient to explain what won and why.

## Output

Return:
- required outcome;
- measured constraint;
- assumptions broken;
- candidate mechanisms;
- cheapest discriminating test;
- counter-evidence;
- winner/losers;
- what becomes deterministic afterward;
- one next move and stop condition.

## Success condition

This skill becomes PROVEN after it changes the recommended mechanism on at least two distinct real constraints and those replacements pass their bounded owner-relevant proof.
