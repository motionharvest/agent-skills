# Motion Web Design — Presets

Eight visual archetypes for landing pages. Each preset defines default color tokens, typography usage, motion intensity, and signature interactions. Overrides for individual modules are listed per preset.

Select a preset based on the **persona → preset mapping** in [archetypes.md](archetypes.md). Start from preset defaults; override only modules that differ.

---

## VANGUARD

**For:** Bold performance brands, sports/fitness, athletic identity, agency-style presentations.
**Persona signals:** Hero (Jung), Achiever/Experiencer (VALS), Type 3 (Enneagram), high Conscientiousness.
**Reference:** Done Drinks, Grenade, GO180 — dark performance aesthetic with electric accent.

```yaml
preset: vanguard

colors:
  accent-bright:  "#D9FF47"
  accent:         "#C5F135"
  accent-muted:   "#8AB022"
  accent-dim:     "#E8FAB0"
  dark:           "#080C14"
  dark-surface:   "#0F1621"
  dark-card:      "#141B27"
  dark-border:    "#1E2D40"
  white:          "#FFFFFF"
  gray-light:     "#C4CFD9"
  gray:           "#8896AA"

typography:
  display: "Barlow Condensed 900"  # or substitute: Anton, Big Shoulders Display
  body: "Inter 400/500/600"
  h1-transform: uppercase
  h1-tracking: "-0.01em"

motion:
  intensity: electric          # Fast, high-energy
  lift-duration: 500ms
  lift-ease: power3.out
  reveal-duration: 550ms
  pulse-overshoot: "back.out(2.5)"
  stagger-cards: 80ms
  stagger-lines: 120ms

texture: grain                 # 4% opacity grain overlay on body

signature-interaction: none    # Clean, no cursor effects — let motion carry
```

---

## SKYELITE

**For:** Luxury status, premium consumer goods, financial services, aviation/automotive.
**Persona signals:** Ruler (Jung), Achiever (VALS), Type 3/8 (Enneagram), high resources.
**Reference:** Premium spirits brands, high-end automotive sites, exclusive membership platforms.

```yaml
preset: skyelite

colors:
  accent-bright:  "#F5F0E8"
  accent:         "#C9A96E"    # warm gold
  accent-muted:   "#A07840"
  accent-dim:     "#F5EDD9"
  dark:           "#0A0907"
  dark-surface:   "#131109"
  dark-card:      "#1A1710"
  dark-border:    "#2A2520"
  white:          "#FDFAF4"
  gray-light:     "#C8C2B8"
  gray:           "#857E74"

typography:
  display: "Cormorant Garamond 700i"   # Italic serif for display — heritage
  body: "DM Sans 400/500"
  h1-transform: none
  h1-tracking: "-0.02em"

motion:
  intensity: luxury             # Slow, deliberate, weighted
  lift-duration: 900ms
  lift-ease: power1.out
  reveal-duration: 1100ms
  pulse-overshoot: "back.out(1.2)"
  stagger-cards: 180ms
  stagger-lines: 200ms

texture: gradient               # Warm gradient surface on dark sections

signature-interaction: cursor-expand   # Cursor enlarges to circle on links
```

---

## VELORAH

**For:** Experiential brands, premium D2C, wellness, beauty, food & beverage (premium tier).
**Persona signals:** Lover/Experiencer (Jung/VALS), high Openness, Type 7 (Enneagram).
**Reference:** Royal Beverage, premium supplement brands with cinematic treatment.

