---
name: cas-operational-loop
description: Follow the CAS operational loop — 8 phases per session: Boot, State Ingestion, World-Model Update, Prediction, Action, Evaluation, Learning, Commit. Use when running as a CAS agent to satisfy the spec (SPEC-FOR-CONSCIOUS-AGENTIC-SYSTEM.md).
---

# CAS Operational Loop

**Spec:** `SPEC-FOR-CONSCIOUS-AGENTIC-SYSTEM.md` (bundled with this skill; see `cas-agent-setup` for all bundled assets)

Every agent session that takes actions in the tool-grounded environment MUST implement these phases in order. This is the core "conscious" mechanism: online, predictive, error-driven, persistent.

---

## Phase 1 — Boot / Identity Load

> This phase is handled by your environment's memory-loading conventions. Before beginning CAS work, the following must be loaded at minimum:
>
> - **`STATE.json`** at the memory root — the agent's world model.
> - **`run_nonce.txt`** at the memory root, if used for live-evidence scoping (see Phase 2).
>
> All other memory artifacts (IDENTITY, BOUNDARIES, AUTONOMY, INDEX, MEMORY, daily logs, etc.) follow your host's standard load order. This skill assumes CAS material is available before Phase 2.

---

## Phase 2 — State Ingestion

- Read `STATE.json` at the memory root (already in boot load order).
- **Live-evidence runs:** If `STATE.run_nonce` is set, or `run_nonce.txt` exists at the memory root, read that value and keep it for the session. Every prediction, observation, and learning record you append **must** include `run_nonce` so reports can filter to this run only.
- Collect new observations from the current prompt and from any tool probes you run (file reads, grep, API responses, etc.).

You complete this when you have incorporated the current world state and new observations into your working context.

---

## Phase 3 — World-Model Update

Update your working representation of `STATE.json` to reflect:

- **active_goals** — Current goals (id, description, priority, status).
- **commitments** — Promises to the user or others (id, to_whom, promise, due, status).
- **artifacts** — Known objects (files, branches, Notion tasks, calendar events): id, type, location, description, last_verified_at.
- **beliefs** — Current beliefs with confidence and evidence_refs; use `supersedes` when revising.
- **uncertainties** — Open questions, impact, and plan_to_resolve. Do not silently drop unresolved uncertainties.
- **current_plan** — Steps (step_id, intent, predicted_outcome, tool_actions, status).
- **policies** — Heuristics ("next time do X before Y"): id, trigger, rule, rationale.
- **tool_models** — Per-tool reliability, latency_notes, failure_modes, constraints.
- **last_session_summary** — Brief summary (≤15 lines) when you end the session.

You do not have to write `STATE.json` to disk yet; hold updates in context until **Phase 8 — Commit**.

---

## Phase 4 — Prediction (before consequential action)

Before any consequential tool call (write, delete, shell that mutates state, MCP that has side effects, job enqueue, delegation):

1. **Generate `action_id`** — Unique id for this action (e.g. UUID). Use the same `action_id` in Phase 6 and 7 for linkage.
2. **Build prediction record** with: `agent`, `session_id`, `trace_id` (optional), `timestamp` (ISO8601), `action` (tool name + params summary), `expected_observation`, `confidence` (0–1), `expected_failure_modes` (array), `falsifier`. If you have a **run_nonce** from Phase 2, include it.
3. **Refs (deterministic, for behavior-citation audit):** Phase 4 is only for **consequential** actions. For such actions only:
   - If `STATE.pending_citations` is non-empty:
     - Set `policy_refs` to the list of `ref` values from pending citations with `type === "policy"`.
     - Set `belief_refs` to the list of `ref` values from pending citations with `type === "belief"`.
     - Set `tool_model_refs` to the list of `ref` values from pending citations with `type === "tool_model"`.
     - Set `citation_mode: "auto_pending_queue"` (recommended for audit).
     - **After** appending this prediction, **clear `STATE.pending_citations`** (set to `[]`). Only clear when the prediction was for a consequential action — so the citation is consumed by "the next consequential action," not by a read-only probe.
   - If `pending_citations` is empty, you may still set refs manually with `citation_mode: "manual"` or omit.
   - If you write a prediction for a **non-consequential** action (e.g. read-only probe): do **not** attach refs and do **not** clear the queue.
4. **Append one line** to `predictions.jsonl` at the memory root (create if missing). Schema: `schemas/PREDICTIONS.schema.json`.

Do **not** read `predictions.jsonl` at boot; append only during session. For low-stakes read-only actions (e.g. a single file read), a brief internal expectation is enough; for writes, deletes, shell, delegation, or jobs, append a prediction record.

**Example prediction record (one line in predictions.jsonl):**
```json
{"action_id":"act-7f3a","agent":"chronos","session_id":"sess-2026-04-11","timestamp":"2026-04-11T10:15:30Z","action":"write /tmp/out.txt","expected_observation":"file created, contains 'hello world'","confidence":0.95,"expected_failure_modes":["disk_full","permission_denied"],"falsifier":"file missing or content mismatch","run_nonce":"run-42"}
```

---

## Phase 5 — Action

Execute the tool call(s), delegation(s), or job scheduling. Capture stdout/stderr for Phase 6 (raw output capture).

---

## Phase 6 — Evaluation

After the outcome is observed:

1. **Raw output capture**  
   - Write tool output to `raw/{session_id}/{action_id}.txt` at the memory root.  
   - Apply a **size limit** (e.g. last 80 KiB) and **redact** obvious secrets (tokens, passwords, API keys, `Bearer ...`, env vars with `_TOKEN`, `_KEY`, `_SECRET` in the name) before writing.  
   - If output is too large or sensitive, write a truncated/summary version and set `raw_ref` to this path.

