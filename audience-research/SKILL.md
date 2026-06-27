---
name: audience-research
description: >-
  Use when you need to understand your target audience before building personas.
  Identifies the right research sources for any audience segment, searches for
  real pain points, barriers, language, and decision criteria. Outputs research
  synthesis that grounds personas in evidence, not assumptions.
---

# Audience Research

Ground your design decisions in what real users are actually saying and experiencing. This skill finds authentic signals from your target audience across the right sources — avoiding assumptions and marketing noise.

**Distinction:** This skill surfaces *what users need* (pain points, barriers, language). [persona-archetypes](../persona-archetypes/SKILL.md) then explains *who they are* (psychology, decision style, motivation). Together they create personas backed by evidence.

## When to Apply

- Starting a new site or product — need to understand the audience first
- Refining messaging — what language resonates with the segment?
- Identifying pain points and barriers to entry
- Validating audience assumptions before investing in design
- Discovering objections and concerns users actually have
- Finding trust signals that matter to this segment

## Workflow

Copy this checklist:

```
Audience Research:
- [ ] 1. Scope — define the audience segment clearly
- [ ] 2. Map sources — identify where this audience congregates
- [ ] 3. Search — look for pain points, barriers, language, objections
- [ ] 4. Extract quotes — capture authentic voice and concerns
- [ ] 5. Synthesize findings — group into themes
- [ ] 6. Identify trust signals — what makes them confident?
- [ ] 7. Draft research brief — output for persona-building
- [ ] 8. Validate against reference sites (next skill)
```

---

## Phase 1: Scope the Audience

Be specific. "Tech entrepreneurs" is too broad. "SaaS founder, B2B, <$50M ARR, first-time fundraiser" is researchable.

**Define:**
- Primary persona / segment (who are we researching?)
- Context (B2B/B2C, industry, life stage, role)
- Geography (if relevant)
- Pain point hypothesis (what might they struggle with?)

---

## Phase 2: Map Research Sources

**Do NOT assume all audiences use tech sources.** Match the source to where the audience actually congregates:

| Audience segment | Primary sources | Secondary sources |
|---|---|---|
| Tech/developer | Hacker News, GitHub issues, dev Twitter, Stack Overflow | Reddit tech subs, Discord communities |
| Small business/e-commerce | Facebook groups, industry forums, Shopify community | Reddit, YouTube, TikTok business creators |
| Finance/advisory | LinkedIn, industry forums, Twitter finance | Podcasts, newsletters, Medium |
| Creative/design | Twitter/X creator space, Dribbble, Designer Hangout | Instagram, TikTok, design Discord |
| Luxury/premium | Instagram, TikTok, brand-specific communities, forums | Pinterest, YouTube, lifestyle Reddit |
| Healthcare/wellness | Reddit health communities, patient forums, Facebook groups | WebMD comments, Trustpilot, Google reviews |
| Enterprise B2B | LinkedIn, G2/Capterra reviews, industry conferences, Slack | Gartner reports, industry publications |
| Content creators | TikTok, YouTube, Twitter, Substack | Discord communities, patreon discussions |
| Freelancers/contractors | Reddit (r/freelance), Twitter, Slack communities | Industry Discord, Facebook groups |

**Priority order for each source:**
1. **First-party communities** (subreddits, Discord, Slack, forums specific to the industry)
2. **Review platforms** (G2, Capterra, Trustpilot, AppStore ratings) — signal + quotes
3. **Social media** (Twitter/LinkedIn for professionals, TikTok/Instagram for creators)
4. **Aggregator platforms** (Hacker News, ProductHunt, Indie Hackers)
5. **Content** (blogs, podcasts, YouTube comments from that niche)

---

## Phase 3: Search & Extract

For each source, look for:

### Pain Points
- What problems do they mention repeatedly?
- What frustrates them about current solutions?
- What's the gap between what they want and what exists?

**Search terms:** "frustrating," "wish it," "hate when," "broken," "can't," "problem with"

### Barriers to Entry
- What stops them from trying something?
- What concerns do they have?
- What is the friction?

**Search terms:** "scared of," "hesitant to," "worried about," "can't afford," "too complicated," "don't trust"

### Language & Terminology
- What words do they use to describe their problems?
- What jargon matters? What misses the mark?
- How do they self-identify?

**Search terms:** Look at how they talk about themselves and their work — not how marketers talk about them.

### Decision Criteria
- What influences their choice?
- What proof do they ask for?
- What makes them confident?

**Search terms:** "how do you choose," "what matters most," "worth it if," "would need"

### Objections & Concerns
- What are they skeptical about?
- What's the #1 reason they'd say no?
- What catches them off guard?

**Search terms:** "but what about," "haven't tried because," "seems like"

