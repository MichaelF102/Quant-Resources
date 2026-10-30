# Order-flow imbalance

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** seconds to minutes · **Repo projects:** [Project 10](../projects/10-limit-order-book-simulator/) (book reconstruction), [Project 11](../projects/11-market-making-simulation/) (quoting)

## Idea

The order book records the intentions of the market's participants: how much buying and selling interest sits at each price, and how that changes. When buy orders are added or sell orders cancelled faster than the opposite, the price tends to move in the direction of the imbalance over the next few events. Order-flow imbalance is a short-horizon signal built from these book changes. It is the microstructure counterpart of the market-making ideas, and it is used by liquidity providers to decide when to skew their quotes.

## Research question

Does the net order-flow imbalance at the best bid and ask, computed from recorded book events, predict the next short-horizon mid-price change in a liquid stock, and does the prediction survive the spread and fees paid to trade on it?

## Signal

For each event in the order book (add, cancel, or execute on each side):

1. Compute the change in depth at the best bid and best ask, separately for each event type. Following Cont, Kukanov and Stoikov (2014), define the order-flow imbalance as the sum of signed depth changes at the best quotes over a time window.
2. Aggregate over a fixed window, such as 10 seconds or 100 events.
3. Regress the next mid-price change on the imbalance. The slope is the price impact per unit of imbalance.
4. Trade when the predicted move exceeds the half-spread plus fees.

The predicted move is only useful if it is larger than the cost of crossing the spread. Most of the signal's value is absorbed by that cost.

## Data

- Full order book data with event timestamps, such as LOBSTER samples or the exchange's depth feeds. See [data sources](../data/data-sources.md).
- Trade records, for matching executions to book events.
- Sequence numbers, to detect gaps in the data. A gap changes the book and corrupts the imbalance.

## Costs

- The bid-ask spread: a market order crosses it, and a passive order may not fill.
- Exchange fees and rebates, which differ between passive and aggressive orders.
- Latency. The signal decays within seconds, so a strategy that trades after a delay captures only part of it.

## Evaluation

- Report the R² and slope of the price-change regression by window length.
- Report the predicted-move distribution against the spread, and the fraction of signals large enough to cover the cost.
- Report the net profit per trade after spread and fees, under a stated fill model.
- Report results in several market conditions: a calm session and a volatile one.

## What would show it does not work

- The signal is positive but smaller than the spread for most events.
- The result depends on fills at the mid price, which a resting order does not get.
- The predictive power falls off within a second or two of the event.

## Common failure modes

- **Fill optimism.** Assuming an aggressive order fills at the best quote without considering queue position.
- **Timestamp errors.** Events recorded out of order produce spurious imbalance.
- **Ignoring the market's own reaction.** Once a signal is widely used, the price adjusts before the signal is acted on.

## Further reading

- Cont, Kukanov and Stoikov (2014), "The Price Impact of Order Book Events," *Journal of Financial Econometrics*.
- Harris, *Trading and Exchanges* 💸, on the order book and its participants.
- Glosten and Milgrom (1985), "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders," *Journal of Financial Economics*.
