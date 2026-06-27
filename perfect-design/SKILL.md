---
name: perfect-design
description: >-
  Use when you have a website goal and want to improve, build, or fix it. Accepts
  screenshots, descriptions, URLs, or vague ideas. Diagnoses what's needed,
  coordinates specialized skills, and maintains a shared ux.md file for
  visibility. The friendly entry point — no UX jargon required.
---

# Perfect Design

Your collaborative partner for building or improving a website. You describe what you want, share a screenshot or URL, and this skill figures out what needs to happen next.

**Not a replacement for specialized skills** — this coordinates them. It's the friendly front door that understands messy, real-world requests.

## When to Use

- You have a website (or want to build one) and it needs work
- You have a screenshot, URL, or description but don't know where to start
- You want visibility into the whole process without learning UX terminology
- You want to improve something but aren't sure what the problem actually is
- You're coming back to a project and need to remember what's been done

## Workflow

```
Perfect Design:
- [ ] 1. Listen — what's your goal?
- [ ] 2. Diagnose — what's actually needed?
- [ ] 3. Coordinate — route to the right tools
- [ ] 4. Maintain ux.md — shared reference for all work
- [ ] 5. Explain next steps — what comes next?
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
- See what research/personas/architecture is already done
- Avoid duplicating work
- Continue from where the last phase left off

**If it doesn't exist:**
- Create `ux.md` with section headers for each phase
- This becomes the shared reference for all future work

### Step 3: Diagnose What's Needed

Ask clarifying questions in plain language to identify gaps:

| If they say… | Diagnose | Next question |
|---|---|---|
| "Make it look better" | Could be visual, could be structure | "What specifically bothers you? The way it looks, how it feels to use, what it communicates?" |
| "I want more signups" | Could be messaging, trust, friction | "Who should be signing up? What's stopping them?" |
| "Here's my competitor" | Could need reference analysis | "What do you like about theirs that yours doesn't have?" |
| "Site feels slow" | Could be performance or perceived performance | "Is it actually slow, or does it *feel* like it's taking forever?" |
| "Doesn't feel professional" | Could be visual polish, copy tone, hierarchy | "What would make it feel more professional to you?" |

**Rule: Ask max 3 clarifying questions, then infer the rest.**

### Step 4: Route to Specialized Skills

Based on diagnosis, hand off to the right tool:

| Problem | Next skill | What it does |
|---|---|---|
| "I don't know who my audience is" OR "People aren't converting" | `/audience-research` | Finds real pain points, barriers, language from actual users |
| "I have audience research but need psychology" | `/persona-archetypes` | Builds personas grounded in research |
| "I want to see what's working" | `/reference-site-analysis` | Analyzes successful sites, extracts patterns |
| "I have a site but sections are wrong" OR "What should the page flow be?" | `/ux-methodology-process` | Determines architecture, section order, journey |
| "I have structure but it looks bad" OR "UX feels clunky" | `/ux-methodology-design` | Optimizes visual hierarchy, interactions, feedback |
| "I want to build from scratch" | `/audience-site-brief` | Full orchestration: research → personas → reference → architecture → design → build |
| "Nothing's working, need a complete audit" | yourself (or `/perfect-design` again) | Run a diagnostic: read existing ux.md, identify biggest gaps |

**How to hand off:**
- Summarize what you've learned in ux.md
- List what the next skill should focus on
- Link to the skill with a clear, specific prompt
- Example: "Run `/audience-research` to identify pain points for [audience segment]. Focus on [specific pain point they mentioned]."

### Step 5: Update ux.md

After each step (yours or a specialized skill's):
- Update the relevant section in ux.md
- Add findings, decisions, quotes, screenshots
- Note what's done and what's next
- Keep it readable (markdown, short summaries)

### Step 6: Explain Next Steps

Tell the user:
- What you found / what happened
- What's in ux.md (they can reference it)
- What skill runs next and why
- What they should expect
- When to come back to you (or when to run the next skill themselves)

**Example:**
> I've created ux.md and identified that you need audience research first. Your biggest unknown is *why* people aren't converting. I'm routing to `/audience-research` to find real pain points and objections. That will take 2–3 hours. After that, we'll know who we're designing for and can build personas. Come back to me (or run `/audience-site-brief`) when research is done.

---

## Diagnosis Playbook

### Scenario: "My site doesn't convert"

**Diagnose:**
1. Is the audience clear? (Check ux.md for personas)
   - If no → `/audience-research` → `/persona-archetypes`
   - If yes → continue
2. Do we know what objections exist? (Check ux.md for research)
   - If no → `/audience-research` to find objections
   - If yes → continue
3. Is the structure right? (Check ux.md for architecture)
   - If maybe → `/reference-site-analysis` to see what works
   - Then → `/ux-methodology-process` to fix structure
   - If yes → continue
4. Is the design optimized? (Check ux.md for design rules)
   - If no → `/ux-methodology-design` to improve clarity/CTA/hierarchy
   - If yes → A/B test (see ab-testing skill)

### Scenario: "I want to rebuild my site"

1. Check ux.md — anything salvageable?
2. Ask: Who's coming to this site? (Audience hypothesis)
3. Ask: What do you want them to do? (Goal)
4. Route to `/audience-site-brief` with those two pieces
   - It handles the full pipeline: research → personas → reference → architecture → design → build

### Scenario: "Here's a screenshot, make it better"

1. Look at the screenshot
2. Ask: What's not working about it? (Their pain point)
3. Check ux.md — what's already been researched?
4. If ux.md is empty → diagnose: is it research? Architecture? Visual?
5. If ux.md exists → skip duplicate work, route to next phase

---

## ux.md Template

If you need to create ux.md from scratch:

```markdown
# UX Strategy: [Project Name]

