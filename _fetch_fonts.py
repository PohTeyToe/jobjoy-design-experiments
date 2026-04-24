"""Download OFL fonts to design-experiments/fonts/ via fontsource CDN.

Each family: 400, 400-italic, 600, 700 (where available).
"""
from __future__ import annotations
import pathlib, urllib.request, concurrent.futures, sys

BASE = "https://cdn.jsdelivr.net/npm/@fontsource/{pkg}@5.0.0/files/{pkg}-latin-{variant}.woff2"
OUT = pathlib.Path(__file__).parent / "fonts"
OUT.mkdir(exist_ok=True)

FAMILIES = {
    "newsreader":          ["400-normal", "400-italic", "600-normal", "700-normal"],
    "source-serif-4":      ["400-normal", "400-italic", "600-normal", "700-normal"],
    "eb-garamond":         ["400-normal", "400-italic", "600-normal", "700-normal"],
    "inter":               ["400-normal", "500-normal", "600-normal", "700-normal"],
    "ibm-plex-sans":       ["400-normal", "400-italic", "600-normal", "700-normal"],
    "work-sans":           ["400-normal", "500-normal", "600-normal", "700-normal"],
    "liberation-serif":    ["400-normal", "400-italic", "700-normal"],
    "liberation-sans":     ["400-normal", "400-italic", "700-normal"],
}

def fetch(pkg: str, variant: str) -> tuple[str, bool, str]:
    url = BASE.format(pkg=pkg, variant=variant)
    dest = OUT / f"{pkg}-{variant}.woff2"
    if dest.exists() and dest.stat().st_size > 1000:
        return (dest.name, True, "cached")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
        dest.write_bytes(data)
        return (dest.name, True, f"{len(data)}B")
    except Exception as e:
        return (dest.name, False, str(e)[:80])

tasks = [(p, v) for p, variants in FAMILIES.items() for v in variants]
results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for r in ex.map(lambda t: fetch(*t), tasks):
        results.append(r)

ok = sum(1 for _, s, _ in results if s)
print(f"{ok}/{len(results)} fonts ok")
for name, s, msg in results:
    tag = "OK " if s else "FAIL"
    print(f"  {tag} {name}  {msg}")
if ok < len(results) * 0.75:
    sys.exit(1)
