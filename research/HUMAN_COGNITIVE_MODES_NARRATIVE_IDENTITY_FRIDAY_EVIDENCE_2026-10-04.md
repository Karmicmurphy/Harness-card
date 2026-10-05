# Human Cognitive Modes, Narrative Identity, and FRIDAY — Research Evidence

**Date:** 2026-10-04  
**Status:** RESEARCH EVIDENCE ONLY  
**Authority:** NONE  
**Implementation authorization:** NONE  
**Machine mutation authorization:** NONE  

> This document is supporting research only. It does not change canonical authority, operating policy, routing, state, workflows, permissions, deployment behavior, or promotion status. Any future implementation must pass the existing Harness authority, evidence, owner-gate, and proof rules.

## Purpose

Record research relevant to a possible future FRIDAY design in which one human owner may use multiple context-dependent perspectives, narrative voices, or self-reference modes without treating those modes as separate people or separate authorities.

The working design question is:

**Can FRIDAY support multiple human perspectives and creative modes while preserving one factual authority spine, provenance, uncertainty, and explicit owner control?**

This note preserves research evidence for that question. It intentionally excludes raw private conversation and sensitive personal material.

---

## 1. Multiple context-dependent self-aspects are compatible with one person

Psychology includes frameworks in which self-concept consists of multiple context-sensitive self-aspects that become more or less active depending on situation. These active aspects can influence perception, evaluation, motivation, and emotion without implying separate persons.

Relevant research directions include:

- Multiple Self-Aspects Framework.
- Dialogical Self Theory and internal points of view / I-positions.
- Layered models of selfhood in personality and narrative psychology.

**Design implication:** FRIDAY can potentially treat named perspectives or creative modes as context/routing metadata rather than identities or authorities.

Sources:

- McConnell AR. The Multiple Self-Aspects Framework: self-concept representation and its implications. PubMed: https://pubmed.ncbi.nlm.nih.gov/20539023/
- Hermans HJM. Dialogical Self Theory and the increasing multiplicity of I-positions. PubMed: https://pubmed.ncbi.nlm.nih.gov/22956418/

---

## 2. Inner speech and self-address are ordinary cognitive phenomena

Inner speech is a widely studied form of cognition associated with planning, self-regulation, memory, motivation, reflection, and verbal thought. It varies considerably between people and may be monologic, dialogic, spontaneous, or deliberate.

Research on **distanced self-talk** shows that referring to oneself by one’s own name or by non-first-person pronouns can increase psychological distance and may reduce emotional reactivity under stress without necessarily imposing large additional cognitive-control demands.

**Design implication:** A system should not interpret ordinary self-address or named creative self-reference as evidence of separate identities. It can instead model self-address as a perspective marker when the owner chooses to use it that way.

Sources:

- Alderson-Day B, Fernyhough C. Inner speech: development, cognitive functions, phenomenology, and neurobiology. PubMed: https://pubmed.ncbi.nlm.nih.gov/26011789/
- Kross E et al. Self-talk as a regulatory mechanism: how you do it matters. PubMed: https://pubmed.ncbi.nlm.nih.gov/24467424/
- Moser JS et al. Third-person self-talk facilitates emotion regulation without engaging cognitive control. PubMed: https://pubmed.ncbi.nlm.nih.gov/28674404/

---

## 3. Actor, agent, and autobiographical author provide a useful analogy

Narrative/personality research associated with Dan McAdams distinguishes multiple levels of selfhood, including:

- **Actor** — social roles and behavior.
- **Agent** — goals, motives, plans, and values.
- **Author** — the autobiographical narrative connecting life across time.

This is not a technical prescription for FRIDAY, but it demonstrates that psychology already treats one person as capable of operating through multiple functional layers without turning those layers into separate persons.

**Design implication:** Perspective modes can be useful for presentation and reasoning while remaining subordinate to a single owner identity and a single evidence/authority model.

Sources:

