# 15 — Do technical indicators have an edge? An honest test

**Proves:** defining trading rules precisely, avoiding look-ahead in indicator calculations, parameter selection without overfitting, benchmark and null-model comparison, and multiple-testing correction
**Level:** 🟡 · **Time:** 2 weekends
**Prerequisites:** [Project 03](../03-honest-backtester/) (the backtester); [Technical indicators cheat sheet](../../cheatsheets/technical-indicators.md); [Performance metrics cheat sheet](../../cheatsheets/performance-metrics.md); [Pitfalls](../../pitfalls.md)

## Goal

Test three classic technical rules — an EMA crossover, RSI mean reversion, and Bollinger Band reversion — on Indian equities, with costs, out-of-sample evaluation, and a null benchmark. The question is whether any rule beats a baseline after costs, and how much of its apparent performance is explained by parameter choice and multiple testing. The expected result is that most rules fail once these corrections are in place. Report that result plainly. A rule that does not survive the test is a valid finding.

## Data

The same universe and period as [Project 03](../03-honest-backtester/): 10–50 NSE stocks, daily OHLCV, from 2015 onward. Use the same cost model and the same data-cleaning steps for every rule. See [data sources](../../data/data-sources.md) for corporate-action handling; apply it before computing any indicator.

## Steps

1. **Fix the rule definitions before looking at results.** Write each rule with its parameters in a table:
   - EMA crossover: long when EMA₁₀ > EMA₅₀, flat otherwise.
   - RSI mean reversion: long when RSI₁₄ crosses above 30 from below; exit when it crosses above 50. Add a trend filter: only trade when close is above SMA₂₀₀.
   - Bollinger reversion: long when close crosses back above the lower band (SMA₂₀ − 2σ₂₀); exit at the middle band.
2. **Compute indicators without look-ahead.** Each signal on day t uses only data through day t − 1 close, and the position is taken at the day t open or the next close, as the backtester specifies. Do not use centred windows.
3. **Run the backtester with costs.** Apply the cost model from Project 03, including turnover-based costs. Report gross and net results.
4. **Split the sample.** Use 2015–2019 for any parameter choice, 2020–2022 for validation, and 2023 onward as a single untouched test set. Choose the final parameter set in the first two periods only.
5. **Walk-forward check.** Re-estimate the chosen parameter set on a rolling window and test on the next period, with at least five windows. Report results per window.
6. **Benchmarks.**
   - Buy and hold the same universe.
   - Random-entry baseline: random long or flat decisions with the same average exposure and turnover, averaged over many seeds.
   - Block bootstrap of the strategy's returns, to get a confidence interval for its Sharpe ratio.
7. **Multiple testing.** Count every rule and parameter combination you evaluated, including those you discarded. Compute the deflated Sharpe ratio for the best one, as described in the performance metrics cheat sheet.
8. **Write the conclusion.** State which rules, if any, beat the random baseline net of costs out of sample, and by how much. State the number of trials. Do not extend the test period to find a result.

## Done when

- [ ] Every rule's definition, parameters, and entry and exit conditions are written down before the out-of-sample test, and included in the repo.
- [ ] No indicator uses data after the time it is computed. A test checks this by changing future prices and confirming the signals before that point do not change.
- [ ] Parameters are chosen only on the in-sample and validation periods. The final test period is evaluated once per rule.
- [ ] Net-of-cost Sharpe, maximum drawdown, turnover and exposure are reported for each rule and for each benchmark.
- [ ] Random-entry baseline is run with at least 200 seeds, and the rules are compared against its distribution, not a single run.
- [ ] Block-bootstrap confidence intervals are reported for the Sharpe ratio of each rule.
- [ ] The number of trials is reported, and the deflated Sharpe ratio is computed for the best rule.
- [ ] The write-up states whether each rule beats the baseline out of sample, and the conclusion is written even if it is negative.

## Common pitfalls

- **Parameters chosen on the full sample.** Picking the EMA pair that happened to work since 2015 measures the past, not the rule.
- **Centred or forward-shifted indicators.** A rolling window with `center=True`, or a signal computed from the day's close and traded at the same close, looks profitable and is not achievable.
- **Ignoring turnover.** Oscillator rules trade often. Gross results can look good while net results are negative.
- **Stopping at the first good result.** Trying twenty variants and reporting the best is the most common way to fool yourself. Count them.
- **Evaluating only the bull market.** Report results by regime, for example by the trend state of the index.

## Stretch goals

- Add a regime filter based on realised volatility, and test whether the rules work only in one regime.
- Test the same rules on NIFTY 50 as an index, and compare with the stock universe.
- Combine two rules with a vote or a weighted score. Keep the combination rule fixed before testing.
- Compare with a simple momentum rule using the same lookbacks, to see whether any indicator adds information beyond price momentum.

## Further reading

- Sullivan, Timmermann and White (1999), "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap," *Journal of Finance*. Shows how the apparent profitability of many rules disappears once the number of rules tested is accounted for.
- Brock, Lakonishok and LeBaron (1992), "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns," *Journal of Finance*. The classic positive result on moving-average rules. Read it with the 1999 paper, which revisits its data.
- Bailey and López de Prado (2014), "The Deflated Sharpe Ratio." The reference for the multiple-testing correction used in step 7.
