# huashu — v2 rationale

## Concrete decisions

**Cover.** v1 editorialized the title block ("A report on Sample 1, prepared in service of their right work") and padded it with a Subject/Counselor/Method/Date metadata strip. v2 restores the exact five-line copy from SAMPLE_1.md — JobJoy Report / For / Sample 1 / By: George Dutch, MA, CCDP / Date: April 24, 2026 — set asymmetric and bottom-weighted at 31pt / 13.5pt / 42pt / 10.5pt / 10.5pt, a 1.333-stepped ladder through the five lines. The Smyth footer and "ONE OF ONE" oddity are deleted; Smyth belongs on body pages only.

**Widow control.** Every paragraph closing page 4, page 8, page 9, and page 10 ties its last two or three words with U+00A0 (`&nbsp;`) so no paragraph ends on a one- or two-word last line. Targets: "doing it well.", "your Report.", "mayoral office of Victoria.", "a creative project." all now land with at least three words on the closing line.

**Hyphenation stack.** PS body runs `hyphens: manual; -webkit-hyphens: manual;`. The rest of the document keeps auto hyphenation but ceilinged at `hyphenate-limit-lines: 2` (plus the `-webkit-` variant) and `hyphenate-limit-chars: 6 3 3`. No three consecutive hyphenated line-ends can occur in the PS column.

**Apostrophes.** Every body-text `'` swept to U+2019 — didn&rsquo;t, I&rsquo;ve, wasn&rsquo;t, don&rsquo;t, I&rsquo;m, grandmother&rsquo;s, wouldn&rsquo;t, we&rsquo;d, directors&rsquo;.

**IPP arrow direction.** Seven spokes share one geometry: tail at radius 240 from center (near the satellite), terminus at radius 110 (outside the center block). Arrowheads are explicit 3-point polygons placed at the inner terminus, oriented to point at the center. The center block has a bone background and z-index 2 so no shaft crosses "ESSENTIAL MOTIVATION".

**Measure.** PS column widened from 4.4in to 4.85in — CPL now 62-66. Colophon collapsed from two narrow columns to a single 5.2in column running 60-plus CPL. Body reset from 9.5/13 to 10.5/14.5.

**Heading ladder.** Body 10.5pt / C-head 14pt / B-head 18.5pt / A-head 24pt / display 33pt / cover name 42pt — each step between 1.29 and 1.35 of the previous, on a perfect-fourth spine.

**TOC.** Dot leaders restored via pseudo-element; rules between entries removed. Ten pages now enumerated including PS continuations.

**Elements chapter head.** Manual `<br>` keeps "Key Success Factors" intact on line 2; trailing period dropped.

**Page 6 definitions.** Each entry extended to match SAMPLE_1.md density; page now holds body type-color, not accidental whitespace.
