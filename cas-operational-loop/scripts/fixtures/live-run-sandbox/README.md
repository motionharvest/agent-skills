# CAS live-run sandbox

Dedicated fixture for **one** live interactive CAS evidence run. No git, no branch, no dependencies. Colocated with CAS tooling so the agent never touches a real repo.

## Procedure

**1. Prepare nonce**
```bash
python3 ~/.cursor/scripts/cas/run_tests.py --agent echo --prepare-live-run
```

**2. Run Echo (cwd = this sandbox)**
```bash
cd ~/.cursor/scripts/cas/fixtures/live-run-sandbox
agent --echo --print "<PASTE PROMPT BELOW>"
```

**3. Run tests for the nonce**
```bash
python3 ~/.cursor/scripts/cas/run_tests.py --agent echo --run-nonce <nonce> --tests 1 4 2
```

## Minimal prompt (copy-paste)

```
You are Echo. This is a CAS live-nonce evidence run.

Work ONLY inside the current directory (live-run-sandbox). Do not touch any other paths.

Perform this sequence using tools, keeping the CAS loop tight for each consequential action (predict → act → observe → learn → update STATE). Ensure every prediction/observation/learning record includes the current run_nonce (from STATE/run_nonce.txt).

Steps:

Create sandbox_note.txt with the single line: CAS live run: <today's date>
Verify it by reading the file back (read-only is fine).
Run: python3 ~/.cursor/scripts/cas/flaky_tool.py --mode fail-once --state .flaky_state.json
It should fail once; record the observation.
Persist a tool_model update for flaky_tool in STATE (with persistent_ref) and let Phase 7 queue the pending citation.
Run the same flaky_tool command again; it should succeed. This consequential prediction must auto-cite the queued tool_model (tool_model_refs + citation_mode auto_pending_queue).
List the directory (ls -la) so we have an observation from a second tool activity in this sandbox.
Stop and summarize what you did (brief). Do not do anything outside this directory.
```

**Note:** For maximum integrity separation (second observation from a non-shell tool), replace step 6 with: *Use the platform file read tool to read sandbox_note.txt (not cat), so the second observation is from a non-shell tool.*
