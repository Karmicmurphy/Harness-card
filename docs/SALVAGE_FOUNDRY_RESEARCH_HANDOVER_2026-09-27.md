# Salvage Foundry — Canonical Research Handover

**Date:** 2026-09-27  
**Status:** QUEUED RESEARCH / IMPLEMENTATION HANDOVER  
**Owner:** Randy / Harness Card  
**Canonical entry point:** this file  
**Do not reconstruct this project from chat history. Start here.**

## 1. Purpose

Salvage Foundry is a research-and-build project for making the existing Foundation machine improve by recovering engineering mechanisms from old and current systems, matching those mechanisms to recurring constraint shapes, generating challengers, testing them, proving them independently, and retaining the evidence as reusable machine knowledge.

It is **not** a replacement for Harness Card, Artifact Compass, Artifact Salvage, Digital Scrapyard, Foundry, Builder, AIOS, Independent Proof, or Workshop.

It is intended to strengthen the existing chain:

`Harness -> Artifact Compass / Artifact Salvage -> Digital Scrapyard -> Foundry -> Builder -> AIOS -> Independent Proof -> Workshop -> Owner`

The central objective is:

> **Build a machine that accumulates proven advantages.**

The project does not reject AI. It should use deterministic and zero-model mechanisms wherever they are sufficient, then escalate to AI workers where ambiguity, synthesis, extraction, invention, or implementation genuinely earns the additional intelligence cost.

Working law:

> **AI discovers. Salvage Foundry mechanizes.**

Whenever AI repeatedly solves the same class of problem, the machine should attempt to turn that success into a rule, recipe, test, constraint, mechanism card, transformation, lookup, benchmark, or other reusable deterministic capability.

---

## 2. Locked theory

Do not begin from a blank-page invention model.

Treat engineering history as a scrapyard of **mechanisms**, not products or artifacts.

Possible source material includes:

- abandoned software;
- obsolete protocols;
- discontinued hardware;
- old operating systems;
- industrial controls;
- aerospace and scientific systems;
- expired/superseded standards;
- patents and patent families;
- technical manuals;
- failed or abandoned products;
- university/lab research;
- archived or unfashionable implementations;
- the owner's own repository/warehouse history;
- prior failures;
- successful descendants produced by Salvage Foundry itself.

The useful unit is not "an old modem" or "a dot-matrix printer." The useful unit is the mechanism under the constraint that shaped it.

Example abstractions:

- **Old modem:** maintain synchronization over unreliable communication using bounded acknowledgement, retry, error detection, sequence state and renegotiation.
- **Dot-matrix printer:** produce arbitrarily long output while holding only a bounded working slice in memory.
- **Delay-tolerant networking:** store-and-forward across intermittent or delayed connectivity without assuming continuous end-to-end reachability.
- **Kermit:** negotiate protocol behavior to fit wildly different endpoints and communications constraints.

The core hypothesis is:

> Products disappear. Constraints recur. Mechanisms often remain useful.

---

## 3. Research conclusion

A wide Artifact Compass / Artifact Salvage pass was performed across:

- TRIZ and historical invention-method literature;
- functional modeling / mechanism abstraction;
- package management and dependency solving;
- compiler rewrite systems and e-graphs;
- formal verification and proof-carrying-code ideas;
- reproducible builds and software supply-chain provenance;
- storage/filesystem self-healing;
- distributed-system reconciliation;
- runtime assurance / Simplex architectures;
- statistical control and drift detection;
- operating-system generations and rollback;
- fuzzing / mutation / differential / metamorphic testing;
- NASA / NIST / IETF / protocol history;
- patent and archival data sources;
- modern agent runtimes and Jarvis/Alice-style projects;
- the owner's existing PersonalJarvis salvage and Digital Scrapyard estate.

The search reached **working saturation**: later passes were adding examples and implementations, but were no longer changing the mechanism map or recommended architecture materially.

This does **not** claim that every repository, paper or patent on Earth was inspected. It means additional broad research currently has lower information value than a bounded implementation/proof experiment.

---

