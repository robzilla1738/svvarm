# Component & HTML Mastery

This file defines the strict rules for writing DOM architecture, semantic HTML, and placeholder assets. 

A million-dollar design system falls apart if it is built on "div soup" or inaccessible, non-semantic markup.

## 1. Semantic Architecture over Div Soup
Never use a `<div>` when a semantic HTML5 tag describes the content better.
- Use `<header>`, `<main>`, `<footer>` for primary page structure.
- Use `<section>` for distinct thematic blocks (hero, features, pricing).
- Use `<article>` for self-contained, syndicatable content (blog posts, user cards).
- Use `<aside>` for sidebars or secondary content.
- Use `<nav>` for any cluster of navigation links.

**The "Wrapper" Rule:** Do not add empty `<div>` wrappers just to apply flexbox gaps or margins. Apply spacing primitives directly to the semantic containers.

## 2. Interactive Primitives
Never build interactive elements out of `<div>` or `<span>` tags.
- **Buttons**: If it triggers an action on the page, it MUST be a `<button type="button">`.
- **Links**: If it navigates to a new URL, it MUST be an `<a>` with an `href`.
- **Forms**: Always wrap inputs in a `<form>` tag.
- **Modals**: Use the native `<dialog>` element, not absolute-positioned divs.
- **Toggles/Accordions**: Prefer native `<details>` and `<summary>` elements over complex custom state unless animation requirements absolutely dictate otherwise.

## 3. Tailwind Translation Protocol
When working in a Tailwind environment, you MUST map our OKLCH design tokens to the Tailwind config.
Do not fall back to default Tailwind colors (`bg-gray-500`, `text-indigo-600`) when design tokens are defined.

```js
// Required mapping structure for tailwind.config.js / tailwind.config.ts
theme: {
  colors: {
    bg: "var(--color-bg)",
    surface: {
      DEFAULT: "var(--color-surface)",
      elevated: "var(--color-surface-elevated)",
      subtle: "var(--color-surface-subtle)",
    },
    text: {
      DEFAULT: "var(--color-text)",
      muted: "var(--color-text-muted)",
      subtle: "var(--color-text-subtle)",
    },
    primary: {
      DEFAULT: "var(--color-primary)",
      hover: "var(--color-primary-hover)",
      active: "var(--color-primary-active)",
    },
    border: {
      DEFAULT: "var(--color-border)",
      strong: "var(--color-border-strong)",
    },
    success: "var(--color-success)",
    warning: "var(--color-warning)",
    error: "var(--color-error)",
    info: "var(--color-info)",
  }
}
```

## 4. The Placeholder Asset Strategy
When generating UI that requires media, never use ugly generic placeholders (e.g., `via.placeholder.com`). 
The UI must look expensive even when empty.

**For abstract structural representations:**
Use a solid block colored with `--color-surface-elevated` or `--color-surface` and place a single, perfectly centered, muted Lucide/Phosphor icon inside it to indicate the media type (e.g., `<Image />` or `<Video />`).

**For photographic placeholders:**
Use high-quality Unsplash source URLs, but apply parameters that match the project's style direction.
- *Minimal/monochrome directions*: `https://images.unsplash.com/photo-[id]?auto=format&fit=crop&w=800&q=80&grayscale=true`
- *Warm/natural directions*: Add `&tint=warm` or select nature/architecture imagery.
- *Bold/vibrant directions*: Select highly saturated, vibrant imagery.

## 5. Framework Architecture (React & Next.js)
If building for modern frameworks like Next.js App Router:
- **RSC Safety**: Global state and complex interactions work ONLY in Client Components. 
- **Interactivity Isolation**: Do not put `'use client'` at the top of a massive page file. Isolate interactive UI (buttons, heavy animations, forms) into specific leaf components with `'use client'`. Let the parent remain a static Server Component.

## 6. Performance & Rendering Guardrails
- **Z-Index Restraint**: NEVER arbitrarily spam `z-50` or `z-10` unprompted. Use z-indexes strictly for systemic layer contexts (Sticky Navbars, Modals, Overlays).
- **Noise/Grain Performance**: If applying noise/grain filters, apply them EXCLUSIVELY to fixed, `pointer-events-none` pseudo-elements covering the screen (`fixed inset-0 z-50`). NEVER apply CSS noise to scrolling containers, as this causes continuous GPU repaints and destroys mobile performance.

## 7. Component Recipes

Complete, token-based CSS recipes for common components. All use `var(--color-*)` and `var(--space-*)` tokens so they adapt to any style direction.

### Button (Primary + Secondary)

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-xs);
  padding: var(--space-sm) var(--space-md);
  font-family: var(--font-body, inherit);
  font-size: var(--text-body-sm, 0.875rem);
  font-weight: 500;
  line-height: 1;
  border-radius: 0.375rem;
  border: 1px solid transparent;
  cursor: pointer;
  transition: background-color 150ms ease, border-color 150ms ease, box-shadow 150ms ease;
  text-decoration: none;
  white-space: nowrap;
}

.btn--primary {
  background: var(--color-primary);
  color: var(--color-bg);
  border-color: var(--color-primary);
}
.btn--primary:hover {
  background: var(--color-primary-hover);
  border-color: var(--color-primary-hover);
}
.btn--primary:active {
  background: var(--color-primary-active);
}
.btn--primary:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}

.btn--secondary {
  background: transparent;
  color: var(--color-text);
  border-color: var(--color-border-strong);
}
.btn--secondary:hover {
  background: var(--color-surface-subtle);
  border-color: var(--color-text-muted);
}
.btn--secondary:active {
  background: var(--color-surface);
}
.btn--secondary:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

### Card

