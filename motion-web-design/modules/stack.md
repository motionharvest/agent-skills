# Module: Stack

Vite + GSAP + Lenis project setup. Use this for all new builds.

## Scaffold Commands

```bash
npm create vite@latest . -- --template vanilla
npm install gsap @studio-freight/lenis
```

## package.json (minimal)

```json
{
  "name": "[project-name]",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "gsap": "^3.12.0",
    "@studio-freight/lenis": "^1.0.0"
  },
  "devDependencies": {
    "vite": "^5.0.0"
  }
}
```

## vite.config.js

```js
import { defineConfig } from 'vite';

export default defineConfig({
  base: './',
  build: {
    outDir: 'dist',
    assetsInlineLimit: 4096,
  }
});
```

## index.html (boilerplate)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>[Page Title]</title>

  <!-- Google Fonts (from design-system.md) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="[GOOGLE_FONTS_URL]" rel="stylesheet" />

  <!-- CSS imports -->
  <link rel="stylesheet" href="/src/styles/tokens.css" />
  <link rel="stylesheet" href="/src/styles/base.css" />
  <link rel="stylesheet" href="/src/styles/typography.css" />
  <link rel="stylesheet" href="/src/styles/layout.css" />
  <!-- Component styles imported per-section -->
</head>
<body>
  <!-- Sections go here -->
  <script type="module" src="/src/main.js"></script>
</body>
</html>
```

## src/main.js (boilerplate)

```js
import Lenis from '@studio-freight/lenis';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

import { initHero } from './animations/hero.js';
import { initSections } from './animations/sections.js';
import { initMicro } from './animations/micro.js';

gsap.registerPlugin(ScrollTrigger);

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smooth: true,
});

lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => { lenis.raf(time * 1000); });
gsap.ticker.lagSmoothing(0);

window.addEventListener('DOMContentLoaded', () => {
  initHero();
  initSections();
  initMicro();
});
```

## Bundle Size Target

- Target: <120KB JS total after `npm run build`
- GSAP core + ScrollTrigger: ~60KB gzipped
- Lenis: ~8KB gzipped
- Application code: <50KB target
