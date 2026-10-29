# Cheat sheets

Reference sheets for the formulas, conventions and interview questions used across the roadmaps and projects. Each sheet covers definitions, the main results, units and conventions, common mistakes, and interview questions.

| Sheet | Covers | Used in |
|---|---|---|
| [Greeks](greeks.md) | Black-Scholes and Black-76 Greeks, second-order Greeks, units, dividends, delta hedging and P&L | [Project 01](../projects/01-monte-carlo-pricer/), [Project 02](../projects/02-implied-vol-surface/) |
| [Distributions](distributions.md) | Normal, lognormal, Student-t, chi-square, gamma, exponential, Poisson, binomial, Pareto, multivariate normal, simulation methods | Roadmap Phase 1, [Project 01](../projects/01-monte-carlo-pricer/) |
| [Stochastic calculus](stochastic-calculus.md) | Brownian motion, Itô's lemma, GBM, Girsanov and risk-neutral pricing, Feynman–Kac, common SDEs, Euler and Milstein schemes | [Project 01](../projects/01-monte-carlo-pricer/), derivatives roadmap |
| [Performance metrics](performance-metrics.md) | Returns and annualisation, Sharpe and its uncertainty, probabilistic and deflated Sharpe, drawdown, VaR and ES, IC, transaction costs, position sizing | [Project 03](../projects/03-honest-backtester/), [Pitfalls](../pitfalls.md) |
| [Time series](time-series.md) | Stationarity, ACF and PACF, ARMA, Box–Jenkins, unit-root and cointegration tests, GARCH, Kalman filter | [Project 05](../projects/README.md), [Project 07](../projects/README.md) |
| [Fixed income](fixed-income.md) | Bond pricing, day-count conventions, YTM, duration, DV01, convexity, bootstrapping, forward rates, Nelson–Siegel | Roadmap Phase 1 (risk and derivatives), [Project 12](../projects/README.md) |
| [Credit risk](credit-risk.md) | PD, LGD, EAD, expected and unexpected loss, hazard rates, CDS, Merton model, portfolio credit risk | [Project 12](../projects/README.md), risk and model validation roadmap |
| [Technical indicators](technical-indicators.md) | Trend, momentum, volatility and volume indicators with verdicts and caveats | [Project 15](../projects/15-technical-indicator-study/), [Project 03](../projects/03-honest-backtester/) |

## Conventions

- Rates are continuously compounded unless stated otherwise. Check the convention before combining a formula with a quoted rate.
- Time is in years for option formulas and in periods for return statistics. Annualise with N = 252 for daily trading data.
- Greeks are quoted per unit change in the underlying, and per vol point, calendar day or 1% of rates where noted.

If a formula here disagrees with a textbook, check the textbook's conventions (continuous or simple rates, per-period or annualised units) before assuming an error.
