# Risk parity

*Last reviewed: Oct 2026*

**Difficulty:** intermediate · **Holding period:** monthly rebalance · **Repo projects:** [Project 06](../projects/06-covariance-shootout/) (covariance inputs), [Project 12](../projects/12-risk-engine-var-es/) (risk measurement)

## Idea

Most portfolios that look diversified by capital are dominated by their most volatile holding. Risk parity allocates so that each asset contributes an equal share of total portfolio risk. A low-volatility asset such as government bonds gets a larger capital weight than an equity index, so the risk is shared. Risk parity is an allocation method rather than a signal, and it is often applied on top of other strategies or across asset classes.

## Research question

Across a diversified set of assets, does an equal-risk-contribution allocation earn a better risk-adjusted return than equal-weight or market-cap allocation, net of costs, and how does it behave when correlations between assets change?

## Method

For a portfolio with weights w and covariance matrix Σ, the risk contribution of asset i is

RC_i = w_i (Σw)_i / (wᵀΣw)

Equal risk contribution sets RC_i = 1/n for all i. There is no closed form in general. Solve numerically, with non-negative weights that sum to one, and check that the solution satisfies the equal-risk condition to a stated tolerance.

Steps:

1. Estimate the covariance matrix on a rolling window, using shrinkage as in [Project 06](../projects/06-covariance-shootout/).
2. Solve for equal risk contributions each month.
3. Hold the weights until the next rebalance, and record the turnover.
4. Optionally, apply a volatility target to the whole portfolio, scaling exposure up or down.

## Data

- Daily returns for a diversified set of assets: equity indices, government bonds, gold, and possibly currencies. Use instruments that can be traded at the modelled size.
- Covariance estimates with a stated window and shrinkage method.
- Financing costs for any leverage used to reach the volatility target.

## Costs

- Rebalancing costs, which depend on how much the risk weights change each month.
- Futures roll and margin costs for instruments held through futures.
- Financing for leverage, which can be large when bond weights are scaled up to match equity risk.

## Evaluation

- Report the portfolio's return, volatility, Sharpe ratio and maximum drawdown, net of costs.
- Report the realised risk contributions over time, to check that they stayed near equal.
- Compare with equal weight, market-cap weight and a 60/40 benchmark on the same assets and dates.
- Report the sensitivity to the covariance window and shrinkage intensity.
- Report the deflated Sharpe ratio across windows and assets tried.

## What would show it does not work

- The risk-parity portfolio does not beat the simple benchmarks net of financing and costs.
- Its performance depends on a long run of falling bond yields, which is a rates bet rather than a diversification result.
- Equal risk contributions are unstable because the covariance estimates change sharply from month to month.

## Common failure modes

- **Leverage hidden in the weights.** Scaling up a low-volatility asset to match risk requires leverage, whose cost and margin are easy to ignore.
- **Correlation regime change.** In some periods, stocks and bonds fall together, and the diversification assumption fails.
- **Estimation error.** A covariance matrix from a short window produces unstable weights. Test the sensitivity to the window.

## Further reading

- Maillard, Roncalli and Teïletche (2010), "On the Properties of Equally-Weighted Risk Contributions Portfolios," *Journal of Portfolio Management*.
- Ledoit and Wolf (2004), "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices," *Journal of Multivariate Analysis*.
- Grinold and Kahn, *Active Portfolio Management* 💸, on risk budgeting.
