# Strategies

*Last reviewed: Oct 2026*

The strategy families that systematic and quantitative firms are known to use, and how to study each one in a way that tests whether it works. Each strategy file states a research question, a signal, the data it needs, the costs it must survive, and what would show it does not work.

This folder is for learning and research. Nothing here is investment advice, and nothing here describes any firm's actual trading book.

## Read this before the strategy files

- **Predictive is not profitable.** A signal can predict returns and still lose money once costs, market impact and risk are included. Every strategy file ends with a cost and capacity section for this reason.
- **Firm associations are public descriptions.** Firms describe their business in public material. Their exact strategies are generally confidential. The [firm profiles](firm-profiles.md) file records only what each firm's own site says, with a date.
- **Test before you trust.** Use [Project 03](../projects/03-honest-backtester/) and the [evaluation framework](evaluation-framework.md) for every strategy, and count every variant you try.

## The strategy families

| Family | What it does | Study it in | Repo project |
|---|---|---|---|
| Statistical arbitrage | Trades residual deviations after removing market and sector exposure | [Statistical arbitrage](statistical-arbitrage.md) | [Project 05](../projects/05-pairs-trading-cointegration/) (pairs), [Project 13](../projects/13-pca-nse-stocks/) (factors) |
| High-frequency market making | Quotes both sides, earns the spread, manages inventory and adverse selection | [Market making](market-making.md) | [Project 10](../projects/10-limit-order-book-simulator/), [Project 11](../projects/11-market-making-simulation/) |
| Factor investing and cross-sectional selection | Ranks stocks on characteristics associated with return differences | [Multi-factor equity](multi-factor-equity.md) | [Project 08](../projects/08-factor-model-indian-equities/) |
| Options volatility and relative value | Trades implied against realised volatility and relative prices across strikes and expiries | [Options relative value](options-relative-value.md) | [Project 02](../projects/02-implied-vol-surface/), [Project 14](../projects/14-finite-difference-black-scholes/) |
| Time-series momentum and trend following | Holds assets with positive trends, scales by volatility | [Time-series momentum](time-series-momentum.md) | [Project 16](../projects/16-time-series-momentum/) |
| Machine learning for return prediction | Nonlinear models of returns from many features | [ML alpha research](ml-alpha-research.md) | [Project 09](../projects/09-purged-cross-validation/) |
| Optimal execution and market impact | Decides how fast to trade a large order | [Execution and market impact](execution-and-impact.md) | [Project 17](../projects/17-optimal-execution/), with [Project 10](../projects/10-limit-order-book-simulator/) for the book |
| Systematic global macro | Trades rates, currencies and indices on macro signals | [Systematic macro](systematic-macro.md) | None yet |
| Pairs trading and relative value | Trades two related assets when their spread leaves its equilibrium | [Statistical arbitrage](statistical-arbitrage.md) | [Project 05](../projects/05-pairs-trading-cointegration/) |
| Portfolio optimisation and risk allocation | Turns signals into weights under risk, cost and exposure limits | [Portfolio optimisation](portfolio-optimisation.md) | [Project 06](../projects/06-covariance-shootout/), [Project 12](../projects/12-risk-engine-var-es/) |

## Where to start

Study in this order. Each step reuses the one before.

1. [Cross-sectional momentum](cross-sectional-momentum.md): the simplest signal with a long research record. It shows what a complete study looks like.
2. [Multi-factor equity](multi-factor-equity.md): combining signals, which needs the momentum work first.
3. [Statistical arbitrage](statistical-arbitrage.md): residual signals and their costs.
4. [Time-series momentum](time-series-momentum.md): a different signal family, to compare with step 1.
5. [ML alpha research](ml-alpha-research.md): only after the simple models are well tested.
6. [Portfolio optimisation](portfolio-optimisation.md): applies to every strategy above.

## Files in this folder

| File | Covers |
|---|---|
| [Cross-sectional momentum](cross-sectional-momentum.md) | Ranking stocks by past return, with trend filters and volatility sizing |
| [Multi-factor equity](multi-factor-equity.md) | Combining momentum, value, quality and low volatility |
| [Statistical arbitrage](statistical-arbitrage.md) | Residual reversion after market and sector exposure, and pairs |
| [Time-series momentum](time-series-momentum.md) | Trend signals on each asset, scaled by volatility |
| [ML alpha research](ml-alpha-research.md) | Gradient boosting and regularised models, with evaluation discipline |
| [Portfolio optimisation](portfolio-optimisation.md) | Turning signals into weights with costs and constraints |
| [Market making](market-making.md) | Quoting, inventory, adverse selection |
| [Options relative value](options-relative-value.md) | Implied against realised volatility, variance risk premium |
| [Execution and market impact](execution-and-impact.md) | VWAP, TWAP, implementation shortfall, impact models |
| [Systematic macro](systematic-macro.md) | Macro signals across asset classes |
| [Evaluation framework](evaluation-framework.md) | Metrics, validation pipeline, and the falsification checklist for every strategy |
| [India trading costs](india-trading-costs.md) | Cost components for Indian equities and derivatives, and how to model them |
| [Firm profiles](firm-profiles.md) | What each firm's own site says, with the date checked |
| [Public research](public-research.md) | Free datasets and papers to start from |

## What this folder does not do

- It does not give parameter values to trade. Every number in a strategy file is a starting point to test, not a recommendation.
- It does not claim any firm uses any strategy described here. The firm profiles record public descriptions only.
- It does not replace the [roadmaps](../roadmaps/) or the [projects](../projects/). Use the strategy files to choose what to build.
