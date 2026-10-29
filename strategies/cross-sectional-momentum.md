# Cross-sectional momentum

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** weeks to months · **Repo project:** [Project 04](../projects/04-momentum-mean-reversion-study/)

## Idea

Stocks that have risen more over the past year tend to keep outperforming their peers over the following months. The strategy ranks a universe by past return, buys the top group, and avoids or shorts the bottom group. The effect was documented in US equities in the early 1990s and has been studied in many markets since.

## Research question

Does a 12-minus-1-month momentum signal earn a net-of-cost premium in NSE equities, and does it survive changes in market regime?

## Signal

For each stock on each rebalance date:

1. Compute the total return over the past 12 months, skipping the most recent month (to avoid short-term reversal). Call it R₁₂₋₁.
2. Keep only stocks whose price is above its 200-day moving average. This is a trend filter; state whether you apply it and test both versions.
3. Rank the remaining stocks on R₁₂₋₁.
4. Hold the top decile (or top third, for a smaller universe) with weights proportional to inverse volatility, scaled so the portfolio's volatility targets a stated level.

Rebalance monthly unless the research question says otherwise.

## Data

- Daily adjusted prices for NIFTY 500 constituents, from 2005 onward. See [data sources](../data/data-sources.md).
- Point-in-time index membership, so the universe on each date is the one that existed then.
- Corporate actions applied before any return is computed.

## Implementation notes

- Compute the signal with `shift` so the day's own close never enters its own decision.
- Use the same universe filters (minimum price, minimum traded value) on every date, and state them.
- Use the [performance metrics](../cheatsheets/performance-metrics.md) for every reported figure, including the deflated Sharpe ratio if you test variants.

## Costs

- Turnover of a monthly top-decile portfolio is high. Estimate it and charge costs per unit traded, using the components in [India trading costs](india-trading-costs.md).
- Shorting the bottom group is restricted in Indian cash equities. Test a long-only version as well, and report both.
- Impact grows with the size of the position relative to traded volume. Cap positions at a stated fraction of average daily volume.

## Evaluation

Report, for gross and net returns:

- Annualised return, volatility and Sharpe ratio.
- Maximum drawdown and its duration.
- Turnover per rebalance.
- The mean and standard error of the monthly long-short spread.
- Results split by sub-period, including any crash years. Momentum has had sharp reversals after market rebounds, so the drawdown matters as much as the average.

## What would show it does not work

- Net-of-cost Sharpe is not distinguishable from zero over the full sample.
- The premium is concentrated in a few months or a few stocks.
- Results disappear when the universe is restricted to point-in-time members.
- The trend filter is the only thing that makes the result look good.

## Common failure modes

- **Survivorship bias.** Today's index members have done well by construction.
- **Short-term reversal mixed in.** Using the most recent month, without skipping it, dilutes the signal.
- **Crash exposure.** A momentum portfolio can lose heavily in a sharp market rebound, after a period in which the market was falling.
- **Liquidity.** A top-ranked stock may be illiquid. Filter on traded value before ranking.

## Further reading

- Jegadeesh and Titman (1993), "Returns to Buying Winners and Selling Losers," *Journal of Finance*.
- Daniel and Moskowitz (2016), "Momentum Crashes," *Journal of Financial Economics*. The crash risk of momentum portfolios.
- Asness, Moskowitz and Pedersen (2013), "Value and Momentum Everywhere," *Journal of Finance*. Momentum across markets and asset classes.

See [papers](../resources/papers.md) for the full citations.
