# Module: Quality Gate

Complete verification before calling the build done. Run this top-to-bottom at the end of every motion-web-design session.

## Animation Quality

- [ ] **Hero entrance** — Record a screen capture. Step through at 1/4 speed. Each hero element should appear distinctly, with a gap between eyebrow → headline → sub → CTA → visual. No simultaneous reveals.
- [ ] **Stagger is visible but not slow** — Scroll a card grid at normal pace. The cascade should feel energized, not mechanical. If it feels slow, reduce stagger by 15ms.
- [ ] **COUNT animations fire correctly** — Scroll past the stats section at normal pace. Numbers should animate. Scroll back up quickly and scroll down again — they should re-animate if `once: true` is NOT set, or fire only once if it is.
- [ ] **FAQ accordion uses GSAP** — Open each FAQ item. Height should animate smoothly. If it jumps, the `max-height` CSS hack was used instead of GSAP — fix it with the micro.js pattern.
- [ ] **PULSE on CTAs** — Hover every primary CTA. Entry (scale up), exit (scale back), mousedown (squish), mouseup (bounce). All four states should work.
- [ ] **Nav scroll state** — Scroll 60px down. Nav should change state (solid bg + backdrop-filter). Scroll back to top — it should return to transparent.
- [ ] **Lenis vs. native scroll** — Scroll down with mouse wheel and touch (if testing mobile). Lenis should feel smooth, not jarring. No double-scroll or stutter.
- [ ] **Parallax hero visual** — Scroll slowly through the hero. The visual should move at a different speed than the content (parallax effect confirms depth separation).
- [ ] **Section color transition** — Scroll into the final CTA section. Background color should transition smoothly (dark → accent). The `scrub` value is correct if it follows your scroll speed.

## Visual Quality

- [ ] **Grain texture visible** — Look at a dark section at 100% zoom. Subtle noise should be visible. If the page looks completely flat/matte, the grain CSS is not applying.
- [ ] **Typography hierarchy** — Hero headline looks significantly different from section H2, which looks different from body copy. If all weights feel similar, increase display font weight or size.
- [ ] **Accent color usage** — Count accent color instances. If accent appears more than 4–5 times above the fold, it's overused. Accent = signal; overuse = noise.
- [ ] **Spacing consistency** — Check section padding. Each section should have equivalent vertical breathing room. Sections that feel "cramped" need more padding.
- [ ] **Dark card borders visible** — On dark-on-dark card layouts, check that `var(--dark-border)` is visible. If cards disappear into the background, increase border opacity.

## Performance

- [ ] **Lighthouse: LCP ≤2.5s** — Run `npm run build && npm run preview`, then Lighthouse in Chrome. LCP (Largest Contentful Paint) must be ≤2.5s. If failing, check hero image: it should have `loading="eager"` and `fetchpriority="high"`.
- [ ] **Lighthouse: CLS ≤0.1** — Cumulative Layout Shift. Fails if images don't have explicit `width` and `height` attributes. Add them.
- [ ] **Lighthouse: TBT ≤200ms** — Total Blocking Time. Fails if JS is blocking the main thread. GSAP animations should not run until DOMContentLoaded.
- [ ] **Bundle size** — `npm run build` output. JS bundle should be <120KB total. If oversized, check for accidentally importing all of GSAP instead of named plugins.
- [ ] **Images: lazy loading below fold** — Open DevTools → Network → Images. Page load should only request the hero image immediately. Section images should load as you scroll.

## Accessibility

- [ ] **`prefers-reduced-motion` respected** — Add `@media (prefers-reduced-motion: reduce)` to DevTools. All animations should be disabled or instant.
- [ ] **Alt text on all content images** — Product images, testimonial avatars, and hero images should have descriptive alt text. Decorative images should have `alt=""`.
- [ ] **Focus visible on all interactive elements** — Tab through the page. Every link, button, and FAQ toggle should show a visible focus ring (not just the browser default).
- [ ] **Color contrast** — Body text on dark backgrounds: check with DevTools accessibility panel. WCAG AA requires 4.5:1 for normal text.

## Cross-Browser

- [ ] **Chrome** — Primary dev browser; should work.
- [ ] **Safari (macOS)** — Test `backdrop-filter: blur()` — Safari has quirks. Test sticky nav. Test GSAP parallax (no GPU compositing differences).
- [ ] **Firefox** — `backdrop-filter` requires `-webkit-` prefix in some versions. Check nav blur.
- [ ] **Mobile (iOS Safari, 375px)** — Scroll feel (Lenis on iOS), hero sizing (`100svh` not `100vh`), tap targets ≥44×44px.
- [ ] **Mobile (Android Chrome, 430px)** — Check reduced motion preference respecting.

## Content

- [ ] **Every section has correct copy** — No placeholder text ("Lorem ipsum"), no "[INSERT NAME]" tokens.
- [ ] **Unsplash images display correctly** — All `<img>` tags with Unsplash URLs load. Check in a fresh private browsing window (no cache).
- [ ] **Video slots documented** — `VIDEO_PROMPTS.md` exists. Every `data-video-slot` attribute in HTML has a corresponding entry.
- [ ] **Nav links work** — All nav links scroll to correct sections (via Lenis `scrollTo` or anchor links).
- [ ] **CTA links point to real targets** — No `href="#"` on production CTAs.

## Sign-Off

Build is complete when all items above are checked. If any item cannot be met, document the gap in a `KNOWN_ISSUES.md` file in the project root.
