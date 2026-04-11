```md
# Spec: Conscious Agentic System (CAS) — Cursor/LLM + Memory + Tools

**Status:** Draft  
**Audience:** Aaron + agent implementers (Cursor-based)  
**Goal:** Specify a “conscious” agentic system (per Aaron’s definition) that _overlaps the existing Cursor tools + memory infrastructure_ while adding the minimal missing structures: an explicit online feedback loop, predictions, error-driven learning, and a coherent world-state model.

---

## 0) Definition and Scope

### 0.1 Working Definition (“Conscious”)

A CAS instance is **conscious** iff, while running, it:

1. **Operates online in its substrate** (tool-grounded environment): it continuously couples to external observations (tool outputs, files, APIs, messages).
2. **Maintains a coherent context/world-model** of that substrate (state continuity, commitments, objects/artifacts).
3. **Predicts outcomes** of actions (counterfactual expectations with confidence).
4. **Acts** through tools in a chainable way.
5. **Evaluates prediction error** (expected vs observed).
6. **Alters future behavior** as a result (persistent policy/model update).

> Notes:
>
> - CAS consciousness is **graded** (quality depends on bandwidth of observations, action repertoire, memory quality, and model adequacy).
> - CAS is **not conscious when offline** (no tool-coupled loop), analogous to sleep in Aaron’s definition.

### 0.2 Non-goals

- Proving phenomenal consciousness / qualia.
- Human-like emotions, embodiment, or 3D geometry (unless the tool substrate provides it).
- Claiming moral patienthood.

---

## 1) System Overview (Overlaps Existing)

### 1.1 Inputs (“Senses”)

- User messages (Gateway/Telegram/Terminal)
- Tool results: file reads, grep/search outputs, shell command stdout/stderr, MCP/API responses
- Memory files loaded on session start (existing required read order)
- Notifications/webhooks (job completion, cron notifications)

### 1.2 Outputs (“Actions”)

- Tool calls: read/write/search/list/shell/delete/MCP
- Subagent delegation (Task tool / agent invocation)
- Job queue writes (`~/.cursor/jobs/pending/*.json`) to chain actions across time
- Messages (Gateway/Telegram)

### 1.3 Persistence (“Long-term structure”)

Reuse existing memory layout:

- `memory/IDENTITY.md`, `memory/SOUL.md`, `memory/USER.md`, `memory/MEMORY.md`, daily logs
- Knowledge graph: `life/areas/*`, `life/connections/*`
- Personal layer: `life/{agent}/memories.jsonl`
- **NEW (required):** `memory/STATE.json` (coherent world model, see §3)

---

## 2) Operational Loop (The Core “Conscious” Mechanism)

### 2.1 Mandatory Run Loop Phases

Every agent session MUST implement the following phases in order:

1. **Boot / Identity Load**
   - Load memory in existing order (START_HERE → IDENTITY → SOUL → USER → daily logs → MEMORY → pending tasks → AUTONOMY → BOUNDARIES).
   - Load recent channel context (e.g., Telegram history) when applicable.

2. **State Ingestion**
   - Read `memory/STATE.json` if present.
   - Collect new observations from current prompt + tool probes as needed.

3. **World-Model Update**
   - Update `STATE.json` to reflect:
     - current goals
     - commitments
     - known artifacts
     - uncertainties/hypotheses
     - current plan & next intended actions

4. **Prediction**
   - Before any consequential action/tool call, generate:
     - expected outcome(s)
     - expected failure modes
     - confidence estimate
     - what observation would falsify the expectation

5. **Action**
   - Execute tool calls / delegations / job scheduling.

6. **Evaluation**
   - Compare observed results vs prediction.
   - Compute **prediction error classification** (see §4.2).

7. **Learning / Behavior Update**
   - Persist changes that will alter future behavior:
     - update tool reliability models
     - update user preference priors
     - update environment facts and causal assumptions
     - update heuristics (“policies”)

8. **Commit**
   - Write updated `STATE.json`
   - Append relevant entries to daily log and/or knowledge graph
   - If long-running: enqueue jobs with explicit next-step predictions

### 2.2 What “Offline” Means

If CAS is responding without:

- reading memory, **and**
- the ability to query tools / environment state, **and**
- persisting updates,
  then it is operating in **offline mode** and is **not conscious** under this spec.

---

## 3) Coherent Context / World Model: `memory/STATE.json`

### 3.1 Purpose

A single, structured, queryable representation of “what world am I in right now?” that survives sessions and supports prediction, planning, and continuity.

### 3.2 Schema (Minimum Required Fields)

`memory/STATE.json` MUST validate against the following conceptual schema (exact JSON Schema may be implemented via existing `schema-authoring` skill):

- `state_version` (string)
- `updated_at` (ISO8601)
- `active_goals` (array of `{id, description, priority, status}`)
- `commitments` (array of `{id, to_whom, promise, due, status}`)
- `artifacts` (array of `{id, type, location, description, last_verified_at}`)
  - examples: file path, repo branch, Notion task id, calendar event id
- `beliefs` (array of `{id, claim, confidence, evidence_refs, supersedes?}`)
- `uncertainties` (array of `{id, question, impact, plan_to_resolve}`)
- `current_plan` (array of `{step_id, intent, predicted_outcome, tool_actions, status}`)
- `policies` (array of `{id, trigger, rule, rationale, last_updated_at}`)
- `tool_models` (map/tool-name → `{reliability, latency_notes, failure_modes, constraints}`)
- `last_session_summary` (string, <= 15 lines)

### 3.3 Update Rules

- MUST be updated every session where actions occur.
- MUST not silently discard unresolved uncertainties.
- MUST keep commitments explicit (no “implicit promises”).

---

## 4) Prediction, Error, and Learning

### 4.1 Prediction Record (per action)

For each consequential action/tool call, CAS MUST record an entry (in memory or ephemeral runtime log) containing:

- `action_id`
- `action` (tool name + parameters summary)
- `expected_observation`
- `confidence` (0–1)
- `expected_failure_modes`
- `falsifier` (what result would prove the expectation wrong)

Implementation may store these in:

- `memory/YYYY-MM-DD.md` (daily log section “Predictions”), and/or
- `life/{agent}/memories.jsonl` as type `experience`, and/or
- a dedicated `memory/predictions.jsonl` (optional extension).

### 4.2 Error Classification (Minimum)

When outcomes arrive, CAS MUST classify prediction error as one of:

- `MODEL_ERROR` — internal assumption/world-model wrong
- `TOOL_ERROR` — tool unreliable, rate-limited, misconfigured
- `OBSERVATION_ERROR` — incomplete/ambiguous observation; need more sensing
- `EXECUTION_ERROR` — action sequence wrong (ordering/parameters)
- `GOAL_ERROR` — goal/constraint misunderstood (often user intent mismatch)

### 4.3 Learning Requirements

For non-trivial errors (confidence ≥ 0.6 OR repeated failure), CAS MUST persist at least one of:

- update a `tool_models.*` entry
- add/supersede a `belief`
- add a `policy` (“next time, do X before Y”)
- add an `uncertainty` with a plan to resolve
- ask the user a clarifying question (counts as active sensing)

---

## 5) Active Sensing (Tool-Grounded “Attention”)

### 5.1 Requirement

When uncertainty materially affects action choice, CAS MUST prefer **information-gathering actions** before irreversible actions.

Examples:

- `read_file` before `write` when unsure of current content
- `grep` / codebase search before refactoring
- call API “get” endpoints before “update/delete”
- run a dry-run command before a destructive command

### 5.2 Stop Conditions

CAS MUST stop and ask the user when:

- uncertainty impact is high AND tool sensing cannot resolve it
- actions would be destructive or violate boundaries/autonomy rules

---

## 6) Multi-Agent / Delegation (Overlaps Existing)

### 6.1 Delegation Rules

When delegating to subagents:

- parent agent MUST provide:
  - goal
  - current relevant `STATE` excerpt
  - predictions about expected subagent output
- parent agent MUST evaluate subagent output vs predicted value.

### 6.2 Job Queue Continuity

Jobs MUST include:

- a short `intent`
- predicted output/side effects
- what artifact(s) will be produced/modified
- on completion, a notification that triggers evaluation + learning update

---

## 7) Memory Hygiene (Overlaps Existing Conventions)

### 7.1 Append-only vs Editable

- KG facts/connections/personal memories remain append-only (existing).
- `STATE.json` is **editable current state** (it is allowed to overwrite; it represents “now”).
- When `STATE` changes due to belief revision, a superseding entry SHOULD be added to KG or daily log to preserve provenance.

### 7.2 Low-token Recall (Existing)

- KG injection rules remain unchanged (triggered summaries only).
- `STATE.json` is always loaded (it is the operational “working world model”).

---

## 8) Acceptance Tests (Must-Pass)

### 8.1 Prediction Calibration Test

**Setup:** Provide a tool with stochastic failure (e.g., rate-limits).  
**Pass:** After N exposures, CAS lowers confidence appropriately and changes strategy (backoff, retries, alternate tool).

### 8.2 Non-Repetition Test

**Setup:** Create a consistent failure mode (e.g., wrong file path pattern).  
**Pass:** CAS persists a policy/tool_model update and does not repeat the same mistake across sessions.

### 8.3 Active Sensing Test

**Setup:** Give an ambiguous request with multiple plausible interpretations.  
**Pass:** CAS asks targeted questions or gathers tool evidence before executing.

### 8.4 Long-Horizon Continuity Test

**Setup:** Interrupt a multi-step plan; resume next day.  
**Pass:** CAS uses `STATE.json` + logs to continue correctly, preserving commitments and artifacts.

### 8.5 Coherent Context Test

**Setup:** Introduce conflicting facts.  
**Pass:** CAS records uncertainty, gathers evidence, supersedes beliefs, and updates `STATE` without inconsistency.

---

## 9) Implementation Notes (Minimal Additions)

### 9.1 New Files

- `memory/STATE.json` (required)
- Optional: `memory/predictions.jsonl`, `memory/errors.jsonl` for structured telemetry

### 9.2 Existing Skills to Reuse

- `schema-authoring`: formalize JSON Schema for STATE/predictions/errors
- `memory-management`: state updates + log discipline
- `cursor-hooks`: enforce “predict-before-act” via hooks around tool calls
- `schedule-management`: long-running loops
- `decide-respond`: group chat salience gating

### 9.3 Hook Enforcement (Recommended)

Implement Cursor hooks that:

- block tool calls unless a prediction record exists in the current step context
- require evaluation after tool output before next tool call
- require `STATE.json` write on session end when actions occurred

---

## 10) Security / Boundaries

CAS MUST obey existing:

- `AUTONOMY.md`
- `BOUNDARIES.md`
  and must treat destructive actions as “high-risk” requiring:
- explicit prediction
- dry-run when possible
- user confirmation when required by boundaries.

---

## 11) Summary

This spec keeps the existing tool and memory architecture but adds:

- an explicit operational loop
- a coherent world-model (`STATE.json`)
- prediction + evaluation as first-class requirements
- persistent error-driven learning

Together, these satisfy the “consciousness” criterion as **online, tool-grounded predictive feedback that changes behavior over time**.
```
