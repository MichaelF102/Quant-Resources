# Mean reversion (single asset)

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** days to weeks · **Repo project:** [Project 04](../projects/04-momentum-mean-reversion-study/) (reversal), [Project 15](../projects/15-technical-indicator-study/) (rule testing)

## Idea

A stock's price can drift away from its recent average and come back. Single-asset mean reversion measures how far the current price sits from its own moving average, in units of its recent volatility, and trades the expected return to the average. It differs from [short-term reversal](short-term-reversal.md), which ranks stocks against each other, and from [statistical arbitrage](statistical-arbitrage.md), which trades residuals against a factor model. Here each asset is compared only with its own history.

The question is whether the deviation is temporary or the start of a permanent change. A stock that falls because its business is deteriorating does not revert, and that is the main risk.

## Research question

For NSE stocks and index futures, does a z-score of the price against its trailing mean, entered at a stated extreme and exited at the mean, earn a positive net return, and does the result hold after excluding periods of news-driven moves?

## Signal

1. **Compute the mean and volatility.** Use a trailing mean of the price (or log price) over a window such as 20 days, and the standard deviation of the price over the same window.
2. **Compute the z-score.** Z_t = (P_t − μ_t) / σ_t, using only data up to day t − 1 for the statistics, so that the day's own move does not enter its own standard deviation.
3. **Enter long** when Z is at or below −2, and short, where permitted, when Z is at or above +2.
4. **Exit** when Z returns to 0, after a stated maximum holding period, or at a stop.
5. **Stop.** Use a volatility-based stop, for example at Z = −4, or a fixed multiple of ATR from the entry price.

Price z-scores are non-stationary when the price trends. Test the same rule on log returns or on a detrended series as a robustness check, and report both.

## Data

- Adjusted daily prices with corporate actions applied. A split or bonus issue appears as a sharp move that a z-score will treat as a deviation.
- News and earnings dates, to identify deviations caused by scheduled events. Test with and without those dates.
- Liquidity data for filtering. Mean reversion is strongest in less liquid stocks, where it is hardest to trade.

## Costs

- Each entry and exit crosses the spread, and deviations are often small relative to it.
- Mean reversion trades when prices are falling, which is when liquidity can be thinnest. Model the spread wider in those periods.
- Use the costs from [India trading costs](india-trading-costs.md).

## Evaluation

- Report the average return per trade, net of costs, with its standard error.
- Report the result separately for entries after scheduled news and for other entries.
- Report the frequency of stop-outs. A high stop-out rate with a small average gain shows that the stop is doing most of the work.
- Report the sensitivity to the window length and the entry threshold. Report every combination tested.
- Report the deflated Sharpe ratio across windows and thresholds.

## What would show it does not work

- The average net return per trade is not significantly positive.
- The profitable trades come from entries that were not caused by news, and the news-driven entries lose money.
- The results hold only in a single regime, such as a long bull market, in which falling prices were always temporary.

## Common failure modes

- **Trend mistaken for deviation.** A stock in a steady decline has a persistently negative Z-score. It is not mean-reverting.
- **Look-ahead in the statistics.** Including the entry day's own price in the mean or standard deviation.
- **Survivorship.** Stocks that fell and did not recover are removed from the current index, so the rule looks better than it was.
- **Corporate actions.** An unadjusted split looks like a 50% fall and produces a false entry.

## Further reading

- Poterba and Summers (1988), "Mean Reversion in Stock Prices: Evidence and Implications," *Journal of Financial Economics*.
- Fama and French (1988), "Permanent and Temporary Components of Stock Prices," *Journal of Political Economy*.
- Ornstein–Uhlenbeck process, covered in the [stochastic calculus cheat sheet](../cheatsheets/stochastic-calculus.md), for the continuous-time model of reversion.
