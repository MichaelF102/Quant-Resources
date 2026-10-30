# Post-earnings announcement drift

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** days to weeks · **Repo project:** none yet

## Idea

When a company reports earnings that are much better or worse than expected, its share price adjusts on the announcement, but not completely. Prices continue to drift in the direction of the surprise over the following weeks. The effect was documented in the late 1960s and has been studied extensively since. It is one of the few event-based anomalies with a long record across markets.

## Research question

In NSE equities, does a standardised earnings surprise predict returns over the 60 trading days after the announcement, net of costs, and is the drift larger for surprises that are harder to explain by other information?

## Signal

1. **Measure the surprise.** Actual earnings per share minus a forecast, scaled by the price or by the volatility of past surprises. Define the forecast before testing: a seasonal random walk (the same quarter last year plus the average change) is a common, simple choice.
2. **Use the announcement date**, not the fiscal period end. The surprise becomes information on the date it is published. Use the exchange filing time, and treat any announcement after market hours as the next trading day.
3. **Rank surprises** each announcement period. Go long the highest-surprise group and short the lowest, or hold long only, for a stated holding period.
4. **Exit** after the holding period, or on a stated stop.

## Data

- Earnings announcement dates from exchange filings, with time of release. Dates are point-in-time information; do not use the date a vendor later recorded.
- Quarterly earnings per share as first reported, and the history of estimates if the surprise uses analyst forecasts. Analyst estimate databases are usually paid.
- Daily adjusted prices and volume, with corporate actions applied.

## Costs

- Turnover is high around announcement seasons and low between them. Costs cluster in the same weeks.
- Small companies have wide spreads and fewer analysts. The drift is often larger in those stocks, and so are the costs.
- Charge costs on traded value using [India trading costs](india-trading-costs.md), and apply a liquidity filter before ranking.

## Evaluation

- Report the abnormal return over the holding period for each surprise group, using a market model or a size-and-value adjusted benchmark.
- Report the drift by size bucket and by liquidity bucket.
- Report the result with and without the first few days after announcement, since some of the response is immediate.
- Report the deflated Sharpe ratio across surprise definitions and holding periods tried.

## What would show it does not work

- The drift is not significantly different from zero after costs.
- The effect is concentrated in micro-cap stocks that cannot be traded at the modelled size.
- Results depend on a surprise definition chosen after looking at the data.

## Common failure modes

- **Wrong announcement timing.** Treating a post-market announcement as if it were known at the open.
- **Vendor-revised earnings.** Using later-corrected figures in place of the originally reported ones.
- **Analyst forecasts with look-ahead.** Forecasts recorded after the announcement, or from a database that was updated later.

## Further reading

- Ball and Brown (1968), "An Empirical Evaluation of Accounting Income Numbers," *Journal of Accounting Research*. The original study.
- Bernard and Thomas (1989), "Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?," *Journal of Accounting Research*.
- Hirshleifer, Lim and Teoh (2009), "Driven to Distraction: Extraneous Events and Underreaction to Earnings News," *Journal of Finance*.
