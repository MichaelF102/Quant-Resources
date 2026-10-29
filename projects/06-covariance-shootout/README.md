# 06 — Covariance estimation shoot-out

**Proves:** why the sample covariance matrix is unreliable when the number of assets is large relative to the number of observations, shrinkage estimators, factor-model covariance, and out-of-sample evaluation of risk forecasts
**Level:** 🟡 · **Time:** 1–2 weekends
**Prerequisites:** [QR roadmap](../../roadmaps/quant-researcher.md) Phases 2 and 6; [Linear algebra cheat sheet](../../cheatsheets/linear-algebra.md)

## Goal

Compare three covariance estimators for a portfolio of Indian stocks: the sample covariance, Ledoit–Wolf shrinkage, and a single-factor model. Judge them by how well they forecast the portfolio's realised risk out of sample, and by whether the minimum-variance portfolio they produce is stable.

## Data

Daily adjusted returns for 50 NIFTY 50 constituents, over at least five years. Use the sources in [data sources](../../data/data-sources.md). Use the same universe and period for all estimators.

## Steps

1. **Set up the comparison.** Use a rolling window of 252 trading days to estimate the covariance matrix, then forecast the next 21 days. Roll forward one month at a time.
2. **Sample covariance.** Estimate Σ̂ directly. Note its condition number and whether it is invertible for your window and universe size.
3. **Ledoit–Wolf shrinkage.** Shrink the sample covariance towards a structured target. Use `sklearn.covariance.LedoitWolf` and record the estimated shrinkage intensity over time.
4. **Single-factor model.** Use the equal-weighted index as the factor. Estimate each stock's beta and idiosyncratic variance, and build Σ = β β′ σ²_m + D, where D is diagonal.
5. **Minimum-variance portfolios.** For each estimator and each month, compute the long-only minimum-variance portfolio. Record turnover between months.
6. **Evaluate.** For each estimator, compare the forecast volatility of the portfolio with its realised volatility in the following month. Report the mean absolute error of the forecast and the average turnover.
7. **Stability.** Repeat with a window of 126 days, and report how the ranking changes.

## Done when

- [ ] All three estimators use the same universe, windows and rebalancing dates
- [ ] Forecast volatility is compared with realised volatility out of sample, with the error reported for each estimator
- [ ] Turnover of the minimum-variance portfolios is reported, with the average weight in the largest holding
- [ ] The condition number of the sample covariance is reported for each window
- [ ] The shrinkage intensity over time is plotted for Ledoit–Wolf
- [ ] The write-up says which estimator forecasts best, which gives the most stable portfolio, and whether these are the same

## Common pitfalls

- **Judging by in-sample fit.** The sample covariance always fits its own window best. Only out-of-sample forecast error matters.
- **Realised volatility from the same window.** The forecast must be compared with returns that come after the estimation window.
- **Ignoring turnover.** A minimum-variance portfolio that changes every month can be costly. Report turnover next to risk.
- **Long-only constraints.** A solver failure on a long-only problem can be silent. Check that the weights sum to one and are non-negative.
- **Mixing returns and prices.** Covariance must be estimated on returns, not on price levels.

## Stretch goals

- Add a constant-correlation target for Ledoit–Wolf, and compare it with the identity target.
- Estimate the factor model with two or three factors, using PCA on the returns, and compare with the single-factor version.
- Use a risk-parity portfolio built on each estimator, and compare with the minimum-variance result.

## Further reading

- Ledoit and Wolf (2004), "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices," *Journal of Multivariate Analysis*. The shrinkage estimator used here.
- Ledoit and Wolf (2003), "Honey, I Shrunk the Sample Covariance Matrix," *Journal of Portfolio Management*. A readable account of why shrinkage helps.
- Grinold and Kahn, *Active Portfolio Management* 💸, chapter on risk models.
