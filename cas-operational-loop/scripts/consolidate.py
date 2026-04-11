#!/usr/bin/env python3
"""
CAS log consolidation (Option B rotation). See docs/CAS-LOG-CONSOLIDATION-SPEC.md.

Rotates hot predictions/observations/learning to memory/archive/cas/YYYY-MM/,
appends to cas-index.jsonl, writes consolidation note to daily log.
Durability check: do not rotate if any learning record with persistent_ref
is missing from STATE (policy/tool_model/belief).
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_RETAIN_DAYS = 7
DEFAULT_RETAIN_MB = 50


def agent_memory_root(agent: str) -> Path:
    root = Path(os.environ.get("CURSOR_AGENTS_ROOT", Path.home() / ".cursor" / "agents"))
    return root / agent / "memory"


def load_state(memory_root: Path) -> dict | None:
    p = memory_root / "STATE.json"
    if not p.exists():
        return None
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


def load_jsonl_raw(path: Path) -> list[str]:
    """Return list of raw lines (for append to archive without re-parse)."""
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


def durability_check(learning_records: list[dict], state: dict) -> list[str]:
    """Return list of warnings (persistent_ref not in STATE)."""
    warnings = []
    persistent_types = {"policy", "tool_model", "belief"}
    for rec in learning_records:
        if rec.get("update_type") not in persistent_types:
            continue
        ref = rec.get("persistent_ref") or ""
        if not ref.strip():
            continue
        # Check STATE has this ref
        if rec.get("update_type") == "policy":
            policies = state.get("policies") or []
            if not any(str(p.get("id")) == ref for p in policies):
                warnings.append(f"learning persistent_ref policy {ref!r} not in STATE.policies")
        elif rec.get("update_type") == "tool_model":
            tool_models = state.get("tool_models") or {}
            if ref not in tool_models:
                warnings.append(f"learning persistent_ref tool_model {ref!r} not in STATE.tool_models")
        elif rec.get("update_type") == "belief":
            beliefs = state.get("beliefs") or []
            if not any(str(b.get("id")) == ref for b in beliefs):
                warnings.append(f"learning persistent_ref belief {ref!r} not in STATE.beliefs")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="CAS log consolidation (Option B rotation)")
    parser.add_argument("--agent", default="echo", help="Agent name")
    parser.add_argument("--retain-days", type=int, default=DEFAULT_RETAIN_DAYS)
    parser.add_argument("--retain-mb", type=float, default=DEFAULT_RETAIN_MB)
    parser.add_argument("--protect-active-nonce", action="store_true", default=True, help="Skip rotate if STATE.run_nonce present in hot logs")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be done, do not write")
    args = parser.parse_args()

    memory_root = agent_memory_root(args.agent)
    if not memory_root.exists():
        print(f"Memory root not found: {memory_root}", file=sys.stderr)
        return 1

    state = load_state(memory_root) or {}
    active_nonce = (state.get("run_nonce") or "").strip() if args.protect_active_nonce else ""

    # Hot paths
    pred_path = memory_root / "predictions.jsonl"
    obs_path = memory_root / "observations.jsonl"
    learn_path = memory_root / "learning.jsonl"

    # Load hot logs (raw lines for append; parsed for checks)
    pred_lines = load_jsonl_raw(pred_path)
    obs_lines = load_jsonl_raw(obs_path)
    learn_lines = load_jsonl_raw(learn_path)

    if not pred_lines and not obs_lines and not learn_lines:
        if not args.dry_run:
            print("No hot log content; nothing to rotate.")
        return 0

    # Protect active evidence window
    if active_nonce:
        all_text = "\n".join(pred_lines + obs_lines + learn_lines)
        if active_nonce in all_text:
            print(f"Active run_nonce {active_nonce!r} present in hot logs; skipping rotation (protected).")
            return 0

    # Retention: check oldest timestamp and size
    def oldest_ts(lines: list[str]) -> str | None:
        for line in lines:
            try:
                obj = json.loads(line)
                ts = obj.get("timestamp")
                if ts:
                    return ts
            except json.JSONDecodeError:
                continue
        return None

    def total_mb() -> float:
        total = 0
        for p in (pred_path, obs_path, learn_path):
            if p.exists():
                total += p.stat().st_size
        return total / (1024 * 1024)

    oldest = oldest_ts(pred_lines) or oldest_ts(obs_lines) or oldest_ts(learn_lines)
    now = datetime.now(timezone.utc)
    retain_cutoff = now.timestamp() - (args.retain_days * 86400)
    proceed = False
    if oldest:
        try:
            # Parse ISO-ish
            dt = datetime.fromisoformat(oldest.replace("Z", "+00:00"))
            if dt.timestamp() < retain_cutoff:
                proceed = True
        except Exception:
            pass
    if total_mb() >= args.retain_mb:
        proceed = True
    if not proceed:
        print(f"Retention not exceeded (retain_days={args.retain_days}, retain_mb={args.retain_mb}). Nothing to rotate.")
        return 0

    # Durability check
    learning_records = load_jsonl(learn_path)
    durability_warnings = durability_check(learning_records, state)
    if durability_warnings:
        for w in durability_warnings:
            print(f"WARNING: {w}", file=sys.stderr)
        print("Durability check failed; skipping rotation. Fix STATE or clear persistent_ref before archiving.", file=sys.stderr)
        return 1

    # Rotation date and archive dir
    rotate_date = now.strftime("%Y-%m-%d")
    yyyy_mm = now.strftime("%Y-%m")
    archive_dir = memory_root / "archive" / "cas" / yyyy_mm
    archive_dir.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print(f"DRY RUN: would rotate to {archive_dir}")
        print(f"  predictions.{rotate_date}.jsonl ({len(pred_lines)} lines)")
        print(f"  observations.{rotate_date}.jsonl ({len(obs_lines)} lines)")
        print(f"  learning.{rotate_date}.jsonl ({len(learn_lines)} lines)")
        return 0

    # Append hot content to archive files (same-day append)
    for name, lines in [("predictions", pred_lines), ("observations", obs_lines), ("learning", learn_lines)]:
        if not lines:
            continue
        archive_file = archive_dir / f"{name}.{rotate_date}.jsonl"
        with open(archive_file, "a", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")

    # Replace hot files with empty
    for path in (pred_path, obs_path, learn_path):
        path.write_text("", encoding="utf-8")

    # Move raw/ for session_ids that appear in rotated observations (from in-memory obs_lines)
    obs_records = [json.loads(line) for line in obs_lines if line.strip()]
    session_ids = {r.get("session_id") for r in obs_records if r.get("session_id")}
    raw_root = memory_root / "raw"
    archive_raw = archive_dir / "raw"
    raw_count = 0
    for sid in session_ids:
        src = raw_root / sid
        if not src.is_dir():
            continue
        dst = archive_raw / sid
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            for f in src.iterdir():
                if f.is_file():
                    shutil.copy2(f, dst / f.name)
                    raw_count += 1
        else:
            for f in src.rglob("*"):
                if f.is_file():
                    raw_count += 1
            shutil.copytree(src, dst)
        shutil.rmtree(src)

    # cas-index.jsonl
    run_nonces = set()
    for line in pred_lines + obs_lines + learn_lines:
        try:
            obj = json.loads(line)
            if obj.get("run_nonce"):
                run_nonces.add(obj["run_nonce"])
        except json.JSONDecodeError:
            pass
    index_entry = {
        "ts": now.isoformat(),
        "agent": args.agent,
        "archived_since": oldest or now.isoformat(),
        "archived_until": now.isoformat(),
        "run_nonces": list(run_nonces),
        "session_ids": list(session_ids),
        "counts": {
            "predictions": len(pred_lines),
            "observations": len(obs_lines),
            "learning": len(learn_lines),
            "raw_files": raw_count,
        },
        "archive_root": f"memory/archive/cas/{yyyy_mm}/",
        "rotated_files": [
            f"predictions.{rotate_date}.jsonl",
            f"observations.{rotate_date}.jsonl",
            f"learning.{rotate_date}.jsonl",
        ],
    }
    index_path = memory_root / "cas-index.jsonl"
    with open(index_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(index_entry) + "\n")

    # Consolidation note to today's daily log
    log_path = memory_root / f"{rotate_date}.md"
    note = f"\n\n## CAS consolidation {now.isoformat()}\n- Rotated to {archive_dir}\n- Lines: predictions={len(pred_lines)}, observations={len(obs_lines)}, learning={len(learn_lines)}\n- Index appended to cas-index.jsonl\n"
    if durability_warnings:
        note += "- Warnings: " + "; ".join(durability_warnings) + "\n"
    if log_path.exists():
        log_path.write_text(log_path.read_text(encoding="utf-8") + note, encoding="utf-8")
    else:
        log_path.write_text(note.lstrip(), encoding="utf-8")

    print(f"Consolidated: {len(pred_lines)} predictions, {len(obs_lines)} observations, {len(learn_lines)} learning -> {archive_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
