# Time series cheat sheet

*Last reviewed: Oct 2026*

Notation: X_t series, μ mean, ε_t white noise with variance σ², L lag operator (L X_t = X_(t−1)), γ_k autocovariance at lag k, ρ_k autocorrelation at lag k, n sample size, h forecast horizon.

## 1. Stationarity

Weak (covariance) stationarity: constant mean, constant variance, and autocovariance γ_k that depends only on the lag k.

- White noise: mean zero, constant variance, zero autocorrelation at all nonzero lags.
- Random walk: X_t = X_(t−1) + ε_t. Not stationary; variance grows linearly in t.
- Differencing: ΔX_t = X_t − X_(t−1). Prices are usually integrated of order one (I(1)); their returns are typically stationary.
- Trend-stationary: stationary around a deterministic trend. Differencing over-differences such a series.

## 2. Autocorrelation

Sample autocorrelation at lag k:

ρ̂_k = Σ_(t=k+1)ⁿ (X_t − X̄)(X_(t−k) − X̄) / Σ_(t=1)ⁿ (X_t − X̄)²

- Standard error under white noise: approximately 1/√n. Bands at ±1.96/√n mark individual significance at 5%.
- Partial autocorrelation at lag k is the correlation between X_t and X_(t−k) after removing the effect of intermediate lags. Estimate it with the Durbin–Levinson recursion.

## 3. AR, MA and ARMA

| Model | Equation | Stationarity or invertibility | Key moments |
|---|---|---|---|
| AR(1) | X_t = c + φX_(t−1) + ε_t | \|φ\| < 1 | Mean c/(1 − φ); variance σ²/(1 − φ²); ρ_k = φ^k |
| AR(p) | X_t = c + Σφ_i X_(t−i) + ε_t | Roots of 1 − Σφ_i z^i outside unit circle | Yule–Walker equations for γ_k |
| MA(1) | X_t = μ + ε_t + θε_(t−1) | Always stationary | ρ₁ = θ / (1 + θ²); ρ_k = 0 for k ≥ 2 |
| MA(q) | X_t = μ + Σθ_i ε_(t−i) with θ₀ = 1 | Always stationary | ACF cuts off after lag q |
| ARMA(p, q) | AR(p) and MA(q) combined | Stationarity from the AR roots; invertibility from the MA roots | ACF and PACF both tail off |

Half-life of an AR(1) shock: −ln 2 / ln φ for 0 < φ < 1.

### AR(1) forecasts

- Conditional mean: E[X_(t+h) | X_t] = μ + φ^h (X_t − μ)
- Conditional variance: σ²(1 − φ^(2h)) / (1 − φ²)
- As h grows, the forecast reverts to μ and the variance converges to the unconditional variance.

### Yule–Walker equations for AR(p)

γ_k = Σ_(i=1)^p φ_i γ_(k−i), for k ≥ 1

Solve the first p equations for the coefficients given sample autocovariances. This gives a method-of-moments estimator.

## 4. Model identification and fitting

Box–Jenkins procedure:

1. Check stationarity. Difference if needed.
2. Inspect the ACF and PACF to suggest p and q.
3. Estimate by maximum likelihood.
4. Check residuals: they should look like white noise (Ljung–Box test, no pattern in the ACF).
5. Compare candidate models out of sample.

Selection criteria: AIC and BIC penalise complexity. Use them to rank candidates, but confirm the choice on out-of-sample forecast error.

ARIMA(p, d, q) applies ARMA(p, q) to the d-th difference. Seasonal ARIMA is written SARIMA(p, d, q)(P, D, Q)_s, with seasonal period s.

### Forecast evaluation

- MAE and RMSE for accuracy in the same units as the series.
- Diebold–Mariano test to compare the predictive accuracy of two models.
- Always evaluate on data not used for fitting, and in a rolling or expanding window if the series is non-stationary.

## 5. Unit-root and stationarity tests

- Dickey–Fuller regression: Δy_t = a + γ y_(t−1) + ε_t. Null hypothesis: γ = 0 (unit root). The test statistic uses non-standard critical values.
- Augmented Dickey–Fuller (ADF): adds lagged differences to the regression to remove autocorrelation in ε_t. Choose the lag order by information criterion.
- KPSS: null hypothesis is stationarity. Using it alongside ADF gives a cross-check; the two can disagree when the tests have low power.
- Ljung–Box: Q(m) = n(n + 2) Σ_(k=1)^m ρ̂_k² / (n − k), approximately χ²(m) under no autocorrelation.
- Engle's ARCH-LM test: tests for autocorrelation in squared residuals.

