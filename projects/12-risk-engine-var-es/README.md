# 12 — Risk engine: VaR and Expected Shortfall

**Proves:** historical, parametric and Monte Carlo estimation of Value at Risk and Expected Shortfall, backtesting with exception counts and the Kupiec test, and why a model can pass a backtest and still understate tail losses
**Level:** 🟡 · **Time:** 2 weekends
**Prerequisites:** [Risk roadmap](../../roadmaps/risk-model-validation.md) Phase 3; [Performance metrics cheat sheet](../../cheatsheets/performance-metrics.md), tail-risk section; [Greeks cheat sheet](../../cheatsheets/greeks.md)

## Goal

Build a risk engine for a multi-asset portfolio that estimates one-day Value at Risk (VaR) and Expected Shortfall (ES) at 99% and 97.5%, using three methods. Backtest the estimates over a long out-of-sample period. The question: which method gives the most accurate risk numbers, and where does each one fail?

## Data

Daily adjusted prices for a portfolio of about 10 assets: five NIFTY 50 stocks, the NIFTY index, one gold or bond ETF, and one currency pair if you can source it. Use the sources in [data sources](../../data/data-sources.md). Fix the portfolio weights at the start, and rebalance daily to those weights, stating the rule.

## Steps

1. **Compute portfolio returns.** Use the fixed weights and daily asset returns.
2. **Historical VaR and ES.** Use the last 500 days. VaR is the negative of the α quantile of returns. ES is the negative of the average return on days at or below that quantile.
3. **Parametric VaR and ES.** Assume normal returns with the sample mean and standard deviation over 500 days. VaR = −(μ + σ Φ⁻¹(α)). ES = −(μ − σ φ(Φ⁻¹(α))/α).
4. **Monte Carlo VaR and ES.** Simulate asset returns from a multivariate normal with the sample covariance, 100,000 draws, and compute the quantiles as in step 2.
5. **Rolling backtest.** Roll the 500-day window forward daily over at least 1,000 days. For each day, record the VaR estimate and whether the next day's loss exceeded it.
6. **Kupiec test.** For each method and confidence level, count the exceptions x out of T days, and compute the likelihood-ratio statistic:
   LR = −2 ln[(1 − p)^(T − x) p^x] + 2 ln[(1 − x/T)^(T − x) (x/T)^x], where p = 1 − confidence. Under the null, LR is chi-squared with one degree of freedom.
7. **Expected Shortfall check.** Compare the realised average loss beyond VaR with the ES estimate on the exception days.
8. **Stress.** Add a stress scenario using the worst 20-day window in the sample, and report the loss of each method.

## Done when

- [ ] All three methods are implemented and tested against a hand-computed case for one day
- [ ] VaR and ES are reported at 99% and 97.5% for each method
- [ ] A rolling backtest of at least 1,000 days is run, with exception counts for each method and level
- [ ] The Kupiec statistic and its p-value are reported for each method and level
- [ ] The average realised loss on exception days is compared with ES, with a stated conclusion
- [ ] The write-up says which method passes backtesting, and which fails in the tail or under stress

## Common pitfalls

- **Overlapping backtest windows.** Consecutive exceptions are not independent when volatility clusters. The Kupiec test assumes independence, so check exceptions for clustering as well.
- **Normal assumption in the tails.** Parametric VaR often passes at 97.5% and fails at 99%. Report both levels.
- **Historical window too short.** A 500-day window may not contain a crisis. Report what the window covers.
- **Sign convention.** VaR is usually reported as a positive loss. Keep the convention consistent between the code and the report.
- **Monte Carlo seed.** Fix the seed and record it, or results will change between runs.

## Stretch goals

- Estimate VaR with filtered historical simulation: standardise returns by a GARCH volatility forecast, then apply the historical quantile to scaled returns. Use [Project 07](../07-garch-volatility-forecasting/).
- Add the Christoffersen test for independence of exceptions to the Kupiec test.
- Decompose portfolio VaR into the contribution of each asset, and check that the contributions sum to the total.

## Further reading

- Kupiec (1995), "Techniques for Verifying the Accuracy of Risk Measurement Models," *Journal of Derivatives*. The proportion-of-failures test.
- Christoffersen (1998), "Evaluating Interval Forecasts," *International Economic Review*. The independence test.
- Basel Committee on Banking Supervision, *Minimum capital requirements for market risk* (2019), linked in the [risk roadmap](../../roadmaps/risk-model-validation.md). The move from VaR to expected shortfall for internal models.