## Project Goal
[One sentence: what are we building and why?]

## Audience & Research
[Who are we designing for? What are their pain points?]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /audience-research

## Personas
[Psychology, decision style, trust signals]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /persona-archetypes

## Reference Sites
[What's working for similar audiences?]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /reference-site-analysis

## Page Architecture
[Sections, order, flow]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /ux-methodology-process

## Design Optimization
[Visual hierarchy, interactions, feedback]
- Status: ❌ Not started | 🔄 In progress | ✅ Done
- Next: Run /ux-methodology-design

## Copy & Messaging
[Headlines, tone, objection handling]
- Status: ❌ Not started | 🔄 In progress | ✅ Done

## Visual Direction
[Preset, colors, typography]
- Status: ❌ Not started | 🔄 In progress | ✅ Done

## A/B Testing Backlog
[What to validate after launch]
- Status: ❌ Not started

## Last Updated
[Date]
```

---

## Anti-Patterns

- **Pretending to know more than you do** — "I see the problem" when you don't. Ask clarifying questions instead.
- **Running the wrong skill first** — If they have no idea who their audience is, research comes before personas.
- **Skipping ux.md** — The file is the coordination layer. Maintain it religiously.
- **Overloading with all problems at once** — Focus on one gap at a time. Let specialized skills do their work.
- **Using UX jargon** — These users don't know what "progressive disclosure" means. Say "show the essential stuff, hide details behind 'See more'" instead.
- **Assuming prior phases are done** — Always check ux.md first. Previous work might be incomplete or missing.

---

## When to Hand Back to the User

After each handoff to a specialized skill:
- Wait for them to run the skill
- Come back when they ask
- OR automatically check in when they return to perfect-design

If they say "what do I do next?":
1. Read ux.md
2. See what's done vs. what's not
3. Route to the next logical step
4. Explain why and what to expect

---

## Quick Reference

| User says | You do |
|---|---|
| "Make my site better" | Check ux.md, diagnose, route |
| "I don't know where to start" | Ask goal + current state, route to /audience-site-brief |
| "I have a screenshot" | Look at it, ask what's wrong, diagnose, route |
| "I'm coming back to this project" | Read ux.md, see what's done, continue from there |
| "Should I do X or Y?" | Check ux.md; if it tells you, say so; if not, diagnose what's actually needed |

---

## Quality Gate

You've done your job if:
- [ ] User feels heard (you understood their goal)
- [ ] ux.md exists and is readable
- [ ] Next step is clear (which skill runs next, why)
- [ ] User knows where their work lives (ux.md)
- [ ] No UX jargon was used
- [ ] You diagnosed accurately (routed to right skill)
