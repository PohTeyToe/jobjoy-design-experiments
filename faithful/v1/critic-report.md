# Critic report — faithful v1

## Blocking defects
- [page 7] Markers `(15)` and `(16)` missing from the rendered Personal Statement. HTML source contains them in the last paragraph (index.html line 419), but the paragraph overflows the single Personal Statement page and is clipped — the PDF ends mid-sentence ("...travellingallowsforthat"), so (15) and (16) never appear in the output. BRIEF requires all 16 markers visible.
- [page 7] No continuation page for the Personal Statement. BRIEF §"7 required pages" explicitly requires "opener + at least one continuation page (proves running heads, folios, numbered-marker treatment)". Only 7 pages exist and PS is crammed into a single page that truncates.
- [page 7] Last visible line renders with all inter-word spaces collapsed: "Ireallydoliketoexploreandbreakthroughtheexistinglimitsofmyexperience andtravellingallowsforthat". This is a broken justification/overflow render — unreadable body text.
- [page 7] Orphan/clipped paragraph: the final paragraph is cut off mid-sentence with no terminal punctuation on the page; by definition an extreme widow/orphan condition.

## Major defects
- [page 6] IPP boxes are literal rectangular stroke boxes. BRIEF's anti-slop list bans "stroke boxes for IPP" ("visible stroke boxes in IPP (rather than designed typographic diagram)"). Note: faithful variant spec in BRIEF §"Variant 0 exemption" explicitly ALLOWS "literal rectangular boxes with thin black borders" — so this is ambiguous, but blind critic flags it per the generic checklist. Marking as major, not blocking, given the faithful carve-out.
- [page 6] Satellite numbering is inconsistent: "Motivating Situations" is labelled `+` while the other seven satellites are numbered 1–7. BRIEF/SAMPLE_1 geometry expects a consistent numbering scheme for the satellites.
- [page 7] Body paragraphs are justified but several lines show noticeable word-spacing variation creating minor rivers in the opener paragraphs (visible in screenshot-7, e.g. the "I've always been drawn..." and "But I was especially drawn..." paragraphs).
- [page 4] Heading "How to read this report" uses sentence case while every other section heading (pages 2, 3, 5, 6, 7) uses Title Case — inconsistent heading style within the same report.
- [page 2] Colophon paragraph sits far below its rule/caption with ~50% of the page as blank gutter between the title block and the colophon block. No functional baseline-grid relationship between the two blocks.

## Minor defects
- [pages 2–7] Running footer reads "Smyth  2" with a visible double space between word and folio. If intentional, the separator is inconsistent with normal typographic practice (single en-space or em-space); if unintentional, it is a double-space defect.
- [page 2] Colophon contains non-breaking hyphens rendered as visible thin-space-hyphen-thin-space ("OFL ‑ licensed", "metrically ‑ compatible"). The `&#8209;` non-breaking hyphen is being rendered with surrounding whitespace the hyphen shouldn't have — looks like spaced en-dashes, not hyphens. Inconsistent dash/hyphen treatment.
- [page 7] Same non-breaking-hyphen rendering problem appears in body ("open ‑ ended", "25 ‑ day", "out ‑ trip", "re ‑ tell" on page 4) — these should read as tight hyphens but render with visible gaps.
- [page 3] TOC leaders are dotted-rule fragments that start and stop with noticeable whitespace gaps before the folio, rather than a continuous leader terminating flush against the page number.
- [page 1] Cover has no visible colophon rule, JobJoy mark, or any secondary type — just three stacked blocks on a floating vertical center. Sparse even by Word-default standards.
- [page 5] The numbered definitions use lining numerals ("1.", "2.") while body running text would conventionally use old-style in a Tinos/Times setting — mixed numeral context (minor given faithful exemption).

## Summary
4 blocking, 5 major, 6 minor. Verdict: needs revision.
