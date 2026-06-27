# Module: Images

Unsplash integration for all photography. Free, high-quality, covers all standard content categories.

## URL Format

```
https://images.unsplash.com/photo-{PHOTO_ID}?auto=format&fit=crop&w={WIDTH}&q=80
```

**Required parameters:**
- `auto=format` — Serves WebP to browsers that support it (automatic, no code needed)
- `fit=crop` — Maintains aspect ratio while filling exact dimensions
- `w={WIDTH}` — Set to the actual CSS render width (not 2x; the CDN handles DPR)
- `q=80` — Quality/size balance; use 90 for hero images

**Optional parameters:**
- `h={HEIGHT}` — Explicit height (auto-crops)
- `crop=entropy` — Crop to highest visual information (good for faces)
- `crop=faces` — Prioritize face detection (avatars, testimonials)
- `fp-x=0.5&fp-y=0.3` — Custom focal point (0–1 range)

## HTML Patterns

### Hero image (above the fold — eager)
```html
<img
  src="https://images.unsplash.com/photo-{ID}?auto=format&fit=crop&w=1400&q=90"
  alt="[Descriptive alt text]"
  class="hero-bg-image"
  width="1400"
  height="900"
  loading="eager"
  fetchpriority="high"
/>
```

### Below-fold image (lazy)
```html
<img
  src="https://images.unsplash.com/photo-{ID}?auto=format&fit=crop&w=800&q=80"
  alt="[Descriptive alt text]"
  class="section-image"
  width="800"
  height="600"
  loading="lazy"
/>
```

### Avatar (testimonial)
```html
<img
  src="https://images.unsplash.com/photo-{ID}?auto=format&fit=crop&w=80&q=80&crop=faces"
  alt="[Name], [role]"
  class="testimonial-avatar"
  width="80"
  height="80"
  loading="lazy"
/>
```

## Search Strategy by Content Type

| Content needed | Unsplash search terms | Notes |
|---------------|----------------------|-------|
| Athlete running | `athlete trail running performance` | Horizontal orientation |
| Strength training | `gym barbell strength workout` | Dark studio lighting preferred |
| Cycling | `cyclist road bike performance race` | Action shots, speed blur |
| Recovery/wellness | `athlete recovery stretch yoga` | Calmer, softer lighting |
| Sports drink / bottle | `sports drink water bottle gym` | Product category |
| Team/group | `fitness group class training` | Social proof sections |
| Marathon | `marathon race runner city` | Crowd + individual shots |
| Female athlete | `female athlete running strength` | For gender balance in testimonials |
| Outdoor sports | `trail hiking mountain outdoor athlete` | Explorer/Organic Odyssey brands |
| Portrait (testimonial) | `portrait athlete headshot professional` | Keep small w= value |

## Performance Rules

1. **Hero image** — `loading="eager"` + `fetchpriority="high"` — this is the LCP element
2. **All other images** — `loading="lazy"` (browser handles the threshold)
3. **Always include** `width` and `height` attributes — prevents CLS (layout shift)
4. **Width** = actual CSS render width, not 2x (Unsplash CDN handles DPR)
5. **Alt text** — always descriptive ("Marathon runner on a misty trail road"), never empty for content images

## Finding Photo IDs

1. Search on unsplash.com
2. Click a photo → URL contains `/photo-{ID}`
3. Copy the full photo ID (format: 1234567890-abcdef123456)
4. Build the direct URL using the format above

**Alternatively**, use the Unsplash Source API (no API key needed for simple use):
```
https://source.unsplash.com/random/1200×800/?trail,runner,performance
```

Note: Random URLs are non-deterministic — use specific photo IDs in production so images don't change on reload.

## Placeholder Pattern (before photo IDs are sourced)

```css
/* Image placeholder while sourcing actual Unsplash photos */
.img-placeholder {
  background: linear-gradient(135deg, var(--dark-surface) 0%, var(--dark-card) 100%);
  aspect-ratio: 16 / 9;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--gray);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
```

```html
<div class="img-placeholder" role="img" aria-label="[Image description — placeholder]">
  Image: [brief content description]
</div>
```
