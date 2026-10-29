# Distributions cheat sheet

*Last reviewed: Oct 2026*

Notation: μ mean, σ standard deviation, λ rate, ν degrees of freedom, k degrees of freedom or count, α shape, β rate, Φ and φ the standard normal CDF and PDF, Φ⁻¹ the standard normal quantile function.

## 1. Summary

| Distribution | Support | Mean | Variance | Skewness | Excess kurtosis | Typical use |
|---|---|---|---|---|---|---|
| Normal N(μ, σ²) | ℝ | μ | σ² | 0 | 0 | Shocks, errors, standardised returns |
| Lognormal | (0, ∞) | e^(μ + σ²/2) | (e^(σ²) − 1) e^(2μ + σ²) | (e^(σ²) + 2)√(e^(σ²) − 1) | e^(4σ²) + 2e^(3σ²) + 3e^(2σ²) − 6 | Asset prices under GBM |
| Student-t(ν) | ℝ | 0 (ν > 1) | ν / (ν − 2) (ν > 2) | 0 (ν > 3) | 6 / (ν − 4) (ν > 4) | Fat-tailed returns |
| Chi-square(k) | [0, ∞) | k | 2k | √(8/k) | 12 / k | Sample variance, likelihood-ratio tests |
| Gamma(α, β) | (0, ∞) | α/β | α/β² | 2/√α | 6/α | Waiting times, positive-valued models |
| Exponential(λ) | [0, ∞) | 1/λ | 1/λ² | 2 | 6 | Inter-arrival times of Poisson processes |
| Poisson(λ) | {0, 1, 2, …} | λ | λ | 1/√λ | 1/λ | Counts of jumps or order arrivals |
| Binomial(n, p) | {0, …, n} | np | np(1 − p) | (1 − 2p)/√(np(1 − p)) | (1 − 6p(1 − p))/(np(1 − p)) | Discrete up/down moves, tree models |

## 2. Normal

- Density: φ(x) = (1/(σ√(2π))) exp(−(x − μ)²/(2σ²))
- Standardise: Z = (X − μ)/σ, so P(X ≤ x) = Φ((x − μ)/σ)
- Sums of independent normals are normal, with means and variances adding
- Tail approximation for large z: P(Z > z) ≈ φ(z)/z

Quantiles of the standard normal:

| Level | One-sided | Two-sided |
|---|---|---|
| 90% | 1.2816 | 1.6449 |
| 95% | 1.6449 | 1.9600 |
| 99% | 2.3263 | 2.5758 |

## 3. Lognormal

- X = e^Y with Y ~ N(μ, σ²). Then ln X is normal, the median is e^μ, and the mode is e^(μ − σ²).
- Moments: E[Xⁿ] = exp(nμ + n²σ²/2) for any n.
- Quantiles: x_p = exp(μ + σ Φ⁻¹(p)).
- Always positive and right-skewed. The mean exceeds the median.
- Under GBM, S_T is lognormal, with ln(S_T / S₀) ~ N((μ − σ²/2)T, σ²T).

## 4. Student-t

- Standardised form: T = Z / √(χ²(ν)/ν) with Z independent of the chi-square term.
- Heavier tails than the normal. Tends to the normal as ν → ∞.
- Variance needs ν > 2. Kurtosis needs ν > 4.
- Common choice for return models. Estimate ν by maximum likelihood, and compare it with a normal fit using a likelihood-ratio or information criterion.
- Scaled t: a variable with unit variance is √((ν − 2)/ν) · T.

## 5. Chi-square and gamma

- χ²(k) is the sum of k squared independent standard normals. It is the special case Gamma(k/2, 1/2).
- Z² ~ χ²(1).
- Sample variance: (n − 1)s² / σ² ~ χ²(n − 1) under normality.
- Gamma(α, β) has density β^α x^(α−1) e^(−βx) / Γ(α). It is the sum of α independent exponentials with rate β when α is an integer.

## 6. Exponential and Poisson

- Poisson with rate λ per unit time: P(N = k) = e^(−λ) λᵏ / k!
- Inter-arrival times between Poisson events are exponential with mean 1/λ.
- Sum of n independent Exponential(λ) variables is Gamma(n, λ).
- Exponential is memoryless: P(T > s + t | T > s) = P(T > t).
- Poisson approximation of binomial: Binomial(n, p) ≈ Poisson(np) when n is large and p is small.

## 7. Binomial

- Number of successes in n independent trials with success probability p.
- Normal approximation for large n: N(np, np(1 − p)). Apply a continuity correction for small n.
- The Cox–Ross–Rubinstein tree uses this structure: each step is an up or down move with risk-neutral probability q = (e^(rΔt) − d)/(u − d).

## 8. Heavy tails and power laws

- Pareto(x_m, α): P(X > x) = (x_m / x)^α for x ≥ x_m. The mean exists for α > 1, and the variance for α > 2.
- Cauchy: no finite mean or variance. The sample mean does not converge.
- Tail index: a Pareto tail with index α has ES finite only when α > 1.
- Extreme events in equity returns are better described by Student-t or stable distributions than by the normal.

## 9. Multivariate normal

- X ~ N(μ, Σ) with density proportional to exp(−½(x − μ)ᵀΣ⁻¹(x − μ)).
- Simulation: write Σ = LLᵀ (Cholesky), then X = μ + LZ with Z standard normal.
- Conditional distribution: for partitioned X = (X₁, X₂), X₁ | X₂ is normal with mean μ₁ + Σ₁₂Σ₂₂⁻¹(x₂ − μ₂) and covariance Σ₁₁ − Σ₁₂Σ₂₂⁻¹Σ₂₁.
- Sample correlation has standard error approximately (1 − ρ²)/√n for normal data.

## 10. Simulation methods

- Inverse transform: if U ~ Uniform(0, 1), then F⁻¹(U) has distribution F.
- Box–Muller: with U₁, U₂ independent uniforms, Z₁ = √(−2 ln U₁) cos(2πU₂) and Z₂ = √(−2 ln U₁) sin(2πU₂) are independent standard normals.
- Antithetic variates: pair each Z with −Z, which reduces variance for monotone payoffs. See [Project 01](../projects/01-monte-carlo-pricer/).

## 11. Common mistakes

- Treating log-returns as normal when prices are lognormal, and the reverse.
- Assuming finite variance for Student-t with ν ≤ 2, or finite mean for Pareto with α ≤ 1.
- Using the normal approximation for a Poisson with small λ.
- Confusing the rate λ of the exponential with its mean (the mean is 1/λ).
- Estimating tail probabilities from a normal fit when the data are heavy-tailed.

## 12. Interview favourites

- Why does the lognormal have mean e^(μ + σ²/2) and not e^μ? Jensen's inequality, and E[e^Y] for normal Y.
- A stock is lognormal. What is the distribution of its log-return over T years? Normal, with mean (μ − σ²/2)T and variance σ²T.
- Why are Student-t tails important for risk models? They put more probability on extreme moves than a normal with the same variance.
- What is the distribution of the sum of two independent Poisson variables? Poisson with the sum of the rates.
- Why does the sample mean of Cauchy draws not settle down? The distribution has no finite mean, so the law of large numbers does not apply.