## 4. Strong factual precedents

Salvage Foundry should not claim that mining prior engineering for reusable principles is unprecedented.

Relevant precedents include:

- **TRIZ:** recurring inventive principles recovered from large bodies of patent material.
- **Functional Basis / function modeling:** representation of what engineered systems do independently of a specific physical implementation.
- **Case-based mechanism synthesis:** prior research has reused and composed mechanism/function primitives to synthesize new designs.
- **FFTW wisdom:** empirical selection among implementation plans, retention of winning plans, and later reuse of that operational knowledge.
- **git rerere:** remember a prior conflict resolution and reuse it when the same conflict shape reappears.
- **git bisect run:** mechanically locate the history point that changes a measurable property.
- **SAT/constraint solvers:** avoid repeating impossible branches through learned conflict clauses.
- **Simplex / Runtime Assurance:** allow a complex/evolving component to operate while a simpler high-assurance controller preserves the safety boundary.
- **Proof-Carrying Code / certificate checking:** an untrusted producer can provide evidence that a much smaller verifier checks.
- **Nix / atomic deployment systems:** preserve generations and rollback rather than destroying the previous known-good state.
- **ZFS/Btrfs/Merkle repair:** detect divergence/corruption and repair from trusted state.

The potential value of Salvage Foundry is in combining these ideas into one owner-governed continuous salvage-and-promotion loop, not in pretending the individual ideas are new.

---

## 5. Existing Randy-owned primitives — reuse, do not rebuild

### Harness Card

Current self-improvement loop:

`OBSERVE -> CLASSIFY -> ROOT CAUSE -> FIX -> PROVE -> GENERALIZE -> GUARD -> RECORD -> REUSE`

Current Harness already writes learned rules from verified incidents and has a non-negotiable rule that generated learning may strengthen proof/quality requirements but may not weaken protected boundaries or promote weak evidence.

### Artifact Compass

Already asks:

> **What mechanisms could solve this?**

It already widens across modern systems, open source, standards, academic ancestors, OS/database/compiler/networking analogues, embedded/industrial/DSP/game systems, laboratories, abandoned systems and cross-domain analogues.

### Adaptive Pass Rule

Already establishes:

> **PASSES MUST EARN PASSES.**

Use it to stop research when bounded experiments become more informative.

### Missing Gear

Digital Scrapyard already contains a deterministic collision/ranking engine that:

- accepts typed artifacts / warehouse manifests;
- rewards real output->input bridges;
- rewards shared mechanisms/capabilities and cross-domain distance;
- suppresses known overlaps and metadata-only novelty;
- leaves unrelated artifacts isolated;
- requires no model, embeddings, vector database, paid service, or API key.

This is the first zero-model recombination primitive. Extend it only as needed; do not replace it with another framework.

### PersonalJarvis salvage already completed

Canonical salvage already exists in:

`Karmicmurphy/digital-scrapyard-autopilot/warehouse/intake/personal-jarvis-2026-09-21/`

High-value recovered patterns include:

- capability routing;
- pure dispatch;
- fast ACK / slow worker;
- provider fallback;
- isolated worktree worker;
- bounded worker -> critic;
- persist-before-publish;
- one ToolExecutor safety funnel;
- risk tiers;
- atomic configuration mutation;
- private evidence-backed learning;
- draft-only learned skills;
- per-worker capability grants/denies;
- exact action approvals;
- honest unavailable states.

**Do not reopen PersonalJarvis wholesale. Salvage the mechanisms already recovered.**

---

## 6. Core data structure: Mechanism Card

Create a normalized machine-readable card describing behavior rather than branding or product identity.

Minimum conceptual schema:

