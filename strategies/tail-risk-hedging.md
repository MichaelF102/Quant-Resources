# Tail-risk hedging

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** continuous, rolled as contracts expire · **Repo projects:** [Project 12](../projects/12-risk-engine-var-es/) (stress and tail measures), [Project 02](../projects/02-implied-vol-surface/) (option prices)

## Idea

Tail-risk hedging is not a return strategy in the usual sense. It buys protection against rare, large losses in a portfolio, paying a steady premium in calm periods. The premium is the cost of insurance: options and volatility products are priced to reflect the risk they cover, so protection usually has a negative expected return on its own. The question is whether the protection, in the scenarios that matter, is worth what it costs in the others.

Some strategies in this folder, such as [short-volatility option selling](options-relative-value.md) and [cross-sectional momentum](cross-sectional-momentum.md) crash exposure, are the risks that a tail hedge is designed to offset. A portfolio with those exposures should be evaluated with and without its hedge.

## Research question

For a stated equity or multi-asset portfolio, does a rolling programme of out-of-the-money puts, put spreads or a volatility overlay reduce the loss in the worst periods by more than its cost in ordinary periods, and what is the net effect on long-run return and risk?

## Instruments

- **Index puts.** Long out-of-the-money puts on the index, rolled before expiry. Simple, but expensive when volatility is already high.
- **Put spreads.** Long a put and short a further out-of-the-money put. Cheaper, but protection stops at the lower strike.
- **Volatility products.** Variance or volatility exposure through options or futures. Their payoff depends on the realised path, not only the final level.
- **Trend overlays.** Reducing exposure when a trend signal turns negative. These are not options, but they cut the same losses at a lower premium, with the risk of whipsaw.

## Method

1. Define the portfolio to be protected, with its exposure and its historical worst periods.
2. Define the hedge: instrument, strike or signal, expiry, roll rule and notional, all fixed before the test.
3. Price the hedge each period using the surface method from [Project 02](../projects/02-implied-vol-surface/), and check the prices against a model.
4. Compare the hedged and unhedged portfolio over the same dates, with the hedge's full cost included.

## Data

- Index and option prices for the portfolio's exposures, including the full strike range, from the NSE derivatives data. See [data sources](../data/data-sources.md).
- Historical stress periods, defined in advance by date. Do not select the periods after seeing the hedge's results.
- Volatility index data as a benchmark for hedge pricing.

## Costs

- The premium paid each roll. This is the main cost and is paid in almost every period.
- Bid-ask spreads on options, which are wide in far out-of-the-money strikes.
- Margin and capital tied up in the hedge, which lowers returns on the rest of the portfolio.
- Taxes and charges on each option trade, from [India trading costs](india-trading-costs.md).

## Evaluation

- Report the hedged and unhedged portfolio's return, volatility, maximum drawdown, and worst monthly loss, all net of hedge cost.
- Report the hedge's payoff in each stress period, separately.
- Report the cost of the hedge in calm periods, as an annual drag.
- Report the sensitivity of the result to the strike and tenor chosen. A hedge that works at one strike and fails at the next is fragile.
- Report the deflated Sharpe ratio across strikes, tenors and rules tried.

## What would show it does not work

- The hedge's annual cost exceeds the reduction in losses over the sample, net of the portfolio's own risk.
- The payoff comes from one stress period, and the hedge fails in others.
- The hedge is only effective when bought at low volatility, which is not a reliable pattern to rely on.

## Common failure modes

- **Hedging after the crash.** Buying protection once volatility has spiked is expensive, and the spike has already happened.
- **Basis risk.** A hedge on an index does not fully protect a portfolio of different stocks.
- **Roll timing.** A hedge that rolls at one fixed point can be out of the money during the very period it is needed.
- **Assuming the tail is known.** Historical worst periods are a small sample. A hedge sized to them may be too small or too large.

## Further reading

- Kelly and Jiang (2014), "Tail Risk and Asset Prices," *Review of Financial Studies*. Tail risk as a priced factor.
- Carr and Wu (2009), "Variance Risk Premiums," *Review of Financial Studies*. The premium that volatility buyers pay.
- Daniel and Moskowitz (2016), "Momentum Crashes," *Journal of Financial Economics*. A tail risk that a hedge can target.