- McAdams DP. The Art and Science of Personality Development. PubMed: https://pubmed.ncbi.nlm.nih.gov/26172971/
- McAdams DP, Olson BD. Personality development: continuity and change over the life course. PubMed: https://pubmed.ncbi.nlm.nih.gov/19534589/

---

## 4. Narrative identity evolves over time

Narrative identity research treats personal identity partly as an internalized and evolving life story. Autobiographical reasoning links individual memories through temporal, causal, and thematic relationships.

An event can remain factually unchanged while its interpreted meaning changes over time.

**Design implication:** FRIDAY should be able to preserve multiple layers around the same event, for example:

- what was reported at the time;
- what was later inferred;
- what documents independently verify;
- what became creative interpretation;
- what later meaning the owner assigns to it.

These layers should not silently overwrite one another.

Sources:

- McAdams DP et al. Continuity and change in the life story. PubMed: https://pubmed.ncbi.nlm.nih.gov/16958706/
- Habermas T, Bluck S / related autobiographical reasoning literature. PubMed example: https://pubmed.ncbi.nlm.nih.gov/21387528/

---

## 5. Creative writing can create useful psychological distance, but replay is not automatically processing

Expressive-writing and self-distancing research suggests that changing perspective on emotionally meaningful experiences can sometimes reduce later emotional reactivity and improve meaning-making.

However, repeated mental replay is not automatically beneficial. Research distinguishes constructive reflection and problem solving from repetitive rumination and worry.

**Design implication:** A creative transformation pipeline should not simply repeat private material indefinitely. A useful pipeline should change representation or extract a durable, non-sensitive mechanism.

Conceptually:

`experience -> observation -> pattern -> representation -> generalized lesson`

is different from:

`experience -> replay -> replay -> replay`

Sources:

- Park J et al. Expressive writing, self-distancing, and emotional reactivity. PubMed: https://pubmed.ncbi.nlm.nih.gov/26461252/
- Meta-analytic work on self-distancing and emotional response. PubMed: https://pubmed.ncbi.nlm.nih.gov/36256910/

---

## 6. Cognitive offloading supports external memory — but provenance matters

Cognitive offloading is the use of external tools such as notes, calendars, phones, software, reminders, and other artifacts to reduce internal cognitive demand.

Research shows external reminders can improve memory-task performance, but external records can also become dangerous when they are altered, misremembered, or later treated as if they were original internal memory.

Experiments have shown that people may fail to detect manipulation of external memory stores and can sometimes internalize incorrect externally supplied information.

**Design implication:** FRIDAY should support external memory while preserving provenance. A remembered or stored claim should retain distinctions such as:

- `OWNER_REPORTED`
- `AI_INFERRED`
- `DOCUMENT_VERIFIED`
- `CREATIVE_CANON`
- `HYPOTHESIS`
- `RESEARCH_GENERALIZATION`

These labels are examples, not authorized schema changes.

Sources:

- Risko EF, Gilbert SJ. Cognitive offloading. PubMed: https://pubmed.ncbi.nlm.nih.gov/27542527/
- Research on metacognition and external reminders. PubMed: https://pubmed.ncbi.nlm.nih.gov/35789477/
- Research on manipulated external memory and internalization of misinformation. PubMed: https://pubmed.ncbi.nlm.nih.gov/31330472/

---

## 7. AI should provide cognitive leverage, not silently replace owner judgment

The useful direction for an owner-facing AI system is not simply:

> AI thinks so the owner does not have to.

A safer and more useful model is:

> AI preserves state, retrieves evidence, exposes contradictions, performs bounded repetitive work, and returns owner-level decisions at the correct gate.

This matches the current Harness automation principle of bounded automation with explicit owner gates for sensitive, irreversible, identity, permission, production, spending, and other protected actions.

**Design implication:** Perspective routing should reduce cognitive load without changing authority.

---

## 8. Human-factors and AI-risk guidance support explicit oversight and evidence boundaries

