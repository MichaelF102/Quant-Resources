# 08 — Factor model for Indian equities

**Proves:** cross-sectional regression, factor construction from prices and fundamentals, the Fama–French approach applied outside the US, the point-in-time problem in fundamental data, and the difference between a factor's premium and its exposure
**Level:** 🔴 · **Time:** 3–4 weekends
**Prerequisites:** [QR roadmap](../../roadmaps/quant-researcher.md) Phases 3 and 5; [Project 04](../04-momentum-mean-reversion-study/); [Data sources](../../data/data-sources.md), including the fundamentals checklist

## Goal

Build a small set of factors for Indian equities: at least value, size and momentum, using prices and, where you can source them, as-reported accounting data. Estimate each stock's exposures by cross-sectional regression, and test whether the factor premia are significant over time and robust to the choice of universe. The question: which factors earn a premium in India over the period you can test, and how much of that premium comes from the data rather than the economics?

## Data

- **Prices:** adjusted daily prices, from 2005 onward, as in Project 04.
- **Fundamentals:** book value, earnings, and market capitalisation, as they were reported on each filing date. This is the hard part. Use a source that keeps point-in-time records, or record the filing date for each value yourself. A later restatement must not appear before its release date.
- **Universe:** NIFTY 500 members, point-in-time where you can get it.

Record the source, the date of each download, and every adjustment, as described in [Version control and CI](../../tools-and-technologies/version-control-and-ci.md).

## Steps

1. **Build the data set.** One row per stock per month: returns, market cap, book-to-price, earnings-to-price, and the filing date of each fundamental. Lag every fundamental to its filing date.
2. **Define the factors.** Size: log market cap (short minus long). Value: book-to-price (high minus low). Momentum: 12-1 month return, as in Project 04. Write the definitions down before testing.
3. **Form portfolios.** Each month, sort stocks into terciles or quintiles on each factor, and compute the long-short return.
4. **Cross-sectional regression.** Each month, regress the stocks' returns on their factor exposures (Fama–MacBeth). Average the coefficients over time, and compute Newey–West standard errors for the averages.
5. **Test robustness.** Repeat with a different universe cut (for example, dropping the smallest 20% by market cap), and with a different sample period. Report which conclusions change.
6. **Report exposures.** Show the average exposure of your portfolio to each factor, so a reader can separate a factor premium from exposure to a market-wide effect.

## Done when

- [ ] Each fundamental is lagged to its filing date, and the lag is checked in code with a test
- [ ] Factor definitions are fixed before the premium is estimated, and listed in the README
- [ ] Fama–MacBeth coefficients are reported with Newey–West standard errors
- [ ] Results are shown for at least two universes and two sample periods
- [ ] The number of factors and variants tested is reported, with a multiple-testing caveat
- [ ] The write-up says which premia survive robustness checks, and which depend on a data choice

## Common pitfalls

- **Look-ahead in fundamentals.** Annual results are published months after the fiscal year-end. Using them in the same month is look-ahead.
- **Survivorship bias.** A universe of current index members excludes firms that failed. This flatters value and size premia.
- **Confusing a factor with a sector bet.** Value in India can load heavily on a few sectors. Report sector exposures.
- **Restated data.** Financial statements are often restated. Use the originally reported figures where you can.
- **Micro-cap noise.** A few very small stocks can drive a size premium. Test with a minimum market-cap cut.

## Stretch goals

- Add a quality factor, such as profitability, and test whether it adds to value.
- Compare a factor model built from prices alone with one that uses fundamentals, and report what the fundamentals add.
- Estimate the factor covariance matrix and use it in the covariance comparison of Project 06.

## Further reading

- Fama and French (1993), "Common Risk Factors in the Returns on Stocks and Bonds," *Journal of Financial Economics*. The three-factor model.
- Fama and MacBeth (1973), "Risk, Return, and Equilibrium: Empirical Tests," *Journal of Political Economy*. The cross-sectional regression method.
- Kenneth French's data library, linked in [Data sources](../../data/data-sources.md). Use it to check your US implementation before running the Indian one.
