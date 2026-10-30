# Trend-following rules

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** weeks to months · **Repo project:** [Project 15](../projects/15-technical-indicator-study/) (testing indicator rules), [Project 16](../projects/16-time-series-momentum/) (the portfolio version)

## Idea

Trend following holds a position while a price trend persists and exits when it ends. The rule-based versions use moving averages, channel breakouts and volatility-based trailing stops to decide when a trend has started and when it has finished. They are the practical implementation of the trend idea. [Time-series momentum](time-series-momentum.md) states the signal as a return sign; these rules state it as indicator crossings and stops, which change how and when trades happen.

The rules are simple to describe and easy to overfit. Most of the research question is about parameter choice, costs, and whether a rule earns more than a trivial benchmark.

## Research question

For a diversified set of liquid instruments, do rule-based trend systems (moving-average crossover, Donchian channels, SuperTrend, and ATR trailing stops) earn a positive net return over a common benchmark, and which rule components contribute most to the result?

## Rules

- **Moving-average crossover.** Long when a short moving average is above a long one, for example 50 and 200 days. Flat or short otherwise.
- **Donchian channel.** Long on a breakout above the highest close of the past N days, exit on a break below the lowest close of the past M days, with M smaller than N.
- **SuperTrend.** A trailing band set at a multiple of ATR around the price. Long while the price is above the band, and it flips when the price crosses it.
- **ATR trailing stop.** A stop placed at a multiple of ATR below the highest close since entry, which ratchets upward as the trend extends.
- **ADX filter.** Trade only when ADX, the trend-strength indicator, is above a threshold. Applied as a filter on any of the rules above.

Each rule is defined by its parameters. Fix them before testing.

## Method

1. Build the rules on each instrument separately, with signals computed on closes and positions taken on the next session.
2. Size each position by volatility, using the approach in [time-series momentum](time-series-momentum.md), so that instruments contribute similar risk.
3. Test each rule component alone and combined, on the same instruments and dates.
4. Compare against two benchmarks: buy and hold of the same instruments, and the time-series momentum signal with a single lookback.
5. Use the [indicator study](../projects/15-technical-indicator-study/) procedure for the walk-forward and null-model checks.

## Data

- Daily OHLC and close prices for each instrument, with roll rules for futures and corporate actions for stocks.
- The indicators' input series. ATR and ADX need adjusted high and low prices.
- A common calendar, so that all instruments are tested over identical dates.

## Costs

- Trend rules trade rarely compared with oscillators, so costs are usually smaller. Test that claim with the actual turnover.
- Each whipsaw costs a round trip. Report the number of whipsaws per year.
- Futures roll and margin costs, as in [time-series momentum](time-series-momentum.md). Costs from [India trading costs](india-trading-costs.md).

## Evaluation

- Report net return, Sharpe ratio, maximum drawdown and turnover for each rule, against both benchmarks.
- Report the contribution of each component: entry rule, exit rule, stop, and filter. A result that depends on the stop alone is a finding about the stop.
- Report the win rate and the average trade, and check how much of the result comes from the top few trades.
- Report the deflated Sharpe ratio across parameter sets and components tried.

## What would show it does not work

- The rules do not beat buy and hold net of costs over the sample.
- The result depends on one parameter set, or on one instrument class.
- The benefit comes from avoiding a single crash, which may not recur.

## Common failure modes

- **Parameter search on the full sample.** The best moving-average pair chosen over 30 years is a fit to history.
- **Look-ahead through the close.** Entering at the close that generated the signal.
- **Sideways markets.** Long periods of whipsaw can erase the gains of trending periods.
- **Contract roll effects.** A roll that moves a continuous series can trigger a crossover that reflects no real change.

## Further reading

- Brock, Lakonishok and LeBaron (1992), "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns," *Journal of Finance*.
- Sullivan, Timmermann and White (1999), "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap," *Journal of Finance*.
- Hurst, Ooi and Pedersen (2017), "A Century of Evidence on Trend-Following Investing," *Journal of Portfolio Management*.
