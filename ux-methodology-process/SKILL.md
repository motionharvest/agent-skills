---
name: ux-methodology-process
description: >-
  Use after audience research and reference site analysis. Applies laws of UX
  that determine page structure, section order, and user flow. Informs WHAT
  sections exist and HOW they're sequenced — not visual design. Output is
  refined page architecture ready for design optimization.
---

# UX Methodology: Process

Use evidence-based psychology to determine the *structure* of your page — what sections matter, why, and what order works best.

**Distinction:** This skill determines *what the page contains and how it flows*. [ux-methodology-design](../ux-methodology-design/SKILL.md) then optimizes *how to present* that structure. Together they shape both substance and style.

## When to Apply

- After audience research + reference sites — ready to design page architecture
- Your rough sections exist but you're not sure of the order
- Deciding which sections to include or cut
- Determining how to sequence information for this specific audience
- Balancing competing demands (e.g., educate vs. convert)

## Workflow

Copy this checklist:

```
UX Process Design:
- [ ] 1. Map user mental model (Jakob's, Mental Model)
- [ ] 2. Define journey peaks and endings (Peak-End, Goal-Gradient)
- [ ] 3. Chunk information (Miller's, Chunking)
- [ ] 4. Determine section sequence (Serial Position, Zeigarnik)
- [ ] 5. Reduce choices per section (Hick's, Choice Overload)
- [ ] 6. Plan disclosure/progression (Paradox of Active User, Flow)
- [ ] 7. Match task pacing (Parkinson's, Flow)
- [ ] 8. Simplify ruthlessly (Occam's)
- [ ] 9. Document final architecture
```

---

## Process Laws Reference

### Mental Model & Expectations

**Jakob's Law** — Users expect your site to work like others they know.
- **Use for:** Section ordering, familiar patterns (Hero → CTA → Proof is expected)
- **Application:** "Our audience expects [reference site patterns]. Follow that pattern unless you have a reason to break it."
- **In this phase:** Determines what sections should exist and their default order

**Mental Model** — Users carry compressed beliefs about how systems work.
- **Use for:** Flow that matches how they think the process works
- **Application:** "In [audience]'s mind, the process is: problem → solution → proof → action. Structure sections in that order."
- **In this phase:** Shapes the logical progression of content

### Journey Structure

**Peak-End Rule** — People remember emotional peaks and how it ends, not the average.
- **Use for:** Deciding where to place the most compelling content
- **Application:** "Place the emotional high-point (customer success story / breakthrough moment) here. End on a clear action or win."
- **In this phase:** Determines section placement, not just existence

**Goal-Gradient Effect** — Effort and motivation accelerate as users approach the goal.
- **Use for:** Section ordering — momentum builds toward conversion
- **Application:** "Put friction-light sections early, proof mid-page, the ask (CTA) near the end. Each section should feel closer to the goal."
- **In this phase:** Shapes the progression from awareness → consideration → commitment

**Zeigarnik Effect** — Unfinished tasks stay top-of-mind; completion feels satisfying.
- **Use for:** Deciding if you need a progress section or multi-step flow
- **Application:** "Show progress toward a goal: 'Step 1 of 3,' progress bars, or 'You're X% closer.' This keeps users engaged."
- **In this phase:** May create a new section type (progress tracker, milestones) or shape existing ones

### Information Architecture

**Miller's Law** — Working memory holds ~7±2 items (about 5–9 chunks).
- **Use for:** How many sections total? How many choices per section?
- **Application:** "With 7±2 sections, users can hold the structure in mind. If you have 12 sections, group them into 5–7 category sections."
- **In this phase:** Determines ideal page architecture — 5–7 main sections is usually right; more requires grouping

**Chunking** — Break information into meaningful groups.
- **Use for:** Grouping related content into sections
- **Application:** "Group 'How it works,' 'Demo,' and 'Use cases' together rather than scattering them. Users process grouped information better."
- **In this phase:** Informs section clustering and hierarchy

**Hick's Law** — Decision time grows with number and complexity of choices.
- **Use for:** Limiting choices per section; breaking flows into steps
- **Application:** "If a section has 7+ options, break it into substeps or use progressive disclosure (show 3, reveal more)."
- **In this phase:** May split one section into multiple, or add progressive disclosure

