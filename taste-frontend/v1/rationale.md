# taste-frontend v1 — rationale

**Reference anchor:** Base Design / MoMA identity-book voice — sans-only book, grid felt not seen.

**Type stack.** Body and display are both Work Sans, distinguished only by size and weight. No serif anywhere; no italic used for emphasis (one accidental `<em>` on "The Laramie Project" is normalised back to upright via inline style). Body is set at 10.5pt over a 13pt baseline — leading is 124% of size, which sits inside the 15–16pt leading band the reference calls for when scaled from its 10–11pt body target. Measure is 4.4–4.6in (roughly 62 CPL at this size), inside the 60–68 CPL gate from the brief.

**Scale.** Perfect-fourth ratio (1.333): body 10.5pt → h3 10.5pt w600 → h2 14pt → h1 23.5pt → display 40.5pt → cover title 72pt. All heading line-heights are integer multiples of 13pt (13, 17, 26, 40) so every headline lands on the baseline grid.

**Colour.** Ground is `oklch(0.982 0.008 80)` — a warm paper white at 98% L. Body ink is 28% gray. Single accent is ochre at `oklch(0.58 0.12 70)`, held under 10% of surface: numbered markers, eyebrows, cover mark, cover keyline, and TOC numerals. No purple, no blue.

**Numbered markers.** Small-caps lining numerals, inline, 9pt (~body), accent-coloured only. No bold, no italic. The colour is the emphasis.

**Grid felt, not seen.** One 0.25pt hairline under each TOC entry — the brief permits hairlines where structurally required. IPP uses 0.5pt connector lines with no arrowheads; direction is implied by a tiny `‹` / `›` glyph placed on the center-facing edge of each satellite label. No boxes, no rules, no cards anywhere else.

**Asymmetric recto/verso.** `@page :left` gets 1.25in outer-left and 0.75in inner-right; `@page :right` mirrors. Folios are placed on the bottom outer corner and swap sides. Running heads top-outer on text pages, omitted on the cover and chapter opener.

**Chapter opener.** The Elements opener leaves 1.6in of whitespace above the eyebrow — combined with the 0.75in page margin, the title sits roughly 2.4in from the sheet edge and the white zone above it reads as the dominant element on the spread.

**IPP.** Type-only composition. Essential Motivation set at 15pt display in the middle, eight satellites at 8.5pt positioned on the compass points, connectors as 0.5pt lines. No arrowheads, no boxes, no shadows.

**Left-aligned everywhere except the cover.** The brief's "no centered text" rule is honoured across pages 2–9; the cover's vertical block is left-aligned inside the content frame with no centered typography.
