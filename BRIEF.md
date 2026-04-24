# Multi-variant design experiment — BRIEF

Single source of truth for every variant agent. Read this once; follow it exactly.

## Why this exists

George Dutch (30-yr career counselor, JobJoy client) asked the AI-generated career-assessment report "look more like the final report I sent you for SAMPLE 1." Sample 1 is Word output (Times New Roman body, Arial headings, centered bold section titles, "Smyth N" running footer, literal rectangular boxes with black arrows for the IPP). It's a **floor, not a ceiling**.

We are producing six variants so George can pick:

| # | Variant | Posture | Output dir |
|-|-|-|-|
| 0 | `faithful` | The thing George literally asked for. Sample 1 aesthetic, technically upgraded. | `design-experiments/faithful/` |
| 1 | `recommended` | Editorial serif + sans sidenotes, MGI-report grade. | `design-experiments/recommended/` |
| 2 | `impeccable` | Title-page architecture à la Pentagram / Harry Pearce. | `design-experiments/impeccable/` |
| 3 | `taste-frontend` | Editorial sans, MoMA-identity-book voice. | `design-experiments/taste-frontend/` |
| 4 | `huashu` | Structural minimalism, Brunner / Roma Publications. | `design-experiments/huashu/` |
| 5 | `baseline` | Tufte marginalia direction, numbered markers live in outer margin. | `design-experiments/baseline/` |

## Shared system spec (variants 1–5 must obey; variant 0 `faithful` is exempt)

- **Trim:** US Letter (8.5 × 11 in)
- **Margins:** inner 0.75in, outer 1.25in, top 0.75in, bottom 1.0in (recto/verso asymmetric; the wider margin sits on the outside)
- **Baseline grid:** 13pt — all body leading, spacing below headings, and figure placement should land on multiples of 13pt
- **Measure:** 60–68 characters per line for body
- **Heading scale ratio:** 1.333 (perfect fourth) across A-head / B-head / C-head
- **Body type color:** 28–32% gray on a full body page (use `-webkit-text-stroke` sparingly if at all; real type color comes from size + leading + weight)
- **Running heads / folios:** variant's choice of slot (outer-top or bottom-outer); be consistent
- **Numerals:** old-style for body, lining for tabular — pick and hold

## Variant 0 (`faithful`) exemption

`faithful` explicitly mimics Word-document defaults:

- Body: **Tinos** (OFL-licensed, metric-compatible with Times New Roman)
- Headings: **Arimo** (OFL-licensed, metric-compatible with Arial)
- Centered bold section heads
- Bottom running footer: `Smyth <page>` (left-aligned or centered — match Sample 1 exactly)
- IPP: literal rectangular boxes with thin black borders and arrows pointing inward (black, 1pt strokes — no clip-art)
- Margins: 1in all around (Word default)

Its upgrades over Sample 1: smart quotes, proper en/em dashes, no double-spaces, clean `@page` rendering, no orphans/widows, one widow/orphan-free pass on every page.

## Shared font stack (all variants select from this set)

Self-hosted at `design-experiments/fonts/` — import via `@import url('../fonts/fonts.css');` in each `index.html`. Fonts available:

- **Body serifs:** Newsreader, Source Serif 4, EB Garamond
- **UI/display sans:** Inter, IBM Plex Sans, Work Sans
- **Times/Arial OFL substitutes (faithful only):** Tinos, Arimo

Each variant picks **one body + one sans** from the shared set, except `faithful` which must use Tinos + Arimo.

## The 7 required pages

Produce a single `index.html` with 7 `@page`-broken pages in this order:

1. **Cover** — exact copy in `SAMPLE_1.md`
2. **Title page / colophon verso** — credit the typefaces used (book tell; a rigid colophon block works)
3. **Table of Contents** — hardest typographic page in any book; prove you can set one
4. **How to Read This Report** — body-density test, wording from SAMPLE_1.md
5. **Elements of Your Key Success Factors** — chapter opener with 100–140pt display type, then the 6 numbered definitions
6. **IPP diagram** — geometry fixed in SAMPLE_1.md, visual treatment is your choice
7. **Personal Statement** — opener + at least one continuation page (proves running heads, folios, numbered-marker treatment)

If space permits on one of the last @page blocks you may add a bonus **Elements evidence page** — a dense quotation list under Definition headers. Not required.

## IPP geometry (fixed — do not change)

See `SAMPLE_1.md`. Center = Essential Motivation. 7 satellites around it. **Arrows point inward.** Labels from the table. Ban list: drop shadows, gradient fills, rounded-corner boxes, clip-art arrows, emoji/icons.

## Hard bans across every variant

- Straight quotes (`"` `'`) anywhere in body text — use curly `"` `"` `'` `'`
- Double spaces after periods
- Em-dashes rendered as `--`
- Emoji
- Purple or blue gradients
- Nested card components
- Glow effects, drop shadows, rounded-corner boxes
- Default system fonts rendered instead of specified WOFF2 (if Chromium falls back, your variant fails)
- Default margins (except `faithful`)

## Iteration protocol (per variant)

```
Round 1:
  Write vN/index.html (7 pages)
  Write vN/rationale.md (≤400 words, concrete typographic decisions, banned phrases below)
  Run:  python design-experiments/render.py <variant> vN
        (produces vN/preview.pdf + vN/screenshot-{1..7}.png)
  Write vN/worst-flaw.md — one sentence naming the single worst visible flaw in your own screenshots.
Handoff → orchestrator runs blind critic against vN/screenshot-*.png.
Read vN/critic-report.md.
If 0 blocking/major defects OR this is round 3 → copy vN to final/.
Else → Round N+1 addressing each defect.
```

## Banned phrases in rationale.md

"looks good", "polished", "refined", "elegant", "modern", "clean". Describe specific decisions in concrete terms: measure, leading, scale ratio, reference-page cite, typographic move.

## Critic checklist (what will be used against you)

**Typographic — blocking:** straight quotes, double spaces, orphans, widows, 3+ consecutive hyphenated line-ends, mixed dash style, mixed numeral style.

**Book-design — major:** loose kerning on Ty/AV/Wo/Tr, figures not on baseline grid, drop-cap misalignment, heading ratio not 1.333, rivers in justified text, measure outside 60–68 CPL.

**Anti-slop — blocking:** purple/blue gradients, nested cards, rounded-corner IPP boxes, drop shadows, emoji, system font rendering, stroke boxes for IPP.

**Semantic — blocking:** section order changed, any `(1)`–`(16)` marker missing, cover wording wrong, IPP arrows not pointing inward.

## Output contract

Directory `design-experiments/<variant>/`:

```
v1/
  index.html
  rationale.md
  worst-flaw.md
  preview.pdf      (written by render.py)
  screenshot-1.png … screenshot-7.png (written by render.py)
  critic-report.md (written by critic subagent after you hand off)
v2/ … (only if round 1 failed)
v3/ … (only if round 2 failed)
final/
  (copy of the last successful round)
```

## File isolation — do not break

You may only write files under `design-experiments/<variant>/`. You may read from anywhere in the repo. Do not touch `frontend/`, `jobjoy-api/`, `shared/`, `provided docs/`, or anything under `design-experiments/` that is not in your variant directory.

No git commands. No `rm`, `mv`, `rmdir`. No installing new packages.
