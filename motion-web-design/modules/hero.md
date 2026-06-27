# Module: Hero

Hero section layouts and entrance animation variants. The hero sets the energy for everything below — build it last so you know what timing feels right in context.

## Layout Variants

### Full-Viewport (VANGUARD, VELORAH, SKYELITE)
```html
<section class="hero-section" data-section="hero">
  <!-- Background: image or video -->
  <div class="hero-bg">
    <img src="[unsplash-url]" alt="" aria-hidden="true" class="hero-bg-image"
         loading="eager" fetchpriority="high" width="1400" height="900" />
    <div class="hero-overlay"></div>
  </div>

  <!-- Content -->
  <div class="hero-content container">
    <p class="hero-eyebrow eyebrow">Category Label</p>
    <h1 class="hero-h1">
      <span class="line">First headline line</span>
      <span class="line">Second line</span>
      <span class="line accent">Accent line.</span>
    </h1>
    <p class="hero-sub">Supporting subheadline text here.</p>
    <div class="hero-ctas">
      <a href="#shop" class="btn-primary btn-accent hero-cta-primary">Primary CTA</a>
      <a href="#science" class="btn-ghost hero-cta-secondary">Secondary CTA</a>
    </div>
    <p class="hero-risk">Risk reversal text — no commitment required.</p>
  </div>

  <!-- Visual (product / illustration) -->
  <div class="hero-visual">
    <img src="[product-image]" alt="Product name" class="hero-product"
         loading="eager" fetchpriority="high" width="600" height="700" />
  </div>
</section>
```

```css
.hero-section {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.hero-bg-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.35;  /* Background stays dark; content reads over it */
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    var(--dark) 30%,
    transparent 100%
  );
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 680px;
}

.hero-h1 {
  font-family: var(--font-display);
  font-size: clamp(3rem, 7vw, 6rem);
  line-height: 0.95;
  letter-spacing: -0.01em;
  text-transform: uppercase;  /* VANGUARD only */
  margin-bottom: 1.5rem;
}

.hero-h1 .line { display: block; }
.hero-h1 .accent { color: var(--accent); }

.hero-visual {
  position: absolute;
  right: 0;
  bottom: 0;
  width: 45%;
  z-index: 1;
}

.hero-visual img {
  width: 100%;
  height: auto;
}
```

### Split 50/50 (VEX, LITHOS)
Content left, visual right, equal weight.

```html
<section class="hero-section hero-split">
  <div class="hero-left">
    <!-- eyebrow, h1, sub, ctas -->
  </div>
  <div class="hero-right">
    <!-- product image or data visualization -->
  </div>
</section>
```

```css
.hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
  align-items: center;
  gap: var(--space-lg);
}
```

---

## Entrance Sequence

See full implementation in SKILL.md Phase 6. Key variants:

### LIFT variant (VANGUARD, VEX, ORGANIC ODYSSEY)
```js
tl.from('.hero-h1 .line', {
  y: 70, opacity: 0, duration: 0.7, stagger: 0.12, ease: 'power3.out'
})
```

### REVEAL variant (SKYELITE, VELORAH, PRISMA)
```js
tl.from('.hero-h1 .line', {
  clipPath: 'inset(0 100% 0 0)',
  duration: 0.9, stagger: 0.18, ease: 'power3.inOut'
})
```

---

## Mobile Hero (≤767px)

```css
@media (max-width: 767px) {
  .hero-section {
    min-height: 90svh;  /* Use svh on mobile to account for browser chrome */
    padding: var(--space-xl) 0 var(--space-lg);
  }

  .hero-visual {
    position: relative;
    width: 100%;
    max-width: 400px;
    margin: var(--space-md) auto 0;
  }

  .hero-h1 {
    font-size: clamp(2.25rem, 10vw, 3.5rem);
  }
}
```