```yaml
identity:
  mechanism_id:
  name:
  source_artifact:
  source_date_or_era:
  provenance:
  rights_state:
  evidence_state:

function:
  purpose:
  failure_prevented:
  observable_behavior:

original_problem:
  description:

constraint_fingerprint:
  memory:
  compute:
  power:
  bandwidth:
  latency:
  storage:
  noise:
  reliability:
  connectivity:
  materials:
  manufacturing:
  environment:
  human_attention:
  cost:
  maintenance:
  repairability:
  safety:

mechanism:
  inputs: []
  outputs: []
  state: []
  transformations: []
  feedback:
  trigger:
  failure_behavior:
  recovery_behavior:

why_it_worked:
  governing_principle:
  assumptions: []
  tradeoffs: []
  known_failure_modes: []

transfer:
  modern_constraint_analogues: []
  interfaces: []
  composability: []
  known_incompatibilities: []

rights:
  patent_status:
  copyright_or_license:
  code_reuse_state:
  attribution_obligations: []
  clean_room_required: false
  manual_review_required: false

evidence:
  historical: []
  modern_tests: []
  benchmark_receipts: []
  proof_receipts: []

lineage:
  parents: []
  children: []
  recombinations: []
  wins: []
  losses: []
  superseded_by:
```

---

## 7. Constraint fingerprint

The constraint fingerprint is more important than the original product name.

Example target:

```text
POWER          severe
MEMORY         severe
BANDWIDTH      severe
CONNECTIVITY   intermittent
LATENCY        tolerant
NOISE          moderate
STATE          local preferred
RECOVERY       autonomous
INFRASTRUCTURE unreliable
```

Search for historical systems that experienced similar pressure even if their domain names are unrelated.

Potential matches could include packet radio, spacecraft telemetry, store-and-forward messaging, Kermit, dial-up negotiation, SCADA, scientific instruments, old embedded loggers, DTN, etc.

The system should therefore search by **constraint shape + function**, not only keywords.

---

## 8. Rights Gate

"Old" does not mean "free to copy."

Separate:

1. factual information;
2. mechanism/principle;
3. patent rights;
4. implementation copyright/license obligations;
5. brand/trademark/UI/persona material.

Suggested rights states:

```text
FACTUAL_REFERENCE
MECHANISM_REFERENCE
CLEAN_ROOM_ADAPTATION_CANDIDATE
CODE_REUSE_PERMITTED
CODE_REUSE_WITH_OBLIGATIONS
HUMAN_RIGHTS_REVIEW
BLOCKED
UNKNOWN
```

Expired patent material may become a reuse candidate only after Rights Gate verifies relevant patent family/jurisdiction/status and checks for other controlling rights.

Open-source code is not automatically "reference only"; classify by the actual license and obligations.

Artifact Compass discovers. Rights Gate decides what may proceed.

---

## 9. Candidate generation ladder

Attempt the cheapest adequate mechanism first:

```text
exact known winner
-> deterministic rule
-> known recipe
-> existing mechanism reuse
-> mechanism adaptation
-> Missing Gear typed recombination
-> constraint solver / SAT / SMT
-> rewrite / e-graph / equality saturation
-> quality-diversity / evolutionary exploration
-> cheap specialized or local AI
-> general AI worker
-> owner judgment / authority
```

No candidate receives extra authority because it came from a smarter model.

---

## 10. Fitness must remain a vector

Do not reduce candidate quality to one magic number.

Hard constraints stay hard.

Example vector:

```text
functional_success   PASS
constraint_fit       0.97
memory               416 bytes
energy               0.81
latency              0.72
reliability          0.98
dependency_mass      0.91
repairability        0.94
rights_clarity       1.00
proofability         0.96
owner_burden         0.97
```

Retain different winners for different niches where appropriate (low-memory, low-power, highest-reliability, no-network, minimum-dependency, etc.). Quality-diversity / MAP-Elites style thinking is a better fit than a single global champion.

---

## 11. Evidence reinforcement and decay

Borrow the useful part of ant-colony behavior without turning historical success into permanent lock-in.

```text
success -> reinforce
failure -> penalize
time -> decay stale confidence
environment change -> revalidate
new challenger -> reopen competition when materially different
```

Evidence should accumulate, but applicability must decay when conditions change.

---

## 12. Wisdom Registry

Create durable records of what actually won, against what, under which conditions.

Concept:

