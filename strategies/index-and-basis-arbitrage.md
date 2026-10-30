# Index and basis arbitrage

*Last reviewed: Oct 2026*

**Difficulty:** intermediate to advanced · **Holding period:** intraday to expiry · **Repo project:** none yet

## Idea

A futures contract on an index must trade at a price that reflects the cost of holding the underlying until expiry. If the futures price drifts too far above that cost-of-carry price, a trader can sell the futures and buy the basket, locking in the difference at expiry. The reverse works when futures trade too cheap. The difference between futures and spot is the basis. Basis arbitrage is the trade of closing that gap when it is wide enough to cover the costs.

For Indian markets this is the cash–futures arbitrage that exchange-traded index and stock futures make possible. It is one of the most direct arbitrages in the market, and its profitability depends almost entirely on costs and on how well the basket tracks the index.

## Research question

After all transaction costs, financing and tracking error, does the basis of NIFTY futures and of liquid stock futures exceed the cost of carry often enough to earn a positive return, and how much capital does the trade need?

## Theory

With continuous dividend yield q and risk-free rate r, the fair futures price is

F = S e^((r − q) T)

The cash–futures arbitrage is profitable when the market futures price exceeds F by more than the costs of the trade. The threshold is:

- Long the basket and short the futures when F_market > S e^((r − q)T) + costs.
- Short the basket and long the futures when F_market < S e^((r − q)T) − costs, if shorting the basket is feasible.

The threshold is the key output: the basis must exceed the costs of buying the basket, selling the future, financing, and the expected tracking error, before the trade pays.

## Signal

1. Compute the fair futures price each minute or each day, using the spot index or the basket, the risk-free rate for the remaining time, and the dividend yield expected before expiry.
2. Compute the basis: market futures price minus fair price.
3. Trade when the net basis, after costs, exceeds a threshold set in advance.
4. Close the position at expiry, or when the basis converges to fair value.

Expected dividends are a major input. An error in expected dividends becomes a false basis. Use the company dividend announcements, not a guess.

## Data

- Index or stock futures prices and spot prices at the same timestamps. Synchronisation matters: a few seconds of mismatch can create a false basis.
- The risk-free rate for each expiry, from RBI government securities data.
- Dividend announcements and record dates for each constituent.
- Contract specifications for lot size and expiry, recorded by date. See [India markets](../careers/india-markets.md).
- For exchange-traded fund arbitrage, the ETF's net asset value and creation and redemption rules, where available.

## Costs

- Brokerage, exchange and clearing charges on both legs, and transaction taxes on futures and on delivery, with rates from [India trading costs](india-trading-costs.md).
- Spread on each leg. Basket trades cross the spread on every stock.
- Margin and financing for the futures position.
- Tracking error: the basket will not match the index exactly. Estimate it from historical differences.
- Settlement at expiry, which depends on the contract's settlement method. Check the rules for the period tested.

## Evaluation

- Report the distribution of net basis captured per trade, not only the average.
- Report the number of trades per month and the capital employed.
- Report the return on capital employed, net of all costs, and the time to convergence.
- Report the frequency of failed convergence, where the basis widened at expiry or the basket moved against the futures.

## What would show it does not work

- The basis rarely exceeds the costs in the sample period.
- Profitable trades are concentrated in a few days of unusual volatility, when fills are hardest.
- The strategy depends on an assumed dividend forecast that cannot be observed in advance.

## Common failure modes

- **Synchronisation error.** Spot and futures timestamps that differ create a basis that does not exist.
- **Dividend misestimation.** An unexpected dividend moves the fair price.
- **Basket tracking error.** A basket of the index's stocks may not track it closely, especially in stress.
- **Settlement and expiry risk.** The futures settle on a stated price on expiry day, which may differ from the spot price the trader expected.

## Further reading

- Hull, *Options, Futures, and Other Derivatives* 💸, chapters on futures pricing and the cost of carry.
- Exchange circulars on index futures and on arbitrage margin. Check the current rules before relying on any figure.
