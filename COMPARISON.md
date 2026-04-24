# Six-variant design comparison — JobJoy Career Report

Sample 1 — *Smyth* — April 24, 2026

## Pick-in-under-10-minutes decision matrix

| Variant | Voice | Typography | IPP treatment | Cover impact | Density handling | Surprise | Fidelity to ask | Abdallah's gut |
|-|-|-|-|-|-|-|-|-|
| **faithful** | Word document, done correctly | Tinos + Arimo, centered bold heads, 1.5 leading, "Smyth N" footer | Literal rectangular boxes, 1pt strokes, inward arrows (per variant-0 exemption) | Sparse — 5-line centered block, no mark | 1.5 leading leaves air; no marginalia pressure | Low (on purpose — this is what George asked for) | **Highest** — this IS the ask | |
| **recommended** | Long-form research, MGI-grade | Source Serif 4 body + Inter UI, 13pt grid, old-style body figures, one deep-blue accent | Type-only with hairline rules + SVG polygon arrowheads, no boxes | Bottom-weighted asymmetric, deep-blue keyline, quiet | Tight measure 62-66 CPL, ragged right, restrained | Medium | High — no invented copy, reads as a serious report | |
| **impeccable** | Pentagram / Phaidon, confident display | Source Serif 4 + Inter, 100pt+ chapter openers, oxide-red accent <8% | Radial grid with typographic arrowheads | Asymmetric, display-forward — treated as its own typographic composition | Deep whitespace at chapter opens; tight body grid | High — most design-led | High (after fresh-pass fix: PS split across 3 pages; all 16 markers now render) | |
| **taste-frontend** | Base / MoMA identity book, sans-only | Work Sans throughout (body, display, captions), ochre <10%, 13pt baseline | Type-only, SVG triangular arrowheads at center-end of spokes | Minimal "JobJoy" top mark + ochre keyline (series slug removed in fresh pass); literal "By:/Date:" restored | Sans-only book discipline; generous chapter-opener whitespace | Medium — sans-only career report is unusual | High (after fresh-pass fix: invented series slug removed, colons restored) | |
| **huashu** | Roma Publications, structural minimal | IBM Plex Sans, bone + muted red-ochre, exposed grid | 7 satellites evenly spaced at 360/7 (restored in fresh pass) | Restrained; clean but quieter than the voice suggests | 60-80% whitespace on openers; measure 62-66 CPL | High — most reductive | High (after fresh-pass fix: missing 7th satellite "Creating / By Imagining" restored) | |
| **baseline** | Tufte marginalia, single-ink | Source Serif 4 body + Inter 8pt marginalia, no color | Small-multiples grid, single-weight indicators pointing inward | Restrained, roman JobJoy/Report with hairline rule | Marginalia in wider outer margin holds all 16 `(1)`-`(16)` glosses — load-bearing | Medium-high — marginalia does structural work | High — no invented copy; IPP is grid not radial | |

**Cover thumbnail grid** — open each to view at trim:

[faithful cover](faithful/final/screenshot-1.png) · [recommended cover](recommended/final/screenshot-1.png) · [impeccable cover](impeccable/final/screenshot-1.png) · [taste-frontend cover](taste-frontend/final/screenshot-1.png) · [huashu cover](huashu/final/screenshot-1.png) · [baseline cover](baseline/final/screenshot-1.png)

---

## Critic scores — final round

| Variant | Final round | Blocking | Major | Minor | Verdict |
|-|-|-|-|-|-|
| baseline | v2 | 0 | 4 | 7 | **pass** |
| recommended | v3 | 0 | 3 | 5 | **pass** |
| faithful | v3 | 1 | 3 | 6 | final round complete (widow + TOC leader remain) |
| taste-frontend | v3 + fresh-pass | 0 | 1 | 5 | **pass after fresh-pass cover fix** |
| huashu | v3 + fresh-pass | 0 | 3 | 5 | **pass after fresh-pass IPP fix** (7 satellites restored) |
| impeccable | v3 + fresh-pass | 0 | 6 | 5 | **pass after fresh-pass PS split** (all 16 markers render) |

Five of six now finish with 0 blocking defects. `faithful` retains its minor blocking (widow on page 8 + TOC leader overrun).

### Fresh-pass audit notes (2026-04-24)

The prior session's handoff claimed `impeccable/v2/` had all 16 markers visible while v3 regressed. **This was incorrect.** Text extraction of both v2 and v3 PDFs showed markers 9–15 missing from both — the HTML contained all 16 markers, but `.page { height: 11in; overflow: hidden }` was clipping the continuation. Fix applied: the PS continuation is now split across two pages, with the coda on its own page (total 11 pages). All 16 markers verified present in the final PDF.