```yaml
problem_family: python/path-containment-repair
environment:
  python: "3.12"
  platform: linux
  repo_size: small
  proof_type: unit-tests
contestants:
  - large_model
  - small_model
  - deterministic_rewrite_v3
winner: deterministic_rewrite_v3
result:
  success: true
  runtime_ms: 82
  recurring_cost: 0
  proof: CERTIFIED
invalidates_on:
  - material environment change
  - winning implementation version change
  - proof contract change
  - new security finding
```

Next time the same shape appears, prefer the known winner and avoid paying intelligence again unless invalidated.

Economic law:

> **Never pay intelligence twice for a problem the machine has already learned to solve mechanically.**

---

## 13. Capability Downshift

Repeated AI success should trigger an attempt to mechanize the result:

```text
AI solves repeated problem
-> identify repeatable pattern
-> extract deterministic rule/recipe/transformation/test
-> prove it
-> register it
-> future jobs use deterministic route first
```

Potential deterministic tools/mechanism families include OpenRewrite, Coccinelle, AST-based rewriting, constraint solvers, e-graphs/equality saturation, fixed rule engines, and generated validators.

---

## 14. Proof must evolve too

Do not improve candidates while leaving weak tests unchanged.

Possible proof amplifiers:

- regression tests;
- differential testing;
- property-based testing;
- metamorphic testing;
- mutation testing;
- deterministic failure reduction;
- static analysis;
- symbolic execution;
- model checking;
- SAT/SMT verification;
- translation validation;
- reproducible builds.

Permanent law:

> **Every important failure should improve the regression corpus or proof mechanism that allowed it through.**

---

## 15. Proof-carrying promotion

Promotion should move toward a producer/certificate/checker split.

A candidate should arrive with machine-checkable evidence such as:

```text
candidate
+ source SHA
+ mechanism lineage
+ rights receipt
+ dependency lock
+ test receipt
+ benchmark receipt
+ security/provenance receipt
+ proof certificate
          |
          v
small independent verifier
          |
      CERTIFY / REJECT
```

The Builder, producing model, Compass, or Salvage worker may not certify itself.

---

## 16. Simplex / Runtime Assurance boundary

This is the strongest safety architecture recovered during research.

Separate the system into:

```text
EVOLVING ZONE
- Artifact Compass
- Artifact Salvage
- AI workers
- recombination
- new tools
- new models
- new routes
- new recipes
- optimization / experiments

------------------------------
NON-EVOLVING ASSURANCE KERNEL
- owner authority
- workspace identity
- protected paths
- credential scope
- rights requirements
- proof requirements
- spending limits
- promotion rules
- rollback requirement
- certificate verifier
- audit-history integrity
```

Constitutional law:

> **The thing capable of evolving is never the thing holding ultimate authority over its own evolution.**

---

## 17. Generations and rollback

A successful challenger must not erase the previous known-good state.

Maintain lineage such as:

```text
GEN-041 proven incumbent
GEN-042 failed candidate
GEN-043 certified candidate
GEN-044 current incumbent
```

Rejected generations remain evidence.

Use atomic/generation-style deployment ideas from systems such as Nix/OSTree/A-B update strategies where appropriate.

---

## 18. Estate self-healing

Storage/distributed-system mechanisms suggest a future **Estate Scrubber**:

```text
canonical manifest
-> hash/tree comparison
-> locate exact divergence
-> compare trusted lineage
-> restore / quarantine / request review
```

Relevant mechanism families include checksummed filesystems, Merkle-tree comparison, append-only logs and WAL/MANIFEST recovery.

This is a deterministic integrity lane, not an AI judgment lane.

---

## 19. External source yards worth adapters

Candidate future adapters include:

- EPO Open Patent Services;
- WIPO PATENTSCOPE;
- Lens patent/scholarly data;
- NASA Technical Reports Server;
- NIST publications;
- IETF Datatracker + Historic/Obsolete RFCs + expired Internet-Drafts;
- Computer History Museum software-history material;
- Bitsavers and technical-manual archives;
- package/registry metadata such as deps.dev / ecosystem indexes;
- GitHub and other source repositories;
- the owner's own Digital Scrapyard / warehouse / repository estate.