### Extract Real Quotes
Do NOT paraphrase. Capture exact quotes showing:
- The pain point they name
- Their tone (urgent? resigned? hopeful?)
- Specificity (concrete examples beat vague complaints)

---

## Phase 4: Synthesis

Group findings into **4–6 themes**:

```markdown
## Research Findings

### Theme 1: [Clear name]
- **Signal:** [pattern observed across multiple sources]
- **Quotes:** 
  - "[exact quote]" — [source]
  - "[exact quote]" — [source]
- **Implication for design:** [how this changes what we build]

### Theme 2: [Clear name]
...
```

**Avoid:**
- Lumping everything together ("users want good UX")
- Single-source findings (need at least 2 sources agreeing)
- Interpretations instead of data (source quote first, then your analysis)

---

## Phase 5: Identify Trust Signals

What makes *this* audience confident? (Varies wildly by segment)

| Audience | Trust signals |
|---|---|
| Tech/developers | Transparent specs, GitHub stars, peer proof (HN upvotes), benchmarks, case studies |
| Finance/advisory | Credentials, third-party validation (Gartner, awards), regulatory compliance, long track record |
| Small business | Customer stories, case studies, clear ROI, no complexity, local presence |
| Creative | Portfolio, social proof (followers, collaborations), aesthetic quality, creative freedom |
| Healthcare | Medical credentials, peer review, patient testimonials, regulatory approval |
| Luxury | Exclusivity, heritage, craftsmanship proof, curator selection, premium aesthetics |

Extract: "How do they signal trust in the research?" This informs design decisions downstream.

---

## Phase 6: Research Brief Output

```markdown
# Audience Research Brief: [Segment Name]

## Scope
- **Segment:** [who]
- **Context:** [B2B/B2C, industry, life stage]
- **Research sources:** [which platforms searched]

## Key Findings

### Pain Point #1: [Name]
- **Evidence:** [what they're saying]
- **Quotes:** [2–3 exact quotes with source]
- **Frequency:** [how common]

### Pain Point #2: [Name]
...

### Barriers to Entry
- **Concern #1:** [what stops them]
- **Concern #2:** [what stops them]

### Language & Tone
- **They say:** [actual terminology]
- **They don't like:** [misses, jargon that fails]
- **Tone:** [how they talk — urgent/casual/technical/emotional]

### Decision Criteria
- **What matters:** [what influences their choice]
- **Proof they want:** [what validates trust]

### Trust Signals in This Segment
- **#1 signal:** [what makes them confident]
- **#2 signal:** [what makes them confident]

## Next Steps
- Validate against reference sites (who is winning with this audience?)
- Use these insights + frameworks to build persona card
```

---

## Anti-Patterns

- **Demographic-only research** — "millennials aged 25–35" without psychographics
- **Single-source findings** — one Reddit thread ≠ evidence
- **Paraphrasing instead of quoting** — your interpretation ≠ their voice
- **Assuming tech sources universally** — HN is wrong for most audiences
- **No timestamp / recency check** — 5-year-old threads may not reflect current state
- **Mixing audience segments** — "young professionals" conflates student, recent grad, and mid-career
- **Ignoring negative signals** — if no one mentions a pain point, it's probably not one
- **Skipping objections** — what they DON'T say is often as important as what they do

---

## Quick-Start Examples

### Example 1: B2B SaaS for accountants
**Sources:** 
- r/accounting, r/accountant
- LinkedIn accountant groups
- Accounting software reviews (G2, Capterra)
- AccountingToday forum, Slack communities

**Search for:** "frustrated with manual entry," "compliance headache," "client data security," "integrations broken"

### Example 2: Indie game developers
**Sources:**
- r/gamedev, r/indiegames
- Twitter #gamedev #indiedev
- Game dev Discord communities
- YouTube game dev channels + comments
- itch.io community forums

**Search for:** "marketing is hard," "discoverability nightmare," "engine choice," "funding barriers"

### Example 3: Luxury travel advisors
**Sources:**
- Instagram luxury travel creators
- TikTok luxury niche
- Luxury travel subreddits
- Luxury brand communities
- Travel blogs + comments
- Pinterest luxury boards

**Search for:** "authentic experiences," "overtourism concerns," "budget flexibility," "personalization"

---

## Quality Gate

Before handing off to persona-archetypes:

- [ ] 4–6 themes identified with evidence from multiple sources
- [ ] Real quotes extracted (not paraphrases)
- [ ] Pain points are specific, not generic ("hard to find customers" not "marketing is hard")
- [ ] Barriers to entry documented
- [ ] Language & tone captured
- [ ] Trust signals for this segment named
- [ ] No single-source findings
- [ ] Implications for design are explicit (not just observations)
