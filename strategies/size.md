# Size

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** monthly to annual · **Repo project:** [Project 08](../projects/08-factor-model-indian-equities/) (as a factor)

## Idea

Smaller companies have historically earned higher average returns than larger ones, after adjusting for risk. The premium has been documented in many markets since the early 1980s. Explanations include compensation for illiquidity, for the higher risk of small firms, and for the limited attention they receive. The premium has been unstable: it was large in some periods and absent in others, and much of it sits in the smallest stocks, where trading costs are highest.

Size is one of the five factors in the article's factor set. It is tested here on its own; [multi-factor equity](multi-factor-equity.md) combines it with the others.

## Research question

In NSE equities, does a long position in small-cap stocks, short in large-cap stocks, earn a positive net premium over the sample, and does the premium survive a minimum liquidity filter and realistic costs?

## Signal

1. **Measure size.** Market capitalisation at the rebalance date, using shares outstanding and price, with the share count as at that date.
2. **Rank** stocks each month by market capitalisation.
3. **Define the groups.** Small: the bottom quintile or the bottom third of a universe with a liquidity filter. Large: the top quintile or top third.
4. **Hold** the small group long and the large group short, equal-weighted, or hold the small group long-only, and report both.
5. **Rebalance** monthly, or at the frequency stated in advance.

The universe filter matters more than the ranking. Without a minimum traded value, the small-cap premium is mostly a premium for stocks that cannot be traded at the modelled size.

## Data

- Market capitalisation with share counts updated for splits, bonuses, rights issues and buybacks. Errors in share counts create false size changes.
- Traded value over a trailing window, for the liquidity filter.
- Point-in-time index membership, so that a stock enters the universe only when it was eligible.
- Corporate actions applied to prices.

## Costs

- Small stocks have wide spreads and high impact. The premium before costs is often much larger than the premium after them.
- The short leg, in large caps, is restricted in Indian cash equities, as noted in [India trading costs](india-trading-costs.md). Test the long-only version as the primary result.
- Liquidity filtering reduces the universe and can reduce the premium. Report both.

## Evaluation

- Report the size premium gross and net, with its standard error and sub-period results.
- Report the result with and without the liquidity filter, and at several minimum traded values.
- Report the exposure of the small-cap portfolio to value, momentum and market beta, since small stocks often carry other factor exposures.
- Report the deflated Sharpe ratio across definitions and filters tried.

## What would show it does not work

- The premium is not significant after costs and the liquidity filter.
- It is concentrated in the smallest stocks, which are not tradeable at the modelled size.
- It is explained by value or momentum exposure in a factor regression.
- It has been absent in the most recent years.

## Common failure modes

- **Stale share counts.** A company that issued shares, and whose count was not updated, looks smaller than it is.
- **Survivorship.** Small companies that failed are removed from current universes, which flatters the premium.
- **Illiquid names.** A stock that has not traded for days can have a stale price and a market value that does not reflect a real transaction.
- **Data mining on the cutoff.** Choosing the small-cap cutoff after seeing the result.

## Further reading

- Banz (1981), "The Relationship Between Return and Market Value of Common Stocks," *Journal of Financial Economics*.
- Fama and French (1992), "The Cross-Section of Expected Stock Returns," *Journal of Finance*.
- Fama and French (1993), "Common Risk Factors in the Returns on Stocks and Bonds," *Journal of Financial Economics*.