```css
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 0.5rem;
  padding: var(--space-lg);
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
}
.card__title {
  font-size: var(--text-h3, 1.25rem);
  font-weight: 600;
  line-height: 1.3;
  color: var(--color-text);
}
.card__description {
  font-size: var(--text-body, 1rem);
  line-height: 1.5;
  color: var(--color-text-muted);
}
.card__footer {
  margin-top: auto;
  padding-top: var(--space-sm);
  border-top: 1px solid var(--color-border);
}
```

### Input (with Error and Focus States)

```html
<div class="input-group">
  <label class="input-group__label" for="email">Email</label>
  <input class="input-group__field" type="email" id="email" placeholder="you@example.com" />
  <p class="input-group__error" role="alert">Please enter a valid email address</p>
</div>
```

```css
.input-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
}
.input-group__label {
  font-size: var(--text-label, 0.8125rem);
  font-weight: 500;
  color: var(--color-text);
}
.input-group__field {
  padding: var(--space-sm) var(--space-md);
  font-size: var(--text-body, 1rem);
  line-height: 1.5;
  color: var(--color-text);
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 0.375rem;
  transition: border-color 150ms ease, box-shadow 150ms ease;
}
.input-group__field::placeholder {
  color: var(--color-text-subtle);
}
.input-group__field:focus {
  outline: none;
  border-color: var(--color-focus);
  box-shadow: 0 0 0 3px oklch(from var(--color-focus) l c h / 0.2);
}
.input-group__field[aria-invalid="true"],
.input-group--error .input-group__field {
  border-color: var(--color-error);
  box-shadow: 0 0 0 3px oklch(from var(--color-error) l c h / 0.15);
}
.input-group__error {
  font-size: var(--text-caption, 0.75rem);
  color: var(--color-error);
  display: none;
}
.input-group--error .input-group__error {
  display: block;
}
```

### Nav

```html
<header class="site-header">
  <nav class="site-nav" aria-label="Main navigation">
    <a class="site-nav__logo" href="/">Logo</a>
    <ul class="site-nav__links">
      <li><a href="/features">Features</a></li>
      <li><a href="/pricing">Pricing</a></li>
      <li><a href="/docs">Docs</a></li>
    </ul>
    <div class="site-nav__actions">
      <a class="btn btn--secondary" href="/login">Sign in</a>
      <a class="btn btn--primary" href="/signup">Get started</a>
    </div>
  </nav>
</header>
```

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  background: oklch(from var(--color-bg) l c h / 0.85);
  backdrop-filter: blur(12px) saturate(1.5);
  -webkit-backdrop-filter: blur(12px) saturate(1.5);
  border-bottom: 1px solid var(--color-border);
}
.site-nav {
  display: flex;
  align-items: center;
  gap: var(--space-lg);
  padding: var(--space-sm) var(--space-md);
  max-inline-size: var(--wide-max, 90rem);
  margin-inline: auto;
}
.site-nav__logo {
  font-weight: 700;
  font-size: var(--text-h3, 1.25rem);
  color: var(--color-text);
  text-decoration: none;
}
.site-nav__links {
  display: flex;
  gap: var(--space-md);
  list-style: none;
  margin: 0;
  padding: 0;
}
.site-nav__links a {
  color: var(--color-text-muted);
  text-decoration: none;
  font-size: var(--text-body-sm, 0.875rem);
  transition: color 150ms ease;
}
.site-nav__links a:hover {
  color: var(--color-text);
}
.site-nav__actions {
  margin-inline-start: auto;
  display: flex;
  gap: var(--space-sm);
  align-items: center;
}
```

### Modal (Native `<dialog>`)

```html
<dialog class="modal" id="my-modal">
  <div class="modal__content">
    <h2 class="modal__title">Confirm action</h2>
    <p class="modal__body">Are you sure you want to proceed?</p>
    <div class="modal__actions">
      <button class="btn btn--secondary" data-close>Cancel</button>
      <button class="btn btn--primary">Confirm</button>
    </div>
  </div>
</dialog>
```

```css
.modal {
  border: none;
  border-radius: 0.75rem;
  padding: 0;
  max-inline-size: min(90vw, 32rem);
  background: var(--color-surface);
  color: var(--color-text);
  box-shadow: 0 25px 50px -12px oklch(0% 0 0 / 0.25);
}
.modal::backdrop {
  background: oklch(0% 0 0 / 0.5);
  backdrop-filter: blur(4px);
}
.modal__content {
  padding: var(--space-lg);
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}
.modal__title {
  font-size: var(--text-h3, 1.25rem);
  font-weight: 600;
}
.modal__body {
  color: var(--color-text-muted);
  line-height: 1.5;
}
.modal__actions {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-sm);
  padding-top: var(--space-sm);
}
```

```js
// Open/close
document.querySelector('[data-open-modal]').addEventListener('click', () => {
  document.getElementById('my-modal').showModal();
});
document.querySelectorAll('[data-close]').forEach(btn => {
  btn.addEventListener('click', () => btn.closest('dialog').close());
});
```

---

## 8. Data & Typography Content Rules
- **Anti-Emoji Policy [CRITICAL]**: NEVER use emojis in code, markup, text content, or alt text. Emojis ruin premium aesthetics. Replace them entirely with high-quality icons (Lucide/Phosphor) or clean SVG primitives.
- **The "Jane Doe" Effect (No Generic Mock Data)**: 
  - *Names*: "John Doe", "Sarah Chan", or "Jack Su" are BANNED. Invent creative, realistic-sounding names (e.g., "Elara Vance", "Tobias Sterling").
  - *Numbers*: Avoid predictable outputs like `99.99%`, `50%`, or `1234567`. Use organic, messy data (`47.2%`, `+1 (312) 847-1928`).
  - *Brands*: "Acme", "Nexus", "SmartFlow" are BANNED. Invent premium, contextual brand names.