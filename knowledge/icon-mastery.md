# Iconography Mastery

This file defines the strict rules for sourcing, sizing, and styling icons. 

## 1. Approved Icon Libraries
Never hallucinate raw SVG paths for icons. Never use FontAwesome, Material Icons, or Heroicons unless strictly required by the existing codebase. 

Use ONLY the following libraries based on the project's style direction:

*   **Lucide (`lucide-react` / `lucide-vue-next`)**: The default for general use. Neutral, clean, and highly legible.
*   **Phosphor Icons (`@phosphor-icons/react` / `@phosphor-icons/vue`)**: The default for premium, editorial, or multi-weight needs. 
*   **Radix Icons (`@radix-ui/react-icons`)**: The default for dense, technical, or minimal interfaces (fits the "Apple/Linear" aesthetic).

## 2. The Golden Rule: Never Mix Families
If a project uses Lucide, every single icon must be Lucide. Do not mix Radix and Phosphor. Do not mix filled icons with line icons unless representing an active/inactive state (e.g., a filled heart for "liked", outline for "unliked").

## 3. Stroke Weight Matching
Icons are typography. Their stroke weight must optically match the font weight of the text next to them.
*   If text is `font-weight: 300` -> use `stroke-width="1"` or Phosphor Light.
*   If text is `font-weight: 400` -> use `stroke-width="1.5"` or Phosphor Regular.
*   If text is `font-weight: 600+` -> use `stroke-width="2"` or `2.5` or Phosphor Bold.

## 4. Size Constraints
Icons must align to the typographic grid.
*   **Inline with text**: Icon size must exactly match the `line-height` of the adjacent text, not the font-size (e.g., `size={24}` for 16px text with 1.5 line-height).
*   **Standalone (Buttons)**: Typically `20px` or `24px`.
*   **Decorative/Hero**: `48px` or `64px` max.

## 5. Implementation Standard
Prefer importing specific icons from the library rather than using script tags, icon fonts, or hallucinating SVG paths.

```tsx
// DO THIS
import { ArrowRight, Settings } from 'lucide-react';

// NEVER DO THIS
<i class="fas fa-arrow-right"></i>
// OR
<svg> /* hallucinated 20-line path */ </svg>
```

## Evaluation Protocol
When auditing iconography, check:
1. Is the library strictly one of the approved three (Lucide, Phosphor, Radix)?
2. Is the family consistent across the entire page (no mixing)?
3. Does the icon stroke weight optically match the adjacent text weight?
4. Is the icon sized to match the line-height of its adjacent text?