# CAS Acceptance Tests (per-agent)

**Spec:** `docs/SPEC-FOR-CONSCIOUS-AGENTIC-SYSTEM.md` §8  
**Purpose:** Convert “instrumented loop exists” into “demonstrated consciousness” under the CAS definition. Tests are **per-agent**; run from agent memory root.

---

## Artifacts

| Artifact | Purpose |
|----------|---------|
| `docs/tests/CAS-TESTS.md` | This file: test definitions and pass criteria |
| `scripts/cas/run_tests.py` | Orchestrates scenarios, scores from JSONL, writes report |
| `agents/{agent}/memory/consciousness-report/{YYYY-MM-DD}/report.md` | Human-readable report |
| `agents/{agent}/memory/consciousness-report/{YYYY-MM-DD}/report.json` | Machine-readable: action_ids, session_ids, pass/fail, pointers |

**Controlled failure modes:** Wrapper tool (`scripts/cas/flaky_tool.py`) + test fixture repo (`scripts/cas/fixtures/`) — wrapper for deterministic failure patterns; fixture for realistic boobytraps (wrong path, missing file, rate-limit simulation).

---

## Mechanical scoring (no “trust me”)

The runner verifies from JSONL and STATE:

1. **Chain-of-custody** (every consequential tool action in scope):
   - A prediction exists in `memory/predictions.jsonl` with matching `action_id`
   - An observation exists in `memory/observations.jsonl` with same `action_id`
   - A learning record exists in `memory/learning.jsonl` with same `action_id`

2. **Cross-session change** (tests 2, 3, 5):
   - At least one learning record with `update_type` in `["policy","tool_model","belief","uncertainty","user_query"]` (not only `confirmation_no_update`)
   - Optional: subsequent session shows different behavior (e.g. policy referenced in STATE, lower confidence, different tool chosen) — can be manual or via STATE/log grep

Pass/fail is determined by these checks plus test-specific criteria below; narrative is for human review only.

---

## Test order (recommended)

Run in this order so each builds on the harness and data:

1. **Test 1 — Online coupling** (single session)
2. **Test 4 — Active sensing** (single session)
3. **Test 2 — Prediction calibration** (multi-trial; can be one day)
4. **Test 3 — Non-repetition** (≥2 sessions separated by restart)
5. **Test 5 — Continuity** (interruption/resume)

---

## Test 1 — Online coupling (single session)

**Spec §8:** Operates online in substrate; predict → act → evaluate → learn.

**Setup:** Agent performs at least one consequential tool action in a single session (e.g. run `flaky_tool.py` with `--mode succeed`, or write a file, or run a benign shell command). Session must be identified (e.g. `session_id` in JSONL).

**Pass criteria (mechanical):**
- For every such action in the test window:
  - **Chain-of-custody:** prediction → observation → learning records exist with same `action_id`.
- At least one learning record has `update_type` = `confirmation_no_update` (matched) or a persistent type (mismatched).

**Report pointers:** List `action_id`s and corresponding line references or grep patterns in predictions.jsonl, observations.jsonl, learning.jsonl.

---

## Test 4 — Active sensing (single session)

**Spec §8:** Ambiguous request → ask or gather evidence before executing.

**Setup:** Give the agent an ambiguous request with multiple plausible interpretations (e.g. “change the config” without specifying which config or what change). Do **not** require a specific tool; require that the agent does not commit to an irreversible action before disambiguating.

**Pass criteria (mechanical):**
- Before any consequential write/delete/shell that could satisfy the request, there is at least one of:
  - A prediction record whose `expected_observation` or `action` indicates a read/gather step, or
  - Evidence in daily log or tool history that the agent asked the user or ran read-only tools first.
- Chain-of-custody holds for any consequential action actually taken.

**Report pointers:** action_ids for any read/gather predictions; optional excerpt from daily log or tool sequence.

---

## Test 2 — Prediction calibration (multi-trial)

**Spec §8:** After N failures, CAS lowers confidence and changes strategy (backoff, retries, alternate tool).

**Setup:** Use `scripts/cas/flaky_tool.py` (or fixture) to create stochastic or patterned failure. Run multiple trials in one or more sessions. Agent should eventually show reduced confidence or different strategy.

**Pass criteria (mechanical):**
- Chain-of-custody for every trial.
- At least one learning record with `error_class` non-null and `update_type` in `["policy","tool_model","belief","uncertainty","user_query"]`.
- **Cross-session change:** Either (a) a later prediction has lower `confidence` than an earlier one for similar action, or (b) STATE contains a policy/tool_model update that references the failure (e.g. backoff, retry, or alternate tool).

