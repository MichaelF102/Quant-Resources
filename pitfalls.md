# Pitfalls: why most backtests lie

*Read this before your first backtest, not after.*

A backtest is a hypothesis test with a very large number of hidden degrees of freedom. Almost every error below makes a strategy look **better** than it is, which is why they survive: nobody debugs good news.

---

## 1. Look-ahead bias

Using information that wasn't available at decision time.

- Trading at today's close on a signal computed from today's close.
- Using full-sample statistics (mean, std, min-max scaling) to normalise features.
- Fundamental data stamped with the **period end date** instead of the **release date** — quarterly results arrive weeks later.

**Fix:** shift signals by one bar; fit any scaler on training data only; use point-in-time data with release dates.

## 2. Survivorship bias

Testing only on assets that exist today. Companies that went bankrupt or were delisted are silently excluded, inflating returns — especially for value and small-cap strategies.

**Fix:** use historical index constituents as of each date, and a dataset that includes delisted securities.

## 3. Overfitting & multiple testing

Try enough parameter combinations and one will look brilliant by chance. If you test 100 independent strategies with no edge, about 5 will look significant at the 5% level.

**Fix:**
- Decide hypotheses and parameters **before** looking at results.
- Track how many variations you tried, and adjust (Bonferroni, or the **deflated Sharpe ratio** of Bailey & López de Prado).
- Prefer simple rules with economic justification over complex fits.
- Hold out a final test period you touch **once**.

## 4. Leaky cross-validation

Standard k-fold CV shuffles time-series data, so the model trains on the future to predict the past. Labels that span several days (e.g. 5-day forward returns) also overlap between train and test folds.

**Fix:** walk-forward validation, or purged k-fold with an embargo (López de Prado, *Advances in Financial Machine Learning*, ch. 7).

## 5. Ignoring transaction costs and capacity

A strategy that trades daily with 2 bps of edge is negative after costs. Include:

- Brokerage, STT, exchange charges, GST and stamp duty (India-specific — they add up, especially on options).
- Bid-ask spread and slippage, which grow with trade size.
- Market impact: what works on ₹1 lakh may not work on ₹10 crore.

**Fix:** report results with and without costs; show how performance degrades as costs double.

## 6. Data-snooping through the research process

Even with a clean holdout, if you keep revising your idea after seeing holdout results, the holdout becomes training data.

**Fix:** keep a research log of every test and result, including the failures.

## 7. Unrealistic execution assumptions

- Assuming you can short any stock (Indian cash equities restrict overnight shorting; use futures).
- Assuming fills at the close price for a market-on-close order in an illiquid name.
- Ignoring circuit limits that freeze trading.

## 8. Regime blindness

A strategy tested only from 2020–2024 has seen one rate cycle and one crash-and-recovery. Report performance by sub-period and in stress windows (2008, 2013 taper tantrum, March 2020).

---

## A minimal honest-backtest checklist

- [ ] Signals use only data available at decision time
- [ ] Universe includes delisted names / historical constituents
- [ ] Realistic costs, with sensitivity analysis
- [ ] Number of variations tried is recorded
- [ ] Out-of-sample period untouched until the end
- [ ] Results split by sub-period
- [ ] A plausible economic reason why the edge should exist

## Further reading

- Bailey, Borwein, López de Prado & Zhu, *Pseudo-Mathematics and Financial Charlatanism* (2014) 🆓 — short and pointed.
- Harvey, Liu & Zhu, *…and the Cross-Section of Expected Returns* (2016) — why t > 3 is the new bar for factor discovery.
