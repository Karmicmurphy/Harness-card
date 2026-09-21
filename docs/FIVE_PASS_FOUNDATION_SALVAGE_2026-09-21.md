# Five-Pass Foundation Salvage — Frankenstein Warehouse V0

Date: 2026-09-21  
Status: **WORKING FOUNDATION SALVAGE DECISION — IMPLEMENTATION CANDIDATES, NOT AUTOMATIC AUTHORITY**

## Mission

Finish a functional, bounded, provable software factory from the estate that already exists. Do not build another monolithic AI system.

The target machine is allowed to improve itself only through the existing human-owned lifecycle:

```text
observe -> propose candidate -> build/test -> independent proof -> promote/activate -> monitor -> rollback if needed
```

No model, worker, external repository, or imported artifact receives authority merely by being useful.

---

## Legal rule before all five passes

**Copying only a file, function, snippet, or "5%" of a licensed project does not automatically remove the source license or copyright obligations.**

Warehouse dispositions:

- **REUSE** — exact code may be imported only when Rights Gate records a compatible license and required notices/obligations.
- **ADAPT** — permissive component can be wrapped or modified with provenance retained.
- **CLEAN-ROOM MECHANISM** — learn the architecture/algorithm/pattern, then write our own implementation without copying protected expression; patent/technology-transfer questions remain separate.
- **REFERENCE ONLY** — useful for comparison/ideas; no code import.
- **BLOCK** — no license, incompatible terms, noncommercial-only for commercial core, or unresolved rights.

Publicly reachable does not mean ownerless.

---

# PASS 1 — Recover what we already own

## Existing functional authorities

| Existing repo | Function to keep | Foundation role |
|---|---|---|
| `Karmicmurphy/Harness-card` | recovery, scope, rules, proof requirements, continuity | GOVERNOR |
| `Karmicmurphy/temporal-capability-foundry` | typed job/capability lifecycle, Builder, evaluation, promotion, activation, rollback | FACTORY |
| `Karmicmurphy/Untethered-AIOS` | bounded process lifecycle, scheduler, capability/path grants, runtime audit | DISPATCH / RUNTIME |
| `Karmicmurphy/digital-scrapyard-autopilot` | Artifact Compass, Salvage, Rights Gate, Recombination Forge, Proof Gate, Thought Economy, Capability Downshift | SALVAGE / METHODS |
| `Karmicmurphy/Ollie_Twis_Holo_workshop` | human cockpit, handoff, returned artifacts, receipts, review | FRONT DESK |
| CERT-RIVER / PRISM-RIVER lineage | independent claim/proof/certificate discipline | INSPECTION LINE — archived executable implementation not yet verified |

This is **not five repositories inside one repository**. They are separate specialized repositories linked through explicit contracts.

## Existing mechanisms that should not be rebuilt

- explicit path/capability grants;
- bounded scheduler/process lifecycle;
- typed Foundry job/candidate lifecycle;
- promotion/activation/rollback;
- artifact/provenance registry concepts;
- receipt/evidence concepts;
- salvage/rights/proof methods;
- Workshop adapter boundary and human approvals;
- deterministic unit/CI proof paths.

Verdict: **KEEP AND LINK.**

---

# PASS 2 — Remove AI where ordinary machinery can win

Thought Economy result:

```text
IGNORE -> CACHE -> RULE -> SCRIPT -> WORKER -> TINY MODEL -> CENTRAL AI -> OWNER
```

## No-model workers

These should be deterministic by default:

- file/repository inventory;
- hashes/checksums;
- duplicate and exact-match detection;
- Git tree/history/diff analysis;
- dependency extraction;
- license-file discovery;
- path and capability enforcement;
- job state machines;
- scheduling and time/resource limits;
- test execution;
- automatic post-edit retest;
- acceptance comparators;
- syntax/AST parsing;
- structural code search;
- structural rewrite when an exact rule exists;
- proof receipts;
- quarantine/rollback;
- health/watchdog checks;
- change detection / estate delta updates.

## Tiny-model-only candidates

Use a model only when the input is genuinely fuzzy:

- semantic artifact similarity;
- fuzzy classification/routing after rules fail;
- ranking candidate artifacts;
- extracting structured facts from messy documents;
- generating one narrow code patch after deterministic localization.

## Bigger-model escalation only

- ambiguous multi-file debugging;
- novel architecture reasoning;
- incomplete/contradictory requirements;
- invention synthesis where no deterministic procedure exists.

Verdict: **DOWN-SHIFT THE FACTORY.**

---

# PASS 3 — Permissive external salvage candidates

These are candidates for technical evaluation; exact version/license evidence must be pinned before import.