Rejecting a unit root with ADF is evidence for stationarity, but it has low power against near-unit-root alternatives. A sample of a few hundred observations can fail to distinguish a random walk from a slowly mean-reverting series.

## 6. Cointegration

- Two series are cointegrated if a linear combination of them is stationary while each is I(1).
- Engle–Granger: regress one series on the other, then test the residuals with ADF. Use the Engle–Granger critical values, which are more negative than the ordinary ADF values.
- Johansen: a multivariate test that estimates the number of cointegrating relations (the rank of Π in the VECM) and the cointegrating vectors.
- Error correction model: Δy_t = α β′y_(t−1) + Σ Γ_i Δy_(t−i) + ε_t. Here β contains the cointegrating vectors and α the speed of adjustment.

Pair trading uses the spread β′y_t as the stationary series to trade; see [Project 05](../projects/README.md).

## 7. Volatility models

Returns: r_t = σ_t z_t, with z_t i.i.d., mean zero and variance one.

### ARCH(1)

σ²_t = ω + α r²_(t−1). Stationary requires α < 1; unconditional variance ω / (1 − α).

### GARCH(1, 1)

σ²_t = ω + α r²_(t−1) + β σ²_(t−1)

- Stationary when α + β < 1. Unconditional variance: ω / (1 − α − β).
- Persistence is α + β. Values near 1 mean slow decay of volatility shocks.
- h-step variance forecast: E[σ²_(t+h)] = V_L + (α + β)^(h−1) (σ²_(t+1) − V_L), with V_L the unconditional variance.
- Fit by maximum likelihood, usually with Student-t innovations for fat tails.
- Leverage effects: GJR-GARCH and EGARCH allow negative shocks to raise volatility more than positive ones, which fits equity returns better.

## 8. State space models and the Kalman filter

State space form:

- State: x_t = A x_(t−1) + w_t, w_t ~ N(0, Q)
- Observation: y_t = C x_t + v_t, v_t ~ N(0, R)

Kalman filter recursions:

- Predict: x̂_(t|t−1) = A x̂_(t−1|t−1), P_(t|t−1) = A P_(t−1|t−1) Aᵀ + Q
- Update: K_t = P_(t|t−1) Cᵀ (C P_(t|t−1) Cᵀ + R)⁻¹, then x̂_(t|t) = x̂_(t|t−1) + K_t (y_t − C x̂_(t|t−1))

Use: a time-varying hedge ratio for pairs, where the state is the hedge coefficient and the observation is the price of one leg.

## 9. Other tools

- Hurst exponent H: E[R/S] grows as n^H. H = 0.5 for a random walk, H > 0.5 for persistence (trending), H < 0.5 for mean reversion. Estimate with caution on short samples.
- Regime-switching (Markov) models: switch between parameter sets with a hidden Markov chain. Useful for volatility regimes.
- Vector autoregression (VAR): models several series jointly. Use it as a base for cointegration analysis with the VECM.

## 10. Common mistakes

- Regressing one non-stationary series on another: spurious regression can show a high R² and significant coefficients.
- Fitting ARMA on prices instead of returns, which produces a unit root.
- Testing for cointegration on the full sample when the spread is used out of sample.
- Choosing ARMA orders by in-sample fit alone, which overfits.
- Reading a large Ljung–Box p-value as proof of independence. It only fails to reject autocorrelation at the tested lags.
- Using ADF critical values for Engle–Granger residuals.
- Overlooking seasonality and structural breaks, which can make a unit-root test misleading.

## 11. Interview favourites

- What is the stationarity condition for AR(1)? |φ| < 1.
- A price series has a unit root. What do you model instead? Its returns, or its log-returns.
- What does α + β close to 1 mean in GARCH(1, 1)? Volatility shocks persist for a long time.
- Why can two random walks look correlated? They can share trends, so the sample correlation of levels is misleading. Test for cointegration, or work with returns.
- Two cointegrated series drift apart for a long period. Does that break the relationship? Not necessarily. Cointegration says the spread reverts eventually; its half-life may be long.
- What is the autocorrelation at lag 2 of an MA(1)? Zero.
