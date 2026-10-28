# 03 — Honest vectorised backtester

**Proves:** look-ahead prevention, transaction cost modelling, performance metrics, testing your own research code
**Level:** 🟡 · **Time:** 2 weekends
**Prerequisites:** [QR roadmap](../../roadmaps/quant-researcher.md) Phase 3; read [Pitfalls](../../pitfalls.md) first

## Goal

Build a small backtesting library that makes cheating **hard**. Most homemade backtesters overstate returns by quietly using tomorrow's information or ignoring costs. Yours should catch those mistakes by design — and include tests proving it does.

You'll reuse this backtester in later projects (04, 05, 08), so build it as a module, not a notebook.

## Data

Daily OHLCV for 10–50 NSE stocks or ETFs, 2015 onward.

- Quick start: `yfinance` with `.NS` tickers (adjusted close).
- Better: NSE bhavcopy, applying corporate actions yourself.

See [data sources](../../data/data-sources.md) and its checklist — especially survivorship bias.

## Design

```
backtester/
├── data.py        # load, align, validate prices
├── signals.py     # example strategies → target weights
├── engine.py      # weights → positions → P&L, with costs
├── metrics.py     # performance statistics
└── tests/
    ├── test_engine.py
    └── test_lookahead.py
```

**Core interface:** a strategy is a function that takes prices and returns **target weights** for each asset, where row *t* may only use data up to *t*. The engine — not the strategy — applies the one-day lag between deciding and earning, and a perturbation test (below) verifies the strategy never reads ahead. Together these make accidental look-ahead hard to ship.

```python
def strategy(prices: pd.DataFrame) -> pd.DataFrame:
    """Return target weights indexed like prices. Row t may use data up to t."""
    ...

result = run_backtest(prices, strategy, cost_bps=15)
```

## Steps

1. **Data validation.** Check for missing values, duplicate dates, non-positive prices and suspicious jumps (> 30% in a day often signals an unadjusted split). Fail loudly.
2. **Engine.** Compute returns; shift weights by one day so weights decided at close *t* earn returns from *t* to *t+1*; compute portfolio returns.
3. **Costs.** Turnover = sum of absolute weight changes. Cost = turnover × cost_bps. Make it configurable; start with 10–20 bps round-trip for liquid Indian large-caps, and remember STT and stamp duty in India.
4. **Metrics.** CAGR, annualised volatility, Sharpe (state your risk-free assumption), Sortino, max drawdown and its duration, annual turnover, hit rate. Annualise with ~250 trading days for NSE.
5. **Example strategies.** Equal-weight buy-and-hold (your benchmark), 12-1 month momentum, and a simple moving-average crossover.
6. **Report.** Equity curve, drawdown chart, and a table comparing strategies **before and after costs**.

## Done when

- [ ] The engine applies the one-day lag itself; strategies cannot bypass it
- [ ] **Look-ahead test (perturbation):** scramble all prices after some date *t*, re-run the strategy, and assert every weight up to and including *t* is unchanged. A lag alone can't catch a strategy that reads future rows (e.g. `returns.shift(-1)`), but this test does. Write it as a unit test and show it fails on a deliberately cheating strategy
- [ ] **Cost test:** doubling `cost_bps` reduces net return by exactly the turnover × extra cost
- [ ] **Sanity test:** a constant equal-weight portfolio with zero costs matches a hand calculation
- [ ] Metrics reported before and after costs, side by side
- [ ] Results split into at least two sub-periods (e.g. 2015–2019 and 2020 onward)

## Common pitfalls

- **Survivorship bias:** using today's NIFTY 50 constituents for 2015. Your momentum strategy will look better than it was. If you can't get historical constituents, state the bias explicitly in your results.
- **Unadjusted prices:** a 1:1 bonus issue looks like a 50% crash. Validate before trusting any result.
- **Annualising Sharpe from overlapping or monthly returns incorrectly.** Daily mean × 250 and daily std × √250.
- **Ignoring the cash leg:** if weights don't sum to 1, decide what happens to the rest (cash at the risk-free rate, or zero).
- **Tuning on the full sample.** Pick strategy parameters in advance, or on the first sub-period only.

## Stretch goals

- Add slippage proportional to volatility or to trade size relative to average daily volume.
- Add position limits and a maximum gross leverage constraint.
- Compute the **deflated Sharpe ratio** given the number of strategy variants you tried.
- Refactor into an **event-driven** engine where the same strategy runs on historical replay or a simulated feed (the QD roadmap's Phase 7 checkpoint).
- Benchmark against `vectorbt` on the same strategy to validate your numbers.

## Further reading

- López de Prado, *Advances in Financial Machine Learning*, ch. 11–14 💸 — backtesting dangers and statistics.
- Ernest Chan, *Quantitative Trading* (2nd ed.) 💸 — practical, accessible; ch. 3 on backtesting.
