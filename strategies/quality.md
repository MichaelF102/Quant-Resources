# Quality

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** monthly to annual · **Repo project:** [Project 08](../projects/08-factor-model-indian-equities/) (as an optional factor)

## Idea

Firms that are profitable, with stable earnings and low leverage, have tended to earn higher returns than firms that are unprofitable or fragile. Quality is measured in several ways: profitability (gross profit over assets), earnings quality (accruals), safety (low leverage and stable earnings), and growth in profitability. The premium is less well explained by simple risk than value is, which is one reason it is studied on its own.

## Research question

In NSE equities, does a profitability-based quality ranking earn a positive net premium over the sample, and does it add to value and momentum, or does it mostly overlap with them?

## Signal

Define one or more measures before testing:

- **Gross profitability:** revenue minus cost of goods sold, divided by total assets.
- **Accruals:** the gap between earnings and cash flow, scaled by assets. Low accruals indicate higher quality.
- **Leverage:** debt to equity, with low leverage ranked higher.

Standardise each measure cross-sectionally each month, combine with equal weights, and rank. Go long the highest-quality group and, if testing a long-short version, short the lowest.

## Data

- Financial statements as first reported, lagged to the filing date. Quality measures are sensitive to restatements and to changes in accounting definitions.
- Consolidated or standalone basis: state which one is used, and keep it consistent.
- Point-in-time index membership and corporate actions for prices.

## Costs

- Quality tends to be a slow-moving characteristic, so turnover is lower than for momentum. Confirm this in the data.
- Charge costs on traded value using [India trading costs](india-trading-costs.md).

## Evaluation

- Test each measure alone, and the combined measure, on the same dates and costs.
- Report the correlation of quality with value and momentum. A factor that is mostly a copy of value adds little to a multi-factor model.
- Report the premium in sub-periods and by size group.
- Report the deflated Sharpe ratio across measures tried.

## What would show it does not work

- The quality premium is not distinguishable from zero after costs.
- It is entirely explained by value or momentum exposure in a regression.
- It depends on one accounting definition that changed during the sample.

## Common failure modes

- **Accounting definitions.** A change in how a company reports can move the measure without any change in business.
- **Sector differences.** Some sectors have structurally higher gross margins. Rank within sectors if the premium is a sector effect.
- **Data mining.** Several quality definitions give several chances to find a premium.

## Further reading

- Novy-Marx (2013), "The Other Side of Value: The Gross Profitability Premium," *Journal of Financial Economics*.
- Asness, Frazzini and Pedersen (2019), "Quality Minus Junk," *Review of Accounting Studies*.
- Fama and French (2015), "A Five-Factor Asset Pricing Model," *Journal of Financial Economics*, where profitability is one of the factors.
