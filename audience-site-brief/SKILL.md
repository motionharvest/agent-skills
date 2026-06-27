---
name: audience-site-brief
description: >-
  Use when a user wants a landing page and provides only a text description of
  their goal or brand — no reference site. Produces an audience strategy, page
  architecture, copy direction, and a build prompt ready for motion-web-design.
  If the user has a URL and screenshots, use site-to-build-prompt instead.
---

# Audience Site Brief

Turn a vague goal ("I want a site for X") into a complete **site strategy brief** grounded in research, personas, reference patterns, and UX principles — then output a **build prompt** ready for [motion-web-design](../motion-web-design/SKILL.md).

> **URL + screenshots?** Use [site-to-build-prompt](../site-to-build-prompt/SKILL.md) instead — it runs this pipeline with visual analysis and outputs a self-contained prompt for a powerful coding model.

This skill orchestrates child skills in sequence. Read each child skill at its phase — do not rely on memory alone.

| Phase | Child skill | Purpose |
|-------|-------------|---------|
| 2 | [audience-research](../audience-research/SKILL.md) | What the audience actually needs (pain points, barriers, language) |
| 3 | [persona-archetypes](../persona-archetypes/SKILL.md) | Who you're speaking to (grounded in research) |
| 4 | [reference-site-analysis](../reference-site-analysis/SKILL.md) | What works for similar audiences (patterns that validate) |
| 5 | [ux-methodology-process](../ux-methodology-process/SKILL.md) | Page architecture and section order |
| 6 | [ux-methodology-design](../ux-methodology-design/SKILL.md) | Visual hierarchy and interaction design |
| 7 | [ab-testing](../ab-testing/SKILL.md) | What to validate after launch |
| 8 | [visual-identity](../visual-identity/SKILL.md) | Brand personality, typography, motion vocabulary — pre-code design lock |
| 9–10 | [motion-web-design](../motion-web-design/SKILL.md) | How it looks and moves — receives design-system.md from visual-identity |

**Distinction:** [persona-archetypes](../persona-archetypes/SKILL.md) defines **human** audiences. [motion-web-design/archetypes.md](../motion-web-design/archetypes.md) defines **visual site** templates (VEX, Velorah, etc.). This skill connects them.

---

## Workflow

Copy this checklist and track progress:

```
Audience Site Brief (Full Pipeline):
- [ ] 1. Broad intake — capture goal, audience hypothesis
- [ ] 2. Research audience — pain points, barriers, language (audience-research)
- [ ] 3. Build persona — who they are (grounded in research evidence)
- [ ] 4. Analyze references — what works for this audience
- [ ] 5. Design process — page architecture, section order (ux-methodology-process)
- [ ] 6. Design optimization — visual hierarchy, interactions (ux-methodology-design)
- [ ] 7. Architect page — sections, copy direction (synthesized from phases 2–6)
- [ ] 8. Map visual archetype — motion site preset + rationale
- [ ] 8b. Visual identity — brand keywords, typography, color tokens, motion vocabulary (visual-identity)
- [ ] 9. Draft experiment backlog — ranked A/B hypotheses
- [ ] 10. Output build prompt — handoff to motion-web-design (includes design-system.md)
- [ ] 11. Confirm with user before building (unless they asked to build immediately)
```

---

## Phase 1: Broad Intake

Start with one open question, then fill gaps. Do not ask more than 5 questions total before inferring the rest.

**Opening prompt (use verbatim):**

> Describe what you're trying to achieve in your own words — the product or brand, who should care, what you want them to feel, and what action you want them to take. Don't worry about design details yet.

**Gap-fill only if missing:**

| Gap | Ask |
|-----|-----|
| Product unclear | "What are you offering — product, service, portfolio, or cause?" |
| Audience unclear | "Who is the ideal person landing on this page?" |
| Action unclear | "What is the one primary action? (book, buy, sign up, contact, explore)" |
| Context unclear | "Where does traffic come from — ads, search, referrals, direct?" |
| Constraint | "Any hard constraints — brand colors, existing copy, must-include sections?" |

**Capture as intake block:**

```markdown
## Intake
- **Goal:** [one sentence]
- **Offering:** [what it is]
- **Primary audience:** [who]
- **Desired feeling:** [emotional outcome]
- **Primary action:** [CTA goal]
- **Traffic context:** [cold/warm, channel]
- **Constraints:** [any]
```