| Source | Useful atom | Rights posture | Proposed use |
|---|---|---|---|
| Agentless — OpenAutoCoder | localization -> repair -> validation; avoid agent wandering | MIT | Builder architecture/reference or selective reuse |
| mini-SWE-agent — Princeton/Stanford SWE-agent team | radically small software-engineering loop | MIT | compare loop mechanics; salvage only useful atoms |
| SWE-bench | reproducible issue/patch/test evaluation concepts | MIT | create tiny Randy-scale repair benchmark |
| DSPy — Stanford | metric-driven optimization of LM programs/prompts | MIT | later optimize small models from proof traces; not runtime foundation |
| ast-grep | AST structural search and rewriting | MIT | deterministic localization / safe structural edits |
| Tree-sitter | fast incremental syntax trees | MIT | repository parsing/localization across languages |
| Spack — LLNL | specs, concretization, versions/variants/dependency reasoning | MIT OR Apache-2.0 | artifact/capability compatibility and exact environment specs |
| NASA F Prime | explicit components, ports/interfaces, queues, generated glue, testing | Apache-2.0 | component/contract patterns; do not import full flight framework |
| NASA Open MCT | plugin/telemetry/provider UI architecture | Apache-2.0 (with third-party notices to inspect) | Workshop cockpit inspiration/components only if useful |
| NASA cFE/cFS components released under Apache-2.0 | software-bus / reusable component patterns | version/component specific | AIOS messaging/health concepts; verify each repo |
| Microsoft BitNet | CPU-efficient 1-bit inference runtime/models | MIT | old-x86 local inference experiment |
| Microsoft bitnet-embedding-270m | tiny CPU embedding/retrieval | MIT | estate/artifact semantic search bake-off |
| IBM Granite 4.0 H 350M | tiny instruct/hybrid model | Apache-2.0 | fuzzy classification/routing wildcard |
| Qwen2.5-Coder 0.5B Instruct | tiny code-specialized patch generator | Apache-2.0 | narrow Builder patch bake-off |
| Hugging Face SmolLM2 360M Instruct | tiny general instruct model | Apache-2.0 | routing/extraction baseline |

Sources inspected 2026-09-21 include:
- https://github.com/OpenAutoCoder/Agentless
- https://github.com/SWE-agent/mini-swe-agent
- https://github.com/SWE-bench/SWE-bench
- https://github.com/stanfordnlp/dspy
- https://github.com/ast-grep/ast-grep
- https://github.com/tree-sitter/tree-sitter
- https://github.com/spack/spack
- https://github.com/nasa/fprime
- https://github.com/nasa/openmct
- https://github.com/nasa/cFE
- https://github.com/microsoft/BitNet
- Hugging Face model cards for Microsoft BitNet, IBM Granite, Qwen, SmolLM2.

Verdict: **TEST SMALL ATOMS; DO NOT VENDOR WHOLE PRODUCTS BY DEFAULT.**

---

# PASS 4 — Valuable reference-only / manual-rights candidates

| Source | Useful mechanism | Rights disposition now |
|---|---|---|
| Liquid AI LFM2.5 230M/350M | extremely small edge generative models | MANUAL RIGHTS REVIEW — LFM 1.0/custom |
| Liquid LFM2.5 Encoder 230M/350M | CPU-oriented classification/understanding | MANUAL RIGHTS REVIEW |
| Liquid LFM2.5 Embedding / ColBERT 350M | retrieval / artifact matching | MANUAL RIGHTS REVIEW |
| Google FunctionGemma 270M | tiny function/tool routing | MANUAL RIGHTS REVIEW — Gemma terms |
| Salesforce xLAM 1B FC | function calling | REFERENCE ONLY for commercial core — CC-BY-NC |
| NASA Ogma / Copilot lineage | generate deterministic runtime monitors from formal properties | REFERENCE/CLEAN-ROOM until exact license obligations are cleared |
| NASA SCH repository | deterministic time-slot scheduler | REFERENCE/CLEAN-ROOM because repository currently identifies NASA Open Source Agreement |
| historical MIT program-repair research | generate-and-validate, condition synthesis; warning that weak tests accept bad patches | RESEARCH/MECHANISM; inspect individual software rights before code reuse |
| GenProg / Angelix / Astor / kGenProg research | generate-and-validate and search-space reduction | mechanism candidates; use permissive code only after individual Rights Gate |

## Critical research lesson

MIT CSAIL's patch-correctness work found that weak validation can accept incorrect patches. Therefore:

**"tests passed" is development evidence, not independent certification.**

This supports keeping Builder, proof/certification, and promotion separate.

Verdict: **LEARN AGGRESSIVELY, COPY CONSERVATIVELY.**

---

# PASS 5 — Recombine into the smallest working Frankenstein

## Foundation V0

```text
                        RANDY
                          |
                          v
                    WORKSHOP
              human job / artifact
                          |
                          v
                     HARNESS
          scope + rules + proof contract
                          |
                          v
                     FOUNDRY
          typed job / lifecycle / evidence
                          |
          +---------------+----------------+
          |                                |
          v                                v
  deterministic workers             fuzzy intelligence
  ---------------------             ------------------
  inventory/hash/git                embeddings / ranking
  AST/tree-sitter                   tiny classifier
  ast-grep localization             narrow patch model
  test/retest                       larger model only on escalation
  rights/provenance
  acceptance comparator
          |                                |
          +---------------+----------------+
                          |
                          v
                       AIOS
       wake bounded worker + explicit grants
                          |
                          v
               candidate artifact / receipt
                          |
                          v
              INDEPENDENT PROOF LANE
       rerun acceptance + monitors + quarantine
                          |
                          v
              Foundry promotion decision
                          |
                          v
               Workshop shows evidence
                          |
                          v
                        RANDY
```

