# Low volatility

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** monthly · **Repo project:** [Project 08](../projects/08-factor-model-indian-equities/) (as an optional factor)

## Idea

Low-volatility and low-beta stocks have historically earned returns at least as high as high-volatility and high-beta stocks, which contradicts the simple risk–return trade-off. Two explanations are discussed: leverage constraints (investors who want more risk buy high-beta stocks rather than levering low-beta ones) and lottery preferences (investors overpay for stocks with a small chance of large gains). The strategy holds the low-volatility group and often shorts or underweights the high-volatility group.

## Research question

In NSE equities, does a ranking on trailing volatility or beta earn a positive net premium over the sample, and is the premium separate from the size and value exposure of low-volatility stocks?

## Signal

1. Estimate each stock's volatility over the past 252 trading days from daily returns, or its beta against the index over the same window.
2. Rank stocks cross-sectionally each month, with the lowest volatility ranked highest.
3. Hold the low-volatility group long, equal-weighted or inverse-volatility weighted. Optionally short the high-volatility group.
4. Report the group returns, gross and net.

Betting-against-beta weights stocks by the inverse of their beta, which is a different construction. Test it as a variant.

## Data

- Adjusted daily returns, with corporate actions applied.
- Index returns for beta estimation, and the same index for all stocks.
- Point-in-time membership and liquidity filters.
- Rates or the index levels needed for the beta regression.

## Costs

- Low-volatility portfolios hold large, stable companies, which are more liquid. Costs may be lower than for value or momentum.
- The short leg, if used, carries borrowing or futures costs. Test the long-only version first.
- Charge costs on traded value using [India trading costs](india-trading-costs.md).

## Evaluation

- Report the premium gross and net, with its standard error and sub-period results.
- Report the exposure of the portfolio to size, value and market beta. A low-volatility portfolio that is mostly a bet on large, low-beta stocks should say so.
- Report performance in rising markets. Low-volatility portfolios often lag strongly when the market rises quickly, which is part of the premium's risk.
- Report the deflated Sharpe ratio across definitions tried.

## What would show it does not work

- The premium is not significant net of costs.
- The portfolio's returns are explained by size and value exposure in a factor regression.
- The premium depends on a single crash period, when the high-volatility group fell most.

## Common failure modes

- **Estimation noise.** Volatility estimated from a short window is noisy. Use a window long enough for stability, and test sensitivity to it.
- **Beta instability.** Beta changes with the regime. A low beta in one period may not persist.
- **Sector concentration.** Low-volatility portfolios often hold heavy weights in a few defensive sectors.

## Further reading

- Ang, Hodrick, Xing and Zhang (2006), "The Cross-Section of Volatility and Expected Returns," *Journal of Finance*.
- Frazzini and Pedersen (2014), "Betting Against Beta," *Journal of Financial Economics*.
- Black (1972), "Capital Market Equilibrium with Restricted Borrowing," *Journal of Business*, for the leverage-constraint argument.
