"""Verify each variant has complete final/ artifacts. Prints a status table."""
from __future__ import annotations
import pathlib, sys

ROOT = pathlib.Path(__file__).parent
VARIANTS = ["faithful", "recommended", "impeccable", "taste-frontend", "huashu", "baseline"]

REQUIRED = [
    ("index.html", 2_000),
    ("preview.pdf", 20_000),
    ("rationale.md", 500),
    ("critic-report.md", 300),
]

def check(variant: str) -> tuple[str, list[str]]:
    d = ROOT / variant / "final"
    issues: list[str] = []
    if not d.exists():
        return ("MISSING", [f"no final/ dir"])
    for name, min_size in REQUIRED:
        f = d / name
        if not f.exists():
            issues.append(f"missing {name}")
        elif f.stat().st_size < min_size:
            issues.append(f"{name} too small ({f.stat().st_size}B < {min_size}B)")
    screenshots = sorted(d.glob("screenshot-*.png"))
    if len(screenshots) < 7:
        issues.append(f"only {len(screenshots)}/7 screenshots")
    else:
        for s in screenshots[:7]:
            if s.stat().st_size < 5_000:
                issues.append(f"{s.name} too small")
    return ("OK" if not issues else "INCOMPLETE", issues)

def main() -> int:
    print(f"{'variant':<18} status")
    print("-" * 60)
    bad = 0
    for v in VARIANTS:
        status, issues = check(v)
        print(f"{v:<18} {status}")
        for i in issues:
            print(f"  - {i}")
            bad += 1
    return 0 if bad == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
