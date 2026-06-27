# Module: Responsive

Breakpoints, mobile typography, animation handling, and layout adaptation.

## Breakpoint System

```css
/* src/styles/tokens.css — add to :root */
:root {
  --bp-sm:  480px;   /* Large phones */
  --bp-md:  768px;   /* Tablets, landscape phones */
  --bp-lg:  1024px;  /* Small laptops */
  --bp-xl:  1280px;  /* Desktop */
  --bp-2xl: 1536px;  /* Large desktop */
}
```

**Media query usage (mobile-first):**
```css
/* Base: mobile */
.hero-h1 { font-size: 2.5rem; }

/* Tablet and up */
@media (min-width: 768px) {
  .hero-h1 { font-size: 4rem; }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .hero-h1 { font-size: clamp(3rem, 6vw, 5.5rem); }
}
```

## Fluid Typography (clamp)

Use `clamp()` for display type that should scale with viewport:

```css
/* Hero headline */
.hero-h1 { font-size: clamp(2.25rem, 7vw, 6rem); }

/* Section H2 */
.section-h2 { font-size: clamp(1.75rem, 4vw, 3.5rem); }

/* H3 (cards, subheadings) */
.card-title { font-size: clamp(1.1rem, 2vw, 1.5rem); }

/* Eyebrow labels */
.eyebrow { font-size: clamp(0.65rem, 1vw, 0.75rem); }
```

## Layout Adaptation

### Grid collapse (4-col → 2-col → 1-col)
```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-md);
}

@media (max-width: 1024px) {
  .card-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .card-grid { grid-template-columns: 1fr; }
}
```

### Hero adaptation (stacked on mobile)
```css
@media (max-width: 767px) {
  .hero-section {
    min-height: 90svh;  /* svh accounts for mobile browser chrome */
    flex-direction: column;
    justify-content: flex-end;
    padding-bottom: var(--space-xl);
  }

  .hero-visual {
    position: relative;
    width: 100%;
    max-width: 320px;
    margin: 0 auto var(--space-md);
    order: -1; /* Visual above content on mobile */
  }
}
```

### Container adaptation
```css
.container {
  width: 90%;
  max-width: var(--max-width);
  margin: 0 auto;
}

@media (max-width: 768px) {
  .container { width: 92%; }
}
```

## Mobile Animation Handling

Complex GSAP ScrollTrigger animations on low-end Android devices drop frames. Simplify or disable on mobile.

```js
// src/animations/sections.js — wrap all GSAP init
const isMobile = window.innerWidth < 768;
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion || isMobile) {
  // Reveal all animated elements immediately
  gsap.set('[data-animate]', { opacity: 1, y: 0, x: 0, clipPath: 'none' });
  // Disable ScrollTrigger globally
  ScrollTrigger.disable();
  return;
}

// Full animation init runs only on desktop + motion preference
initHero();
initSections();
```

**Alternative: simplified mobile animations (CSS-only)**

Instead of disabling entirely, use CSS transitions for mobile:
```css
/* Mobile: simple CSS fade-in instead of GSAP */
@media (max-width: 767px) {
  .card, .section-h2, .eyebrow {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }

  .card.visible, .section-h2.visible, .eyebrow.visible {
    opacity: 1;
    transform: none;
  }
}
```

```js
// Simple IntersectionObserver for mobile (replaces GSAP on mobile)
if (isMobile) {
  const observer = new IntersectionObserver(
    (entries) => entries.forEach(e => {
      if (e.isIntersecting) e.target.classList.add('visible');
    }),
    { threshold: 0.2 }
  );
  document.querySelectorAll('.card, .section-h2, .eyebrow').forEach(el => {
    observer.observe(el);
  });
}
```

## Mobile Viewport Height

Use `svh` (small viewport height) for hero sections on mobile — avoids the browser chrome collapsing issue:

```css
.hero-section {
  min-height: 100vh;                   /* Desktop fallback */
  min-height: 100svh;                  /* Modern mobile — excludes browser chrome */
}
```

## Touch Targets

Per WCAG and Fitts's Law — minimum 44×44px for all interactive elements:

```css
.btn-primary, .btn-ghost, .nav-link, .faq-q {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 24px;  /* Ensures touch target size */
}
```

## Testing Breakpoints

Test at these widths before calling the build complete:
- 375px — iPhone SE / small phone
- 430px — iPhone Pro Max
- 768px — iPad portrait
- 1024px — iPad landscape / small laptop
- 1280px — Standard desktop
- 1440px — Wide desktop (most common Awwwards preview size)