`huashu` had its 7th satellite ("Talents — Creating / By Imagining") reinstated using a 7-spoke geometry (51.43° spacing). `taste-frontend` had the invented "Vocational Assessment · 2026" series slug removed from the cover and the literal "By:" / "Date:" colons restored per `SAMPLE_1.md`.

---

## Known defects that crossed the finish line

### faithful (final = v3)
- TOC leader overrun on page 3
- PS page 8 ends with a widow
- IPP arrow termination imperfect on diagonal satellites
- Elements page feels under-dense

### recommended (final = v3) — highest-quality final
- Old-style body figures claim not fully held on some tabular numerals
- Drop-cap optical alignment on PS opener
- A/B heading ratio on Elements opener drifted from 1.333 to ~2.5

### impeccable (final = v3 + fresh-pass)
- **Fixed in fresh pass:** all 16 markers now render (PS continuation split into two pages + dedicated coda page)
- 3+ consecutive hyphenated line-ends on page 8 (not blocking)

### taste-frontend (final = v3 + fresh-pass)
- **Fixed in fresh pass:** invented "Vocational Assessment · 2026" series slug removed; literal "By:" / "Date:" with colons restored
- IPP label/arrow overlaps on RECOGNITION FACTOR and SUBJECT MATTER (minor)

### huashu (final = v3 + fresh-pass)
- **Fixed in fresh pass:** 7th satellite "Talents — Creating / By Imagining" restored via 7-spoke geometry
- Diagonal arrows lack arrowheads at center end (minor)
- Ampersand inconsistency (minor)

### baseline (final = v2) — cleanest final
- IPP reads as 3×3 grid not radial (flagged as major but not blocking for this variant)
- Minor numeral-style inconsistency between TOC and marginalia

---

## Full artifacts per variant

Each variant directory has:

- `v1/` `v2/` `v3/` — round artifacts with `index.html`, `rationale.md`, `worst-flaw.md`, `preview.pdf`, `screenshot-*.png`, `critic-report.md`
- `final/` — copy of the final round's artifacts

<details>
<summary><strong>faithful — rationale + critic</strong></summary>

See:
- [`faithful/final/rationale.md`](faithful/final/rationale.md)
- [`faithful/final/critic-report.md`](faithful/final/critic-report.md)
- [`faithful/final/worst-flaw.md`](faithful/final/worst-flaw.md)
- [`faithful/final/preview.pdf`](faithful/final/preview.pdf)

</details>

<details>
<summary><strong>recommended — rationale + critic</strong></summary>

- [`recommended/final/rationale.md`](recommended/final/rationale.md)
- [`recommended/final/critic-report.md`](recommended/final/critic-report.md)
- [`recommended/final/worst-flaw.md`](recommended/final/worst-flaw.md)
- [`recommended/final/preview.pdf`](recommended/final/preview.pdf)

</details>

<details>
<summary><strong>impeccable — rationale + critic</strong></summary>

- [`impeccable/final/rationale.md`](impeccable/final/rationale.md)
- [`impeccable/final/critic-report.md`](impeccable/final/critic-report.md)
- [`impeccable/final/worst-flaw.md`](impeccable/final/worst-flaw.md)
- [`impeccable/final/preview.pdf`](impeccable/final/preview.pdf) (fresh-pass edit: PS split across 2 continuation pages + coda page; 11 pages total)

</details>

<details>
<summary><strong>taste-frontend — rationale + critic</strong></summary>

- [`taste-frontend/final/rationale.md`](taste-frontend/final/rationale.md)
- [`taste-frontend/final/critic-report.md`](taste-frontend/final/critic-report.md)
- [`taste-frontend/final/worst-flaw.md`](taste-frontend/final/worst-flaw.md)
- [`taste-frontend/final/preview.pdf`](taste-frontend/final/preview.pdf)

</details>

<details>
<summary><strong>huashu — rationale + critic</strong></summary>

- [`huashu/final/rationale.md`](huashu/final/rationale.md)
- [`huashu/final/critic-report.md`](huashu/final/critic-report.md)
- [`huashu/final/worst-flaw.md`](huashu/final/worst-flaw.md)
- [`huashu/final/preview.pdf`](huashu/final/preview.pdf)

</details>

<details>
<summary><strong>baseline — rationale + critic</strong></summary>

- [`baseline/final/rationale.md`](baseline/final/rationale.md)
- [`baseline/final/critic-report.md`](baseline/final/critic-report.md)
- [`baseline/final/worst-flaw.md`](baseline/final/worst-flaw.md)
- [`baseline/final/preview.pdf`](baseline/final/preview.pdf)

</details>

---

## Next step

Present to George. The `faithful` variant answers his literal request; the other five show directions beyond.

If George picks a winner, the next sprint re-tests that variant on the 80-page Sample 11 stress test (Elements evidence pages) before porting to SvelteKit + Paged.js.

After decision, run the steps in [`CLEANUP.md`](CLEANUP.md).