If the user gives rich context upfront, skip redundant questions and proceed.

---

## Phase 2: Research Audience

Read [audience-research/SKILL.md](../audience-research/SKILL.md). Search real user sources for pain points, barriers, language, and decision criteria.

**Key outputs:**
- 4–6 themes of pain points with real quotes
- Barriers to entry this audience faces
- Language and terminology they use
- Trust signals that matter to them
- Objections they commonly raise

**Use for:** Grounding persona-building in evidence, not assumptions. This research informs persona psychology, messaging tone, and what objections to address on the page.

---

## Phase 3: Build Personas

Read [persona-archetypes/SKILL.md](../persona-archetypes/SKILL.md). Apply the Framework Picker and Layering Order. **Ground frameworks in research findings from Phase 2.**

**Inference rules from intake:**

| Intake signal | Start hypothesis | Site direction hint |
|---------------|------------------|---------------------|
| B2B / technical / dev | Type 5, Sage, Spectator | VEX, SynapseX |
| Luxury / premium service | Achiever, Ruler, Experiencer | SkyElite, Velorah |
| Creative / studio / art | Creator, Type 4, Experiencer | Prisma, VANGUARD |
| Nature / film / experiential | Explorer, high Openness | Organic Odyssey, Lithos |
| Finance / advisory / VC | Thinker, high C, Ruler | VEX |
| AI / dev tools | Sage, Type 5, I-RIASEC | SynapseX |
| Agency / bold brand | Hero, Rebel, Type 3 | VANGUARD |

Label inferences as **hypothesis** until validated. Pick **2–3 frameworks max** per persona.

**Output:** Primary persona card (use template from persona-archetypes) plus optional secondary (20%) and anti-persona (10%). Include:

- Core tension (want vs fear)
- Decision style and trust signals
- Messaging tone, lead-with, avoid list
- CTA style for this audience
- UX & motion implications from persona-archetypes Design & Motion Mapping table

For multi-audience conflicts, prioritize primary (70%) and note secondary accommodations — do not design for "everyone."

---

## Phase 4: Analyze Reference Sites

Read [reference-site-analysis/SKILL.md](../reference-site-analysis/SKILL.md). Find 3–5 high-signal sites serving this audience and extract UX patterns.

**Key outputs:**
- Sites validated by user reviews (4.5+ stars), market performance, or engagement
- Common patterns (section order, copy angles, visual strategies)
- Differentiation opportunities (where you can improve)
- Anti-patterns (what successful sites avoid)

**Use for:** Validating your architecture ideas against real-world success. See what sections, copy approaches, and visual styles actually resonate with your audience. Avoid cargo-culting; extract the *why*.

---

## Phase 5: UX Process Design

Read [ux-methodology-process/SKILL.md](../ux-methodology-process/SKILL.md). Determine page architecture: which sections exist, why, and in what order.

**Use laws that inform structure:**
- **Mental Model & Jakob's Law** — does the section order match what users expect?
- **Peak-End Rule** — where's the emotional high-point? Where should it sit?
- **Goal-Gradient Effect** — does momentum build toward the CTA?
- **Zeigarnik Effect** — do users see progress toward completion?
- **Miller's Law & Chunking** — are sections grouped meaningfully? (aim for 5–7 main sections)
- **Hick's Law** — does each section present ≤5 choices, or use progressive disclosure?
- **Serial Position Effect** — is the first section your strongest value prop? Last section your clearest CTA?

**Output:** Finalized page architecture with section map showing order, purpose, and disclosure levels.

**Journey map (brief):**

