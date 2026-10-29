# Multi-factor equity

*Last reviewed: Oct 2026*

**Difficulty:** intermediate to advanced · **Holding period:** monthly · **Repo project:** [Project 08](../projects/08-factor-model-indian-equities/)

## Idea

Stocks differ systematically along characteristics such as past return (momentum), price relative to fundamentals (value), profitability (quality), and volatility (low volatility). Each characteristic has a research record of return differences. Combining several weakly correlated characteristics into one ranking can give a better risk-adjusted return than any single one.

## Research question

Does a composite of momentum, value, quality and low volatility improve out-of-sample risk-adjusted returns in NSE equities, compared with its best single component?

## Signals

Define each factor before testing, with its exact definition written in the README:

| Factor | Example definition | Data needed |
|---|---|---|
| Momentum | 12-minus-1-month return | Adjusted prices |
| Value | Book-to-price, or earnings-to-price | Fundamentals, lagged to filing date |
| Quality | Return on equity, or accruals | Fundamentals, lagged to filing date |
| Low volatility | Negative of trailing 252-day volatility | Adjusted prices |

Standardise each factor cross-sectionally each month (winsorise, then z-score). Combine with equal weights, then test alternative weightings and report the sensitivity.

## Portfolio construction

- Sort on the composite and hold the top quintile or tercile, equal-weighted or with inverse-volatility weights.
- Optionally neutralise sector exposure, by ranking within sectors. State whether you do, and test both versions.
- Cap single-stock weights and sector weights; state the caps.

## Data

- Point-in-time fundamentals, lagged to the filing date. This is the hardest data requirement in the program. See the fundamentals checklist in [data sources](../data/data-sources.md).
- Corporate actions and index membership as at each date.

## Costs

- Monthly rebalancing with a quintile portfolio has moderate turnover. Charge costs on traded value using [India trading costs](india-trading-costs.md).
- Value and quality tilts can hold less liquid stocks. Test impact sensitivity by excluding the least liquid tenth.

## Evaluation

- Test each factor alone and the composite, on the same dates, universe and costs.
- Report the factor exposures of the portfolio so a reader can separate a factor premium from market or sector exposure.
- Use Fama–MacBeth regressions for the factor premia, with Newey–West standard errors. See [Project 08](../projects/08-factor-model-indian-equities/).
- Report the deflated Sharpe ratio across the number of factor sets and weightings tried.

## What would show it does not work

- The composite does not beat its best single factor out of sample.
- The premia are not stable across sub-periods, or depend on one factor and one year.
- Results disappear once fundamentals are point-in-time.

## Common failure modes

- **Restated fundamentals.** A value factor built from restated accounts uses information that was not available at the time.
- **Data mining.** Trying many combinations and reporting the best one. Count the trials.
- **Crowding.** Widely known factor tilts can lose their premium as more capital chases them. Compare sub-periods.

## Further reading

- Fama and French (2015), "A Five-Factor Asset Pricing Model," *Journal of Financial Economics*.
- Asness, Moskowitz and Pedersen (2013), "Value and Momentum Everywhere," *Journal of Finance*.
- Kenneth French's data library, linked in [data sources](../data/data-sources.md), for US factors to check an implementation.
- AQR's public research datasets, in [public research](public-research.md).
