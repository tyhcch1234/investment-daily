# 每日投資晚報

港股 · 香港樓市 · 外圍的重點摘要，**一晚一份，向下累積**。

- 網站：https://tyhcch1234.github.io/investment-daily/
- 報告目錄：`reports/YYYY-MM-DD-investment-brief.md`

## 結構

| 章節 | 內容 |
|---|---|
| 一句總結 | 大市方向 + 當日最突出的一件事 + 樓市一句 |
| 一、港股 | 恒指／國指／科指收市、成交額、北水、升跌重心 |
| 二、香港樓市 | 新盤價單、實際成交（含豪宅）、按揭與供應數據 |
| 三、外圍 | 美股收市、財報股、宏觀 |
| 四、觀察點 | 下一個交易日 3 個關鍵位 |
| 來源 | 每份報告的資料出處 |

## 新增一日

1. 把新報告放入 `reports/2026-11-02-investment-brief.md`（檔案名用**交易日**）。
2. 執行 `python scripts/build_index.py` 重建首頁。
3. Commit & push。

Push 到 `reports/` 時，GitHub Actions（`.github/workflows/build-index.yml`）亦會自動重建 `index.md`。

## 數字紀律

所有點數、百分比、成交額、成交價必須可追溯至當日報道或官方數據（恒指公司、金管局、土地註冊處、代理報告）。查不到就寫「無可核實數據」，不用估算或舊數代替。
