# AI Builder Think Tank — 2026-10-04

Purpose: preserve the deep-research pass derived from the YouTube video `AI Just Exploded: GPT-7 BEL, 99% AGI, Gemini 4 RSI, Alien Mind, JEV` and the primary-source research traced outward from its claims.

Source video:

https://www.youtube.com/watch?v=dk-hx4_cqpk

Captured: 2026-10-04/05 UTC.

This is **research evidence, not automatic authority**. Nothing in this file changes Harness rules, Foundation authority, owner gates, model routing, or FRIDAY runtime behavior by itself. Any mechanism below must still pass the existing Harness sequence: candidate -> bounded test -> independent proof -> deliberate promotion.

## Method and limits

The video is approximately 1 hour 43 minutes and acts as a compilation of several current AI-news threads: alleged BEL/GPT-7 leaks, GPT-6 Astra/ARC-AGI-3 results, Gemini 4/RSI rumors, Jakub Pachocki's "alien mind" argument, recursive self-improvement research, automated AI research, and Jev.

YouTube did not expose a clean complete timestamped transcript through the available extraction path during this pass. The research therefore did **not** pretend to perform a verbatim line-by-line transcript audit. Instead it recovered the video structure, identified the major claims, and traced those claims outward into primary papers, lab posts, technical reports, benchmark writeups, engineering posts, and current model/research artifacts.

The main research rule used here:

> Treat the video as an index of claims, not as evidence that the claims are true.

## Executive finding

The strongest current work is not converging on "one infinitely smart model that does everything." It is converging on **systems around models**:

- persistent and selective context;
- harnesses;
- replay/history;
- tools;
- skills;
- agent loops;
- multiple candidate branches;
- hidden/held-out evaluation;
- independent verification;
- sandboxed execution;
- selective human authority;
- cheap deterministic routing before expensive reasoning;
- recursive improvement of the system surrounding the model.

That direction is materially relevant to Foundation/FRIDAY because the machine is already organized around governance, bounded building, runtime execution, a user control surface, salvage/reuse, proof receipts, and sanitized learning.

The core architectural interpretation is:

> The intelligence of the machine is not equal to the intelligence of the model.

A more useful framing is:

`MACHINE CAPABILITY ~= MODEL x MEMORY x CONTEXT x TOOLS x HARNESS x SEARCH x VERIFICATION x ENVIRONMENT`

The strongest near-term opportunity for FRIDAY is therefore not to chase every frontier-model rumor. It is to improve the **repeatable system that chooses, uses, verifies, and learns from mechanisms**.

---

# 1. Video claim triage

## BEL / GPT-7 leak

**Status: UNVERIFIED LEAK / CLAIMED**

The video presents BEL as a massive internal OpenAI model and potential GPT-7 foundation, with extraordinary parameter-count claims.

Research verdict:

- A post-Astra internal OpenAI model can plausibly exist and current OpenAI work clearly includes newer internal research systems.
- The specific BEL identity, GPT-7 branding, parameter count, and capability claims were not established strongly enough by primary evidence to promote them beyond leak/rumor status.
- Do not build FRIDAY architecture around an alleged model name or alleged size.

What is useful underneath the rumor is the **process** visible in current OpenAI research: large-scale RL, multi-agent decomposition, parallel exploration, staged difficulty, tool use, and feeding successful intermediate discoveries back into later research.

## GPT-6 Astra "99% AGI"

**Status: REAL BENCHMARK RESULT / MISLEADING LABEL**

ARC Prize reported that Astra achieved a 99.9% result on the ARC-AGI-3 Semi-Private evaluation using a provider-specific harness, while a standard harness scored far lower.

Primary source:

https://arcprize.org/blog/astra

Research interpretation:

- The result is real benchmark evidence.
- "99% AGI" is not a valid interpretation. ARC-AGI is an evaluation of aspects of generalization and adaptation, not a declaration that a system is 99% of the way to AGI.
- The more important finding for FRIDAY is the performance difference caused by the **harness**.

Reported comparison in the ARC Prize writeup:

- standard harness: approximately 62.7%;
- provider harness: approximately 99.9%;
- on shared solved cases, the provider setup was also substantially faster and used materially fewer tokens.

This is strong evidence that state preservation, compaction, tool/context handling, and orchestration architecture can change observed capability dramatically without changing the underlying task definition.

## Gemini 4 RSI

**Status: UNCONFIRMED LEAK / IDENTITY UNKNOWN**

The video's specific Gemini 4 RSI identity and benchmark claims were not sufficiently grounded in primary evidence during this pass.

Do not promote the leak.

The better research target is the real current recursive-self-improvement literature, especially Dream-RSI and ModularRSI.

## Jakub Pachocki — "An Alien Mind"

