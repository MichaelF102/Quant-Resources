# Performance metrics cheat sheet

*Last reviewed: Oct 2026*

Notation: P_t price at time t, r_t period return, r_f risk-free rate per period, r_b benchmark return, T number of periods, N periods per year (252 for daily trading data), w weights, MAR minimum acceptable return, θ threshold for the Omega ratio.

## 1. Returns

| Measure | Formula | Notes |
|---|---|---|
| Simple return | r_t = P_t / P_(t−1) − 1 | Additive across assets in a portfolio |
| Log return | ln(P_t / P_(t−1)) | Additive over time |
| Cumulative return | ∏(1 + r_t) − 1 | Compounding |
| Arithmetic mean | (1/T) Σ r_t | Annualise by multiplying by N |
| Geometric mean | (∏(1 + r_t))^(1/T) − 1 | Growth rate actually realised |
| CAGR | (final / initial)^(1/years) − 1 | Geometric annual growth |

Annualisation:

- Return: mean per period × N (arithmetic) or (1 + r̄)^N − 1 (compounded)
- Volatility: σ_period × √N
- Sharpe: under i.i.d. returns, the annual Sharpe equals the period Sharpe × √N, because the mean scales by N and the volatility by √N.

## 2. Risk-adjusted return

| Metric | Formula | Notes |
|---|---|---|
| Sharpe ratio | mean(r − r_f) / std(r − r_f) × √N | Annualise only if returns are approximately i.i.d. |
| Sortino ratio | mean(r − MAR) / DD × √N | DD = √(mean(min(r − MAR, 0)²)); penalises downside only |
| Calmar ratio | CAGR / \|max drawdown\| | Return per unit of worst loss |
| Information ratio | mean(r − r_b) / std(r − r_b) × √N | Active return per unit of tracking error |
| Omega ratio | E[max(r − θ, 0)] / E[max(θ − r, 0)] | Uses the whole distribution; no normality assumption |
| Treynor ratio | mean(r − r_f) / β | Excess return per unit of market risk |

### Alpha and beta

Regress excess returns on a benchmark: r_t − r_f = α + β(r_b,t − r_f) + ε_t.

- α per period × N gives annualised alpha. Check its t-statistic before reporting it.
- Tracking error = std(r − r_b) × √N.

### Sharpe ratio uncertainty

For an annualised Sharpe SR observed over T years, assuming i.i.d. normal returns, the standard error is approximately √((1 + SR²/2) / T). Short samples give very wide intervals; five years at SR = 1 gives a standard error of about 0.55.

### Probabilistic Sharpe ratio

With per-period Sharpe SR̂, sample length T, skewness γ₃ and kurtosis γ₄ (non-excess), the probability that the true Sharpe exceeds a benchmark SR* is

PSR(SR*) = Φ( (SR̂ − SR*)√(T − 1) / √(1 − γ₃ SR̂ + ((γ₄ − 1)/4) SR̂²) )

Negative skew or fat tails widen the denominator, so the same observed Sharpe carries less evidence.

### Deflated Sharpe ratio

When the best of N independent trials is selected, its expected maximum Sharpe under zero true skill is approximately

E[max SR] ≈ √V · [(1 − γ) Φ⁻¹(1 − 1/N) + γ Φ⁻¹(1 − 1/(Ne))]

where V is the variance of the Sharpe estimates across trials and γ ≈ 0.5772 is the Euler–Mascheroni constant. Under i.i.d. returns over T years, V ≈ 1/T for annual Sharpe.

Example: with N = 100 trials and T = 5 years, the expected maximum annual Sharpe under zero skill is about 1.13 from the formula (about 1.12 in simulation). Compare the selected strategy's Sharpe against this hurdle, not against zero.

Bailey and López de Prado (2014) develop the full deflated Sharpe ratio, which combines this hurdle with the probabilistic Sharpe ratio.

## 3. Drawdown

- Drawdown at time t: P_t / max(P_s, s ≤ t) − 1
- Maximum drawdown: the most negative drawdown over the sample.
- Duration: time from a peak to recovery. Report it alongside depth.
- Ulcer index: √(mean(DD_t²)), in percentage points. Penalises long, shallow drawdowns that a maximum drawdown ignores.

