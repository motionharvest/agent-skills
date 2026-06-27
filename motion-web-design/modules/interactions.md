# Module: Interactions

Micro-interactions beyond buttons: card hover, FAQ accordion, cursor effects, and scroll-reactive elements.

## Card Hover (PULSE variant)

Cards that rise on hover add tactile depth without being distracting.

```js
// In initMicro()
function initCards() {
  document.querySelectorAll('.card[data-hover]').forEach(card => {
    card.addEventListener('mouseenter', () => {
      gsap.to(card, { y: -8, duration: 0.3, ease: 'back.out(1.4)' });
    });
    card.addEventListener('mouseleave', () => {
      gsap.to(card, { y: 0, duration: 0.3, ease: 'power2.out' });
    });
  });
}
```

**Flavor card variant (rotation + lift):**
```js
document.querySelectorAll('.flavor-card').forEach(card => {
  card.addEventListener('mouseenter', () => {
    gsap.to(card, { y: -12, rotate: -1, duration: 0.35, ease: 'back.out(1.6)' });
  });
  card.addEventListener('mouseleave', () => {
    gsap.to(card, { y: 0, rotate: 0, duration: 0.3, ease: 'power2.out' });
  });
});
```

## FAQ Accordion

Full GSAP accordion (no `max-height` CSS hack — it's choppy).

```js
function initFAQ() {
  document.querySelectorAll('.faq-item').forEach(item => {
    const btn = item.querySelector('.faq-q');
    const answer = item.querySelector('.faq-a');
    if (!btn || !answer) return;

    btn.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');

      // Close all open items
      document.querySelectorAll('.faq-item.open').forEach(openItem => {
        openItem.classList.remove('open');
        openItem.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
        gsap.to(openItem.querySelector('.faq-a'), {
          height: 0, duration: 0.3, ease: 'power2.inOut', overwrite: true
        });
      });

      // Open clicked item (if it was closed)
      if (!isOpen) {
        item.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');

        // Measure height first
        gsap.set(answer, { height: 'auto' });
        const fullHeight = answer.offsetHeight;
        gsap.fromTo(answer,
          { height: 0 },
          { height: fullHeight, duration: 0.4, ease: 'power2.out', overwrite: true }
        );
      }
    });
  });
}
```

## Image Parallax on Card Hover

For premium cards with background images (VELORAH, SKYELITE presets).

```js
document.querySelectorAll('.media-card').forEach(card => {
  const img = card.querySelector('.media-card-img');
  if (!img) return;

  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width - 0.5) * 10; // ±5deg
    const y = ((e.clientY - rect.top) / rect.height - 0.5) * 10;

    gsap.to(img, { x: x * -1.5, y: y * -1.5, duration: 0.4, ease: 'power2.out' });
  });

  card.addEventListener('mouseleave', () => {
    gsap.to(img, { x: 0, y: 0, duration: 0.5, ease: 'power2.out' });
  });
});
```

## Scroll Progress Indicator

For long pages — thin progress bar at top of viewport.

```html
<div class="scroll-progress" aria-hidden="true"></div>
```

```css
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 2px;
  background: var(--accent);
  transform-origin: left;
  z-index: 1000;
}
```

```js
gsap.to('.scroll-progress', {
  scaleX: 1,
  ease: 'none',
  scrollTrigger: {
    start: 'top top',
    end: 'bottom bottom',
    scrub: 0.3,
  }
});
gsap.set('.scroll-progress', { scaleX: 0 });
```

## Cursor Spotlight (ORGANIC ODYSSEY preset)

Hero section where cursor creates a spotlight glow effect.

```html
<div class="cursor-spotlight" aria-hidden="true"></div>
```

```css
.cursor-spotlight {
  position: fixed;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(143, 196, 74, 0.12) 0%,  /* --accent with alpha */
    transparent 70%
  );
  pointer-events: none;
  z-index: 1;
  transform: translate(-50%, -50%);
  transition: opacity 0.3s ease;
  opacity: 0;
}
```

```js
const spotlight = document.querySelector('.cursor-spotlight');
if (spotlight) {
  document.addEventListener('mousemove', (e) => {
    gsap.to(spotlight, {
      x: e.clientX, y: e.clientY,
      duration: 0.6, ease: 'power2.out'
    });
    spotlight.style.opacity = '1';
  });

  document.addEventListener('mouseleave', () => {
    spotlight.style.opacity = '0';
  });
}
```

## Number Reveal Animation

For large feature numbers (stats, credentials) — alternative to COUNT that uses clip-path.

```js
// Clip-path reveal for a number that's already the right value (no counting)
gsap.from('.feature-number', {
  clipPath: 'inset(0 100% 0 0)',
  duration: 0.8,
  ease: 'power3.inOut',
  scrollTrigger: { trigger: '.feature-number', start: 'top 80%' }
});
```

## Horizontal Scroll Section (PRISMA preset)

For editorial/creative presets with horizontal scroll panels.

```html
<section class="horizontal-scroll-section" data-section="work">
  <div class="horizontal-scroll-track">
    <div class="panel">Panel 1</div>
    <div class="panel">Panel 2</div>
    <div class="panel">Panel 3</div>
  </div>
</section>
```

```js
const track = document.querySelector('.horizontal-scroll-track');
if (track) {
  const panels = track.querySelectorAll('.panel');
  const totalWidth = (panels.length - 1) * 100; // vw

  gsap.to(track, {
    x: () => -(track.scrollWidth - window.innerWidth),
    ease: 'none',
    scrollTrigger: {
      trigger: '.horizontal-scroll-section',
      start: 'top top',
      end: () => `+=${track.scrollWidth - window.innerWidth}`,
      scrub: 1,
      pin: true,
      anticipatePin: 1
    }
  });
}
```