**Status: CONFIRMED**

Primary source:

https://openai.com/index/an-alien-mind/

Pachocki explicitly uses the "alien mind" framing and traces current reasoning systems through reinforcement learning, increasingly capable computer interaction, scientific work, collaborative systems, and the possibility that AI begins materially improving the process used to build later AI systems.

The useful takeaway is not mysticism. It is that capability improvements may be **qualitative**, not only smooth quantitative scaling, and the evaluation/control system needs to be ready for behaviors that were not directly hand-designed.

## AI improving AI

**Status: CONFIRMED IN BOUNDED FORMS**

Current work demonstrates AI systems improving:

- agent harnesses;
- search/exploration policies;
- coding agents;
- post-training recipes;
- tool-use strategies;
- evaluation strategies;
- research workflows;
- model-training processes.

This should not be described as proven uncontrolled runaway self-replication. The credible current pattern is **bounded recursive improvement under an evaluation environment**.

## Jev

**Status: REAL / MATERIAL ALTERNATIVE PATTERN**

Jev is important less as a replacement for language models than as an attack on an assumption: not every intelligent system action needs to generate open-ended text.

Relevant reporting:

https://www.wsj.com/tech/ai/startup-typesafe-ais-jev-model-sparks-copycats-talk-of-llm-alternatives-e39ff57d

The useful FRIDAY lesson is to separate:

- open-ended reasoning/generation;
- typed decisions;
- classification/routing;
- calibrated confidence;
- deterministic policy.

If FRIDAY only needs `ALLOW / DENY / ROUTE / RETRY / STOP / SELECT`, a giant generative model may be the wrong mechanism.

---

# 2. Think-tank roster

"Profile" below means public research/problem-solving style inferred from published work and statements. It is **not** a clinical psychological diagnosis.

## Jakub Pachocki — frontier reasoning / large-scale RL

Role in think tank: **Frontier Reasoner**

Observed style:

- scale experiments until qualitative capability changes appear;
- use reinforcement learning to turn pretrained knowledge into longer-horizon reasoning behavior;
- pay attention to discontinuities, not only benchmark averages;
- treat unexpected capability as both useful evidence and a control/safety problem;
- view advanced systems as increasingly able to participate in research itself.

FRIDAY question:

> What becomes possible if the reasoning loop itself improves, and what proof/control must exist before relying on that new behavior?

Primary source:

https://openai.com/index/an-alien-mind/

## Noam Brown — search, games, self-play, decomposition

Role: **Strategist**

Observed style:

- strategic search;
- self-play;
- game-theoretic reasoning;
- decomposition into interacting agents/roles;
- use of environment feedback instead of pure next-token generation;
- parallel exploration where useful.

FRIDAY question:

> Which parts of this problem can be searched, branched, or attacked in parallel instead of betting everything on one solution path?

Historical research lineage includes poker and Diplomacy systems; current public OpenAI comments have emphasized recursive self-improvement as a high-priority direction.

Relevant public forum/video context:

https://forum.openai.com/en/public/videos/ai-economics-in-the-forum-2025

## Francois Chollet — novelty, generalization, benchmark skepticism

Role: **Generalization / Bullshit Detector**

Observed style:

- distinguishes skill from intelligence;
- asks how efficiently a system acquires new skill under novelty;
- distrusts benchmark memorization and overfitting;
- values explicit refinement and search;
- emphasizes hidden/generalization evidence.

FRIDAY question:

> Did the machine learn a reusable capability, or did we merely teach it this exact test?

Foundational paper:

https://arxiv.org/abs/1911.01547

## Jeff Clune — open-ended search and AI-generating algorithms

Role: **Evolution Architect**

Observed style:

- stop hand-designing every final component;
- design processes capable of generating better processes;
- preserve diversity;
- retain stepping stones that may look locally worse but enable later breakthroughs;
- evaluate whole adaptive systems rather than only static models.

FRIDAY question:

> Why are we continually rewriting one incumbent when we could preserve a family tree of proven alternatives and let evidence select among them?

Primary paper:

https://arxiv.org/abs/1905.10985

## Dario Amodei — scaling plus verification/control discipline

Role: **Risk Governor**

Observed style:

- scaling-oriented empiricism;
- operational control;
- interpretability and monitoring;
- concern that capability can improve faster than institutions/evaluators can safely absorb;
- emphasizes pacing and governance at the frontier.

FRIDAY question:

> Can our ability to evaluate and control this new capability keep pace with our ability to create it?

Relevant essay:

https://darioamodei.com/post/we-must-pace-the-frontier

## Diogo Almeida / TypeSafe AI / Jev — calibrated machine decisions

Role: **Decision Engineer**

Observed style:

