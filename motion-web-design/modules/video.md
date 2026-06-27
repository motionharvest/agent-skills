# Module: Video

Video generation requires a separate Replicate integration. This module covers how to document video slots during the build so they can be filled when generation is available, and what placeholder treatment to use in the meantime.

## Video Slot Pattern

Mark every video location in the HTML with a `data-video-slot` attribute. This creates a clear handoff point for when Replicate integration is available.

```html
<!-- Video slot with gradient placeholder -->
<div class="video-slot" data-video-slot="hero-background">
  <video
    class="video-element"
    autoplay
    muted
    loop
    playsinline
    poster="[optional poster image URL — use Unsplash still frame]"
    aria-hidden="true"
  >
    <!-- src filled when Replicate video is generated -->
    <!-- Prompt documented in VIDEO_PROMPTS.md -->
  </video>
  <!-- Placeholder shown until video loads -->
  <div class="video-placeholder"></div>
</div>
```

## CSS Placeholder Treatment

```css
/* While video is not yet generated / loading */
.video-slot {
  position: relative;
  overflow: hidden;
}

.video-element {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 0.6s ease;
}

.video-element.loaded {
  opacity: 1;
}

/* Gradient placeholder (matches page dark bg) */
.video-placeholder {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    var(--dark) 0%,
    var(--dark-surface) 50%,
    var(--dark) 100%
  );
}

/* Optional: animated gradient placeholder */
.video-placeholder--animated {
  background: linear-gradient(
    90deg,
    var(--dark) 25%,
    var(--dark-surface) 50%,
    var(--dark) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

## VIDEO_PROMPTS.md

Write this file in the project root. This is the documentation for all video generation.

```markdown
# Video Generation Prompts

These slots require video generated via Replicate or similar video generation platform.
Integration requires a separate Replicate API setup — see external documentation.

---

## Slot: hero-background

**Location:** Hero section, full-bleed background overlay
**Dimensions:** 1920×1080
**Duration:** 10–15s loop, no audio
**Overlay:** Dark gradient overlay applied in CSS above the video

**Generation prompt:**
[Action description] in slow motion cinematic 4K, [lighting description], 
shot on ARRI Alexa, lens flare, shallow depth of field, [mood] energy.
Color grade: [matching brand palette]. Loop-ready, no text, no faces.

**Specific example (VANGUARD athletic brand):**
Elite trail runner in slow motion on a misty mountain path, early morning golden light,
cinematic 4K, shot on ARRI Alexa, lens flare, shallow depth of field, high-performance energy.
Color grade: desaturated with electric lime color cast on highlights. Loop-ready, no text.

---

## Slot: product-lifestyle

**Location:** Ingredients / product section
**Dimensions:** 800×600
**Duration:** 6–8s loop, no audio

**Generation prompt:**
[Product] in [environment], [motion detail — drops, condensation, pour], [lighting],
macro/medium shot, dark moody studio lighting with single key light, [brand color] accent.

---

## Slot: [other-slot]

[follow same format]
```

## JavaScript: Video Load Handler

```js
// Show video when loaded, hide placeholder
document.querySelectorAll('.video-element').forEach(video => {
  if (!video.src) return; // Skip slots without src yet

  video.addEventListener('loadeddata', () => {
    video.classList.add('loaded');
  });

  // Fallback: if video takes too long
  setTimeout(() => {
    if (video.readyState >= 3) video.classList.add('loaded');
  }, 3000);
});
```

## When Video Slots Are Required

Use a video slot when:
- The build prompt specifies "video background" in a section
- A section's visual impact would be significantly enhanced by motion (hero, premium product feature)
- The persona/preset calls for cinematic treatment (VELORAH, SKYELITE, PRISMA)

Skip video slots when:
- The hero design works with a still photograph (most VANGUARD, VEX builds)
- The project is time-constrained and Replicate integration is not planned
- Product photography is the primary visual (product images > video)