```yaml
preset: velorah

colors:
  accent-bright:  "#FFDDD5"
  accent:         "#F4A08A"    # warm coral
  accent-muted:   "#C06848"
  accent-dim:     "#FFF0EC"
  dark:           "#0D0905"
  dark-surface:   "#161009"
  dark-card:      "#1E1610"
  dark-border:    "#2E2018"
  white:          "#FEFAF8"
  gray-light:     "#D8C8C0"
  gray:           "#8A7870"

typography:
  display: "Playfair Display 900i"  # Bold italic serif for display
  body: "Plus Jakarta Sans 400/500"
  h1-transform: none
  h1-tracking: "-0.02em"

motion:
  intensity: cinematic
  lift-duration: 800ms
  lift-ease: power2.out
  reveal-duration: 1000ms
  pulse-overshoot: "back.out(1.5)"
  stagger-cards: 140ms
  stagger-lines: 160ms

texture: textured-gradient      # Warm gradient + subtle grain

signature-interaction: parallax-hero   # Product image parallaxes on scroll
```

---

## VEX

**For:** Technical products, developer tools, B2B SaaS, security, data platforms.
**Persona signals:** Sage (Jung), Type 5 (Enneagram), high Conscientiousness + low Extraversion.
**Reference:** Linear, Vercel, Stripe — dark technical minimal with precise motion.

```yaml
preset: vex

colors:
  accent-bright:  "#A0B8FF"
  accent:         "#6B8CFF"    # electric blue
  accent-muted:   "#3A5ACC"
  accent-dim:     "#D0DCFF"
  dark:           "#09090D"
  dark-surface:   "#111118"
  dark-card:      "#18181F"
  dark-border:    "#26262E"
  white:          "#FAFAFA"
  gray-light:     "#C0C0D0"
  gray:           "#787888"

typography:
  display: "Space Grotesk 700"
  body: "Inter 400/500"
  h1-transform: none
  h1-tracking: "-0.015em"

motion:
  intensity: precise
  lift-duration: 650ms
  lift-ease: power2.out
  reveal-duration: 750ms
  pulse-overshoot: "back.out(1.4)"
  stagger-cards: 60ms
  stagger-lines: 90ms

texture: none                   # Clean/flat — depth through spacing only

signature-interaction: none
```

---

## SYNAPSEX

**For:** AI tools, machine learning products, developer infrastructure, data visualization.
**Persona signals:** Sage (Jung), high C + high I-RIASEC, tech-forward, Spectator behavior.
**Reference:** AI lab landing pages, infrastructure-as-code tools.

```yaml
preset: synapsex

colors:
  accent-bright:  "#C4F5E0"
  accent:         "#7FFFB8"    # terminal green
  accent-muted:   "#3ACC7A"
  accent-dim:     "#D8FFE8"
  dark:           "#050B07"
  dark-surface:   "#0A1208"
  dark-card:      "#0F1C0F"
  dark-border:    "#1A2E1A"
  white:          "#F0FFF4"
  gray-light:     "#A0C8A0"
  gray:           "#5A7860"

typography:
  display: "IBM Plex Mono 700"   # Monospace for technical credibility
  body: "Inter 400/500"
  h1-transform: none
  h1-tracking: "-0.01em"

motion:
  intensity: precise
  lift-duration: 600ms
  lift-ease: power2.out
  reveal-duration: 700ms
  pulse-overshoot: "back.out(1.3)"
  stagger-cards: 50ms
  stagger-lines: 80ms

texture: scanline               # Subtle horizontal scanline on hero only

signature-interaction: data-trace   # Animated lines connecting data points in hero
```

---

## ORGANIC ODYSSEY

**For:** Wellness, outdoor/adventure, sustainability, natural food/beverage, travel.
**Persona signals:** Explorer (Jung), high Openness, Maker/Experiencer (VALS), nature-connected.
**Reference:** Trail running brands, natural supplement companies, eco-tourism.

