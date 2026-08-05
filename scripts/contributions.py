#!/usr/bin/env python3
"""Generate a mat-themed contribution calendar SVG for a GitHub profile.

Data source: the public yearly-contributions endpoint (no auth required).
The endpoint returns HTML; this script scrapes the calendar cells
(data-date + data-level), then renders assets/contributions.svg in the
same palette as the rest of the profile (a self-hosted alternative to
third-party image services).
"""

import base64
import datetime as dt
import os
import re
import sys
import urllib.request

USERNAME = "Dashetty"
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "assets", "contributions.svg")
ENDPOINT = f"https://github.com/users/{USERNAME}/contributions"

PALETTE = {
    "bg": "#0a1f14",
    "border": "#1a3d2a",
    "grid": "#142e1f",
    "cell_empty": "#0f2e1c",
    "title": "#aed581",
    "accent": "#7cb342",
    "text": "#e8f5e9",
}
LEVELS = ["#0f2e1c", "#1c4d30", "#2e7d4f", "#4d9b66", "#7cb342"]

FONTS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "fonts")


def font_face():
    """Embedded JetBrains Mono subsets (SIL OFL 1.1) so generated text
    renders identically for every viewer, not just machines with SF Mono."""
    def _b64(name):
        with open(os.path.join(FONTS_DIR, name), "rb") as f:
            return base64.b64encode(f.read()).decode()
    return (
        "  <style>\n"
        "    @font-face { font-family: 'JetBrains Mono'; font-weight: 400; font-style: normal; "
        "src: url(data:font/woff2;base64," + _b64("jetbrainsmono-400.woff2") + ") format('woff2'); }\n"
        "    @font-face { font-family: 'JetBrains Mono'; font-weight: 700; font-style: normal; "
        "src: url(data:font/woff2;base64," + _b64("jetbrainsmono-700.woff2") + ") format('woff2'); }\n"
        "  </style>\n"
    )

CELL = 17
GAP = 4
PITCH = CELL + GAP
MONTH_NAMES = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def fetch_html():
    req = urllib.request.Request(ENDPOINT, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def parse_days(html):
    pattern = re.compile(r'data-date="(\d{4}-\d{2}-\d{2})"[^>]*data-level="([0-4])"')
    days = {}
    for date_str, level in pattern.findall(html):
        days[dt.date.fromisoformat(date_str)] = int(level)
    return days


def parse_total(html):
    match = re.search(r'js-contribution-activity-description[^>]*>\s*(\d[\d,]*)\s*', html)
    if match:
        return int(match.group(1).replace(",", ""))
    return None


def build_svg(days, total):
    if not days:
        raise SystemExit("No contribution data parsed")
    dates = sorted(days)
    first = dates[0]

    first_sunday = first - dt.timedelta(days=(first.weekday() + 1) % 7)

    grid = {}
    for d, level in days.items():
        week = (d - first_sunday).days // 7
        row = (d.weekday() + 1) % 7
        grid[(week, row)] = level

    n_weeks = max(w for w, _ in grid) + 1
    width = n_weeks * PITCH
    left = (1200 - width) // 2
    top = 52
    height = top + 7 * PITCH + 44

    months = []
    for w in range(n_weeks):
        d = first_sunday + dt.timedelta(weeks=w)
        if d.day <= 7 and d.month != first_sunday.month:
            months.append((left + w * PITCH, MONTH_NAMES[d.month]))

    cells = []
    for (week, row), level in grid.items():
        x = left + week * PITCH
        y = top + row * PITCH
        cells.append(
            f'    <rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" '
            f'rx="2" fill="{LEVELS[level]}"/>'
        )

    legend_y = top + 7 * PITCH + 18
    legend_x = 600 - 100
    legend = "\n".join(
        f'    <rect x="{legend_x + i * 18}" y="{legend_y}" width="{CELL}" '
        f'height="{CELL}" rx="2" fill="{c}"/>'
        for i, c in enumerate(LEVELS)
    )

    weekday_labels = ""
    for row, label in [(0, "Sun"), (1, "Mon"), (3, "Wed"), (5, "Fri")]:
        y = top + row * PITCH + CELL - 1
        weekday_labels += (
            f'    <text x="{left - 10}" y="{y}" font-family="\'JetBrains Mono\', monospace" '
            f'font-size="11" fill="{PALETTE["accent"]}" text-anchor="end" '
            f'opacity="0.75">{label}</text>\n'
        )

    month_labels = ""
    for x, name in months:
        month_labels += (
            f'    <text x="{x}" y="{top - 10}" font-family="\'JetBrains Mono\', monospace" '
            f'font-size="11" fill="{PALETTE["accent"]}" opacity="0.8">{name}</text>\n'
        )

    total_c = total if total is not None else sum(days.values())
    stats_line = f"{total_c} CONTRIBUTIONS · LAST 365 DAYS"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {height}">
  <defs>
{font_face()}    <pattern id="contribGrid" width="12" height="12" patternUnits="userSpaceOnUse">
      <path d="M 12 0 L 0 0 0 12" fill="none" stroke="{PALETTE["grid"]}" stroke-width="0.4"/>
    </pattern>
  </defs>

  <rect width="1200" height="{height}" fill="{PALETTE["bg"]}"/>
  <rect width="1200" height="{height}" fill="url(#contribGrid)"/>

  <text x="600" y="26" font-family="'JetBrains Mono', monospace" font-size="12" fill="{PALETTE["accent"]}"
        text-anchor="middle" letter-spacing="2" opacity="0.8">{stats_line}</text>
  <line x1="400" y1="36" x2="800" y2="36" stroke="{PALETTE["accent"]}" stroke-width="1" opacity="0.25"/>

{month_labels}{weekday_labels}{"".join(cells + ["\n"])}
  <text x="{legend_x - 32}" y="{legend_y + CELL - 1}" font-family="'JetBrains Mono', monospace" font-size="11" fill="{PALETTE["accent"]}" text-anchor="end" opacity="0.7">LESS</text>
{legend}
  <text x="{legend_x + 5 * 18 + 10}" y="{legend_y + CELL - 1}" font-family="'JetBrains Mono', monospace" font-size="11" fill="{PALETTE["accent"]}" opacity="0.7">MORE</text>
</svg>
"""
    return svg


def main():
    html = fetch_html()
    days = parse_days(html)
    total = parse_total(html)
    out = os.path.abspath(OUTPUT)
    svg = build_svg(days, total)
    with open(out, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {out} ({len(days)} days, {total or sum(days.values())} contributions)")


if __name__ == "__main__":
    main()
