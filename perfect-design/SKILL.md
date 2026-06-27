---
name: perfect-design
description: >-
  Use when you have a website goal and want to improve, build, or fix it. Accepts
  screenshots, descriptions, URLs, or vague ideas. Diagnoses what's needed,
  coordinates the full design pipeline (research → personas → references →
  architecture → design → visual identity → build → testing), and maintains a
  shared ux.md file for visibility. The friendly entry point — no UX jargon required.
---

# Perfect Design

Your collaborative partner for building or improving a website. You describe what you want, share a screenshot or URL, and this skill figures out what needs to happen next — then drives the work all the way through to a built, tested site.

**Not a replacement for specialized skills** — this coordinates them. It's the friendly front door that understands messy, real-world requests and knows the complete path from "I have an idea" to "the site is live and being optimized."

## When to Use

- You have a website (or want to build one) and it needs work
- You have a screenshot, URL, or description but don't know where to start
- You want visibility into the whole process without learning UX terminology
- You want to improve something but aren't sure what the problem actually is
- You're coming back to a project and need to remember what's been done

## The Full Pipeline

Perfect design is not one step — it's a sequence. Every phase feeds the next, and all of them coordinate through `ux.md`. This skill's job is to know where the user is in this pipeline and move them forward (or jump straight to the gap that matters).

| # | Phase | Skill | Produces |
|---|-------|-------|----------|
| 1 | **Research** | [`/audience-research`](../audience-research/SKILL.md) | Real pain points, barriers, language, objections |
| 2 | **Personas** | [`/persona-archetypes`](../persona-archetypes/SKILL.md) | Who they are, how they decide, what resonates |
| 3 | **References** | [`/reference-site-analysis`](../reference-site-analysis/SKILL.md) | Validated patterns from sites that work |
| 4 | **Architecture** | [`/ux-methodology-process`](../ux-methodology-process/SKILL.md) | What sections exist and in what order |
| 5 | **Design** | [`/ux-methodology-design`](../ux-methodology-design/SKILL.md) | Visual hierarchy, interactions, feedback |
| 6 | **Visual Identity** | [`/visual-identity`](../visual-identity/SKILL.md) | `design-system.md` — keywords, type, color, motion |
| 7 | **Build** | [`/motion-web-design`](../motion-web-design/SKILL.md) | Coded, running Vite + GSAP + Lenis site |
| 8 | **Testing** | [`/ab-testing`](../ab-testing/SKILL.md) | Prioritized experiment backlog for launch |

**Two ways to run the pipeline:**
- **Guided end-to-end** — for "build me a site from scratch," hand the whole sequence to [`/audience-site-brief`](../audience-site-brief/SKILL.md), which orchestrates phases 1–8 and outputs the build prompt. Use this when the user wants one continuous flow.
- **Targeted** — for "fix this one thing," diagnose the gap and jump straight to the relevant phase. Don't make someone redo research when they only need a design pass.

Either way, **don't stop at phase 5.** A design that never gets a visual identity, never gets built, and never gets tested isn't a perfect design — it's a spec. Carry the user through to a running, optimized site.

## Workflow

```
Perfect Design:
- [ ] 1. Listen — what's your goal?
- [ ] 2. Check ux.md — what's already done?
- [ ] 3. Diagnose — which pipeline phase is the gap?
- [ ] 4. Coordinate — route to the right skill (or run the full pipeline)
- [ ] 5. Maintain ux.md — shared reference for all work
- [ ] 6. Advance — move to the next phase, don't stop early
- [ ] 7. Explain next steps — what comes next and why?
```

---

## How It Works

### Step 1: Listen

Start with one open question in plain language:

> What are you trying to accomplish with this site? You can describe it, show me a screenshot, give me a URL — whatever helps me understand.

**Accept any input:**
- Screenshots (visual feedback on design)
- URLs (live sites to analyze)
- Descriptions ("I want more signups", "Site feels slow", "Doesn't look professional")
- Comparisons ("I want it to feel like [reference site]")
- Half-formed ideas ("I'm not sure what's wrong")

