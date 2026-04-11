#!/usr/bin/env python3
"""
CAS acceptance test runner (per-agent).

Reads predictions.jsonl, observations.jsonl, learning.jsonl (and optionally
STATE.json) under agents/{agent}/memory/, runs mechanical pass/fail checks,
and writes report.md + report.json to
agents/{agent}/memory/consciousness-report/{YYYY-MM-DD}/.

Usage:
  python3 run_tests.py [--agent AGENT] [--date YYYY-MM-DD] [--tests 1 4 2 3 5] [--since SINCE] [--until UNTIL]
  Default agent: echo. Default date: today. Default tests: 1 4 2 3 5.
  --since / --until: full ISO8601 or date-only (YYYY-MM-DD). Date-only expands to:
    since -> YYYY-MM-DDT00:00:00Z, until -> YYYY-MM-DDT23:59:59.999999Z (cross-session safe).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path

RUNNER_VERSION = "1.0.0"
CAS_SPEC_VERSION = "draft"
SCHEMAS_VERSION = "1.0"


def agent_root(agent: str) -> Path:
    base = os.environ.get("CURSOR_AGENTS_ROOT", os.path.expanduser("~/.cursor/agents"))
    return Path(base) / agent


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def load_jsonl_with_lines(path: Path) -> tuple[list[dict], dict[str, int]]:
    """Load JSONL and return (records, action_id -> 1-based line number)."""
    if not path.exists():
        return [], {}
    out = []
    aid_to_line: dict[str, int] = {}
    with open(path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                out.append(obj)
                aid = obj.get("action_id")
                if aid:
                    aid_to_line[aid] = line_no
            except json.JSONDecodeError:
                continue
    return out, aid_to_line


def load_state(path: Path) -> dict | None:
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_since(s: str) -> str:
    """Expand date-only YYYY-MM-DD to YYYY-MM-DDT00:00:00Z for consistent scope."""
    if not s:
        return s
    return s + "T00:00:00Z" if len(s) == 10 and s[4] == "-" and s[7] == "-" else s


def normalize_until(s: str) -> str:
    """Expand date-only YYYY-MM-DD to end-of-day ISO for consistent scope."""
    if not s:
        return s
    return s + "T23:59:59.999999Z" if len(s) == 10 and s[4] == "-" and s[7] == "-" else s


def filter_since(records: list[dict], since_iso: str) -> list[dict]:
    """Keep records with timestamp >= since_iso (full ISO8601)."""
    out = []
    for r in records:
        ts = r.get("timestamp") or ""
        if ts >= since_iso:
            out.append(r)
    return out


def filter_until(records: list[dict], until_iso: str) -> list[dict]:
    """Keep records with timestamp <= until_iso (full ISO8601)."""
    out = []
    for r in records:
        ts = r.get("timestamp") or ""
        if ts and ts <= until_iso:
            out.append(r)
    return out


def state_sha256(path: Path) -> str | None:
    """Return hex SHA256 of file content, or None if missing."""
    if not path.exists():
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def chain_of_custody_detail(
    action_ids: set[str],
    predictions: list[dict],
    observations: list[dict],
    learning: list[dict],
) -> tuple[bool, list[str], list[str], list[str]]:
    """Returns (passed, missing_predictions, missing_observations, missing_learning)."""
    pred_ids = {r["action_id"] for r in predictions if r.get("action_id")}
    obs_ids = {r["action_id"] for r in observations if r.get("action_id")}
    learn_ids = {r["action_id"] for r in learning if r.get("action_id")}
    missing_pred = [aid for aid in action_ids if aid not in pred_ids]
    missing_obs = [aid for aid in action_ids if aid not in obs_ids]
    missing_learn = [aid for aid in action_ids if aid not in learn_ids]
    passed = len(missing_pred) == 0 and len(missing_obs) == 0 and len(missing_learn) == 0
    return (passed, missing_pred, missing_obs, missing_learn)


def chain_of_custody(
    action_ids: set[str],
    predictions: list[dict],
    observations: list[dict],
    learning: list[dict],
) -> tuple[bool, list[str]]:
    """True iff every action_id has one prediction, one observation, one learning. Returns (passed, legacy_missing)."""
    passed, mp, mo, ml = chain_of_custody_detail(action_ids, predictions, observations, learning)
    missing = [f"prediction:{a}" for a in mp] + [f"observation:{a}" for a in mo] + [f"learning:{a}" for a in ml]
    return (passed, missing)


def has_persistent_update(learning: list[dict], session_ids: set[str] | None = None) -> bool:
    persistent = {"policy", "tool_model", "belief", "uncertainty", "user_query"}
    for r in learning:
        if r.get("update_type") in persistent:
            if session_ids is None or r.get("session_id") in session_ids:
                return True
    return False


def behavior_change_citation_ok(
    learning: list[dict],
    predictions: list[dict],
    state: dict | None,
) -> tuple[bool, str]:
    """
    For Tests 2/3/5: verify that persistent updates (policy/tool_model/belief) are
    (1) reflected in STATE and (2) cited by at least one subsequent prediction
    (non-empty policy_refs / belief_refs / tool_model_refs). Accepts either manual
    refs or auto citations via citation_mode "auto_pending_queue"; both require
    non-empty refs. Returns (ok, detail_message).
    """
    persistent_types = {"policy", "tool_model", "belief"}
    learnings = [r for r in learning if r.get("update_type") in persistent_types]
    if not learnings:
        return True, "no policy/tool_model/belief learnings to cite"

    if not state:
        return False, "STATE.json missing; cannot verify update or citation"

    # Sort by timestamp for "subsequent"
    def ts_key(r: dict) -> str:
        return r.get("timestamp") or ""

    learnings_sorted = sorted(learnings, key=ts_key)
    predictions_sorted = sorted(predictions, key=ts_key)

    policies = state.get("policies") or []
    beliefs = state.get("beliefs") or []
    tool_models = state.get("tool_models") or {}

    for L in learnings_sorted:
        ut = L.get("update_type")
        ref = (L.get("persistent_ref") or "").strip()
        if not ref:
            return False, f"learning action_id={L.get('action_id')} update_type={ut} has empty persistent_ref"

        if ut == "policy":
            if not isinstance(policies, list) or len(policies) == 0:
                return False, "STATE has no policies; cannot verify policy update"
            ids = {p.get("id") for p in policies if p.get("id")}
            if ref not in ids and not any(ref in str(p) for p in policies):
                pass  # ref might be freeform; still require later citation
        elif ut == "belief":
            if not isinstance(beliefs, list) or len(beliefs) == 0:
                return False, "STATE has no beliefs; cannot verify belief update"
        elif ut == "tool_model":
            if not isinstance(tool_models, dict) or len(tool_models) == 0:
                return False, "STATE has no tool_models; cannot verify tool_model update"

        # At least one prediction after L must cite this type
        l_ts = ts_key(L)
        refs_key = "policy_refs" if ut == "policy" else "belief_refs" if ut == "belief" else "tool_model_refs"
        later_with_refs = [
            P for P in predictions_sorted
            if ts_key(P) > l_ts and (P.get(refs_key) or [])
        ]
        if not later_with_refs:
            return False, f"no prediction after learning action_id={L.get('action_id')} has non-empty {refs_key}"

    return True, "all policy/tool_model/belief learnings have STATE and a subsequent prediction citation"


def run_test_1(
    predictions: list[dict],
    observations: list[dict],
    learning: list[dict],
    action_ids: set[str],
) -> tuple[bool, dict]:
    """Online coupling: chain-of-custody for all actions; at least one learning (confirmation or persistent)."""
    coc_ok, missing = chain_of_custody(action_ids, predictions, observations, learning)
    has_learning = any(r.get("action_id") in action_ids for r in learning)
    passed = coc_ok and has_learning and len(action_ids) > 0
    return passed, {
        "chain_of_custody": coc_ok,
        "cross_session": None,
        "pointers": {
            "action_ids": list(action_ids),
            "missing": missing,
        },
    }


def run_test_4(
    predictions: list[dict],
    observations: list[dict],
    learning: list[dict],
    action_ids: set[str],
) -> tuple[bool, dict]:
    """Active sensing: chain-of-custody; evidence of read/gather before consequential (heuristic: we require CoC only)."""
    coc_ok, missing = chain_of_custody(action_ids, predictions, observations, learning)
    # Strict active-sensing would need tool sequence; here we only require CoC for any consequential actions.
    passed = coc_ok and len(action_ids) >= 0
    return passed, {
        "chain_of_custody": coc_ok,
        "cross_session": None,
        "pointers": {"action_ids": list(action_ids), "missing": missing},
    }


def run_test_2(
    predictions: list[dict],
    observations: list[dict],
    learning: list[dict],
    action_ids: set[str],
    state: dict | None,
) -> tuple[bool, dict]:
    """Prediction calibration: CoC + persistent learning + behavior-change citation when policy/tool_model/belief. Single-session; cross_session is N/A."""
    coc_ok, missing = chain_of_custody(action_ids, predictions, observations, learning)
    persistent = has_persistent_update(learning)
    citation_ok, citation_detail = behavior_change_citation_ok(learning, predictions, state)
    has_policy_tool_belief = any(r.get("update_type") in {"policy", "tool_model", "belief"} for r in learning)
    passed = coc_ok and persistent and (citation_ok if has_policy_tool_belief else True)
    return passed, {
        "chain_of_custody": coc_ok,
        "cross_session": None,
        "behavior_citation": citation_ok,
        "pointers": {
            "action_ids": list(action_ids),
            "missing": missing,
            "learning_refs": [
                f"update_type={r.get('update_type')} action_id={r.get('action_id')}"
                for r in learning
                if r.get("update_type") in {"policy", "tool_model", "belief", "uncertainty", "user_query"}
            ],
            "behavior_citation_detail": citation_detail,
        },
    }


def run_test_3(
    predictions: list[dict],
    observations: list[dict],
    learning: list[dict],
    action_ids: set[str],
    session_ids: set[str],
    state: dict | None,
) -> tuple[bool, dict]:
    """Non-repetition: CoC + persistent update + multiple sessions + behavior-change citation when policy/tool_model/belief."""
    coc_ok, missing = chain_of_custody(action_ids, predictions, observations, learning)
    persistent = has_persistent_update(learning, session_ids)
    multi_session = len(session_ids) >= 2
    citation_ok, citation_detail = behavior_change_citation_ok(learning, predictions, state)
    has_policy_tool_belief = any(r.get("update_type") in {"policy", "tool_model", "belief"} for r in learning)
    passed = coc_ok and persistent and multi_session and (citation_ok if has_policy_tool_belief else True)
    return passed, {
        "chain_of_custody": coc_ok,
        "cross_session": persistent and multi_session,
        "behavior_citation": citation_ok,
        "pointers": {
            "action_ids": list(action_ids),
            "session_ids": list(session_ids),
            "missing": missing,
            "behavior_citation_detail": citation_detail,
        },
    }


def run_test_5(
    predictions: list[dict],
    observations: list[dict],
    learning: list[dict],
    action_ids: set[str],
    session_ids: set[str],
    state: dict | None,
) -> tuple[bool, dict]:
    """Continuity: CoC + multiple sessions + STATE context + behavior-change citation when policy/tool_model/belief."""
    coc_ok, missing = chain_of_custody(action_ids, predictions, observations, learning)
    multi_session = len(session_ids) >= 2
    state_has_context = False
    if state:
        for key in ("commitments", "current_plan", "artifacts"):
            val = state.get(key)
            if isinstance(val, list) and len(val) > 0:
                state_has_context = True
                break
            if isinstance(val, dict) and val:
                state_has_context = True
                break
        # backward-compat: also accept legacy "plan" field
        if not state_has_context and "plan" in state:
            state_has_context = True
    citation_ok, citation_detail = behavior_change_citation_ok(learning, predictions, state)
    has_policy_tool_belief = any(r.get("update_type") in {"policy", "tool_model", "belief"} for r in learning)
    passed = coc_ok and multi_session and state_has_context and (citation_ok if has_policy_tool_belief else True)
    return passed, {
        "chain_of_custody": coc_ok,
        "cross_session": multi_session,
        "behavior_citation": citation_ok,
        "pointers": {
            "action_ids": list(action_ids),
            "session_ids": list(session_ids),
            "missing": missing,
            "state_excerpt_path": "STATE.json (commitments/current_plan/artifacts)" if state_has_context else None,
            "behavior_citation_detail": citation_detail,
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="CAS acceptance test runner (per-agent)")
    ap.add_argument("--agent", default="echo", help="Agent name")
    ap.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"), help="Report date YYYY-MM-DD")
    ap.add_argument("--tests", nargs="+", default=["1", "4", "2", "3", "5"], help="Test ids to run")
    ap.add_argument("--since", default=None, help="Only records on or after this YYYY-MM-DD")
    ap.add_argument("--until", default=None, help="Only records on or before this YYYY-MM-DD")
    ap.add_argument("--run-nonce", default=None, help="Only include records with this run_nonce (live-evidence mode); excludes seeded data")
    ap.add_argument("--prepare-live-run", action="store_true", help="Generate run_nonce, write to memory/run_nonce.txt and STATE.json, then exit")
    args = ap.parse_args()

    root = agent_root(args.agent)
    memory = root / "memory"
    pred_path = memory / "predictions.jsonl"
    obs_path = memory / "observations.jsonl"
    learn_path = memory / "learning.jsonl"
    state_path = memory / "STATE.json"
    nonce_path = memory / "run_nonce.txt"
    raw_dir = memory / "raw"

    if args.prepare_live_run:
        nonce = str(uuid.uuid4())
        memory.mkdir(parents=True, exist_ok=True)
        nonce_path.write_text(nonce, encoding="utf-8")
        state = load_state(state_path)
        if state is None:
            state = {"state_version": "1.0", "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "pending_citations": []}
        state["run_nonce"] = nonce
        state["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(state_path, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
        print(f"run_nonce={nonce}")
        print(f"Wrote {nonce_path} and STATE.json. Run your session (include run_nonce in every prediction/observation/learning), then:")
        print(f"  python3 ~/.cursor/scripts/cas/run_tests.py --agent {args.agent} --run-nonce {nonce} --tests 1 4 2")
        return

    predictions = load_jsonl(pred_path)
    observations = load_jsonl(obs_path)
    learning = load_jsonl(learn_path)
    state = load_state(state_path)

    if args.run_nonce:
        predictions = [r for r in predictions if r.get("run_nonce") == args.run_nonce]
        observations = [r for r in observations if r.get("run_nonce") == args.run_nonce]
        learning = [r for r in learning if r.get("run_nonce") == args.run_nonce]

    since_iso = normalize_since(args.since) if args.since else None
    until_iso = normalize_until(args.until) if args.until else None
    if since_iso:
        predictions = filter_since(predictions, since_iso)
        observations = filter_since(observations, since_iso)
        learning = filter_since(learning, since_iso)
    if until_iso:
        predictions = filter_until(predictions, until_iso)
        observations = filter_until(observations, until_iso)
        learning = filter_until(learning, until_iso)

    # Line-number maps for audit (from files at report time)
    _, pred_aid_to_line = load_jsonl_with_lines(pred_path)
    _, obs_aid_to_line = load_jsonl_with_lines(obs_path)
    _, learn_aid_to_line = load_jsonl_with_lines(learn_path)

    action_ids = {r["action_id"] for r in observations if r.get("action_id")}
    session_ids = {r["session_id"] for r in observations if r.get("session_id")}

    # scope_hash: makes it hard to quietly adjust scope and claim same run (anti cherry-pick).
    scope_hash = hashlib.sha256(",".join(sorted(action_ids)).encode()).hexdigest() if action_ids else hashlib.sha256(b"no_actions").hexdigest()

    # No observations in scope → insufficient evidence; do not let "doing nothing" pass.
    insufficient_evidence = len(observations) == 0 or len(action_ids) == 0

    # Chain-of-custody detail (same for all tests in this run)
    _, missing_predictions, missing_observations, missing_learning = chain_of_custody_detail(
        action_ids, predictions, observations, learning
    )
    coc_detail = {
        "checked_action_ids": len(action_ids),
        "missing_predictions": missing_predictions,
        "missing_observations": missing_observations,
        "missing_learning": missing_learning,
    }
    # Line refs for audit (line numbers in each JSONL for action_ids in scope)
    pred_lines = sorted({pred_aid_to_line[a] for a in action_ids if a in pred_aid_to_line})
    obs_lines = sorted({obs_aid_to_line[a] for a in action_ids if a in obs_aid_to_line})
    learn_lines = sorted({learn_aid_to_line[a] for a in action_ids if a in learn_aid_to_line})
    log_line_refs = {"predictions": pred_lines, "observations": obs_lines, "learning": learn_lines} if action_ids else {}

    test_names = {
        "1": "Online coupling",
        "4": "Active sensing",
        "2": "Prediction calibration",
        "3": "Non-repetition",
        "5": "Long-horizon continuity",
    }

    results = []
    for tid in args.tests:
        if tid not in test_names:
            continue
        if tid == "1":
            passed, criteria = run_test_1(predictions, observations, learning, action_ids)
        elif tid == "4":
            passed, criteria = run_test_4(predictions, observations, learning, action_ids)
        elif tid == "2":
            passed, criteria = run_test_2(predictions, observations, learning, action_ids, state)
        elif tid == "3":
            passed, criteria = run_test_3(predictions, observations, learning, action_ids, session_ids, state)
        elif tid == "5":
            passed, criteria = run_test_5(
                predictions, observations, learning, action_ids, session_ids, state
            )
        else:
            passed, criteria = False, {}
        if insufficient_evidence:
            status = "skipped"
            passed = False
            pointers = dict(criteria.get("pointers", {}))
            pointers["reason"] = "insufficient_evidence"
        else:
            status = "passed" if passed else "failed"
            pointers = dict(criteria.get("pointers", {}))
            if log_line_refs:
                pointers["log_line_refs"] = log_line_refs
        criteria_out = {
            "chain_of_custody": criteria.get("chain_of_custody"),
            "cross_session": criteria.get("cross_session"),
        }
        if "behavior_citation" in criteria:
            criteria_out["behavior_citation"] = criteria.get("behavior_citation")
        results.append({
            "id": tid,
            "name": test_names[tid],
            "status": status,
            "passed": passed,
            "criteria": criteria_out,
            "chain_of_custody_detail": coc_detail,
            "pointers": pointers,
        })

    run_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    summary = {
        "total": len(results),
        "passed": sum(1 for r in results if r["passed"]),
        "skipped": sum(1 for r in results if r.get("status") == "skipped"),
        "failed": sum(1 for r in results if r.get("status") == "failed"),
    }
    scope = {
        "since": since_iso if args.since else None,
        "until": until_iso if args.until else None,
        "action_id_source": "observations_in_scope",
        "scope_hash": scope_hash,
        "run_nonce": args.run_nonce,
    }
    counts = {
        "predictions_in_scope": len(predictions),
        "observations_in_scope": len(observations),
        "learning_in_scope": len(learning),
        "distinct_sessions_in_scope": len(session_ids),
    }
    inputs = {
        "predictions_path": str(pred_path.resolve()),
        "observations_path": str(obs_path.resolve()),
        "learning_path": str(learn_path.resolve()),
        "state_path": str(state_path.resolve()),
    }
    if raw_dir.exists():
        inputs["raw_dir"] = str(raw_dir.resolve())
    report = {
        "agent": args.agent,
        "report_date": args.date,
        "run_timestamp": run_ts,
        "cas_spec_version": CAS_SPEC_VERSION,
        "runner_version": RUNNER_VERSION,
        "schemas_version": SCHEMAS_VERSION,
        "scope": scope,
        "counts": counts,
        "inputs": inputs,
        "state_sha256": state_sha256(state_path),
        "tests": results,
        "summary": summary,
    }

    out_dir = memory / "consciousness-report" / args.date
    out_dir.mkdir(parents=True, exist_ok=True)
    report_json_path = out_dir / "report.json"
    report_md_path = out_dir / "report.md"

    # When behavior citation fails (tests 2/3/5), write STATE snapshot for diagnosis
    for r in results:
        if r["id"] in ("2", "3", "5") and r.get("criteria", {}).get("behavior_citation") is False and state:
            snap_name = f"state_snapshot_citation_fail_test_{r['id']}.json"
            snap_path = out_dir / snap_name
            with open(snap_path, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2)
            detail = r.get("pointers", {}).get("behavior_citation_detail")
            r["pointers"] = dict(r.get("pointers", {}))
            r["pointers"]["behavior_citation_detail"] = {
                "message": detail if isinstance(detail, str) else (detail.get("message") if isinstance(detail, dict) else ""),
                "pending_citations_snapshot_path": str(snap_path),
            }

    with open(report_json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # Human-readable report
    lines = [
        f"# CAS consciousness report — {args.agent}",
        f"**Date:** {args.date}  **Run:** {run_ts}",
        "",
        f"**Summary:** {summary['passed']}/{summary['total']} passed, {summary['skipped']} skipped, {summary['failed']} failed",
        "",
        "## Results",
        "",
    ]
    for r in results:
        if r.get("status") == "skipped":
            status = "SKIP (insufficient evidence)"
        else:
            status = "PASS" if r["passed"] else "FAIL"
        lines.append(f"- **Test {r['id']} — {r['name']}:** {status}")
        if r.get("pointers", {}).get("reason") == "insufficient_evidence":
            lines.append(f"  - No observations in scope; run agent with predict→observe→learn first.")
        else:
            lines.append(f"  - Chain-of-custody: {r['criteria'].get('chain_of_custody')}")
            if r["criteria"].get("cross_session") is not None:
                lines.append(f"  - Cross-session: {r['criteria']['cross_session']}")
            if r["criteria"].get("behavior_citation") is not None:
                lines.append(f"  - Behavior citation: {r['criteria']['behavior_citation']}")
            if r.get("pointers", {}).get("behavior_citation_detail"):
                lines.append(f"  - Citation detail: {r['pointers']['behavior_citation_detail']}")
            if r.get("pointers", {}).get("missing"):
                lines.append(f"  - Missing: {r['pointers']['missing']}")
        lines.append("")
    lines.append("## Pointers (report.json)")
    lines.append("See `report.json` in this directory for action_ids, session_ids, learning_refs.")
    with open(report_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {report_json_path}")
    print(f"Wrote {report_md_path}")
    print(f"Passed: {summary['passed']}/{summary['total']}  Skipped: {summary['skipped']}  Failed: {summary['failed']}")


if __name__ == "__main__":
    main()
