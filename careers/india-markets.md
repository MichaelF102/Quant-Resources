# Indian markets: structure and practice

*Last reviewed: Oct 2026 · Exchange timings, lot sizes and regulations change. Check the NSE and SEBI circulars before relying on any figure here.*

A working guide to how Indian markets are organised, for anyone building or testing strategies on Indian data or interviewing at firms that trade it. It covers the exchanges and regulators, the trading day, derivatives, settlement, and the data quirks that break naive backtests.

## 1. Institutions

| Body | Role |
|---|---|
| SEBI (Securities and Exchange Board of India) | Securities regulator: sets rules for exchanges, intermediaries, listed companies and market conduct |
| NSE (National Stock Exchange) | Largest exchange by derivatives volume. Publishes the NIFTY indices and the bhavcopy archives |
| BSE | Second exchange for cash equities. Uses scrip codes alongside symbols |
| Clearing corporations | Guarantee trades after execution. Each exchange has its own clearing corporation |
| RBI (Reserve Bank of India) | Monetary policy, interest rates, foreign exchange, and government securities |

The primary sources for data are the NSE and BSE websites. The [data sources](../data/data-sources.md) file covers access and caveats.

## 2. The trading day

- **Equity cash market:** regular session 09:15 to 15:30 IST, Monday to Friday, excluding exchange holidays.
- **Pre-open session:** a call auction before the regular session. Check the current timings in the exchange circular; they have been revised before.
- **Closing price:** derived from the closing session. Know which price a data vendor uses: last trade, weighted average, or closing auction.
- **Holidays:** the exchange publishes its holiday list each year. A backtest needs that list to avoid counting a holiday as a trading day.

## 3. Settlement

Cash equity trades settle on a T+1 basis, meaning one business day after the trade. Check that settlement is still T+1 when you read this, since the cycle has been shortened before.

For a backtest, settlement affects when cash and shares are available for reuse, not the price at which a trade occurs. Model it if your strategy trades the same capital daily.

## 4. Price limits and circuit filters

- Individual stocks have **circuit limits**: a price band around the previous close, set by the exchange. A stock that hits the upper or lower band may stop trading for the day.
- Limits differ between stocks and are revised periodically.
- A stock at a circuit limit has no fills at the trading price, so a daily backtest must treat such days as untradeable.

## 5. Indices

- **NIFTY 50:** the benchmark of 50 large companies. The index is a free-float market-cap weighted price index.
- **NIFTY 500:** a broader set of 500 companies, used in [Projects 04 and 08](../projects/README.md).
- **India VIX:** a volatility index derived from NIFTY option prices. Use it as a benchmark for implied volatility work, and check its calculation method before comparing it with a model.

An index value is usually a **price index**: it excludes dividends. For total return, use the exchange's total return index where one exists.

## 6. Derivatives

- **Products:** index futures and options (on NIFTY and other indices), and stock futures and options on eligible stocks.
- **Lot sizes:** each contract has a fixed number of units, the lot size. The exchange revises lot sizes from time to time. Record the lot size for each date, or your notional exposure will be wrong.
- **Expiry:** contracts expire on set days. Index options have had weekly and monthly expiries, and the expiry days have changed. Check the current contract specification.
- **Settlement:** index derivatives are cash-settled. Stock derivatives have been physically settled in some periods. Check the rules for the period you are testing.
- **Settlement price and close:** the bhavcopy's settlement price is not the same as the last trade. Use the settlement price for end-of-day marks.
- **Open interest and volume:** filter thin strikes before fitting a volatility surface. See [Project 02](../projects/02-implied-vol-surface/).

## 7. Shorting

Short selling in cash equities is restricted for most participants. Strategies that need to short a stock usually do so through futures or stock options, or they do not short at all. A backtest that shorts freely overstates performance. [Project 05](../projects/05-pairs-trading-cointegration/) shows how to handle this.

## 8. Corporate actions

Corporate actions are common in Indian stocks: bonus issues, stock splits, rights issues, mergers, demergers, and dividends. A few practical rules:

- Read the exchange's corporate-action announcements, not only the vendor's adjusted price.
- A bonus issue or split changes the number of shares, so the price falls by the adjustment ratio. A naive return calculation shows a large false loss.
- A symbol or ISIN can change after a merger or demerger, so keep a dated mapping.

See [Databases and storage](../tools-and-technologies/databases-and-storage.md) for storing the mapping.

## 9. Data quirks that break backtests

- **Symbols and scrip codes.** NSE symbols and BSE scrip codes differ. Map them with dates.
- **Missing days.** Halts, suspensions and holidays create gaps. Decide how to represent them and test the decision.
- **Unadjusted prices.** Bhavcopy prices are unadjusted for corporate actions.
- **Survivorship.** Delisted stocks may be absent from the data. This flatters returns.
- **Time zone.** Exchange times are IST. A file timestamped in UTC shows a different date for late-session events.

## 10. Where this shows up in the program

| Topic | Where to read more |
|---|---|
| Data pipeline for bhavcopy and corporate actions | [Quant Developer research track](../roadmaps/quant-developer.md), [Databases and storage](../tools-and-technologies/databases-and-storage.md) |
| Volatility surface for NIFTY options | [Project 02](../projects/02-implied-vol-surface/) |
| Backtest that respects circuits and settlement | [Project 03](../projects/03-honest-backtester/) |
| Market microstructure and exchange rules | [Market microstructure](../cheatsheets/market-microstructure.md) |
| Firms and entry routes | [Careers in India](india.md) |

## 11. Before you rely on a rule in this file

- Check the NSE and SEBI circulars for the period you are testing.
- Check the exchange holiday list.
- Confirm lot sizes and expiry days for each contract, and for each date.
- Confirm the settlement cycle and circuit limits.
