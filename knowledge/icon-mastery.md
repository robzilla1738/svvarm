# Iconography Mastery

This file defines the strict rules for sourcing, sizing, and styling icons.

## 1. Approved Icon Libraries
Never hallucinate raw SVG paths for icons. Never use FontAwesome, Material Icons, or Heroicons unless strictly required by the existing codebase.

Use ONLY the following libraries based on the project's style direction:

*   **Lucide (`lucide-react` / `lucide-vue-next`)**: The default for general use. Neutral, clean, and highly legible.
*   **Phosphor Icons (`@phosphor-icons/react` / `@phosphor-icons/vue`)**: The default for premium, editorial, or multi-weight needs.
*   **Radix Icons (`@radix-ui/react-icons`)**: The default for dense, technical, or minimal interfaces (fits the "Apple/Linear" aesthetic).

---

## Library Selection Decision Tree

| Project Style | Library | Why |
|--------------|---------|-----|
| General SaaS, dashboard, utility | **Lucide** | Neutral, clean, widest icon coverage |
| Editorial, marketing, brand-heavy | **Phosphor** | 6 weight variants (thin→fill) let you match any typographic weight |
| Dense UI, dev tools, minimal/Linear aesthetic | **Radix** | 15×15px grid, designed for tight spaces, fewer icons but curated |
| Existing codebase uses something else | **Match existing** | Consistency > preference. Never mix. |

### Comparison

| Feature | Lucide | Phosphor | Radix |
|---------|--------|----------|-------|
| Icon count | 1,400+ | 1,200+ | 300+ |
| Base grid | 24×24 | 24×24 (but scales well to 16) | 15×15 |
| Weight variants | Stroke width only | 6 named weights | Single weight |
| Fill variants | No (stroke only) | Yes (Fill weight) | Mixed (some filled) |
| Best for | General purpose | Editorial/premium | Dense/minimal |
| Tree-shakeable | Yes | Yes | Yes |

**Rule:** If you need more than ~250 unique icons, Lucide or Phosphor. If you need fewer than 100 and want maximum density, Radix.

---

## 2. The Golden Rule: Never Mix Families
If a project uses Lucide, every single icon must be Lucide. Do not mix Radix and Phosphor. Do not mix filled icons with line icons unless representing an active/inactive state (e.g., a filled heart for "liked", outline for "unliked").

## 3. Stroke Weight Matching
Icons are typography. Their stroke weight must optically match the font weight of the text next to them.
*   If text is `font-weight: 300` -> use `stroke-width="1"` or Phosphor Light.
*   If text is `font-weight: 400` -> use `stroke-width="1.5"` or Phosphor Regular.
*   If text is `font-weight: 600+` -> use `stroke-width="2"` or `2.5` or Phosphor Bold.

---

## Decorative vs Functional Icons

### Functional Icons (convey meaning or action)
Must have an accessible name. The icon IS the label.

```tsx
// Icon-only button — MUST have aria-label
<button aria-label="Close dialog" class="btn-icon">
  <X size={20} aria-hidden="true" />
</button>

// Icon WITH visible text — icon is decorative
<button>
  <ArrowRight size={16} aria-hidden="true" />
  <span>Continue</span>
</button>
```

### Decorative Icons (visual only, no information)
Must be hidden from assistive technology.

```tsx
// Icon next to text label — purely decorative
<li>
  <Check size={16} aria-hidden="true" />
  <span>Feature included</span>
</li>

// Icon as section decoration
<div class="feature-icon" aria-hidden="true">
  <Zap size={48} />
</div>
```

### Rules
- If removing the icon would lose information → it's functional → needs `aria-label`
- If removing the icon would only lose decoration → it's decorative → needs `aria-hidden="true"`
- Never put `aria-label` AND visible text on the same element (screenreaders would announce both)
- Never use `title` attribute on icons for tooltips — use a real tooltip component

---

## Icon-in-Button Patterns

### Leading Icon (icon before text)
```tsx
<button class="btn">
  <Plus size={16} aria-hidden="true" />
  <span>Create project</span>
</button>
```

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  min-height: 44px; /* touch target */
}
.btn svg {
  flex-shrink: 0;
}
```

### Trailing Icon (icon after text)
```tsx
<a href="/pricing" class="btn-secondary">
  <span>View pricing</span>
  <ArrowRight size={16} aria-hidden="true" />