1. **Arrival (Hero)** — strongest value prop (Serial Position: first is remembered)
2. **Engagement** — progressive disclosure, don't overwhelm (Paradox of Active User)
3. **Confidence (Peak)** — emotional high-point (customer success, breakthrough moment)
4. **Consideration** — address objections, show options (Hick's Law: limit to 3–5 variants)
5. **Closure (Final CTA)** — clearest call-to-action (Serial Position: last is remembered)

---

## Phase 6: UX Design Optimization

Read [ux-methodology-design/SKILL.md](../ux-methodology-design/SKILL.md). Optimize how to present the architecture from Phase 5.

**Use laws that inform presentation:**
- **Von Restorff & Selective Attention** — what's the primary CTA? Make it visually distinct.
- **Fitts's Law** — button sizing and placement; make CTAs easy to hit (40–48px minimum)
- **Proximity, Similarity, Common Region** — group related elements; use spacing, borders, color
- **Cognitive Load & Working Memory** — use progressive disclosure, bullets instead of paragraphs
- **Doherty Threshold** — interactions feel instant (<400ms) or show progress
- **Aesthetic-Usability Effect** — invest in polish (typography, color, imagery, spacing)

**Output:** Design rules for visual hierarchy, button styling, form feedback, interaction responsiveness, and overall polish. These inform the motion-web-design build.

---

## Phase 7: Page Architecture & Copy Direction

Synthesize Phases 2–6 into final page structure and messaging direction. You now have:
- Research findings (pain points, language, objections)
- Persona (who they are, how they decide)
- Reference patterns (what works for this audience)
- Architecture (sections, order)
- Design rules (visual hierarchy, emphasis)

**Now finalize:**
- Exact section list and ordering
- Copy direction for each section
- Messaging tone and angles for A/B testing

**Section planner:**

| If primary action is… | Typical sections (adapt) |
|-----------------------|--------------------------|
| Book / contact | Hero → proof → how it works → FAQ/objections → CTA |
| Buy / sign up | Hero → outcome → social proof → pricing anchor → CTA |
| Explore / portfolio | Hero → statement → work/samples → about → contact |
| Trust / enterprise | Hero → logos/metrics → case study → security → demo CTA |

**Copy direction (not final copy yet):**

Use the Messaging Matrix from [persona-archetypes/synthesis.md](../persona-archetypes/synthesis.md):

```markdown
## Copy Direction
- **Headline angle:** [outcome-first / proof-first / identity-first — with rationale]
- **Subhead role:** [objection handler / outcome expander / credibility]
- **Primary CTA copy:** [specific action + risk reversal if needed]
- **Secondary CTA:** [lower commitment option for cold traffic]
- **Proof placement:** [what proof, where relative to CTA]
- **Tone:** [from persona card]
- **Avoid:** [anti-patterns from persona]
- **Nav labels:** [familiar, ≤5 items — Hick's Law]
```

**Headline framework:** Outcome-first beats feature-first (ab-testing Priority #1). Write 2–3 headline **angles** for A/B testing, not one final headline.

**Objection map:** Top 3 objections from persona → where on page each is addressed.

---

## Phase 8: Visual & Motion Composition

Read [motion-web-design/presets.md](../motion-web-design/presets.md) and [modules/README.md](../motion-web-design/modules/README.md).

**Then run [visual-identity/SKILL.md](../visual-identity/SKILL.md)** to lock the design language (brand keywords → typography → color tokens → motion vocabulary → texture → preset selection). This produces `design-system.md`, which is the required handoff artifact for motion-web-design.

Cross-reference persona → site mapping from [persona-archetypes/synthesis.md](../persona-archetypes/synthesis.md#persona--motion-site-mapping):

| Audience signals | Preset base | Module overrides to consider |
|------------------|-------------|------------------------------|
| Sage, high C, low E | VEX, SynapseX | motion.subtle, video.raw or gradient |
| Lover, Experiencer, high O | Velorah, Organic Odyssey | motion.cinematic, typography.cinematic-serif |
| Ruler, Achiever, premium | SkyElite, VANGUARD | colors.light-premium or bold-agency type |
| Creator, high O, editorial | Prisma | sections.full-editorial |
| Explorer, experiential | Organic Odyssey, Lithos | interactions.cursor-spotlight |

**Output selection with rationale:**

```markdown
## Visual Direction
- **Preset base:** [VEX | Velorah | SkyElite | ...] — from presets.md
- **Why:** [2 sentences linking persona psychology to preset choice]
- **Module overrides:** [list any modules that differ from preset — e.g. colors.accent, motion.heading_effect]
- **Page depth:** [hero-only | multi-section — ref sections module]
- **Signature interaction:** [interactions module ID or none]
```

If primary and secondary personas conflict visually, choose primary preset and note one module override for secondary (e.g., add `sections` with specs link).

---

## Phase 9: Experiment Backlog

Read [ab-testing/SKILL.md](../ab-testing/SKILL.md). Draft **3–5 pre-launch hypotheses** ranked by PIE (Potential, Importance, Ease).

Prioritize per ab-testing evidence:
1. Headline / value prop angles (not color tests)
2. CTA copy + microcopy under button
3. Social proof placement relative to hero CTA
4. Friction points (form length, commitment level)
5. Section order if multi-section

Use hypothesis template from ab-testing:

> Because [persona insight / observation], we believe [change] will increase [metric] because [reason].

**Persona-calibrated CTA tests:**

| Persona | Test variant A | Test variant B |
|---------|----------------|----------------|
| Sage / skeptical | "See how it works" | "Read the architecture" |
| Achiever / status | "Start winning" | "Join leaders who..." |
| Cold traffic | "See if we can help" | "Get a quote" |
| Premium service | "Book a consultation" | "Explore membership" |

Document as backlog — implementation comes after v1 launch unless user requests variant build.

---

## Phase 10: Build Prompt Output

Synthesize Phases 1–9 into a single **build prompt** the agent (or user) runs with motion-web-design. This is the primary deliverable.

Use [build-prompt-template.md](build-prompt-template.md) for audience/content layers, then assemble **module compose blocks** from [motion-web-design/compose-prompt.md](../motion-web-design/compose-prompt.md). Start from the chosen preset in [presets.md](../motion-web-design/presets.md); paste overrides for any module that differs.

The prompt must be self-contained: a developer agent with only motion-web-design loaded can build without re-reading this skill.

**After outputting the brief, ask:**

> I've produced the site brief and build prompt above. Should I proceed to build using the motion-web-design skill, or do you want to refine the audience/copy direction first?

If user said "build it" upfront, skip the confirmation and invoke motion-web-design immediately with the generated prompt.

---

## Quality Gate

Before delivering the brief:

- [ ] Research findings (4–6 themes) backed by real quotes, not paraphrases
- [ ] Persona grounded in research evidence + psychology frameworks (max 3 frameworks)
- [ ] Reference sites validated by user reviews/market data (not just Google rank)
- [ ] Page architecture (5–7 sections) matches persona mental model + reference patterns
- [ ] Architecture documented with section map (order, purpose, disclosure level)
- [ ] Design rules specify visual hierarchy, CTA emphasis, and interaction feedback
- [ ] Headline angles are outcome-first; at least 2 variants for testing
- [ ] Objections mapped (from research) to sections that address them
- [ ] Visual archetype choice justified by persona + reference site patterns
- [ ] CTA matches decision style (low-commit for skeptical; direct for warm)
- [ ] A/B backlog prioritizes copy/messaging over cosmetic changes
- [ ] Build prompt includes preset + module compose blocks
- [ ] Primary persona drives 70%+ of decisions; secondary noted explicitly

---

## Anti-Patterns

- **Design-first** — picking VEX because it looks cool before defining audience
- **Demographic-only** — "millennials who like tech" without psychographics
- **Framework soup** — 6+ personality systems on one persona card
- **Single headline** — no test variants when goal is conversion
- **UX law laundry list** — citing 20 laws without actionable rules
- **Ignoring traffic context** — same page for cold ads and warm referrals without note
- **Skipping build prompt** — delivering analysis without handoff artifact
- **Confusing archetypes** — mixing human Jung archetypes with visual VEX/Velorah without mapping

---

## Additional Resources

- [build-prompt-template.md](build-prompt-template.md) — Final deliverable format for motion-web-design handoff
- [persona-archetypes/synthesis.md](../persona-archetypes/synthesis.md) — Messaging matrix, persona → site mapping
- [visual-identity/SKILL.md](../visual-identity/SKILL.md) — Brand personality, typography, motion vocabulary (Phase 8b)
- [motion-web-design/archetypes.md](../motion-web-design/archetypes.md) — Persona → preset mapping
- [motion-web-design/presets.md](../motion-web-design/presets.md) — 8 visual archetypes with token bundles
- [motion-web-design/compose-prompt.md](../motion-web-design/compose-prompt.md) — Build prompt assembly template
- [ab-testing/patterns.md](../ab-testing/patterns.md) — Winning patterns by category
