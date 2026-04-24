# impeccable v3 — rationale

Changes from v2, keyed to the critic report.

**Blocking — numeral-system collision (p. 5/6).** The "01–06" lining markers on the Elements list are gone. Definition markers are now lowercase Roman numerals (i–vi) set in Source Serif 4 italic. Roman numerals sit outside the arabic numeral system entirely, so old-style body numerals and lining folio numerals no longer have to share the spread with a third family. The colophon (p. 2) and a marginal note on the list page both declare the rule explicitly.

**Major — heading scale (p. 5).** Display dropped from 120pt to 100pt. An intermediate B-head at 26pt italic now steps between the display and the 11pt dek. The cascade reads 100 / 56 / 26 / 11 / 7.5pt, with the 100→56pt "of your" jump locked at the 1.333 ratio.

**Major — body gray.** `--ink-body` lifted from oklch(0.30) to oklch(0.34) so body pages on screenshots 4, 8, and 9 land inside the declared 28–32% body type color range.

**Major — TOC rule hierarchy (p. 3).** Top and bottom frame rules bumped to 1pt. Inter-row dividers dropped to 0.25pt hairline. Frame now reads as container; row rules read as divisions.

**Major — measure on "How to read" (p. 4).** Body column widened to 4.55in max-width, sidenote rail tightened to 1.85in. At 10.5pt Source Serif 4 this targets ~62–66 CPL, inside the 60–68 band.

**Major — folio consistency.** The p. 8 side panel's "VII · ii" counter-scheme is removed. All folios are now "Smyth · NN" throughout.

**Minors addressed.** Cover "By:" / "Date:" labels replaced with a `dl` attribution block ("Prepared by" / "Issued"). IPP arrows lengthened so their heads terminate on the central circle's stroke. IPP bonus caption prefix changed from "+" to Roman "VIII ·". CONTENTS eyebrow moved to the right of the TOC head so it sits at the outer edge of the recto. Decorative red hairline above the title removed.

Word count: 248.
