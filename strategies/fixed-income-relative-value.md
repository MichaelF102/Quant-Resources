# Fixed-income relative value

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** weeks to months · **Repo project:** none yet; the cheat sheets [fixed income](../cheatsheets/fixed-income.md) and [credit risk](../cheatsheets/credit-risk.md) cover the maths

## Idea

Bonds, swaps and futures on the same underlying rates should price consistently with each other. When they do not, a trader can take offsetting positions that profit as prices converge. Typical trades are yield-curve positions (steepeners and flatteners), swap-spread trades (the difference between swap rates and government bond yields of the same maturity), and bond-futures basis trades. The trades are hedged against the level of rates, so they take a view on relative value, not on direction.

## Research question

Do relative-value spreads in government bonds, swap rates and bond futures, hedged for duration, revert to their historical averages over a stated horizon, and does a rule based on those spreads earn a positive net return after financing and transaction costs?

## Trades

- **Curve trades.** Long one maturity and short another, with the notional chosen so DV01s match. The trade takes a view on the shape of the curve.
- **Swap spread.** Pay the fixed leg of a swap and receive the government bond yield, or the reverse, hedged for duration. The spread reflects credit, liquidity and supply.
- **Bond futures basis.** Buy the cash bond and sell the futures, weighted by the conversion factor. The basis is the difference between the cash price and the futures-implied price.
- **Credit basis.** The difference between a bond's credit spread and its CDS spread. See [credit risk](../cheatsheets/credit-risk.md).

## Signal

1. Compute the spread for each trade, from a consistent data source, on a daily basis.
2. Standardise the spread against its trailing mean and volatility, with a window set in advance.
3. Enter when the z-score exceeds a threshold, and exit when it returns to its mean or after a stated time.
4. Hedge duration with DV01-matched offsetting positions. Recompute the hedge when rates move.

## Data

- Government bond yields and prices by maturity, from official sources where available. Check the bootstrapping and interpolation used for the curve; see [fixed income](../cheatsheets/fixed-income.md).
- Swap rates for the same maturities.
- Bond futures prices, contract specifications and conversion factors.
- Liquidity and bid-ask data for the instruments traded. Thin markets widen the apparent spread.

## Costs

- Bid-ask spread on each leg, which is large for less liquid maturities.
- Financing and repo costs for holding bonds. The carry on a bond position can be larger than the spread, so financing must be modelled.
- Transaction costs and margin on futures.
- Hedge rebalancing costs as rates move.

## Evaluation

- Report the trade's return net of financing, carry and costs, per trade and as a portfolio.
- Report the hedge's residual exposure to the level and slope of the curve. A hedge that leaves large residual exposure is a directional bet.
- Report stress behaviour: spreads can widen sharply in funding crises, when a leveraged trade is forced to close.
- Report the deflated Sharpe ratio across spreads and thresholds tried.

## What would show it does not work

- The spread does not revert within the holding period, or reverts too slowly to cover financing.
- The trade's losses come from a single funding or liquidity episode.
- Net returns are negative after financing and costs, even when the spread reverts.

## Common failure modes

- **Carry ignored.** A position that earns a small spread but pays a larger financing cost loses money while the spread is right.
- **Structural change.** A new regulation, a change in supply or a benchmark change can move a spread to a new level permanently.
- **Leverage and forced exits.** Relative-value trades are often highly levered, so a temporary spread widening can force a loss before reversion.

## Further reading

- Tuckman and Serrat, *Fixed Income Securities* 💸, on curve and basis trades.
- Hull, *Options, Futures, and Other Derivatives* 💸, on futures pricing and the cost of carry.
- Duffie (1996), "Special Repo Rates," *Journal of Finance*, for repo-driven price effects in bond markets.
