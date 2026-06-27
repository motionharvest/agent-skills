# Motion Web Design — Compose Prompt

How to assemble a self-contained build prompt that a developer agent can execute with only `motion-web-design` loaded — no prior context needed.

A build prompt is the deliverable from audience-site-brief Phase 10. It contains all decisions from research, persona, architecture, and visual identity in one document that drives the actual code build.

---

## Build Prompt Template

Copy and fill in this template. Replace `[...]` placeholders.

```markdown
# Build Prompt: [Project Name]

## Stack
Vite + GSAP + ScrollTrigger + Lenis. Vanilla JS with ES modules.
Skill: motion-web-design

## Preset
[VANGUARD | SKYELITE | VELORAH | VEX | SYNAPSEX | ORGANIC ODYSSEY | PRISMA | LITHOS]

Rationale: [1 sentence linking persona signals to this preset]

Module overrides: [list any deviations from preset defaults, or "none"]

---

## Design System (from visual-identity)

### Brand Personality
| Keyword | Visual Translation |
|---------|-------------------|
[5 rows]

### Typography
- Display: [font, weights]
- Body: [font, weights]
- Google Fonts: [import URL]

### Color Tokens
```css
:root {
  --accent-bright: [hex];
  --accent:        [hex];
  --accent-muted:  [hex];
  --accent-dim:    [hex];
  --dark:          [hex];
  --dark-surface:  [hex];
  --dark-card:     [hex];
  --dark-border:   [hex];
  --white:         [hex];
  --gray-light:    [hex];
  --gray:          [hex];
}
```

### Texture
[Grain | Gradient | None] — [1-sentence implementation note]

### Motion Vocabulary
| Name | GSAP shorthand | When |
|------|----------------|------|
| LIFT   | [shorthand] | section entrances |
| REVEAL | [shorthand] | hero H1, section H2 |
| COUNT  | [shorthand] | stats, numbers |
| PULSE  | [shorthand] | CTAs, buttons |

---

## Page Architecture

### Sections (in order)

#### 1. Nav
[Links: list — max 5 items]
[CTA: button label]

#### 2. Hero
**H1:** [exact headline]
**Subheadline:** [supporting copy]
**Primary CTA:** [label] → [action]
**Secondary CTA:** [label] → [action]
**Risk text:** [e.g., "No commitment required"]
**Visual:** [product image / illustration brief — Unsplash search terms]
**Motion:** Hero entrance sequence — see SKILL.md Phase 6

#### 3. Stats Bar
**Format:** [number with label, repeated 3–4 times]
**Numbers:** [list with units]
**Motion:** COUNT animation as bar enters viewport

#### 4. [Section name]
**Headline:** [eyebrow + H2]
**Body:** [1–2 sentence direction]
**Cards:** [number, content brief each]
**Motion:** [LIFT with stagger | alternating LIFT | none]

[Repeat for each section]

#### N. Final CTA
**H2:** [headline]
**Subheadline:** [supporting copy]
**CTA:** [label]
**Motion:** Background transitions dark→accent on scroll enter

#### Footer
[Links, copyright, social links]

---

## Copywriting Notes

**Tone:** [from persona card]
**Vocabulary to use:** [terms the audience uses]
**Vocabulary to avoid:** [terms that trigger distrust]
**Objection handling:** [top 3 objections → sections that address them]

---

## Image Sourcing (Unsplash)

[For each visual slot, list Unsplash search terms and target dimensions]

| Slot | Search terms | Dimensions |
|------|-------------|------------|
| Hero background | [terms] | 1400×900 |
| [other slots] | [terms] | [dims] |

---

## Video Slots (Replicate)

[List any video slots — will generate VIDEO_PROMPTS.md per SKILL.md Phase 10]

| Slot | Location | Brief |
|------|----------|-------|
| [name] | [section] | [1-sentence direction] |

---

## Quality Gate

Build is complete when all items in SKILL.md quality gate are checked.
```

