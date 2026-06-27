# Module: Motion

GSAP patterns implementing the 4 motion vocabulary moves (LIFT, REVEAL, COUNT, PULSE) plus Lenis scroll setup. These patterns are referenced throughout SKILL.md.

## Motion Vocabulary: LIFT

Element rises from y+40 with fade. Used for all section entrances.

```js
// Basic LIFT (single element)
gsap.from(el, { y: 40, opacity: 0, duration: 0.6, ease: 'power3.out' });

// LIFT with ScrollTrigger
gsap.from(el, {
  y: 40, opacity: 0, duration: 0.6, ease: 'power3.out',
  scrollTrigger: { trigger: el, start: 'top 75%' }
});

// LIFT cascade (cards, 80ms stagger)
gsap.from('.card', {
  y: 40, opacity: 0, duration: 0.6, ease: 'power3.out',
  stagger: 0.08,
  scrollTrigger: { trigger: '.card-grid', start: 'top 75%' }
});

// LIFT alternating left/right (ingredients layout)
document.querySelectorAll('.card').forEach((card, i) => {
  gsap.from(card, {
    x: i % 2 === 0 ? -30 : 30, y: 20, opacity: 0,
    duration: 0.55, ease: 'power2.out',
    scrollTrigger: { trigger: card, start: 'top 80%' },
    delay: i * 0.06
  });
});
```

**Timing by preset:**
| Preset | duration | ease | y |
|--------|----------|------|---|
| VANGUARD | 0.5s | power3.out | 40 |
| SKYELITE | 0.9s | power1.out | 60 |
| VELORAH | 0.8s | power2.out | 50 |
| VEX | 0.65s | power2.out | 35 |
| ORGANIC ODYSSEY | 0.7s | power2.inOut | 40 |

---

## Motion Vocabulary: REVEAL

Text unmasks left→right via clip-path. For hero headlines and section H2.

```js
// REVEAL — clip-path animation
gsap.from('.hero-h1 .line', {
  clipPath: 'inset(0 100% 0 0)',
  duration: 0.7,
  stagger: 0.15,
  ease: 'power3.inOut',
  scrollTrigger: { trigger: '.hero-h1', start: 'top 80%' }
});
```

**HTML pattern (required for REVEAL — overflow hidden wrapper):**
```html
<h2 class="section-h2">
  <span class="reveal-wrap">
    <span class="line">First headline line</span>
  </span>
  <span class="reveal-wrap">
    <span class="line">Second headline line</span>
  </span>
</h2>
```

```css
.reveal-wrap {
  display: block;
  overflow: hidden;
}
```

**Alternative: y-translate reveal (simpler, works without wrapping):**
```js
gsap.from('.hero-h1 .line', {
  y: 70, opacity: 0, duration: 0.7, stagger: 0.12, ease: 'power3.out'
});
```

---

## Motion Vocabulary: COUNT

Numbers animate from 0 to target value as they enter the viewport. Used in stats bars and social proof.

```js
// src/animations/sections.js — call once in initSections()
function initCounters() {
  document.querySelectorAll('[data-count]').forEach(el => {
    const target = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    const decimals = parseInt(el.dataset.decimals || '0');

    ScrollTrigger.create({
      trigger: el,
      start: 'top 85%',
      once: true,
      onEnter: () => {
        const obj = { val: 0 };
        gsap.to(obj, {
          val: target,
          duration: 1.6,
          ease: 'power2.out',
          onUpdate() { el.textContent = prefix + obj.val.toFixed(decimals) + suffix; }
        });
      }
    });
  });
}
```

**HTML usage:**
```html
<!-- Integer (750mg) -->
<span data-count="750" data-suffix="mg">750mg</span>

<!-- Decimal (4.8 stars) -->
<span data-count="4.8" data-decimals="1" data-suffix=" stars">4.8 stars</span>

<!-- Large number with prefix (12,400+ athletes) -->
<span data-count="12400" data-suffix="+" class="stat-number">12,400+</span>
```

---

## Motion Vocabulary: PULSE

Scale + glow on hover for CTAs. Spring easing creates tactile, physical feedback.

```js
// In initMicro() — applied to all .btn-primary
document.querySelectorAll('.btn-primary, .btn-accent').forEach(btn => {
  btn.addEventListener('mouseenter', () => {
    gsap.to(btn, { scale: 1.03, duration: 0.2, ease: 'back.out(1.7)' });
  });
  btn.addEventListener('mouseleave', () => {
    gsap.to(btn, { scale: 1, duration: 0.2, ease: 'power2.out' });
  });
  btn.addEventListener('mousedown', () => {
    gsap.to(btn, { scale: 0.97, duration: 0.08, ease: 'power3.in' });
  });
  btn.addEventListener('mouseup', () => {
    gsap.to(btn, { scale: 1.02, duration: 0.15, ease: 'back.out(2)' });
  });
});
```

**PULSE overshoot by preset:**
| Preset | mouseenter overshoot | scale |
|--------|---------------------|-------|
| VANGUARD | back.out(2.5) | 1.04 |
| SKYELITE | back.out(1.2) | 1.02 |
| VELORAH | back.out(1.5) | 1.03 |
| VEX | back.out(1.4) | 1.02 |

**CSS glow (optional for Electric brands):**
```css
.btn-primary {
  transition: box-shadow 0.2s var(--ease-out);
}
.btn-primary:hover {
  box-shadow: 0 8px 30px rgba(var(--accent-rgb), 0.4);
}
```

---

## Parallax Scroll

Subtle depth on hero visual — creates foreground/background separation.

```js
// Hero visual parallaxes at half scroll speed
gsap.to('.hero-visual', {
  y: -60,
  ease: 'none',
  scrollTrigger: {
    trigger: '.hero-section',
    start: 'top top',
    end: 'bottom top',
    scrub: 1.5    // Smooth lag behind scroll
  }
});

// Background element moves slower (deeper)
gsap.to('.hero-bg', {
  y: -30,
  ease: 'none',
  scrollTrigger: {
    trigger: '.hero-section',
    start: 'top top',
    end: 'bottom top',
    scrub: 2
  }
});
```

---

## Section Color Transitions (scrub)

For final CTA sections that change color on scroll.

```js
gsap.to('[data-section="final-cta"]', {
  backgroundColor: 'var(--accent)',
  color: 'var(--dark)',
  ease: 'none',
  scrollTrigger: {
    trigger: '[data-section="final-cta"]',
    start: 'top 80%',
    end: 'top 20%',
    scrub: 1
  }
});
```

---

## Reduced Motion (mandatory)

```js
// Check before initializing any animations
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // Kill all ScrollTriggers, show elements immediately
  gsap.set('[data-animate]', { opacity: 1, y: 0, x: 0, clipPath: 'none' });
  return; // Skip animation initialization
}
```
