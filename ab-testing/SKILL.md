---
name: ab-testing
description: >-
  Use after audience-site-brief Phase 6 (UX design optimization) to plan
  conversion experiments. Produces a prioritized test backlog using the PIE
  framework (Potential, Importance, Ease), hypothesis templates, and
  persona-calibrated CTA variants. Run before launch to identify what to
  validate first, not what to guess at.
---

# A/B Testing

Plan experiments that validate messaging and UX decisions before, during, and after launch. This skill produces a prioritized backlog, not just a list of "things to try." The distinction matters: without prioritization, teams test button colors while leaving the value prop unvalidated.

**Evidence:** 40+ years of conversion research shows that copy/messaging tests consistently outperform visual/color tests by 3–5x in average lift.

## When to Apply

- After UX design phase — you have a page architecture and design rules
- Before launch — to identify what hypotheses to validate first
- After launch with traffic — to run structured tests instead of random changes
- When stakeholders want to "just change X to see if it helps" — to redirect toward hypotheses first

## Workflow

Copy this checklist:

```
A/B Testing:
- [ ] 1. List what you believe (assumptions → hypotheses)
- [ ] 2. PIE score each hypothesis
- [ ] 3. Rank — high PIE first
- [ ] 4. Write hypothesis statement for top 5
- [ ] 5. Define success metric for each
- [ ] 6. Calculate minimum sample size
- [ ] 7. Document test backlog
```

---

## Phase 1: Priority Order

Test in this category order. Violating it wastes traffic on low-impact tests.

| Priority | Category | Why |
|----------|----------|-----|
| 1st | **Headline / value prop** | Biggest lever — if message doesn't land, nothing else matters |
| 2nd | **CTA copy + microcopy** | Directly determines click rate; high-impact, low-effort |
| 3rd | **Social proof placement** | Trust signals near CTAs consistently improve conversion |
| 4th | **Section order / content** | Structural changes (problem before proof, proof before price) |
| 5th | **Form friction** | If there's a form — number of fields, field labels, progress cues |
| Last | **Visual design** | Color, button size, images — marginal impact vs. message |

**Why this order matters:** A strong value prop with a red button beats a weak value prop with a perfectly optimized CTA. Don't test the button until you know the message lands.

---

## Phase 2: PIE Scoring

Score each hypothesis 1–10 on three dimensions:

| Dimension | Question | Example |
|-----------|----------|---------|
| **Potential** | How much improvement is possible? | Headline test: 10 (high upside). Color test: 2 (minimal) |
| **Importance** | How much traffic or value does this affect? | Hero CTA: 10 (every user). FAQ question 4: 2 (few users scroll that far) |
| **Ease** | How easy is it to implement and run? | Copy swap: 9. Backend logic change: 2 |

**PIE = (P + I + E) / 3**

High PIE (>7): Run these first. Low PIE (<5): Deprioritize or eliminate.

---

## Phase 3: Hypothesis Template

Every test needs a hypothesis written before starting. No hypothesis = no test.

```
Because [observation or persona insight],
we believe [specific change]
will [increase | decrease] [metric]
because [mechanism — why it should work].

We'll know it worked when [success metric] [improves by / increases to] [target] 
within [time period].
```

**Example:**

```
Because our primary persona (Type 3 Achiever) responds to identity-based messaging 
over feature lists (per persona research),
we believe changing the hero headline from "Zero sugar. 750mg electrolytes." (feature-led)
to "Built for athletes who read the label." (identity-led)
will increase hero CTA click-through rate
because identity language creates immediate recognition — the audience sees themselves 
in the message before they process the features.

We'll know it worked when CTA CTR increases by ≥15% over 4 weeks.
```

---

## Phase 4: Headline Testing

The highest-impact test for any landing page. Run this before testing anything else.

**Four headline angles to test:**

| Angle | Formula | Example |
|-------|---------|---------|
| **Outcome-first** | "You will [result]" | "Recover in half the time" |
| **Identity-first** | "For people who [are X]" | "Built for athletes who read the label" |
| **Proof-first** | "[Number] people have [outcome]" | "12,400 athletes switched. Here's why." |
| **Problem-first** | "Tired of [pain]?" | "Done drinking sugar water disguised as recovery?" |

**Persona calibration:**

| Persona type | Best angle | Worst angle |
|-------------|-----------|------------|
| Achiever / Hero / Type 3 | Identity-first | Proof-first (feels like conformity) |
| Sage / Type 5 | Proof-first | Identity-first (feels like manipulation) |
| Lover / Experiencer | Outcome-first | Problem-first (too negative) |
| Explorer / Type 7 | Problem-first | Proof-first (too mainstream) |
| Ruler / Achiever | Status-first variant | Problem-first |

