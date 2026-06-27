# Motion Web Design — Modules

Individual module specs for use with compose-prompt.md. Start from the selected preset in presets.md. Only reference modules that **differ** from preset defaults.

## Module Index

| Module | File | Purpose |
|--------|------|---------|
| Stack | [stack.md](stack.md) | Vite project scaffold, package.json, Lenis+GSAP setup |
| Typography | [typography.md](typography.md) | Type scale, Google Fonts, CSS variables |
| Colors | [colors.md](colors.md) | Token system, texture options |
| Motion | [motion.md](motion.md) | GSAP patterns, motion vocabulary implementation |
| Hero | [hero.md](hero.md) | Hero layouts, entrance sequence variants |
| Nav | [nav.md](nav.md) | Sticky nav, scroll state, mobile menu |
| CTA | [cta.md](cta.md) | Button styles, PULSE micro-interaction |
| Sections | [sections.md](sections.md) | Content section patterns, scroll reveal |
| Interactions | [interactions.md](interactions.md) | Cards, FAQ, accent interactions |
| Images | [images.md](images.md) | Unsplash integration, responsive images |
| Video | [video.md](video.md) | Video slots, Replicate documentation |
| Responsive | [responsive.md](responsive.md) | Breakpoints, mobile animation handling |
| Quality Gate | [quality-gate.md](quality-gate.md) | Build verification checklist |

## How to Use

1. Select a preset from [../presets.md](../presets.md)
2. Start from preset defaults — most values are already set
3. For each section of your build prompt that differs from the preset, paste the relevant module block with your overrides
4. Modules are composable — stack them in any order in the build prompt
