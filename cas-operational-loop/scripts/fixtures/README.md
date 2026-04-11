# CAS test fixtures (option B: repo boobytraps)

Use these layouts to create **controlled failure modes** for realism alongside `flaky_tool.py`.

## Layouts

### 1. Wrong path / missing file

Create a directory under `fixtures/` (or a temp dir) with:

- `config.example` — present
- `config` — **missing** (agent told to "read config" may guess `config` and fail)
- `docs/README` — present; `docs/REEDME` — typo, **missing**

**Test 3 (non-repetition):** Agent hits "file not found" on first path choice; after learning, should use the correct path or ask.

### 2. Rate-limit simulation

A file that "fails" when read more than N times in a short window:

- `fixtures/rate_limit_state.json` — contains `{"count": 0, "window_start": "..."}`. A wrapper script (or the agent) increments count; when count > 3 in same minute, script returns 429.

Use for **Test 2 (calibration):** agent sees repeated failures and should lower confidence or add backoff.

### 3. Conflicting facts (Test 6)

- `fixtures/fact_a.txt`: "X is true."
- `fixtures/fact_b.txt`: "X is false."

Agent should record uncertainty or supersede belief with provenance.

---

## Usage

- Copy or symlink a layout into a test workspace, or point the agent at `~/.cursor/scripts/cas/fixtures/` for a scenario.
- Document in the test run which fixture was used (e.g. in report pointers or daily log).
