# Persona Synthesis — Combining Frameworks

How to merge archetype systems into actionable personas without framework soup.

---

## Synthesis Workflow

```
1. RESEARCH    → interviews, analytics, sales notes, reviews
2. HYPOTHESIZE → pick 2-3 frameworks that explain observed behavior
3. DRAFT       → persona card (see SKILL.md template)
4. STRESS TEST → does it predict channel, objections, tone?
5. PRIORITIZE  → primary (70% focus) + secondary (20%) + anti (10%)
6. DERIVE      → messaging matrix, UX implications, motion direction
7. VALIDATE    → test copy/creative with real segment members
```

---

## Framework Combination Recipes

### Recipe: B2B SaaS Primary Buyer

| Layer | Framework | Why |
|-------|-----------|-----|
| Traits | Big Five + DISC | communication in sales cycle |
| Motivation | Enneagram or McClelland | what drives the purchase |
| Context | Buying Committee role | content format |
| Behavior | Technographics | where to reach them |

### Recipe: D2C Lifestyle Brand

| Layer | Framework | Why |
|-------|-----------|-----|
| Identity | Jung + VALS | brand story + lifestyle |
| Motivation | Schwartz values | cause and tone |
| Behavior | Shopping archetype | funnel design |
| Context | Generational (light) | channel selection |

### Recipe: Developer Tool

| Layer | Framework | Why |
|-------|-----------|-----|
| Traits | Big Five (O↑, C↑, E↓) | doc-heavy, skeptical |
| Motivation | Enneagram 5 | competence, understanding |
| Identity | Jung Sage | truth, depth |
| Context | RIASEC (I/R) | content topics |
| Behavior | Spectator/Critic | HN, docs, not TikTok |

### Recipe: Luxury Service

| Layer | Framework | Why |
|-------|-----------|-----|
| Identity | Jung Ruler + Lover | status + experience |
| Segment | VALS Achiever/Experiencer | resources + motivation |
| Shopping | Experience Seeker | pays for moments |
| Motion | SkyElite / Velorah | site archetype match |

---

## Multi-Persona Map Template

```markdown
# Audience Map — [Product/Brand]

## Primary (60–70% revenue/fit)
**Name:** [Archetype Name]
**Framework stack:** [list]
**One line:** [essence]
**Key message:** [single sentence value prop]

## Secondary (20–30%)
**Name:** [Archetype Name]
**Framework stack:** [list]
**One line:** [essence]
**Key message:** [single sentence]

## Anti-Persona (explicitly NOT for)
**Name:** [Who we don't serve]
**Why:** [misaligned expectations, support burden, wrong JTBD]
**What we say no to:** [feature requests, deals to decline]
```

---

## Segment Matrix (2×2 Examples)

### Openness × Resources (VALS-adjacent)

```
                    High Resources
        ┌──────────────┬──────────────┐
        │  Innovator   │  Achiever    │
 High O │  Explorer    │  Experiencer  │
        ├──────────────┼──────────────┤
        │  Maker       │  Believer    │
 Low O  │  (practical) │  (traditional)│
        └──────────────┴──────────────┘
                    Low Resources
```

### Risk × Research Depth

```
                    Deep Research
        ┌──────────────┬──────────────┐
        │  Analyst     │  Researcher  │
 Low    │  (enterprise)│  (comparison)│
 Risk   ├──────────────┼──────────────┤
        │  Satisficer  │  Impulse     │
 High   │  (trusted    │  (emotional  │
 Risk   │   default)   │   trigger)   │
        └──────────────┴──────────────┘
                    Quick Decision
```

---

## Messaging Matrix

| Persona | Headline angle | Proof type | CTA | Tone |
|---------|----------------|------------|-----|------|
| Sage / Type 5 | "Understand how it works" | whitepaper, architecture | "Read docs" | precise |
| Hero / Type 3 | "Win faster" | metrics, logos | "Start winning" | bold |
| Caregiver / Type 2 | "Support your team" | testimonials | "Help your team" | warm |
| Rebel / Experiencer | "Break the rules" | disruptive case study | "Join the movement" | raw |
| Ruler / Achiever | "Command your market" | executive brief | "Schedule briefing" | authoritative |

