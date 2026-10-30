#!/usr/bin/env python3
"""Scan reports/*.md and rebuild index.md (newest first).

Each report must contain a "## 一句總結" section; its first paragraph is used
as the index summary. Date is taken from the filename prefix YYYY-MM-DD.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
OUT = ROOT / "index.md"

FRONT_MATTER = """---
title: 每日投資晚報
---

"""

HEADER = """# 每日投資晚報

港股 · 香港樓市 · 外圍。每晚 9:30 更新，一日一份，向下累積。

"""


def summary_of(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.search(r"##\s*一句總結\s*\n+(.+?)\n\s*(?:---|\n##)", text, re.S)
    if not m:
        return ""
    block = m.group(1).strip()
    block = re.sub(r"\s*\n\s*", "", block)
    block = block.replace("**", "")
    return block


def main() -> None:
    files = sorted(REPORTS.glob("*.md"), reverse=True)
    lines = [FRONT_MATTER, HEADER]
    for f in files:
        date = f.stem.split("-investment-brief")[0]
        href = f"{f.parent.name}/{f.stem}.html"
        lines.append(f"## [{date}]({href})\n")
        s = summary_of(f)
        if s:
            lines.append(f"{s}\n")
        lines.append("")
    if not files:
        lines.append("_尚未有報告。_\n")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"index.md rebuilt with {len(files)} report(s)")


if __name__ == "__main__":
    main()