Do not add all adapters before V0 proves the loop.

---

## 20. AI workers — useful roles

AI is explicitly allowed and expected where useful.

### Archaeologist
Extract candidate mechanisms from awful historical manuals, patents, archaic code, diagrams, and terminology.

### Scout
Search obscure source domains when deterministic discovery saturates.

### Translator
Normalize incompatible technical vocabularies into common function/constraint terminology.

### Mechanic
Turn a mechanism/recombination into an executable bounded prototype.

### Inventor
Generate candidate designs when deterministic recombination stalls.

### Adversary
Try to falsify the current favorite and expose missing constraints.

### Critic/Judge
Provide analysis, but remain separate from Independent Proof.

Permanent rule:

> **No AI worker certifies its own output.**

---

## 21. Jarvis / Alice / Jev findings and anti-hype rule

Research found that public "Jarvis" demonstrations often collapse multiple independent capabilities into one label:

- polished interface;
- voice interaction;
- tool execution;
- persistent state;
- memory;
- planning;
- learning;
- self-modification;
- safe self-evolution.

These are not the same capability.

A polished video does not prove autonomous learning or safe self-evolution.

Use claim states:

```text
PROVEN
IMPLEMENTED_NARROW
PROTOTYPE
ROADMAP
MARKETING_CLAIM
UNKNOWN
REJECTED
```

For every external Jarvis/Alice/agent system inspect:

- is the demo live, recreated, or unclear?
- is source available?
- are tests meaningful?
- what actions really run without approval?
- is "memory" merely transcript retrieval, embeddings, structured state, or evidence-backed revisioned memory?
- does behavior actually change from evidence?
- what can self-modification change?
- can challengers be generated, tested, independently proved, promoted and rolled back?
- what is truly local versus cloud-backed?
- what is sandboxed?
- what proof exists beyond a video?
- what license/rights obligations apply?

Strong phrases such as "AGI," "never hallucinates," "fully autonomous," "self-learning," and "self-evolving" increase the burden of proof.

### PersonalJarvis
Already heavily salvaged into Digital Scrapyard. Do not re-import the whole project.

### A.L.I.C.E.-style systems
Useful as mechanism yards for mission graphs, experience ledgers, resource accounting, revisioned learning, replaceable models, and rollback semantics. Roadmap claims must not be promoted into current capability.

### Jev / typed decision workers
Potentially useful as a specialized classification/routing/scoring worker between deterministic rules and general models. "Does not emit free-form hallucinated text" must not be interpreted as "cannot make a wrong decision." It must compete on measured task-family performance and cost.

### Other agent frameworks
OpenVoiceOS, AutoGen, LangGraph, OpenHands, Open Interpreter, Agent Zero, Letta/Mem0-style memory systems and similar projects are source yards for message buses, resumability, state checkpoints, sandboxing, approval boundaries, worker isolation, provider abstraction and memory structures. They are not reasons to replace Harness/AIOS/Foundry with another agent framework.

---

## 22. Anti-hype / evidence rule

Never equate:

- a video with a benchmark;
- a README claim with implementation;
- local UI with local intelligence;
- transcript storage with learning;
- embeddings with verified memory;
- tool calling with autonomous governance;
- code generation with self-evolution;
- CI with real-world proof;
- novelty inside the local library with novelty to humanity.

Use evidence classes and preserve uncertainty.

---

## 23. Complete operating loop