---

## Module Compose Blocks

Reference individual module files when you need to override a specific preset default. Paste only the blocks that differ from the selected preset.

### Stack block
```
MODULE: stack
Vite + GSAP 3 + Lenis.
- GSAP plugins: ScrollTrigger
- Lenis version: latest stable
```

### Typography block (override)
```
MODULE: typography
Display font: [font name] [weights]
Body font: [font name] [weights]
Override preset default: [what differs]
```

### Colors block (override)
```
MODULE: colors
Accent: [hex] (overrides preset)
Texture: grain at 0.05 opacity (overrides preset "none")
```

### Motion block (override)
```
MODULE: motion
Intensity: electric (overrides preset "precise")
LIFT timing: 500ms power3.out
PULSE overshoot: back.out(2.5)
```

### Hero block
```
MODULE: hero
Layout: [full-viewport | split-50/50 | text-only | product-hero]
H1 split into .line spans: [yes | no]
Visual: [athlete image | product can | illustration | video-slot]
Entrance: [GSAP timeline per SKILL.md Phase 6]
```

### Images block
```
MODULE: images
Primary slot: hero-athlete — Unsplash search: "trail runner morning light"
Secondary slots: [list]
All: auto=format, fit=crop, q=80
```

### Video block
```
MODULE: video
Slot: hero-background, dimensions: 1920×1080, loop: true
Prompt direction: [athlete activity + mood + color grade]
Placeholder: dark gradient matching --dark color until video filled
```

---

## Example: VANGUARD Sports Nutrition Build Prompt

