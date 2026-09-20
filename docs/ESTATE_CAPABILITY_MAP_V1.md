# Estate Capability Map — V1

Date: 2026-09-20

Status: **RECONCILIATION MAP — NOT FINAL ARCHITECTURE**

This is the first capability-first view of the recovered estate. It extends the existing Harness recovery system; it does not replace the estate ledger, ecosystem authority index, project authority, or live repo truth.

Machine-readable companion: `state/ESTATE_CAPABILITY_MAP_V1.json`.

## First major finding

The estate already contains most of the layers Randy has been describing.

The missing problem is not “invent an AI factory.” The missing problem is **reconcile the interfaces and authority boundaries among mechanisms that already exist**.

A plausible recovered stack is emerging, but it is not architecture authority yet:

```text
Human front door / artifacts
  -> Twis Holo Workshop

Cross-project intent / scope / recovery
  -> Harness Card

Discovery / salvage / rights / recombination
  -> Digital Scrapyard salvage suite
  -> Foundry Temporal Compass / salvage registry

Typed jobs / bounded software work / learning lifecycle
  -> Temporal Capability Foundry

Scheduling / process lifecycle / explicit capability grants
  -> Untethered AIOS primitives

Independent proof / certificate / quarantine
  -> CERT-RIVER / PRISM-RIVER / RiverKernel lineage
     (must still be reconciled to live code/packages)
```

The rule is **do not merge these repos**. Name the primitive, preserve the authority boundary, and build only the smallest adapters that proof requires.

## What we already own

### Human cockpit + artifact system — Workshop

Live repo: `Karmicmurphy/Ollie_Twis_Holo_workshop@04a5b694...`

This is materially more complete than a shell. Current repo evidence includes:

- SQLite + FTS5 artifact index;
- project switching;
- artifact save/search/delete;
- session-close records;
- project capsule ZIP export;
- folder import with hashes, source authority, skipped-file reporting and receipt;
- Coding Bench constrained to project folders;
- Recovery Importer;
- Artifact Compass UI;
- Receipt Ledger;
- module registry;
- Powerhose Engine Harness;
- Local Model Socket;
- Tiny AI Lane;
- Generation Router;
- MCP Gate;
- optional Cloudflare remote hull.

The important existing design law is already written there:

> Engines are replaceable tools. Artifacts are the permanent system.

### Cross-project control + recovery — Harness Card

Live repo: `Karmicmurphy/Harness-card@40d2161...`

Harness already owns:

- recover-before-rebuild;
- intent/current-truth recovery;
- project routing;
- scope control;
- skill routing;
- proof/closeout law;
- estate source-yard ledger;
- ecosystem authority index;
- current planning/reconciliation marker.

Harness should remain the operating/recovery authority rather than becoming another execution kernel.

### Capability lifecycle + Software Builder — Foundry

Current builder branch: `software-builder-v0@431651c...`

Foundry already owns a proven integrated capability lifecycle:

`intent -> job -> execution -> evaluation -> learning candidate -> promotion -> activation -> rollback`

Software Builder adds:

`inspect -> edit -> test -> observe failure -> repair -> retest -> receipt`

The real Ollama engine is now attached:

- runtime: Ollama on GitHub Actions;
- model: `qwen2.5-coder:1.5b-instruct`;
- engine smoke test: PASS;
- required initial failing capability test: observed;
- model changed only `src/untethered_aios/capabilities.py`;
- tests were not edited;
- latest proof run `35522934878`: **BLOCKED** because the worker exhausted its 10-step budget before a passing retest.

Important correction: `state/SOFTWARE_BUILDER_V0_AUTHORITY.json` is stale. It still says no callable coding runtime exists. Do not treat that statement as current truth; live branch + CI supersede it.

### Scheduler / bounded capabilities — Untethered AIOS

Live repo: `Karmicmurphy/Untethered-AIOS@17a717e...`

Reusable primitives are real code, not just architecture prose:

- process states and cooperative scheduler;
- spawn/suspend/resume/cancel;
- wait/event wakeup;
- max tick bound;
- explicit capability registry;
- unknown/ungranted capability denial;
- path containment;
- child grants must be a subset of parent grants;
- hash-addressed audit receipts.