```text
OWNER OBJECTIVE
      |
      v
HARNESS
lock intent / authority / acceptance contract
      |
      v
PROBLEM COMPILER
function + constraints + environment + hard requirements
      |
      v
WISDOM REGISTRY
known winner / known failure / known resolution?
      |
  +---+---+
  |       |
known   unknown
  |       |
  |       v
  |   ARTIFACT COMPASS / SALVAGE
  |   internal + external source yards
  |       |
  |       v
  |   MECHANISM EXTRACTION
  |   deterministic first; AI archaeologist when useful
  |       |
  |       v
  |   RIGHTS / PROVENANCE
  |       |
  +---+---+
      v
MECHANISM LIBRARY
      |
      v
CANDIDATE GENERATION
exact reuse / recipe / adaptation / Missing Gear / constraint solve /
rewrite / quality diversity / evolutionary search / AI proposal
      |
      v
FOUNDRY QUARANTINE
      |
      v
BUILDER / REWRITER
      |
      v
AIOS EXECUTION
      |
      v
PROOF AMPLIFIER
      |
      v
INDEPENDENT PROOF
      |
 +----+-----+
 |          |
REJECT    CERTIFY
 |          |
 v          v
REJECTION  RUNTIME ASSURANCE / CANARY
MEMORY          |
           +----+----+
           |         |
         worse     better
           |         |
        rollback   promote
           |         |
           +----+----+
                v
          NEW GENERATION
                |
                v
        EXPERIENCE / WISDOM /
        REGRESSION / LINEAGE
                |
                +------> NEXT ITERATION
```

---

## 24. Strict meaning of self-evolving

Salvage Foundry is self-evolving only when previous evidence measurably changes future behavior in a useful way.

Not sufficient:

- storing transcripts;
- increasing prompt context;
- installing another plugin;
- changing configuration without proof.

Valid example:

```text
old route: large model repair
-> same defect family solved repeatedly
-> machine extracts deterministic rewrite
-> rewrite is regression-tested and independently proved
-> rewrite becomes preferred route
-> future instances bypass expensive model
```

Another valid example:

```text
incumbent A
-> historical recombination B
-> B proves lower energy under same required reliability
-> bounded field trial remains stable
-> B promoted
-> A retained as rollback
-> conditions and evidence stored
```

---

## 25. What the machine should accumulate

Durable knowledge classes:

- rule memory;
- resolution memory;
- winner/wisdom memory;
- rejection memory;
- failure/regression corpus;
- route-performance memory;
- cost memory;
- incompatibility/constraint memory;
- security memory;
- rights memory;
- provenance memory;
- proof memory;
- mechanism lineage;
- environment/validity conditions.

Failure is also learning: rejected candidates should produce minimal reproducers, constraints, regression tests, lineage penalties, and lessons where justified.

---

## 26. Novelty boundary

Separate:

```text
LIBRARY_NOVEL
SEARCH_NOVEL
PRIOR_ART_UNKNOWN
KNOWN_PRIOR_ART
INDEPENDENT_REDISCOVERY
```

Never promote "new to our mechanism graph" into "new to humanity" without dedicated prior-art proof.

---

## 27. Minimum implementation artifacts

Do **not** create a Salvage Foundry monolith.

Minimum additions after this handover is selected for implementation:

### Harness Card
- `SALVAGE_FOUNDRY_CONTRACT.md` (or equivalent canonical governance contract)
- `state/SALVAGE_FOUNDRY_WISDOM.jsonl` or another append-oriented wisdom format

### Digital Scrapyard
- Mechanism Card schema v0
- Constraint Fingerprint taxonomy v0
- mechanism seed library
- Missing Gear extension only where needed
- external-source adapters only after V0

### Foundry
- candidate experiment contract
- disposable incumbent/challenger runner
- candidate certificate schema

### AIOS
- runtime measurement/correlation interface as needed

### Independent Proof
- independent certificate verifier

### Workshop
- readable summary of what was tried, source, match reason, contestants, winner, proof, rights, cost, lineage, rollback, and owner action required

---

## 28. V0 — prove the loop before scaling

Keep V0 deliberately small.

Suggested target:

- 100–500 deliberately diverse Mechanism Cards;
- at least ten engineering domains;
- roughly ten modern constrained problems;
- one transparent deterministic incumbent/challenger experiment through the existing Foundation proof chain.

For each problem:

```text
compile function + constraints
-> retrieve historical analogues
-> explain why each matched
-> generate/recombine candidates
-> rank transparently
-> build strongest bounded candidate
-> test
-> prove
-> record winner/failure evidence
-> repeat the same problem
```

