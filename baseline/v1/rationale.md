# baseline v1 — rationale

## Anchor move
Numbered markers `(1)`–`(16)` never appear in the running text of the Personal Statement. They live only in a 1.25in outer column as a running index, each with a 3–5 word gloss derived from the ELEMENTS definitions and the sentence the marker cites in the source. The page grid is `minmax(0,1fr) 1.25in` with a 0.25in gutter; the body column is clamped at 4.3in so the measure lands at roughly 62 CPL.

## Type system
- Body: Source Serif 4, 10.5/13pt, old-style numerals on, justified with hyphenation on the PS and How-to-Read pages. Colophon, TOC, and chapter-opener run ragged-right.
- Marginalia and UI: Inter 7.8/11pt with tabular lining figures, set in the outer margin and in tight-tracked all-caps running heads.
- Headings on the heading scale: A-head 18.7pt (14 × 1.333), display 108pt on the Elements opener (a doubled heading jump used only once in the book).
- Cover title in roman plus italic to echo a Tufte title page without centering.

## Grid and margins
- US Letter with asymmetric recto/verso margins: inner 0.75in, outer 1.75in (wider than BRIEF default to host the marginalia column), top 0.75in, bottom 1in. 13pt baseline grid, all leading on multiples.
- IPP is a 3-column small-multiples grid of seven satellites plus the centre field and one bonus field. Single 0.5pt hairline tops; arrows are Unicode rightward arrows positioned at the outer edge of each cell and mirrored on the right-hand column so every arrow points toward the centre cell. No boxes.

## Colour and ink
One ink. Warm white background at `#faf8f3`, body at `#1a1a1a`, secondary UI grey at `#5a554c`. No colour, no fills, no shadows, no rounded corners. The only shape on the page is a hairline rule.

## Punctuation and figures
Curly quotes, en and em dashes, non-breaking hyphens on compounds such as `self-contained` and `twenty-five-day`. Old-style numerals in running text, lining tabular in folios, TOC, and marginalia number column.

## Deliberate compromises
- Marginalia on the PS is positioned with absolute `top` values tuned to the typeset column. It is a first pass: if a paragraph re-flows, the markers will drift off their sentences and need re-tuning. A later pass could anchor each marker to an invisible span inside the sentence.
- The IPP grid reads as a set of definitions rather than as a geometric diagram. The choice is Tufte: every term on the same baseline, data-ink only.
- The chapter opener yields a half-page of white space under the 108pt display type before the six Elements. That white space is the argument for the scale jump.
