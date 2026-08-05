# 🛠️ SVG Editing Cheat Sheet — Make Changes Yourself

## The Golden Rule

> **SVG files are just text.** Open them in any code editor (VS Code, Notepad, Cursor) and edit the text. Save. Done.

You don't need Illustrator, Figma, or any design tool. These are all hand-coded SVGs.

---

## Quick Anatomy of an SVG

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 WIDTH HEIGHT">
  <!-- Everything lives here -->
</svg>
```

| Attribute | What It Does |
|-----------|-------------|
| `viewBox="0 0 1100 320"` | The canvas size. First two numbers are origin (always 0,0). Last two are width and height in pixels. |
| `width="100%"` | When used in README, stretches to fill container |

---

## The 5 Things You'll Actually Change

### 1. Changing Text Content

Find this pattern:
```xml
<text x="100" y="50" font-family="'JetBrains Mono', monospace" font-size="12" fill="#e8f5e9">
  Python
</text>
```

Just change what's between `>` and `</text>`:
```xml
<text x="100" y="50" font-family="'JetBrains Mono', monospace" font-size="12" fill="#e8f5e9">
  Go  <!-- changed from Python -->
</text>
```

### 2. Changing Progress Bar Width (Skill Levels)

In `skill_matrix.svg`, each skill has TWO rectangles:

```xml
<!-- Background bar (always full width) -->
<rect x="160" y="4" width="250" height="14" rx="3" fill="#0f2e1c" stroke="#1a3d2a" stroke-width="1"/>

<!-- Fill bar (this is the actual level) -->
<rect x="160" y="4" width="237" height="14" rx="3" fill="#7cb342" opacity="0.85"/>
<!--                    ^^^^
                        CHANGE THIS NUMBER (0 to 250) -->

<!-- Percentage label -->
<text x="420" y="15" font-family="'JetBrains Mono', monospace" font-size="11" fill="#aed581">
  95%
  <!-- ^^^ CHANGE THIS TO MATCH -->
</text>
```

**Math:** `width / 250 * 100 = percentage`

| If you want | Set width to |
|-------------|-------------|
| 100% | 250 |
| 95% | 237 |
| 90% | 225 |
| 85% | 212 |
| 80% | 200 |
| 75% | 187 |
| 70% | 175 |
| 65% | 162 |
| 60% | 150 |
| 55% | 137 |
| 50% | 125 |

### 3. Changing Colors

All colors are hex codes. Search-and-replace in your editor:

| What | Current Value | What It Looks Like |
|------|--------------|-------------------|
| Background | `#0a1f14` | Dark green |
| Grid lines | `#1a3d2a` | Slightly lighter green |
| Accent/primary | `#7cb342` | Yellow-green (ticks, bars) |
| Text primary | `#e8f5e9` | Light green-white |
| Text secondary | `#aed581` | Soft green |

**Example:** Want orange accents instead of green?
1. Open the SVG
2. Find-and-replace all `#7cb342` with `#ff9800`
3. Find-and-replace all `#aed581` with `#ffb74d`
4. Find-and-replace all `#e8f5e9` with `#fff3e0`
5. Save

### 4. Moving Things Around (Positioning)

Every element has `x` and `y` coordinates:

```xml
<text x="100" y="50">Hello</text>
<!--     ^^^   ^^^
        left   top
        edge   edge -->
```

**To move right:** Increase `x`
**To move down:** Increase `y`
**To move left:** Decrease `x`
**To move up:** Decrease `y`

**For groups (columns of items):**
```xml
<g transform="translate(50, 70)">
  <!-- everything inside moves together -->
</g>
```
Change the two numbers: `(x, y)`

### 5. Adding a New Skill

In `skill_matrix.svg`, copy an entire `<g>...</g>` block (one skill), paste it below, then change:
1. The `transform="translate(X, Y)"` — move it down by ~40px from the last item
2. The skill name text
3. The subtitle text
4. The fill bar `width`
5. The percentage text

---

## The Skill Matrix Layout (So You Understand the Spacing)

```
┌─────────────────────────────────────────────────────────────────┐
│  TITLE: BLADE SHARPNESS MATRIX                                  │
├──────────────────────────────┬──────────────────────────────────┤
│  LEFT COLUMN (x=50)          │  RIGHT COLUMN (x=530)            │
│                              │                                  │
│  Python ─────[████████] 95%  │  SQL ────────[██████░░] 80%      │
│  TypeScript ──[███████░] 90% │  Git ────────[███████░] 85%       │
│  React ───────[███████░░] 85%│  Docker ─────[████░░░░] 60%       │
│  CSS ─────────[████████] 95%  │  System Des ─[████░░░░] 50%       │
│                              │                                  │
│  name at x=0                 │  name at x=0                     │
│  bar starts at x=160         │  bar starts at x=180             │
│  bar max width=250           │  bar max width=200               │
│  % text at x=420             │  % text at x=390                 │
└──────────────────────────────┴──────────────────────────────────┘
```

**Why the bars are different widths?** Left column has more space. Right column is tighter.

**The gap between columns:** 530 - (50 + 160 + 250) = 70px of breathing room.

---

## Common Problems & Fixes

### "Text is cut off at the edge"
→ The `viewBox` is too small. Increase the width:
```xml
viewBox="0 0 1100 320"  →  viewBox="0 0 1300 320"
```

### "Two things overlap"
→ One of these is too close to the other:
- `x` positions
- `y` positions  
- `width` of a bar extending into text

**Fix:** Increase the gap. If bar text is at x=420 and next column starts at x=500, that's only 80px. Move the next column to x=550 for more space.

### "I changed text but it looks weird"
→ Longer text needs more space. If you change "Python" to "Python & FastAPI", the bar might need to start further right:
```xml
<!-- Before -->
<rect x="160" y="4" .../>

<!-- After (move bar right so name fits) -->
<rect x="200" y="4" .../>
```

### "The percentage doesn't match the bar"
→ `width / max_width * 100` should equal your percentage text. If bar width is 200 and max is 250, that's 80%. Make sure the text says 80%.

---

## Workflow: Edit → Preview → Commit

1. **Edit** the `.svg` file in your code editor
2. **Preview** by opening the file in your browser (Chrome, Safari, Firefox)
   - Just double-click the file, it opens in browser
   - Hit `Cmd/Ctrl + R` to refresh after saving
3. **Commit** to GitHub when it looks right

---

## Pro Tips

- **Use VS Code with an SVG extension** — it gives you color previews and auto-completion
- **Keep a backup** — copy the original file before making big changes
- **Change one thing at a time** — save and preview after each change
- **The `opacity` attribute** controls transparency: 1.0 = fully visible, 0.0 = invisible, 0.5 = half transparent
- **The `rx` attribute** on rectangles controls corner roundness. Higher = more rounded.

---

## Want to Go Further?

### Add a New Section Divider

Copy any `divider_v2_*.svg`, change the text in the middle:
```xml
<text x="550" y="50" ...>YOUR NEW TITLE</text>
```

### Add a New Project Card

Copy any `project_v2_*.svg`, change:
1. Project name (the bold text)
2. Description
3. Tech tag text AND the tag width: `width="{len(tech)*8+24}"` → count characters, multiply by 8, add 24

### Change the Header Text

Open `v2_header.svg`. Find:
```xml
<text x="600" y="175" ...>H A R D E E P</text>
<text x="600" y="220" ...>D A S H E T T Y</text>
```

Change to whatever you want. Adjust `y` values if text gets taller/shorter.

---

*The mat is yours. Adjust the grid. Sharpen the blades. Make the cuts.*
