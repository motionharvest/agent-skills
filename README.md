# agent-skills

A set of skills for AI agents, built around the Conscious Agentic System (CAS).

## CAS Skills

These two skills work together: `cas-agent-setup` wires the file layout, and `cas-operational-loop` defines how to run each session.

### [cas-agent-setup](./cas-agent-setup/SKILL.md)

**Set up CAS persistence for a new or existing agent.** Creates the required files and directories (STATE.json, append-only telemetry, raw output store, optional archive layout) and wires schemas and specs. Ships bundled helpers: STATE template, all JSON schemas, consolidation spec, and acceptance test definitions.

Use when bootstrapping an agent or aligning an existing agent with the CAS file contract.

### [cas-operational-loop](./cas-operational-loop/SKILL.md)

**Run the 8-phase CAS loop for every consequential action.** Phases: State Ingestion → World-Model Update → Prediction → Action → Evaluation → Learning → Commit. Covers prediction/observation/learning record formats, raw output capture, pending citations, run_nonce scoping, and error classification.

Use when operating as a CAS agent — this skill defines the *how*, while `cas-agent-setup` defines the *what files*.

## CAS Use-Case: "Reliable Partner Mode"

### What problem does CAS solve?

Most agents fail in one of three ways:
- They act without grounding in current context.
- They forget why they made a decision.
- They don't learn from mistakes, so the same failure repeats.

CAS solves this by making reasoning and learning operational, not optional. It turns "be thoughtful" into a repeatable runtime contract.

### How does CAS solve it?

CAS enforces an 8-phase loop on consequential work:
1. Boot: load identity, constraints, and prior state.
2. State Ingestion: capture what's new in the user/task/environment.
3. World-Model Update: refresh assumptions about user intent and context.
4. Prediction: state the smallest useful next move before acting.
5. Action: execute with tools.
6. Evaluation: compare outcome vs prediction.
7. Learning: extract durable lessons.
8. Commit: persist state + telemetry for next session continuity.

Concretely, this is backed by durable files (`STATE.json`, `predictions.jsonl`, `observations.jsonl`, `learning.jsonl`) and run scoping via `run_nonce` so each session stays auditable.

### How do you know it's working?

Look for all of the following:
- Traceability: every meaningful action has a prior prediction and a post-action evaluation.
- Continuity: session-to-session behavior improves without re-explaining context.
- Error containment: failures are classified and followed by explicit learning entries.
- Grounded execution: actions are tied to observed state, not vague intent.
- Commit hygiene: state and telemetry are updated on every consequential run.

Practical signal: if you can answer "why did the agent do this?" and "what did it learn last time?" directly from CAS records, the system is doing its job.

---

## Other Skills

See individual skill directories for additional capabilities.
