# Lead–lag across related markets

*Last reviewed: Oct 2026*

**Difficulty:** advanced · **Holding period:** seconds to days, depending on the pair · **Repo project:** none yet

## Idea

Some related instruments react to news at different speeds. A futures contract may move before the cash market, a large stock may move before its smaller peers, a foreign listing may move before the local one, or an index may lead a basket of its members. If one series predicts the next move of another, a trader can position in the lagging instrument. Lead–lag strategies are a family of relationships, and each one must be tested separately, because the lags shrink quickly as markets become more efficient.

## Research question

Does the return of one instrument, such as a futures contract, a large stock or a foreign listing, predict the next-period return of a related instrument in the Indian market, after controlling for the common market factor, and does the predicted move exceed the cost of trading it?

## Signal

1. **Choose the pairs in advance**, on economic grounds. Examples: index futures and index constituents; large stocks and their smaller sector peers; an ADR or a foreign listing and the local share.
2. **Estimate the cross-autocorrelation.** Regress the lagging instrument's return on the leading instrument's return at the chosen lag, after removing the market return.
3. **Test several lags**, from one interval to one day, and report all of them.
4. **Trade** when the leading instrument's recent move exceeds a threshold, in the direction of the move, in the lagging instrument, and exit after the stated horizon.

The lag and threshold are fixed before testing. The number of pairs and lags tested must be reported, since with many pairs some will show a lead–lag by chance.

## Data

- Synchronised prices for the pair, at a frequency that resolves the lag. Daily data may miss lags of minutes.
- Trading hours for each market. A foreign listing and a local share may not overlap in time, so the lag is partly an artefact of closing times.
- Market index returns for controlling the common factor.
- Corporate actions and holiday calendars for both markets.

## Costs

- The cost of trading the lagging instrument, which is the target of the trade. For small stocks, the spread can exceed the predicted move.
- Futures and ETF costs when one leg is a derivative.
- Latency: lead–lag edges shrink quickly, so a trade that acts after a delay may capture none of the lag.

## Evaluation

- Report the cross-autocorrelation at each lag, with its standard error, and the number of pairs and lags tested.
- Report the net return of the rule after costs, per trade and as a portfolio.
- Report the lag's stability over time. A lead–lag that disappears in later years is a sign of arbitrage that has been competed away.
- Report the deflated Sharpe ratio across pairs, lags and thresholds tried.

## What would show it does not work

- The cross-autocorrelation is not significant once the market factor is removed.
- The lag is shorter than the time needed to trade.
- The predicted move is smaller than the cost of crossing the spread on the lagging instrument.

## Common failure modes

- **Non-synchronous closes.** A lag created by different trading hours is not a trading opportunity.
- **Thin instruments.** A lagging instrument that cannot be traded at the modelled size.
- **Common news.** Both instruments react to the same news at the same time, so the apparent lead is a common-factor effect.
- **Data alignment.** Timestamps in different time zones or with different conventions create false leads.

## Further reading

- Lo and MacKinlay (1990), "When Are Contrarian Profits Due to Stock Market Overreaction?," *Review of Financial Studies*.
- Hou (2007), "Industry Information Diffusion and the Lead-Lag Effect in Stock Returns," *Review of Financial Studies*.
- Harris, *Trading and Exchanges* 💸, on how information reaches different markets.