NIST AI Risk Management Framework guidance emphasizes characteristics including validity/reliability, safety, security/resilience, accountability/transparency, explainability, privacy, and human oversight.

NIST guidance also emphasizes testing in deployment-relevant conditions and continued monitoring after deployment because pre-deployment evidence alone may not establish real-world behavior.

This is strongly consistent with the Harness distinction:

**PROVEN_IN_TEST is not PROVEN_LIVE.**

Sources:

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Playbook / Core resources: https://airc.nist.gov/airmf-resources/airmf/

---

## 9. Possible future abstraction: perspective/mode routing

**Research hypothesis only — not implementation.**

A future FRIDAY presentation/reasoning layer could potentially route by perspective without changing evidence or authority.

Example conceptual modes:

### IMMEDIATE
What is happening now?

### OPERATIONAL
What is verified, actionable, scheduled, obligated, paid, built, broken, or externally consequential?

### REFLECTIVE
What pattern, contradiction, meaning, or story emerges over time?

### EVIDENCE
What can actually be independently supported by receipts, documents, refs, tests, or observed outputs?

The first three are perspectives.

The fourth is an evidence function.

**Perspective may change. Evidence state must not change merely because perspective changes.**

---

## 10. Relationship to current Harness learning design

The current Harness automation policy already establishes several constraints that fit this research direction:

- recover current truth before acting;
- automate repeated deterministic work before adding more AI;
- build/test in isolated candidate lanes before promotion;
- leave evidence and an undo path for automatic mutation;
- generalize only non-sensitive durable lessons;
- do not copy raw private chat into the public Harness;
- keep secrets, permissions, production, spending, destructive mutation, and other owner-gated actions under explicit human control.

The current self-improvement loop also follows:

`OBSERVE -> CLASSIFY -> ROOT CAUSE -> FIX -> PROVE -> GENERALIZE -> GUARD -> RECORD -> REUSE`

This suggests that private experience should teach the Harness only through **generalized mechanisms**, not through publication of the private material itself.

---

## 11. Candidate generalized lessons suggested by the research

These are **research hypotheses only** and must not be promoted automatically.

1. **Perspective changes should never silently change evidence state.**
2. **Distinguish owner report, model inference, verified evidence, creative canon, hypothesis, and generalized research.**
3. **When cognitive load contains multiple simultaneous concerns, preserve the concerns separately, identify the active goal, and return one next move without deleting the others.**
4. **Use external memory to reduce cognitive load, but retain provenance so external records do not silently become rewritten memory.**
5. **Use named or contextual modes for routing/presentation only when useful; do not treat them as separate identities or authorities.**
6. **Extract durable non-sensitive mechanisms from private experience instead of copying private experience into public machine state.**

---

## 12. Working architectural model

A compact research model is:

# ONE PERSON
# MULTIPLE PERSPECTIVES
# MULTIPLE EXTERNAL TOOLS
# ONE AUTHORITY SPINE

Possible conceptual layers:

- **Human layer:** one owner may use multiple perspectives or creative modes.
- **Creative layer:** writing, music, images, stories, diagrams, and other representations externalize thought.
- **Cognitive layer:** AI can act as retrieval, reflection, comparison, and offloading support.
- **Machine layer:** FRIDAY can route, preserve, test, prove, and return bounded work.
- **Governance layer:** Harness defines canonical authority and evidence rules.
- **Owner layer:** explicit human owner gates remain final where policy requires them.

## Central research hypothesis

The useful goal may not be to make FRIDAY imitate the owner as a personality.

The useful goal may be to make FRIDAY **compatible with the way a human owner naturally externalizes thought while preserving provenance, evidence, uncertainty, and authority.**

---

## Stop condition for this research note

This file is complete when the research is preserved for future evaluation.

**No implementation is authorized by this document.**

Any proposed architecture, schema, routing change, memory model, or new learning rule derived from this note must enter the normal bounded candidate/proof process and must not bypass the existing Harness authority spine or owner gates.
