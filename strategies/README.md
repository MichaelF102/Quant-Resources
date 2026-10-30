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
| Pairs trading and relative value | Trades two related assets when their spread leaves its equilibrium | [Pairs trading](pairs-trading.md) | [Project 05](../projects/05-pairs-trading-cointegration/) |
| Portfolio optimisation and risk allocation | Turns signals into weights under risk, cost and exposure limits | [Portfolio optimisation](portfolio-optimisation.md) | [Project 06](../projects/06-covariance-shootout/), [Project 12](../projects/12-risk-engine-var-es/) |
| Cross-sectional momentum | Ranks stocks on past return, skipping the latest month | [Cross-sectional momentum](cross-sectional-momentum.md) | [Project 04](../projects/04-momentum-mean-reversion-study/) |
| Short-term reversal | Holds recent losers and shorts recent winners over days to a month | [Short-term reversal](short-term-reversal.md) | [Project 04](../projects/04-momentum-mean-reversion-study/) |
| Carry | Holds assets with high yield or roll return, across currencies, bonds and commodities | [Carry](carry.md) | None yet |
| Index and basis arbitrage | Trades the gap between index futures and the cost-of-carry price of the basket | [Index and basis arbitrage](index-and-basis-arbitrage.md) | None yet |
| Value | Holds stocks cheap on book or earnings relative to price | [Value](value.md) | [Project 08](../projects/08-factor-model-indian-equities/) |
| Quality | Holds profitable, stable, low-leverage firms | [Quality](quality.md) | [Project 08](../projects/08-factor-model-indian-equities/) |
| Low volatility | Holds low-volatility or low-beta stocks | [Low volatility](low-volatility.md) | [Project 08](../projects/08-factor-model-indian-equities/) |
| Post-earnings announcement drift | Trades in the direction of earnings surprises over the following weeks | [Post-earnings announcement drift](post-earnings-announcement-drift.md) | None yet |
| Merger arbitrage | Holds the target of an announced deal, earning the spread if it closes | [Merger arbitrage](merger-arbitrage.md) | None yet |
| Fixed-income relative value | Trades curve, swap-spread and futures-basis relationships, hedged for duration | [Fixed-income relative value](fixed-income-relative-value.md) | None yet |
| Order-flow imbalance | Predicts short-horizon price moves from changes in book depth | [Order-flow imbalance](order-flow-imbalance.md) | [Project 10](../projects/10-limit-order-book-simulator/), [Project 11](../projects/11-market-making-simulation/) |
| Alternative data and sentiment | Uses text and other non-price data to predict returns | [Alternative data and sentiment](alternative-data-and-sentiment.md) | [Project 09](../projects/09-purged-cross-validation/) (evaluation) |
| Dispersion and volatility arbitrage | Trades index volatility against component volatility, and implied against realised correlation | [Dispersion and volatility arbitrage](dispersion-and-volatility-arbitrage.md) | [Project 02](../projects/02-implied-vol-surface/), [Project 14](../projects/14-finite-difference-black-scholes/) |
| Risk parity | Allocates so each asset contributes equal risk | [Risk parity](risk-parity.md) | [Project 06](../projects/06-covariance-shootout/), [Project 12](../projects/12-risk-engine-var-es/) |
| Lead–lag across markets | Trades a lagging instrument on the recent move of a related one | [Lead–lag across related markets](lead-lag-cross-market.md) | None yet |
| Seasonality and calendar effects | Trades stated calendar windows, such as month-end or expiry periods | [Seasonality and calendar effects](seasonality-and-calendar-effects.md) | None yet |
| Industry momentum | Holds the best-performing sectors over the past several months | [Industry momentum](industry-momentum.md) | [Project 04](../projects/04-momentum-mean-reversion-study/) (ranking and evaluation) |
| Tail-risk hedging | Buys protection against rare large losses, paying a steady premium | [Tail-risk hedging](tail-risk-hedging.md) | [Project 12](../projects/12-risk-engine-var-es/), [Project 02](../projects/02-implied-vol-surface/) |
| Mean reversion (single asset) | Trades the deviation of a price from its own moving average, in volatility units | [Mean reversion (single asset)](mean-reversion-single-asset.md) | [Project 04](../projects/04-momentum-mean-reversion-study/), [Project 15](../projects/15-technical-indicator-study/) |
| Trend-following rules | Moving-average crossovers, Donchian channels, SuperTrend and ATR stops | [Trend-following rules](trend-following-rules.md) | [Project 15](../projects/15-technical-indicator-study/), [Project 16](../projects/16-time-series-momentum/) |
| Breakout and volatility expansion | Buys range breaks confirmed by volume, with ATR stops | [Breakout and volatility expansion](breakout-volatility-expansion.md) | [Project 15](../projects/15-technical-indicator-study/) |
| Regime switching | Changes exposure according to an estimated market state | [Regime switching](regime-switching.md) | [Project 09](../projects/09-purged-cross-validation/) (validation) |
| Size | Small-cap against large-cap, with a liquidity filter | [Size](size.md) | [Project 08](../projects/08-factor-model-indian-equities/) |

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
| [Pairs trading](pairs-trading.md) | Two-stock spreads: pair selection, hedge ratios, stop-outs and structural breaks |
| [Short-term reversal](short-term-reversal.md) | Short-horizon reversal, its liquidity dependence, and its turnover cost |
| [Carry](carry.md) | Carry across currencies, bonds and commodities, and its crash profile |
| [Index and basis arbitrage](index-and-basis-arbitrage.md) | Cash–futures arbitrage on NSE, cost-of-carry thresholds, and expiry risk |
| [Value](value.md) | Book-to-price and earnings-to-price, point-in-time fundamentals and value traps |
| [Quality](quality.md) | Profitability, accruals and leverage, and overlap with value |
| [Low volatility](low-volatility.md) | Low volatility and low beta, the leverage-constraint explanation, and rising-market lag |
| [Post-earnings announcement drift](post-earnings-announcement-drift.md) | Earnings surprises, announcement timing and the drift after them |
| [Merger arbitrage](merger-arbitrage.md) | Deal spreads, implied completion probability and failure risk |
| [Fixed-income relative value](fixed-income-relative-value.md) | Curve, swap-spread and bond-futures basis trades, hedged for duration |
| [Order-flow imbalance](order-flow-imbalance.md) | Book-depth changes and short-horizon price impact |
| [Alternative data and sentiment](alternative-data-and-sentiment.md) | Text signals, publication-time leakage and dictionary overfitting |
| [Dispersion and volatility arbitrage](dispersion-and-volatility-arbitrage.md) | Implied against realised correlation and correlation-spike risk |
| [Risk parity](risk-parity.md) | Equal risk contributions, leverage cost and correlation regimes |
| [Lead–lag across related markets](lead-lag-cross-market.md) | Cross-autocorrelation across instruments and non-synchronous closes |
| [Seasonality and calendar effects](seasonality-and-calendar-effects.md) | Calendar windows, data-mining risk, and the discipline needed to test them |
| [Industry momentum](industry-momentum.md) | Sector-level momentum and its overlap with stock momentum |
| [Tail-risk hedging](tail-risk-hedging.md) | Protection instruments, their premium, and when a hedge pays for itself |
| [Mean reversion (single asset)](mean-reversion-single-asset.md) | Z-scores against a price's own average, news-driven deviations, and trend mistaken for reversion |
| [Trend-following rules](trend-following-rules.md) | Rule-based trend systems, the contribution of each component, and parameter overfitting |
| [Breakout and volatility expansion](breakout-volatility-expansion.md) | Range breaks, same-bar entry, and false breakouts |
| [Regime switching](regime-switching.md) | Hidden-state models, filtering versus smoothing, and label switching |
| [Size](size.md) | The small-cap premium, share-count errors, and the liquidity filter it depends on |
| [Evaluation framework](evaluation-framework.md) | Metrics, validation pipeline, and the falsification checklist for every strategy |
| [India trading costs](india-trading-costs.md) | Cost components for Indian equities and derivatives, and how to model them |
| [Firm profiles](firm-profiles.md) | What each firm's own site says, with the date checked |
| [Public research](public-research.md) | Free datasets and papers to start from |

## What this folder does not do

- It does not give parameter values to trade. Every number in a strategy file is a starting point to test, not a recommendation.
- It does not claim any firm uses any strategy described here. The firm profiles record public descriptions only.
- It does not replace the [roadmaps](../roadmaps/) or the [projects](../projects/). Use the strategy files to choose what to build.
