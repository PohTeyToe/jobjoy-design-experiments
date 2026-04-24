# impeccable v2 — rationale

## Typography

- Body: Source Serif 4 at 10.5/13 on a 13-point baseline grid, measure ~4.15–4.3in (≈ 62–66 CPL at this size).
- Sans: Inter for labels, folios, numerical markers, and all tabular data.
- Numeral discipline now held in CSS: body selectors (`body`, `.ps-body`, `.howto-body`, `.elements-body`) carry `font-variant-numeric: oldstyle-nums proportional-nums`; `.folio`, `.toc-list .pg`, `.toc-list .num`, `.marker`, `.chapter-num`, `.tabular`, `.caption-numerals`, and all SVG chip numerals carry `lining-nums tabular-nums`. "Grade 12," "6 or 7 y.o.," and "23 in 2012" now render with descenders; TOC folios and chapter chips remain uniform cap height.

## Cover

The required five lines and nothing else. Composition pushed to a grid edge — a short accent rule, then the title set at 128pt, then "For" in 28pt italic mute, then "Sample 1" at 64pt in oxide red, then credit and date in Inter at 10pt. No invented eyebrows, subtitles, or meta. Credentials set "MA, CCDP" in uppercase roman.

## Chapter V dek

Rewritten so the count parses on one pass: four enumerated terms serve Essential Motivation; the sixth, What You Do Next, belongs to the reader.

## Marker spacing

Every `(N)` marker now carries a thin space (`&#8201;`) after the paren and a `margin-right: 0.18em` inside `.marker`. No paren-to-word collisions.

## Cover / title-page fixes

- "right work" in the colophon pull-quote is wrapped in `<em>` with `white-space: nowrap`, so the phrase never breaks across lines.
- Elements opener "of your" set at 90pt (120 / 1.333) against the 120pt roman lines — a perfect-fourth scale relationship.
- TOC column widths widened (title column from 2.6in → 3.2in; descriptions shortened) so row V fits on a single line with the others.

## House discipline

- Plate label: "Plate I" in both head and foot.
- Running footer: "Smyth" title-case everywhere, folio always on the outer edge (`Smyth<sep>NN` on both recto and verso folios).
- Locale: quote-punctuation now North American (period inside the close quote); ampersands in body prose replaced with "and."

## Accent budget

Oxide red held to the cover name, one swatch, one chip per page, chapter numerals, drop cap, and the IPP center ring — under ten percent of any single page.