Likely role: **salvage scheduling/lifecycle/grant primitives**, not replace Foundry or Workshop.

### Salvage / rights / recombination method — Digital Scrapyard

Live repo: `Karmicmurphy/digital-scrapyard-autopilot@40a04675...`

Exact reusable skill inventory recovered in the current tree includes:

Artifact Compass, Artifact Salvage, Capability Downshift, Cost & Complexity Challenge, Deep-Sea Salvage, Intent Recovery Compass, Market Want Board, Owner Interruption Minimizer, Project Closeout Gate, Project Context Harvester, Proof Gate, Rabbit-Hole Governor, Recombination Forge, Rights Gate, and Thought Economy.

That is the canonical salvage-method source. Foundry can index it; Workshop can surface it; neither needs to recreate it.

### Independent certification — River lineage

Recovered authority currently lives in Harness lineage/index material and Workshop FlashRiver extraction, not one verified canonical live repo.

Recovered concepts include CERT-RIVER, PRISM-RIVER, RiverKernel, quarantine, claim-boundary proof, no-certificate-no-use, proof failure/repair/rerun, and receipt/trace/certificate separation.

This is the biggest unresolved overlap. **Do not let Builder become its own final certifier simply because Foundry has evaluation receipts.**

### Real production proving ground — First3 Local

Live repo: `Karmicmurphy/nemoclw_new_agent@fdb4d3b...`

First3 already has a serious deterministic release chain:

full tests -> synthetic funnel -> exact Cloudflare deploy -> live smoke -> Stripe commissioning contract.

Keep it separate. Once builder + independent certification boundaries are stable, First3 is an excellent real bounded proving ground.

## Overlap decisions — V1

**Proof:** keep Foundry development/evaluation feedback, AIOS audit, Workshop artifact receipts, and CERT-RIVER certification distinct until claim/certificate semantics are reconciled.

**Execution:** do not choose one “winner” and throw the rest away. Foundry owns typed capability work; Software Builder owns coding-loop boundaries; AIOS offers schedulable process/grant primitives; Workshop is the human-facing engine surface.

**Discovery:** Artifact Compass is one lineage with three useful forms: Scrapyard method, Workshop UI/local artifact search, Foundry mechanism/provenance trace.

**Local AI:** Foundry Ollama runtime and Workshop Local Model Socket are adjacent replaceable-engine boundaries. Reuse a shared manifest/adapter concept rather than create another model layer.

## First invention candidates

### 1. Estate Front Door / Cabinet of Curiosities

Combine Harness estate authority + Workshop Artifact Compass/My Work + Recovery Importer + Foundry mechanism trace + Recombination Forge.

Goal: one place that can answer:

- what do I have?
- what works?
- what overlaps?
- what failed but contains useful parts?
- what weird useful thing did the estate discover?

Start read/recommend-only. No autonomous authority.

### 2. Builder-to-CERT Bridge

Feed Software Builder receipts to a clean independent CERT-RIVER-derived proof lane.

Builder can test itself for development feedback. Independent certifier reruns acceptance proof from clean state and decides certificate/quarantine.

Blocked until River lineage is reconciled to exact reusable artifacts.

### 3. Free-First Software Worker

Foundry Software Builder + Ollama/Qwen + GitHub runner + AIOS scoped grants, later surfaced through Workshop Local Model Socket.

Most of this already exists. The current engineering gap is not “find an AI.” It is getting the small model through the bounded loop efficiently enough to pass within budget.

## Immediate next reconciliation

1. Recover exact CERT-RIVER / PRISM-RIVER / RiverKernel implementation artifacts from the archived/Library/Workshop lineage.
2. Map their contracts against Foundry evaluation/proof, AIOS audit, and Workshop receipts.
3. Refresh the stale Software Builder authority pointer after the next meaningful proof change rather than trusting the old blocker.
4. Define a machine-maintainable estate delta update so future passes scan **what changed**, not the entire estate again.
5. Then run a second invention pass across product/creative repos using this capability vocabulary.

## Non-claims

- This is not final architecture.
- No repos were merged or deleted.
- No autonomous spending/deploy/delete authority was added.
- Workshop local-private runtime claims still need verification against the actual local authority when available.
- CERT-RIVER is recovered lineage, but a single current canonical implementation repo has not yet been verified.