**Choice Overload** — Too many options hurt decisions and satisfaction.
- **Use for:** Curating what options to show
- **Application:** "This section has 8 features. Show top 3 features, hide the rest behind 'See all.' Users choose better with fewer options."
- **In this phase:** Decides what content is primary vs. secondary/optional

### Progression & Pacing

**Serial Position Effect** — First and last items in a series are remembered best.
- **Use for:** Deciding what goes in first and last position
- **Application:** "Hero section: make it your strongest value prop. Final CTA: make it your clearest call-to-action. Middle sections can be supportive."
- **In this phase:** Shapes hero content, final section content, and nav placement

**Parkinson's Law** — Tasks expand to fill available time.
- **Use for:** Pacing sections and forms to match user expectations
- **Application:** "A long-form section will feel slow. A multi-step form feels like more work. Match section 'weight' to importance."
- **In this phase:** May create sub-sections to break up dense content, or combine lightweight sections

**Paradox of the Active User** — Users skip detailed onboarding and dive in.
- **Use for:** Progressive disclosure — show essentials, hide details
- **Application:** "Instead of a long 'How it works' section, show the core flow visually, with a toggle for detailed steps."
- **In this phase:** Determines if a section needs multiple disclosure levels or collapsed details

**Flow** — Immersion when challenge matches skill.
- **Use for:** Balancing information density with user readiness
- **Application:** "Early sections assume less knowledge; later sections can go deeper. Match section complexity to journey stage."
- **In this phase:** Shapes how much detail/depth each section has relative to where it sits

### Simplification

**Occam's Razor** — Among equal solutions, choose the one with fewest assumptions.
- **Use for:** Deciding what sections to cut
- **Application:** "Do you really need both 'Features' and 'Use cases' sections? Can one section do both? Cut it."
- **In this phase:** Ruthlessly removes sections that don't earn their place

---

## Architecture Decision Workflow

### Step 1: Define User Mental Model

Ask:
- What process does the user *expect* to follow?
- How do they think about the problem → solution journey?
- What familiar patterns have they seen elsewhere (reference sites)?

**Example:**
- Tech buyer expects: Problem → How it works → Proof → Pricing → Sign up
- Luxury traveler expects: Inspiration → Destination details → Personalization → Book

### Step 2: Map Journey Peaks

