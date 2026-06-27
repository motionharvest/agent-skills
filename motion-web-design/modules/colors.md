# Module: Colors

Full token system, derivation method, texture implementations, and semantic naming conventions.

## Token Derivation Method

Start from two seeds — one accent + one base dark — and derive the full system:

```
Seeds:
  accent:  [source hex — the primary brand color]
  base:    [darkest page background]

Derived tokens (systematic derivation):

Accent scale:
  {accent}-bright:  Lighten accent 15% (hover states, glow highlights)
  {accent}:         Source color (CTAs, primary accent)
  {accent}-muted:   Darken accent 20% (secondary text on light bg)
  {accent}-dim:     Mix: 10% accent + 90% white (badge bg, light tints)

Dark surface scale:
  dark:           Base (page background)
  dark-surface:   Lighten 6% (alternate sections)
  dark-card:      Lighten 10% from surface (elevated cards)
  dark-border:    Lighten 15% (dividers, subtle borders)

Neutral scale:
  white:          #FFFFFF
  gray-light:     70–75% lightness — body text on dark
  gray:           50–55% lightness — secondary text, labels
```

## VANGUARD Token Set (reference implementation)

```css
:root {
  /* Lime accent scale */
  --accent-bright: #D9FF47;
  --accent:        #C5F135;
  --accent-muted:  #8AB022;
  --accent-dim:    #E8FAB0;

  /* Dark surface scale */
  --dark:          #080C14;
  --dark-surface:  #0F1621;
  --dark-card:     #141B27;
  --dark-border:   #1E2D40;

  /* Neutrals */
  --white:         #FFFFFF;
  --gray-light:    #C4CFD9;
  --gray:          #8896AA;

  /* RGB values for opacity variants */
  --accent-rgb: 197, 241, 53;
  --dark-rgb:   8, 12, 20;
}
```

## Semantic Usage

| Token | Semantic purpose |
|-------|-----------------|
| `--accent` | Primary CTA, active state, eyebrow text, accent text |
| `--accent-bright` | Hover state, glow highlights |
| `--accent-muted` | Text on accent-colored backgrounds |
| `--accent-dim` | Tinted section backgrounds, badge fills |
| `--dark` | Page base background |
| `--dark-surface` | Alternate sections (every other section) |
| `--dark-card` | Card backgrounds, elevated surfaces |
| `--dark-border` | 1px borders, dividers |
| `--white` | Headlines, strong emphasis text |
| `--gray-light` | Body copy, secondary content |
| `--gray` | Labels, captions, placeholder text |

## Texture Implementations

### Grain overlay (most common — VANGUARD, ORGANIC ODYSSEY)

```css
/* src/styles/base.css */
body::after {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  opacity: 0.04;  /* 3–5% range; 4% is usually right */
  pointer-events: none;
  z-index: 9998;
}
```

### Gradient surface (SKYELITE, VEX)

```css
/* Applied per-section, not globally */
.section--surface {
  background: linear-gradient(
    160deg,
    var(--dark-surface) 0%,
    color-mix(in oklch, var(--dark-surface), var(--accent) 3%) 100%
  );
}
```

### Radial glow accent (hero sections)

```css
/* Glow behind hero visual / product */
.hero-glow {
  position: absolute;
  width: 600px;
  height: 600px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(var(--accent-rgb), 0.15) 0%,
    transparent 70%
  );
  pointer-events: none;
  transform: translate(-50%, -50%);
}
```

## Dark → Light Section Transition

For ingredient sections or social proof on a lighter background:

```css
.section--tinted {
  background: var(--accent-dim);
  color: var(--dark);
}

.section--tinted .section-h2 { color: var(--dark); }
.section--tinted .eyebrow { color: var(--accent-muted); }
.section--tinted p { color: color-mix(in oklch, var(--dark), white 30%); }
```

## Dynamic Color Variables (RGB for opacity)

Anywhere you need `rgba()` variants:

```css
:root {
  /* Add RGB variants for common colors */
  --accent-rgb:    197, 241, 53;  /* --accent as r,g,b */
  --dark-rgb:      8, 12, 20;
  --white-rgb:     255, 255, 255;
}

/* Usage */
.card:hover {
  box-shadow: 0 20px 60px rgba(var(--dark-rgb), 0.6);
}

.glow {
  box-shadow: 0 0 40px rgba(var(--accent-rgb), 0.4);
}
```
