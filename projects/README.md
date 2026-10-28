# Project ladder

*If you can't build it, you don't know it yet.*

Projects are roughly ordered by difficulty.

**Status key:** ✅ starter code · 📋 full spec · 📝 outline only Each one names the concepts it proves, the data to use, and a **done when** checklist, so you know when to stop polishing and move on.

| # | Project | Proves | Data | Level | Status |
|---|---|---|---|---|---|
| 01 | [Monte Carlo option pricer](01-monte-carlo-pricer/) | Risk-neutral pricing, simulation, variance reduction | Synthetic | 🟢 | ✅ Starter code |
| 02 | [Implied volatility surface](02-implied-vol-surface/) | Black-Scholes inversion, root-finding, the smile | NSE F&O bhavcopy | 🟡 | 📋 Full spec |
| 03 | [Honest vectorised backtester](03-honest-backtester/) | Costs, slippage, look-ahead prevention, metrics | NSE bhavcopy / yfinance | 🟡 | 📋 Full spec |
| 04 | Momentum & mean-reversion study | Signal construction, IC, decay analysis | NIFTY 500 daily | 🟡 | 📝 Outline |
| 05 | Pairs trading with cointegration | Engle-Granger / Johansen, walk-forward testing | NSE sector pairs | 🟡 | 📝 Outline |
| 06 | Covariance estimation shoot-out | Sample vs. Ledoit-Wolf vs. factor covariance | NIFTY 50 daily | 🟡 | 📝 Outline |
| 07 | GARCH volatility forecasting | ARCH effects, GARCH(1,1), forecast evaluation | NIFTY index | 🟡 | 📝 Outline |
| 08 | Factor model for Indian equities | Fama-French style factors, cross-sectional regression | NSE + fundamentals | 🔴 | 📝 Outline |
| 09 | Purged cross-validation for a ML signal | Leakage, purging & embargo, deflated Sharpe | Any daily panel | 🔴 | 📝 Outline |
| 10 | Limit order book simulator (C++) | Matching engine, data structures, latency | Synthetic / LOBSTER sample | 🔴 | 📝 Outline |
| 11 | Market-making simulation | Inventory risk, Avellaneda-Stoikov quoting | Synthetic | 🔴 | 📝 Outline |
| 12 | Risk engine: VaR & Expected Shortfall | Historical / parametric / MC VaR, backtesting VaR | Multi-asset portfolio | 🟡 | 📝 Outline |
| 13 | PCA on NSE stocks | Eigen-decomposition, covariance structure, factor interpretation | NIFTY 50 daily | 🟢 | 📝 Outline |

---

## Spec template

Every project folder follows this structure so they're easy to review and compare.

```markdown
# NN — Project name

**Proves:** concepts this demonstrates
**Level:** 🟢 / 🟡 / 🔴 · **Time:** estimate
**Prerequisites:** roadmap phase(s)

## Goal
One paragraph: what you're building and the question it answers.

## Data
Source, frequency, period, and how to load it.

## Steps
1. …
2. …

## Done when
- [ ] Concrete, checkable criteria

## Common pitfalls
- What usually goes wrong

## Stretch goals
- Optional extensions

## Further reading
- One or two resources, with verdicts
```

---

## Example outline

### 05 — Pairs trading with cointegration 🟡

**Goal:** Find cointegrated pairs within an Indian sector and test a mean-reversion strategy on the spread.

**Done when:**
- [ ] Pair selection happens on a **formation window only**; trading happens on the following out-of-sample window
- [ ] Hedge ratio estimated via OLS (and optionally Kalman filter); z-score entry/exit rules defined in advance
- [ ] Walk-forward over at least 5 rolling windows, with results reported per window
- [ ] Multiple-testing caveat stated: testing 100 pairs at 5% significance gives ~5 false positives

**Common pitfalls:** selecting pairs on the full sample (look-ahead); ignoring that cointegration breaks down; not accounting for short-selling constraints in Indian cash equities (use futures for the short leg).