Using Peak-End Rule + Goal-Gradient:
- Where is the emotional high-point? (Customer success story? Product demo? Breakthrough moment?)
- Where should that sit? (Usually mid-to-late journey, when they're engaged)
- What should the final section feel like? (Action, satisfaction, clarity)

### Step 3: Chunk Content into Sections

Using Miller's Law + Chunking:
- How many sections total? (Aim for 5–7 main sections if possible)
- What belongs together? (Feature details? Proof? Social proof?)
- Is any section doing two jobs? (Can it be split or merged?)

### Step 4: Decide Section Order

Using Serial Position + Zeigarnik + Jakob's Law:
- First section: Strongest value prop (uses Serial Position — first is remembered)
- Middle sections: Supporting information, proof, objection handling
- Final section: Clearest CTA (uses Serial Position — last is remembered)
- Progress: Do users need to *see* progress toward the goal? (Zeigarnik)

### Step 5: Reduce Choices Per Section

Using Hick's Law + Choice Overload:
- How many options/choices does each section present?
- If >5, does it need progressive disclosure or sub-sections?
- Can you recommend a default?

### Step 6: Plan Disclosure Levels

Using Paradox of Active User + Flow:
- What information is essential vs. detailed?
- Does this section need expandable sections ("See details")?
- Can the core message stand alone?

### Step 7: Validate Against Audience

- Does this sequence match the audience's mental model (from audience-research)?
- Does this architecture echo patterns from successful reference sites?
- Are sections ordered by increasing commitment? (Progressive engagement)

---

## Architecture Template

```markdown
# Page Architecture: [Your Site]

## Overall Structure

**Primary goal:** [What's the one thing we want them to do?]
**User mental model:** [How they think about this process]
**Section count:** [Ideal: 5–7 main sections]

## Section Map

| Order | Section | Purpose | Choices offered | Disclosure level |
|-------|---------|---------|-----------------|------------------|
| 1 | Hero | Strongest value prop | None (just CTA) | Surface only |
| 2 | How it works | Show process | 1 CTA variant | Progressive disclosure |
| 3 | Social proof | Build confidence | See testimonials / case study | Expandable |
| 4 | Pricing | Show options | 3 tiers (primary + secondary) | Details on hover |
| 5 | FAQ | Address objections | Expandable categories | Collapsed by default |
| 6 | Final CTA | Conversion | Single, clear CTA | No additional choices |

## Journey Flow (Peak-End + Goal-Gradient)

1. **Arrival (Hero)** — Jakob's Law: familiar pattern, strong value prop
2. **Engagement (How it works)** — Paradox of Active User: show the path quickly
3. **Confidence (Proof)** — Peak-End Rule: emotional high-point here
4. **Consideration (Pricing/Options)** — Hick's Law: 3–5 options max, recommend one
5. **Resolution (FAQ)** — Address lingering objections
6. **Closure (Final CTA)** — Serial Position: strongest call-to-action; clear win

## Information Chunking (Miller's Law)

- **Primary sections:** 5 (easy to hold in mind)
- **Choices per section:** 3 (max; prevents Hick's Law overload)
- **Nav items:** 5 (matches primary section count)

## Disclosure Strategy (Paradox of Active User)

- **Hero:** Surface only
- **How it works:** Show core flow; expand for detailed steps
- **Case study:** Summary visible; click to expand
- **Pricing:** Show 3 main tiers; click for annual pricing / add-ons
- **FAQ:** Questions visible; answers hidden until clicked

## Simplification Check (Occam's Razor)

- Do we need both "Features" AND "How it works"? → Merged into "How it works"
- Do we need "Team" section for conversion? → Cut for now; add later
- Do we need "Blog" link in nav? → Link in footer only (Hick's Law: limit nav)

## Next Steps
- Validate this sequence with [audience-research findings]
- Compare against [reference sites] — do patterns match?
- Ready for /ux-methodology-design to optimize presentation
```

---

## Common Patterns by Audience

### Technical / Skeptical Audience (B2B SaaS, dev tools)
```
Hero (value prop) 
  → Architecture / How it works (show the system)
  → Proof (benchmarks, GitHub stars, case studies)
  → Pricing 
  → FAQ (objection handling)
  → CTA
```

### Impulse / Emotional Audience (Luxury, lifestyle, creator tools)
```
Hero (inspiration)
  → Visual story / Demo (show the experience)
  → Social proof (testimonials, community)
  → How it works (brief, assume they want in)
  → Call to action
```

### Small Business / Practical Audience
```
Hero (outcome: "Save 5 hours/week")
  → Proof (customer stories with results)
  → How it works (simple, not technical)
  → Pricing (clear, no surprises)
  → FAQ
  → CTA
```

---

## Anti-Patterns

- **No clear mental model match** — audience expects X flow, you built Y flow
- **Too many sections** — 10+ sections overwhelm (use grouping or hide less critical ones)
- **Choices scattered** — "What should I do?" at every section instead of progressive narrowing
- **Peak in wrong place** — best content early, nothing surprises mid-journey
- **No progress feeling** — users can't tell if they're closer to the goal
- **Disclosure mismatch** — everything hidden (users don't know what's available) or nothing hidden (overwhelming)
- **Hero → Pricing (no proof)** — skips confidence building
- **Ending without action** — last section is generic footer, not a clear next step

---

## Quality Gate

Before moving to ux-methodology-design:

- [ ] 5–7 main sections identified
- [ ] Section order matches audience mental model (reference sites + audience research)
- [ ] Peak-End rule applied (highest-value section placed strategically)
- [ ] Serial Position considered (strong hero + final CTA)
- [ ] Hick's Law applied (≤5 choices per section, or progressive disclosure)
- [ ] Miller's Law respected (5±2 groups max)
- [ ] Parkinson's Law considered (section weight matches importance)
- [ ] Occam's Razor applied (every section earns its place)
- [ ] Disclosure levels documented (surface vs. expandable)
- [ ] Architecture mapable in table form above
- [ ] Matches reference site patterns OR justified deviation
