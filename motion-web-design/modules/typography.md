# Module: Typography

Type scale system, Google Fonts setup, and CSS variables. Apply from design-system.md values.

## CSS Variables

```css
/* src/styles/tokens.css — typography section */
:root {
  /* Font families */
  --font-display: '[Display Font]', system-ui, sans-serif;
  --font-body:    '[Body Font]', system-ui, sans-serif;
  --font-mono:    'IBM Plex Mono', monospace;  /* SynapseX/VEX presets */

  /* Type scale (fluid — adapts with viewport) */
  --text-display: clamp(3rem, 7vw, 6rem);     /* Hero H1 */
  --text-h1:      clamp(2.25rem, 5vw, 4rem);  /* Section headlines */
  --text-h2:      clamp(1.75rem, 3.5vw, 2.75rem);
  --text-h3:      clamp(1.1rem, 2vw, 1.5rem);
  --text-body:    1rem;                        /* 16px — body copy */
  --text-sm:      0.875rem;                    /* 14px — labels, captions */
  --text-xs:      0.75rem;                     /* 12px — microcopy, badges */
  --text-eyebrow: 0.7rem;                      /* 11px — eyebrow labels */

  /* Line heights */
  --lh-tight:   0.95;   /* Display type */
  --lh-heading: 1.1;    /* H2, H3 */
  --lh-body:    1.75;   /* Body paragraphs */
  --lh-relaxed: 1.9;    /* Longer reads */

  /* Letter spacing */
  --ls-tight:   -0.02em;   /* Condensed display type */
  --ls-normal:  0;          /* Body */
  --ls-wide:    0.08em;     /* Labels */
  --ls-wider:   0.12em;     /* Eyebrow */
}
```

## Google Fonts Import (index.html)

```html
<!-- Preconnect for performance -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

<!-- Example: Barlow Condensed + Inter (VANGUARD) -->
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
```

**Common combinations by preset:**

| Preset | Google Fonts URL fragment |
|--------|--------------------------|
| VANGUARD | `Barlow+Condensed:wght@700;900&Inter:wght@400;500;600` |
| SKYELITE | `Cormorant+Garamond:ital,wght@1,700&DM+Sans:wght@400;500` |
| VELORAH | `Playfair+Display:ital,wght@1,700;1,900&Plus+Jakarta+Sans:wght@400;500` |
| VEX | `Space+Grotesk:wght@400;500;700&Inter:wght@400;500` |
| SYNAPSEX | `IBM+Plex+Mono:wght@400;700&Inter:wght@400;500` |
| ORGANIC ODYSSEY | `Barlow+Semi+Condensed:wght@600;800&DM+Sans:wght@400;500` |
| PRISMA | `Syne:wght@700;800&Plus+Jakarta+Sans:wght@400;500` |
| LITHOS | `Instrument+Serif:ital,wght@0,400;1,400&Instrument+Sans:wght@400;500` |

## Typography CSS

```css
/* src/styles/typography.css */

/* Base */
body {
  font-family: var(--font-body);
  font-size: var(--text-body);
  line-height: var(--lh-body);
  color: var(--gray-light);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Display type (hero) */
.hero-h1 {
  font-family: var(--font-display);
  font-size: var(--text-display);
  line-height: var(--lh-tight);
  letter-spacing: var(--ls-tight);
  color: var(--white);
  text-transform: uppercase;  /* VANGUARD only — remove for other presets */
}

/* Section headings */
.section-h2 {
  font-family: var(--font-display);
  font-size: var(--text-h1);
  line-height: var(--lh-heading);
  letter-spacing: var(--ls-tight);
  color: var(--white);
}

/* Subsection heading */
.section-h3, .card-title {
  font-family: var(--font-body);
  font-size: var(--text-h3);
  font-weight: 600;
  line-height: var(--lh-heading);
  color: var(--white);
}

/* Eyebrow label */
.eyebrow {
  font-family: var(--font-body);
  font-size: var(--text-eyebrow);
  font-weight: 600;
  letter-spacing: var(--ls-wider);
  text-transform: uppercase;
  color: var(--accent);
}

/* Body copy */
p {
  font-size: var(--text-body);
  line-height: var(--lh-body);
  color: var(--gray-light);
}

/* Accent text */
.accent { color: var(--accent); }
.accent-muted { color: var(--accent-muted); }

/* Large stat numbers */
.stat-number, .ingredient-amount {
  font-family: var(--font-display);
  font-weight: 900;
  line-height: 1;
  color: var(--accent);
}
```

## Accessible Font Loading

Prevent FOUT (flash of unstyled text) with `font-display: swap`:

```css
/* The Google Fonts `display=swap` parameter handles this automatically */
/* Manual @font-face: */
@font-face {
  font-family: 'DisplayFont';
  src: url('/fonts/display.woff2') format('woff2');
  font-weight: 900;
  font-display: swap;  /* Show fallback until font loads */
}
```
