# Systematic global macro

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** weeks to months · **Repo projects:** none yet

## Idea

Systematic macro strategies trade the economy through liquid instruments: government bond futures, currency pairs, equity index futures, and commodities. Signals come from macroeconomic data (inflation, growth, policy rates), from the shape of the yield curve, and from market trends and carry. The strategies are systematic in that the rules are fixed in advance and applied mechanically across markets.

## Research question

Do macro-derived signals (carry, trend, yield-curve slope, or inflation surprise) earn a net-of-cost premium across a diversified set of rates, currencies and indices in India and in a comparison set of markets, and does the premium depend on regime?

## Signals

- **Carry.** The yield an asset earns if its price does not change, such as the interest-rate differential between currencies, or the roll yield on futures.
- **Trend.** See [time-series momentum](time-series-momentum.md).
- **Yield-curve slope.** The difference between long and short rates, as a signal for growth and policy expectations. Define the points on the curve and the data source.
- **Macro surprise.** The difference between a released figure and its consensus or a model forecast. The data must be point-in-time: a series that is revised later must be used as it was first published. The [data sources](../data/data-sources.md) file covers vintage data through ALFRED for US series.

## Data

- Futures and spot series for government bonds, currencies and indices, with roll rules stated.
- Macroeconomic series with release dates, from RBI or other official sources. Check the vintage: revised values are not what a trader saw.
- Yield-curve data, with the bootstrapping method documented (see [fixed income](../cheatsheets/fixed-income.md)).

## Costs

- Futures roll costs and margin costs.
- Currency conversion costs for an investor whose base currency differs from the instrument's.
- Costs of holding bonds, including financing, and of shorting, where it requires a borrowing arrangement.

## Evaluation

- Report each signal alone and the combination, net of costs.
- Report results by asset class, because a macro strategy can be concentrated in one.
- Report the correlation of the strategy with equity returns in stress periods.
- Count the signal definitions tried, and deflate the Sharpe ratio across them.

## What would show it does not work

- The combined signal does not beat carry alone net of costs.
- The result depends on revised macro data that would not have been available at the time.
- Returns are concentrated in one regime and one currency.

## Common failure modes

- **Revised data.** Using the latest values of macro series in a backtest is look-ahead.
- **Regime dependence.** A signal can work in one rate cycle and fail in the next.
- **Few independent observations.** Monthly macro data gives a small number of independent observations, so statistical tests have low power.

## Further reading

- Ilmanen, *Expected Returns* 💸, on carry and other sources of return across asset classes.
- Asness, Moskowitz and Pedersen (2013), "Value and Momentum Everywhere," *Journal of Finance*, for carry and trend across markets.
- Man Group's public research on systematic strategies, in [public research](public-research.md).
