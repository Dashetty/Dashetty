# 🟩 Cutting Mat README v2 — Setup Guide

## What Changed from v1

This version is built **entirely around your identity**:
- Your "finisher" mentality → "I don't start things I don't intend to finish"
- Your pixel-perfect obsession → "My product designer eye doesn't sleep"
- Your AI + system design trajectory → "Currently Cutting" section with progress bars
- Your graphic design background → Visual craft language throughout
- Your job/collab goals → "Open to opportunities & collaborations" front and center
- No corporate onboarding mentions — this is your craft, not your employer's

## File Structure

```
assets/
├── v2_header.svg                      # Main banner (1200×400) — faithful to your screenshot
├── skill_matrix.svg                   # Blade sharpness matrix — your tech stack visualized
├── currently_cutting.svg              # WIP section with progress indicators
├── divider_v2_workbench.svg           # "The Workbench" section
├── divider_v2_toolkit.svg           # "Blade Sharpness Matrix" section
├── divider_v2_current_cuts.svg      # "Currently on the Mat" section
├── divider_v2_finished_cuts.svg       # "Finished Cuts" section
├── divider_v2_connect.svg             # "Registration Marks" section
├── footer.svg                         # Closes out the mat
├── project_v2_portfolio.svg           # Project card: Portfolio
├── project_v2_vista_forms.svg         # Project card: Vista Forms
├── project_v2_pet_tumor_calc.svg      # Project card: PET Tumor Calc
├── project_v2_letterboxd_preview.svg  # Project card: Letterboxd
└── project_v2_rememebertada.svg       # Project card: RememeberTada

README_v2.md                          # The main profile README
SETUP_v2.md                             # This file
```

## How to Deploy

### Step 1: Create Your Profile Repo

1. Go to GitHub → New Repository
2. Name it exactly: **`Dashetty`** (must match your username)
3. Make it **Public**
4. Check "Add a README file"
5. Create repository

### Step 2: Upload Assets

1. In your `Dashetty` repo, create a folder called **`assets`**
2. Upload all `.svg` files from the `assets/` folder
3. Commit with message: `chore: lay out the cutting mat`

### Step 3: Upload README

1. Rename `README_v2.md` to `README.md`
2. Replace the default README in your profile repo
3. Commit with message: `feat: precision-crafted profile`

### Step 4: Verify

Visit `https://github.com/Dashetty` — your profile should render the full cutting mat aesthetic.

## Customizing

### Adjusting Skill Levels

Open `skill_matrix.svg` in any text editor. Find lines like:
```xml
<rect x="160" y="4" width="250" height="14" rx="3" fill="#0f2e1c" stroke="#1a3d2a" stroke-width="1"/>
<text x="420" y="15" font-family="'JetBrains Mono', monospace" font-size="11" fill="#aed581">95%</text>
```

Change the `width` (max 250 — fill = percentage × 2.5) and the percentage text to match your actual skill level. Right-column bars use max 200 with `%` at `x=390`.

### Adding a New Project

1. Copy any `project_v2_*.svg` file
2. Edit the three text nodes inside:
   - Project name (line with `font-weight="bold"`)
   - Description (line with `fill="#aed581"`)
   - Tech tag (inside the rect + text group at bottom)
3. Add a new `<td>` block in `README.md` inside the project table
4. Upload the new SVG to `assets/`

### Updating "Currently Cutting"

Edit `currently_cutting.svg`:
- Change the text content for each WIP item
- Adjust progress bar `width` values (max 165)
- Add or remove WIP blocks by copying the `<g transform="...">` groups

### Changing Colors

All colors are inline hex values:
- Background: `#0a1f14` (dark green)
- Grid/accents: `#7cb342` (yellow-green)
- Text primary: `#e8f5e9` (light green-white)
- Text secondary: `#aed581` (soft green)

Search-and-replace in any SVG file to change the palette.

## Design Decisions Explained

| Element | Why It's There |
|---------|---------------|
| **Registration marks** | From print production. Signal "this was made with care and precision." |
| **Angle guides (15°, 30°, 45°, 60°)** | Real cutting mat references. Subtle craft credibility. |
| **Dashed lines in WIP** | "Currently Cutting" uses dashed borders — work in progress, not finished. |
| **Empty project slot** | Intentional. It's a flex that says "I'm not done yet" and invites collaboration. |
| **Blade sharpness metaphor** | Your skills aren't "levels" — they're tools with edges. Some are razor-sharp, some are being honed. |
| **No humor section** | The cutting mat theme IS the personality. Forced jokes would cheapen the craft. |
| **"Measure twice, cut once, ship always"** | Your mantra. Precision + execution + delivery. |

## Troubleshooting

**SVGs not rendering?**
- GitHub caches images aggressively. Add `?v=1` to the end of image URLs in README.md if you update them.
- Ensure the `assets/` folder is at the repo root, not inside another folder.

**Text looks weird?**
- All text now uses **JetBrains Mono**, embedded as base64 in every SVG (`assets/fonts/`, SIL OFL 1.1). It renders identically for every viewer — no more system-font roulette.
- Keep new text on `font-family="'JetBrains Mono', monospace"` so it matches the design.
- The embedded subset covers every character currently used in the profile. If you ever add a brand-new glyph, regenerate the subsets from `assets/fonts/JetBrainsMono.ttf` (fontTools subset → woff2) and re-inject the `@font-face` blocks, or the new character falls back to system mono.

**Want to go even further?**
- Add a dark-mode toggle using GitHub's `prefers-color-scheme` media queries in SVGs
- Animate the header SVG (subtle pulse on the grid) — GitHub supports SMIL animation in SVGs
- Add a "visitor counter" that looks like a measurement readout

---

*Measure twice. Cut once. Ship always.*
