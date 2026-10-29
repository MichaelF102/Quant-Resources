# Market microstructure cheat sheet

*Last reviewed: Oct 2026*

How orders become trades. Used by the [Quant Developer roadmap](../roadmaps/quant-developer.md) (Phase 6), the [Quant Trader roadmap](../roadmaps/quant-trader.md) (Phase 5), and [Project 10](../projects/10-limit-order-book-simulator/) and [Project 11](../projects/11-market-making-simulation/).

## 1. Order types

| Order | Behaviour | Typical use |
|---|---|---|
| Market | Executes immediately at the best available prices | Urgent fills; pays the spread and any depth beyond the best quote |
| Limit | Executes at the limit price or better; otherwise rests in the book | Passive liquidity; controls price |
| Immediate-or-cancel (IOC) | Executes what it can at once, cancels the rest | Taking liquidity without leaving a resting order |
| Fill-or-kill (FOK) | Executes in full at once or not at all | All-or-nothing takers |
| Stop | Becomes a market (or limit) order when a trigger price trades | Risk limits; can gap through the trigger |
| Iceberg (reserve) | Shows only part of its size; refreshes from hidden quantity | Hiding size from other participants |
| Good-till-cancelled (GTC) and day | Time in force; how long a resting order stays | Day orders expire at the session close |

## 2. The order book

- **Bid:** the best price a buyer will pay. **Ask (offer):** the best price a seller will accept. The **spread** is ask minus bid.
- **Mid price:** (bid + ask) / 2.
- **Depth:** total quantity at each price level.
- **Level:** all orders at one price. Within a level, orders form a queue.

## 3. Matching rules

- **Price-time priority (FIFO):** better prices match first. Among orders at the same price, the earliest arrival matches first.
- **Pro-rata:** some futures markets split an incoming order across resting orders at the same price in proportion to their size.
- **Trade price:** a trade occurs at the price of the resting (passive) order.
- **Partial fills:** an order that is only partly filled keeps its place in the queue for its remaining quantity.
- **Replace:** reducing quantity keeps time priority. Changing price, or increasing quantity, usually loses it.

## 4. Auctions and sessions

- **Continuous trading:** orders match as they arrive, within a session.
- **Opening and closing auctions:** orders are collected, then a single price is set that maximises executed volume. The imbalance between buy and sell interest is published before the auction.
- **Pre-open session:** the Indian exchanges use a pre-open call auction before the regular session. Check the current timings in the NSE circulars, since they have changed over time.
- **Circuit limits:** exchanges halt or limit trading when a price moves beyond a set band. Treat limit-hit days as a special case in any backtest.

## 5. Costs and quality measures

- **Quoted spread:** ask − bid at the time of a trade.
- **Effective spread:** 2 × |trade price − mid| at the time of the trade. Captures price improvement.
- **Realised spread:** the effective spread minus the movement of the mid price after the trade, measured over a short horizon. It estimates what the liquidity provider kept.
- **Price impact:** how far the mid price moves after a trade. Large impact means the trade revealed information or consumed liquidity.
- **Implementation shortfall:** the difference between the decision price and the final average execution price, including unfilled quantity.

## 6. Adverse selection and inventory

- A market maker loses when trading against better-informed counterparties. The spread compensates for this as well as for holding cost.
- **Inventory:** holding a position while the price moves. A market maker shifts quotes to reduce inventory, as in the Avellaneda–Stoikov model (see [Project 11](../projects/11-market-making-simulation/)).
- **Toxic flow:** orders that consistently move the price against the market maker. Detect it with post-trade price moves.

## 7. Market data feeds

- **Level 1:** best bid, best ask, and the last trade.
- **Level 2:** the depth of several levels on each side.
- **Level 3 (full book):** every order, with its ID, price and quantity. Needed to rebuild the queue exactly.
- **Incremental feeds:** messages that add, modify, cancel and execute orders. The book must be rebuilt from them, and a gap in sequence numbers means messages were lost.

## 8. Nasdaq ITCH 5.0 message types

The main message types in the ITCH 5.0 specification, which you should confirm against the version you use:

| Type | Meaning |
|---|---|
| S | System event (start of messages, start and end of market hours) |
| A | Add order, without attribution |
| F | Add order, with market participant attribution |
| E | Order executed, against a resting order |
| C | Order executed with a different price than the resting order |
| X | Order cancel (partial) |
| D | Order delete (full cancel) |
| U | Order replace: a new order ID and price or quantity, which can lose priority |
| P | Trade message for a non-displayed order |

Reconstructing a book means applying each message to the order keyed by its reference number, in sequence.

## 9. Common mistakes

- Treating the last trade price as the fair value. It may be from a small trade or a stale level.
- Ignoring the queue position. Two orders at the same price do not have the same fill probability.
- Using quoted spread in a backtest that trades at the mid. The cost is the effective half-spread, not the quoted spread.
- Assuming an order fills at the price you see on a bar chart. A limit order fills only if the market trades through it.
- Forgetting circuit limits and auction periods in a daily backtest.

## 10. Interview favourites

- Why does a limit order placed at the best bid not always fill? The price may not trade, or the queue ahead of it may absorb the trades.
- What is the difference between quoted and effective spread? The effective spread measures what a trade actually paid relative to the mid, so it captures price improvement and the spread a marketable order crosses.
- Why does a market maker widen the spread after a news event? Adverse selection rises, because informed traders are more likely to be active.
- What is an iceberg order for? To hide size, so the market does not see the full quantity a trader wants to execute.