- rejects the assumption that all machine intelligence should communicate via prose;
- separates decision systems from generative language systems;
- values structured outputs, typed actions, calibration, and efficiency.

FRIDAY question:

> Why are we spending expensive model reasoning here when the machine only needs a bounded decision?

Relevant reporting:

https://www.wsj.com/tech/ai/startup-typesafe-ais-jev-model-sparks-copycats-talk-of-llm-alternatives-e39ff57d

## Dream-RSI team — historical replay as an improvement environment

Role: **Replay Architect**

Observed style:

- treat the history of a discovery/search process as an environment;
- replay alternatives cheaply against previously observed trajectories;
- improve exploration policy before paying for new real-world execution;
- feed new real runs back into the replay environment.

FRIDAY question:

> What can we learn by replaying new policies against old receipts before spending another real execution?

Paper:

https://arxiv.org/abs/2609.14858

## ModularRSI team — evolve the harness by component

Role: **Harness Engineer**

Observed style:

- separate agent behavior into modules;
- compare success/failure trajectories across tasks;
- improve modules independently;
- recombine only after evidence;
- reduce benchmark-specific overfitting.

Paper's useful decomposition:

- agent loop;
- tool use;
- observation management;
- context management;
- task completion detection.

FRIDAY question:

> Which exact module is failing? Do not redesign the entire machine until we know.

Paper:

https://arxiv.org/abs/2609.14857

## ScienceBuddy team — nested improvement loops

Role: **Learning Engineer**

Observed style:

- one loop improves the agent/harness;
- another loop improves the underlying learned system;
- real user interactions can produce evaluation tasks/rubrics;
- feedback becomes structured evidence rather than raw unquestioned memory.

FRIDAY question:

> Can owner interaction become a sanitized evaluation candidate rather than automatically becoming a permanent rule?

Paper:

https://arxiv.org/abs/2609.17523

## AIDE2 team — self-modification with hidden evaluation

Role: **Self-Improvement Tester**

Observed style:

- make the research agent's own implementation an optimization target;
- propose code/system changes automatically;
- evaluate against hidden tasks;
- reject most changes;
- require generalization rather than local benchmark gaming.

FRIDAY question:

> Can FRIDAY propose modifications to herself while an independent evaluator—not the proposer—decides whether the change survives?

Paper:

https://arxiv.org/abs/2609.26457

## A-Evolve team — automated post-training and metric skepticism

Role: **Metric Skeptic**

Observed style:

- automated multi-round training/improvement;
- close loop between evaluation and training strategy;
- detect when the current metric is no longer a good proxy;
- change search strategy rather than blindly maximizing a misleading score.

FRIDAY question:

> Is the thing we are optimizing still the same thing the owner actually cares about?

Paper:

https://arxiv.org/abs/2606.20657

## Meta Capacity Efficiency engineering team — stable tools + composable skills

Role: **Production Engineer**

Observed style:

- standardized tool interfaces;
- reusable skills;
- context gathering;
- diagnosis;
- candidate repair;
- validation;
- human review for consequential outputs;
- reuse expert procedures across many workflows.

FRIDAY question:

> Is this a recurring expert procedure that should become a skill over stable tools instead of another one-off agent architecture?

Engineering post:

https://engineering.fb.com/2026/04/16/developer-tools/capacity-efficiency-at-meta-how-unified-ai-agents-optimize-performance-at-hyperscale/

---

# 3. Combined problem-solving doctrine

When the above research styles are collapsed into mechanisms instead of personalities, the think tank behaves like this:

1. **Define the real outcome, not the current implementation.**
2. **Separate novelty/generalization from memorized skill.**
3. **Identify the exact failing module.**
4. **Ask whether deterministic logic or a typed decision is enough before invoking generative intelligence.**
5. **Generate multiple genuinely different mechanisms when uncertainty is high.**
6. **Preserve useful alternatives instead of deleting every loser immediately.**
7. **Replay candidate policies against historical receipts before expensive execution.**
8. **Execute promising candidates in isolated environments.**
9. **Use hidden/held-out evaluation so the candidate cannot optimize directly against every test.**
10. **Require independent proof; the proposer cannot be the sole judge.**
11. **Attack the metric itself when optimization and user outcome diverge.**
12. **Promote only the mechanism that proves better under unseen evidence and acceptable cost.**
13. **Downshift repeated success into a rule, script, cache, skill, typed decision model, or smaller mechanism.**
14. **Keep owner authority for genuinely consequential boundaries.**

This strongly aligns with existing Foundation principles:

- current verified truth over stale memory;
- rules before work;
- proof before promotion;
- candidate != commitment;
- AI-last / cheapest capable mechanism;
- bounded execution;
- owner authority, not owner labor;
- sanitized learning rather than raw chat ingestion;
- complexity may exist underneath FRIDAY but should not leak into the owner experience.

