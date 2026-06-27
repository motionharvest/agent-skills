---
name: reference-site-analysis
description: >-
  Use after researching your audience. Finds 3–5 successful sites serving that
  audience using real signals (user reviews, market data, engagement) instead of
  search ranking. Analyzes their UX patterns, copy approaches, and visual
  strategies. Outputs validated reference patterns that inform your site
  architecture and design.
---

# Reference Site Analysis

Learn from what's already working with your target audience — not what's trendy or well-marketed, but what users actually validate.

**Distinction:** This skill finds *successful competitors and peers*, analyzes *their UX*, and extracts *patterns that work*. [persona-archetypes](../persona-archetypes/SKILL.md) explains *who your audience is*. [audience-research](../audience-research/SKILL.md) documents *what they need*. Together, reference analysis shows *how others have solved it*.

## When to Apply

- Before designing page architecture — what sections/flows do successful sites use?
- Before choosing copy approach — what messaging angles resonate with this audience?
- Before visual direction — what style/tone do winning sites in this space use?
- Validating assumptions — does the data support your hypothesis about what works?
- Finding anti-patterns — what do successful sites *avoid*?

## Workflow

Copy this checklist:

```
Reference Site Analysis:
- [ ] 1. Define competitive set — who serves similar audience?
- [ ] 2. Find success signals — user reviews, market data, engagement
- [ ] 3. Shortlist high-signal sites (3–5)
- [ ] 4. Analyze UX patterns — sections, flow, hierarchy
- [ ] 5. Extract copy approaches — headlines, messaging, tone
- [ ] 6. Document visual strategy — style, motion, emphasis
- [ ] 7. Identify patterns & anti-patterns
- [ ] 8. Synthesize reference brief
```

---

## Phase 1: Define Competitive Set

**Direct competitors:** Same service/product, same audience
- Example: if building a time-tracking SaaS, Toggl, Clockify, Harvest

**Audience peers:** Different product, same audience or similar psychographics
- Example: if targeting indie developers, look at: Vercel, Supabase, Stripe (serve same audience differently)
- Example: if targeting luxury travelers, look at: Airbnb, Luxury Hotels sites, travel agencies

**Adjacency:** Related category, same audience need
- Example: if targeting small business accountants, Quickbooks, Wave, Xero (direct) but also accounting blogs, CPA association sites

**Geographic/niche variants:**
- If international, find local players in key markets
- If niche, find adjacent verticals serving similar psychographics

Do NOT assume competitors only exist in your immediate category. Cast wide for "who wins with this audience?"

---

## Phase 2: Find Success Signals

**Do NOT rely on search ranking.** High Google rank ≠ good UX. Use real validation:

### User Reviews & Ratings
- **Where to look:** G2, Capterra, Trustpilot, AppStore reviews, Product Hunt, specialized review sites
- **What to extract:** What do users love? What do they complain about? What's the tone?
- **Signal strength:** 100+ reviews with 4.5+ stars = validated product

### Market Performance
- **Revenue/growth:** Crunchbase, PitchBook (if VC-backed), company websites (annual reports, press releases)
- **Funding:** Series stage = investors validated the model; public = users voted with wallets
- **Customer count:** If public, stated customer numbers; if not, infer from social, job postings
- **Signal strength:** Growing revenue and customers = solving real problems

### Engagement & Community
- **Social metrics:** Twitter followers, newsletter subscribers, community Discord/Slack activity
- **Content engagement:** Average blog post comments, YouTube video engagement
- **Community participation:** How active is their community forum or subreddit?
- **Signal strength:** Organic engagement (not paid followers) shows audience resonance

### Third-Party Validation
- **Awards:** Industry awards, publication recognition (not marketing awards)
- **Press:** Reputable media coverage, not just press releases
- **Partnerships:** Strategic partnerships suggest market position
- **Signal strength:** Real partnerships > press releases

### Alternative: No Direct Metrics Available?
Look for **proxy signals:**
- Job postings volume (hiring = growth)
- Domain age & stability (still operating after 5+ years)
- Regular product updates (active development)
- Community mentions in research (from Phase 1 audience-research)

---

## Phase 3: Shortlist High-Signal Sites

**Score each site:**

