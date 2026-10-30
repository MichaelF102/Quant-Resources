# Seasonality and calendar effects

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** days to one month · **Repo project:** none yet

## Idea

Some returns appear to depend on the calendar: higher returns in particular months (the January effect), around month-end or month-start (the turn-of-month effect), on particular weekdays, or around scheduled market events such as index rebalances and derivatives expiry. Calendar strategies buy the stock or index in the favourable window and hold cash or the opposite position otherwise.

This is the family to approach with the most caution. Calendar patterns are easy to find in data, easy to explain after the fact, and easy to lose once they are published. A calendar effect that is not supported by a stated reason and by out-of-sample data should be treated as a hypothesis, not a strategy.

## Research question

Does a stated calendar window in NSE index or stock returns (for example the last trading day of the month and the first three days of the next) earn a positive abnormal return, net of costs, in data that were not used to find the window, and is the effect still present in the most recent years?

## Specifying the effect

Write the hypothesis before looking at the data:

1. **The window.** Define it in trading days relative to a fixed event, such as the last trading day of the month or an expiry day. Do not search over windows.
2. **The reason.** State the mechanism you expect: institutional flows, rebalancing, or a documented behavioural pattern. A window without a reason is a candidate for rejection.
3. **The benchmark.** The abnormal return is measured against the market or against a matched-calendar control, so that a rise in the market during those days is not mistaken for a calendar effect.

## Data

- Daily index and stock prices, from a long history, with corporate actions applied.
- Event calendars: monthly and quarterly expiry dates, index rebalance dates, and exchange holidays. Record them as they were scheduled.
- Enough years to estimate the effect with a standard error that can distinguish it from zero. A few years of data cannot.

## Costs

- A calendar strategy trades on a fixed schedule, so costs are predictable, but a short window with a few trades a year can still have high costs per unit of return.
- Index futures or ETFs are usually cheaper to trade than a basket of stocks. Use the costs for the instrument traded, from [India trading costs](india-trading-costs.md).
- Transaction taxes apply on each entry and exit. Count the round trips.

## Evaluation

- Report the average abnormal return in the window, its standard error, and the number of observations. A window with few observations has a wide interval.
- Report the result for each year separately. An effect that comes from one or two years is not a pattern.
- Report the result in the most recent subperiod, after the hypothesis was stated.
- Report every window tested, including those discarded. The deflated Sharpe ratio across windows is required, and a simple Bonferroni-style count of trials should be shown alongside it.

## What would show it does not work

- The effect is not significant once the number of windows tested is accounted for.
- It disappears when the window is moved by one trading day, which means the result depends on exact timing details.
- It is absent in recent years, or it reverses.

## Common failure modes

- **Data mining.** Testing every month, every weekday and every week of the year gives about one significant result in twenty at 5% significance, with no real effect.
- **Post-hoc explanations.** A reason written after the pattern is found is not a test of the pattern.
- **Calendar confounds.** A window may coincide with a known volatility event or a rate decision. Control for the event.
- **Holiday handling.** Shifting windows around exchange holidays can change which days are included. Record the rule.

## Further reading

- Ariel (1987), "A Monthly Effect in Stock Returns," *Journal of Financial Economics*.
- Lakonishok and Smidt (1988), "Are Seasonal Anomalies Real? A Ninety-Year Perspective," *Review of Financial Studies*.
- Keim (1983), "Size-Related Anomalies and Stock Return Seasonality," *Journal of Financial Economics*.
