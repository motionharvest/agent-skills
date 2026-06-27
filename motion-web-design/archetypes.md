# Motion Web Design — Archetypes

Maps human persona signals (from persona-archetypes) to visual site presets (from presets.md). Use this after visual-identity has run its preset selection phase.

**Process:**
1. Identify the primary persona's dominant signals (Jung archetype, VALS segment, Enneagram type)
2. Match to a preset row
3. Confirm with visual-identity keyword list (does the preset vocabulary match?)
4. List any module overrides for secondary persona accommodation

---

## Persona → Preset Mapping

| Audience signals | Primary preset | Secondary accommodation |
|-----------------|----------------|------------------------|
| Hero, Achiever VALS, Type 3, sports/fitness | **VANGUARD** | None needed — primary audience fully served |
| Ruler, Achiever/Experiencer, premium consumer | **SKYELITE** | Add `sections.testimonials` with more polish |
| Lover, Experiencer VALS, Type 7, premium B2C | **VELORAH** | None |
| Sage, Type 5, I-RIASEC, dev tools, B2B SaaS | **VEX** | Add `sections.case-study` for Achiever buyers |
| Sage, tech-forward, AI/ML products | **SYNAPSEX** | VEX fallback if SYNAPSEX feels too niche |
| Explorer, high Openness, outdoor/wellness | **ORGANIC ODYSSEY** | Add VANGUARD motion intensity if athletic |
| Creator, Type 4, Experiencer, editorial | **PRISMA** | Subdue motion if secondary audience is Sage |
| Thinker, high C, advisory/architecture/finance | **LITHOS** | None |

---

## Signal Priority Order

When signals conflict, use this priority:

1. **Jung archetype** — strongest indicator of brand story direction
2. **VALS segment** — indicates resource level and aspiration axis
3. **Enneagram type** — refines emotional register and trust style
4. **Industry category** — override anything above if category norms are very strong (e.g., fintech almost always needs LITHOS or VEX regardless of persona)

---

## Multi-Audience Conflicts

When primary (70%) and secondary (20%) personas map to incompatible presets:

| Conflict | Resolution |
|----------|-----------|
| VANGUARD + VEX | Use VANGUARD preset; add ingredient transparency / data table sections (serves Sage secondary) |
| VELORAH + LITHOS | Use VELORAH; reduce motion intensity by 20%; add clean whitespace sections |
| PRISMA + SKYELITE | Use SKYELITE; use editorial typography override; add `sections.full-editorial` module |
| SYNAPSEX + ORGANIC ODYSSEY | These audiences rarely co-exist; revisit the persona work |

**Rule:** Design for the primary persona (70%); accommodate the secondary through one module override, not a whole different preset.

---

## Category-Level Overrides

Some industries have strong category norms that override persona mapping:

| Category | Default preset override | Why |
|----------|------------------------|-----|
| Sports nutrition / performance | **VANGUARD** | Category aesthetic expectation is dark + electric |
| Fintech / investment | **LITHOS or VEX** | Trust is built through restraint |
| Luxury fashion/beauty | **VELORAH or SKYELITE** | Expectation of premium visual register |
| Developer tools / infrastructure | **VEX or SYNAPSEX** | Developer audience distrusts "marketing" aesthetics |
| Natural / organic food | **ORGANIC ODYSSEY** | Category visual language overrides persona |
| Creative agency portfolio | **PRISMA** | Portfolio work must express creative range |

---

## Quick-Reference Cheat Sheet

```
Who is the audience?         → Preset

Athletes / performance        → VANGUARD
Luxury buyers                 → SKYELITE
Premium experience seekers    → VELORAH
Developers / technical B2B    → VEX
AI / ML / data products       → SYNAPSEX
Outdoor / wellness / nature   → ORGANIC ODYSSEY
Creative / editorial          → PRISMA
Finance / architecture        → LITHOS
```

---

## Validation Check

Before confirming a preset, verify:

- [ ] The chosen preset's color palette matches the brand personality keywords (from visual-identity)
- [ ] The motion intensity matches the keyword list (VANGUARD + "delicate" is a contradiction)
- [ ] The typography style fits the audience's decision style (Sage audiences distrust decorative serifs)
- [ ] The texture choice aligns with the brand's authenticity signals
- [ ] A secondary persona user landing on this page would not feel excluded

---

## Preset Details

See [presets.md](presets.md) for full color token bundles, typography defaults, motion timing, and texture decisions for each preset.