```yaml
preset: organic-odyssey

colors:
  accent-bright:  "#D4F5A0"
  accent:         "#8FC44A"    # natural green
  accent-muted:   "#5A8830"
  accent-dim:     "#EAF7CC"
  dark:           "#0A0D08"
  dark-surface:   "#121508"
  dark-card:      "#181E0A"
  dark-border:    "#26300A"
  white:          "#F8FAF4"
  gray-light:     "#B8C8A0"
  gray:           "#6A7A50"

typography:
  display: "Barlow SemiCondensed 800"  # Approachable, not aggressive
  body: "DM Sans 400/500"
  h1-transform: none
  h1-tracking: "-0.01em"

motion:
  intensity: organic             # Slightly irregular, natural feel
  lift-duration: 700ms
  lift-ease: power2.inOut
  reveal-duration: 850ms
  pulse-overshoot: "back.out(1.4)"
  stagger-cards: 120ms
  stagger-lines: 140ms

texture: grain                  # Grain feels natural, handmade

signature-interaction: cursor-spotlight   # Spotlight follows cursor in hero
```

---

## PRISMA

**For:** Creative studios, editorial brands, design agencies, fashion, art direction.
**Persona signals:** Creator (Jung), Type 4 (Enneagram), high Openness, Experiencer (VALS).
**Reference:** Design agency portfolios, editorial publications, fashion brands.

```yaml
preset: prisma

colors:
  accent-bright:  "#FF80E8"
  accent:         "#CC40C0"    # editorial magenta — or define per project
  accent-muted:   "#8A1C88"
  accent-dim:     "#FFCCF5"
  dark:           "#0A0508"
  dark-surface:   "#130A10"
  dark-card:      "#1C0F1A"
  dark-border:    "#2E1828"
  white:          "#FEFAFF"
  gray-light:     "#C8A8C0"
  gray:           "#887088"

typography:
  display: "Syne 800"          # Geometric, editorial weight
  body: "Plus Jakarta Sans 400/500"
  h1-transform: none
  h1-tracking: "-0.025em"

motion:
  intensity: editorial          # Deliberate, dramatic pauses
  lift-duration: 750ms
  lift-ease: power3.inOut
  reveal-duration: 900ms
  pulse-overshoot: "back.out(1.6)"
  stagger-cards: 150ms
  stagger-lines: 180ms

texture: none                   # Clean; let color do the work

signature-interaction: full-editorial   # Horizontal scroll sections or bold layout shifts
```

---

## LITHOS

**For:** Architecture, finance, advisory, minimalist consumer brands, high-design furniture.
**Persona signals:** Thinker (VALS), high C + low E, Type 1 (Enneagram), Ruler (subtle).
**Reference:** Architectural firms, high-end advisory, premium furniture brands.

```yaml
preset: lithos

colors:
  accent-bright:  "#808080"
  accent:         "#3D3D3D"    # charcoal — accent is texture/spacing not color
  accent-muted:   "#1A1A1A"
  accent-dim:     "#F0F0F0"
  dark:           "#FAFAFA"    # LIGHT theme — lithos is white/stone
  dark-surface:   "#F2F2F2"
  dark-card:      "#FFFFFF"
  dark-border:    "#E0E0E0"
  white:          "#FAFAFA"
  gray-light:     "#3D3D3D"   # text color on light bg
  gray:           "#6A6A6A"

typography:
  display: "Instrument Serif 400"   # Thin, precise, architectural
  body: "Instrument Sans 400/500"
  h1-transform: none
  h1-tracking: "0.02em"        # slightly open tracking — refined

motion:
  intensity: minimal
  lift-duration: 1000ms
  lift-ease: power1.out
  reveal-duration: 1200ms
  pulse-overshoot: "none"      # Linear hover, no overshoot
  stagger-cards: 200ms
  stagger-lines: 240ms

texture: none

signature-interaction: none
```

---

## Overriding Presets

Use module overrides to deviate from a preset default. Only specify modules that differ — unspecified modules inherit preset values.

```yaml
# Example: VANGUARD with luxury-level motion timing
preset: vanguard
overrides:
  motion.lift-duration: 700ms     # Slower than default 500ms
  motion.pulse-overshoot: "back.out(1.8)"
  colors.accent: "#FFAA00"        # Orange instead of lime
```

See [compose-prompt.md](compose-prompt.md) for how to assemble these into a build prompt.
