---
name: ux-methodology-design
description: >-
  Use after page architecture is finalized. Applies laws of UX that optimize
  presentation: visual hierarchy, interaction design, accessibility, and
  performance. Shapes HOW to display existing content for maximum clarity,
  usability, and delight — not WHAT content exists.
---

# UX Methodology: Design

Optimize *how* you present information through visual hierarchy, interaction design, and performance. These laws ensure users can actually use what you've built.

**Distinction:** [ux-methodology-process](../ux-methodology-process/SKILL.md) determines *what sections and order*. This skill optimizes *how to design them*. Together they make both the structure and presentation work.

## When to Apply

- After page architecture is set (sections, order, content decided)
- Creating visual hierarchy and emphasis
- Designing interactions (buttons, forms, animations)
- Reviewing existing design for usability issues
- Optimizing accessibility and performance
- Balancing aesthetics with usability

## Workflow

Copy this checklist:

```
UX Design Optimization:
- [ ] 1. Visual hierarchy (Von Restorff, Selective Attention)
- [ ] 2. Grouping & spacing (Law of Proximity, Common Region, Similarity)
- [ ] 3. CTA targeting & placement (Fitts's, Serial Position)
- [ ] 4. Response time (Doherty)
- [ ] 5. Cognitive load reduction (Cognitive Load, Working Memory)
- [ ] 6. Feedback & input handling (Postel's, Doherty)
- [ ] 7. Simplification (Occam's, Tesler's)
- [ ] 8. Polish & confidence (Aesthetic-Usability)
- [ ] 9. Audit & iterate
```

---

## Design Laws Reference

### Visual Emphasis & Hierarchy

**Von Restorff Effect** — The distinctive item stands out and is remembered.
- **Use for:** Deciding what to emphasize (primary CTA, key value prop)
- **Application:** "Make the primary button distinctive: contrast color, size, or position. Don't emphasize everything."
- **In this phase:** Shapes button styling, color choices, where emphasis goes

**Selective Attention** — Users filter to goal-relevant stimuli.
- **Use for:** Guiding attention deliberately; preventing distraction
- **Application:** "Use color, size, whitespace, and motion to guide to the CTA. Avoid competing elements."
- **In this phase:** Determines visual hierarchy, reduces visual noise, guides eye flow

**Cognitive Load** — Users have limited mental resources for interfaces.
- **Use for:** Simplifying what's visible at once
- **Application:** "Don't show 20 options at once. Use progressive disclosure, defaults, and grouping to reduce mental load."
- **In this phase:** May hide secondary options, use collapsible sections, simplify copy

### Visual Grouping (Gestalt)

**Law of Proximity** — Nearby objects are perceived as related.
- **Use for:** Spacing to show relationships
- **Application:** "Group related controls close together; space unrelated items farther apart. Spacing communicates meaning."
- **In this phase:** Determines margins, padding, section spacing

**Law of Similarity** — Similar elements read as a group.
- **Use for:** Consistent visual treatment for related items
- **Application:** "All buttons look the same; all testimonials look the same. Don't vary style arbitrarily."
- **In this phase:** Shapes component design consistency

**Law of Common Region** — Elements sharing a boundary group together.
- **Use for:** Borders, cards, backgrounds to show relationships
- **Application:** "Put related form fields in a card. Put a feature list in a bordered box. Boundaries = grouping."
- **In this phase:** Determines card usage, borders, backgrounds

**Law of Uniform Connectedness** — Visual connectors bind elements.
- **Use for:** Lines, frames, color to show relationships
- **Application:** "Draw a line around form fields or connect list items with consistent styling to show they belong together."
- **In this phase:** Shapes connector lines, frames, color usage

### Interaction & Performance

**Fitts's Law** — Acquisition time depends on target size and distance.
- **Use for:** Button sizing, CTA placement, spacing
- **Application:** "Large buttons, lots of padding. Mobile CTAs: 48x48px minimum. Place primary CTA where it's easy to reach."
- **In this phase:** Shapes button sizing, touch-target spacing, CTA placement

**Doherty Threshold** — Productivity peaks when neither user nor system waits (~400ms).
- **Use for:** Responsiveness and perceived performance
- **Application:** "Button clicks should feel instant. Long waits need progress indicators. Use skeleton screens for perceived speed."
- **In this phase:** Determines loading states, progress indicators, animation timing

**Postel's Law** — Accept varied input; send consistent output.
- **Use for:** Form design and feedback
- **Application:** "Forms should accept 'phone' or '(555) 123-4567' as valid. Feedback should be clear: 'Invalid email' not 'Error.'"
- **In this phase:** Shapes form validation, error messages, accessibility

