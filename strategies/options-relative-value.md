# Options relative value

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** days to expiry · **Repo projects:** [Project 02](../projects/02-implied-vol-surface/), [Project 14](../projects/14-finite-difference-black-scholes/)

## Idea

Options carry a price for volatility. Implied volatility is what the market charges for future variance; realised volatility is what actually happens. On average, implied volatility has tended to exceed subsequently realised volatility, and the gap is called the variance risk premium. Relative-value strategies try to earn that premium, or to trade mispricing between strikes, expiries and related options, while hedging the exposures that are not the target.

## Research question

After hedging delta and controlling vega and gamma, does selling options on NIFTY earn a positive net premium relative to subsequently realised volatility, and is the premium stable across sub-periods?

## Methods

- **Variance risk premium.** Compare implied volatility with subsequent realised volatility over the option's life. Report the average gap and its standard error.
- **Vol surface relative value.** Compare the implied volatility of options at different strikes or expiries against a fitted surface, as in [Project 02](../projects/02-implied-vol-surface/). A deviation from a smooth surface is a candidate signal.
- **Calendar and skew trades.** Positions that profit if the term structure or the skew moves towards a model's prediction.
- **Dispersion.** Trades the difference between index volatility and the volatility of its components. Requires many single-stock options and is hard to execute in a market with limited liquidity.

## Data

- Option chain data with settlement prices, open interest and volume. The NSE F&O bhavcopy supplies daily settlement prices. See [data sources](../data/data-sources.md).
- Realised volatility computed from index or stock returns over matching windows.
- The risk-free rate for each expiry, from the RBI's T-bill data.

## Hedging and exposures

- Delta-hedge with the underlying or futures, rebalanced at a stated frequency. The hedging frequency affects both P&L and costs.
- Report the net exposure to gamma, vega and theta, not only delta.
- Know which option's price is the input: settlement prices may be stale for illiquid strikes.

## Costs

- Option bid-ask spreads are wide for most strikes. Use the mid price only where the spread is small, and report the spread cost separately.
- Brokerage, exchange charges and taxes on options and futures, as in [India trading costs](india-trading-costs.md).
- Margin requirements for short options. A strategy that needs more capital than it can hold is not feasible.

## Evaluation

- Realised P&L of a hedged position, net of costs, with its distribution across expiries.
- Vega-weighted and gamma-weighted exposure over time.
- Drawdown, paying particular attention to volatility spikes. Short-volatility strategies lose most in the periods when volatility rises quickly.
- The deflated Sharpe ratio across strikes, expiries and rules tried.

## What would show it does not work

- The variance risk premium is not significantly different from zero after costs.
- The strategy's losses in volatility spikes wipe out its gains in calm periods.
- The premium disappears when the hedging frequency is realistic.

## Common failure modes

- **Short-volatility blow-ups.** Selling options collects a small, steady premium and can lose heavily in one event. Measure the tail.
- **Stale prices.** Using a settlement price for a strike that did not trade.
- **Mismatched windows.** Comparing implied volatility with realised volatility over different horizons.

## Further reading

- Carr and Wu (2009), "Variance Risk Premiums," *Review of Financial Studies*.
- Sinclair, *Volatility Trading* 💸, on the practice of volatility relative value.
- Gatheral, *The Volatility Surface* 💸, on fitting surfaces and checking for arbitrage.
