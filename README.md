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

---

## Other Skills

See individual skill directories for additional capabilities.
