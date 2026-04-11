---
name: cas-agent-setup
description: Create or update CAS persistence for an agent — STATE, append-only telemetry, raw capture, optional archival, and tests. Use when adding CAS storage to a new or existing agent. How to run the loop lives in cas-operational-loop.
---

# CAS Agent Setup

**Purpose:** Ensure the agent has the **files and directories** CAS needs: `STATE.json`, append-only telemetry, raw output store, optional archive layout, and a test harness. **How to run the 8-phase loop** (predict → act → observe → learn → commit) is defined only in **`cas-operational-loop`** — load that skill when executing CAS, not this one.

**When to use:** First-time CAS layout on an agent, or aligning an existing agent with the CAS file contract.

**Related skill:** `cas-operational-loop` — operational procedure, phases, and schemas by name.

---

## 0. Bundled Assets (ship with this skill)

This skill ships helper files in its directory. Copy or symlink them into your deployment:

| Asset | Bundled path | Purpose |
|-------|-------------|---------|
| STATE template | `STATE.template.json` | Blank STATE.json with all required fields; use as the starting point. |
| Conscious agent spec | `SPEC-FOR-CONSCIOUS-AGENTIC-SYSTEM.md` | Full spec: consciousness definition, error taxonomy, test requirements. |
| Consolidation spec | `CAS-LOG-CONSOLIDATION-SPEC.md` | Archival policy, rotation strategy, durability check, tooling interface. |
| CAS acceptance tests | `tests/CAS-TESTS.md` | Per-agent test definitions: online coupling, prediction calibration, non-repetition, continuity, active sensing. |
| STATE schema | `schemas/STATE.schema.json` | JSON Schema for `STATE.json` fields and required structure. |
| Predictions schema | `schemas/PREDICTIONS.schema.json` | JSON Schema for `predictions.jsonl` records. |
| Observations schema | `schemas/OBSERVATIONS.schema.json` | JSON Schema for `observations.jsonl` records. |
| Learning schema | `schemas/LEARNING.schema.json` | JSON Schema for `learning.jsonl` records. |
| CAS Report schema | `schemas/CAS-REPORT.schema.json` | JSON Schema for test-run reports. |

Report output goes to `{agent-root}/memory/consciousness-report/{YYYY-MM-DD}/` (report.md + report.json) when you run the test harness.

---

## 1. Paths (under the agent's memory root)

Use the same root your environment uses for agent memory (e.g. `memory/` next to the agent's other persistent files). All paths below are relative to that root.

| Artifact | Path | Notes |
|----------|------|--------|
| World model | `STATE.json` | Align fields with `STATE.schema.json`. |
| Predictions | `predictions.jsonl` | Append-only; create if missing; do not bulk-read at session start. |
| Observations | `observations.jsonl` | Append-only; create if missing. |
| Learning | `learning.jsonl` | Append-only; create if missing. |
| Raw tool output | `raw/{session_id}/{action_id}.txt` | Store/redact/truncate per cas-operational-loop; link from observations. |
| Run scope (optional) | `run_nonce.txt` | If used, cas-operational-loop requires `run_nonce` on prediction/observation/learning lines. |

**Consequential actions** (writes, deletes, mutating shell, side-effecting APIs, jobs, delegation) must follow the loop in **`cas-operational-loop/SKILL.md`**, including appending predictions before action and observations/learning after.

---

## 2. Schemas and specs

Symlink or copy the bundled schemas/specs into your deployment. Document their location in your agent's INDEX so the loop skill and test runner can find them.

| Topic | Bundled path |
|--------|-------------|
| Conscious agent spec | `SPEC-FOR-CONSCIOUS-AGENTIC-SYSTEM.md` |
| STATE schema | `schemas/STATE.schema.json` |
| Predictions schema | `schemas/PREDICTIONS.schema.json` |
| Observations schema | `schemas/OBSERVATIONS.schema.json` |
| Learning schema | `schemas/LEARNING.schema.json` |
| CAS Report schema | `schemas/CAS-REPORT.schema.json` |
| Consolidation spec | `CAS-LOG-CONSOLIDATION-SPEC.md` |

---

## 3. Optional — log consolidation

If you run archival to cap growth of jsonl/raw, see **`CAS-LOG-CONSOLIDATION-SPEC.md`** (bundled). Key layout:

- **Archive root:** `archive/cas/` with monthly subdirs `YYYY-MM/`.
- **Index:** `cas-index.jsonl` at the memory root — one line per consolidation run (timestamps, ranges, counts, rotated filenames).
- **Durability rule:** Before archiving learning lines that claim `persistent_ref` for policy/tool_model/belief updates, confirm `STATE.json` contains that change; otherwise keep the lines hot and surface a warning.

---

## 4. Checklist — new CAS layout

- [ ] `STATE.json` created from `STATE.template.json`, valid against your copy of `schemas/STATE.schema.json`.
- [ ] Empty or seeded `predictions.jsonl`, `observations.jsonl`, `learning.jsonl` at memory root.
- [ ] Directory `raw/` exists (sessions create `raw/{session_id}/` as needed).
- [ ] Symlink or copy bundled schemas/specs into your deployment; document their location in the agent's INDEX.
- [ ] Test harness wired: `tests/CAS-TESTS.md` is reachable; report output dir `consciousness-report/{YYYY-MM-DD}/` is writable.
- [ ] (Optional) `archive/cas/`, `cas-index.jsonl`, consolidation script wired by operators.
- [ ] Agent instructions point consequential work at **`cas-operational-loop`** (this skill does not define boot order or unrelated memory tools).

---

## 5. Checklist — upgrade existing agent

- [ ] Add missing telemetry files and `raw/` if absent.
- [ ] Extend `STATE.json` with CAS fields your schema requires (e.g. `pending_citations`, `run_nonce` if you use scoped runs).
- [ ] Symlink or copy bundled schemas/specs; update the agent's INDEX to point to their location.
- [ ] Test harness reachable: confirm `tests/CAS-TESTS.md` is in scope and report output dir is writable.
- [ ] (Optional) Add archive layout and schedule consolidation (see `CAS-LOG-CONSOLIDATION-SPEC.md`).

---

## 6. References

| Use | Where |
|-----|--------|
| Run the CAS loop | `cas-operational-loop/SKILL.md` |
| Test definitions | `tests/CAS-TESTS.md` (bundled) |
| Consolidation spec | `CAS-LOG-CONSOLIDATION-SPEC.md` (bundled) |
| Conscious agent spec | `SPEC-FOR-CONSCIOUS-AGENTIC-SYSTEM.md` (bundled) |
| Schemas | `schemas/` directory (bundled) |

This skill is **only** the CAS file layout and pointers. Boot order, memory skills, and channel-specific loaders belong elsewhere.
