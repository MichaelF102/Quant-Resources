# Credit risk cheat sheet

*Last reviewed: Oct 2026*

Notation: PD probability of default over a horizon, LGD loss given default, R recovery rate (R = 1 − LGD), EAD exposure at default, EL expected loss, UL unexpected loss, λ constant hazard rate, V_t firm asset value, D face value of debt, σ asset volatility, μ asset drift, r risk-free rate, T horizon in years.

## 1. Core parameters

| Parameter | Definition | Typical source |
|---|---|---|
| PD | Probability the obligor defaults within the horizon (usually one year) | Ratings, scorecards, market-implied estimates |
| LGD | Fraction of exposure lost if default occurs | Historical recoveries, collateral, seniority |
| EAD | Amount owed at the time of default, including drawn and expected drawdowns on undrawn commitments | Exposure models, credit conversion factors |
| EL | PD × LGD × EAD | Pricing, provisioning |
| UL | Standard deviation of the loss distribution | Portfolio models, capital |

Expected loss is the average loss the institution should price in and provision for. Unexpected loss is the variability around that average, and it drives economic capital.

### Recovery and LGD

- R = 1 − LGD. Recovery is measured on a defined basis, such as market value of defaulted bonds 30 days after default, so check the definition before comparing LGDs.
- Seniority matters: senior secured debt usually recovers more than subordinated debt.
- LGD estimates are often cyclical. Downturn LGD is usually higher than average LGD and is what regulators require for capital.

### Expected and unexpected loss

For a single loan with independent PD, LGD and EAD (assuming a Bernoulli default event):

- EL = PD · LGD · EAD
- Var(Loss) ≈ EAD² · LGD² · PD(1 − PD) when LGD is fixed; the variance includes LGD variance if it is random.

For a portfolio, UL depends on default correlation. Correlation is the main driver of tail losses.

## 2. Hazard rates and survival

- Survival probability over t years with constant hazard λ: S(t) = e^(−λt)
- Cumulative default probability over t years: PD(t) = 1 − e^(−λt)
- Annual PD from a constant hazard: 1 − e^(−λ)

Example: λ = 2% per year gives a 5-year default probability of 1 − e^(−0.1) ≈ 9.5%.

### Credit spread approximation

For a bond with recovery R and hazard λ, the par credit spread is approximately

s ≈ λ(1 − R) = PD_annual × LGD

With λ = 2% and R = 40%, the approximate spread is 120 bp.

This approximation ignores discounting and the difference between the risk-free and risky annuity. It is accurate for small spreads and short maturities, and it gives a useful sanity check on a quoted spread.

## 3. CDS

A credit default swap pays the protection buyer (1 − R) × notional if the reference entity defaults. The buyer pays a periodic premium, the CDS spread.

- Par CDS spread: the premium that makes the swap value zero at inception.
- Upfront plus running structures: used when spreads are very wide or narrow, with a fixed running coupon (for example 100 bp or 500 bp) and an upfront payment.
- CDS-bond basis: difference between the CDS spread and the bond's credit spread. Its sign depends on funding, delivery options and supply.

## 4. Merton structural model

The firm's asset value follows geometric Brownian motion:

dV = μV dt + σV dW

Equity is a call option on the firm's assets with strike D (the face value of debt maturing at T):

E₀ = V₀ N(d₁) − D e^(−rT) N(d₂)

d₁ = [ln(V₀/D) + (r + σ²/2)T] / (σ√T), d₂ = d₁ − σ√T

Two probabilities follow:

- **Risk-neutral default probability:** N(−d₂)
- **Real-world default probability** (using drift μ): PD = N(−d₂^P), where d₂^P = [ln(V₀/D) + (μ − σ²/2)T] / (σ√T)

Distance to default is d₂^P. It measures how many standard deviations the firm's asset value is above the default barrier, under the real-world measure.

### Worked example

V₀ = 100, D = 70, T = 1, μ = 8%, σ = 25%: d₂^P ≈ 1.62 and PD = N(−1.62) ≈ 5.2%. A Monte Carlo simulation of terminal asset values gives 5.2% as well.

### Limitations

- Assumes a single debt maturity and continuous monitoring of the default barrier.
- Equity volatility and asset volatility are not observed directly; they must be inferred by solving the equity pricing equation and its delta relation.
- Real defaults often come from liquidity shortfalls before assets reach the barrier, so Merton PDs can understate short-horizon risk for firms with large short-term debt.
- Empirical spreads are usually wider than the model implies for short maturities.

## 5. Reduced-form models

Default is a jump governed by a hazard rate λ(t), typically estimated from CDS or bond spreads rather than from balance-sheet data. Advantages: fits observed spreads well, simple to calibrate. Disadvantage: the hazard rate is not linked to firm fundamentals.

## 6. Rating migration and transition matrices

A transition matrix P gives the probability of moving from one rating class to another in one year. Default is an absorbing state.

- Multi-year transition: P^n, assuming the Markov property.
- Real transition matrices show rating momentum and cyclicality. The Markov assumption is a simplification; duration effects and business-cycle conditioning are real.
- Use cohort analysis for historical estimates, and check that withdrawn ratings are handled consistently.

## 7. Portfolio credit risk

### Single-factor (Vasicek) model

Asset return for obligor i: X_i = √ρ · M + √(1 − ρ) · ε_i, where M is a systematic factor, ε_i idiosyncratic, and ρ the asset correlation. Obligor i defaults when X_i < Φ⁻¹(PD_i).

Conditional on M, default events are independent, so the portfolio loss distribution can be computed in closed form for large homogeneous portfolios. Its quantiles drive the Basel IRB capital formula.

### Copulas and correlation

Default correlation controls tail risk. Gaussian copulas understate joint extreme defaults; t-copulas and factor models with heavy tails are used in practice. Stress the correlation parameter, not only the PD.

### Credit VaR

Credit VaR at confidence α is the loss quantile above expected loss. Expected shortfall is often preferred for the same reasons as in market risk.

## 8. Common mistakes

- Treating PD as the probability of loss. Loss is PD × LGD × EAD in expectation.
- Using through-the-cycle PDs for stressed pricing, or point-in-time PDs for long-horizon capital.
- Ignoring EAD growth on revolving facilities: undrawn commitments often draw down before default.
- Setting LGD from average recoveries in a downturn scenario.
- Calibrating the hazard rate to a CDS spread without adjusting for the premium leg and the recovery convention.
- Comparing Merton PDs with rating-agency PDs as if they were the same measure.

## 9. Interview favourites

- A loan has PD 2%, LGD 45% and EAD 1,000,000. What is the expected loss? 2% × 45% × 1,000,000 = 9,000.
- Why does correlation matter more than PD for portfolio tail risk? Diversification of idiosyncratic default risk is limited when defaults cluster in recessions.
- In Merton, why does equity behave like a call? Shareholders have limited liability: they receive the residual value of assets above the debt.
- A bond has a 300 bp spread and recovery 40%. What is the approximate hazard rate? About 5% per year (s / (1 − R) = 0.03 / 0.6).
- Why can Merton understate short-term default risk? Liquidity-driven defaults can occur before asset value reaches the debt barrier.