## 4. Tail risk

- Value at Risk at level α: VaR_α = −quantile_α(r). A 95% daily VaR uses the 5th percentile of returns.
- Expected Shortfall: ES_α = −E[r | r ≤ quantile_α(r)]. ES is coherent; VaR is not sub-additive in general.
- Tail ratio: |quantile_95%(r)| / |quantile_5%(r)|. Values below 1 indicate a heavier left tail.
- Skewness and kurtosis of returns: report alongside Sharpe, since both affect the reliability of VaR and the PSR.

Estimate VaR and ES with historical simulation, with a parametric fit, or with filtered historical simulation under GARCH. Compare the methods out of sample with a backtest such as Kupiec's proportion-of-failures test.

## 5. Signal evaluation

- Information coefficient (IC): correlation between the signal at t and the return from t to t + 1, usually rank-based (Spearman) and computed cross-sectionally each period.
- Mean IC and its t-statistic across periods: IC_mean × √(periods) / std(IC).
- Single cross-sectional IC with N assets: approximate t-statistic IC × √(N − 2) / √(1 − IC²).
- IC decay: average IC at horizons h = 1, 2, …. A signal that decays quickly needs faster rebalancing.
- Quantile spreads: average return of the top decile minus the bottom decile, with its own standard error.

## 6. Trading statistics

- Turnover per period: ½ Σ|w_t − w_(t−1)|. Multiply by per-unit cost for cost drag.
- Hit rate: share of profitable periods or trades.
- Profit factor: gross profit / gross loss.
- Expectancy per trade: p × avg win − (1 − p) × avg loss.
- Exposure: share of time invested. Report it next to returns, since low exposure flatters Sharpe.
- Capacity: the trade size at which market impact erodes the expected return.

### Transaction cost models

- Linear cost: c · |Δw|, with c in basis points.
- Square-root impact: cost ≈ c · σ · √(Q / ADV) · Q, where Q is the order size, ADV the average daily volume, and σ the daily volatility.

## 7. Position sizing

- Continuous Kelly fraction: f* = μ / σ², with μ the excess return and σ the volatility per period.
- Binary bet with win probability p and payoff b to 1: f* = p − (1 − p)/b.
- Full Kelly maximises long-run growth but is volatile. Most practitioners use a fraction of Kelly.

## 8. Uncertainty and resampling

- Block bootstrap: resample blocks of consecutive returns to keep autocorrelation. Choose the block length from the autocorrelation decay.
- Bootstrapped Sharpe confidence interval: report the 5th and 95th percentiles, not only the point estimate.
- Walk-forward results: report metrics per window, then the pooled out-of-sample series.

## 9. Common mistakes

- Annualising a daily Sharpe with the wrong factor, or annualising a monthly figure with √252.
- Comparing a Sharpe computed on excess returns with one computed on raw returns.
- Reporting Sharpe alone for a strategy with large drawdowns or negative skew.
- Calculating drawdown from average equity rather than the running peak.
- Ignoring transaction costs and turnover when comparing strategies.
- Selecting the best trial from many and reporting its Sharpe without a multiple-testing adjustment.
- Treating autocorrelated returns as i.i.d. when annualising. Positive autocorrelation inflates the √N-scaled Sharpe.

## 10. Interview favourites

- A strategy has annual Sharpe 2 and maximum drawdown 40%. What do you ask? Sample length, leverage, exposure, whether returns are net of costs, and whether the Sharpe was selected from many trials.
- Why can a daily Sharpe of 0.1 be a strong result? Annualised it is 0.1 × √252 ≈ 1.6.
- Why use Expected Shortfall over VaR? ES reflects the size of losses beyond the quantile, which VaR ignores.
- Two strategies have equal Sharpe. Which do you prefer? The one with less negative skew and a shallower drawdown, all else equal.
- What is the difference between Sharpe and Information ratio? Sharpe measures excess return against cash; the Information ratio measures active return against a benchmark per unit of tracking error.