### Simplification

**Occam's Razor** — Prefer the simplest solution.
- **Use for:** Removing unnecessary elements, reducing visual complexity
- **Application:** "Do you need that icon? That animation? That color? Remove it if it doesn't earn its place."
- **In this phase:** Trims visual elements, simplifies copy, removes flourishes

**Tesler's Law** — Complexity is conserved; assign it wisely.
- **Use for:** Deciding where complexity lives (system vs. user)
- **Application:** "Complex sorting logic? Hide it in the backend; show users a simple 'Sort by' dropdown. Move complexity away from users."
- **In this phase:** Shapes how options are presented, what's automatic, what's user choice

**Working Memory** — Users hold 4–7 chunks in mind for ~20–30 seconds.
- **Use for:** Breaking information into scannable chunks
- **Application:** "Don't write paragraphs. Use bullet points. Don't show 10 options; show 3 + 'See all.' Help users process chunks."
- **In this phase:** Shapes copy brevity, list formatting, how much info is visible at once

### Polish & Confidence

**Aesthetic-Usability Effect** — Pretty design feels more usable.
- **Use for:** Visual polish, professional appearance
- **Application:** "Invest in typography, color, spacing, images. Users trust polished interfaces more."
- **In this phase:** Shapes typeface choice, color refinement, imagery quality, overall finish

**Cognitive Bias** — Be aware of systematic biases in design decisions.
- **Use for:** Testing assumptions rather than relying on "it looks good"
- **Application:** "Just because you like this color doesn't mean users will convert more. Recognize your bias; test."
- **In this phase:** Encourages design rationale beyond "looks good" — grounded in user research

---

## Design Decision Workflow

### Step 1: Visual Hierarchy (Von Restorff + Selective Attention)

What's the most important element on this page?
- Primary CTA (usually)
- Key value prop (in hero)
- Customer success story (in proof section)

**Apply Von Restorff:**
- Make it visually distinct: color, size, position
- Don't make *everything* distinct — that defeats the purpose

**Apply Selective Attention:**
- Direct the eye to it through visual weight, color, whitespace
- Remove competing distractions
- Use contrast (color, size, shape) to guide focus

**Example:**
```
Hero section:
- Headline (large, dark text)
- Subheading (medium, secondary color)
- CTA button (large, bright color, lots of space around it)
- Secondary link ("Learn more") — subtle styling

User's eye is drawn to: CTA button (size + color + whitespace)
```

### Step 2: Group & Space (Proximity + Similarity + Common Region)

For each section, ask: What belongs together?

**Apply Law of Proximity:**
- Cluster related items close together
- Use spacing to separate unrelated groups

**Apply Law of Similarity:**
- Give similar items consistent styling
- Different styling = different category

**Apply Law of Common Region:**
- Put related items in cards, boxes, or bounded areas
- Use background color, borders, or frames

**Example:**
```
Feature list:
- Icon (small, left) → Feature title → Feature description
  [These three are close together: belong together]
  
  [Space]
  
- Next feature

Card borders or background color around the group signals: "These belong together"
```

### Step 3: CTA Design (Fitts's Law + Serial Position)

