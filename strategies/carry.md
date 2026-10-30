# Carry

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** weeks to months · **Repo project:** none yet

## Idea

Carry is the return an asset earns if its price does not change. A high-yielding currency, a bond with a steep roll-down, or a commodity future in backwardation earns carry as long as its price stays put. Carry strategies buy the high-carry assets and sell the low-carry ones. The return is compensation for risk: high-carry assets tend to fall when risk appetite falls, so carry trades suffer in sharp reversals. The premium is the average net of those losses.

Carry appears in several asset classes at once. The [systematic macro](systematic-macro.md) file uses it as one signal. This file treats it as a strategy family in its own right.

## Research question

Across a diversified set of currencies, bond futures and commodity futures, does a carry ranking earn a positive net premium that survives costs, and how large are its losses in risk-off periods?

## Signal

For each asset on each rebalance date:

- **Currencies:** the interest-rate differential between the currency and the base currency. Use the forward discount, or the difference of short-term deposit rates, and state which.
- **Bond futures:** the yield of the bond minus the financing rate, or the roll-down along the curve.
- **Commodity futures:** the roll yield, computed from the front and next contract prices on a stated calendar.

Rank the assets each month, go long the top group and short the bottom group, and weight by inverse volatility so that each position carries similar risk.

## Data

- Short-term interest rates for each currency or country, from official or reliable sources, with dates.
- Futures prices for each contract along the curve, with a stated roll rule.
- Currency spot and forward prices, or the rates needed to derive the forward discount.

For Indian instruments, check the availability of liquid bond and currency futures with enough history. A short history is a reason to test on comparison markets and say so.

## Costs

- Futures roll costs and margin.
- Currency conversion costs for an investor in another base currency.
- Financing costs for holding bonds, which reduce the carry itself. Net financing is part of the return, not a separate cost.

## Evaluation

- Report the long-short return per asset class and for the portfolio, net of costs.
- Report the correlation of carry with equity returns, and its performance in the worst equity months.
- Report the crash profile: the largest monthly loss, and how long the drawdown lasted.
- Report the deflated Sharpe ratio across signal definitions tried.

## What would show it does not work

- The long-short spread is small relative to its drawdowns.
- Returns depend on one currency or one period.
- The strategy's gains disappear once financing and roll costs are included.

## Common failure modes

- **Carry is not free.** Ignoring the currency or price move that offsets the yield gives a return that looks riskless and is not.
- **Interest-rate data revisions.** A rate series revised later gives returns that were not available at the time.
- **Crowding and unwinds.** Carry trades can unwind sharply and together, so the worst month can be much worse than the average suggests.

## Further reading

- Koijen, Moskowitz, Pedersen and Vrugt (2018), "Carry," *Journal of Financial Economics*. Carry across asset classes.
- Ilmanen, *Expected Returns* 💸, chapters on carry and its risks.
- Asness, Moskowitz and Pedersen (2013), "Value and Momentum Everywhere," *Journal of Finance*.
