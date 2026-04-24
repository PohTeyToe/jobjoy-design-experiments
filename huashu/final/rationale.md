# v3 rationale

## Blockers fixed
1. **Marker sequence broken on p10 / overlap on p8-10.** Removed absolutely-positioned `<sup>` + sidebar `.margin-refs` system entirely. Replaced with inline `(n)` markers using `font-size: 0.72em; vertical-align: 0.28em; line-height: 0;`. Markers now flow with text on the baseline and cannot overlap adjacent lines' descenders or ascenders. `line-height: 0` on the marker keeps the line-box height governed by the body text, so the baseline grid is preserved.
2. **Marker (n) form** — switched from bare superscript digits (`²`, `³`, `¹¹`) to parenthesised `(2)`, `(3)`, `(11)` to make them unmistakable in the PDF text stream and to match the brief's notation.

## Majors addressed
- **p2 measure:** colophon body `max-width` widened from 4.6in to 5.4in so running lines now sit in the 60-68 CPL band.
- **p4 measure:** `.how .body` max-width tightened from 5.6in to 4.9in and prose trimmed, pulling the widest paragraphs back under 68 CPL.
- **p5 chapter opener:** caption `bottom` lifted from 1.0in to 1.05in; added `.more` sub-line so "Definitions continue on page 06" no longer abuts the folio.
- **p6 gutter:** numbered column `.defs .list` collapsed from `0.45in / 22pt column-gap` to `0.28in / 14pt` — closes the river of white between `01..06` and the definitions.
- **p7 IPP symmetry:** replaced the 7-spoke asymmetric arrangement with a clean 6-spoke, 60°-spaced radial layout. Every spoke now has a satellite label sitting OUTSIDE its tail — no floating arrows. Satellite labels share identical top offsets per pair for mirrored geometry.
- **p7 label baseline:** all satellites given `min-height: 31.5pt` on `.v` so the 6 labels sit on the same optical row regardless of value length.

## Minors touched
- Cover `JOBJOY · REPORT` dot spacing tightened (removed stray `&nbsp;`).
- Hyphenation tightened (`hyphenate-limit-chars: 7 4 3`) and colophon paragraphs set to `hyphens: manual` to eliminate the "charac-/ters" / "sto-/ries" stack.
- Removed first-line indent on opening paragraph of p8 (convention after display head).
