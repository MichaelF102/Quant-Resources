# Pairs trading

*Last reviewed: Oct 2026*

**Difficulty:** intermediate to advanced · **Holding period:** days to weeks · **Repo project:** [Project 05](../projects/05-pairs-trading-cointegration/)

## Idea

Two stocks whose prices have moved together for a long time, such as two companies in the same industry with similar exposures, tend to keep a stable relationship. When the spread between them moves far from its usual level, a trader can buy the cheaper stock and sell the dearer one, betting that the spread returns. The strategy is market-neutral in its design, but the bet is on one relationship. If the relationship breaks, the loss does not revert.

This is the two-asset special case of [statistical arbitrage](statistical-arbitrage.md). It is also the case that most readers can test first.

## Research question

For pairs selected within one sector, using only data before the trading period, does a z-score rule on the spread earn a positive net return out of sample, and how often do the pairs stop being related?

## Signal

1. **Select pairs on a formation window** (for example 12 months). Test each candidate pair for cointegration, using Engle–Granger, and keep pairs that pass a threshold set in advance.
2. **Estimate the hedge ratio** by regression of one log price on the other, over the formation window.
3. **Build the spread** as the log price of one leg minus the hedge ratio times the log price of the other, and standardise it against its formation-window mean and standard deviation.
4. **Enter** when the z-score exceeds a threshold (commonly 2 in absolute value). **Exit** when it returns to zero. **Stop out** at a wider threshold (commonly 4), or after a stated holding period.
5. **Roll forward** the formation window, and re-select pairs at each roll.

The parameters are fixed before the trading window. Changing them after seeing trades is look-ahead in disguise.

## Data

- Adjusted daily prices for stocks within one sector, from at least five years before the trading period.
- Corporate actions applied before any spread is computed, since a bonus issue on one leg creates a false spread jump.
- For the short leg, futures or options prices if shorting cash equities is not possible for the investor. See [India trading costs](india-trading-costs.md).

## Costs

- Costs are paid on both legs, on every entry and exit. A pair that moves 1% in its spread per trade can be wiped out by round-trip costs on two legs.
- Short-leg financing, whether through futures basis or borrowing.
- Model the spread. Use the midpoint only with a stated fill assumption.

## Evaluation

- Report results per window, not pooled. A pooled result can hide a few years of losses.
- Report the number of pairs tested, and the number expected to pass by chance at the chosen significance level.
- Report the frequency of stop-outs and the average holding period.
- Report the deflated Sharpe ratio across thresholds and formation windows tried.

## What would show it does not work

- Net returns are not significant after costs in the trading windows.
- Most profits come from pairs that were selected in a window where the relationship was strongest, and fall off in later windows.
- Stop-outs cost more than the reverting trades earn.

## Common failure modes

- **Selection on the full sample.** The best pairs are chosen with information from the trading period.
- **Structural breaks.** A merger, a change in business mix, or a regulatory change can permanently move one leg.
- **Hidden factor exposure.** Two stocks in the same sector can share a sector factor that is not hedged. Check the residual exposure.
- **Testing many pairs.** Among 100 pairs at 5% significance, about five will pass by chance.

## Further reading

- Gatev, Goetzmann and Rouwenhorst (2006), "Pairs Trading: Performance of a Relative-Value Arbitrage Rule," *Review of Financial Studies*.
- Engle and Granger (1987), "Co-integration and Error Correction," *Econometrica*.
- Avellaneda and Lee (2010), "Statistical Arbitrage in the US Equities Market," *Quantitative Finance*.
