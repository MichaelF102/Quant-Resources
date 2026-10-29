# ML alpha research

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** depends on the prediction horizon · **Repo project:** [Project 09](../projects/09-purged-cross-validation/)

## Idea

Machine-learning models can learn nonlinear relationships between many features and future returns, such as interactions between volatility, liquidity and momentum. The research question is whether a model's out-of-sample predictions carry information that a simple linear model does not, after the cost of a more complex model and the cost of trading on its predictions.

## Research question

Does a gradient-boosted or regularised model predict cross-sectional returns in NSE equities out of sample better than a simple linear model on the same features, and does the difference survive trading costs and selection bias?

## Method

1. **Define the target.** A forward return over a stated horizon, cross-sectionally demeaned or ranked each period. Store the start and end dates of each label, since overlapping labels cause leakage.
2. **Build features.** Use only information available at each date: lagged returns, volatility, volume, liquidity, and point-in-time fundamentals. Document each feature's lookback.
3. **Split the data.** Use purged, embargoed splits, as in [Project 09](../projects/09-purged-cross-validation/). Hold out a final period that is not touched during model development.
4. **Fit a baseline.** A regularised linear model on the same features. A model that cannot beat this baseline does not justify its complexity.
5. **Fit the candidates.** Gradient-boosted trees (such as LightGBM or XGBoost) and, optionally, a neural network. Keep hyperparameter ranges fixed in advance.
6. **Turn predictions into positions.** Rank by prediction, hold the top and bottom groups, and apply the same portfolio rules to every model.
7. **Evaluate on the final period** once, and report it.

## Evaluation

- The information coefficient on the held-out period, with its standard error, and the decay of IC over horizons.
- Net-of-cost returns of the portfolio built from each model.
- The deflated Sharpe ratio across all models and hyperparameter settings tried.
- A feature-importance analysis that is stable across periods. An importance that changes sign by period is a warning.

## Costs and capacity

- A model that predicts well but trades every day can lose its edge entirely to costs. Report turnover.
- A signal that works only in small, illiquid stocks has little capacity. Report the portfolio's value-weighted exposure to the smallest stocks.

## What would show it does not work

- The gradient-boosted model does not beat the linear baseline out of sample.
- The IC is positive in-sample but falls to zero on the final period.
- Net returns are negative after costs, even when gross IC is positive.

## Common failure modes

- **Leakage.** Shuffled cross-validation, overlapping labels, and features that use future data. Test the splitter directly.
- **Selection bias.** Trying many models and reporting the best. Count the trials.
- **Target leakage through survivorship.** A universe that excludes delisted stocks makes a model look better than it is.
- **Overfitting hyperparameters.** Tuning on the final period, which turns it into a validation set.

## Further reading

- Gu, Kelly and Xiu (2020), "Empirical Asset Pricing via Machine Learning," *Review of Financial Studies*. A large comparison of machine-learning methods for return prediction.
- López de Prado (2018), *Advances in Financial Machine Learning* 💸. Labelling, sample weights and backtest overfitting.
- Bailey and López de Prado (2014), "The Deflated Sharpe Ratio," *Journal of Portfolio Management*.

See [papers](../resources/papers.md) for the full citations.
