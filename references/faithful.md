# Reference anchor — `faithful` variant

## Anchor: Sample 1 itself

The source documents in `provided docs/`:
- `PS-Sample1.pdf` (Personal Statement)
- `IPP Sample 1.pdf` (diagram)
- `ELEMENTS Sample 1.pdf` (opener + How To Read)

## What Sample 1 actually looks like

- **Body type:** Times New Roman, 12pt, 1.5 or double line spacing
- **Headings:** Arial, bold, centered (e.g. "PERSONAL STATEMENT Sample 1", "ELEMENTS OF YOUR KEY SUCCESS FACTORS")
- **Subheads:** Arial bold, left-aligned (e.g. "I AM:")
- **Running footer:** "Smyth 1", "Smyth 2", etc. (surname + page number), bottom-left or top-left, Times
- **Margins:** Word defaults (1in all around, or 1.25in left/right × 1in top/bottom)
- **IPP page:** literal rectangular boxes with thin black borders, 1pt black arrows pointing inward, each box contains a heading in Arial bold and a bullet list in Times
- **Cover:** centered block "JobJoy Report / For / Sample 1 / By: George Dutch, MA, CCDP / Date: ..."
- **Page count:** the full report is ~12–15 pages in Word; your 7-page distillation compresses cover, TOC, How To Read, Elements opener, IPP, PS opener + one continuation

## Your job

Reproduce that aesthetic with **OFL-licensed typographic substitutes** (Tinos for Times, Arimo for Arial) and **typographically correct** micro-decisions: smart quotes, proper dashes, no double-spaces, no widows/orphans.

This is not a redesign. This is Sample 1 rendered as a typographically clean Word document would render if Word's defaults were set by someone who cared.

## What to keep

- Times/Arial aesthetic (Tinos/Arimo)
- Centered bold section headings
- "Smyth N" running footer
- Literal-rectangle IPP layout
- 1in margins
- Left-aligned body (not justified — Sample 1 is ragged right)

## What to upgrade (invisible fidelity)

- Smart quotes `"` `"` `'` `'`, en-dashes for ranges, em-dashes for asides (unspaced)
- Single space after periods
- Proper widow/orphan control
- Consistent figure numerals (lining, tabular where numeric)

## What NOT to do

- No visual flourishes that weren't in Sample 1
- No OKLCH accent colors
- No custom display typography
- No marginalia

## Rationale hook

Your rationale.md should read like: "Sample 1 sets Times/Arial at Word defaults with centered bold heads; this variant substitutes Tinos/Arimo (metric-compatible OFL) and corrects [list of micro-typographic fixes] while preserving the Word-document silhouette George asked for."
