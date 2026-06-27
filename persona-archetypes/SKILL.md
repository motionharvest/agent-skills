---
name: persona-archetypes
description: >-
  Use when defining a target audience, buyer persona, or ICP. Applies layered
  psychological and behavioral frameworks (Big Five, Enneagram, Jung, VALS,
  DISC) to identify who the audience is, how they decide, what messaging
  resonates, and what UX or motion style fits them.
---

# Persona Archetypes

Aggregation of personality, motivation, brand-story, marketing, and digital-behavior frameworks for defining **who** a person or audience is — not just demographics, but how they think, decide, feel, consume, and respond.

**Distinction:** [motion-web-design/archetypes.md](../motion-web-design/archetypes.md) covers **visual site layouts** (VEX, Velorah, etc.). This skill covers **human personas and audiences**.

## When to Apply

- Creating or refining user personas, ICPs, or buyer profiles
- Choosing tone, messaging, or content strategy for a segment
- Mapping brand voice to audience psychology
- Designing UX/motion for specific decision styles or trust thresholds
- Auditing whether creative speaks to one personality type only

## Workflow

Copy this checklist when building a persona:

```
Persona Build:
- [ ] 1. Scope — one primary persona or segment map?
- [ ] 2. Context — B2B/B2C, category, channel, life stage
- [ ] 3. Pick 2–3 frameworks max (see Framework Picker below)
- [ ] 4. Layer frameworks — traits → motivations → behavior → expression
- [ ] 5. Draft persona card (template below)
- [ ] 6. Derive implications — messaging, channels, UX, motion, objections
- [ ] 7. Name the archetype — memorable label, not just "User A"
- [ ] 8. Validate — does this explain real observed behavior?
```

**Rule:** Never stack more than 3 frameworks on one persona. More frameworks ≠ more accuracy; they dilute messaging.

## Framework Picker

| If you need to understand… | Start with | Add if needed |
|----------------------------|------------|---------------|
| How they think & decide | Big Five (OCEAN) | MBTI or DISC |
| Deep motivations & fears | Enneagram | Schwartz Values |
| Work/collaboration style | DISC | MBTI or RIASEC |
| Career/vocation pull | Holland RIASEC | Big Five |
| Brand story & emotional hook | Jung 12 Archetypes | Hero's Journey roles |
| Consumer lifestyle segment | VALS | Generational cohort |
| Tech/social adoption | Diffusion of Innovation | Social Technographics |
| B2B buying dynamics | Buying Committee roles | DISC + Jobs to Be Done |
| Relationship/trust style | Attachment styles | Love languages |
| Gamified/community product | Bartle player types | 90-9-1 rule |
| What job they're hiring you for | Jobs to Be Done | Empathy map |
| Values that drive choices | Schwartz 10 Values | Maslow needs level |

Full catalog (50+ systems): [frameworks.md](frameworks.md)

## Layering Order

Apply frameworks in this sequence — each layer answers a different question:

```
1. TRAITS      → How are they wired?        (Big Five, MBTI, DISC)
2. MOTIVATION  → What do they want/fear?     (Enneagram, Schwartz, Maslow)
3. IDENTITY    → What story do they tell?    (Jung archetype, VALS segment)
4. BEHAVIOR    → What do they actually do?  (Technographics, diffusion, 90-9-1)
5. CONTEXT     → When/where does this show? (Generational, B2B role, JTBD)
```

## Persona Card Template