**Don't ask for:**
- Perfect articulation (they don't need UX vocabulary)
- All the information upfront (gather as you go)
- Technical details yet (focus on goals first)

### Step 2: Check ux.md

Before proceeding, check if `ux.md` exists in the project:

**If it exists:**
- Read it to understand prior work
- See which pipeline phases are done (each has a status line)
- Avoid duplicating work
- Continue from the first incomplete phase

**If it doesn't exist:**
- Create `ux.md` with a section for every pipeline phase (template below)
- This becomes the shared reference for all future work

### Step 3: Diagnose the Gap

Ask clarifying questions in plain language to identify which phase the user actually needs:

| If they say… | Diagnose | Next question |
|---|---|---|
| "Make it look better" | Could be design (5) or visual identity (6) | "What specifically bothers you? The way it looks, how it feels to use, what it communicates?" |
| "I want more signups" | Could be research (1), messaging, or testing (8) | "Who should be signing up? What's stopping them?" |
| "Here's my competitor" | Reference analysis (3) | "What do you like about theirs that yours doesn't have?" |
| "Site feels slow" | Build/performance (7) or perceived performance (5) | "Is it actually slow, or does it *feel* like it's taking forever?" |
| "Doesn't feel professional" | Visual identity (6) — usually a missing brand language | "What would make it feel more professional to you?" |
| "It looks generic" | Visual identity (6) | "Does it feel like *your* brand, or could it be anyone's?" |
| "Build me a site" | Full pipeline (1→8) | "Who's coming to this site, and what's the one thing you want them to do?" |

**Rule: Ask max 3 clarifying questions, then infer the rest.**

### Step 4: Route to the Right Phase

Based on diagnosis, hand off to the right skill. This table is the full pipeline — route to the **earliest incomplete phase that blocks the user's goal**, not always phase 1.

| Problem / situation | Skill | What it does |
|---|---|---|
| "I don't know who my audience is" OR "People aren't converting" | `/audience-research` | Finds real pain points, barriers, language from actual users |
| "I have research but need to know how they think/decide" | `/persona-archetypes` | Builds psychology-grounded personas from research |
| "I want to see what's working for sites like mine" | `/reference-site-analysis` | Analyzes successful sites, extracts validated patterns |
| "Sections are wrong" OR "What should the page flow be?" | `/ux-methodology-process` | Determines architecture, section order, journey |
| "It looks bad" OR "UX feels clunky" | `/ux-methodology-design` | Optimizes visual hierarchy, interactions, feedback |
| "It looks professional but generic — no personality" | `/visual-identity` | Locks brand keywords, typography, color tokens, motion vocabulary → `design-system.md` |
| "Build / rebuild the site with great animations" | `/motion-web-design` | Builds a Vite + GSAP + Lenis site from `design-system.md` + build prompt |
| "It's live — what should I test to improve it?" | `/ab-testing` | Prioritized experiment backlog (headlines first, color last) |
| "Build me a site from scratch" (wants one continuous flow) | `/audience-site-brief` | Orchestrates phases 1–8, outputs the build prompt |
| "Nothing's working, need a complete audit" | yourself | Read ux.md, find the earliest gap, route there |

**How to hand off:**
- Summarize what you've learned in ux.md
- List what the next skill should focus on
- Link to the skill with a clear, specific prompt
- Example: "Run `/audience-research` to identify pain points for [audience segment]. Focus on [specific pain point they mentioned]."

### Step 5: Update ux.md

After each step (yours or a specialized skill's):
- Update the relevant phase section in ux.md and flip its status
- Add findings, decisions, quotes, screenshots
- Note what's done and what's next
- Keep it readable (markdown, short summaries)

### Step 6: Advance — Don't Stop Early

After a phase completes, **proactively move to the next one.** The most common failure is stopping at "the design looks good" without ever locking a visual identity, building the site, or planning what to test.

- Research done → personas
- Personas done → references
- References done → architecture
- Architecture done → design
- Design done → **visual identity** (don't skip — this is what makes it not generic)
- Visual identity done → **build** (a `design-system.md` that never ships isn't finished)
- Build done → **testing backlog** (a perfect design proves itself with data)

If the user only wanted a targeted fix, confirm they're satisfied and note the remaining phases in ux.md so they (or the next session) can pick up where it stopped. But always *offer* the next phase — don't leave the pipeline half-run silently.

### Step 7: Explain Next Steps

Tell the user:
- What you found / what happened
- What's in ux.md (they can reference it)
- What phase runs next and why
- What they should expect
- When to come back to you (or when to run the next skill themselves)

**Example:**
> I've created ux.md and identified that you need audience research first. Your biggest unknown is *why* people aren't converting. I'm routing to `/audience-research` to find real pain points and objections. After that we'll build personas, check reference sites, set the architecture and design, lock a visual identity, build the site, and finish with a test backlog. We're at step 1 of 8 — I'll walk you through each one.

---

## Diagnosis Playbook

### Scenario: "My site doesn't convert"

Walk the pipeline backward from the goal until you hit the gap:
1. Is the audience clear? (Check ux.md for research + personas)
   - If no → `/audience-research` → `/persona-archetypes`
2. Do we know what objections exist? (research)
   - If no → `/audience-research` to find objections
3. Is the structure right? (architecture)
   - If maybe → `/reference-site-analysis`, then `/ux-methodology-process`
4. Is the design optimized? (design)
   - If no → `/ux-methodology-design`
5. Does it have a distinct brand, or is it generic? (visual identity)
   - If generic → `/visual-identity`
6. Is the built experience polished? (build)
   - If no → `/motion-web-design`
7. Everything's in place but conversion is flat?
   - → `/ab-testing` to validate headlines, CTAs, proof placement

### Scenario: "I want to build my site from scratch"

1. Check ux.md — anything salvageable?
2. Ask: Who's coming to this site? (audience hypothesis)
3. Ask: What do you want them to do? (goal)
4. Route to `/audience-site-brief` with those two pieces
   - It runs the full pipeline (1–8) and outputs a build prompt for `/motion-web-design`
5. After the build, run `/ab-testing` to set up the launch experiment backlog

### Scenario: "Here's a screenshot, make it better"

1. Look at the screenshot
2. Ask: What's not working about it? (their pain point)
3. Check ux.md — what's already been done?
4. If ux.md is empty → diagnose the gap: research? architecture? design? identity?
5. Route to that phase, then carry forward through the remaining phases

### Scenario: "I built it — now what?"

Don't treat the build as the finish line.
1. Confirm visual identity was actually locked (not improvised during build)
2. Run `/ab-testing` to produce a prioritized experiment backlog
3. Note in ux.md which hypotheses to validate first (headlines and CTAs before cosmetics)

---

## ux.md Template

If you need to create ux.md from scratch:

```markdown
# UX Strategy: [Project Name]

## Project Goal
[One sentence: what are we building and why?]

## 1. Audience & Research
[Who are we designing for? What are their pain points?]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /audience-research

## 2. Personas
[Psychology, decision style, trust signals]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /persona-archetypes

## 3. Reference Sites
[What's working for similar audiences?]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /reference-site-analysis

## 4. Page Architecture
[Sections, order, flow]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /ux-methodology-process

## 5. Design Optimization
[Visual hierarchy, interactions, feedback]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /ux-methodology-design

## 6. Visual Identity
[Brand keywords, typography, color tokens, motion vocabulary → design-system.md]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /visual-identity

## 7. Build
[Coded site — Vite + GSAP + Lenis, choreographed motion]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /motion-web-design

## 8. A/B Testing Backlog
[What to validate after launch — headlines and CTAs first]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /ab-testing

## Copy & Messaging
[Headlines, tone, objection handling — synthesized across phases]
- Status: ❌ Not started | 🔄 In progress | ✅ Done

## Last Updated
[Date]
```

---

## Anti-Patterns

- **Stopping at the design phase** — a "perfect design" that never gets a visual identity, never ships, and never gets tested is just a mockup. Carry the pipeline through to build and testing.
- **Pretending to know more than you do** — "I see the problem" when you don't. Ask clarifying questions instead.
- **Running the wrong skill first** — If they have no idea who their audience is, research comes before personas.
- **Skipping ux.md** — The file is the coordination layer. Maintain it religiously, with a status for every phase.
- **Skipping visual identity** — going straight from design rules to build is exactly what produces "correct but generic" sites.
- **Overloading with all problems at once** — Focus on one gap at a time. Let specialized skills do their work.
- **Using UX jargon** — These users don't know what "progressive disclosure" means. Say "show the essential stuff, hide details behind 'See more'" instead.
- **Assuming prior phases are done** — Always check ux.md first. Previous work might be incomplete or missing.

---

## When to Hand Back to the User

After each handoff to a specialized skill:
- Wait for them to run the skill
- Come back when they ask
- OR automatically check in when they return to perfect-design, and advance to the next phase

If they say "what do I do next?":
1. Read ux.md
2. Find the first incomplete phase
3. Route to it
4. Explain why and what to expect — and name the phases still ahead

---

## Quick Reference

| User says | You do |
|---|---|
| "Make my site better" | Check ux.md, diagnose the gap phase, route |
| "I don't know where to start" | Ask goal + current state, route to /audience-site-brief for the full pipeline |
| "I have a screenshot" | Look at it, ask what's wrong, diagnose, route, then carry forward |
| "I'm coming back to this project" | Read ux.md, find first incomplete phase, continue |
| "Should I do X or Y?" | Check ux.md; if it tells you, say so; if not, diagnose what's actually needed |
| "It's built — are we done?" | No — route to /ab-testing for the launch experiment backlog |

---

## Quality Gate

You've done your job if:
- [ ] User feels heard (you understood their goal)
- [ ] ux.md exists, is readable, and has a status for all 8 phases
- [ ] You diagnosed accurately (routed to the right phase, not always phase 1)
- [ ] The next step is clear (which skill runs next, why) — and the remaining phases are named
- [ ] You didn't stop at design — visual identity, build, and testing were offered or scheduled
- [ ] User knows where their work lives (ux.md)
- [ ] No UX jargon was used
