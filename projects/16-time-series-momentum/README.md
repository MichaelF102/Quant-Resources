# 16 — Time-series momentum across assets

**Proves:** trend signals on each asset against its own history, volatility scaling, continuous futures construction and roll effects, diversification across asset classes, and evaluation of a portfolio whose inputs are in different currencies and units
**Level:** 🟡 · **Time:** 2–3 weekends
**Prerequisites:** [Strategies: time-series momentum](../../strategies/time-series-momentum.md); [Project 03](../03-honest-backtester/); [Project 04](../04-momentum-mean-reversion-study/); [Performance metrics](../../cheatsheets/performance-metrics.md)

## Goal

Build a diversified trend-following portfolio from the past-return sign of each asset, scaled to a common volatility, and test whether it improves risk-adjusted returns and reduces drawdowns compared with a buy-and-hold benchmark in the same assets. The question: does the time-series momentum premium appear in a small set of Indian and comparison instruments, and does it survive a stated roll rule and costs?

## Data

Daily prices for a small set of liquid instruments. The aim is breadth across asset classes; liquidity matters more than the list.

- **Equity:** NIFTY 50 index futures (or the index price, stated as price return).
- **Rates:** government bond futures or a bond index, where a series with enough history and liquidity is available. If none is, use a US Treasury futures series and state the substitution clearly.
- **Currency:** a major pair against the rupee, or a dollar index proxy.
- **Commodity:** gold or crude oil futures, stated.

For each instrument, record the source, the adjustment method, and the roll rule. A roll that jumps between contracts creates returns that never existed; the roll rule must be fixed before any results are computed. Use the [data sources](../../data/data-sources.md) file to check availability.

## Steps

1. **Build continuous series.** For futures, roll from the front contract to the next on a fixed calendar rule (for example, a stated number of days before expiry). Compute returns on the continuous series and record the number of rolls.
2. **Define the signal.** For each asset and month-end, take the sign of the excess return over the past 12 months, using the instrument's price return net of the risk-free rate. Compute it with the price on the decision date only.
3. **Scale to volatility.** Estimate each asset's volatility from the past 60 trading days. Set each position to a target volatility divided by that estimate, with a stated cap on gross leverage per asset.
4. **Combine.** Equal risk budget across assets. Net the positions into a portfolio return and record the gross and net exposure each month.
5. **Benchmarks.** (a) Equal-weight buy-and-hold of the same assets, with the same rebalancing. (b) A volatility-scaled buy-and-hold. Report both alongside the trend portfolio.
6. **Costs.** Charge the roll cost on each roll and a per-unit trading cost on each rebalance trade, using the rate table in [India trading costs](../../strategies/india-trading-costs.md) for Indian instruments and a stated assumption for others.
7. **Robustness.** Repeat with lookbacks of 3, 6 and 12 months, and with the combined signal of all three. Count every variant.

## Done when

- [ ] The roll rule is written down before results are computed, and the number of rolls per instrument is reported
- [ ] The signal uses only prices up to the decision date, confirmed by a shift test
- [ ] Gross and net returns are reported for the trend portfolio and both benchmarks, with the same costs and dates
- [ ] Each asset class's contribution to the portfolio return is reported, so no single instrument drives the result
- [ ] The correlation of the trend portfolio with the equity benchmark is reported, overall and in its five worst equity months
- [ ] The number of lookbacks and signal variants tested is reported, with the deflated Sharpe ratio of the best one
- [ ] The write-up states whether the diversification benefit appears net of costs, and in which years the strategy lost money

## Common pitfalls

- **Roll artefacts.** A roll that always moves to a more expensive contract produces a systematic drag, or a gain, that is not a trend.
- **Mixed units and currencies.** Returns in rupees and dollars must be converted consistently. Say which currency each return is in.
- **Using the full-sample volatility.** Scaling by volatility estimated over the whole sample is look-ahead.
- **Choosing the best lookback.** The best lookback in-sample is often a poor one out of sample. Report all of them.
- **Thin instruments.** A small instrument can show a strong trend that cannot be traded at the modelled size. Report the notional per instrument.

## Stretch goals

- Add a carry signal for the bond and currency instruments, and test whether combining carry with trend adds to diversification.
- Compare the monthly signal with a weekly one, and report the turnover difference.
- Add a drawdown-based risk control that reduces exposure after a stated loss, and test whether it improves the worst outcomes without hurting the average.

## Further reading

- Moskowitz, Ooi and Pedersen (2012), "Time Series Momentum," *Journal of Financial Economics*.
- Hurst, Ooi and Pedersen (2017), "A Century of Evidence on Trend-Following Investing," *Journal of Portfolio Management*. A long-history test across asset classes.
- Daniel and Moskowitz (2016), "Momentum Crashes," *Journal of Financial Economics*. The crash risk of momentum portfolios.