</a>
```
Trailing icons typically indicate navigation direction or expansion (chevrons, arrows).

### Icon-Only Button
```tsx
<button aria-label="Delete item" class="btn-icon">
  <Trash2 size={20} aria-hidden="true" />
</button>
```

```css
.btn-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;  /* minimum touch target */
  height: 44px; /* minimum touch target */
  padding: 0;
  border-radius: var(--radius-md);
  color: var(--color-text-muted);
  background: transparent;
  border: none;
  cursor: pointer;
  transition: color 150ms ease, background-color 150ms ease;
}
.btn-icon:hover {
  color: var(--color-text);
  background: var(--color-surface-subtle);
}
.btn-icon:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

**Critical:** Icon-only buttons MUST be at least 44×44px for touch accessibility, even if the icon itself is 20px. The padding absorbs the difference.

---

## 4. Sizing Reference Table

| Context | Icon Size | Notes |
|---------|-----------|-------|
| Inline with body text (16px) | 16px or `1em` | Match line-height feel, not font-size |
| Inline with small text (14px) | 14px | Tight spaces: breadcrumbs, metadata |
| In buttons | 16–20px | 16px for small buttons, 20px for standard |
| Navigation items | 20px | Consistent across all nav icons |
| Sidebar navigation | 20–24px | Match the sidebar text size |
| Feature highlight | 32–40px | Section icons, benefit lists |
| Hero / decorative | 48–64px | Maximum size. Beyond 64px, use an illustration |
| Badge / status dot | 8–12px | `filled` circle or small indicator |

**Rule:** Never exceed 64px for icons. At that size, you need illustration, not iconography. Icons are meant to be read at a glance — oversizing them makes them feel empty and clip-art-like.

---

## 5. Color and Contrast

### Default: `currentColor`
Icons should inherit their text color by default. Never hard-code icon colors unless they represent a specific state.

```css
/* Icons inherit text color */
svg { color: currentColor; }

/* Muted icons for secondary information */
.icon-muted { color: var(--color-text-muted); }

/* Active/interactive icons */
.icon-active { color: var(--color-primary); }
```

### Contrast Requirements
| Icon type | Minimum contrast | Standard |
|-----------|-----------------|----------|
| Functional (conveys meaning) | 3:1 against background | WCAG 2.1 SC 1.4.11 |
| Decorative | No requirement | — |
| Interactive (button) | 3:1 + visible focus ring | WCAG 2.1 SC 1.4.11 |
| Disabled | Exempt from contrast | But must not be interactive |

### Active State Treatment
```css
/* Filled variant for active/selected state */
.nav-item.is-active svg {
  fill: currentColor;
  stroke: none;
}

/* Or color change */
.nav-item.is-active svg {
  color: var(--color-primary);
}
```

Use filled-vs-outline to communicate active-vs-inactive state (like iOS tab bars). This is the ONE case where mixing filled and outline icons in the same interface is acceptable.

---

## Anti-Patterns

### Mixing Libraries
```tsx
// NEVER — Lucide search with Phosphor settings with Radix hamburger
import { Search } from 'lucide-react';
import { GearSix } from '@phosphor-icons/react';
import { HamburgerMenuIcon } from '@radix-ui/react-icons';
```
Pick one library. Use it everywhere. If one library doesn't have the icon you need, find the closest equivalent — do not bring in a second library for one icon.

### Inconsistent Fill/Outline
```tsx
// NEVER — mixing filled and outline in the same navigation
<nav>
  <Home fill="currentColor" />    {/* filled */}
  <Users strokeWidth={1.5} />     {/* outline */}
  <Settings fill="currentColor" /> {/* filled */}
  <Bell strokeWidth={1.5} />      {/* outline */}
</nav>
```
All icons in a set must use the same style. The only exception: filled = active, outline = inactive.

### Hallucinated SVG Paths
AI models frequently generate SVG `<path>` data that doesn't render correctly. The paths look valid but produce garbled shapes.
```tsx
// NEVER — hallucinated path data
<svg viewBox="0 0 24 24">
  <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
</svg>
```
**Always** import from an approved library. If you need a custom icon, use a real SVG editor.

