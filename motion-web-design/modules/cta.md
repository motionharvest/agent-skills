# Module: CTA

Button styles, PULSE micro-interaction, and CTA best practices.

## Button HTML

```html
<!-- Primary: filled accent — most important CTA on page -->
<a href="#shop" class="btn-primary btn-accent">Start Performing</a>

<!-- Ghost: outline only — secondary action -->
<a href="#science" class="btn-ghost">See the Science</a>

<!-- Text link — lowest commitment -->
<a href="#ingredients" class="btn-text">Read the ingredients →</a>

<!-- Small variant — nav CTA -->
<a href="#shop" class="btn-primary btn-accent btn-sm">Shop Now</a>
```

## CSS

```css
/* Shared base */
.btn-primary, .btn-ghost, .btn-text {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  text-decoration: none;
  font-family: var(--font-body);
  font-weight: 600;
  font-size: 0.9375rem;  /* 15px */
  letter-spacing: 0.01em;
  border-radius: var(--radius);
  cursor: pointer;
  transition: box-shadow var(--dur-mid) var(--ease-out);
  white-space: nowrap;
  min-height: 48px;  /* Fitts's Law — minimum touch target */
  padding: 12px 28px;
}

/* Filled accent button */
.btn-accent {
  background: var(--accent);
  color: var(--dark);
  border: 2px solid transparent;
}

.btn-accent:hover {
  background: var(--accent-bright);
  /* Box shadow glow for electric presets */
  box-shadow: 0 8px 30px rgba(197, 241, 53, 0.3);
}

/* Ghost / outline button */
.btn-ghost {
  background: transparent;
  color: var(--white);
  border: 2px solid var(--dark-border);
}

.btn-ghost:hover {
  border-color: var(--white);
  background: rgba(255,255,255,0.05);
}

/* Text link button */
.btn-text {
  background: transparent;
  color: var(--accent);
  border: none;
  padding: 12px 4px;
  font-weight: 500;
}

.btn-text:hover { color: var(--accent-bright); }

/* Small variant */
.btn-sm {
  font-size: 0.8125rem;
  min-height: 40px;
  padding: 10px 20px;
}
```

## GSAP PULSE (from micro.js)

```js
function initButtons() {
  // Primary CTA buttons
  document.querySelectorAll('.btn-primary').forEach(btn => {
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
}
```

## Microcopy Pattern

Always pair the primary CTA with risk-reduction microcopy directly below:

```html
<div class="cta-group">
  <a href="#shop" class="btn-primary btn-accent">Start Performing</a>
  <p class="cta-microcopy">60-day guarantee · Free shipping over $50</p>
</div>
```

```css
.cta-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.75rem;
}

.cta-microcopy {
  font-size: 0.8125rem;
  color: var(--gray);
  line-height: 1.4;
}
```

## CTA Placement Rules

- **Hero** — Primary CTA + ghost CTA + risk microcopy, above the fold
- **Post-proof** — Repeat primary CTA immediately after testimonials (most visitors convert here)
- **Final CTA section** — Primary CTA only; context is "decision time"
- **Nav** — Small primary CTA in header (always visible on scroll)
- **Never** — Two identical primary CTAs side by side (creates choice paralysis)

## Focus State (accessibility)

```css
.btn-primary:focus-visible,
.btn-ghost:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}
```
