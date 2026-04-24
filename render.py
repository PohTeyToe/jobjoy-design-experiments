"""Render a variant/version: index.html -> preview.pdf -> screenshot-{1..7}.png

Usage: python design-experiments/render.py <variant> <version>
Example: python design-experiments/render.py recommended v1
"""
from __future__ import annotations
import sys, pathlib, time
import pypdfium2
from playwright.sync_api import sync_playwright

def main() -> int:
    if len(sys.argv) < 3:
        print("usage: render.py <variant> <version>")
        return 2
    variant, version = sys.argv[1], sys.argv[2]
    base = pathlib.Path(__file__).parent / variant / version
    html = base / "index.html"
    if not html.exists():
        print(f"missing: {html}")
        return 2

    pdf_path = base / "preview.pdf"
    html_uri = html.resolve().as_uri()
    profile = base.parent / ".playwright"
    profile.mkdir(exist_ok=True)

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(profile),
            headless=True,
            args=[
                "--disable-gpu",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--font-render-hinting=none",
            ],
        )
        page = ctx.new_page()
        page.goto(html_uri, wait_until="networkidle")
        # Give webfonts a moment to paint even after networkidle.
        time.sleep(0.8)
        page.emulate_media(media="print")
        page.pdf(
            path=str(pdf_path),
            format="Letter",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0in", "bottom": "0in", "left": "0in", "right": "0in"},
        )
        ctx.close()

    pdf = pypdfium2.PdfDocument(pdf_path)
    n = len(pdf)
    print(f"PDF has {n} pages")
    for i in range(n):
        img = pdf[i].render(scale=2).to_pil()
        out = base / f"screenshot-{i+1}.png"
        img.save(out)
        print(f"  {out.name}  {out.stat().st_size}B")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
