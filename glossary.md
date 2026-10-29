# Glossary

*Last reviewed: Oct 2026*

Short definitions of the terms used across the repo, with a link to where each one is developed. Definitions are brief on purpose; follow the link for the formula and the caveats.

## A

- **Adverse selection.** The loss a liquidity provider makes when trading against better-informed counterparties. See [Market microstructure](cheatsheets/market-microstructure.md).
- **Alpha.** Return not explained by exposure to a benchmark or factors. The intercept in a regression on excess returns. See [Performance metrics](cheatsheets/performance-metrics.md).
- **American option.** An option that can be exercised at any time up to expiry. See [Options problems](interview/options-derivatives.md).
- **ARCH / GARCH.** Models in which today's variance depends on past squared shocks (ARCH) and past variances (GARCH). See [Time series](cheatsheets/time-series.md).
- **ARMA.** A model combining autoregressive and moving-average terms. See [Time series](cheatsheets/time-series.md).
- **Arbitrage.** A riskless profit with no net investment. Pricing models assume it is absent. See [Options problems](interview/options-derivatives.md).
- **Ask.** The lowest price a seller will accept. See [Market microstructure](cheatsheets/market-microstructure.md).
- **Avellaneda–Stoikov model.** A market-making model with inventory-dependent quotes. See [Project 11](projects/11-market-making-simulation/).

## B

- **Backtest.** A test of a trading rule on historical data. See [Pitfalls](pitfalls.md) and [Project 03](projects/03-honest-backtester/).
- **Basis points (bp).** One hundredth of a percentage point. Also used for trading costs. See [Fixed income](cheatsheets/fixed-income.md).
- **Bhavcopy.** The daily end-of-day file published by the exchange. See [Data sources](data/data-sources.md).
- **Bid.** The highest price a buyer will pay. See [Market microstructure](cheatsheets/market-microstructure.md).
- **Black-76.** The Black model for options on forwards and futures. See [Greeks](cheatsheets/greeks.md).
- **Black-Scholes.** The option pricing formula under geometric Brownian motion with constant volatility. See [Greeks](cheatsheets/greeks.md) and [Stochastic calculus](cheatsheets/stochastic-calculus.md).
- **Block bootstrap.** Resampling blocks of consecutive observations to keep dependence. See [Performance metrics](cheatsheets/performance-metrics.md).
- **Brownian motion.** A continuous process with independent normal increments. See [Stochastic calculus](cheatsheets/stochastic-calculus.md).

## C

- **CAGR.** Compound annual growth rate. See [Performance metrics](cheatsheets/performance-metrics.md).
- **Calmar ratio.** Return divided by the absolute maximum drawdown. See [Performance metrics](cheatsheets/performance-metrics.md).
- **Cointegration.** Two or more non-stationary series whose linear combination is stationary. See [Time series](cheatsheets/time-series.md) and [Project 05](projects/05-pairs-trading-cointegration/).
- **Convexity.** The second derivative of a bond's price with respect to yield, or of an option's price with respect to the underlying. See [Fixed income](cheatsheets/fixed-income.md).
- **Corporate action.** A split, bonus, dividend, merger or similar event that changes a stock's price or identity. See [Data sources](data/data-sources.md).
- **Credit default swap (CDS).** A contract that pays on a reference entity's default. See [Credit risk](cheatsheets/credit-risk.md).
- **CVaR.** Another name for expected shortfall. See [Performance metrics](cheatsheets/performance-metrics.md).

## D

- **Day-count convention.** The rule for counting days between cash flows. See [Fixed income](cheatsheets/fixed-income.md).
- **Deflated Sharpe ratio.** A Sharpe ratio adjusted for the number of trials that produced it. See [Performance metrics](cheatsheets/performance-metrics.md) and [Project 09](projects/09-purged-cross-validation/).
- **Delta.** The sensitivity of an option's price to the underlying price. See [Greeks](cheatsheets/greeks.md).
- **Drawdown.** The fall from a running peak in equity. See [Performance metrics](cheatsheets/performance-metrics.md).
- **DV01.** The change in a bond's price for a one-basis-point change in yield. See [Fixed income](cheatsheets/fixed-income.md).