Central V0 proof target:

> **The second run makes a measurably better decision because of evidence produced by the first run.**

If that is not demonstrated, do not claim self-evolution.

---

## 29. V0 acceptance contract

V0 does not pass unless:

1. Mechanism cards have traceable provenance.
2. Rights state is explicit.
3. Deterministic lanes are reproducible for identical inputs/configuration/seed where applicable.
4. Known relationships cannot masquerade as discoveries.
5. Unrelated artifacts remain isolated rather than forced into fake combinations.
6. Hard constraints cannot be traded away for a higher fitness score.
7. Candidate cannot modify its own authority rules, acceptance tests or proof boundary.
8. Every promoted candidate has independent evidence.
9. Failed candidates remain in rejection/failure memory.
10. Wisdom records environment and validity conditions.
11. Material environment changes trigger revalidation/invalidation.
12. Previous proven generation remains recoverable.
13. Second-run improvement is measurable.
14. No global novelty claim is made without prior-art evidence.
15. AI-produced candidates receive no greater authority than deterministic candidates.

---

## 30. Implementation order

When the owner explicitly promotes this project from queued research into active work, the next worker should:

1. Read `state/CURRENT_PROJECT.json` and current authority first.
2. Resolve canonical Artifact Compass / Artifact Salvage / Missing Gear / Rights Gate / Proof Gate sources.
3. Treat **this file** as the canonical Salvage Foundry research handover.
4. Draft the minimum Salvage Foundry governance contract; do not add another orchestration framework.
5. Define Mechanism Card schema v0.
6. Define Constraint Fingerprint taxonomy v0.
7. Define Wisdom Record schema v0.
8. Select 100–500 seed mechanisms from diverse sources including the existing estate.
9. Select ~10 constrained modern problems.
10. Extend Missing Gear only as necessary for mechanism cards / constraint fingerprints.
11. Build one deterministic incumbent/challenger experiment.
12. Execute it through Foundry/AIOS.
13. Independently prove the result.
14. Record winner and failure evidence.
15. Repeat the identical problem.
16. Prove stored evidence beneficially changes the second decision.
17. Stop and review before adding autonomous crawling, model swarms, deployments, or UI work.

---

## 31. Locked exclusions

Until V0 proves the loop:

- do not create another OS;
- do not replace Harness;
- do not replace Foundry/AIOS/Independent Proof;
- do not import an entire Jarvis/Alice agent framework;
- do not reopen PersonalJarvis as an architecture project;
- do not build a giant UI;
- do not crawl the entire internet;
- do not grant AI workers promotion authority;
- do not allow the candidate to edit its proof boundary;
- do not enable autonomous deployment/spending;
- do not call local-library novelty global novelty;
- do not claim self-evolution until second-run improvement is measured.

---

## 32. Main laws

**Engineering law**  
Recover the mechanism. Match the constraint. Test the descendant. Keep the evidence.

**Economic law**  
Never pay intelligence twice for a problem the machine has already learned to solve mechanically.

**AI law**  
AI discovers. Salvage Foundry mechanizes.

**Authority law**  
The thing capable of evolving is never the thing holding ultimate authority over its own evolution.

**Promotion law**  
Nothing becomes stronger merely because it is new. It must beat what the machine already has under declared constraints, survive rights/safety gates, carry evidence, preserve rollback, and leave behind permanent knowledge of the contest.

---

## 33. Handover status

**Research:** working saturation reached.  
**Theory:** technically plausible and grounded in mature engineering mechanisms.  
**Integrated Salvage Foundry:** not yet implemented/proven.  
**Existing prerequisites:** substantial portions already exist across Harness Card, Digital Scrapyard, Foundry, AIOS and Independent Proof.  
**Main missing gear:** a general **Mechanism Card -> incumbent/challenger -> independent certificate -> promotion/rollback -> Wisdom** loop.  
**Next action:** bounded V0 experiment when owner explicitly promotes this queued research project.

Do not ask the owner to reconstruct this idea from prior chat. Use this document.