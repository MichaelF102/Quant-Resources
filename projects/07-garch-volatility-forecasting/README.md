# 07 — GARCH volatility forecasting

**Proves:** volatility clustering and ARCH effects, GARCH(1,1) estimation, forecast evaluation for a volatility model, and why a model's distributional assumption matters for risk
**Level:** 🟡 · **Time:** 1–2 weekends
**Prerequisites:** [QR roadmap](../../roadmaps/quant-researcher.md) Phase 3; [Time series cheat sheet](../../cheatsheets/time-series.md), volatility section; [Quant libraries](../../tools-and-technologies/quant-libraries.md)

## Goal

Fit GARCH-family models to the daily returns of the NIFTY 50 index, forecast its volatility one day to one month ahead, and judge the forecasts against a simple benchmark. The question: does a GARCH model forecast NIFTY volatility better than a rolling window, and does the answer change with the distribution assumed for the shocks?

## Data

Daily close of the NIFTY 50 index, from 2005 onward. Use the source in [data sources](../../data/data-sources.md) (for example a total return or price index, stated). Compute log returns, in percent.

Realised volatility benchmark: the square root of the sum of squared daily returns over the following 21 days, from the same series. Use it as the target for out-of-sample evaluation, and say so in the write-up.

## Steps

1. **Check for ARCH effects.** Test the returns for autocorrelation in squared returns with Ljung–Box and Engle's ARCH-LM test. Report both.
2. **Fit a GARCH(1,1) by maximum likelihood.** Use the `arch` package (`arch_model` with `vol="GARCH"`, `p=1`, `q=1`). Report the parameters, persistence α + β, and the implied unconditional volatility.
3. **Compare distributions.** Fit the same model with normal and Student-t innovations. Compare log-likelihood and information criteria.
4. **Compare variants.** Fit a GJR-GARCH (asymmetric) model, and test whether negative shocks raise volatility more than positive ones.
5. **Forecast out of sample.** Estimate on an expanding window, starting from 2010. Forecast the variance for horizons of 1, 5 and 21 days, at each point in time.
6. **Benchmarks.** Compare with a 21-day rolling historical volatility and with an exponentially weighted moving average (EWMA, decay 0.94).
7. **Evaluate.** Report the root mean squared error and the QLIKE loss for each model and horizon. Show a calibration plot: forecast against realised volatility.

## Done when

- [ ] ARCH effects are tested and reported before any model is fitted
- [ ] GARCH(1,1) parameters, persistence and unconditional volatility are reported, with standard errors
- [ ] Normal and Student-t innovations are compared with a stated criterion
- [ ] Out-of-sample forecasts are produced from an expanding window, with no parameter estimated on data after the forecast date
- [ ] GARCH, GJR-GARCH, rolling and EWMA forecasts are compared on the same dates, horizons and loss functions
- [ ] The write-up states which model forecasts best at each horizon, and what that means for a risk limit

## Common pitfalls

- **Estimating on the full sample, then forecasting within it.** The fitted parameters have seen the data being forecast.
- **Confusing variance and volatility.** Forecast variance first, then take the square root. Averaging volatilities over horizons is not the same as averaging variances.
- **Using the wrong units.** Percent returns and decimal returns give different parameter values. Check the scale before comparing with published numbers.
- **Overlapping forecast windows.** Monthly realised volatility computed at daily steps overlaps. Use non-overlapping windows when testing significance.
- **Trusting persistence close to one.** A near-unit root in volatility can be a sign of a structural break, not of long memory. Test for breaks.

## Stretch goals

- Fit a regime-switching model and compare it with GARCH.
- Use the forecasts to set a volatility-targeting position size, and report the turnover and drawdown of the resulting strategy.
- Compare NIFTY volatility with India VIX over the same period, if you have a reliable source, and discuss the differences.

## Further reading

- Engle (1982), "Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation," *Econometrica*. The ARCH model.
- Bollerslev (1986), "Generalized Autoregressive Conditional Heteroskedasticity," *Journal of Econometrics*. GARCH.
- Patton (2011), "Volatility Forecast Comparison Using Imperfect Volatility Proxies," *Journal of Econometrics*. Why the choice of loss function matters.
