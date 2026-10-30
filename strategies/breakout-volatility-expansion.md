# Breakout and volatility expansion

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** days to weeks · **Repo project:** [Project 15](../projects/15-technical-indicator-study/) (rule testing), [Project 03](../projects/03-honest-backtester/) (backtester)

## Idea

Prices often spend a period in a narrow range, with low volatility, and then move sharply out of it. Breakout strategies buy when the price closes above the top of a recent range, and sell or short when it closes below the bottom. The idea is that a range breakout signals a change in supply and demand, and that the new trend will carry beyond the breakout point. The strategy profits from the transition from low to high volatility, and it accepts a high rate of small losses from false breakouts.

Breakouts are a rule-based cousin of trend following. [Trend-following rules](trend-following-rules.md) use moving averages; breakouts use price levels and volatility.

## Research question

For NSE stocks and index futures, does a breakout above a stated N-day high, filtered by volume and volatility, earn a positive net return over the following weeks, and does the result survive the costs of the frequent small losses?

## Signal

1. **Define the range.** Use the highest high (or close) over the past N days, for example 20, 55 or 100. Keep the lookback fixed in advance.
2. **Define the breakout.** A close above the range high. Use closes rather than intraday highs unless the strategy trades intraday, so that the decision uses information available at the close.
3. **Confirm.** Require volume above a multiple of its trailing average, and optionally a rising volatility measure such as ATR relative to its trailing level.
4. **Enter** at the next session's open, not at the breakout close, to avoid trading on the same bar that generated the signal.
5. **Stop.** Set a stop at a stated multiple of ATR below the entry, for example two ATR. Exit on a trailing stop, or when the price closes back inside the range.

The entry and stop rules must be written down before testing. Changing them after seeing the results is the most common way breakout tests become unreliable.

## Data

- Daily OHLCV for the universe, with corporate actions applied. Adjusted high and low prices must be adjusted consistently with the close.
- For index futures, a continuous series with a stated roll rule. Breakouts across a roll gap can look like real breakouts.
- Liquidity filters, because breakouts in illiquid stocks are often driven by a few trades.

## Costs

- Breakout systems trade often in choppy markets, when most breakouts fail. Turnover can be high relative to the number of profitable trades.
- Entries at the next open include slippage on gap openings, which is significant in a breakout.
- Use the costs for the instrument traded, from [India trading costs](india-trading-costs.md).

## Evaluation

- Report the win rate, the average win and the average loss, and the expectancy per trade, net of costs.
- Report the distribution of trade outcomes. Breakout returns are skewed; a few large winners often carry the result.
- Report results by market regime, since breakouts work in trending periods and fail in sideways ones.
- Report the rule's sensitivity to N and to the stop multiple. A rule that works only at one lookback is fragile.
- Report the deflated Sharpe ratio across rule variants tried, and the number of trades behind each figure.

## What would show it does not work

- The expectancy per trade is not positive after costs and slippage.
- Returns come from a small number of large trades, and the typical trade loses money.
- Results depend on the entry at the breakout close, which the strategy cannot achieve.

## Common failure modes

- **Same-bar entry.** Entering at the breakout close, which uses the close to decide a trade and then trades at it.
- **False breakouts.** A close above resistance followed by a return inside the range. The majority of signals in a sideways market.
- **Gap risk.** A stock that opens far above the breakout level gives a poor entry and a wide stop.
- **Survivorship.** A backtest on current index constituents excludes stocks that broke out and then failed.

## Further reading

- Brock, Lakonishok and LeBaron (1992), "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns," *Journal of Finance*. Includes range-break rules.
- Lo, Mamaysky and Wang (2000), "Foundations of Technical Analysis," *Journal of Finance*. Pattern recognition tested statistically.
- Park and Irwin (2007), "What Do We Know About the Profitability of Technical Analysis?," *Journal of Economic Surveys*. A review of the evidence, with its weaknesses.