| Signal | Points | Notes |
|--------|--------|-------|
| User reviews 4.5+ stars, 100+ reviews | 3 | Gold standard |
| Growing revenue / funding validated | 2 | Market signal |
| 1000+ social engagement/month | 1 | Audience resonance |
| Awards / reputable press | 1 | Third-party validation |

**Threshold:** Pick top 3–5 with 5+ points combined. Quality > quantity.

**Avoid:**
- Sites ranked #1 on Google (probably paid SEO, not UX)
- Sites with negative reviews (even if pretty)
- New sites without history (can't validate)
- Sites that don't serve your specific audience

---

## Phase 4: Analyze UX Patterns

Visit each shortlisted site. Document:

### Page Structure & Sections
- **Hero section:** What's the value prop? How long? Image/video/animation?
- **Section order:** What comes after hero? How many sections total?
- **Sections present:** Proof section? Pricing? FAQ? How-it-works? Social proof? CTA placement?
- **Navigation:** What's in the nav? How many items? Sticky?

### Copy Approach
- **Headline:** What's the lead? Outcome-first? Problem-first? Feature-first?
- **Subheading:** Does it expand on the headline or address an objection?
- **Body copy:** Long-form or scannable bullets? Technical or narrative?
- **CTA copy:** Action verb? Specific or vague? Single or multiple CTAs?
- **Tone:** Formal/casual? Urgent/relaxed? Technical/narrative?

### Visual Hierarchy
- **Hero emphasis:** What's the most prominent element? Color contrast?
- **Section emphasis:** How does the eye move down the page?
- **White space:** Dense or open? Breathing room or packed?
- **Typography:** Serif or sans-serif? How many font weights? Headings vs body hierarchy?
- **Color palette:** Primary + accent colors; where do they emphasize?

### Interaction & Motion
- **Scroll effects:** Parallax? Fade-in? Animations on scroll?
- **Hover states:** Buttons change? Images reveal? Links animated?
- **Micro-interactions:** Form validation? Success states? Loading indicators?
- **Video/animation:** Autoplaying? Muted? Where does video sit in flow?

### Trust Signals
- **Social proof placement:** Logos, testimonials, metrics — where and how prominent?
- **Credentials:** Team bios, certifications, awards — if shown, where?
- **Security/compliance:** Badges, privacy language — how visible?
- **Proof type:** Case studies? Customer logos? Metrics? Reviews embedded?

---

## Phase 5: Pattern Extraction

Across the 3–5 sites, identify:

### Consistent Patterns (What's working)
- Do all sites use a "How it works" section? Where? What form does it take?
- Do they all lead with outcome vs. features? 
- Do they all show customer logos? Testimonials? Metrics?
- Do they use video/animation consistently?
- Is there a common CTA flow?

### Differentiators (What's unique, and why)
- One site is more narrative; one is data-driven. For which audience segment?
- One leads with pricing; others hide it. Why might that matter?
- One is animated; one is static. Does it match their audience?

### Anti-Patterns (What successful sites avoid)
- Do they avoid auto-playing video?
- Do they avoid cluttered navigation?
- Do they avoid long forms?

### Audience-Specific Signals
- **For developers:** Do they show code, architecture, technical depth?
- **For luxury:** Do they emphasize exclusivity, heritage, craftsmanship?
- **For small business:** Do they lead with ROI/simplicity, case studies?
- **For creative:** Do they prioritize visuals, portfolio, community?

---

## Phase 6: Reference Analysis Brief

```markdown
# Reference Site Analysis: [Audience Segment]

## Competitive Set
| Site | Signal Score | Why chosen |
|------|--------------|-----------|
| [Site 1] | 7/10 | [key validation: reviews, revenue, engagement] |
| [Site 2] | 6/10 | ... |
| [Site 3] | 5/10 | ... |

## Common Patterns (All high-signal sites)
### Section Structure
- **Hero + subheading** → single strong value prop
- **"How it works" section** → [visual style: timeline/steps/video]
- **Social proof** → [form: logos/metrics/testimonials; placement: after hero or mid-page]
- **CTA placement** → [multiple CTAs or single? button style?]

### Copy Approach
- **Headline angle:** [outcome-first / problem-first / identity-first]
- **Example:** "[exact headline from site 1], [site 2], [site 3]"
- **Tone:** [professional/narrative/urgent/relatable/technical]

### Visual Strategy
- **Color palette:** [primary, accent — psychology match for audience]
- **Typography:** [serif/sans? why that choice for this audience]
- **Motion:** [consistent across sites? autoplaying video? animations?]
- **Density:** [information-dense or spacious? match to audience research]

## Differentiation Points (Where sites diverge)
| Aspect | Site A | Site B | Site C |
|--------|--------|--------|--------|
| Pricing placement | Hidden | Prominent | Mid-page |
| Video use | Heavy | Minimal | None |
| Technical depth | High | Medium | Low |

**Why it matters:** [which audience segment values which approach]

## Anti-Patterns (Avoided by successful sites)
- Autoplaying audio (all sites avoid)
- Cluttered navigation (all keep it to 5 items max)
- Long forms upfront (all use progressive disclosure or short lead magnets)

## Implications for Your Site

### What to Adopt
- Copy approach: [which headline angle works for this audience]
- Section order: [proven sequence for this audience]
- Trust signals: [what validation matters most]
- Visual tone: [style that matches audience psychographics]

### What to Avoid
- [Which anti-patterns did successful sites skip?]

### Unique Opportunity
- [Where can you differentiate or improve on the reference sites?]

## Next Steps
- Use these patterns to inform page architecture
- Cross-reference with ux-methodology for optimization
- Choose visual preset (motion-web-design) aligned with these patterns
```

---

## Anti-Patterns

- **Only analyzing competitors** — audience peers matter just as much
- **Relying on Google ranking** — search rank ≠ UX quality
- **Choosing sites because they look cool** — need real validation signals
- **Analyzing too many sites** — 3–5 high-signal > 20 random sites
- **No recency check** — old screenshots don't show current state (visit live sites)
- **Confusing aesthetic preference with data** — "I like this design" ≠ "users validated this"
- **Ignoring anti-patterns** — what's *not* on successful sites is as important
- **Skipping the "why"** — pattern without context is just cargo culting
- **No signal validation** — visiting a site with 1 star reviews wastes time

---

## Example: Indie Developer SaaS

**High-signal sites:** Vercel, Supabase, Stripe, GitHub

**Pattern 1: Technical credibility first**
- All show architecture diagrams, performance metrics, code examples
- All lead with "built for developers"
- Testimonials come mid-page, not hero

**Pattern 2: Copy angle**
- "The platform built by developers, for developers" or similar
- Lead with capability, not outcome
- Heavy use of code snippets

**Pattern 3: Visual strategy**
- Dark/black background (developer aesthetic)
- Neon or vibrant accent (stands out against dark)
- Minimal animation (respect dev time sensitivity)
- Monospace font for code

**Anti-patterns avoided:**
- No "sign up now!" urgency
- No generic testimonials
- No feature lists without context

**Unique opportunity:** If other sites feel corporate/corporate-y, could break through with genuine community voice or case studies from builders.

---

## Example: Luxury Travel Advisors

**High-signal sites:** Luxury hotel sites, high-end travel agencies, premium travel creators

**Pattern 1: Exclusivity & curation**
- Heavy emphasis on "handpicked," "curated," "private"
- Testimonials are highly specific travel stories, not generic praise
- Imagery prioritizes the experience over the transaction

**Pattern 2: Copy angle**
- Lead with aspiration ("Discover untouched..." not "Book now")
- Narrative-driven, not feature-driven
- Emphasize personalization and relationships

**Pattern 3: Visual strategy**
- High-quality photography (often cinematic video)
- Serif typography (elegance, heritage)
- Generous whitespace (breathing room, premium feel)
- Warm color palette (accessible luxury vs. cold premium)
- Motion is subtle and purposeful

**Anti-patterns avoided:**
- No "limited time offer" urgency
- No generic map pins
- No feature lists (only experience-forward language)

**Unique opportunity:** Could emphasize sustainability or local impact while maintaining luxury feel.

---

## Quality Gate

Before handing off to ux-methodology-process:

- [ ] 3–5 sites shortlisted with combined signal score ≥5
- [ ] Signals documented (reviews, revenue, engagement data)
- [ ] UX patterns extracted across all sites
- [ ] Copy approaches captured with exact headlines
- [ ] Visual strategies documented (not subjective opinions)
- [ ] 3+ consistent patterns identified
- [ ] Anti-patterns named explicitly
- [ ] Differentiation points documented
- [ ] Implications for your site are explicit
- [ ] Why these sites work (for this audience) is explained