```markdown
# [Archetype Name] — [One-line essence]

## Snapshot
- **Segment:** [primary / secondary audience]
- **Role:** [job title, life role, or relationship to product]
- **Core tension:** [want vs fear in one sentence]

## Framework Stack
| Layer | Framework | Profile |
|-------|-----------|---------|
| Traits | Big Five | O↑ C→ E↓ A↑ N↓ |
| Motivation | Enneagram | Type 5 — Investigator |
| Identity | Jung | Sage (primary), Explorer (secondary) |
| Behavior | Social Technographics | Critic → Collector |
| Context | B2B role | Technical evaluator |

## Psychographic Profile
- **Values:** knowledge, autonomy, craft quality
- **Fears:** being wrong publicly, vendor lock-in, hype without substance
- **Decision style:** research-heavy, slow, evidence-first
- **Trust signals:** case studies, transparent specs, peer proof
- **Anti-patterns:** urgency tactics, vague superlatives, dark patterns

## Messaging
- **Tone:** precise, respectful, understated confidence
- **Lead with:** proof, methodology, long-term value
- **Avoid:** hype, FOMO, celebrity endorsements
- **CTA style:** "See the data" / "Read the architecture" not "Buy now"

## Channel & Media
- **Where:** technical blogs, Hacker News, podcasts, documentation
- **Format:** long-form, diagrams, benchmarks, comparison tables
- **Social role:** Spectator → Critic (reads, rarely posts)

## UX & Motion Implications
- **Density:** information-rich, scannable hierarchy
- **Motion:** subtle, purposeful — no gratuitous animation
- **Onboarding:** optional deep-dive, skip-friendly for experts
- **Friction tolerance:** high for forms if value is clear; zero for dark patterns

## Objections & Responses
| Objection | Response angle |
|-----------|----------------|
| "Is this proven?" | Third-party validation, metrics |
| "Too complex" | Progressive disclosure, sane defaults |

## Quote (in their voice)
> "I don't need another tool. I need the right tool — and I need to understand exactly how it works before I commit."
```

## Quick-Reference Indices

### Jung 12 Brand/Audience Archetypes

| Archetype | Core desire | Fear | Voice |
|-----------|-------------|------|-------|
| Innocent | safety, happiness | punishment for wrongdoing | optimistic, simple |
| Everyman | belonging, connection | standing out, exclusion | friendly, relatable |
| Hero | mastery, courage | weakness, vulnerability | bold, inspiring |
| Caregiver | protect, serve others | selfishness, ingratitude | warm, generous |
| Explorer | freedom, discovery | entrapment, conformity | adventurous, authentic |
| Rebel | revolution, change | powerlessness, ineffectiveness | disruptive, raw |
| Lover | intimacy, passion | loneliness, rejection | sensual, appreciative |
| Creator | innovation, expression | mediocrity, stagnation | imaginative, artistic |
| Jester | joy, living in moment | boredom, gloom | playful, irreverent |
| Sage | truth, understanding | ignorance, deception | wise, analytical |
| Magician | transformation, vision | unintended consequences | visionary, charismatic |
| Ruler | control, prosperity | chaos, being overthrown | authoritative, refined |

### Big Five at a Glance

| Trait | High → | Low → |
|-------|--------|-------|
| Openness | curious, creative, novelty-seeking | practical, conventional, routine |
| Conscientiousness | organized, disciplined, reliable | flexible, spontaneous, casual |
| Extraversion | outgoing, energetic, talkative | reserved, solitary, reflective |
| Agreeableness | cooperative, trusting, empathetic | competitive, skeptical, direct |
| Neuroticism | emotionally reactive, anxious | calm, resilient, steady |

### Enneagram Motivation Map

| Type | Name | Core desire | Core fear |
|------|------|-------------|-----------|
| 1 | Reformer | integrity, improvement | being corrupt/evil |
| 2 | Helper | being loved, needed | being unwanted |
| 3 | Achiever | success, admiration | worthlessness |
| 4 | Individualist | identity, significance | having no identity |
| 5 | Investigator | competence, understanding | being useless/incompetent |
| 6 | Loyalist | security, support | being without support |
| 7 | Enthusiast | satisfaction, fulfillment | pain, deprivation |
| 8 | Challenger | self-protection, control | being controlled/harmed |
| 9 | Peacemaker | inner stability, peace | loss, fragmentation |

### DISC Workplace Styles

| Style | Pace | Priority | Prefers |
|-------|------|----------|---------|
| D Dominance | fast | results | directness, control |
| I Influence | fast | people | enthusiasm, recognition |
| S Steadiness | steady | cooperation | stability, sincerity |
| C Conscientiousness | deliberate | accuracy | data, quality |