## Builder V0 correction

Current model-controlled loop is too agent-like for a tiny local model.

Replace its default path with an **Agentless-style deterministic repair pipeline**:

```text
1. worker runs failing test
2. worker extracts failure locations/symbols
3. worker uses exact search + AST/structural localization
4. worker preloads the smallest relevant code window
5. model gets ONE narrow job: propose patch
6. worker applies patch in bounded workspace
7. worker automatically reruns targeted tests
8. worker runs broader regression gate
9. independent lane reruns acceptance
10. promote only if proof allows it
```

The model does not choose whether to inspect, retest, prove, promote, deploy, or broaden scope.

## Patch-brain bake-off

Do not choose one model by brand.

Minimum candidate set:

1. **NO MODEL** — deterministic known-rule/structural repair where possible.
2. **Qwen2.5-Coder 0.5B Instruct** — Apache-2.0.
3. **Qwen2.5-Coder 1.5B Instruct** — current baseline, Apache-2.0.
4. **Granite 4.0 H 350M** — Apache-2.0 wildcard.
5. **SmolLM2 360M Instruct** — Apache-2.0 baseline.
6. **BitNet general/embedding candidates** — MIT, especially for CPU-limited estate work.
7. **Liquid 230M/350M** — benchmark only after Rights Gate clears model terms.

Measure:
- exact patch success;
- targeted and regression test pass;
- model calls;
- wall time;
- memory;
- CPU;
- model size;
- license/redistribution posture;
- hallucinated/unnecessary edits;
- owner intervention.

Smallest candidate that reliably meets the gate wins for that job class.

## Artifact/estate retrieval bake-off

Start with:
1. exact hash/path/name/grep;
2. AST/symbol index;
3. BitNet embedding 270M or another permissive small embedder;
4. Liquid retriever only after Rights Gate;
5. larger semantic model only if the small stack misses materially.

---

# What "self-improving" is allowed to mean

Allowed:

```text
successful novel trace
-> collect evidence
-> identify repeatable step
-> convert to rule/script/worker/micro-model
-> regression test
-> independent proof
-> candidate promotion
-> human-controlled activation
```

Not allowed:

- unrestricted self-modification;
- model rewriting governance;
- model changing its own permissions;
- silently replacing proof criteria;
- self-deploying;
- self-spending;
- hiding provenance;
- promoting a model because it says it improved.

This is **Capability Downshift**, not runaway autonomy.

---

# Build sequence to make the machine functional

## Gate A — Foundation contracts
- update stale authority records;
- define one tiny cross-repo job envelope;
- define receipt/evidence linkage IDs;
- preserve separate receipt semantics.

## Gate B — Deterministic Builder
- convert default Builder path to localization -> one patch proposal -> automatic retest;
- add AST/structural localization candidate;
- keep model adapter replaceable;
- build small repair benchmark.

## Gate C — Foundry -> AIOS wake adapter
- candidate workspace;
- explicit grants/path scopes;
- resource/tick limit;
- terminal result + AIOS audit linked to Foundry evidence.

## Gate D — Independent Certifier V0
Do not wait for a perfect resurrected River implementation.

Build the smallest independently executing proof lane that can:
- pin candidate/hash;
- rerun exact acceptance tests outside Builder;
- verify forbidden files were not touched;
- run deterministic policy/property checks;
- issue CERTIFIED / REJECTED / QUARANTINED for the exact claim;
- never deploy.

Recover additional CERT-RIVER primitives later without changing this boundary.

## Gate E — Workshop handoff
After authoritative local Workshop state is reconciled:
- submit job;
- show state;
- show artifact/diff;
- show Builder receipt;
- show AIOS runtime receipt;
- show independent proof result;
- require Randy for publish/deploy/permanent actions.

## Gate F — Learning/downshift loop
Only after A-E are working:
- collect successful traces;
- discover repeated decisions;
- convert repeats into rules/scripts/tiny models;
- benchmark changes;
- promote only through proof.

---

# Do not build

- another AI OS;
- another scheduler;
- another giant agent framework;
- one giant merged repository;
- one giant all-purpose LLM brain;
- another proof database unless evidence requires one;
- autonomous deployment/spend/destructive authority.

# Foundation verdict

The viable invention is a **human-owned software factory whose intelligence is sparse and replaceable**.

Most of the machine is deterministic software. Models are replaceable tools used only at fuzzy boundaries. Existing repositories remain separate functional authorities connected by small contracts.

The next implementation target is **Deterministic Builder V0**, followed by the **Foundry -> AIOS Wake Adapter V0**, then **Independent Certifier V0**.
