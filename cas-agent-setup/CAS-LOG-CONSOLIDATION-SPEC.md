# Spec Addendum: CAS Log Consolidation (“Morning Practice” / Archival)

**Status:** Draft  
**Applies to:** Each agent under `{agent-root}/memory/`  
**Goal:** Prevent unbounded growth of CAS telemetry (`predictions.jsonl`, `observations.jsonl`, `learning.jsonl`, `raw/`) while preserving:
- auditability (reports reproducible via `run_nonce`/date scoping),
- continuity (durable updates remain in `STATE.json`),
- low boot cost (CAS logs still “do not read at boot”).

This spec is a follow-up to: “CAS JSONL is append-only; no consolidation step exists yet.”

---

## 1) Definitions

### 1.1 CAS Telemetry (hot logs)
Append-only files in the agent memory root:
- `predictions.jsonl`
- `observations.jsonl`
- `learning.jsonl`
- `raw/{session_id}/{action_id}.txt`

### 1.2 Durable Knowledge (must survive consolidation)
Durable items are those that change future behavior or long-horizon context:
- `STATE.policies[*]`
- `STATE.tool_models[*]`
- `STATE.beliefs[*]`
- `STATE.commitments[*]`
- `STATE.artifacts[*]`

### 1.3 Evidence windows
An “evidence window” is a bounded slice of telemetry referenced by:
- `run_nonce` (preferred) or
- `since/until` timestamps

Evidence windows MUST remain reproducible after consolidation.

---

## 2) Design Principles / Constraints

1. **Boot stays light:** Consolidation must not increase boot reads.
2. **No silent loss of durability:** Any learning record with a persistent update MUST be reflected in `STATE.json` before archival.
3. **Auditability preserved:** Reports generated for a given `run_nonce` remain possible either from hot logs or archives.
4. **Low-token / mechanical by default:** Consolidation is deterministic and scriptable; reflective summarization is optional and bounded.
5. **Append-only semantics preserved:** Hot logs remain append-only; consolidation moves/copies lines to archives but does not rewrite history content.

---

## 3) Required Files / Directories

Per agent:

- `memory/archive/cas/` (directory)
  - `YYYY-MM/` subdirs (one per month)
- `memory/cas-index.jsonl` (append-only index of archival runs; small)

Optional:
- `memory/archive/cas/reports/` (store report.json/report.md snapshots)

---

## 4) Consolidation Policy (Default)

### 4.1 Retention (hot logs)
Keep in hot logs:
- records from the last **N days** (default: 7) OR last **M MB** (default: 50MB), whichever is smaller.

Everything older is eligible for archival.

### 4.2 Protect active evidence windows
Never archive records if they match:
- current `STATE.run_nonce` (active live-evidence run), or
- a configured “protected nonce list” (optional), or
- a time window that includes “today” (safety buffer).

### 4.3 Raw outputs
Raw outputs follow the same retention rule as observations:
- if all observations for a given `session_id` are archived, the corresponding `raw/{session_id}/` directory is moved to the archive.

---

## 5) Archival Format

### 5.1 Archive paths — rotation
When consolidating, **rotate** hot logs into the archive; do not rewrite them in place.

**Rotated filenames** (written into `memory/archive/cas/YYYY-MM/`):
- `predictions.{YYYY-MM-DD}.jsonl` — snapshot of hot predictions at rotation time
- `observations.{YYYY-MM-DD}.jsonl`
- `learning.{YYYY-MM-DD}.jsonl`

Same-day consolidations append to the same rotated file (so one file per day per type, per month dir). Raw dirs:
- `raw/{session_id}/` → moved to `memory/archive/cas/YYYY-MM/raw/{session_id}/`

**After rotation:** New empty `predictions.jsonl`, `observations.jsonl`, `learning.jsonl` in the agent memory root (hot logs). No in-place rewrite of hot files; history lives only in archives.

### 5.2 cas-index.jsonl (required)
Each consolidation run appends one entry:

```json
{
  "ts": "2026-02-12T03:00:00Z",
  "agent": "echo",
  "archived_since": "2026-01-01T00:00:00Z",
  "archived_until": "2026-02-01T23:59:59Z",
  "run_nonces": ["..."],
  "session_ids": ["sess-..."],
  "counts": {
    "predictions": 1200,
    "observations": 1200,
    "learning": 1200,
    "raw_files": 980
  },
  "archive_root": "memory/archive/cas/2026-02/",
  "rotated_files": [
    "predictions.2026-02-01.jsonl",
    "observations.2026-02-01.jsonl",
    "learning.2026-02-01.jsonl"
  ]
}
```

Purpose: make “find evidence for run_nonce X” cheap (search index, then read from archive_root + rotated_files or by session_id in raw/).

---

## 6) Durability Check (Required Gate Before Archival)

Before archiving any learning records, the consolidator MUST verify:

For every `learning.jsonl` record eligible for archival with:
- `update_type in {"policy","tool_model","belief"}`
- `persistent_ref` non-empty

Then:
1) `STATE.json` contains the referenced object in the corresponding section.
2) If not, the consolidator MUST:
   - mark the record as “not safe to archive” and leave it hot, OR
   - attempt to repair by forcing a `STATE` sync (only if deterministic and safe).

**Default behavior:** do not repair automatically; keep hot and log a warning.

This prevents losing behavior-changing knowledge to cold storage.

---

## 7) Consolidation Procedure (Mechanical, Required)

### 7.1 Trigger / Schedule
Per agent, run:
- daily at low-activity time (e.g., 03:00 local), AND/OR
- when hot telemetry exceeds M MB.

### 7.2 Steps (deterministic)
1) Load `STATE.json`.
2) Determine eligible record set by timestamp retention and protected nonce rules.
3) Run durability check (§6). Exclude any learning records that fail from archival.
4) **Rotate** (see §8): rename hot files to `predictions.{ROTATE_DATE}.jsonl`, etc.; move to `memory/archive/cas/YYYY-MM/`. Move eligible `raw/{session_id}/` to archive. Create new empty hot files in memory root. (No rewrite of hot file content; only move.)
5) Append one entry to `cas-index.jsonl`.
6) Write a brief “consolidation note” to today’s daily log:
   - how many lines archived
   - where archived
   - any warnings (durability check failures)

---

## 8) Hot Log Strategy

**Rotation only — never rewrite hot log content.**

### 8.1 How it works
- **Retention window:** Keep records from the last **N days** (default 7) in the hot files. When consolidating, the *entire* current hot file is rotated out (no line-by-line filter); retention is “keep the most recent hot file that covers the last N days” or “rotate when hot file exceeds M MB.”
- **Rotation:** Rename `predictions.jsonl` → `predictions.{ROTATE_DATE}.jsonl` (same for observations, learning); move to `memory/archive/cas/YYYY-MM/`. Create new empty hot files in memory root. Move `raw/{session_id}/` for session_ids whose observations are in the rotated set.
- **Append-only preserved:** Rotated files in the archive are never modified. Hot files are only appended to until the next rotation.

### 8.2 Exact archive filenames
- `memory/archive/cas/YYYY-MM/predictions.YYYY-MM-DD.jsonl`
- `memory/archive/cas/YYYY-MM/observations.YYYY-MM-DD.jsonl`
- `memory/archive/cas/YYYY-MM/learning.YYYY-MM-DD.jsonl`
- `memory/archive/cas/YYYY-MM/raw/{session_id}/{action_id}.txt`

Same-day reruns: append to existing `predictions.YYYY-MM-DD.jsonl` (and same for observations/learning) so archives stay append-only.

---

## 9) Optional Reflective Layer (Bounded, Not Required)

On a weekly cadence, the agent MAY:
- read only `STATE.last_session_summary` + `cas-index.jsonl` entries for the week
- write ≤ 15 bullets into `MEMORY.summary.md` (durable principles) and/or `life/{agent}/memories.jsonl` (personal reflections)

Hard constraints: max inputs loaded; max output bullets; no long prose.

---

## 10) Interfaces / Tooling

### 10.1 Script (recommended)
Add `scripts/cas/consolidate.py` next to your agent scripts tree (not hardcoded to any editor install).

CLI:
```bash
python3 scripts/cas/consolidate.py --agent echo \
  --retain-days 7 --retain-mb 50 \
  --protect-active-nonce true
```

### 10.2 Scheduling
Use existing schedule-management or job queue to run the script daily (e.g. 03:00).

### 10.3 Runner support for archived nonces
Your test runner SHOULD support generating a report for a `run_nonce` that has been archived: resolve `run_nonce` via `cas-index.jsonl` (find entry whose `run_nonces` or time range includes it), then load predictions/observations/learning from the referenced `archive_root` + rotated files (or by scanning archive for matching `run_nonce` in lines). No change to report schema; only input paths become “hot logs OR archive paths.”

---

## 11) Acceptance Criteria

Consolidation is “implemented” when:

1) Hot logs do not grow without bound (rotation enforced).
2) Archives exist and contain rotated files.
3) `cas-index.jsonl` records each consolidation run.
4) Durability check prevents archiving any persistent update missing from STATE.
5) CAS runner can generate a report for a nonce in hot logs OR for a nonce in archives (via index + archive paths).

---

## 12) Notes / Rationale

- CAS consciousness depends on **online loop + STATE**, not on keeping all telemetry hot.
- Telemetry is for audit/debugging; keep it searchable but cold by default.
- The index is the middle ground: low boot cost, high retrieval efficiency.
- Rotation preserves “append-only” for the historical record; the hot file is the current window only.
</think>
<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>
StrReplace