### VALS Consumer Segments

| Segment | Motivation | Resources | Marketing hook |
|---------|------------|-----------|----------------|
| Innovators | varied | high | leading-edge, best-in-class |
| Thinkers | ideals | high | knowledge, proven value |
| Believers | ideals | low | tradition, trust, community |
| Achievers | achievement | high | status, success, premium |
| Strivers | achievement | low | aspirational, accessible luxury |
| Experiencers | self-expression | high | novelty, energy, experience |
| Makers | self-expression | low | practical, DIY, functional |
| Survivors | security | low | safety, value, simplicity |

## Combining Frameworks — Examples

**SaaS developer tool (B2B)**
- Big Five: high Openness, high Conscientiousness, low Extraversion
- Enneagram 5 + Jung Sage
- Social Technographics: Critic/Spectator
- Buying role: Technical evaluator
- Motion site: SynapseX or VEX archetype (see motion-web-design)

**Luxury travel (B2C)**
- VALS: Achiever or Experiencer
- Enneagram 3 or 7
- Jung: Ruler + Lover
- Generational: Gen X or older Millennial HENRYs
- Motion site: SkyElite or Velorah

**Creative studio audience**
- Big Five: high Openness, moderate Extraversion
- Enneagram 4 + Jung Creator
- VALS: Experiencers
- Social: Creator/Conversationalist
- Motion site: Prisma or VANGUARD

## Design & Motion Mapping

| Persona signal | Visual/motion direction |
|----------------|-------------------------|
| High Openness | experimental layout, novel interactions |
| High Conscientiousness | clear hierarchy, predictable nav, specs visible |
| Low Extraversion | calm pacing, no autoplay audio, generous whitespace |
| Enneagram 3/Achiever | social proof, metrics, premium polish |
| Enneagram 5/Sage | depth on demand, documentation links, no fluff |
| Rebel/Experiencer VALS | bold type, kinetic motion, rule-breaking |
| Believer/Survivor VALS | familiar patterns, trust badges, conservative palette |
| Spectator behavior | strong hero, minimal required interaction |
| Creator behavior | shareable moments, embed tools, UGC hooks |

## Evidence Hierarchy

When citing frameworks, respect scientific rigor:

| Tier | Frameworks | Use for |
|------|------------|---------|
| A — Strong empirical | Big Five, HEXACO, RIASEC, Schwartz Values | messaging tests, trait-based personalization |
| B — Useful heuristics | DISC, MBTI, Enneagram, Jung 12, VALS | workshops, creative direction, team alignment |
| C — Behavioral observation | Technographics, 90-9-1, diffusion curve | channel strategy, community design |
| D — Cultural/fun | Astrology, Human Design, doshas | only if audience explicitly uses them |

Never present Tier B–D as science. Label them as narrative or strategic tools.

## Anti-Patterns

- **Demographics-only personas** — age + job title without psychographics
- **Framework soup** — 6+ systems on one card
- **Stereotype trap** — "all Gen Z want X" without segment nuance
- **Designer projection** — building for yourself, not the segment
- **Single-archetype sites** — premium brands often need primary + secondary audience

## Additional Resources

- [frameworks.md](frameworks.md) — Master catalog of 50+ archetype systems
- [psychological.md](psychological.md) — MBTI 16, Enneagram wings/instincts, Big Five facets, RIASEC, temperaments
- [brand-motivation.md](brand-motivation.md) — Jung families, Schwartz values, Maslow, Hero's Journey roles, Spiral Dynamics
- [audience-digital.md](audience-digital.md) — VALS detail, technographics, diffusion, generational, B2B roles, JTBD, empathy maps
- [behavioral-relational.md](behavioral-relational.md) — Attachment, love languages, conflict styles, VARK, communication styles
- [synthesis.md](synthesis.md) — Multi-persona maps, segment matrices, audit checklist, interview questions