Primary CTA characteristics:
- **Size:** Large enough to hit (48x48px mobile, 40px desktop minimum)
- **Distance:** Easy to reach (not at the very edge)
- **Color:** Visually distinct (uses Von Restorff)
- **Position:** Uses Serial Position (first hero CTA high; final CTA prominent at end)
- **Spacing:** Plenty of white space around it (doesn't compete)

**Common mistake:** Button too small or lost in a sea of text/color.

**Apply Fitts's:**
- Desktop: 40x40px minimum
- Mobile: 48x48px minimum (thumb-friendly)
- Plenty of padding around it (easier to target)

**Apply Serial Position:**
- Hero CTA: Make it prominent (first thing they can act on)
- Final CTA: Make it clear and strong (last chance to convert)

### Step 4: Feedback & Performance (Doherty + Postel's)

**For buttons and interactions:**
- Click → Immediate visual feedback (change color, scale, show loader)
- Response time <400ms (feels instant)
- Longer waits → progress indicator (don't leave user guessing)

**For forms:**
- Input validation → Clear, specific error ("Email must include @" not "Invalid")
- Accept varied input (phone formats, email cases, spaces in ZIP)
- Submit → Clear success state ("Success! Check your email")

**Example:**
```
Form field:
1. User types → instant inline validation
2. Error → red border + specific message
3. Correct input → green checkmark
4. Submit → spinning icon + message "Creating account..."
5. Success → confirmation message + next CTA
```

### Step 5: Copy Simplification (Working Memory + Cognitive Load)

Apply Working Memory principle:
- 4–7 chunks stay in mind for ~20–30 seconds
- Use bullet points instead of paragraphs
- Break information into scannable blocks

**Example:**
```
❌ Don't:
"Our platform helps you manage tasks by providing a unified interface where you can create, assign, and track progress on all your work across teams, with real-time notifications and integrations with your favorite tools."

✓ Do:
- Create and assign tasks
- Track progress in real-time
- Integrates with Slack, Zapier, GitHub
- Notifications keep everyone in sync
```

### Step 6: Progressive Disclosure (Cognitive Load + Occam's)

What information is essential vs. nice-to-have?

**Apply progressive disclosure:**
- Show essential info by default
- Hide details behind "See more," expandable sections, tooltips
- Advanced options in a settings tab

**Example:**
```
Pricing section:
- Show 3 main tiers (essential)
- Click "See details" → expand to show features per tier
- Click "FAQ" → expand common questions
- Advanced: Annual pricing toggle hidden until clicked
```

### Step 7: Consistency & Polish (Aesthetic-Usability + Similarity)

**Consistency:**
- All buttons same style and sizing
- All testimonials same format
- All form fields same styling
- Spacing and margins predictable

**Polish:**
- High-quality typography (typeface, sizing, line height)
- Cohesive color palette (5–6 colors, use intentionally)
- High-quality images or illustrations
- White space (breathing room, not cramped)
- No typos or grammatical errors

---

## Design Review Checklist

When reviewing your design:

- [ ] **Hierarchy:** Can the user identify the primary action in <3 seconds?
- [ ] **Grouping:** Related items are visually grouped (proximity, borders, color)?
- [ ] **CTA:** Button is 40–48px, has breathing room, visually distinct?
- [ ] **Response:** Interactions feel instant (<400ms) or show progress?
- [ ] **Copy:** Scannable bullet points, not dense paragraphs?
- [ ] **Consistency:** All buttons/form fields/cards look the same?
- [ ] **Clutter:** Can you remove anything without breaking function?
- [ ] **Polish:** Typography, color, spacing feel intentional, not random?

---

## Common Issues & Fixes

| Issue | Laws involved | Fix |
|-------|---------------|-----|
| Can't find the CTA | Von Restorff, Fitts's | Make it bigger, brighter, more space around it |
| Too much information visible | Cognitive Load, Working Memory | Hide secondary info, use progressive disclosure |
| Buttons are hard to click | Fitts's | Make them bigger; more padding; easier to reach |
| Form feels overwhelming | Cognitive Load, Chunking | Break into steps or cards; show progress |
| Design feels bland | Aesthetic-Usability | Improve typography, color, imagery, spacing |
| Users miss important info | Selective Attention | Use color, size, or whitespace to guide to it |
| Button clicks don't feel responsive | Doherty | Add immediate visual feedback; show progress for waits >400ms |
| Site looks inconsistent | Similarity | Use component library; standardize styling |

---

## Anti-Patterns

- **Emphasizing everything** — Von Restorff only works if one thing is distinct
- **Too many choices visible** — show 3, hide the rest (Cognitive Load)
- **No feedback on click** — users don't know if something happened
- **Form errors vague** — "Invalid input" not as clear as "Email must include @"
- **Tiny buttons or far away** — Fitts's Law: make them bigger and closer
- **No visual grouping** — all elements equally spaced looks random
- **Dense paragraphs** — Working Memory: use bullets and short sentences
- **Inconsistent styling** — button that's sometimes blue/sometimes green is confusing
- **Slow interactions** — anything >400ms needs a progress indicator
- **Polish neglected** — "I'll fix typography later" — polish matters (Aesthetic-Usability)

---

## Quality Gate

Before handing off to motion-web-design:

- [ ] Primary CTA is visually distinct and easy to target
- [ ] Related elements grouped (proximity, borders, color)
- [ ] All buttons same size/style
- [ ] All forms same styling (inputs, labels, errors)
- [ ] Copy is scannable (bullets, short sentences)
- [ ] Information hierarchy matches audience priority
- [ ] Interactions provide feedback <400ms
- [ ] Color palette is cohesive (5–6 colors, used intentionally)
- [ ] Typography is professional and scannable
- [ ] No clutter — can you remove anything without breaking it?
- [ ] Design matches reference site aesthetic + audience psychographics
