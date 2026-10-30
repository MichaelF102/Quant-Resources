# Regime switching

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** variable, set by the regime · **Repo project:** none yet; [Project 09](../projects/09-purged-cross-validation/) provides the validation discipline it needs

## Idea

Returns, volatility and correlations are not constant. They behave differently in bull markets, bear markets, quiet periods and turbulent ones. A regime-switching strategy identifies the current market state and changes its exposure or its choice of strategy to match. The model of regimes is usually latent: it is inferred from the data rather than observed directly, and it comes with a probability of being in each regime, not a certainty.

This is an overlay, not a standalone signal. It decides how much of the other strategies to hold, and when.

## Research question

Does a regime model estimated from NIFTY returns, volatility and breadth identify periods in which a momentum or a mean-reversion strategy performs differently, and does switching between them, using only regime probabilities available at the time, improve net risk-adjusted returns out of sample?

## Models

- **Markov-switching model.** A hidden state that follows a Markov chain, with a different mean and variance in each state. Hamilton (1989) introduced the approach for economic time series.
- **Hidden Markov model (HMM).** The same idea with more general emission distributions, fitted by the Baum–Welch algorithm or by maximum likelihood.
- **Gaussian mixture models and clustering.** Classify observations into groups by their features. Simpler, but without a time structure, so they ignore persistence.
- **Rule-based classifiers.** Thresholds on volatility, trend and breadth. Transparent and easy to test, and often as good as the models above out of sample.

Start with a rule-based classifier. A more complex model must beat it out of sample to justify its added complexity.

## Method

1. **Choose the features.** For example, realised volatility over 21 days, the return over 126 days, and the share of NIFTY 500 stocks above their 200-day average. Every feature must be computable at the decision date.
2. **Fit the regime model on a training period only.** Record the number of regimes chosen and the reason for the choice.
3. **Filter in real time.** For each decision date, compute the regime probabilities using only data up to that date. Filtering is not smoothing: smoothed probabilities use future data and are look-ahead.
4. **Map regimes to exposure.** For example, hold the momentum strategy when the probability of the trending regime exceeds a threshold, and reduce exposure otherwise. Set the thresholds in advance.
5. **Evaluate on later data**, rolling the training window forward.

## Data

- Daily index returns and volatility, from [data sources](../data/data-sources.md).
- Breadth measures from constituent-level data, with point-in-time membership.
- Returns of the strategies being switched between, from the same backtester and cost model.

## Costs

- Regime switches cause turnover when the strategy changes exposure. A model that flips often pays costs on every flip.
- Probability thresholds set the flip frequency. Report the number of switches per year.
- Costs of each underlying strategy still apply, from [India trading costs](india-trading-costs.md).

## Evaluation

- Compare the switching strategy with each component alone, and with a static blend, over the same dates and costs.
- Report the number of regime switches per year and the average duration of each regime.
- Report the accuracy of regime identification against a later, independent definition of the regimes, such as the drawdown periods. Use the independent definition only for checking, never for fitting.
- Report the deflated Sharpe ratio across models, feature sets and thresholds tried.

## What would show it does not work

- The switching strategy does not beat the best static component net of costs out of sample.
- The regimes are identified only after the market has already moved, so the switch comes too late.
- The result depends on the number of regimes or on the feature set chosen after looking at results.

## Common failure modes

- **Smoothed probabilities.** Using full-sample smoothed regime probabilities in a backtest is look-ahead, even though the model seems accurate.
- **Overfitting regimes.** With enough states, a model will fit any history. Two or three regimes is usually enough.
- **Label switching.** Hidden states have no inherent names. Naming a state "bull" after fitting, and then checking it against the same data, is circular.
- **Regime change in the sample.** A model fitted in one period may not describe the next one.

## Further reading

- Hamilton (1989), "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle," *Econometrica*.
- Ang and Bekaert (2002), "Regime Switches in Interest Rates," *Journal of Business and Economic Statistics*.
- Guidolin and Timmermann (2007), "Asset Allocation under Multivariate Regime Switching," *Journal of Economic Dynamics and Control*.
