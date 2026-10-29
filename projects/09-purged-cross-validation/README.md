# 09 — Purged cross-validation for an ML signal

**Proves:** why standard k-fold cross-validation leaks information in financial data, purging and embargo, the effect of overlapping labels, and deflated performance metrics for model selection
**Level:** 🔴 · **Time:** 2–3 weekends
**Prerequisites:** [QR roadmap](../../roadmaps/quant-researcher.md) Phase 5; [Project 03](../03-honest-backtester/); [Performance metrics cheat sheet](../../cheatsheets/performance-metrics.md), multiple-testing section

## Goal

Build a machine-learning classifier that predicts the sign of the next five-day return for a panel of Indian stocks. Evaluate it first with ordinary k-fold cross-validation, then with purged and embargoed cross-validation. Show how much of the apparent accuracy comes from leakage, and report the performance that remains. The question: how much of an ML signal's apparent skill survives a valid evaluation?

## Data

A daily panel of 30–50 NIFTY 500 stocks from 2010 onward. Features: returns over 1, 5, 21 and 63 days; volatility over 21 days; volume relative to its 63-day average. All features use data up to the close of the day they are computed. Labels: the sign of the five-day forward return, with the day-zero close as the reference.

## Steps

1. **Build labels with an interval.** Each label covers the period from its start date to its end date (five trading days later). Store both dates with each observation.
2. **Baseline: ordinary k-fold.** Use five folds with shuffling. Report the mean accuracy and the area under the ROC curve. Keep this result; it is the number the purging should reduce.
3. **Time-ordered splits.** Use expanding-window splits, with the training set always before the test set. Report accuracy.
4. **Purged and embargoed splits.** For each test fold, remove from the training set any observation whose label interval overlaps the test period (purging). Then remove a further 1% of observations after the test period (embargo). Implement this as a splitter class that scikit-learn can use.
5. **Test the splitter.** Write a test that checks no training label interval overlaps any test label interval, and that the embargo is applied.
6. **Model selection.** Compare three models (logistic regression, a random forest, and gradient boosting), each with the same purged splits. Count the number of configurations tried.
7. **Deflate.** Report the deflated Sharpe ratio of the best model's long-short strategy, using the number of configurations as the number of trials.

## Done when

- [ ] Ordinary k-fold, expanding-window and purged-embargoed results are reported side by side
- [ ] The purged splitter passes a test that no training label overlaps any test label, and the embargo is applied
- [ ] The gap between ordinary k-fold and purged accuracy is reported and explained
- [ ] Every model and configuration tried is counted, and the deflated Sharpe ratio of the best one is reported
- [ ] Performance is reported for at least two periods that were not used for model selection
- [ ] The write-up states whether the signal has skill after purging, and how large the effect is after costs

## Common pitfalls

- **Overlapping labels.** A five-day label observed on consecutive days shares four days of return. Ordinary k-fold puts these in both training and test sets.
- **Feature leakage.** A feature computed over a window that extends into the test period leaks, even with purging. Check each feature's window.
- **Tuning on the test set.** Choosing a model because it performed well on the held-out fold is model selection on the test set. Keep a separate final period.
- **Accuracy as the only metric.** A classifier that predicts the majority class can be accurate on an imbalanced label. Report AUC and the strategy's return.
- **Forgetting costs.** A signal that flips every day can have high accuracy and negative net return.

## Stretch goals

- Replace the classifier with a sequence model (for example, an LSTM) on the same features and splits. Report whether it beats the simpler models after purging. Keep the same evaluation discipline; the model choice does not change the leakage rules.
- Use sample weights based on label uniqueness, as described in López de Prado's book, and test whether they change the result.
- Compare with a combinatorial purged cross-validation scheme, and report the spread of the results.

## Further reading

- López de Prado (2018), *Advances in Financial Machine Learning* 💸. Chapters on labelling, sample weights, purged cross-validation and backtest overfitting.
- Bailey, Borwein, López de Prado and Zhu (2014), "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance," *Notices of the AMS*.
- Bailey and López de Prado (2014), "The Deflated Sharpe Ratio," *Journal of Portfolio Management*.
