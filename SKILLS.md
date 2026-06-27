# Skills Manifest

Available skills organized by category and tool support.

## UX & Design Skills

These skills coordinate website design and improvement work through a shared `ux.md` file.

### [perfect-design](./perfect-design/SKILL.md)
**General entry point for site improvement.** Accepts messy input (screenshots, descriptions, URLs, vague goals). Diagnoses what's needed, maintains `ux.md`, routes to specialized skills. No UX jargon required.

**Tools:** Claude Code, Cursor CLI  
**Dependencies:** None (coordinates other skills)  
**When to use:** You have a website goal and don't know where to start.

### [audience-research](./audience-research/SKILL.md)
**Find real user pain points and language.** Searches Reddit, forums, reviews, industry communities (not just tech) for what your audience actually struggles with. Grounds personas in evidence.

**Tools:** Claude Code, Cursor CLI  
**Dependencies:** None  
**When to use:** Before building personas; when you need to understand audience barriers and objections.

### [reference-site-analysis](./reference-site-analysis/SKILL.md)
**Analyze successful sites for your audience.** Finds 3–5 high-signal sites (validated by user reviews, market data, engagement). Extracts UX patterns that actually work.

**Tools:** Claude Code, Cursor CLI  
**Dependencies:** Requires audience research or persona (recommended)  
**When to use:** After understanding your audience; before designing architecture.

### [ux-methodology-process](./ux-methodology-process/SKILL.md)
**Determine page architecture and flow.** Uses psychology-based laws (Peak-End Rule, Mental Model, Miller's Law, etc.) to decide what sections exist, why, and in what order. Informs **structure**, not visual design.

**Tools:** Claude Code, Cursor CLI  
**Dependencies:** Recommended: audience research + personas  
**When to use:** You have content but need to figure out the right page flow.

### [ux-methodology-design](./ux-methodology-design/SKILL.md)
**Optimize visual hierarchy and interactions.** Uses design-focused laws (Fitts's Law, Von Restorff, Doherty Threshold, etc.) to improve how existing content is presented. Informs **presentation**, not structure.

**Tools:** Claude Code, Cursor CLI  
**Dependencies:** Requires page architecture (from ux-methodology-process)  
**When to use:** After page structure is set; when optimizing for clarity, usability, polish.

### [persona-archetypes](./persona-archetypes/SKILL.md)
**Build psychologically-grounded personas.** Applies 50+ frameworks (Big Five, Enneagram, Jung archetypes, VALS, DISC, etc.) to understand audience psychology, decision style, messaging resonance, and UX preferences.

**Tools:** Claude Code, Cursor CLI  
**Dependencies:** Recommended: audience research  
**When to use:** After understanding audience pain points; to inform messaging and design choices.

### [audience-site-brief](./audience-site-brief/SKILL.md)
**Full orchestration: research → personas → architecture → design → build.** Coordinates the entire UX pipeline for users who want end-to-end guidance. Produces a build prompt for `motion-web-design`.

**Tools:** Claude Code, Cursor CLI  
**Dependencies:** All other UX skills (called by this orchestrator)  
**When to use:** When starting a new site from scratch and want guided flow.

---

## CAS Skills

Conscious Agentic System infrastructure for reliable, auditable agent behavior.

### [cas-agent-setup](./cas-agent-setup/SKILL.md)
**Set up CAS persistence.** Creates required file structure (STATE.json, telemetry, schemas) for a new or existing agent. Includes templates and acceptance tests.

**Tools:** All  
**When to use:** Bootstrapping an agent with CAS.

### [cas-operational-loop](./cas-operational-loop/SKILL.md)
**Run the 8-phase CAS loop.** Defines the operational rhythm: State Ingestion → World-Model Update → Prediction → Action → Evaluation → Learning → Commit.

**Tools:** All  
**When to use:** Operating as a CAS agent for consequential work.

---

## Other Skills

### [inspector-overlay](./inspector-overlay/SKILL.md)
[Add description from skill]

**Tools:** [Add]  
**When to use:** [Add]

---

## Installation

See `install.sh` for setup instructions and tool-specific symlink configuration.

## Skills by Tool

### Claude Code
All skills available. Configure in `.cursor/settings.json` or use symlinks to `~/.claude/skills/`.

### Cursor CLI
All skills available. Use symlinks to `~/.cursor/skills/` or reference directly.

### Python
Supported via file-based interface. Use symlinks to project-local `.skills/` or `~/.skills/`.

### OpenCode
[Add tool-specific instructions]

### Codex
[Add tool-specific instructions]

---

## Workflow Examples

### Quick Site Improvement
```
1. Run /perfect-design with screenshot/goal
2. It diagnoses and routes to needed skills
3. Each skill reads/updates ux.md
4. Return to /perfect-design when next phase is ready
```

### Comprehensive New Site
```
1. Run /audience-site-brief with project goal
2. Orchestrates: /audience-research → /persona-archetypes → /reference-site-analysis
3. Then: /ux-methodology-process → /ux-methodology-design
4. Outputs build prompt for /motion-web-design
```

### Just Fix The Copy
```
1. Run /ux-methodology-design with screenshot
2. Skips architecture; focuses on visual hierarchy, emphasis, CTA placement
3. Outputs design improvements only
```

---

## Adding New Skills

1. Create directory: `skills/[skill-name]/`
2. Add `SKILL.md` with frontmatter + detailed guidance
3. Update this SKILLS.md with entry
4. Run `./install.sh` to symlink to your tools
