# Module: Nav

Sticky navigation with scroll-state transition and mobile menu pattern.

## HTML

```html
<nav class="nav" role="navigation" aria-label="Main navigation">
  <div class="nav-inner container">
    <!-- Logo -->
    <a href="/" class="nav-logo" aria-label="[Brand] home">
      <img src="/src/assets/logo.svg" alt="[Brand]" width="120" height="32" />
      <!-- OR: text logo -->
      <span class="nav-logo-text">[Brand]</span>
    </a>

    <!-- Desktop links -->
    <ul class="nav-links" role="list">
      <li><a href="#benefits" class="nav-link">Benefits</a></li>
      <li><a href="#science" class="nav-link">Science</a></li>
      <li><a href="#reviews" class="nav-link">Reviews</a></li>
      <li><a href="#faq" class="nav-link">FAQ</a></li>
    </ul>

    <!-- CTA -->
    <a href="#shop" class="btn-primary btn-sm nav-cta">Shop Now</a>

    <!-- Mobile toggle -->
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">
      <span class="nav-toggle-bar"></span>
      <span class="nav-toggle-bar"></span>
      <span class="nav-toggle-bar"></span>
    </button>
  </div>

  <!-- Mobile menu (hidden by default) -->
  <div class="nav-mobile" aria-hidden="true">
    <ul class="nav-mobile-links" role="list">
      <li><a href="#benefits" class="nav-mobile-link">Benefits</a></li>
      <li><a href="#science" class="nav-mobile-link">Science</a></li>
      <li><a href="#reviews" class="nav-mobile-link">Reviews</a></li>
      <li><a href="#faq" class="nav-mobile-link">FAQ</a></li>
    </ul>
    <a href="#shop" class="btn-primary nav-mobile-cta">Shop Now</a>
  </div>
</nav>
```

## CSS

```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 900;
  transition: background 0.3s var(--ease-out), box-shadow 0.3s var(--ease-out);
}

/* Transparent default */
.nav { background: transparent; }

/* Solid on scroll */
.nav.nav--scrolled {
  background: rgba(8, 12, 20, 0.95);   /* --dark with alpha */
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);   /* Safari */
  box-shadow: 0 1px 0 var(--dark-border);
}

.nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
}

.nav-logo-text {
  font-family: var(--font-display);
  font-weight: 900;
  font-size: 1.5rem;
  letter-spacing: -0.02em;
  color: var(--white);
  text-decoration: none;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: var(--space-md);
  margin: 0;
  padding: 0;
}

.nav-link {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--gray-light);
  text-decoration: none;
  transition: color var(--dur-fast) var(--ease-out);
}

.nav-link:hover { color: var(--white); }

/* Hide mobile elements on desktop */
.nav-toggle { display: none; }
.nav-mobile { display: none; }

@media (max-width: 767px) {
  .nav-links, .nav-cta { display: none; }
  .nav-toggle {
    display: flex;
    flex-direction: column;
    gap: 5px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
  }
  .nav-toggle-bar {
    width: 24px;
    height: 2px;
    background: var(--white);
    transition: transform var(--dur-mid) var(--ease-out);
  }
}

/* Mobile menu */
.nav-mobile {
  position: fixed;
  inset: 0;
  background: var(--dark);
  z-index: 800;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-md);
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--dur-slow) var(--ease-out);
}

.nav-mobile.open {
  opacity: 1;
  pointer-events: auto;
}

.nav-mobile-link {
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 900;
  color: var(--white);
  text-decoration: none;
  text-transform: uppercase;
}
```

## JavaScript (micro.js)

```js
// In initMicro() → initNav()
function initNav() {
  const nav = document.querySelector('.nav');
  const toggle = document.querySelector('.nav-toggle');
  const mobileMenu = document.querySelector('.nav-mobile');

  // Scroll state
  ScrollTrigger.create({
    start: 'top+=72 top',
    onEnter: () => nav.classList.add('nav--scrolled'),
    onLeaveBack: () => nav.classList.remove('nav--scrolled')
  });

  // Mobile toggle
  if (toggle && mobileMenu) {
    toggle.addEventListener('click', () => {
      const isOpen = mobileMenu.classList.contains('open');
      mobileMenu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', !isOpen);
      mobileMenu.setAttribute('aria-hidden', isOpen);
      document.body.style.overflow = isOpen ? '' : 'hidden';
    });

    // Close on link click
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        mobileMenu.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      });
    });
  }

  // Smooth scroll for anchor links (via Lenis)
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const target = document.querySelector(link.getAttribute('href'));
      if (target && lenis) {
        e.preventDefault();
        lenis.scrollTo(target, { offset: -72 }); // -72px for nav height
      }
    });
  });
}
```

Note: `lenis` must be accessible in scope (export from main.js or use a module-level variable).
