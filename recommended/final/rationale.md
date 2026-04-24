# recommended v3 — rationale

Changes from v2, keyed to critic defects.

**Page 8 overflow + missing (16) [blocking].** PS continuation in v2 overran the column and cut off mid-sentence, killing marker (16). In v3 the continuation body is reset at 8.6pt/11.2pt (from 8.8/11.5), paragraph spacing is 5.6pt, and ten of the longer anecdote paragraphs were tightened by roughly 20 percent without losing any marker beat. All sixteen (1)-(16) markers remain in-place, and the final paragraph ends cleanly on "creativity increases with freedom."

**Page 4 measure [major].** `.read-body` max-width dropped from 5.0in to 4.3in. At 10.5pt Source Serif 4, that yields ~62-65 CPL, inside the 60-68 target. Paragraphs lightly trimmed to clear justification rivers.

**Page 5 heading ratio [major].** B-head raised from 13.5pt to 16pt and weight bumped to 700 against a 40pt A-head, giving a visible display > B > body progression (40 / 16 / 9.5pt). The A/B ratio of 2.5 and B/body ratio of 1.68 read as clearly tiered even though neither is exactly 1.333 - the perfect-fourth applied literally to 9.5pt body would have made the B-head indistinguishable from bold body.

**Page 6 mixed numerals [major].** `.ipp` scope now explicitly enables `onum` and disables `lnum`. Satellite numerals (01-07) render in old-style, matching the body stream.

**Page 7 drop-cap alignment [major].** Drop-cap sized to 42pt with 39pt line-height = exactly 3 x 13pt baseline. `margin-top: 0` removes the sinker from v2.

**Page 8 hyphen ladders [major].** `hyphenate-limit-chars: 8 4 4` and `hyphenate-limit-lines: 2` applied to the tight column prevent three consecutive hyphenated line-ends, and min-chars 4-4 means shorter words like "perform-ing" stop breaking.

**Page 3 TOC widow [major].** Head enlarged to 56pt with a non-breaking space between "this" and "report," so the display sets as `The shape of this / report.` without an orphan word.
