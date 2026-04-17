---
name: inspector-overlay
description: install, integrate, remove, and troubleshoot a reusable dom inspector overlay component for nextjs or react apps. use when asked to add the inspector overlay, wire it into app.tsx, app/layout.tsx, or similar root wrappers, explain setup, uninstall it, or troubleshoot installation of the inspector-overlay skill. this skill uses the reference component in references/LlmInspectorOverlay.tsx as the source of truth for the implementation to copy into the target project.
---

# Inspector Overlay

Install, integrate, remove, and troubleshoot the inspector overlay component using the reference file at `references/LlmInspectorOverlay.tsx`.

## What this skill does

This skill adds a development-only UI overlay that lets a user:

- hold `Alt` to inspect elements
- `Alt + click` to select and copy a single-element payload
- `Alt + Shift + click` to add or remove elements from a multi-selection
- see selected elements remain highlighted while `Alt` is held
- copy payloads intended for coding agents or coding llms

Use `references/LlmInspectorOverlay.tsx` as the canonical implementation. Do not rewrite it from scratch unless the user explicitly asks for changes.

## Files in this skill

- `references/LlmInspectorOverlay.tsx` — the source component to copy into the user's project

## Installation workflow

Follow these steps in order.

### 1. Locate the app root

Determine where the overlay should wrap the app.

Common cases:

- React with a root app file:
  - `src/App.tsx`
  - `App.tsx`
- Next.js App Router:
  - `app/layout.tsx`
- Next.js Pages Router:
  - `pages/_app.tsx`

If the project structure is unclear, inspect the repository and identify the correct root wrapper file before making changes.

### 2. Create the component file

Copy `references/LlmInspectorOverlay.tsx` into the project as a client component.

Recommended locations:

- React:
  - `src/components/LlmInspectorOverlay.tsx`
  - or `src/LlmInspectorOverlay.tsx`
- Next.js:
  - `components/LlmInspectorOverlay.tsx`
  - or `src/components/LlmInspectorOverlay.tsx`

Preserve the component name: `LlmInspectorOverlay`.

### 3. Import and wrap the app

Wrap the app's rendered children with `LlmInspectorOverlay`.

#### React example

```tsx
import LlmInspectorOverlay from "./components/LlmInspectorOverlay";

export default function App() {
  return (
    <LlmInspectorOverlay>
      <Router />
    </LlmInspectorOverlay>
  );
}
````

Adjust the import path to match the actual file location.

#### Next.js App Router example

```tsx
import LlmInspectorOverlay from "@/components/LlmInspectorOverlay";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <LlmInspectorOverlay>{children}</LlmInspectorOverlay>
      </body>
    </html>
  );
}
```

#### Next.js Pages Router example

```tsx
import type { AppProps } from "next/app";
import LlmInspectorOverlay from "@/components/LlmInspectorOverlay";

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <LlmInspectorOverlay>
      <Component {...pageProps} />
    </LlmInspectorOverlay>
  );
}
```

### 4. Preserve client-component requirements

If installing into Next.js, ensure the component file keeps:

```tsx
"use client";
```

Do not remove it.

### 5. Verify that development gating is intact

The reference component is intended to be development-only by default via its `enabled` prop default logic.

Do not change that behavior unless the user asks.

If the user wants explicit control, show them this optional usage:

```tsx
<LlmInspectorOverlay enabled={process.env.NODE_ENV === "development"}>
  {children}
</LlmInspectorOverlay>
```

### 6. Recommend semantic hooks when helpful

If the user's goal is to generate better payloads for coding agents, suggest adding stable DOM hooks in their app markup where appropriate:

* `data-testid`
* `data-file`
* `data-component`
* `data-map-key`

Example:

```tsx
<a
  data-testid="quick-link-education-teen-troupe"
  data-file="src/pages/Home.tsx"
  data-component="QuickLinks"
  data-map-key="quickLinks[href='/education/teen-troupe']"
>
  ...
</a>
```

These are optional, but they make payloads much more useful.

## Removal workflow

Use this when the user asks to uninstall, remove, back out, or disable the overlay.

Follow these steps in order.

### 1. Find where the overlay was installed

Check the app root for an import and wrapper such as:

* `import LlmInspectorOverlay from "...";`
* `<LlmInspectorOverlay> ... </LlmInspectorOverlay>`

Common files:

* `src/App.tsx`
* `App.tsx`
* `app/layout.tsx`
* `pages/_app.tsx`

### 2. Remove the wrapper

Unwrap the app so the original rendered tree remains intact.

#### React before

```tsx
export default function App() {
  return (
    <LlmInspectorOverlay>
      <Router />
    </LlmInspectorOverlay>
  );
}
```

#### React after

```tsx
export default function App() {
  return <Router />;
}
```

#### Next.js App Router before

```tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <LlmInspectorOverlay>{children}</LlmInspectorOverlay>
      </body>
    </html>
  );
}
```

#### Next.js App Router after

```tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

### 3. Remove the import

Delete the `LlmInspectorOverlay` import from the root wrapper file.

### 4. Delete the component file

Remove the installed component file, typically one of:

* `src/components/LlmInspectorOverlay.tsx`
* `src/LlmInspectorOverlay.tsx`
* `components/LlmInspectorOverlay.tsx`

Delete it only after confirming no other files still import it.

### 5. Leave optional semantic hooks alone unless asked

Do not remove `data-testid`, `data-file`, `data-component`, or `data-map-key` attributes unless the user explicitly asks for those to be removed too.

Those hooks may still be useful for testing or debugging even after uninstalling the overlay.

### 6. Confirm cleanup

After removal, report:

1. which wrapper file was restored
2. which import was removed
3. whether the component file was deleted
4. whether any semantic hooks were left in place

## Behavior to preserve

When installing, preserve these behaviors from the reference component:

* green hover overlay while inspecting
* blue overlay for selected items
* multi-select support with `Alt + Shift + click`
* selected items remain highlighted until `Alt` is released
* native text selection is suppressed while the inspector is active
* `Escape` clears the current selection state
* payloads are copied to the clipboard

Do not simplify or remove these behaviors unless the user asks.

## How to respond after installation

After making the changes, report:

1. where the component file was created
2. which app root file was updated
3. the exact wrapper that was added
4. any optional semantic hooks that were recommended or added

## How to respond after removal

After uninstalling, report:

1. which root file was restored
2. the exact wrapper that was removed
3. whether the import was removed
4. whether the component file was deleted
5. whether semantic hooks were kept or removed

## Troubleshooting guidance

### If text gets selected while multi-clicking

Ensure the installed version includes the logic that:

* disables native selection while `Alt` is held
* prevents default on `mousedown`
* clears native selection ranges

Do not ship an older version that lacks this behavior.

### If selected overlays disappear too early

Ensure selection is cleared only when:

* `Alt` is released
* `Escape` is pressed

Do not clear selection on `Enter`.

### If Next.js throws a client component error

Confirm:

* `LlmInspectorOverlay.tsx` includes `"use client";`
* the overlay is imported into a valid parent component
* the root wrapper usage is correct for the router style in that app

## Editing rule

If the user asks to modify the overlay behavior, update the implementation by editing the installed copy and keep the reference behavior aligned with the user's request when appropriate.

When describing, installing, or removing this skill, always treat `references/LlmInspectorOverlay.tsx` as the implementation source of truth.

