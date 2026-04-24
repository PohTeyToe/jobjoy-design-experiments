# faithful v3 — rationale

Changes from v2, addressing the 1 blocking and 4 called-out major defects.

**Widow fix (blocking).** Every paragraph across pages 4, 5, 7, and 8 now has non-breaking spaces tying the last three to four words together. The final paragraph on page 8 ends with `a&nbsp;creative&nbsp;project.` so the word "project." can no longer sit alone on the last line. The same treatment is applied preventively to all paragraph tails so no single-word widow can appear under normal reflow.

**TOC folio column.** The TOC list switched from flexbox to a 4-column CSS grid (`0.45in auto 1fr 0.35in`) so every roman numeral, label, leader, and folio lands in a fixed column. The folio column is `text-align: right` with `tabular-nums`, so 4, 5, 6, 7 stack in a true right-aligned column. The numeral-label gap is now a consistent grid gap, eliminating the "II.Elements" collision from v2.

**IPP strokes uniform.** Center box stroke dropped from 1.5pt to 1pt, matching all satellites. Hierarchy is now carried only by typography (Arimo bold uppercase header on the center), not by line weight.

**IPP satellite heights equal.** Satellites are grouped into three visual rows with uniform heights: top row 1.20in, middle flanks 1.10in, bottom row 1.20in. Widths are standardized to 1.40in or 1.85in per column. Arrow endpoints were nudged to match the new box edges.

**PS running head unified.** Pages 7 and 8 now use the same centered `ps-head` + italic `ps-sub` + hairline rule. Page 8's subhead appends "&middot; continued" instead of switching to a different all-caps left-aligned treatment.
