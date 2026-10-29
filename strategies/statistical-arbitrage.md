# Statistical arbitrage

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** intraday to weeks · **Repo projects:** [Project 05](../projects/05-pairs-trading-cointegration/) (pairs), [Project 13](../projects/13-pca-nse-stocks/) (factor structure)

## Idea

Stock returns share common drivers: the market, sectors, styles. Remove those drivers and what remains is a residual. If the residual deviates from its usual level and tends to revert, a trader can take a position against the deviation while hedging the common drivers. The statistical part is estimating the drivers and testing whether the residual actually reverts. The arbitrage label is loose: the position is not riskless.

## Research question

After removing market and sector exposure, do residual deviations in NSE equities revert enough, over a holding period that the costs allow, to earn a positive net return?

## Method

1. **Estimate common factors.** Use PCA on standardised returns over a formation window (see [Project 13](../projects/13-pca-nse-stocks/)), or use observable factors such as the market and sector indices. Keep a stated number of components, chosen before testing.
2. **Compute residuals.** For each stock, regress its returns on the factors over the formation window, and take the residual series.
3. **Score deviations.** Convert the cumulative residual to a z-score against its formation-window mean and standard deviation.
4. **Trade.** Go long stocks with large negative residual z-scores and short stocks with large positive ones, sized so that the factor exposure of the portfolio is near zero.
5. **Exit.** Close positions when the z-score returns to zero, after a stated holding period, or at a stop-loss level.

The pairs version is a special case with one factor: two stocks whose spread is stationary. [Project 05](../projects/05-pairs-trading-cointegration/) covers it in detail.

## Data

- Daily adjusted prices for a liquid universe, such as NIFTY 100 or NIFTY 50. Liquidity is a requirement, not an option.
- Sector classifications, dated, if sector factors are used.
- Intraday data only if the holding period is intraday, and then with its own cost model.

## Costs

This is where most statistical arbitrage research fails. Model each cost explicitly:

- Commissions and taxes on each leg, as in [India trading costs](india-trading-costs.md).
- Bid-ask spread on every trade. A reversal of a few tenths of a percent can disappear in the spread.
- Market impact, which rises with the size of the order relative to volume.
- Financing or the cost of shorting, through futures or stock options.

A residual that reverts by 20 basis points a week is worth nothing if the round trip costs 25.

## Evaluation

- Report the number of variants tested, and the deflated Sharpe ratio of the best one.
- Test on a formation window and a trading window that do not overlap, rolled forward through time.
- Report the exposure of the portfolio to each factor, which should be near zero by design. A residual that is not near zero shows the hedge failed.
- Report the half-life of reversion, estimated from the residual, and check that the holding period is consistent with it.

## What would show it does not work

- Net returns are not significant after realistic costs.
- The reversion weakens sharply over time, or stops entirely in recent periods.
- The strategy's profits come from a small number of large deviations, which are often caused by news rather than noise.

## Common failure modes

- **Structural breaks.** A stock that loses its relationship with its peers does not revert. Use stop-losses and test for breaks.
- **Hidden factor exposure.** A hedge that uses the wrong factors leaves market risk in the portfolio.
- **Estimation on the full sample.** Choosing factors or the number of components with the full sample is look-ahead.
- **Shorting constraints.** Shorting in Indian cash equities is restricted for most investors, so the short leg must be implemented through futures or options, with their costs.

## Further reading

- Avellaneda and Lee (2010), "Statistical Arbitrage in the US Equities Market," *Quantitative Finance*. A factor-based residual approach.
- Gatev, Goetzmann and Rouwenhorst (2006), "Pairs Trading: Performance of a Relative-Value Arbitrage Rule," *Review of Financial Studies*.
- Engle and Granger (1987), "Co-integration and Error Correction," *Econometrica*.

See [papers](../resources/papers.md) for the full citations.
