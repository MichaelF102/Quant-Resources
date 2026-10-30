# Alternative data and sentiment

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** days to weeks · **Repo project:** none yet; [Project 09](../projects/09-purged-cross-validation/) gives the evaluation discipline it needs

## Idea

Information that is not in prices or standard financial statements can predict returns: the tone of company filings and news, job postings, web traffic, satellite images, and similar data. Sentiment analysis measures the tone of text. Alternative-data strategies turn such sources into features and test whether they predict returns after controlling for the standard factors. The strategy's value depends on the signal being new, available on time, and not already in prices.

## Research question

Does a text-based sentiment measure built from exchange filings and news for NSE companies predict next-period abnormal returns, after controlling for momentum, size, value and the market, and does it do so with data that was available at the time?

## Method

1. **Collect the data.** Filings and news with their publication timestamps. Record when each item was available, not when it describes events.
2. **Measure tone.** A dictionary approach (counting positive and negative words from a finance-specific list) is simple and transparent. Machine-learning classifiers can be more accurate but harder to audit. State which one is used.
3. **Aggregate.** Compute a sentiment score per company per period, weighted for length and source.
4. **Test.** Regress next-period abnormal returns on the score, with the standard factors as controls. Use a portfolio sort as a second test.
5. **Out-of-sample check.** Fit the dictionary or classifier on an early period, and test on a later one.

Dictionary choice is a decision that can be overfit. Fix it before the test period, and report the alternatives tried.

## Data

- Exchange filings and company announcements, with timestamps.
- News articles with their publication times and sources.
- Price, volume and factor data from [data sources](../data/data-sources.md).
- Licence terms for any news or text database. Many are paid and restrict redistribution.

## Costs

- Data licences are often the largest cost, and they may be recurring.
- Trading costs as for any equity strategy, from [India trading costs](india-trading-costs.md).
- Processing costs, which matter for real-time signals.

## Evaluation

- Report the signal's correlation with the standard factors. A sentiment score that is mostly momentum is not new information.
- Report the abnormal return spread, gross and net, with its standard error.
- Report results by time of publication relative to the market. A signal that acts before the market adjusts has a different timing requirement from one that acts a day later.
- Report the deflated Sharpe ratio across dictionaries, classifiers and horizons tried.

## What would show it does not work

- The score adds nothing once momentum and size are controlled.
- The effect appears only when the text is used after the market has moved, so it cannot be traded.
- The result depends on a dictionary tuned on the test period.

## Common failure modes

- **Publication-time leakage.** Using a timestamp for when a news story was indexed by a vendor, rather than when it was published.
- **Revised text.** Filings amended later, with the amended version used in the backtest.
- **Overfitting the dictionary.** Choosing words that work on the sample.
- **Coverage bias.** News covers large companies well and small ones poorly, so a sentiment signal can be a size signal.

## Further reading

- Tetlock (2007), "Giving Content to Investor Sentiment: The Role of Media in the Stock Market," *Journal of Finance*.
- Loughran and McDonald (2011), "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks," *Journal of Finance*.
- Gu, Kelly and Xiu (2020), "Empirical Asset Pricing via Machine Learning," *Review of Financial Studies*, for the evaluation of many predictors together.
