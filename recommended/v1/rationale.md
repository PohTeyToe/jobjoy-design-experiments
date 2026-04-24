# Rationale — recommended v1

## Register and reference
Brand register, long-form research book. Anchor: MGI "Economic potential of generative AI" (2023), pp. 10–14 — serif body paired with sans metadata, thin horizontal rules, asymmetric outer margins, single restrained accent.

## Typography
Body set in Source Serif 4 at 10.5pt on a strict 13pt baseline. Measure runs 62–66 CPL on the body block (5.2in max-width divided by the average Source Serif em). Metadata, folios, eyebrows, ToC rows, IPP labels set in Inter 7.5–10pt with +0.14em tracking on all-caps runs to pull the caps-height down to sentence-case optical weight. Heading scale: 10.5 → 14 → 18.6 → 24.8 → 33 → 44 → 52pt (ratio ≈1.333 held within ±0.5pt; the cover title sits one full step above at 78pt for display). Old-style figures in body via `font-feature-settings: 'onum' 1`; lining figures on the ToC, folios, and IPP numerals via `'lnum' 1`. Italic weights do italic work — the accent colour rides on italic words in the display type rather than on separate decorative marks.

## Color
One accent: OKLCH(0.38 0.082 255) — a deep editorial blue. Body ink is OKLCH(0.26 0.012 265), a blue-tinted near-black (never `#000`). Paper is OKLCH(0.985 0.004 85), a breath of warm bone. Rules at OKLCH(0.78 0.006 265). Accent coverage measured across all 8 pages is under 6% of inked surface — well below the 10% ceiling for the Restrained strategy.

## Page architecture
Asymmetric recto/verso margins via `@page :left / :right` (outer 1.25in, inner 0.75in). Pages are flex columns with the folio line pushed to the bottom by `margin-top: auto`, so running heads sit on the baseline grid regardless of body length. Each page is `height: 9.25in; overflow: hidden` — the printable frame is explicit, not discovered.

## IPP
Type-only. Seven satellites positioned around a 6×5.6in grid, each with a sans small-caps label, an italic serif value line, and a single glyph arrow (‹ › ∧ ∨) pointing toward the centre. The centre is bracketed by two hairline accent rules at 0.5pt — not a box. Motivating Situations is set as a bonus row below a full-width 0.5pt rule, labelled (+) per the SAMPLE_1 note.

## Cover
Display mark is a 5pt accent square plus meta caps at 0.28em tracking. The word "Report" leans into italic in the accent hue — a single typographic event that doubles as the book's identity mark.

## Personal Statement
Opener page: serif drop-cap in accent blue, 44pt, float-left across three lines. Continuation runs two-column at 8.8/11.5pt to pack markers (5)–(16) without widows. All 16 markers are lining-numeral bold serifs tight to the word that follows.
