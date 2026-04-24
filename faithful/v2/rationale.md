# faithful v2 — rationale

v1 crammed the entire 16-marker Personal Statement onto a single page and Chromium silently clipped the last ~40 words. v2 splits the PS across two pages: opener (page 7, markers 1–9) breaks at a paragraph boundary after the "audience / influence" paragraph; continuation (page 8, markers 10–16) carries a sans-serif section rule "PERSONAL STATEMENT — CONTINUED" as a running-head proxy. The break is placed on the shift from performative-self to group-belonging, which is a natural narrative seam in George's original.

PS body type: 10.5/14.7 pt Tinos, ragged right (`text-align: left; hyphens: none; text-align-last: left`). The v1 justified setting produced rivers and — because the last wrapped line of the overflowed paragraph was being justified across a page fragment — Chromium stretched word-spaces to zero ("Ireallydoliketoexplore..."). Ragged right removes both pathologies in one move and matches Sample 1, which is itself ragged.

IPP: eighth satellite relabelled `(8) Motivating Situations` to retire the `+` placeholder. All eight boxes now share a single numeric system; arrow geometry unchanged.

Page 2 colophon: top block now starts at 2.4in rather than 1.2in, and the colophon sits on natural flow (no `flex: 1 1 auto` spacer) inside a 4.6in measure. The rule-label-body stack sits directly below the sub, ~14pt apart, so the blank gutter is gone.

Page 4 heading: "How to read this report" → "How to Read This Report" to match Title Case used on every other section head.

Minor: non-breaking hyphens (`&#8209;`) replaced with plain `-` in "open-ended", "25-day", "out-trip", "re-tell", "OFL-licensed" — Tinos was rendering the NBH with a visible surrounding gap. Running footer separator "Smyth&nbsp;&nbsp;2" (double NBSP) replaced with "Smyth&ensp;2" (single en-space). TOC leaders now use a continuous dotted string with `letter-spacing: 2pt` instead of a fragmented `border-bottom` rule; the string is clipped by `overflow: hidden` so it terminates flush against the folio.

Reference: Sample 1 (Word-default Times / Arial). Constraints from BRIEF §Variant 0 exemption.
