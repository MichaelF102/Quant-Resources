# Market making

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** seconds to hours · **Repo projects:** [Project 10](../projects/10-limit-order-book-simulator/), [Project 11](../projects/11-market-making-simulation/)

## Idea

A market maker posts a bid and an ask, and earns the spread when both sides trade. The risks are inventory (holding a position that moves against it) and adverse selection (trading with someone who knows the price is about to move). Profitable market making is about pricing those two risks, not about predicting direction.

## Research question

Given a stated fill model and inventory limit, does a quoting rule earn a positive net return per unit of inventory risk, after the effects of adverse selection?

## Mechanics

- **Quote placement.** Bid and ask around a fair value, with a spread that covers costs and risk.
- **Inventory control.** Shift both quotes against the current position, so a long position makes it cheaper to sell and harder to buy. The [Avellaneda–Stoikov model](../projects/11-market-making-simulation/) gives one formal version.
- **Adverse selection.** Widen quotes when the order flow is informative, for example after a news event or when recent trades have moved the price against the maker.
- **Queue position.** A resting order fills only after the orders ahead of it. Fill probability depends on queue position and on how often the price trades through the level.

## Data

- Order book data (level 2 or full book) for the instrument. The [market microstructure](../cheatsheets/market-microstructure.md) cheat sheet explains the message types.
- Trade data with timestamps accurate to the millisecond at least.
- For a simulation, a calibrated arrival model for market orders. [Project 11](../projects/11-market-making-simulation/) uses a parametric one.

## Costs

- Exchange fees and rebates, which can make a passive order cheaper or dearer than a taker order. Check the fee schedule.
- Technology costs. A quoting strategy that needs very low latency may not be feasible outside a firm with that infrastructure.
- Regulatory obligations for market makers, which exist in some markets. Check the rules before any live quoting.

## Evaluation

- Report P&L as a distribution over simulated sessions, with the 5th percentile, not only the mean.
- Report average inventory and the time spent above an inventory limit.
- Decompose P&L into spread capture, inventory change and adverse selection.
- In a backtest on recorded data, state the fill model. A fill that assumes the quote always trades overstates P&L.

## What would show it does not work

- Spread capture is smaller than the adverse selection cost.
- The strategy loses money in fast markets, when inventory moves most.
- The result depends on an optimistic fill model that the data does not support.

## Common failure modes

- **Optimistic fills.** Assuming a quote is filled whenever the price touches it.
- **Ignoring the end of session.** Inventory must be closed, and the cost of closing it is part of the result.
- **Latency assumptions.** A simulation with zero latency is not a model of a live market.

## Further reading

- Avellaneda and Stoikov (2008), "High-frequency trading in a limit order book," *Quantitative Finance*.
- Glosten and Milgrom (1985), "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders," *Journal of Financial Economics*.
- Harris, *Trading and Exchanges* 💸, on the institutions of market making.