---

# 4. Current training / improvement mechanism map

This section is intentionally broader than the specific video. It captures the current technique families that appeared repeatedly in the traced research.

## Pretraining

Purpose: acquire broad representations and priors from large corpora.

FRIDAY use: consume existing pretrained models; do not attempt frontier-scale pretraining locally.

## Reinforcement learning / reinforcement learning with verifiable rewards

Purpose: teach models to search, reason, act, or optimize trajectories using outcome feedback rather than imitation alone.

FRIDAY use: mainly upstream via model providers. Locally, borrow the **structure**: candidate action -> measurable outcome -> reward/evidence -> policy update.

## Preference learning / RLHF-style alignment

Purpose: align behavior to human preference signals.

FRIDAY use: useful for subjective personal preferences, but subjective preference must remain separate from technical truth/proof.

## Self-play

Purpose: generate increasingly difficult challenges/opponents/tasks without requiring a human to author every example.

FRIDAY use: strong candidate for planner-vs-critic, builder-vs-attacker, or permission/policy adversarial testing.

## Test-time search / refinement loops

Pattern:

`generate -> evaluate -> refine -> repeat`

FRIDAY use: very high value. Candidate generation without iterative evaluation is wasteful; evaluation without another repair loop wastes information.

ARC Prize research has increasingly highlighted refinement as a major current reasoning paradigm.

Reference:

https://arxiv.org/abs/2601.10904

## Harness evolution

Purpose: improve the system around the model—context, tools, agent loop, memory, completion rules—without necessarily changing weights.

FRIDAY use: extremely high value and probably the correct near-term center of gravity.

## Replay-based policy improvement

Purpose: learn from stored search/discovery trajectories before paying to execute new trajectories.

FRIDAY use: extremely high value. Existing receipts, incidents, workflow traces, and candidate outcomes can become replay material.

## Recursive code/system improvement

Purpose: agent proposes modifications to its own orchestration, code, or research process.

FRIDAY use: allowed only in isolated candidate lanes with independent proof and explicit promotion boundaries.

## Hidden/private evaluation

Purpose: prevent self-improving systems from simply gaming visible tests.

FRIDAY use: mandatory before any serious recursive self-improvement mechanism is trusted.

## Quality-diversity / open-ended search

Purpose: preserve diverse promising candidates rather than greedily keeping one current winner.

FRIDAY use: Scrapyard can become a candidate genealogy: mechanism, parent, evidence, cost, failures, useful traits, and retirement reason.

## Multi-agent branching

Purpose: explore alternative hypotheses, decompositions, attacks, and synthesis in parallel.

FRIDAY use: selectively valuable for hard uncertainty; should not become default token-burning theater.

## Sandboxed/stateful agent environments

Purpose: give agents isolated environments for multi-step tool interaction, coding, experimentation, and rollback.

FRIDAY use: copy the lifecycle/authority pattern, not hyperscale infrastructure.

Related DeepSeek infrastructure paper:

https://arxiv.org/abs/2609.22978

## Calibrated decision models / typed decision systems

Purpose: make bounded machine decisions without open-ended generation.

FRIDAY use: excellent for routing, admission, risk classification, budget decisions, retry/stop choices, and proof-state classification when deterministic rules alone are insufficient.

## User interaction -> eval generation

Purpose: convert real user corrections and failures into future evaluation tasks, not unquestioned permanent memory.

FRIDAY use: directly relevant to the sanitized learning intake.

## Automated research loops

Pattern:

`hypothesis -> code -> experiment -> evidence -> critique -> next hypothesis`

FRIDAY use: future Foundry direction once the current automation/proof spine is complete and promotion remains controlled.

## Metric correction

Purpose: detect when the metric being optimized stops representing the real goal.

FRIDAY use: add a recurring challenge to Proof Gate: "Does this score still predict the owner's actual outcome?"

---

# 5. High-signal papers / research corpus

## Dream-RSI — Recursive Self-Improvement through Evolving Worlds

https://arxiv.org/abs/2609.14858

Key mechanism:

- historical discovery tree becomes a replay environment;
- many exploration strategies can be tested cheaply;
- promising policy is selected for real execution;
- new execution expands the replay world.

FRIDAY salvage:

`RECEIPTS -> REPLAY ENVIRONMENT -> CANDIDATE POLICY BAKE-OFF -> ONE REAL RUN`

## ModularRSI — Modular and Generalizable Recursive Harness Self-Improvement

https://arxiv.org/abs/2609.14857

Key mechanism:

- separate harness into modules;
- compare successful and failed trajectories;
- improve modules independently;
- integrate only after evidence.

FRIDAY salvage:

Keep FRIDAY one owner-facing experience while preserving measurable internal boundaries.

## ScienceBuddy — Recursive-in-Recursive Self-Improvement

https://arxiv.org/abs/2609.17523

Key mechanism:

- nested loops improve harness and learning system;
- interaction-derived tasks/evals become part of the improvement pipeline.

FRIDAY salvage:

Owner correction -> sanitized generalized candidate -> eval -> proof -> possible rule/skill promotion.

## AIDE2 — Recursive Self-Improvement of AI Research Agents

https://arxiv.org/abs/2609.26457

Key mechanism:

- agent code itself becomes an optimization target;
- automatic proposals compete;
- hidden evaluation determines survival;
- changes must generalize.

FRIDAY salvage:

Create a **Shadow FRIDAY** lane for self-modification candidates. The candidate never has authority to promote itself.

## A-Evolve-Training

https://arxiv.org/abs/2606.20657

Key mechanism:

- automated multi-round post-training/research loop;
- system can recognize that the current metric is becoming misleading and change search strategy.

FRIDAY salvage:

Proof Gate must be allowed to challenge the fitness function, not merely maximize it.

## The Last AI Built by Humans

https://arxiv.org/abs/2609.11873

Useful as a maturity map rather than a direct implementation recipe.

Possible autonomy progression:

1. improvement-execution autonomy;
2. improvement-strategy autonomy;
3. experience acquisition;
4. environment adaptation;
5. recursive meta-improvement.

FRIDAY interpretation:

Do not skip levels. Current bounded automation work is closer to improvement-execution autonomy than to unrestricted strategy/meta-improvement.

## Darwin Godel Machine

https://arxiv.org/abs/2505.22954

Key mechanism:

- self-modifying coding agent;
- empirical evaluation;
- archive of diverse agents instead of one irreversible lineage.

FRIDAY salvage:

Candidate family tree in Scrapyard. Preserve evidence and parentage of alternatives.

## AI-Generating Algorithms

https://arxiv.org/abs/1905.10985

Key idea:

Shift effort from hand-designing each final intelligent system toward designing systems that can generate and evaluate better intelligent systems.

FRIDAY salvage:

Foundry should eventually manufacture tested mechanisms, while Harness remains the governing authority.

## ARC Prize refinement-loop work

https://arxiv.org/abs/2601.10904

Key mechanism:

`alternative generation -> verification -> feedback -> refinement`

FRIDAY salvage:

Treat one-pass answers as candidates when stakes/uncertainty justify iterative search.

## DeepSeek Elastic Compute / agent environments

https://arxiv.org/abs/2609.22978

Key mechanism:

Large-scale stateful isolated environments for agent experimentation.

FRIDAY salvage:

Use local/CI sandbox contracts and lifecycle boundaries; ignore hyperscale implementation unless scale later becomes real.

---

# 6. Primary current industry / lab evidence

## OpenAI — An Alien Mind

https://openai.com/index/an-alien-mind/

Relevance:

- reasoning through RL;
- increasingly broad computer/research action;
- qualitative capability shifts;
- expectation that AI contributes materially to later AI research.

## OpenAI — Navier-Stokes research

https://openai.com/index/navier-stokes-solution/

Useful process evidence:

- large-scale RL on top of pretrained systems;
- multiple agents/approaches;
- staged easier subproblems;
- feed intermediate discoveries forward;
- swap in stronger systems when available;
- very large parallel research effort.

FRIDAY interpretation:

The process matters more than rumored model labels: decompose, branch, preserve intermediate wins, synthesize, independently verify.

## OpenAI — research acceleration / agent work

https://openai.com/index/research-acceleration-view-inside-openai/

Research interpretation:

Frontier research increasingly uses large amounts of agent work per human workday, often concurrently, but high-level direction remains heavily human-driven.

FRIDAY implication:

> Human judgment aims the machine; machine labor should carry the mechanical workload.

This aligns with:

**Owner authority, not owner labor.**

## ARC Prize — Astra

https://arcprize.org/blog/astra

Key lesson:

Harness/context architecture can massively alter task performance.

FRIDAY implication:

Continuation capsules, state recovery, tool interfaces, compaction, and completion detection are not merely plumbing. They are part of observed intelligence.

## Meta Engineering — unified AI agents for capacity efficiency

https://engineering.fb.com/2026/04/16/developer-tools/capacity-efficiency-at-meta-how-unified-ai-agents-optimize-performance-at-hyperscale/

Key lesson:

Stable tools plus reusable expert skills plus automated context/diagnosis/candidate validation is a production pattern, not merely a research idea.

FRIDAY implication:

This supports skill registry + stable tool contracts + bounded proof rather than inventing a new universal architecture for every task.

---

# 7. Think-tank response to a real FRIDAY problem

