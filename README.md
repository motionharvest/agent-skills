# agent-skills

Reusable skills for AI agents across multiple tools: Claude Code, Cursor CLI, Python, OpenCode, Codex.

---

## Installation

```bash
npx skills@latest add motionharvest/agent-skills
```

This installs all available skills to your configured tools.

---

## UX & Design Skills

A complete end-to-end system for website research, strategy, design, and implementation. All skills coordinate through a shared `ux.md` file — one source of truth for all decisions, research, personas, architecture, and design rules.

**Start here:** Run [`/perfect-design`](./perfect-design/SKILL.md) with a screenshot or vague goal. It diagnoses what's needed and routes to the right tools.

### The Pipeline

**Entry Point**
- **[perfect-design](./perfect-design/SKILL.md)** — General entry point. Accepts messy input (screenshots, URLs, descriptions, half-formed ideas). Diagnoses gaps, maintains `ux.md`, routes to specialized skills. No UX jargon required.

**Research Phase**
- **[audience-research](./audience-research/SKILL.md)** — Find real user pain points, barriers to entry, and language. Searches Reddit, forums, reviews, industry communities (not just tech). Grounds personas in evidence, not assumptions.

**Strategy Phase**
- **[persona-archetypes](./persona-archetypes/SKILL.md)** — Build psychologically-grounded personas using 50+ frameworks (Big Five, Enneagram, Jung, VALS, DISC, etc.). Map how they think, decide, and what messaging resonates.
- **[reference-site-analysis](./reference-site-analysis/SKILL.md)** — Analyze 3–5 high-signal sites (validated by user reviews, market data, engagement). Extract UX patterns that actually work with this audience.

**Architecture Phase**
- **[ux-methodology-process](./ux-methodology-process/SKILL.md)** — Determine page structure and flow using psychology-based laws (Peak-End Rule, Mental Model, Miller's Law, Hick's Law, etc.). Answers: *What sections exist and in what order?*

**Design Phase**
- **[ux-methodology-design](./ux-methodology-design/SKILL.md)** — Optimize visual hierarchy, interactions, and presentation using design laws (Fitts's Law, Von Restorff, Doherty Threshold, etc.). Answers: *How should information be presented?*

**Identity Phase**
- **[visual-identity](./visual-identity/SKILL.md)** — Lock the brand language before writing code. Defines personality keywords, explores typography pairings, expands the color system to a full token set, and names 4 signature motion vocabulary moves. Outputs `design-system.md` ready for the build phase. Award-winning studios run this before implementation.

**Build Phase**
- **[motion-web-design](./motion-web-design/SKILL.md)** — Build the site. Takes a build prompt (from audience-site-brief) and `design-system.md` (from visual-identity) and produces a coded, running landing page using Vite + GSAP + Lenis. Implements choreographed scroll animations, micro-interactions, and polished visual design. Sources imagery from Unsplash and documents video slots for Replicate. Targets Awwwards-quality execution.

**Optimization Phase**
- **[ab-testing](./ab-testing/SKILL.md)** — Plan conversion experiments before and after launch. Produces a prioritized test backlog using the PIE framework (Potential, Importance, Ease), hypothesis templates, and persona-calibrated CTA variants. Enforces the right testing order: headlines first, button color last.

**Full Orchestration**
- **[audience-site-brief](./audience-site-brief/SKILL.md)** — Complete pipeline for users who want guided end-to-end flow. Coordinates all phases and outputs a build prompt for the identity and build phases.

### How It Works

1. **Start:** Run `/perfect-design` with a goal or screenshot
2. **Diagnose:** Skill asks 2–3 clarifying questions, checks `ux.md` for prior work
3. **Route:** Hands off to the appropriate skill in the pipeline
4. **Coordinate:** Each skill reads and updates `ux.md`
5. **Continue:** Come back anytime to check progress or move to the next phase

### Example Workflows

**Quick Improvement**
```
→ Run /perfect-design with screenshot
→ It diagnoses the problem
→ Routes to /ux-methodology-design (if visual) or /audience-research (if strategy)
→ Updates ux.md with findings
```

**New Site From Scratch**
```
→ Run /audience-site-brief with project goal
→ Orchestrates: /audience-research → /persona-archetypes → /reference-site-analysis
→ Then: /ux-methodology-process → /ux-methodology-design
→ Then: /visual-identity → design-system.md
→ Then: /motion-web-design → coded, running site
→ Then: /ab-testing → prioritized test backlog for launch
```

**Copy & Messaging Only**
```
→ Run /audience-research to find pain points
→ Then /persona-archetypes to build personas
→ Use findings to write better copy in /ux-methodology-design
```

See [SKILLS.md](./SKILLS.md) for detailed skill descriptions, dependencies, and tool support.

### The `ux.md` File

All UX skills coordinate through a shared `ux.md` file in your project. This file:
- **Tracks all research** — pain points, language, objections from real users
- **Documents personas** — psychology, decision style, trust signals
- **Records decisions** — what sections exist, why, in what order
- **Captures design rules** — visual hierarchy, emphasis, interaction principles
- **Provides visibility** — one source of truth for the entire design process

Each skill reads `ux.md` first to avoid duplicate work and understand context. Each skill updates it with new findings.

---

## Dev Tools

### [inspector-overlay](./inspector-overlay/SKILL.md)

**Add a DOM inspector overlay to React or Next.js apps.** Installs a development-only component that lets you hold `Alt` to inspect elements, `Alt+click` to copy single-element payloads for coding agents, and `Alt+Shift+click` to build multi-element selections. Payloads include semantic hooks (`data-testid`, `data-file`, `data-component`) that make AI-assisted edits dramatically more precise.

Use when you want to point a coding agent at a specific element without describing it in words.

---

## CAS Skills

Conscious Agentic System infrastructure for reliable, auditable agent behavior. These skills enforce a structured approach to agent reasoning and learning.

### [cas-agent-setup](./cas-agent-setup/SKILL.md)

**Set up CAS persistence for a new or existing agent.** Creates the required files and directories (STATE.json, append-only telemetry, raw output store, optional archive layout) and wires schemas and specs. Ships bundled helpers: STATE template, all JSON schemas, consolidation spec, and acceptance test definitions.

Use when bootstrapping an agent or aligning an existing agent with the CAS file contract.

### [cas-operational-loop](./cas-operational-loop/SKILL.md)

**Run the 8-phase CAS loop for every consequential action.** Phases: State Ingestion → World-Model Update → Prediction → Action → Evaluation → Learning → Commit. Covers prediction/observation/learning record formats, raw output capture, pending citations, run_nonce scoping, and error classification.

Use when operating as a CAS agent — this skill defines the *how*, while `cas-agent-setup` defines the *what files*.

#### Why CAS?

Most agents fail because they:
- Act without grounding in current context
- Forget why they made a decision
- Don't learn from mistakes, so failures repeat

CAS solves this by making reasoning and learning operational. It enforces:
- **Traceability** — every action has a prediction + evaluation
- **Continuity** — session-to-session improvement without re-explaining context
- **Error learning** — failures are classified and followed by explicit learning
- **Grounded execution** — actions tied to observed state, not vague intent