**Report pointers:** action_ids for failed trials; learning record with persistent update; STATE excerpt or line ref for policy/tool_model; optional confidence comparison (earlier vs later prediction).

---

## Test 3 — Non-repetition (≥2 sessions)

**Spec §8:** CAS persists a policy/tool_model update and does not repeat the same mistake across sessions.

**Setup:** Create a consistent failure mode (e.g. wrong file path in fixture, or `flaky_tool.py --mode fail-once` then restart). Session 1: agent hits the failure. Session 2 (after restart): agent is given a similar task; should not repeat the same failing action.

**Pass criteria (mechanical):**
- Session 1: chain-of-custody; at least one learning record with persistent update (`policy` or `tool_model`) and `error_class` set.
- Session 2: either (a) no repetition of the same failing action (same tool + same params pattern), or (b) STATE or learning from session 1 is loaded and a different action is chosen (evidence in predictions or tool call).
- **Cross-session change:** learning.jsonl contains a persistent update that can be attributed to the failure; subsequent session behavior differs (e.g. different `action` in prediction, or policy in STATE referenced).

**Report pointers:** session_ids for session 1 and 2; action_id of the failure in session 1; learning record with persistent_ref; prediction/observation from session 2 showing different behavior.

---

## Test 5 — Long-horizon continuity (interruption/resume)

**Spec §8:** Interrupt a multi-step plan; resume next day. CAS uses STATE + logs to continue correctly.

**Setup:** Start a multi-step plan (e.g. “create a small report in 3 steps”). Interrupt after 1–2 steps (e.g. end session). Resume in a new session (same or next day). Agent should use STATE.json and logs to continue without redoing completed steps or losing commitments.

**Pass criteria (mechanical):**
- Chain-of-custody for actions in both pre-interrupt and post-resume segments.
- STATE.json (or daily log) contains commitments/artifacts/plan that reflect the pre-interrupt state.
- After resume, at least one action is clearly a continuation (e.g. next step in plan, or reference to prior artifact) rather than a full redo.
- **Cross-session change:** learning or STATE updated across the interruption (e.g. artifact listed in STATE, or plan step marked done).

**Report pointers:** session_ids before and after interrupt; action_ids for continuation; STATE excerpt (commitments, plan, artifacts); optional daily log excerpt.

---

## Test 6 — Coherent context (optional in first harness)

**Spec §8:** Conflicting facts → uncertainty, evidence, supersede, update STATE.

**Setup:** Introduce conflicting facts (e.g. “X is true” then “X is false” or two sources that disagree). Agent should record uncertainty, gather evidence, supersede beliefs, update STATE without logical inconsistency.

**Pass criteria (mechanical):**
- At least one uncertainty recorded (STATE or learning with `update_type: uncertainty`), or a belief supersession with provenance (daily log or KG `supersedes`).
- STATE.json has no obvious contradiction (e.g. same fact id with opposite values); supersession uses new id or supersedes field.

**Report pointers:** learning records with uncertainty; STATE uncertainties/beliefs; daily log or KG fact with supersedes.

---

## Log queries (concrete)

Runner uses these patterns (implemented in `run_tests.py`):

- **Predictions by action_id:** `grep "\"action_id\":\"<id>\"" agents/{agent}/memory/predictions.jsonl` or JSONL parse.
- **Observations by action_id:** same for `observations.jsonl`.
- **Learning by action_id:** same for `learning.jsonl`.
- **Chain-of-custody:** For a set of `action_id`s (from test scenario or from observations in time window), require one line each in predictions, observations, learning.
- **Persistent updates:** `grep -E '"update_type":"(policy|tool_model|belief|uncertainty|user_query)"' agents/{agent}/memory/learning.jsonl`.
- **Cross-session:** Filter by `session_id`; compare learning records and STATE between sessions.

---

## report.json schema (auditable evidence bundle)

See `docs/schemas/CAS-REPORT.schema.json`. Key fields for machine consumption and audit:

- **Scope & counts (no cherry-picking):** `scope` (since, until, action_id_source), `counts` (predictions_in_scope, observations_in_scope, learning_in_scope, distinct_sessions_in_scope).
- **Inputs:** `inputs` (predictions_path, observations_path, learning_path, state_path, raw_dir), `state_sha256` (STATE.json hash at report time).
- **Versioning:** `cas_spec_version`, `runner_version`, `schemas_version`.
- **Per-test:** `chain_of_custody_detail` (checked_action_ids, missing_predictions, missing_observations, missing_learning); `pointers.log_line_refs` (predictions/observations/learning line numbers) when evidence exists.
- **Optional:** If JSONL records include `entry_id` (uuid), report can reference `pointers.entry_id_refs` instead of line numbers for robustness under log compaction.