Example problem:

> Local voice is too slow on the old PC.

The merged think-tank does not immediately ask, "Which faster model should we install?"

It asks:

**Chollet lens** — What is the real objective? Fast neural synthesis, or fast perceived response from FRIDAY?

**Jev/Almeida lens** — Does this stage require generative intelligence at all?

**Brown lens** — Which parts can be decomposed and tested in parallel?

**Clune lens** — Generate truly different solution families; preserve useful alternatives.

**Dream-RSI lens** — What old runs/benchmarks can be replayed before another expensive test?

**ModularRSI lens** — Which module is slow: startup, ASR, reasoning, synthesis, routing, disk, or completion behavior?

**Meta lens** — Is the solution a reusable expert procedure/skill over existing tools?

**AIDE2 lens** — Can candidate pipeline changes compete under hidden tests?

**A-Evolve lens** — Is latency the only correct metric, or do intelligibility, owner effort, RAM, startup, and failure recovery matter too?

**Pachocki lens** — Would stronger reasoning/search create a qualitatively different architecture?

**Amodei lens** — Does the proposed automation add capability faster than the current evaluator can control?

**Harness** — Which candidate actually proved better, at acceptable cost, without violating authority?

This is superior to a generic instruction such as "use Sol and think harder." It creates **problem-solving lenses with explicit jobs**.

---

# 8. Direct salvage for Foundation / FRIDAY

## 8.1 Receipt Replay — from Dream-RSI

Candidate concept:

Turn durable historical receipts, incidents, attempted fixes, denials, job correlations, performance benchmarks, and proof outcomes into a replay corpus.

Before changing live behavior, evaluate a candidate policy against previous cases:

- what would it have classified differently?
- where would it have stopped earlier?
- where would it have spent more?
- would it have violated an owner gate?
- would it have produced a false proof claim?
- would it have repeated a known failure?

Potential flow:

`HISTORICAL RECEIPTS -> SANITIZED REPLAY CASES -> CANDIDATE POLICY -> DIFFERENTIAL REPORT -> ONLY THEN REAL TEST`

Status: **RESEARCH CANDIDATE, NOT IMPLEMENTED.**

## 8.2 Evolvable FRIDAY modules — from ModularRSI

Do not evolve "FRIDAY" as one undifferentiated prompt.

Possible independently measurable modules:

- intent recovery;
- current-state recovery;
- authority classification;
- routing / mechanism selection;
- context selection;
- tool selection;
- candidate generation;
- completion detection;
- proof interpretation;
- learning extraction;
- owner interruption decision.

Keep repo/component boundaries where they help measurement and authority. Unify the **experience**, not necessarily implementation storage.

Status: **RESEARCH CANDIDATE.**

## 8.3 Shadow FRIDAY — from AIDE2

Allow FRIDAY/Sol to propose changes to orchestration code, skills, rules, prompts, or routing only inside an isolated candidate lane.

Requirements:

- candidate cannot promote itself;
- hidden/held-out eval set;
- incumbent-vs-candidate comparison;
- cost/latency/owner-interruption metrics;
- policy/authority regression tests;
- independent proof worker;
- explicit rejection record for losers;
- rollback/recovery path.

Status: **RESEARCH CANDIDATE.**

## 8.4 Candidate family tree — from Darwin Godel Machine / quality-diversity work

Scrapyard could preserve:

- candidate ID;
- parent mechanism;
- mutation/change;
- task class;
- proof result;
- hidden-eval result;
- compute/cost;
- owner interruption count;
- strengths;
- failure modes;
- retirement reason;
- reusable submechanisms.

This prevents "failed overall" from meaning "delete every useful idea inside it."

Status: **RESEARCH CANDIDATE.**

## 8.5 Stable tools, evolving skills — from Meta

Prefer:

- stable bounded tool interfaces;
- reusable expert procedures;
- small, testable skills;
- routing based on task type;
- independent validation.

Avoid:

- giant always-loaded meta-prompts;
- new tool stacks when a current interface suffices;
- agent swarms for routine tasks;
- replacing deterministic rules with expensive reasoning.

Status: **SUPPORTING RESEARCH EVIDENCE for existing Harness direction.**

## 8.6 Intelligence ladder — from Jev + cost/complexity logic

Suggested mechanism ladder:

1. deterministic rule;
2. cache / previous proven result;
3. typed decision / lightweight classifier;
4. cheap/small model;
5. Sol-level reasoning;
6. Astra / deep or multi-agent reasoning only when justified.

Status: **RESEARCH CANDIDATE / aligns with existing AI-last principle.**

## 8.7 Interaction-to-evaluation — from ScienceBuddy

Owner correction should not directly become machine law.

Safer sequence:

