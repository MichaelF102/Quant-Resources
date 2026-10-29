# Quant libraries

*Last reviewed: Oct 2026*

Libraries save time, but they also hide choices. A pricing library hides the day-count convention. A backtester hides when a fill happens. Use a library to check your own work, and read its defaults before you trust its output.

**Build the honest backtester in [Project 03](../projects/03-honest-backtester/) before using any backtesting library.** Then compare its output with a library on the same data. A difference tells you which assumption the library makes.

## 1. Pricing and fixed income

| Library | Use it for | Verdict | Link |
|---|---|---|---|
| QuantLib | Bond pricing, yield curves, option and swap pricing, day-count conventions | The standard open-source library for this. Large and complex, so use it to check your own implementation rather than to start from scratch. | [quantlib.org](https://www.quantlib.org/) |
| Your own code (NumPy and SciPy) | Black-Scholes, Greeks, bond maths, Merton | Write these yourself first. The [cheat sheets](../cheatsheets/) give the formulas. Use QuantLib to cross-check. | — |

## 2. Volatility and time series

| Library | Use it for | Verdict | Link |
|---|---|---|---|
| arch | Univariate volatility models, including GARCH-family models | Use it for [Project 07](../projects/README.md). Check the model's documentation for the exact specification and the default distribution. | [Docs](https://arch.readthedocs.io/en/latest/) |
| statsmodels | ARIMA, regression with diagnostics, unit-root and cointegration tests | Use it for inference and tests. Its output is detailed enough to check assumptions. | [Docs](https://www.statsmodels.org/stable/) |

## 3. Optimisation and portfolio construction

| Library | Use it for | Verdict | Link |
|---|---|---|---|
| cvxpy | Convex optimisation problems: mean-variance, constraints, risk budgets | Express the problem in terms of constraints and let the solver handle it. Use it in Phase 6 of the Quant Researcher roadmap. | [Docs](https://www.cvxpy.org/) |
| scipy.optimize | Smaller optimisation problems and root-finding | Enough for implied volatility inversion and simple fits. | — |

## 4. Machine learning

| Library | Use it for | Verdict | Link |
|---|---|---|---|
| scikit-learn | Models, preprocessing, cross-validation utilities | Good for baseline models. Its standard cross-validation splitters ignore time order, so a fold can train on observations that come after its test period, which leaks information. Use time-ordered splits, and write a purged splitter as [Project 09](../projects/README.md) describes. | [Docs](https://scikit-learn.org/stable/) |

## 5. Backtesting libraries

| Library | Style | Verdict | Link |
|---|---|---|---|
| vectorbt | Vectorised, fast for many parameter combinations | Fast for parameter sweeps. Those sweeps are also where overfitting happens, so count the trials and use the deflated Sharpe ratio. | [Repository](https://github.com/polakowo/vectorbt) |
| backtrader | Event-driven, one bar at a time | Clear about the order of events, which helps when reasoning about fills. The repository page did not show a recent release, so check its maintenance status before adopting it. | [Repository](https://github.com/mementum/backtrader) |

**Before using either library, check these points in its documentation:**

- When a signal is computed, and when the trade fills. A fill at the same bar's close as the signal is look-ahead.
- Whether costs and slippage are included by default, and how turnover is charged.
- How corporate actions and missing bars are handled.
- Whether the data is adjusted, and whether delisted symbols are included.

If you cannot answer these questions from the documentation, the library is not ready to trust.

## 6. Choosing a library

| Need | Start with |
|---|---|
| A bond price or a curve | QuantLib, cross-checked by your own code |
| A GARCH forecast | arch, cross-checked by statsmodels for the basics |
| A portfolio with constraints | cvxpy |
| A parameter sweep over a strategy | Your own backtester first, then vectorbt for the sweep |
| A regression with diagnostics | statsmodels |

## 7. Learn when

| Phase | Library |
|---|---|
| QR Phases 1–3 | statsmodels, scipy.stats |
| QR Phase 4 and the fixed-income elective | QuantLib, cross-checked against your own code |
| QR Phase 5 | scikit-learn, with time-ordered splits |
| QR Phase 6 | cvxpy |
| QT Phase 3 | Your own Greeks code, cross-checked with a library |
| Risk Phase 4 | QuantLib for curves, your own code for credit models |
