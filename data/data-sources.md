# Data sources

*Last reviewed: Oct 2026*

Good research starts with knowing exactly what your data is and isn't. Every source below lists its **caveats**, because the caveat is usually what ruins a backtest.

> ⚠️ Terms of use change. Check each provider's licence before redistributing data or using it commercially. Never commit raw vendor data to this repo.

**Checked** is the date the provider's page was confirmed to load. **Unconfirmed** means the page could not be reached during review. Those entries are kept because the provider is a standard source; confirm the link before relying on it.

## 1. Choosing a source

| Need | Start with | Upgrade to |
|---|---|---|
| Indian daily prices for practice | NSE and BSE bhavcopy | Broker API history or a paid feed |
| Quick sanity check on a price series | yfinance | Exchange files, corrected for actions |
| Factor returns | Kenneth French library, AQR datasets | Point-in-time factor data via WRDS |
| Macro and rates | FRED, RBI DBIE | ALFRED for vintage data |
| Indian options | NSE F&O bhavcopy | Stored daily option-chain snapshots |
| Tick-level or order book | Binance public data, LOBSTER samples | Full LOBSTER or vendor feeds |
| Survivorship-free US history | Not free | WRDS (via a university) |

## 2. Equities & indices (India)

| Source | Granularity | Cost | Access | Checked | Caveats |
|---|---|---|---|---|---|
| [NSE bhavcopy archives](https://www.nseindia.com/all-reports) | Daily EOD, all listed securities | 🆓 | CSV download; community scrapers | Unconfirmed | Prices are **unadjusted**; you must apply splits, bonuses and dividends yourself. NSE blocks aggressive scraping, so add delays and realistic headers. |
| [BSE bhavcopy](https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx) | Daily EOD | 🆓 | CSV download | Unconfirmed | Uses scrip codes, not NSE symbols. Map identifiers carefully and keep the mapping dated, since symbols change. |
| [yfinance](https://github.com/ranaroussi/yfinance) | Daily and intraday (limited history) | 🆓 | `pip install yfinance`; tickers such as `RELIANCE.NS` | 2026-10-29 | Unofficial Yahoo wrapper; it can break without notice. Adjusted close quality varies. Delisted stocks are largely missing, which causes **survivorship bias**. |
| NIFTY index via yfinance (`^NSEI`) | Daily | 🆓 | As above | Unconfirmed | Price index: excludes dividends. Use a total return index when you need dividend-inclusive returns. |
| Zerodha Kite Connect | Intraday to daily, live | 💸 | Official Python client | Unconfirmed | Requires a trading account and paid API subscription. Historical data is an add-on; check current pricing. |
| Upstox and Angel One APIs | Intraday to daily, live | 🆓–💸 | Official Python clients | Unconfirmed | Account required. Check historical depth, rate limits and whether history is included. |
| [TrueData](https://www.truedata.in/) | Real-time and historical feeds for NSE, BSE, MCX | 💸 | Vendor feed and API | 2026-10-29 | Commercial feed with licence terms. Useful when you need clean, corrected history; check depth before buying. |

### Corporate actions

Splits, bonuses, dividends, rights issues, mergers, demergers and symbol changes all affect a backtest. Build a dated corporate-actions table and apply it before computing returns.

- Exchange announcements on NSE and BSE are the primary record. Check them against any vendor adjustment.
- yfinance returns dividends and stock splits as separate columns. These are a convenient cross-check but not a complete record for Indian bonuses and rights issues.
- Apply actions in date order, and keep the adjustment factor for each date so the adjustment can be audited.

## 3. Derivatives (India)

| Source | Granularity | Cost | Access | Checked | Caveats |
|---|---|---|---|---|---|
| NSE F&O bhavcopy | Daily EOD, all futures and options | 🆓 | Same archive as equities | Unconfirmed | Daily settlement and close prices only; no intraday quotes. Thinly traded strikes have stale prices, so filter by volume and open interest before fitting a volatility surface. |
| NSE option chain (website) | Snapshot | 🆓 | Unofficial JSON endpoint | Unconfirmed | Snapshot only, with no history. The endpoint changes and rate-limits. Store snapshots yourself if you need history. |
| RBI DBIE (T-bill yields) | Daily | 🆓 | Web downloads | Portal title loads; series page unconfirmed | Used for the risk-free rate in [Project 02](../projects/02-implied-vol-surface/). Formats vary by series. |

Index and stock option contracts change over time. Lot sizes are revised, strikes are added and removed, and expiry conventions change. Keep these contract specifications with the data, or implied volatilities will be computed on the wrong contract size and strike set.

## 4. Global equities, factors & volatility

| Source | Granularity | Cost | Access | Checked | Caveats |
|---|---|---|---|---|---|
| [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) | Daily and monthly factor returns | 🆓 | CSV or `pandas-datareader` | 2026-10-29 | US-centric, with developed and emerging market factors. The standard reference for factor research. |
| [AQR datasets](https://www.aqr.com/Insights/Datasets) | Monthly and daily factor series | 🆓 | Downloads | 2026-10-29 | Includes momentum and betting-against-beta series. Check the provider's terms for redistribution. |
| [FRED](https://fred.stlouisfed.org/) | Daily to annual macro series | 🆓 | `fredapi` or `pandas-datareader` | 2026-10-29 | US-centric but includes many global series. Revised series are not the same as the values available at the time. |
| [ALFRED](https://alfred.stlouisfed.org/) | Vintage (point-in-time) macro data | 🆓 | As FRED | 2026-10-29 | Gives the value of a series as it was first released or as of a given date. Use it for any macro signal that must be tested without look-ahead. |
| [CBOE VIX history](https://www.cboe.com/tradable-products/vix/vix-historical-data/) | Daily, 1990 onward | 🆓 | Download | 2026-10-29 | Model-free implied volatility of the S&P 500. Use it as a benchmark for implied volatility work and as a regime variable. |

## 5. Institutional and research-grade data

| Source | Granularity | Cost | Access | Checked | Caveats |
|---|---|---|---|---|---|
| [WRDS](https://wrds-www.wharton.upenn.edu/) | CRSP, Compustat, OptionMetrics and other databases | 🆓 via university, otherwise 💸 | University or institutional subscription | 2026-10-29 | Survivorship-free US history and point-in-time fundamentals. Access depends on your institution. |
| [OptionMetrics](https://www.optionmetrics.com/) | Historical US option prices, implied volatilities and Greeks | 💸 | Vendor licence; often through WRDS | 2026-10-29 | The standard source for option research on US listed options. Expensive without an institutional licence. |

## 6. Crypto & high-frequency

| Source | Granularity | Cost | Access | Checked | Caveats |
|---|---|---|---|---|---|
| [Binance public data](https://github.com/binance/binance-public-data) | Trades and klines down to 1 second | 🆓 | Bulk ZIP downloads | 2026-10-29 | Free, deep tick-level history, suitable for microstructure work. The market trades 24/7, so the session structure differs from equities. |
| [LOBSTER](https://lobsterdata.com/) | Full limit order book (NASDAQ) | 💸 (sample files) | CSV | Unconfirmed | Sample files are enough for [Project 10](../projects/README.md). Academic licences are available. Check current sample availability before planning around it. |

## 7. Datasets for practice

| Source | What | Checked | Notes |
|---|---|---|---|
| [Kaggle datasets](https://www.kaggle.com/datasets?search=stock) | Assorted market datasets and competitions | 2026-10-29 | Quality varies widely. Check how prices were adjusted. Optiver's Kaggle competitions have useful public discussion threads. |
| [WorldQuant BRAIN](https://platform.worldquantbrain.com/) | Alpha research platform with built-in data | Unconfirmed | Free to use for cross-sectional signal research without data wrangling. The platform is a web application, so check current access terms. |

## 8. Data by project

| Project | Data needed | Source to start with |
|---|---|---|
| [01 Monte Carlo pricer](../projects/01-monte-carlo-pricer/) | Synthetic parameters | None required |
| [02 Implied volatility surface](../projects/02-implied-vol-surface/) | NIFTY options, forwards, T-bill rate | NSE F&O bhavcopy, RBI DBIE |
| [03 Honest backtester](../projects/03-honest-backtester/) | Daily OHLCV for 10–50 Indian stocks | NSE bhavcopy with corporate actions; yfinance as a check |
| [05 Pairs trading](../projects/README.md) | Sector stocks, daily | NSE bhavcopy with corporate actions |
| [07 GARCH volatility](../projects/README.md) | NIFTY index daily | `^NSEI` via yfinance, or a total return index |
| [09 Purged cross-validation](../projects/README.md) | Any daily panel | Kenneth French or AQR factors, or a panel from Kaggle |
| [10 Limit order book simulator](../projects/README.md) | Order book sample | LOBSTER sample files |
| [12 Risk engine](../projects/README.md) | Multi-asset daily prices | FRED for rates; yfinance for prices, with corporate actions checked |

## 9. Checklist before using any dataset

- [ ] Are prices adjusted for splits, bonuses and dividends? Which column is used?
- [ ] Are corporate actions applied in date order, with the adjustment factor recorded?
- [ ] Does the universe include stocks that were **later delisted**? If not, expect upward bias.
- [ ] Are symbols and scrip codes mapped over time, including renames and mergers?
- [ ] For derivatives: are lot sizes, strike sets and expiry conventions recorded for each date?
- [ ] Are timestamps in exchange local time (IST) and aligned across sources? Is the price a close, a settlement or a last trade?
- [ ] How are missing days, halts and holidays represented?
- [ ] For fundamentals: is the value **as-reported** on the filing date, or a later restatement? Are period-end dates separated from release dates?
- [ ] For macro: is the value the vintage available at the time (ALFRED), or the revised series?
- [ ] Are currency and units consistent (INR, lakh or crore, per share or per lot)?
- [ ] Is the licence compatible with your use, and with publishing results derived from the data?

## 10. Record your provenance

For every dataset used in a project, keep a short manifest alongside the raw files (outside the repo):

| Field | Example |
|---|---|
| Source and URL | NSE bhavcopy archive |
| Download date | 2026-10-29 |
| File name and checksum | Original archive name, SHA-256 of the file |
| Adjustments applied | Splits and bonuses from exchange announcements, applied in date order |
| Known gaps | Halted names on specific days |
| Licence | Exchange terms of use, checked on the download date |

A backtest is only reproducible if someone else can recover the same inputs from this record.