### Emoji as Icons
```html
<!-- NEVER — emoji render differently across platforms, can't be styled -->
<button>🗑️ Delete</button>
<span class="status">✅ Active</span>
```
Emoji are not icons. They can't inherit `currentColor`, can't be sized with CSS, and render differently on every platform. Use proper SVG icons.

### Over-Sized Icons
```css
/* NEVER — icons at illustration scale */
.feature-icon svg {
  width: 128px;
  height: 128px;
}
```
Beyond 64px, stroke-based icons look hollow and clip-art-like. At that scale, use an illustration or a custom graphic.

---

## 6. Implementation Standard
Prefer importing specific icons from the library rather than using script tags, icon fonts, or hallucinating SVG paths.

```tsx
// DO THIS
import { ArrowRight, Settings } from 'lucide-react';

// NEVER DO THIS
<i class="fas fa-arrow-right"></i>
// OR
<svg> /* hallucinated 20-line path */ </svg>
```

---

## Worked Example: Dashboard Nav with Mixed Icons → Single Library, Consistent, Accessible

### Before (typical AI output)

```tsx
<nav class="sidebar-nav">
  <a href="/dashboard">
    <svg viewBox="0 0 24 24"><path d="M3 12l2-2m0 0l7-7 7 7M5..." /></svg>
    Dashboard
  </a>
  <a href="/analytics">
    <i class="fas fa-chart-bar"></i>
    Analytics
  </a>
  <a href="/settings">
    <img src="/icons/settings.png" width="20" />
    Settings
  </a>
  <a href="/help">
    ❓ Help
  </a>
</nav>
```

Problems: Hallucinated SVG path, FontAwesome mixed with SVG, PNG icon, emoji as icon, no accessibility attributes, no consistent sizing, no active state.

### After (single library, accessible, consistent)

```tsx
import { LayoutDashboard, BarChart3, Settings, HelpCircle } from 'lucide-react';

function SidebarNav({ currentPath }) {
  const items = [
    { href: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { href: '/analytics', label: 'Analytics', icon: BarChart3 },
    { href: '/settings', label: 'Settings', icon: Settings },
    { href: '/help', label: 'Help', icon: HelpCircle },
  ];

  return (
    <nav aria-label="Main navigation">
      <ul role="list">
        {items.map(({ href, label, icon: Icon }) => (
          <li key={href}>
            <a
              href={href}
              className={`nav-item ${currentPath === href ? 'is-active' : ''}`}
              aria-current={currentPath === href ? 'page' : undefined}
            >
              <Icon size={20} aria-hidden="true" strokeWidth={1.5} />
              <span>{label}</span>
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
```

```css
.nav-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.625rem 1rem;
  color: var(--color-text-muted);
  text-decoration: none;
  border-radius: var(--radius-md);
  transition: color 150ms ease, background-color 150ms ease;
}
.nav-item:hover {
  color: var(--color-text);
  background: var(--color-surface-subtle);
}
.nav-item:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: -2px;
}
.nav-item.is-active {
  color: var(--color-primary);
  background: oklch(from var(--color-primary) l c h / 0.08);
  font-weight: 500;
}
.nav-item svg {
  flex-shrink: 0;
}
```

Key improvements:
- Single library (Lucide) for all icons
- Consistent size (20px) and stroke weight (1.5)
- `aria-hidden="true"` on all icons (text labels provide meaning)
- `aria-label` on `<nav>` for landmark identification
- `aria-current="page"` for active state
- Active state communicated through color, not fill-vs-outline switching
- Proper focus ring for keyboard navigation
- Touch-friendly padding on all items

---

## Evaluation Protocol
When auditing iconography, check:
1. Is the library strictly one of the approved three (Lucide, Phosphor, Radix)?
2. Is the family consistent across the entire page (no mixing)?
3. Does the icon stroke weight optically match the adjacent text weight?
4. Is the icon sized to match the line-height of its adjacent text?
5. Do all functional icons have `aria-label` (icon-only) or `aria-hidden="true"` (with text)?
6. Are icon-only buttons at least 44×44px?
7. Are all icons imported from the library, with no hallucinated SVG paths?
8. Is `currentColor` used instead of hard-coded color values?
9. Do active/inactive states use a consistent pattern across the interface?
10. Are there zero emoji used as interface icons?
