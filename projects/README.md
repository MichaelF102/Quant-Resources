# Project ladder

*If you can't build it, you don't know it yet.*

Projects are roughly ordered by difficulty. For the firms that hire for these skills, see [Careers in India](../careers/india.md).

**Status key:** ✅ starter code · 📋 full spec · 📝 outline only.

Each project names the concepts it proves, the data to use, and a **done when** checklist, so you know when to stop polishing and move on.

To propose a new project, copy the [spec template](TEMPLATE.md) into a new folder and follow it.

| # | Project | Proves | Data | Level | Status |
|---|---|---|---|---|---|
| 01 | [Monte Carlo option pricer](01-monte-carlo-pricer/) | Risk-neutral pricing, simulation, variance reduction | Synthetic | 🟢 | ✅ Starter code |
| 02 | [Implied volatility surface](02-implied-vol-surface/) | Black-Scholes inversion, root-finding, the smile | NSE F&O bhavcopy | 🟡 | 📋 Full spec |
| 03 | [Honest vectorised backtester](03-honest-backtester/) | Costs, slippage, look-ahead prevention, metrics | NSE bhavcopy / yfinance | 🟡 | 📋 Full spec |
| 04 | [Momentum & mean-reversion study](04-momentum-mean-reversion-study/) | Signal construction, IC, decay analysis | NIFTY 500 daily | 🟡 | 📋 Full spec |
| 05 | [Pairs trading with cointegration](05-pairs-trading-cointegration/) | Engle-Granger / Johansen, walk-forward testing | NSE sector pairs | 🟡 | 📋 Full spec |
| 06 | [Covariance estimation shoot-out](06-covariance-shootout/) | Sample vs. Ledoit-Wolf vs. factor covariance | NIFTY 50 daily | 🟡 | 📋 Full spec |
| 07 | [GARCH volatility forecasting](07-garch-volatility-forecasting/) | ARCH effects, GARCH(1,1), forecast evaluation | NIFTY index | 🟡 | 📋 Full spec |
| 08 | [Factor model for Indian equities](08-factor-model-indian-equities/) | Fama-French style factors, cross-sectional regression, point-in-time data | NSE + fundamentals | 🔴 | 📋 Full spec |
| 09 | [Purged cross-validation for a ML signal](09-purged-cross-validation/) | Leakage, purging & embargo, deflated Sharpe. Stretch: a leakage-aware sequence model (LSTM) for forecasting, evaluated with the same purged splits | Any daily panel | 🔴 | 📋 Full spec |
| 10 | [Limit order book simulator (C++)](10-limit-order-book-simulator/) | Matching engine, data structures, latency | Synthetic / LOBSTER sample | 🔴 | 📋 Full spec |
| 11 | [Market-making simulation](11-market-making-simulation/) | Inventory risk, Avellaneda-Stoikov quoting | Synthetic | 🔴 | 📋 Full spec |
| 12 | [Risk engine: VaR & Expected Shortfall](12-risk-engine-var-es/) | Historical / parametric / MC VaR, backtesting VaR | Multi-asset portfolio | 🟡 | 📋 Full spec |
| 13 | [PCA on NSE stocks](13-pca-nse-stocks/) | Eigen-decomposition, covariance structure, factor interpretation | NIFTY 50 daily | 🟢 | 📋 Full spec |
| 14 | [Finite-difference Black-Scholes solver](14-finite-difference-black-scholes/) | Numerical PDE solving, θ-schemes, stability and convergence, American options | Synthetic (Project 01 parameters) | 🟡 | 📋 Full spec |
| 15 | [Technical-indicator study](15-technical-indicator-study/) | Rule definition, look-ahead prevention, walk-forward testing, null benchmarks, multiple testing | NSE daily (Project 03 universe) | 🟡 | 📋 Full spec |
| 16 | [Time-series momentum across assets](16-time-series-momentum/) | Trend signals, volatility scaling, continuous futures and roll effects, diversification | Index, bond, currency and commodity futures | 🟡 | 📋 Full spec |
| 17 | [Optimal execution](17-optimal-execution/) | Almgren–Chriss schedules, market impact, implementation shortfall | Synthetic (LOBSTER optional) | 🔴 | 📋 Full spec |

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
