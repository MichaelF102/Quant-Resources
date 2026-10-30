# Value

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** monthly to annual · **Repo project:** [Project 08](../projects/08-factor-model-indian-equities/)

## Idea

Stocks with low prices relative to their fundamentals, such as book value, earnings or cash flow, have tended to earn higher returns than stocks with high prices relative to the same measures. The usual explanations are risk compensation (cheap firms are more likely to be in distress) and behavioural mispricing (investors extrapolate recent results). The premium is a long-run average with long periods of underperformance.

This file tests value on its own. [Multi-factor equity](multi-factor-equity.md) combines it with other factors.

## Research question

In NSE equities, does a value ranking based on book-to-price or earnings-to-price earn a positive net premium over the sample, and is the premium stable across sub-periods and size groups?

## Signal

1. Define the value measure. Book-to-price (book equity divided by market capitalisation) is the classic choice. Earnings-to-price is an alternative. State the one used before testing.
2. Use fundamentals as they were first reported, lagged to the filing date. A value ranking built with a later restatement is look-ahead.
3. Rank stocks cross-sectionally each month. Sort into quintiles or deciles.
4. Go long the cheapest group and short the most expensive, or hold the cheapest group long-only, and report both.

## Data

- Market capitalisation and book value at each date, with the filing date for book value.
- Point-in-time index membership.
- Corporate actions applied to market prices.
- For India, be careful with book value: the reporting basis (standalone or consolidated) and any restatements must be recorded.

## Costs

- Monthly rebalancing of a value portfolio has moderate turnover. Charge costs on traded value using [India trading costs](india-trading-costs.md).
- Value often holds smaller and less liquid stocks. Test the premium after excluding the least liquid tenth.

## Evaluation

- Report the value spread gross and net, with its standard error and sub-period results.
- Report the size and sector exposures of the value portfolio. Value in some markets is mostly a bet on a few sectors.
- Report the premium separately for large and small stocks, since a size effect can drive the result.
- Report the deflated Sharpe ratio across measures tried.

## What would show it does not work

- The premium is not distinguishable from zero after costs and size controls.
- Results depend on the choice of book value, or on a short sample.
- The premium disappears when fundamentals are point-in-time.

## Common failure modes

- **Restated accounts.** Restated book values make cheap stocks look cheaper in hindsight.
- **Value traps.** Cheap stocks in permanent decline. A value ranking that holds them has a high loss rate that the average hides.
- **Sector concentration.** A value portfolio can be a sector bet in disguise.

## Further reading

- Fama and French (1992), "The Cross-Section of Expected Stock Returns," *Journal of Finance*.
- Asness, Moskowitz and Pedersen (2013), "Value and Momentum Everywhere," *Journal of Finance*.
- Fama and French (2015), "A Five-Factor Asset Pricing Model," *Journal of Financial Economics*.
