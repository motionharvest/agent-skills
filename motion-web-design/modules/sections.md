# Module: Sections

Content section HTML patterns, CSS conventions, and scroll reveal wiring. One section at a time: HTML → CSS → animation.

## Section Anatomy

Every content section follows this structure:

```html
<section class="[section-name]-section section" data-section="[name]">
  <div class="container">
    <!-- Eyebrow label (optional) -->
    <p class="eyebrow">[CATEGORY LABEL]</p>

    <!-- Heading -->
    <h2 class="section-h2">
      <span class="line">First line of heading</span>
      <span class="line">Second line</span>
    </h2>

    <!-- Lead paragraph (optional) -->
    <p class="section-lead">[Supporting paragraph]</p>

    <!-- Content: cards, list, table, etc. -->
    <div class="section-content">
      <!-- Section-specific content -->
    </div>
  </div>
</section>
```

## CSS Conventions

```css
/* Shared section base */
.section {
  padding: var(--space-xl) 0;
}

/* Alternating background */
.section--dark { background: var(--dark); }
.section--surface { background: var(--dark-surface); }
.section--light { background: var(--accent-dim); color: var(--dark); }

/* Eyebrow label */
.eyebrow {
  font-family: var(--font-body);
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 1rem;
}

/* Section heading */
.section-h2 {
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 4vw, 3.5rem);
  line-height: 1.05;
  margin-bottom: 1.5rem;
}

.section-h2 .line { display: block; }

/* Lead paragraph */
.section-lead {
  font-size: 1.125rem;
  line-height: 1.7;
  color: var(--gray-light);
  max-width: 680px;
  margin-bottom: 3rem;
}
```

## Card Patterns

### Standard card grid
```html
<div class="card-grid">
  <div class="card" data-hover>
    <div class="card-icon"><!-- SVG icon --></div>
    <h3 class="card-title">Card Title</h3>
    <p class="card-body">Card description text.</p>
  </div>
  <!-- Repeat -->
</div>
```

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-md);
}

.card {
  background: var(--dark-card);
  border: 1px solid var(--dark-border);
  border-radius: var(--radius-lg);
  padding: var(--space-md);
}

@media (max-width: 768px) {
  .card-grid { grid-template-columns: 1fr; }
}
```

### Ingredient card (number-prominent)
```html
<div class="ingredient-card card">
  <div class="ingredient-amount">
    <span data-count="750" data-suffix="mg">750mg</span>
  </div>
  <h3 class="ingredient-name">Sodium Citrate</h3>
  <p class="ingredient-role">Fluid regulation and muscle function</p>
</div>
```

```css
.ingredient-amount {
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 900;
  color: var(--accent);
  line-height: 1;
  margin-bottom: 0.5rem;
}
```

### Testimonial card
```html
<div class="testimonial-card card">
  <blockquote class="testimonial-quote">
    "Quote text here — specific, with outcome."
  </blockquote>
  <footer class="testimonial-author">
    <img src="[avatar]" alt="[Name], [role]" class="testimonial-avatar"
         width="48" height="48" loading="lazy" />
    <div>
      <p class="author-name">[Name]</p>
      <p class="author-role">[Sport, Achievement]</p>
    </div>
  </footer>
</div>
```

## Stats Bar Section

```html
<section class="stats-section" data-section="stats">
  <div class="container stats-grid">
    <div class="stat-item">
      <p class="stat-number" data-count="750" data-suffix="mg">750mg</p>
      <p class="stat-label">Electrolytes per serving</p>
    </div>
    <!-- 3 more stats -->
  </div>
</section>
```

```css
.stats-section {
  background: var(--accent);
  padding: var(--space-lg) 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-md);
  text-align: center;
}

.stat-number {
  font-family: var(--font-display);
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 900;
  color: var(--dark);
  line-height: 1;
}

.stat-label {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--dark);
  opacity: 0.7;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 0.5rem;
}

@media (max-width: 640px) {
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
}
```

## FAQ Section

```html
<section class="faq-section section" data-section="faq">
  <div class="container">
    <h2 class="section-h2">Common Questions</h2>
    <div class="faq-list">
      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">
          Is this safe for competition?
          <span class="faq-icon" aria-hidden="true">+</span>
        </button>
        <div class="faq-a" style="height: 0; overflow: hidden;">
          <div class="faq-a-inner">
            <p>Answer text here.</p>
          </div>
        </div>
      </div>
      <!-- More items -->
    </div>
  </div>
</section>
```

```css
.faq-item {
  border-bottom: 1px solid var(--dark-border);
}

.faq-q {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 0;
  background: none;
  border: none;
  color: var(--white);
  font-size: 1rem;
  font-weight: 500;
  text-align: left;
  cursor: pointer;
}

.faq-a-inner {
  padding: 0 0 1.5rem;
  color: var(--gray-light);
  line-height: 1.7;
}

.faq-icon {
  transition: transform 0.3s var(--ease-out);
  flex-shrink: 0;
}

.faq-item.open .faq-icon {
  transform: rotate(45deg);
}
```