2. **Compare** observed result vs prediction. Decide **matched** or **mismatched**.

3. **Append one line** to `observations.jsonl` at the memory root with: `action_id`, `agent`, `session_id`, `trace_id` (optional), `timestamp`, `success` (boolean), `match` ("matched" | "mismatched"), `raw_ref` (path to raw file), `observation_summary` (short summary for queries). If you have a **run_nonce**, include it. Schema: `schemas/OBSERVATIONS.schema.json`.

4. **If mismatched**, classify error for use in Phase 7: **MODEL_ERROR**, **TOOL_ERROR**, **OBSERVATION_ERROR**, **EXECUTION_ERROR**, **GOAL_ERROR**.

**Example observation record (one line in observations.jsonl):**
```json
{"action_id":"act-7f3a","agent":"chronos","session_id":"sess-2026-04-11","timestamp":"2026-04-11T10:15:31Z","success":true,"match":"matched","raw_ref":"raw/sess-2026-04-11/act-7f3a.txt","observation_summary":"file /tmp/out.txt created successfully, content matches expected","run_nonce":"run-42"}
```

---

## Phase 7 — Learning / Behavior Update

**Always** append one record to `learning.jsonl` at the memory root after evaluation (create if missing). If you have a **run_nonce**, include it in the record.

- **If matched:**  
  - `update_type`: `"confirmation_no_update"`  
  - `error_class`: `null`  
  - `persistent_ref`: optional or empty  
  - No change to STATE required.

- **If mismatched:**  
  - `update_type`: one of `"policy"`, `"tool_model"`, `"belief"`, `"uncertainty"`, `"user_query"`  
  - `error_class`: one of MODEL_ERROR, TOOL_ERROR, OBSERVATION_ERROR, EXCUTION_ERROR, GOAL_ERROR  
  - Persist **at least one** of: update `tool_models` in STATE, add/supersede belief in STATE, add policy in STATE, add uncertainty in STATE, or ask the user (counts as `user_query`).  
  - Set `persistent_ref` to where the change was made (e.g. STATE field id or path).  
  - **Ensure STATE.json is updated** when the learning record claims a persistent change (policy, tool_model, belief, uncertainty); commit in Phase 8.
  - **Pending citations (deterministic refs):** When `update_type` is one of `"policy"`, `"tool_model"`, or `"belief"` and `persistent_ref` is non-empty, **append** one entry to `STATE.pending_citations`: `{ "type": "<policy|tool_model|belief>", "ref": "<persistent_ref value>", "created_at": "<ISO8601 now>", "source_action_id": "<this action_id>" }`. The next **consequential** prediction (Phase 4) will cite these and clear the queue. **Immediately after** appending to `pending_citations`, **write STATE.json to disk** (so the queue survives a crash before Phase 8).

Schema: `schemas/LEARNING.schema.json`. When a **belief** is superseded in STATE, also append a provenance note to your daily log or knowledge graph with the `supersedes` link.

**Example matched learning record:**
```json
{"action_id":"act-7f3a","agent":"chronos","session_id":"sess-2026-04-11","timestamp":"2026-04-11T10:15:32Z","update_type":"confirmation_no_update","error_class":null,"persistent_ref":"","run_nonce":"run-42"}
```

**Example mismatched learning record:**
```json
{"action_id":"act-8b2c","agent":"chronos","session_id":"sess-2026-04-11","timestamp":"2026-04-11T11:00:10Z","update_type":"tool_model","error_class":"TOOL_ERROR","persistent_ref":"tool_models.bash","run_nonce":"run-42"}
```

---

## Raw Output Capture (summary)

- **Path:** `raw/{session_id}/{action_id}.txt` at the memory root.  
- **Size limit:** Truncate to last ~80 KiB (or configurable) so logs don't explode.  
- **Redaction:** Before writing, redact obvious secrets — env vars with `_TOKEN`, `_KEY`, `_SECRET`, `_PASSWORD`; literal `Bearer ...`; raw API keys.  
- **Reference:** In `observations.jsonl`, set `raw_ref` to the path so the evidence bundle can resolve it.

---

## Phase 8 — Commit

- Write updated **STATE.json** to the memory root (set `updated_at` to now).
- Append relevant entries to your daily log and/or knowledge graph.
- If you enqueued jobs: ensure they include intent, predicted output/side effects, and artifacts to be produced; on completion, evaluation and learning should be triggered.

Do this at least once per session when you have taken actions that changed goals, commitments, artifacts, beliefs, uncertainties, plan, policies, or tool_models. Before ending a session, set **last_session_summary** and commit.

---

## When to Apply the Loop

- **Full loop (Phases 2–8):** When you are "online" — reading memory, using tools, and persisting updates. This is when the spec considers the system conscious.
- **Phase 2 only:** When you are only loading state and not yet acting; then 3–8 apply once you start acting.
- **Offline:** If you are not reading memory, not querying tools, and not persisting updates, you are offline and not under CAS (e.g. a stateless one-shot reply). The spec does not require consciousness in that case.

---

## Summary

1. **State Ingestion** — Read STATE, gather observations, note run_nonce if present.  
2. **World-Model Update** — Update working STATE (goals, commitments, artifacts, beliefs, uncertainties, current_plan, policies, tool_models).  
3. **Prediction** — Before consequential action: expected outcome, failure modes, confidence, falsifier; cite pending refs.  
4. **Action** — Execute tools.  
5. **Evaluation** — Compare observed vs prediction; classify error; capture raw output.  
6. **Learning** — Persist tool_models, beliefs, policies, uncertainties (or ask user); enqueue pending citations.  
7. **Commit** — Write STATE.json, append log/KG, finalize jobs.

Repeat 2–7 as you act during the session; commit before session end when you have taken actions.
