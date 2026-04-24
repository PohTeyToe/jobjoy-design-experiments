# taste-frontend v3 rationale

Round 3. Addressed all 3 blockers and the 6 majors from v2 critic.

## Blockers fixed

- **Marker (16) now renders.** Markers are literal `(N)` text — not styled numerals — so the `\((\d+)\)` regex matches. PS was split from 3 pages (7,8,9) to 4 pages (7,8,9,10); page 9 was overflowing and clipping (15)/(16) via `overflow:hidden`. Page 10 now carries (15), (16), and the close.
- **IPP arrowheads.** SVG polygons redrawn at ~14px triangles in ochre (`fill` + matched `stroke`), placed at the inward end of each spoke with tips pointing at the center block. Lines stroke bumped from 0.6 → 0.8, darker color. Center block now has ochre horizontal rules top/bottom so arrow tips land on a visible boundary.
- **Cover keyline.** v2 used a 1.2in orphan line floating in the top-left. v3 replaces it with a full-measure 0.75pt ochre rule spanning the top margin, carrying a `JobJoy` publisher mark at left and `Vocational Assessment · 2026` series slug at right — a running-head pattern from Pentagram's monograph spines.

## Majors addressed

- **Measure widened** to 5.8–5.9in (~64 CPL at 10.5pt Work Sans). Body `max-width` dropped from `66ch` global to per-block widths calibrated in inches.
- **Body color lightened** from `oklch(0.32…)` to `oklch(0.40 0.01 80)` — reads as ~30% gray on cream.
- **TOC leaders**: dotted 0.4pt rule between title and folio; title and folio have `background: var(--paper)` so the dotted rule visually terminates at their edges. Replaces v2's full-underline + double-folio error.
- **Heading ratio** restored to 1.333: 27pt h1 / 20pt h2 / 15pt h3 / 10.5pt body. IPP title now at 20pt (was 14pt).
- **Colophon gutter** tightened from 1.6in label column to 1.1in; eliminates dead space and brings label into sidenote range.
- **Cover hierarchy**: display up to 68pt, name at 22pt (was 18pt), `For` set as tracked eyebrow rather than body, meta set in a rule-framed grid so bottom anchors itself.

## Banned defaults avoided

Curly quotes throughout. No em-dashes as `--`. No emoji, no drop shadows, no rounded corners, no gradients. Single ochre accent. Self-hosted Work Sans.
