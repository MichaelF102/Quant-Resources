# 05 — Pairs trading with cointegration

**Proves:** cointegration and error correction, the Engle–Granger and Johansen tests, hedge-ratio estimation, walk-forward testing, and the cost of short-selling constraints
**Level:** 🟡 · **Time:** 2 weekends
**Prerequisites:** [QR roadmap](../../roadmaps/quant-researcher.md) Phase 3; [Project 03](../03-honest-backtester/); [Time series cheat sheet](../../cheatsheets/time-series.md), cointegration section

## Goal

Find pairs of stocks within one Indian sector whose price spread is stationary, and test a mean-reversion strategy on that spread out of sample. The question: does a pair that was cointegrated in one period remain cointegrated in the next, and does the strategy earn enough to cover costs?

## Data

Daily adjusted prices for 15–30 stocks within one sector, from 2012 onward. Use the sources in [data sources](../../data/data-sources.md). Apply corporate actions before computing any spread.

Shorting in Indian cash equities is restricted for most investors. A common workaround is to trade the short leg through stock or index futures. Decide the approach before testing and state its costs.

## Steps

1. **Split the sample.** Use a formation window of 12 months to select pairs, and a trading window of the following 6 months. Roll forward in steps of 6 months, for at least five windows.
2. **Select pairs on the formation window only.** Run the Engle–Granger test on each pair in both directions. Keep pairs with p-values below a threshold you set in advance, and record how many pairs you tested.
3. **Estimate the hedge ratio.** Regress one log price on the other by OLS over the formation window. Optionally estimate a time-varying ratio with a Kalman filter, as described in the time series cheat sheet.
4. **Define the spread and the rules.** Spread = log price of leg A − hedge ratio × log price of leg B. Standardise by its formation-window mean and standard deviation. Enter when the z-score exceeds 2 in absolute value; exit when it returns to 0; stop out at 4.
5. **Trade out of sample.** Apply the rules to the trading window only, with the formation-window parameters held fixed.
6. **Costs.** Apply costs to both legs and to the futures roll if used. State the assumption.
7. **Report per window.** Results must be shown for each window, not pooled, so you can see whether the edge is stable.

## Done when

- [ ] Pair selection uses only the formation window; no trading-window data enters the selection step
- [ ] The number of pairs tested is reported, with the expected number of false positives at the chosen significance level
- [ ] Hedge ratio, entry, exit and stop rules are fixed before the trading window is evaluated
- [ ] Results are shown per window, with the number of trades and the average holding period
- [ ] Net-of-cost performance is reported with turnover, and the short-leg implementation is stated
- [ ] A write-up states whether pairs stayed cointegrated across windows, and what happened when they did not

## Common pitfalls

- **Pair selection on the full sample.** This is look-ahead and produces impressive but unreal results.
- **Multiple testing.** Testing 100 pairs at 5% gives about 5 pairs that pass by chance. Count the tests and adjust.
- **Cointegration breaks down.** A stock that loses its business relationship with its partner will drift away permanently. Use a stop-out rule and report how often it triggers.
- **Ignoring the short leg.** A backtest that shorts freely overstates the strategy. Model the constraint.
- **Using the wrong critical values.** Engle–Granger residual tests need their own critical values, not the ordinary ADF table.

## Stretch goals

- Compare the Engle–Granger approach with Johansen on the same group of stocks.
- Replace the fixed z-score thresholds with thresholds chosen by a rolling quantile of the spread, and compare.
- Estimate the spread's half-life and use it to set the holding period.

## Further reading

- Engle and Granger (1987), "Co-integration and Error Correction," *Econometrica*. The original two-step test.
- Johansen (1988), "Statistical Analysis of Cointegration Vectors," *Journal of Economic Dynamics and Control*. The multivariate test.
- Gatev, Goetzmann and Rouwenhorst (2006), "Pairs Trading: Performance of a Relative-Value Arbitrage Rule," *Review of Financial Studies*. A widely cited, careful test of a simple pairs rule.
