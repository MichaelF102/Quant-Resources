# Industry momentum

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** monthly · **Repo project:** none yet; [Project 04](../projects/04-momentum-mean-reversion-study/) provides the momentum ranking and evaluation

## Idea

Cross-sectional momentum ranks individual stocks by past return. Industry momentum ranks industries, and holds the industries that have performed best over the past several months. Part of the stock-level momentum effect appears to come from industries that keep trending, which is why the two signals overlap. Industry momentum is often more stable than stock momentum, has lower turnover, and is easier to implement with sector index futures or ETFs.

## Research question

Does a ranking of NSE sector indices on their past 6- or 12-month returns, held for one month, earn a positive net return, and how much of that return is explained by stock-level momentum already in the portfolio?

## Signal

1. Define the industry classification before testing. Use a published sector classification and keep it fixed, or record the changes by date.
2. For each sector index, compute the return over the past 6 or 12 months, skipping the most recent month.
3. Rank the sectors each month. Hold the top few sectors, equal- or inverse-volatility weighted, and optionally short the bottom few.
4. Rebalance monthly.

Sector indices with a short history or low liquidity should be excluded, and the exclusion rule stated before the test.

## Data

- Daily total-return or price series for each sector index, from the same provider, so that the classification is consistent.
- Constituent-level data if the classification has to be rebuilt from stocks. The reconstruction must use the sector each stock belonged to at the time.
- Corporate actions applied to the constituents. Sector index membership changes must be recorded by date.

## Costs

- Turnover is lower than for stock momentum, because there are fewer positions.
- Sector index futures and ETFs carry different costs. Use the instrument that will be traded, from [India trading costs](india-trading-costs.md).
- Shorting sectors requires futures, which carry margin and roll costs.

## Evaluation

- Report the sector spread, gross and net, with its standard error.
- Regress industry momentum returns on stock momentum returns. A large residual shows that industry momentum adds information; a small residual means it is the same effect.
- Report the sector concentration of the portfolio over time.
- Report the deflated Sharpe ratio across lookbacks, skip periods and sector definitions tried.

## What would show it does not work

- The industry premium is explained by stock momentum in the same portfolio.
- The result depends on one or two sectors that rebounded sharply.
- The sector definition itself was changed to make the result look better.

## Common failure modes

- **Classification drift.** Companies move between sectors, and a fixed classification applied to old data uses information about the present.
- **Concentration.** A momentum portfolio of three sectors can be highly exposed to one macro factor.
- **Crash exposure.** As with stock momentum, sharp reversals in trend can cost a lot in one month.

## Further reading

- Moskowitz and Grinblatt (1999), "Do Industries Explain Momentum?," *Journal of Finance*.
- Jegadeesh and Titman (1993), "Returns to Buying Winners and Selling Losers," *Journal of Finance*.
- Daniel and Moskowitz (2016), "Momentum Crashes," *Journal of Financial Economics*.
