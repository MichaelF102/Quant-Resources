# Short-term reversal

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** days to one month · **Repo project:** [Project 04](../projects/04-momentum-mean-reversion-study/) (the reversal half of its signal set)

## Idea

Stocks that fell sharply over the past week or month tend to bounce back over the following days, and stocks that rose sharply tend to give some of the gain back. The most common explanations are price pressure from liquidity demand and overreaction to news that is later corrected. The effect is short-lived, concentrated in less liquid stocks, and is the reason cross-sectional momentum skips the most recent month.

## Research question

After controlling for liquidity, size and industry, does a cross-sectional rank on the past one-week or one-month return predict next-week returns in NSE stocks, and is the spread large enough to survive costs at the turnover it requires?

## Signal

1. Compute each stock's return over the past 5 trading days (or 21 days, tested separately).
2. Rank stocks cross-sectionally each day or week, and reverse the sign so losers rank high.
3. Go long the bottom quintile by past return and short the top quintile, equal-weighted within each leg.
4. Rebalance at the stated frequency, and report the forward return of each quintile.

Skip the most recent day's close when the signal uses intraday prices. A signal that uses the day's close and trades at that close is look-ahead.

## Data

- Daily adjusted prices and volume for a broad universe, such as NIFTY 500, with point-in-time membership.
- Liquidity measures (traded value, turnover) for filtering. The effect is strongest where liquidity is lowest, so filters change the result.
- Corporate actions applied before returns are computed.

## Costs

This is the strategy most sensitive to costs, because it turns over quickly and trades the least liquid names.

- Compute the turnover per rebalance and charge costs on traded value, using [India trading costs](india-trading-costs.md).
- Estimate the spread cost for the bottom and top quintiles separately. The less liquid quintile carries the larger cost.
- Impact increases with position size relative to traded volume. Cap positions as a share of average daily volume.

## Evaluation

- Report the quintile spread, gross and net, with its standard error.
- Report the spread by liquidity bucket. A result that exists only in the least liquid bucket has little capacity.
- Report the turnover and the average holding period.
- Report the deflated Sharpe ratio across lookbacks and filters tried.

## What would show it does not work

- The net spread is not significantly different from zero after costs.
- The effect disappears when illiquid stocks are excluded, and the remaining spread is too small for the turnover.
- The reversal reverses itself in periods of strong news-driven moves.

## Common failure modes

- **Same-bar look-ahead.** Using the day's close to rank and trading at that close.
- **Ignoring liquidity.** A ranking dominated by illiquid stocks that cannot be traded at the modelled size.
- **Missing news.** Reversal after earnings or corporate announcements is a different effect. Filter out stocks with scheduled events, or test with and without them.

## Further reading

- Jegadeesh (1990), "Evidence of Predictable Behavior of Security Returns," *Journal of Finance*.
- Lehmann (1990), "Fads, Martingales, and Market Efficiency," *Quarterly Journal of Economics*.
- Jegadeesh and Titman (1993), "Returns to Buying Winners and Selling Losers," *Journal of Finance*, for the one-month skip that separates reversal from momentum.
