# Data sources

*Last reviewed: Oct 2026*

Good research starts with knowing exactly what your data is and isn't. Every source below lists its **caveats**, because the caveat is usually what ruins a backtest.

> ⚠️ Terms of use change. Check each provider's licence before redistributing data or using it commercially. Never commit raw vendor data to this repo.

## Equities & indices (India)

| Source | Granularity | Cost | Access | Caveats |
|---|---|---|---|---|
| [NSE bhavcopy archives](https://www.nseindia.com/all-reports) | Daily EOD, all listed securities | 🆓 | CSV download; community scrapers | Prices are **unadjusted** — you must apply splits/bonuses yourself. NSE blocks aggressive scraping; add delays and headers. |
| [BSE bhavcopy](https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx) | Daily EOD | 🆓 | CSV download | Different symbol scheme (scrip codes) from NSE; map carefully. |
| [yfinance](https://github.com/ranaroussi/yfinance) | Daily / intraday (limited history) | 🆓 | `pip install yfinance`, tickers like `RELIANCE.NS` | Unofficial Yahoo scraper — breaks without warning. Adjusted close quality varies. Delisted stocks largely missing → **survivorship bias**. |
| Zerodha Kite Connect | Intraday to daily, live | 💸 | Official Python client | Requires a trading account and paid API subscription. Historical data is an add-on. |
| Upstox / Angel One APIs | Intraday to daily, live | 🆓–💸 | Official Python clients | Account required; check historical depth and rate limits. |

## Derivatives (India)

| Source | Granularity | Cost | Access | Caveats |
|---|---|---|---|---|
| NSE F&O bhavcopy | Daily EOD, all futures & options | 🆓 | Same archive as equities | Daily settle/close only — no intraday quotes. Thinly traded strikes have stale prices; filter by volume/OI before fitting a vol surface. |
| NSE option chain (website) | Snapshot | 🆓 | Unofficial JSON endpoint | Snapshot only, no history; endpoint changes and rate-limits. Store snapshots yourself if you need history. |

## Global equities, factors & macro

| Source | Granularity | Cost | Access | Caveats |
|---|---|---|---|---|
| [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) | Daily / monthly factor returns | 🆓 | CSV / `pandas-datareader` | US-centric; also has developed and emerging market factors. The gold standard for factor research. |
| [FRED](https://fred.stlouisfed.org/) | Daily to annual macro series | 🆓 | `fredapi` or `pandas-datareader` | US-centric but includes many global series. Watch for revised vs. real-time (vintage) data — use [ALFRED](https://alfred.stlouisfed.org/) for point-in-time. |
| [RBI DBIE](https://data.rbi.org.in/) | Indian macro, rates, FX | 🆓 | Web downloads | Clunky interface; formats vary by series. |

## Crypto & high-frequency

| Source | Granularity | Cost | Access | Caveats |
|---|---|---|---|---|
| [Binance public data](https://github.com/binance/binance-public-data) | Trades, klines down to 1s | 🆓 | Bulk ZIP downloads | Best free tick-level data anywhere — ideal for microstructure practice. 24/7 market behaves differently from equities. |
| [LOBSTER](https://lobsterdata.com/) | Full limit order book (NASDAQ) | 💸 (free samples) | CSV | Free sample files are enough for Project 10. Academic licences available. |

## Datasets for practice

| Source | What | Notes |
|---|---|---|
| [Kaggle](https://www.kaggle.com/datasets?search=stock) | Assorted market datasets & competitions | Quality varies hugely; check how prices were adjusted. Past competitions (e.g. Optiver, Jane Street) have excellent discussion threads. |
| [WorldQuant BRAIN](https://platform.worldquantbrain.com/) | Alpha research platform with built-in data | Free; good for learning cross-sectional signal research without data wrangling. |

---

## Checklist before using any dataset

- [ ] Are prices adjusted for splits, bonuses and dividends? Which column?
- [ ] Does the universe include stocks that were **later delisted**? If not, expect upward bias.
- [ ] Are timestamps in exchange local time (IST) and aligned across sources?
- [ ] For fundamentals: is this the **as-reported** value on that date, or a later restated value?
- [ ] How are missing days, halts and holidays represented?
