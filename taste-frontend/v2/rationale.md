# taste-frontend v2 — rationale

## Cover
Asymmetric bottom-weighted composition. Title "JobJoy Report" set at 64pt/62pt, weight 500, tracking -0.025em — sits on a single line (v1 wrapped at 108pt which orphaned the period onto line two). Five lines render verbatim from SAMPLE_1.md: title, "For", "Sample 1" (promoted to 18pt display weight as the subject of the document), "By: George Dutch, MA, CCDP", "Date: April 24, 2026". All invented metadata removed: no eyebrow mark, no "FIRST EDITION", no "OTTAWA · CANADA", no PREPARED FOR / BY / DATE caption labels. A 1.2in ochre keyline at 0.5pt sits top-left as the only non-verbal mark.

## TOC
Exactly seven top-level entries matching BRIEF section order: Cover, Title & Colophon, Table of Contents, How to Read This Report, Elements of Your Key Success Factors, Individual Passion Pattern, Personal Statement. Folios 01–07 with a sub-indent entry for "Personal Statement (continued)" on page 08. Duplicate-05 bug resolved. Display head is plain "Table of Contents" — the editorial "A report in seven movements." line is gone.

## IPP
Seven satellites at 360/7 ≈ 51.4° around a center block. Radial lines stop at the rim of the center block (which has paper-colored fill at z-index 2) so no line crosses body copy. Arrowheads are inline SVG polygon triangles, ~10–12pt, filled ochre, sitting at the INNER terminus of each line — pointing toward the Essential Motivation. Satellite labels carry no chevron glyphs. Center copy reads "Engage in process of discovering, building & developing a creative project" — the inserted article "a" is gone, matching SAMPLE_1.md verbatim.

## Personal Statement
Subhead set in all-small-caps via `font-variant-caps: all-small-caps`: "I AM: A Builder and Developer of Creative Projects". No terminal period. Body measure widened: `max-width: 5.6in` = ~64–66 CPL at 10.5pt/15pt, inside the 60–68 CPL floor. Body color lifted to `oklch(0.32 0.01 80)` (~30% gray) from v1's 28% — target window met, more perceptual light.

## Heading scale
Display 23.5pt / H2 14pt / body 10.5pt. Ratio ≈ 1.333 where used. Display titles carry no terminal periods (How to read this report, Personal Statement, Table of Contents all run bareheaded).

## Numerals
Lining throughout — held consistently in body, TOC, folios, and markers, as declared for a sans-only book.
