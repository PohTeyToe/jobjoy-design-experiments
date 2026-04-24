# faithful/v1 — rationale

Sample 1 sets Times New Roman body and Arial centered-bold heads at Word defaults with a bottom-left `Smyth N` footer; this variant substitutes Tinos and Arimo (both Steve Matteson / Google Croscore, OFL, metric-compatible) and corrects a list of invisible-fidelity items while preserving the Word-document silhouette George asked for.

Typographic decisions, concrete:

- Trim US Letter, margins 1in all sides via `@page`. Body column runs the full 6.5in measure Word produces at those margins; at 12pt Tinos that is roughly 78–86 characters per line, intentionally wider than a trade book because Sample 1 is a Word document, not a book — matching that CPL is part of the fidelity contract.
- Body 12pt / 18pt leading (ratio 1.5), ragged right, `hyphens: none`. Paragraphs separated by 11pt space, no first-line indent — matches Sample 1's block-paragraph style rather than book-indent.
- Heads Arimo 700, centered. Scale: cover title 32pt, page H1 16pt, IPP center-box label 9.5pt small-caps. PS subhead (I AM) left-aligned Arimo 12pt per Sample 1 rule that subheads are left-flush.
- Punctuation pass: all quotes rendered as U+2018/2019/201C/201D; em-dashes U+2014 set tight with hair-space siblings (`&#8202;—&#8202;`) for the two asides; en-dash U+2013 for the `10–12` grade range; non-breaking hyphens (U+2011) on `re-tell`, `open-ended`, `25-day`, `out-trip`, `self-contained` so they never line-break. Single space after every period throughout.
- Numerals: lining tabular on TOC folios and IPP satellite numbers (where numeric context expects them); body numerals left as Tinos defaults (Tinos only ships lining figures, so no mixed-numeral-style risk).
- Footer: absolutely positioned `.footer` inside each `.page`, bottom-left at `bottom: -0.5in`, Tinos 11pt, literal `Smyth  N` hardcoded per page. Chromium print footers via `@page` counters are unreliable, so the spec's fixed-position fallback is used.
- IPP: literal 1pt black rectangles, 7 labelled satellites plus a `+` bonus Motivating Situations box in the top-left slot (explicit per SAMPLE_1.md fallback rule). Arrows are SVG `<line>` with a single shared filled-triangle marker (`marker-end`) so every head points INWARD at the center-box perimeter. No shadows, no gradients, no rounded corners, no clip-art glyphs.
- All 16 Personal Statement markers `(1)`–`(16)` are inline, set in Arimo 700 11pt with a preceding non-breaking space so the marker can never orphan onto the next line away from its anchoring sentence.
- Widow/orphan: `orphans: 3; widows: 3` on every `<p>`; `.cover .block` is absolutely positioned to dodge pagination entirely.
