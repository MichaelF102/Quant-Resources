# 13 — PCA on NSE stocks

**Proves:** eigendecomposition of a covariance matrix, the market and sector structure of stock returns, the difference between a principal component and an economic factor, and how the answer depends on the estimation window
**Level:** 🟢 · **Time:** 1 weekend
**Prerequisites:** [QR roadmap](../../roadmaps/quant-researcher.md) Phase 2; [Linear algebra cheat sheet](../../cheatsheets/linear-algebra.md)

## Goal

Run principal component analysis on the daily returns of NIFTY 50 stocks, and interpret the first components. The question: how much of the common variation in Indian stock returns is explained by one market factor, and do the next components correspond to sectors, to size, or to nothing you can name?

## Data

Daily adjusted returns for the NIFTY 50 constituents, over two years, from the sources in [data sources](../../data/data-sources.md). Drop any stock with a missing day in the window, and record how many were dropped.

## Steps

1. **Prepare the matrix.** Compute daily log returns. Standardise each stock to zero mean and unit variance. Record the matrix dimensions.
2. **Eigendecomposition.** Compute the correlation matrix and its eigenvalues and eigenvectors. Check that the eigenvalues sum to the number of stocks.
3. **Scree plot.** Plot the proportion of variance explained by each component. Report the number needed for 50% and 80%.
4. **Interpret the first component.** Check whether its loadings are all the same sign (a market factor). Report the correlation of its score with the NIFTY index return.
5. **Interpret the next components.** Sort the loadings for components 2 and 3, and compare the top and bottom stocks with their sectors. Report which components look like sectors and which do not.
6. **Stability.** Repeat the analysis on two non-overlapping one-year windows. Report how the loadings of the first three components change, using the absolute correlation between eigenvectors.
7. **Compare with a named factor.** Regress the first component's score on the market return and a size proxy. Report the fit.

## Done when

- [ ] The eigenvalues are shown to sum to the number of stocks, as a check on the computation
- [ ] The scree plot is shown, with the number of components needed for 50% and 80% of variance
- [ ] The first component is tested for a common sign and correlated with the index return
- [ ] Components 2 and 3 are interpreted against sector membership, with a table of loadings
- [ ] Stability across two windows is reported for the first three components
- [ ] The write-up distinguishes statistical components from economic factors, and states which component you can name

## Common pitfalls

- **Eigenvector signs.** An eigenvector is defined only up to sign. Do not interpret the sign of a component without checking that it is consistent.
- **Reading noise as structure.** Components beyond the first few can be sampling noise. Compare the eigenvalues with a random-matrix benchmark before interpreting them.
- **Using prices instead of returns.** Price levels are trending, so the first component will mostly reflect the trend, not co-movement.
- **Survivorship in the index.** The NIFTY 50 membership changes. Using today's constituents over an older window includes stocks that were not members then.

## Stretch goals

- Compare PCA with the Ledoit–Wolf covariance from [Project 06](../06-covariance-shootout/), and report which one gives more stable components.
- Run the analysis on a larger universe (NIFTY 500) and check whether the sector structure becomes clearer.
- Build a statistical factor portfolio from the top components, and test whether it hedges the market exposure of a stock portfolio.

## Further reading

- Jolliffe, *Principal Component Analysis* 💸. The standard reference on the method and on choosing the number of components.
- Laloux, Cizeau, Bouchaud and Potters (1999), "Noise Dressing of Financial Correlation Matrices," *Physical Review Letters*. How random-matrix theory separates signal from noise in stock correlations.
- Grinold and Kahn, *Active Portfolio Management* 💸, the chapter on risk models.
