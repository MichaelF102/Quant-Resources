# Evaluation framework

*Last reviewed: Oct 2026*

The checklist every strategy in this folder must pass before its results are reported. It applies to research notes, to projects, and to any backtest you run.

## 1. The pipeline

A strategy is a research and trading pipeline, not a single indicator. Each stage can invalidate the result, so each one needs a check.

| Stage | Question | Check |
|---|---|---|
| Data | Is the input what it claims to be? | Corporate actions applied; point-in-time membership; fundamentals lagged to filing dates; symbol mapping dated |
| Signal | Does the signal use only information available on the decision date? | Shift test; no centred windows; no same-bar fills |
| Portfolio | Are the weights sensible and feasible? | Position caps; liquidity filter; exposure limits |
| Execution and costs | What does trading cost? | Commissions, taxes, spread, impact, financing, borrowing |
| Validation | Does the result survive data it was not fitted on? | Out-of-sample period; walk-forward; sub-period stability |
| Monitoring | Would you know if it stopped working? | Predefined stop rules; drift monitoring of the signal |

## 2. Metrics

Do not judge a strategy by a single number. Report the set.

| Metric | What it tells you | Watch for |
|---|---|---|
| Net Sharpe ratio | Return per unit of volatility, after costs | Computed on excess returns; annualised with the right factor |
| Maximum drawdown and duration | Worst peak-to-trough loss and how long it lasted | A Sharpe can hide a long drawdown |
| CAGR | Compound annual growth | Depends on the start and end dates |
| Turnover | How much trading the strategy needs | Drives costs; report per rebalance and per year |
| Profit factor | Gross profit divided by gross loss | Easy to inflate with many small wins |
| Information coefficient | Relationship between forecasts and realised returns | Use rank correlation; report its standard error |
| Capacity | How much capital the strategy can deploy before costs erode returns | Estimate from volume and impact; state the assumption |
| Out-of-sample performance | Whether results survive data not used for fitting | Report the period and the number of decisions made in it |

Use the [performance metrics](../cheatsheets/performance-metrics.md) cheat sheet for formulas and the deflated Sharpe ratio.

## 3. Falsification checklist

Before reporting a strategy as working, write down what would show it does not. Then check each item.

- [ ] Net-of-cost Sharpe is distinguishable from zero, with a stated confidence interval.
- [ ] The result holds in at least two sub-periods, including one with a large drawdown.
- [ ] The result survives a realistic cost model, not only the zero-cost version.
- [ ] The result is not concentrated in one stock, sector, year or lookback.
- [ ] A simple benchmark (equal weight, buy and hold, or a random-entry baseline) is reported alongside.
- [ ] The number of variants tested is reported, and the deflated Sharpe ratio is computed for the best.
- [ ] The signal uses only data available on the decision date, which a shift test confirms.
- [ ] The universe is point-in-time, or survivorship bias is stated and bounded.

## 4. Reporting

- State the research question and the decision rule before the results.
- Report gross and net results, and the cost model.
- Report negative results. A strategy that fails the checklist is a finding.
- Keep the code and data manifest in version control, so a reader can rerun the result. See [version control and CI](../tools-and-technologies/version-control-and-ci.md).

## 5. Suggestions for this repo

Time-series momentum ([Project 16](../projects/16-time-series-momentum/)) and execution ([Project 17](../projects/17-optimal-execution/)) now have specs. Systematic macro still has none. A spec for it should follow [the spec template](../projects/TEMPLATE.md) and include the falsification checklist from this file in its done-when list.