## E

- **EAD.** Exposure at default: the amount owed when a borrower defaults. See [Credit risk](cheatsheets/credit-risk.md).
- **Effective spread.** Twice the distance of a trade price from the mid price. See [Market microstructure](cheatsheets/market-microstructure.md).
- **Expected shortfall (ES).** The average loss beyond the VaR quantile. See [Performance metrics](cheatsheets/performance-metrics.md) and [Project 12](projects/12-risk-engine-var-es/).
- **Expected value.** The probability-weighted average of outcomes. See [Probability](cheatsheets/probability.md).

## F

- **Feller condition.** The condition 2κθ ≥ σ² that keeps a CIR process strictly positive. See [Stochastic calculus](cheatsheets/stochastic-calculus.md).
- **Fama–MacBeth regression.** Cross-sectional regressions run each period, with the coefficients averaged over time. See [Project 08](projects/08-factor-model-indian-equities/).
- **Forward price.** The price agreed today for delivery at a future date. See [Options problems](interview/options-derivatives.md).
- **FRTB.** The Basel framework for market-risk capital. See [Risk and model validation roadmap](roadmaps/risk-model-validation.md).

## G

- **Gamma.** The rate of change of delta. See [Greeks](cheatsheets/greeks.md).
- **GBM.** Geometric Brownian motion: the model of prices with lognormal returns. See [Stochastic calculus](cheatsheets/stochastic-calculus.md).
- **Girsanov theorem.** The result that changes the drift of Brownian motion by changing probability measure. See [Stochastic calculus](cheatsheets/stochastic-calculus.md).
- **Greeks.** Sensitivities of an option's value to its inputs. See [Greeks](cheatsheets/greeks.md).

## H

- **Hazard rate.** The instantaneous probability of default, given survival so far. See [Credit risk](cheatsheets/credit-risk.md).
- **Hedge ratio.** The number of units of one asset used to offset exposure to another. See [Project 05](projects/05-pairs-trading-cointegration/).

## I

- **Idempotent.** An operation that gives the same result when repeated. Required for safe data loads. See [Databases and storage](tools-and-technologies/databases-and-storage.md).
- **Implied volatility.** The volatility that makes a model price equal the market price. See [Project 02](projects/02-implied-vol-surface/).
- **Information coefficient (IC).** The correlation between a signal and the subsequent return. See [Performance metrics](cheatsheets/performance-metrics.md) and [Project 04](projects/04-momentum-mean-reversion-study/).
- **Inventory risk.** The risk a market maker carries from holding a position. See [Project 11](projects/11-market-making-simulation/).
- **Itô's lemma.** The chain rule for stochastic processes, with a second-order term. See [Stochastic calculus](cheatsheets/stochastic-calculus.md).

## K

- **Kelly criterion.** The bet size that maximises the long-run growth rate of wealth. See [Probability](cheatsheets/probability.md) and [Performance metrics](cheatsheets/performance-metrics.md).
- **Kupiec test.** A likelihood-ratio test of the number of VaR exceptions. See [Project 12](projects/12-risk-engine-var-es/).

## L

- **LGD.** Loss given default: the fraction of exposure lost after default. See [Credit risk](cheatsheets/credit-risk.md).
- **Limit order.** An order to trade at a stated price or better. See [Market microstructure](cheatsheets/market-microstructure.md).
- **Lookahead bias.** Using information that was not available at the time of the decision. See [Pitfalls](pitfalls.md).
- **Lot size.** The minimum contract quantity for a derivative. See [Data sources](data/data-sources.md).

## M

- **Macaulay duration.** The weighted average time to a bond's cash flows. See [Fixed income](cheatsheets/fixed-income.md).
- **Market impact.** The movement of price caused by a trade. See [Market microstructure](cheatsheets/market-microstructure.md).
- **Martingale.** A process whose expected future value equals its current value. See [Stochastic calculus](cheatsheets/stochastic-calculus.md).
- **Merton model.** The structural credit model in which equity is a call on firm assets. See [Credit risk](cheatsheets/credit-risk.md).
- **Mid price.** The average of the best bid and ask. See [Market microstructure](cheatsheets/market-microstructure.md).