**Test structure:** Run headline A vs headline B. Track: CTA click rate, scroll depth (does the headline make them read further?), time on page.

---

## Phase 5: CTA Testing

Second-highest impact after headlines.

**CTA copy frameworks:**

| Framework | Formula | Example |
|-----------|---------|---------|
| Action + Outcome | "[Verb] [result]" | "Start Performing" |
| Urgency | "[Action] before [consequence]" | "Get it before it sells out" |
| Risk reversal | "[Action] — [safety net]" | "Try it free for 60 days" |
| Identity CTA | "I'm ready to [be X]" | "I'm done with sugar water" |
| Low-commitment | "[Gentle action]" | "See how it works" |

**Microcopy under the button:**

This is often higher impact than the button copy itself. Test:
- Risk reversal: "No commitment. Cancel anytime."
- Social proof: "Join 12,400+ athletes"
- Urgency: "Ships in 2–3 days"
- Nothing (clean look vs. reassurance)

---

## Phase 6: Social Proof Placement

Proof near the CTA consistently outperforms proof in a dedicated "testimonials" section.

**Test order:**

1. **Inline proof** — 1 testimonial immediately above or below the primary CTA
2. **Stats near hero** — "Rated 4.8/5 by 2,400+ athletes" in hero, above fold
3. **Proof before price** — testimonials between features and pricing anchor
4. **Traditional dedicated section** — the default everyone ships

---

## Phase 7: Minimum Sample Size

Don't stop tests early. Use this as a reality check before planning a test.

**Rule of thumb:**
- Baseline conversion rate: [X]%
- Minimum detectable effect: 10–20% relative lift (don't test for less)
- Confidence: 95%

**Sample size calculator shortcut:**

| Baseline CR | Min effect you care about | Sample needed per variant |
|-------------|--------------------------|--------------------------|
| 1% | 20% lift (1.2%) | ~16,000 users |
| 2% | 20% lift (2.4%) | ~8,000 users |
| 5% | 15% lift (5.75%) | ~4,000 users |
| 10% | 10% lift (11%) | ~5,000 users |

**Practical minimum:** Run each variant for at least 2 full weeks (catches day-of-week variance). Stop at 95% confidence or after 4 weeks if inconclusive.

---

## Phase 8: Test Backlog Format

```markdown
# A/B Test Backlog: [Project Name]

## Priority Queue

### Test 1 — Headline Angle (PIE: 8.7)
**Hypothesis:** [full hypothesis statement]
**Variants:** A: [current] | B: [challenger]
**Success metric:** CTA click-through rate
**Sample needed:** [N] per variant
**Status:** Ready to run

### Test 2 — CTA Microcopy (PIE: 8.1)
**Hypothesis:** [...]
**Variants:** A: "No commitment. Cancel anytime." | B: "Join 12,400+ athletes"
**Success metric:** CTA clicks / sessions
**Sample needed:** [N] per variant
**Status:** Queue after Test 1

### Test 3 — Social Proof Placement (PIE: 7.4)
[...]

### Parking Lot (run later or never)
- Button color (lime → white outline) — PIE: 3.2 — low potential, already high contrast
- Hero image swap — PIE: 4.0 — medium potential, low ease (requires new photography)
```

---

## Quality Gate

- [ ] Tests prioritized by category (headlines first, not colors first)
- [ ] Every test has a PIE score with reasoning
- [ ] Every test has a full hypothesis statement (not just "test X vs Y")
- [ ] Success metric defined (not "see what happens")
- [ ] Sample size calculated and realistic for expected traffic
- [ ] 2-week minimum run time noted
- [ ] Backlog distinguishes "ready to run" vs "parking lot"

---

## Anti-Patterns

- **Testing button color first** — the lowest-impact category first; a signal of no hypothesis discipline
- **No success metric** — "let's see if it improves" is not testable; you'll stop whenever it feels right
- **Stopping at 80% confidence** — you'll have false positives that roll back later
- **Testing 4 things simultaneously** — interaction effects make results uninterpretable
- **Never testing the headline** — the most impactful element gets "protected" because everyone is attached to it
- **Running tests below minimum sample** — random noise looks like signal; you'll optimize for variance

---

## Additional Resources

- [patterns.md](patterns.md) — Winning patterns by category from research literature
- [audience-site-brief/SKILL.md](../audience-site-brief/SKILL.md) — Where test hypotheses are first drafted (Phase 9)
- [persona-archetypes/synthesis.md](../persona-archetypes/synthesis.md) — Persona → CTA testing direction
