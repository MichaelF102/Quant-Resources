# Papers

*Last reviewed: Oct 2026*

Academic articles cited across the cheat sheets and projects, grouped by topic. Each entry gives the authors, year, venue and the place in this repo where it is used. Links to the articles are not included here, because they were not checked during review; search the title and the journal to find an accessible copy.

Read the abstract and the main result first. Most of these papers are short enough to read in an afternoon, but a few (marked) are long and are best read in sections.

## Momentum and signals

| Paper | Why read it | Used in |
|---|---|---|
| Jegadeesh and Titman (1993), "Returns to Buying Winners and Selling Losers," *Journal of Finance* | The original momentum study. | [Project 04](../projects/04-momentum-mean-reversion-study/) |
| Moskowitz, Ooi and Pedersen (2012), "Time Series Momentum," *Journal of Financial Economics* | Time-series momentum across asset classes. | [Project 04](../projects/04-momentum-mean-reversion-study/) |
| Brock, Lakonishok and LeBaron (1992), "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns," *Journal of Finance* | The classic positive result on moving-average rules. Read with Sullivan et al. | [Technical indicators](../cheatsheets/technical-indicators.md), [Project 15](../projects/15-technical-indicator-study/) |
| Sullivan, Timmermann and White (1999), "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap," *Journal of Finance* | Shows how the apparent profitability of many rules disappears once the number of rules tested is counted. | [Project 15](../projects/15-technical-indicator-study/) |

## Pairs trading and cointegration

| Paper | Why read it | Used in |
|---|---|---|
| Engle and Granger (1987), "Co-integration and Error Correction," *Econometrica* | The two-step cointegration test and error-correction models. | [Time series](../cheatsheets/time-series.md), [Project 05](../projects/05-pairs-trading-cointegration/) |
| Johansen (1988), "Statistical Analysis of Cointegration Vectors," *Journal of Economic Dynamics and Control* | The multivariate cointegration test. | [Time series](../cheatsheets/time-series.md), [Project 05](../projects/05-pairs-trading-cointegration/) |
| Gatev, Goetzmann and Rouwenhorst (2006), "Pairs Trading: Performance of a Relative-Value Arbitrage Rule," *Review of Financial Studies* | A careful test of a simple pairs rule. | [Project 05](../projects/05-pairs-trading-cointegration/) |

## Volatility

| Paper | Why read it | Used in |
|---|---|---|
| Engle (1982), "Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation," *Econometrica* | Introduces the ARCH model. | [Time series](../cheatsheets/time-series.md), [Project 07](../projects/07-garch-volatility-forecasting/) |
| Bollerslev (1986), "Generalized Autoregressive Conditional Heteroskedasticity," *Journal of Econometrics* | Introduces GARCH. | [Project 07](../projects/07-garch-volatility-forecasting/) |
| Patton (2011), "Volatility Forecast Comparison Using Imperfect Volatility Proxies," *Journal of Econometrics* | Why the choice of loss function matters in volatility forecasting. | [Project 07](../projects/07-garch-volatility-forecasting/) |
| Breeden and Litzenberger (1978), "Prices of State-Contingent Claims Implicit in Option Prices," *Journal of Business* | Recovers the risk-neutral density from option prices. | [Project 02](../projects/02-implied-vol-surface/) stretch goals |

## Covariance and factors

| Paper | Why read it | Used in |
|---|---|---|
| Ledoit and Wolf (2004), "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices," *Journal of Multivariate Analysis* | The shrinkage estimator. | [Linear algebra](../cheatsheets/linear-algebra.md), [Project 06](../projects/06-covariance-shootout/) |
| Ledoit and Wolf (2003), "Honey, I Shrunk the Sample Covariance Matrix," *Journal of Portfolio Management* | A readable account of why shrinkage helps. | [Project 06](../projects/06-covariance-shootout/) |
| Fama and French (1993), "Common Risk Factors in the Returns on Stocks and Bonds," *Journal of Financial Economics* | The three-factor model. | [Project 08](../projects/08-factor-model-indian-equities/) |
| Fama and MacBeth (1973), "Risk, Return, and Equilibrium: Empirical Tests," *Journal of Political Economy* | Cross-sectional regression for factor premia. | [Project 08](../projects/08-factor-model-indian-equities/) |
| Laloux, Cizeau, Bouchaud and Potters (1999), "Noise Dressing of Financial Correlation Matrices," *Physical Review Letters* | Separates signal from noise in correlation matrices. | [Project 13](../projects/13-pca-nse-stocks/) |

## Machine learning and backtesting

| Paper | Why read it | Used in |
|---|---|---|
| Bailey and López de Prado (2014), "The Deflated Sharpe Ratio," *Journal of Portfolio Management* | The multiple-testing correction for Sharpe ratios. | [Performance metrics](../cheatsheets/performance-metrics.md), [Project 09](../projects/09-purged-cross-validation/) |
| Bailey, Borwein, López de Prado and Zhu (2014), "Pseudo-Mathematics and Financial Charlatanism," *Notices of the AMS* | How backtest overfitting inflates results. | [Project 09](../projects/09-purged-cross-validation/), [Pitfalls](../pitfalls.md) |
| Lo (2002), "The Statistics of Sharpe Ratios," *Financial Analysts Journal* | Standard errors for Sharpe ratios, and the effect of autocorrelation. | [Performance metrics](../cheatsheets/performance-metrics.md) |

## Market microstructure and market making

| Paper | Why read it | Used in |
|---|---|---|
| Avellaneda and Stoikov (2008), "High-frequency trading in a limit order book," *Quantitative Finance* | Inventory-aware quoting. The model in Project 11. | [Project 11](../projects/11-market-making-simulation/), [QT roadmap](../roadmaps/quant-trader.md) |
| Glosten and Milgrom (1985), "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders," *Journal of Financial Economics* | Adverse selection and the bid-ask spread. | [Project 11](../projects/11-market-making-simulation/), [Market microstructure](../cheatsheets/market-microstructure.md) |
| Kyle (1985), "Continuous Auctions and Insider Trading," *Econometrica* | Informed trading and price impact. | [Project 11](../projects/11-market-making-simulation/) |

## Credit and risk

| Paper | Why read it | Used in |
|---|---|---|
| Merton (1974), "On the Pricing of Corporate Debt: The Risk Structure of Interest Rates," *Journal of Finance* | Equity as a call on firm assets. The structural credit model. | [Credit risk](../cheatsheets/credit-risk.md) |
| Kupiec (1995), "Techniques for Verifying the Accuracy of Risk Measurement Models," *Journal of Derivatives* | The proportion-of-failures test for VaR. | [Project 12](../projects/12-risk-engine-var-es/) |
| Christoffersen (1998), "Evaluating Interval Forecasts," *International Economic Review* | Tests the independence of VaR exceptions. | [Project 12](../projects/12-risk-engine-var-es/) |

## Reading order

For a first pass through the empirical literature, read in this order: Jegadeesh and Titman, Sullivan et al., Bailey and López de Prado, Ledoit and Wolf (2004), and Avellaneda and Stoikov. These five cover signals, multiple testing, covariance, and market making, which are the four most common themes in the projects.

See [books](books.md) for the textbooks that cover the same material in depth.
