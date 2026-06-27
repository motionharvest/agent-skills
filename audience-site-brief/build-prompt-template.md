# Build Prompt Template

Copy and fill this template as the Phase 7 deliverable. Assemble module blocks via [motion-web-design/compose-prompt.md](../motion-web-design/compose-prompt.md).

---

```markdown
# Motion Site Build — [Brand/Project Name]

> **Instructions:** Build using motion-web-design. Content below + module compose blocks = complete spec.
> Preset base: [VEX | Velorah | SkyElite | ...] — see presets.md for defaults, override below.

---

## Content

brand: [Brand Name]
goal: [one sentence]
primary_action: [CTA goal]
traffic_context: [cold/warm, channel]

hero:
  headline: "[v1 — outcome-first]"
  headline_v2: "[A/B alternate]"
  subhead: "[objection handler / outcome expander]"
  label: "[optional uppercase label]"
  tag_card: "[optional]"

nav:
  brand: "[Brand]"
  links: [Link1, Link2, Link3, Link4]

assets:
  video_slots:
    - slot_id: hero
      placeholder: /assets/videos/hero.mp4
      treatment: gradient
      generation_prompt: |
        [Full prompt for video generation model — see video-prompts.md]
  image_slots: {}

---

## Audience Summary

**[Archetype Name]** — [one-line essence]
- Core tension: [want vs fear]
- Tone: [voice]
- Avoid: [anti-patterns]
- CTA style: [from persona]

---

## UX Requirements

| Law | Rule |
|-----|------|
| [Law 1] | [implementation] |
| [Law 2] | [implementation] |

---

## Preset & Overrides

preset: [skyelite]
overrides:
  - colors.accent: "#202A36"
  - motion.heading_effect: fade-rise
  # only list modules that differ from preset

---

## Modules

# Copy compose blocks from motion-web-design/modules/*.md
# Required: stack, typography, colors, hero-layout, nav, motion, cta, mobile-menu, responsive, quality-gate
# Conditional: video, glass, sections, interactions
# Start from preset bundle in presets.md; replace blocks for overridden modules

[PASTE module compose blocks here — see compose-prompt.md template]

---

## Page Sections (if multi-section)

| # | Section | Content notes |
|---|---------|---------------|
| 1 | Hero | [from content above] |
| 2 | [Section] | [purpose + content direction] |

---

## A/B Test Backlog

| Priority | Hypothesis | Metric |
|----------|------------|--------|
| 1 | Because [insight], [change] will [metric] | [metric] |

---

## Constraints

- [brand colors, assets, out-of-scope items]
```

---

## Assembly Steps

1. Fill **Content** and **Audience Summary** from Phases 1–4
2. Pick **preset** from Phase 5 visual direction
3. Open [presets.md](../motion-web-design/presets.md) — copy full module bundle for that preset
4. Apply **overrides** for any module that differs from preset defaults
5. Paste all compose blocks under **Modules**
6. Paste all compose blocks under **Modules** — include full `video.slots` with generation prompts
7. Add **sections** table if `sections.depth` > hero-only
8. Deliverable includes **VIDEO_PROMPTS.md** at project root with all generation prompts

## Example (Abbreviated)

```markdown
# Motion Site Build — SkyElite Aviation

## Content
hero:
  headline: "Premium."
  headline_v2: "Your time deserves the sky."
  subhead: "Your dedication deserves recognition."

## Preset & Overrides
preset: skyelite
overrides: []    # use preset defaults

## Modules
# (paste skyelite bundle from presets.md + content labels into cta module)
```

Full prompts include all required module compose blocks.
