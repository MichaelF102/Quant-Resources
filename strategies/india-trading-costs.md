# India trading costs

*Last reviewed: Oct 2026 · Rates change. This file lists the cost components and how to model them. It does not give rates. Look up each rate on the broker's schedule and the exchange and government sources for the period you are testing.*

A backtest of an Indian strategy is only as good as its cost model. The components below apply to equities, futures and options. Missing one of them, or using a rate from the wrong period, can change the result enough to reverse a conclusion.

## 1. Components

| Component | What it is | Where it applies | Where to check the rate |
|---|---|---|---|
| Brokerage | Fee charged by the broker per order or per turnover | All segments | The broker's published tariff |
| Securities transaction tax (STT) | Government tax on the traded value, at different rates for delivery, intraday and derivatives | All segments, with different rates | The government's current tax notification |
| Exchange transaction charges | Fee charged by the exchange on traded value | All segments | The exchange's fee schedule |
| Clearing charges | Fee charged by the clearing corporation | All segments | The clearing corporation's schedule |
| SEBI turnover fee | Regulator's fee on traded value | All segments | SEBI's published fee |
| Stamp duty | State duty on the purchase of securities | Delivery purchases | The applicable state rate |
| GST | Goods and services tax on brokerage and exchange charges | Charges, not on traded value | The current GST rate for financial services |
| Bid-ask spread | Cost of crossing the spread on a market order | All segments | Measured from the order book data |
| Market impact | Price movement caused by your own order | Larger orders | Estimated from volume and a stated model |
| Financing and margin | Cost of capital tied up in positions and margin | Futures, options, leveraged positions | The broker's margin and interest terms |
| Short-selling cost | Borrowing cost, or the cost of a futures or option position used to short | Short positions | The broker's terms, or the futures basis |

## 2. Modelling approach

1. **Separate delivery from intraday.** Cash equity delivery and intraday trades carry different tax and stamp rules. A strategy that holds overnight pays the delivery costs.
2. **Use the rate in force on each trade date.** Rates have changed over the sample period. Store the rate schedule with its effective dates.
3. **Apply costs per leg.** A pair trade has two legs, each with its own spread and charges.
4. **Charge the spread on crossing.** A limit order that rests does not pay the half-spread, but it may not fill. Model fills explicitly.
5. **Model impact separately.** Use a stated impact model (see [execution and impact](execution-and-impact.md)), and test its sensitivity.
6. **Report the cost breakdown.** A reader should be able to see how much of the gross return each component consumed.

## 3. A cost template

Use a table like this in the strategy's README, filled in from the sources for the period tested.

| Parameter | Value used | Effective from | Source |
|---|---|---|---|
| Brokerage per order | to fill | to fill | Broker tariff, dated |
| STT (delivery buy and sell) | to fill | to fill | Government notification, dated |
| STT (intraday, sell side) | to fill | to fill | Government notification, dated |
| STT (derivatives) | to fill | to fill | Government notification, dated |
| Exchange charges | to fill | to fill | Exchange schedule, dated |
| SEBI fee | to fill | to fill | SEBI, dated |
| Stamp duty | to fill | to fill | State rate, dated |
| GST on charges | to fill | to fill | Government notification, dated |
| Half-spread assumption | to fill | — | Measured from data |
| Impact model and parameters | to fill | — | State the model |

## 4. Common mistakes

- Using a single flat rate for all segments and periods.
- Applying the delivery rate to an intraday strategy, or the reverse.
- Forgetting that GST applies to the charges, not to the traded value.
- Ignoring stamp duty on purchases in a long-only delivery strategy.
- Assuming a limit order fills at the mid price without a fill model.
- Modelling costs only on entry, and forgetting exits.

## 5. Checklist

- [ ] Each component in section 1 is included, or its exclusion is justified.
- [ ] Rates are dated and sourced, and the rate for each trade date is used.
- [ ] Delivery and intraday are modelled separately.
- [ ] Spread, impact and financing are modelled, not assumed to be zero.
- [ ] A cost breakdown is reported with the net results.
