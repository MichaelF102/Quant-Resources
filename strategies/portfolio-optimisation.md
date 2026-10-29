# Portfolio optimisation

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Applies to:** every strategy in this folder · **Repo projects:** [Project 06](../projects/06-covariance-shootout/), [Project 12](../projects/12-risk-engine-var-es/)

## Idea

A signal says which assets to favour. A portfolio decides how much to hold of each, given expected returns, risk, trading costs, and limits on exposure. Optimisation can add value, but it is also the easiest place to overfit: a small change in the expected returns can move the weights a great deal. Good practice keeps the optimiser simple, regularises its inputs, and compares it with a naive benchmark.

## Research question

Does a constrained optimiser, using shrunk covariance estimates and a turnover penalty, improve net risk-adjusted returns over equal weighting and inverse-volatility weighting, out of sample?

## Methods

- **Equal weight (1/N).** The benchmark that is hard to beat. DeMiguel, Garlappi and Uppal (2009) found that many optimised portfolios fail to beat it out of sample.
- **Inverse volatility.** Weights proportional to the inverse of each asset's volatility.
- **Minimum variance.** Minimise portfolio variance subject to constraints, using a shrunk covariance estimate. See [Project 06](../projects/06-covariance-shootout/).
- **Mean-variance.** Maximise expected return minus a risk penalty. Sensitive to expected returns, which are hard to estimate.
- **Risk parity.** Equalise each asset's contribution to portfolio risk.
- **Volatility targeting.** Scale the whole portfolio so its expected volatility is a stated target.

Use a solver library such as cvxpy for constrained problems. See [quant libraries](../tools-and-technologies/quant-libraries.md).

## Constraints to include

- Long-only or long-short, stated.
- Maximum single-asset and sector weights.
- Gross and net exposure limits.
- Turnover limit or a turnover penalty per rebalance.
- A minimum liquidity filter for holdings.

## Data

- Returns for the assets in the universe, with the covariance estimated on a stated window and shrinkage method.
- Expected returns, if the method uses them, with the signal that produced them documented.
- Transaction cost estimates for each asset, from [India trading costs](india-trading-costs.md).

## Evaluation

- Compare every method on the same universe, dates, costs and constraints.
- Report net Sharpe, maximum drawdown, turnover and the concentration of the weights.
- Report the out-of-sample forecast error of volatility, using the method in [Project 06](../projects/06-covariance-shootout/).
- Test sensitivity: how much the weights change when the inputs change slightly. A method whose weights swing wildly is not robust.

## What would show it does not work

- The optimiser does not beat equal weighting net of costs.
- Turnover is so high that costs erase the advantage.
- Weights concentrate in a few assets, and the concentration is not justified by the signal.

## Common failure modes

- **Estimation error.** Expected returns are much noisier than covariances. Optimising on them amplifies the noise.
- **Covariance from a short sample.** Use shrinkage, and check the condition number.
- **Ignoring turnover.** An optimiser that rebalances daily on noise pays costs that the backtest may not show.
- **Using the same data to choose constraints and evaluate.** Choose constraints before the test period.

## Further reading

- DeMiguel, Garlappi and Uppal (2009), "Optimal Versus Naive Diversification: How Inefficient Is the 1/N Portfolio Strategy?," *Review of Financial Studies*.
- Ledoit and Wolf (2004), "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices," *Journal of Multivariate Analysis*.
- Grinold and Kahn, *Active Portfolio Management* 💸, on turning forecasts into positions.