`OWNER CORRECTION -> GENERALIZED NON-SENSITIVE CANDIDATE -> TEST CASE/RUBRIC -> REPLAY/REAL PROOF -> RULE/SKILL PROMOTION IF EARNED`

Status: **Strongly aligned with current sanitized learning intake.**

## 8.8 Preserve reasoning state — from ARC/Astra

The context/harness difference in ARC evidence implies that state handling is a first-class capability variable.

FRIDAY should treat these as performance-critical:

- current project authority;
- job identity;
- prior successful proof;
- continuation capsule;
- context compaction;
- relevant-vs-irrelevant state selection;
- completion detection;
- restart recovery.

Status: **SUPPORTING RESEARCH EVIDENCE for existing continuation/recovery direction.**

## 8.9 Challenge the metric — from A-Evolve

Proof Gate should periodically ask:

> Does this metric still represent the owner's real goal?

Examples:

- latency while intelligibility gets worse;
- pass rate while owner interruption increases;
- benchmark score while permissions expand;
- fewer tokens while recovery reliability degrades;
- CI green while live user path remains broken.

Status: **RESEARCH CANDIDATE.**

## 8.10 Independent evaluator authority

The system proposing the improvement must never be the only system deciding that the improvement is safe/proven.

Required separation:

`PROPOSER != FINAL PROOF AUTHORITY`

This is consistent with existing Harness proof gates and becomes non-negotiable for self-modification.

Status: **Strong supporting research for existing Harness architecture.**

---

# 9. Suggested new research law candidate

Do **not** automatically promote this into Harness rules from this document alone.

Candidate wording:

> **SELF-IMPROVEMENT MUST OUTPERFORM ITS PARENT ON UNSEEN EVIDENCE.**

Interpretation:

A self-improvement candidate should not survive merely because:

- visible tests pass;
- the proposing model says it is better;
- it solved the exact task it was designed against;
- a PR merged;
- one benchmark improved.

A serious improvement candidate should demonstrate better or at least non-regressed behavior on held-out/unseen cases while remaining inside acceptable cost, latency, permission, safety, and owner-interruption budgets.

Source lineage:

- Chollet / generalization framing;
- AIDE2 hidden evaluation;
- ModularRSI generalizable harness improvement;
- existing Harness proof-before-promotion law.

Status: **CANDIDATE ONLY. Requires bounded proof before promotion.**

---

# 10. Proposed think-tank lenses for FRIDAY

These are not eleven always-running personas. They are **selective reasoning lenses**.

- **CHOLLET LENS — Define the real problem / test novelty.**
- **BROWN LENS — Search, decompose, parallelize.**
- **CLUNE LENS — Preserve diversity and stepping stones.**
- **PACHOCKI LENS — Push reasoning when stronger reasoning may change the solution space.**
- **JEV / ALMEIDA LENS — Remove unnecessary generation; prefer bounded decisions.**
- **MODULAR-RSI LENS — Locate the failing module before redesign.**
- **DREAM-RSI LENS — Replay before spending.**
- **AIDE2 LENS — Evolve candidates under hidden tests.**
- **A-EVOLVE LENS — Attack the metric itself.**
- **META LENS — Turn repeated expertise into reusable skills over stable tools.**
- **AMODEI LENS — Attack the safety/control assumption.**
- **HARNESS — Decide what is allowed to survive.**

Routing rule candidate:

> Do not invoke every lens. Select only the smallest set capable of reducing the current uncertainty.

This preserves the existing Harness idea that passes/skills must earn their cost.

---

# 11. Where Foundation currently maps on an RSI maturity ladder

Research-derived interpretation only; not a new canonical project state.

Foundation/FRIDAY currently demonstrates elements of **bounded improvement-execution autonomy**:

- deterministic control policy exists;
- bounded candidate work can be created/tested;
- independent proof exists in some paths;
- receipts can be persisted/recovered;
- sanitized learning candidates exist;
- owner gates remain explicit.

It is **not proven** as:

- general autonomous work admission across all task classes;
- autonomous improvement-strategy selection;
- autonomous experience acquisition across arbitrary environments;
- general recursive self-modification;
- automatic promotion of new authority;
- unrestricted self-directed learning.

The correct interpretation is:

> Build the evaluation cage before releasing the evolutionary mechanism into it.

Do not import "self-improving AI" language as permission to let FRIDAY rewrite and promote herself without hidden evaluation and owner-governed proof.

---

# 12. What not to copy from frontier labs

Do not cargo-cult:

- enormous agent swarms;
- frontier-scale pretraining;
- giant GPU infrastructure;
- every new benchmark;
- every rumored model;
- multi-agent debate for simple deterministic tasks;
- self-modification without held-out evals;
- raw private interaction ingestion;
- auto-promotion of rules because a model generated them;
- production authority expansion disguised as "learning";
- expensive reasoning when stable code or a small decision mechanism is enough.