```markdown
# Build Prompt: Slurpit Zero Sugar

## Stack
Vite + GSAP + ScrollTrigger + Lenis.

## Preset
VANGUARD

Rationale: Primary persona is Hero archetype / Achiever VALS / Type 3 — VANGUARD's bold, dark, electric performance aesthetic matches exactly.

Module overrides: none

---

## Design System

### Brand Personality
| Keyword | Visual Translation |
|---------|-------------------|
| Electric | Lime accent, fast stagger, high contrast on dark |
| Earned | Grain texture, heavy type, no decorative illustration |
| Precise | Ingredient numbers as display type, no visual noise |
| Raw | 900 weight, athlete photography over renders |
| Clean | One accent, generous whitespace |

### Typography
- Display: Barlow Condensed 900 uppercase
- Body: Inter 400/500/600
- Google Fonts: [URL from Google Fonts for both]

### Color Tokens
```css
:root {
  --accent-bright: #D9FF47;
  --accent:        #C5F135;
  --accent-muted:  #8AB022;
  --accent-dim:    #E8FAB0;
  --dark:          #080C14;
  --dark-surface:  #0F1621;
  --dark-card:     #141B27;
  --dark-border:   #1E2D40;
  --white:         #FFFFFF;
  --gray-light:    #C4CFD9;
  --gray:          #8896AA;
}
```

### Texture
Grain — body::after, SVG turbulence filter, opacity 0.04, position fixed

### Motion Vocabulary
| Name | GSAP shorthand | When |
|------|----------------|------|
| LIFT | from({y:40,opacity:0},{ease:'power3.out',duration:0.5}) | sections |
| REVEAL | clipPath:'inset(0 100% 0 0)' → 'inset(0 0% 0 0)', 0.55s | headlines |
| COUNT | gsap.to({val:0},{val:target,duration:1.6}) | stats bar |
| PULSE | to(el,{scale:1.03,ease:'back.out(2.5)',duration:0.2}) | CTAs |

---

## Page Architecture

### 1. Nav
Links: Benefits, Science, Ingredients, Reviews, FAQ
CTA: Shop Now

### 2. Hero
H1: "BUILT FOR ATHLETES WHO READ THE LABEL."
Subheadline: "Zero sugar. 750mg electrolytes. NSF Certified."
Primary CTA: Start Performing → /shop
Secondary CTA: See the Science → /ingredients
Risk text: "Free shipping over $50. Cancel anytime."
Visual: Athlete photo (Unsplash: "trail runner misty morning") + 3 product cans
Motion: Full GSAP timeline per SKILL.md Phase 6

### 3. Stats Bar
Background: --accent (lime) on dark
Numbers:
- 750mg electrolytes / serving
- 0g sugar
- 45 calories
- NSF Certified

### 4. Problem Section
Eyebrow: THE STATUS QUO
H2: "Most hydration drinks are sugar delivery systems with a sports marketing budget."
Body: 2 paragraphs addressing audience pain with sugar/artificial sweetener distrust
Callout quote (large): "We read the label. You should too."
Motion: LIFT + quote REVEAL

### 5. The Science
Eyebrow: WHY IT WORKS
H2: "Three ingredients do the work. Everything else is noise."
Cards (3): Monk Fruit, Hypotonic Formula, Electrolyte Balance
Each card: Icon + title + 2-sentence description + key number
Motion: LIFT with 100ms stagger, alternate left/right

### 6. Ingredients
Background: --dark-surface
Eyebrow: WHAT'S INSIDE
H2: "Every milligram, explained."
Intro: "We publish full ingredient amounts because we have nothing to hide."
Cards (6): Sodium 750mg, Potassium 200mg, Magnesium 50mg, Monk Fruit, B6, B12
Each: Name + amount + function sentence
Motion: alternating horizontal LIFT

### 7. Social Proof
Eyebrow: ATHLETES WHO SWITCHED
Numbers row: [4.8/5 stars] [12,400+ athletes] [94% reorder rate] [NSF Certified]
Testimonials (3): Name, sport, quote (2–3 sentences), avatar
Motion: COUNT for numbers, LIFT cascade for testimonials

### 8. Flavor Shop
Eyebrow: FIND YOUR FLAVOR
H2: "Three flavors. Same formula."
Flavor cards (3): Citrus Surge, Watermelon Wave, Unflavored Pro
Each card: Can illustration/photo, name, taste note, price, "Add to Cart" CTA
Motion: LIFT + PULSE on card hover

### 9. FAQ
5 questions (accordion):
- Is this safe for competition? (NSF Certified answer)
- What makes it zero sugar? (Monk fruit explanation)
- How does it compare to Gatorade? (Direct comparison)
- When should I drink it? (Before, during, after guidance)
- Can I subscribe? (Yes, 15% off)
Motion: GSAP accordion height animation

### 10. Final CTA
Background: transitions dark→--accent on scroll
H2: "PERFORM HARDER."
Subheadline: "Your first month is risk-free."
CTA: Start Performing
Risk text: "60-day guarantee. No commitment."

### Footer
Links: About, Science, Ingredients, FAQ, Privacy, Terms
Social: Instagram, TikTok
Copyright: © 2025 Slurpit

---

## Image Sourcing (Unsplash)

| Slot | Search | Dimensions |
|------|--------|------------|
| Hero athlete | "trail runner morning mist performance" | 1400×900 |
| Testimonial 1 avatar | "marathon runner portrait" | 80×80 |
| Testimonial 2 avatar | "cyclist female athlete" | 80×80 |
| Testimonial 3 avatar | "gym strength training man" | 80×80 |

## Video Slots

| Slot | Location | Brief |
|------|----------|-------|
| hero-bg | Hero section overlay | Athletic motion, dark cinematic, lime color cast |
```

---

## Notes on Prompt Completeness

A good build prompt passes this check:

- [ ] Preset named + rationale
- [ ] All color tokens as CSS variables
- [ ] Typography specified (font names + import URL)
- [ ] Texture choice made
- [ ] All 4 motion vocabulary moves with GSAP shorthand
- [ ] Every section listed with headline, copy direction, and motion note
- [ ] Unsplash search terms for all image slots
- [ ] Video slots documented (even if not yet generated)
- [ ] No "TBD" or "figure this out later" items