---

## Persona Audit Checklist

Use when reviewing existing personas or creative:

```
Persona Quality Audit:
- [ ] Named archetype (memorable, not "Persona 2")
- [ ] Core tension stated (want vs fear)
- [ ] Max 3 frameworks, each adds unique insight
- [ ] Behavioral evidence cited (not invented)
- [ ] Anti-patterns listed (what repels them)
- [ ] Channel + format specified
- [ ] UX/motion implications derived
- [ ] Objections + responses mapped
- [ ] Quote sounds like a real human
- [ ] Primary vs secondary prioritized
- [ ] Anti-persona defined
- [ ] Not demographic-only
```

---

## Discovery Interview Questions

### Traits & style
- "Walk me through how you decided on your last [category] purchase."
- "Do you prefer to research alone or ask others first?"
- "What would make you trust a brand you'd never heard of?"

### Motivation
- "What would success look like in 6 months?"
- "What's the worst outcome if you choose wrong?"
- "Who else needs to agree with this decision?"

### Behavior
- "Where did you first hear about solutions like this?"
- "Do you post reviews, or only read them?"
- "How long from first visit to purchase typically?"

### Framework mapping (internal — don't ask directly)
- Listen for Enneagram fears in "worst outcome" answers
- Listen for Big Five in research vs impulse patterns
- Listen for VALS in status vs practicality language
- Listen for Technographics in create vs lurk behavior

---

## Persona → Motion Site Mapping

Connect to [motion-web-design/presets.md](../motion-web-design/presets.md) and [modules/](../motion-web-design/modules/README.md):

| Audience signals | Preset base | Module notes |
|------------------|-------------|--------------|
| Sage, high C, low E | VEX, SynapseX | motion.subtle; video raw or gradient |
| Lover, Experiencer, high O | Velorah, Organic Odyssey | typography cinematic-serif |
| Ruler, Achiever, premium | SkyElite, VANGUARD | colors light-premium or bold-agency |
| Creator, high O, editorial | Prisma | sections full-editorial |
| Explorer, experiential | Organic Odyssey, Lithos | interactions cursor-spotlight |

---

## Common Synthesis Mistakes

| Mistake | Fix |
|---------|-----|
| "Our user is everyone" | Force primary/secondary split |
| MBTI + Enneagram + DISC + VALS on one card | Pick 2-3 max |
| Persona is the founder | Interview actual users |
| Demographics only | Add motivation + behavior |
| Static persona, never updated | Revisit quarterly with data |
| Creative ignores persona | Put persona card in brief |
| One site for incompatible personas | Split pages or prioritize |

---

## Quick Persona from Minimal Input

When user gives only a product category, infer starting hypothesis:

| Category | Default hypothesis stack | Validate with |
|----------|-------------------------|---------------|
| Dev tools | Type 5, Sage, I-RIASEC, Spectator | HN, GitHub stars |
| Luxury consumer | Achiever, Ruler, Experience Seeker | Instagram, concierge |
| Wellness | Believer/Maker, Caregiver, LOHAS | community, reviews |
| Agency portfolio | Creator, Type 4, Experiencer | Behance, case studies |
| Fintech | Thinker, high C, Guardian privacy | trust badges, compliance |
| EdTech | Social RIASEC, varied generations | completion data |

**Label as hypothesis** until validated.

---

## Output Formats

### One-liner (for briefs)
> **[Name]** — [Jung archetype] [VALS segment] who [core JTBD] and fears [core fear].

### Slide (for stakeholders)
- Photo placeholder
- Name + role
- 3 bullets: goals, frustrations, behaviors
- 1 quote
- Framework tags (small)

### Full card
Use template in [SKILL.md](SKILL.md)

### Segment map
Use multi-persona template above
