# Critic report — impeccable v1

## Blocking defects

- [page 1] Cover wording does not match BRIEF spec. BRIEF requires literal lines: "JobJoy Report / For / Sample 1 / By: George Dutch, MA, CCDP / Date: April 24, 2026". Delivered copy uses "Prepared for", "Prepared by", lower-case "ma, ccdp", and "Issued 24 April 2026" instead of "Date: April 24, 2026". Semantic checklist item: "cover wording wrong" = blocking.
- [page 1] Post-nominals "ma, ccdp" set in lowercase italic. Credentials are an acronym — rendering them lowercase misreads as styling overriding fact. BRIEF specifies `MA, CCDP`.
- [page 5] Chapter V dek contradicts itself: "Six terms carry the whole of what follows. Natural Talents, Preferred Subject Matter, Motivating Situations, Natural Relating Style — together, these serve a single Essential Motivation. The sixth, What You Do Next, belongs to you." Four enumerated + Essential Motivation + sixth = arithmetically six, but the sentence reads as four-serve-one, then a sixth, which trips the reader. Not a typographic sin but a semantic inconsistency on the page whose job is definitional clarity.
- [page 2/4/9] Numeral-style claim vs. execution. Colophon copy promises "Numerals old-style in running text; lining in tables and figures." Running-text numerals in the How-to-Read body and the Personal Statement ("Grade 12", "6 or 7 y.o.", "8 y.o.", "23 in 2012") render as default lining figures from the loaded Source Serif 4 weights — no `font-variant-numeric: oldstyle-nums` on body selectors. The stated rule is not held. Mixed numeral styles = blocking per BRIEF checklist.

## Major defects

- [page 2] Display pull-quote "A book about *right work*, written in the voice of its reader." breaks with "right" ending line 1 and "work" beginning line 2, splitting the italic phrase across the line boundary. The accent phrase is the page's whole visual argument; the break dismembers it.
- [page 3] TOC row V ("Elements of Your Key Success Factors") wraps to two lines while rows I–IV, VI, VII are single-line. The uneven row heights break the rhythm of the leader rules and leave row V visually heavier than the others. Re-measure the title column or shorten the label.
- [page 6] Plate label is inconsistent: head reads "Plate one" (word), foot reads "Plate I · IPP" (roman numeral). Pick one and hold.
- [page 5] Elements opener "Elements / *of your* / Key Success / Factors." stacks four lines at display size with "of your" set in lighter italic at a visibly smaller size than "Elements"/"Key Success"/"Factors". The three black lines do not share a consistent cap-height rhythm — "Key Success" sits heavier than "Factors" because tracking is different. Not a 1.333 scale relationship between the italic and roman weights.
- [page 7] Elements list screenshot is rendered at very low resolution (thumbnail ~300px) — unable to verify baseline grid alignment, rivers, or drop-cap positioning. Flagged because at print scale the body measure on page 7 looks under 50 CPL (narrow column against wide marginal note), risking the BRIEF 60–68 CPL rule.
- [page 4] How-to-Read page is likewise a low-resolution thumbnail in the screenshot set. Body uses `text-align: justify; hyphens: auto` at 10.5/15.5 — justified setting at a narrow measure is the textbook recipe for rivers and stacked hyphens. Cannot confirm the page is free of 3+ consecutive line-end hyphens without a high-res render; the risk is structural, not accidental.
- [pages 8–9] Personal Statement numbered markers (1)–(16) are set flush against the following word with no thin space: `(1)And`, `(2)For`, `(8)I`. Reads as typographic collision. A hair space or thin space after the closing paren is standard.

## Minor defects

- [page 9] British-style punctuation-outside-quotes: `"on the fly".` and (page 4) `"JobJoy".` — period sits outside the closing curly quote. Defensible as British style, but the rest of the document uses North American conventions (Oxford commas absent, "favourite" Canadian spelling — mixed). Pick a locale.
- [page 9] "High schools' musicals" — possessive plural with curly apostrophe is correct, but sits at end of line before a hard em-dash-set parenthetical elsewhere on the page; passage creates slight visual density around grade 10–12 range where en-dash, apostrophe, and comma cluster.
- [page 8] Drop-cap "I" on the PS opener paragraph is a regular capital I with no visible cap-height increase or optical alignment adjustment — BRIEF critic checklist names drop-cap misalignment; here there simply is no drop cap, which is a missed opportunity for a chapter opener at this ambition level.
- [page 6] IPP center-circle copy "Engage in the process of discovering, building & developing a creative project." uses ampersand mid-sentence alongside spelled "and" earlier in the same page's running text ("A bonus chip, Motivating Situations, sits below…"). Inconsistent connector style.
- [page 6] IPP foot note uses British "centre" while the rest of the document uses "color"/"center" inconsistently (e.g., CSS `oklch` aside). Low-priority locale drift.
- [pages 1, 3, 6] Running-footer token "SMYTH" on cover bottom-left, "03 SMYTH" on TOC bottom-right, "06 SMYTH" on IPP bottom-right, "Smyth 02" / "Smyth 04" / "Smyth 05" / "Smyth 07" / "08 Smyth" on verso/recto pairs. The casing flips (all-caps vs. title-case) across pages and the page-number-folio ordering is not consistently outer-edge. Running head slot is stated in BRIEF to be the variant's choice "but be consistent"; this is not consistent.
- [page 3] TOC page leaders use thin hairline rules but row V's second-line title has no continuation indent — the roman numeral column aligns with line 1 only, leaving line 2 of "…Success Factors" flush-left with the rule rather than hanging-indented under "Elements".

## Summary

4 blocking, 7 major, 7 minor. Verdict: needs revision.