Foundation's advantage is not scale. It can be **tight control, reuse, evidence, and selective intelligence**.

---

# 13. Current highest-value synthesis for FRIDAY

The frontier direction relevant to this machine is:

`OBSERVE`
`-> RECOVER CURRENT AUTHORITY`
`-> DEFINE THE REAL OUTCOME`
`-> IDENTIFY THE FAILING MODULE`
`-> CHECK REPLAY/HISTORY`
`-> CHOOSE CHEAPEST CAPABLE MECHANISM`
`-> GENERATE DISTINCT CANDIDATES WHEN NEEDED`
`-> RUN IN ISOLATION`
`-> TEST VISIBLE + HIDDEN CASES`
`-> ATTACK THE METRIC`
`-> INDEPENDENTLY PROVE OR REJECT`
`-> RECORD RECEIPT + LINEAGE`
`-> EXTRACT SANITIZED LEARNING`
`-> DOWNSHIFT REPEATED SUCCESS`
`-> PROMOTE ONLY UNDER AUTHORITY`
`-> CONTINUE OR STOP AT OWNER GATE`

This is the direct bridge from the current research corpus to the Foundation automation target.

---

# 14. Bottom line

The important discovery from the video is **not** BEL, GPT-7, a single benchmark score, or a rumored Gemini model.

The durable pattern is that state-of-the-art AI development is moving from:

> build one smarter model

into:

> build a system that can repeatedly produce, test, preserve, combine, and reject better ways of thinking and acting.

The most relevant mechanisms for FRIDAY are:

- replay from durable history;
- modular harness evolution;
- hidden/held-out evaluation;
- independent proof;
- candidate diversity and lineage;
- stable tools plus evolving skills;
- calibrated/typed decision routing;
- user-interaction-to-evaluation conversion;
- metric challenge;
- controlled self-improvement under explicit authority.

No model, paper, or research claim in this document automatically changes Foundation authority.

The research belongs in the machine as **evidence and candidate mechanisms**. Harness decides what survives.

---

# Source index

Video
- https://www.youtube.com/watch?v=dk-hx4_cqpk

Primary / high-signal research
- OpenAI — An Alien Mind: https://openai.com/index/an-alien-mind/
- OpenAI — Navier-Stokes solution/research process: https://openai.com/index/navier-stokes-solution/
- OpenAI — Research acceleration inside OpenAI: https://openai.com/index/research-acceleration-view-inside-openai/
- ARC Prize — Astra: https://arcprize.org/blog/astra
- ARC / Abstraction and Reasoning: https://arxiv.org/abs/1911.01547
- Dream-RSI: https://arxiv.org/abs/2609.14858
- ModularRSI: https://arxiv.org/abs/2609.14857
- ScienceBuddy: https://arxiv.org/abs/2609.17523
- AIDE2: https://arxiv.org/abs/2609.26457
- A-Evolve-Training: https://arxiv.org/abs/2606.20657
- The Last AI Built by Humans: https://arxiv.org/abs/2609.11873
- Darwin Godel Machine: https://arxiv.org/abs/2505.22954
- AI-Generating Algorithms: https://arxiv.org/abs/1905.10985
- ARC Prize refinement-loop work: https://arxiv.org/abs/2601.10904
- DeepSeek Elastic Compute / isolated agent environments: https://arxiv.org/abs/2609.22978
- Meta unified AI agents / Capacity Efficiency: https://engineering.fb.com/2026/04/16/developer-tools/capacity-efficiency-at-meta-how-unified-ai-agents-optimize-performance-at-hyperscale/
- Dario Amodei — pace the frontier: https://darioamodei.com/post/we-must-pace-the-frontier
- Jev / TypeSafe AI reporting: https://www.wsj.com/tech/ai/startup-typesafe-ais-jev-model-sparks-copycats-talk-of-llm-alternatives-e39ff57d
- Noam Brown / OpenAI public forum context: https://forum.openai.com/en/public/videos/ai-economics-in-the-forum-2025

## Evidence labels used in this file

- `CONFIRMED` — supported by primary/current source.
- `REAL BENCHMARK RESULT / MISLEADING LABEL` — underlying result exists, headline interpretation overstates it.
- `UNVERIFIED LEAK / CLAIMED` — not strong enough for operational use.
- `RESEARCH CANDIDATE` — mechanism worth testing but not adopted.
- `SUPPORTING RESEARCH EVIDENCE` — external evidence reinforces an existing architecture/rule but does not by itself promote anything.

End state for this artifact: **PRESERVED_RESEARCH / NOT_AUTHORITY**.
