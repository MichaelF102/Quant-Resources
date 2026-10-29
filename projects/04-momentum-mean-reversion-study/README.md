# 04 — Momentum and mean-reversion study

**Proves:** signal construction from price data, information coefficient (IC), decay of predictive power over horizons, and cross-sectional versus time-series signals
**Level:** 🟡 · **Time:** 1–2 weekends
**Prerequisites:** [QR roadmap](../../roadmaps/quant-researcher.md) Phases 1 and 3; [Project 03](../03-honest-backtester/) (the backtester); [Performance metrics](../../cheatsheets/performance-metrics.md)

## Goal

Build two families of return-based signals, time-series momentum and short-term reversal, and measure how well each predicts returns over the following days and weeks. The question: does past return carry information about future return in Indian equities, over which horizon, and does the answer survive transaction costs?

## Data

Daily adjusted prices for NIFTY 500 constituents, 2010 onward, from the sources in [data sources](../../data/data-sources.md). Use the survivorship-aware universe if you have one. If not, state the bias and report results anyway.

Record for each stock and day: adjusted close, and the membership of the index on that date (point-in-time where possible).

## Steps

1. **Define the signals before testing them.** Write them down with their parameters:
   - Time-series momentum: the return over the past 12 months excluding the most recent month.
   - Short-term reversal: the return over the past 5 trading days, with the sign reversed.
2. **Compute signals with no look-ahead.** The signal for day t uses prices through day t − 1. Rank the stocks cross-sectionally each day.
3. **Measure IC.** For each day, compute the Spearman rank correlation between the signal and the forward return over horizons of 1, 5, 21 and 63 days. Average across days and report the t-statistic.
4. **Measure decay.** Plot mean IC against horizon. A signal that decays within a week needs faster rebalancing to be useful.
5. **Quantile spread.** Sort stocks into quintiles each month. Report the average forward return of the top minus the bottom quintile, with its standard error.
6. **Costs.** Build a long-short portfolio from the top and bottom deciles, rebalanced monthly. Compute turnover and apply a cost of at least 20 bp per unit of turnover (state your assumption). Report net returns.
7. **Robustness.** Repeat for three different lookback lengths and state how the results change. Count every variant you test.

## Done when

- [ ] Both signals are defined in a table with their parameters, before any results are shown
- [ ] Mean IC and its t-statistic are reported for each horizon, for both signals
- [ ] Quintile spreads are reported with standard errors, and the gross and net-of-cost versions are both shown
- [ ] Turnover per rebalance is reported, and the cost assumption is stated
- [ ] The number of variants tested is reported, with the deflated Sharpe ratio of the best one
- [ ] The write-up says whether the signal survives costs, and which assumption it depends on most

## Common pitfalls

- **Survivorship bias.** A universe of today's index members has done well by construction. Use point-in-time membership, or state the bias explicitly.
- **Using the same-day close.** A signal computed from today's close and traded at today's close is look-ahead.
- **Pooled IC across stocks.** Average the cross-sectional IC by day. Pooling stock-days inflates the t-statistic because observations are not independent.
- **Ignoring the reversal horizon.** Short-term reversal often lives in the first few days and disappears quickly. Testing only monthly rebalances misses it.

## Stretch goals

- Compare with a volatility-adjusted momentum signal, scaling returns by trailing volatility.
- Test whether momentum is stronger after market-wide drawdowns, and state the regime definition in advance.
- Combine the two signals and test whether the combination improves IC.

## Further reading

- Jegadeesh and Titman (1993), "Returns to Buying Winners and Selling Losers," *Journal of Finance*. The original momentum study.
- Moskowitz, Ooi and Pedersen (2012), "Time Series Momentum," *Journal of Financial Economics*. Time-series momentum across asset classes.
- Grinold and Kahn, *Active Portfolio Management* 💸, chapters on information coefficient and breadth.
