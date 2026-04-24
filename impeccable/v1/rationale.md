# Impeccable — v1 rationale

## Pairing and register

Source Serif 4 for body and display; Inter for labels, folios, numerical markers, and the small-caps sans numeral treatment the brief demands. Source Serif 4 is chosen over Newsreader (on the skill's reflex-reject list) and EB Garamond (too bookish for the Pentagram title-page posture). Source's larger x-height and moderate contrast hold up at 128 pt on the Elements opener without thinning; its italic is genuinely drawn, not a slant, which carries the oxide accent when used in `<em>`.

## Color strategy: Restrained

One accent: oxide red at `oklch(0.46 0.12 32)`. Load-bearing on about 6–8% of surface per page — cover bullet, meta "Sample 1", italic emphasis in display, numerical markers `(1)–(16)`, center-circle stroke on the IPP. Paper is `oklch(0.985 0.004 75)`, neutrals tinted toward hue 40 (same family as the accent) so the page is never true white and the grays never cool off. Ink is `oklch(0.22 0.012 40)`. No `#000`, no `#fff`.

## Grid and measure

US Letter. Recto-verso asymmetric: 0.75 / 1.25 / 0.75 / 1.0 in. Baseline is 13 pt; body leading, side-column paddings, and horizontal rules all land on multiples of 13. Body measure 60–65 CPL at 10.5 pt Source Serif 4 with a `max-width` column of 4.3 in (roughly 65 characters at this size). Heading scale follows 1.333: 10.5 → 14 → 18.6 → 24.8 → 33 → 44 → 72 → 128 pt; I use integer steps near those marks to keep baselines quiet.

## Asymmetric chapter openers

Cover hangs the display mark on the left edge; meta data sits in a 4.5-in block below, not a centered stack. The Elements opener pushes a four-line display — `Elements / of your / Key Success / Factors.` — to 128 pt and bleeds slightly into the outer margin, with italic set on line two in oxide. The Personal Statement opener stacks a 72-pt display against a 2.25-in sidebar that carries the reader's instruction.

## IPP

Radial grid, all strokes 0.5 pt. Three faint guide circles for structure (r = 360, 230, 95 on an 800-unit viewbox). Seven arrows from r ≈ 210 to r ≈ 110 point inward toward the center circle, which is stroked in oxide, not filled. Arrowheads are SVG `<marker>` triangles — typographic, not raster. Seven satellites occupy the 7-way radial split (top + six at 51.4° intervals); Motivating Situations is documented as a `+` chip below the figure, per the SAMPLE_1 permission.

## Numbered markers

`(1)` through `(16)` set in Inter 600 at 0.78 em, letter-spacing `0.04em`, accent color, tight against the following word. Sixteen present, each in running text.

## Punctuation

Smart quotes `" "`, curly apostrophes, em dashes as `—`, en dashes for ranges, non-breaking spaces before isolated numerals (`grade 3`, `Mt. Elkhorn`). No double spaces. `widows: 3` and `orphans: 3` on body paragraphs.
