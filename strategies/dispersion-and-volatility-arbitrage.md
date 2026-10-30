# Dispersion and volatility arbitrage

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** days to expiry · **Repo projects:** [Project 02](../projects/02-implied-vol-surface/) (the surface), [Project 14](../projects/14-finite-difference-black-scholes/) (pricing checks)

## Idea

An index's volatility is related to the volatilities and correlations of its components. When stocks move together, index volatility is high relative to single-stock volatility; when they move apart, the index is calmer. Options markets price this relationship, and it often differs from what the realised relationship turns out to be. A dispersion trade typically sells index volatility and buys single-stock volatility, earning the difference when correlation falls below its implied level. Volatility arbitrage is the broader family: trading implied volatility against realised volatility while hedging the exposures that are not the target.

This is more demanding than the [options relative-value](options-relative-value.md) file. It requires many option positions and a careful hedge.

## Research question

Over index and single-stock options on NSE, does implied correlation, backed out of index and component implied volatilities, exceed realised correlation on average, and does a hedged dispersion position earn a positive net return after costs?

## Theory

For an index of weights w_i and volatilities σ_i with pairwise correlation ρ, the index variance is

σ_index² = Σ w_i² σ_i² + Σ_(i ≠ j) w_i w_j ρ_ij σ_i σ_j

With equal weights and a single average correlation ρ, implied correlation is the value of ρ that makes the index volatility implied by the options equal to the one computed from the components. Compare implied correlation with realised correlation over the same window.

## Signal

1. For each expiry, compute index implied volatility and the implied volatilities of the largest components, using the surface method from [Project 02](../projects/02-implied-vol-surface/).
2. Compute implied correlation from these volatilities.
3. Compute realised correlation over the same window from daily returns.
4. Trade when the implied–realised gap exceeds a threshold set in advance: sell index volatility and buy component volatility in the weights implied by the index, or the reverse.

The position's vega is roughly neutral across the index and components. Its delta is hedged dynamically; the residual gamma and vega exposures are monitored, not hedged.

## Data

- Option chains with settlement prices for the index and its components, from NSE F&O data. See [data sources](../data/data-sources.md). Stale strikes are a major source of error.
- Daily returns for the components, for realised correlation.
- Component weights in the index and any changes over the sample.
- Risk-free rates for each expiry.

## Costs

- Option spreads on many strikes and components. A dispersion trade has many legs, so the spread cost multiplies.
- Margin for short index options and the long components.
- Hedging costs, from delta rebalancing across the components.
- Brokerage and transaction taxes on options, from [India trading costs](india-trading-costs.md).

## Evaluation

- Report the implied–realised correlation gap over the sample, with its distribution and its standard error.
- Report the net P&L of the hedged position per expiry.
- Report the vega, gamma and correlation exposures over time.
- Report stress: dispersion trades lose most in market-wide sell-offs, when correlations rise to one.
- Report the deflated Sharpe ratio across components, expiries and thresholds tried.

## What would show it does not work

- Implied correlation does not exceed realised correlation by enough to cover the costs of many legs.
- Losses in correlation spikes exceed the premium earned in calm periods.
- The strategy depends on component options that are too illiquid to trade at the modelled size.

## Common failure modes

- **Index and component mismatch.** Index options and component options settle at different times or use different calculations.
- **Correlation spikes.** Market sell-offs move correlations towards one, and the position loses on both sides.
- **Stale component prices.** A thinly traded component's settlement price may not reflect a real trade.
- **Hidden directional exposure.** Imperfect vega or delta neutrality leaves a bet on the market's direction.

## Further reading

- Driessen, Maenhout and Vilkov (2009), "The Price of Correlation Risk," *Journal of Finance*.
- Carr and Wu (2009), "Variance Risk Premiums," *Review of Financial Studies*.
- Sinclair, *Volatility Trading* 💸, on dispersion and correlation trades.
