# 17 — Optimal execution: schedules, impact and shortfall

**Proves:** the trade-off between market impact and timing risk, the Almgren–Chriss optimal schedule, implementation shortfall as a cost measure, and the difference between a benchmark (VWAP) and a cost-minimising schedule
**Level:** 🔴 · **Time:** 2–3 weekends
**Prerequisites:** [Strategies: execution and market impact](../../strategies/execution-and-impact.md); [Project 10](../10-limit-order-book-simulator/) is useful but not required; [Stochastic calculus cheat sheet](../../cheatsheets/stochastic-calculus.md); [Performance metrics](../../cheatsheets/performance-metrics.md)

## Goal

Build a simulator of a single stock's price and volume over one trading day, then execute a large parent order with three schedules: TWAP, VWAP, and the Almgren–Chriss optimal schedule. Compare their implementation shortfall, and show how the optimal schedule changes with risk aversion. The question: how much execution cost does a cost-aware schedule save, and at what cost in timing risk?

## Data

Synthetic. Use a fixed seed and record every parameter.

- **Price:** arithmetic Brownian motion within the day, with volatility σ per day and a starting price of 100.
- **Impact:** a temporary impact that depends on the rate of trading and a permanent impact that depends on the total quantity traded, with coefficients η and γ.
- **Volume profile:** an intraday U-shape, with more volume at the open and close, scaled to a daily volume V.
- **Parent order:** X shares to buy, over T trading intervals.

Optional: a day of LOBSTER data, if you have it, for a calibration check. See [data sources](../../data/data-sources.md).

## Steps

1. **Simulate the market.** Generate 10,000 days of prices and volumes from the parameters above, with the seed recorded.
2. **TWAP.** Split X evenly across the T intervals. Record the average execution price and the implementation shortfall against the decision price.
3. **VWAP.** Split X in proportion to the volume profile. Record the same measures.
4. **Almgren–Chriss.** Compute the optimal schedule for risk-aversion parameter λ, with κ = √(λσ²/η̃), where η̃ is the temporary-impact coefficient adjusted for the interval length, as in the paper. The holdings after time t follow x(t) = X sinh(κ(T − t)) / sinh(κT). Trade the difference between consecutive holdings. Check the paper for the exact discretisation before implementing it.
5. **Closed-form check.** For a trivially small order, the schedule should approach a linear TWAP. Test that the schedule and its limit match.
6. **Sweep risk aversion.** Run λ over at least four values. For each, record the expected shortfall and its standard deviation across simulated days.
7. **Efficient frontier.** Plot expected shortfall against the standard deviation of shortfall for each schedule. The optimal schedules should trace a curve; TWAP and VWAP should sit on or inside it.
8. **Sensitivity.** Vary η and γ by ±50% and report how the ranking of schedules changes.

## Done when

- [ ] The simulator is seeded, and the same seed gives identical prices and fills on two runs
- [ ] The closed-form check passes: the schedule sums to X and its holdings decrease monotonically
- [ ] Implementation shortfall is reported for TWAP, VWAP and Almgren–Chriss, as means and standard deviations over at least 10,000 days
- [ ] The risk-aversion sweep shows the trade-off: higher λ gives faster trading, lower timing risk and higher impact
- [ ] The sensitivity test reports whether the ranking of schedules changes, and at which parameter values
- [ ] The write-up states the cost saving of the best schedule, and what it costs in shortfall variance

## Common pitfalls

- **Sign errors.** Buying and selling have opposite signs in both the impact and the shortfall. Test a sell order as well as a buy.
- **Comparing schedules on different parent orders.** Use the same X, T and random seeds for all three.
- **Reporting only the mean shortfall.** A schedule with a lower mean and a much higher variance can be a worse choice. Report both.
- **Confusing κ units.** κ depends on the interval length. Check the units against the paper before comparing schedules.
- **Ignoring the decision price.** Implementation shortfall is measured against the price when the decision was made, not the day's open.

## Stretch goals

- Replace the synthetic price with a day of LOBSTER data, and calibrate η and γ to the observed book.
- Add a limit-order option: a passive schedule that waits for fills at a stated price, and compare its fill rate and shortfall.
- Use a volume forecast from past days in place of the known profile, and measure the cost of the forecast error.

## Further reading

- Almgren and Chriss (2000), "Optimal Execution of Portfolio Transactions," *Journal of Risk*. The model implemented here.
- Perold (1988), "The Implementation Shortfall: Paper Versus Reality," *Journal of Portfolio Management*. The cost measure.
- Almgren, Thum, Hauptmann and Li (2005), "Direct Estimation of Equity Market Impact," *Risk*. An empirical impact law.
