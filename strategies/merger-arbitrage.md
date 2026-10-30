# Merger arbitrage

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** weeks to months, until the deal closes or fails · **Repo project:** none yet

## Idea

When one company agrees to acquire another for a stated price, the target's shares usually trade slightly below the offer price until the deal closes. The gap, the spread, is compensation for the risk that the deal fails. A merger arbitrage trader buys the target (and, in a stock deal, shorts the acquirer to hedge the exchange ratio), and earns the spread if the deal closes. If it fails, the target's price can fall sharply. The return is therefore a short-volatility bet on deal completion, with a payoff that is asymmetric.

## Research question

For announced deals in Indian and comparison markets, does holding the target's shares and hedging the acquirer's shares earn a positive net return after the probability of failure, and how does that return compare with the risk of a failed deal?

## Mechanics

- **Cash deal.** The target is bought at a price below the offer. The return if the deal closes is the spread, annualised over the time to closing.
- **Stock deal.** The target is bought and the acquirer is shorted in the exchange ratio, to hedge the acquirer's price risk.
- **Implied probability.** The spread implies a market probability of completion. Compare it with the trader's own estimate of that probability.

The expected return is approximately p × spread − (1 − p) × (target's fall on failure), before costs and financing. The break-even probability of completion depends on the size of the fall on failure.

## Signal and screen

1. Identify announced deals with a definitive agreement, a stated price and a stated closing timetable.
2. For each deal, compute the gross spread, the annualised spread, and the implied probability of completion.
3. Estimate the downside on failure: the target's price before the announcement, or a fundamental value.
4. Trade where the annualised spread exceeds a threshold set in advance, with position sizes limited by the downside.

## Data

- Announcement dates and deal terms from exchange filings and company announcements.
- Daily prices for the target and acquirer, from the start of the deal to completion or failure.
- Regulatory and shareholder approval timelines, where published.
- Record the outcome of every deal, including failures and deals that were cancelled or revised. A sample of only completed deals overstates the strategy.

## Costs

- Brokerage and transaction taxes on both legs, and the cost of shorting the acquirer in a stock deal. See [India trading costs](india-trading-costs.md).
- Financing for the position over the holding period.
- Position limits imposed by a fixed downside. The strategy needs many deals to diversify deal-failure risk.

## Evaluation

- Report the return per deal, the distribution, and the number of failures.
- Report the annualised return and the drawdown from failed deals.
- Report the sample of deals: announcements, completions and failures, and the period covered. Small samples give unreliable averages.
- Report the deflated Sharpe ratio across screens tried.

## What would show it does not work

- The spread does not compensate for failure risk over the sample.
- Returns depend on a few large deals that completed.
- Failed deals in the sample cost more than the completed deals earned.

## Common failure modes

- **Survivorship in deal samples.** Only completed deals are easy to find in some databases.
- **Regulatory risk.** Approvals can be blocked or delayed. The spread can widen sharply on news.
- **Correlated failures.** Deals in one sector or under one regulator can fail together during a market shock.

## Further reading

- Mitchell and Pulvino (2001), "Characteristics of Risk and Return in Risk Arbitrage," *Journal of Finance*.
- Baker and Savasoglu (2002), "Limited Arbitrage in Mergers and Acquisitions," *Journal of Financial Economics*.
