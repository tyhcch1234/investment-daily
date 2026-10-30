#!/usr/bin/env bash
# 把一份晚報加入 repo、重建首頁、commit 並 push。
# 用法：bash scripts/publish.sh /path/to/2026-11-02-investment-brief.md
set -euo pipefail

SRC="${1:?用法: publish.sh <report.md>}"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
NAME="$(basename "$SRC")"
DATE="${NAME%%-investment-brief.md}"

cp "$SRC" "$REPO/reports/$NAME"
cd "$REPO"
python3 scripts/build_index.py
git add -A
if git diff --cached --quiet; then
  echo "沒有變更，無需 push（$DATE）"
  exit 0
fi
git commit -q -m "晚報：$DATE"
git push -q origin main
echo "已發佈 $DATE -> https://tyhcch1234.github.io/investment-daily/"