## N

- **Nelson–Siegel.** A parametric curve used to fit the yield curve. See [Fixed income](cheatsheets/fixed-income.md).
- **Novikov condition.** A sufficient condition for a change of measure to be valid. See [Stochastic calculus](cheatsheets/stochastic-calculus.md).

## O

- **OLS.** Ordinary least squares: the standard regression estimator. See [Linear algebra](cheatsheets/linear-algebra.md).
- **Ornstein–Uhlenbeck process.** A mean-reverting diffusion. See [Stochastic calculus](cheatsheets/stochastic-calculus.md).
- **Open interest (OI).** The number of outstanding derivative contracts. See [Data sources](data/data-sources.md).

## P

- **PCA.** Principal component analysis: the eigenvectors of the covariance matrix. See [Linear algebra](cheatsheets/linear-algebra.md) and [Project 13](projects/13-pca-nse-stocks/).
- **PD.** Probability of default. See [Credit risk](cheatsheets/credit-risk.md).
- **Price-time priority.** The matching rule: better prices first, then earlier orders. See [Market microstructure](cheatsheets/market-microstructure.md).
- **Probabilistic Sharpe ratio.** The probability that the true Sharpe exceeds a benchmark, given sample size and higher moments. See [Performance metrics](cheatsheets/performance-metrics.md).
- **Purging and embargo.** Removing training observations that overlap a test period, and a gap after it. See [Project 09](projects/09-purged-cross-validation/).
- **Put-call parity.** The identity C − P = S − Ke^(−rT). See [Options problems](interview/options-derivatives.md).

## Q

- **QLIKE.** A loss function for volatility forecasts that is robust to noise in the realised measure. See [Project 07](projects/07-garch-volatility-forecasting/).

## R

- **Reservation price.** The price at which a market maker is indifferent to a trade, given its current inventory. See [Project 11](projects/11-market-making-simulation/).
- **Risk-neutral measure.** The probability measure under which discounted prices are martingales. See [Stochastic calculus](cheatsheets/stochastic-calculus.md).
- **Rho.** The sensitivity of an option's value to the interest rate. See [Greeks](cheatsheets/greeks.md).

## S

- **Sharpe ratio.** Mean excess return divided by its standard deviation. See [Performance metrics](cheatsheets/performance-metrics.md).
- **Shrinkage.** Pulling an estimate towards a target to reduce its variance. See [Linear algebra](cheatsheets/linear-algebra.md) and [Project 06](projects/06-covariance-shootout/).
- **Stationarity.** A property of a process whose mean, variance and autocovariances do not depend on time. See [Time series](cheatsheets/time-series.md).
- **Stop order.** An order that becomes a market order when a trigger price trades. See [Market microstructure](cheatsheets/market-microstructure.md).

## T

- **Theta.** The sensitivity of an option's value to the passage of time. See [Greeks](cheatsheets/greeks.md).
- **Tracking error.** The standard deviation of the difference between a portfolio's return and a benchmark's. See [Performance metrics](cheatsheets/performance-metrics.md).
- **Turnover.** The fraction of a portfolio traded in a period. See [Performance metrics](cheatsheets/performance-metrics.md).

## U

- **Unit root.** A stochastic trend, such as in a random walk. See [Time series](cheatsheets/time-series.md).

## V

- **VaR.** Value at Risk: a loss quantile over a horizon. See [Performance metrics](cheatsheets/performance-metrics.md) and [Project 12](projects/12-risk-engine-var-es/).
- **Vega.** The sensitivity of an option's value to volatility. See [Greeks](cheatsheets/greeks.md).
- **Vanna and volga.** Second-order Greeks: the cross-derivative of delta with volatility, and the second derivative with volatility. See [Greeks](cheatsheets/greeks.md).

## W

- **White noise.** A sequence of uncorrelated variables with zero mean and constant variance. See [Time series](cheatsheets/time-series.md).

## Y

- **Yield to maturity (YTM).** The single discount rate that equates a bond's price to its cash flows. See [Fixed income](cheatsheets/fixed-income.md).
