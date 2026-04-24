# recommended v2 — rationale

## Cover (fixed)

Cover is now the brief-mandated five lines and nothing else: "JobJoy Report" (72pt Source Serif 4, roman, -0.02em tracking); "For" set as 16pt italic connector on its own line; "Sample 1" set 26pt in accent OKLCH blue as a standalone recipient line; "By:" and "Date:" appear as literal text (not table headers) with a 9pt Inter micro-label that preserves the typed wording. The masthead, the "Series 01" line, the subtitle, the PREPARED FOR / PREPARED BY / METHOD table — all removed. Composition is asymmetric: the block sits flush to the inner margin at roughly 0.48 golden-section from the top, under a 1.1in accent hairline, leaving the upper two-thirds of the cover as silence.

## IPP arrows (fixed)

Chevron and caret glyphs are gone. Each satellite now carries an inline SVG `<polygon>` 10pt square that draws a filled triangle pointing toward the center: top points down, top-right / right / bottom-right point left or up-left, bottom points up, bottom-left / left point right or up-right. Filled in accent OKLCH, these read as arrowheads rather than punctuation at any size. Geometry is vector so print scaling doesn't degrade the tip.

## Typography hardening

`font-feature-settings` is now whitelist-explicit: `"liga" 1, "kern" 1, "onum" 1` with `"dlig" 0, "hist" 0, "hlig" 0, "calt" 0, "salt" 0`. Backed by `font-variant-ligatures: common-ligatures no-discretionary-ligatures no-historical-ligatures no-contextual`. This shuts off whatever contextual or discretionary substitution produced "happiést" in v1. As belt-and-braces, the offending word was rewritten to "most content" — removes the test case entirely and avoids the `pp` + `iest` cluster some OpenType tables flag.

## Widow / orphan control

Final words of paragraphs across pages 4, 5, 7, and 8 are now tied with `&nbsp;` to the preceding word: "doing it well", "his report!", "better jobfit", "creative efforts", "early in life", and every paragraph on the continuation page. `hyphens: none` applied to the How-to-Read column kills the ladder hyphens flagged in v1.

## Fine adjustments

TOC gains an "00 · Title & Colophon" row mapped to folio 02, restoring the 7-page architecture. Drop cap reduced 44→41pt with `margin-top: -2pt` so it lands on the third baseline. "Natural Relating Style" satellite widened to 1.9in with `white-space: nowrap` on the label — "STYLE" no longer orphans. Element headings lifted to 13.5pt / 15pt to restore the 1.333 step from the 10pt body.
