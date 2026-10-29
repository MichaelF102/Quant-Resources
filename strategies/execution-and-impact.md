# Execution and market impact

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** minutes to days (the execution horizon) · **Repo projects:** [Project 17](../projects/17-optimal-execution/), with [Project 10](../projects/10-limit-order-book-simulator/) for the book

## Idea

Every strategy trades, and the cost of trading can be as large as the signal. Execution research asks how to trade a given quantity: how fast, in what slices, and with which order types. The central trade-off: trading quickly pushes the price against you (market impact), while trading slowly leaves you exposed to price movement while you wait (timing risk).

## Research question

For a stated order size and horizon, does a schedule that balances impact against timing risk beat a simple time-weighted schedule (TWAP) or a volume-weighted schedule (VWAP), after realistic impact costs?

## Benchmarks

- **TWAP.** Split the order evenly across time. Simple, and a useful baseline.
- **VWAP.** Split the order in proportion to the expected volume profile. Tracks the day's volume-weighted average price, which is a common benchmark, but it is not a cost minimiser on its own.
- **Implementation shortfall.** The difference between the decision price and the final average execution price, including unfilled quantity. This is the cost measure most research uses. The concept was introduced by Perold (1988).

## Model

The Almgren–Chriss framework (2000) chooses a trading schedule that minimises expected cost plus a penalty for timing risk. The model splits impact into a temporary part, which depends on the rate of trading, and a permanent part, which depends on the total quantity traded. The optimal schedule trades faster at the start and slows down as the risk-aversion parameter rises.

A common empirical impact law is the square-root law: impact grows with the square root of the order size relative to daily volume. Almgren et al. (2005) estimated this on institutional equity orders.

## Data

- Trade and quote data, for estimating spread, volume profile and volatility.
- Order-level data from a broker or a simulator, if available, for calibrating impact.
- In a study without order data, state the impact model as an assumption, and test its sensitivity.

## Costs

The cost of execution is the output of this research, so it is not an extra term to add later. Decompose it into:

- Explicit costs: brokerage and exchange charges, as in [India trading costs](india-trading-costs.md).
- Spread: half the bid-ask spread on each market order.
- Temporary impact: the extra price paid for trading quickly.
- Permanent impact: the price move that stays after the trade.
- Timing risk: the variance of the outcome from waiting.

## Evaluation

- Implementation shortfall, mean and distribution, for each schedule on the same set of orders.
- Compare schedules across volatility regimes and times of day.
- Report the sensitivity of the optimal schedule to the impact parameters. A schedule that is optimal only at one parameter value is fragile.

## What would show it does not work

- The optimised schedule does not beat VWAP on realised shortfall.
- The impact parameters cannot be estimated stably from the available data.
- The schedule is so sensitive to parameters that small errors reverse the ranking.

## Common failure modes

- **Benchmark gaming.** Optimising against VWAP can produce a schedule that looks good on the benchmark and costs more in shortfall.
- **Ignoring the order's footprint.** A large order relative to daily volume can move the market for the whole session.
- **Calibrating impact on the same data used to evaluate it.** Keep a separate period for calibration.

## Further reading

- Almgren and Chriss (2000), "Optimal Execution of Portfolio Transactions," *Journal of Risk*.
- Perold (1988), "The Implementation Shortfall: Paper Versus Reality," *Journal of Portfolio Management*.
- Almgren, Thum, Hauptmann and Li (2005), "Direct Estimation of Equity Market Impact," *Risk*.
