# Time-series momentum

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** weeks to months · **Repo project:** [Project 16](../projects/16-time-series-momentum/)

## Idea

Cross-sectional momentum compares assets with each other. Time-series momentum compares each asset with its own past. An asset with a positive return over the past months is held long; one with a negative return is held short or not held. Each position is scaled so that every asset contributes a similar amount of risk. The strategy is applied across many asset classes, so that the trends in one market can offset losses in another.

## Research question

Does a diversified set of trend signals across equity indices, government bonds, currencies and commodities improve risk-adjusted returns and reduce drawdowns, net of costs and in data that were not used to choose the lookback?

## Signal

For each asset on each rebalance date:

1. Compute the excess return over the past 12 months (or several lookbacks, such as 1, 3, 6 and 12 months).
2. Take the sign of the return as the direction: long if positive, short if negative. Alternatively use a continuous score, such as a moving-average gap.
3. Scale the position so that its volatility contribution is a constant. A common choice is to size each position by a target volatility divided by the asset's trailing volatility.
4. Combine the assets with equal risk budgets, and cap the total gross exposure.

Test one lookback first, then the combination of lookbacks. State which you chose before testing, and count the variants.

## Data

- Daily prices for a diversified set of liquid instruments. In India, the practical set is index futures, government bond futures where available, and a few commodity contracts. Check which contracts have enough history and liquidity.
- Continuous series built from futures require a roll rule. State it, because the roll can create artificial returns.
- Use the [data sources](../data/data-sources.md) file to check each series' availability and adjustment.

## Costs

- Futures carry low explicit costs but have roll costs and margin requirements. Model them.
- A trend signal turns over slowly, so costs are usually smaller than for cross-sectional strategies. Test that claim.
- Scaling by volatility can increase turnover in volatile periods. Report turnover by period.

## Evaluation

- Report returns for each asset class and for the portfolio, net of costs.
- Report the correlation of the strategy with equity returns, since diversification is the main argument for trend following.
- Report the drawdown in named stress periods, and how the strategy behaved in each.
- Report the deflated Sharpe ratio across lookbacks and instruments tried.

## What would show it does not work

- The portfolio's Sharpe ratio depends on one asset class or one lookback.
- Results collapse once the roll rule is changed, which indicates the roll is driving the result.
- The strategy is not diversifying: its correlation with equities is high in drawdowns.

## Common failure modes

- **Continuous futures artefacts.** A roll that jumps between contracts can create returns that never existed.
- **Lookback choice.** The best lookback in-sample is often a poor one out of sample.
- **Thin instruments.** A trend signal on an illiquid contract can be impossible to trade at the modelled size.

## Further reading

- Moskowitz, Ooi and Pedersen (2012), "Time Series Momentum," *Journal of Financial Economics*.
- Man Group's public research on systematic trend strategies, in [public research](public-research.md). Check the current publications before citing a specific figure.

## Project

[Project 16](../projects/16-time-series-momentum/) builds this strategy with a stated roll rule, volatility scaling, benchmarks and a deflated Sharpe ratio across lookbacks.
