# Statistics and machine learning problems

Try each for at least 10 minutes before opening the solution. For the ML questions, name the assumption each answer depends on; a good answer states what would change it.

Difficulty: 🟢 warm-up · 🟡 standard · 🔴 hard

---

### 1. Estimating an exponential rate 🟢

Observations x₁, …, xₙ are independent draws from an exponential distribution with rate λ. Find the maximum likelihood estimate of λ.

<details><summary>Solution</summary>

The log-likelihood is ℓ(λ) = n ln λ − λ Σxᵢ. Setting the derivative to zero gives n/λ − Σxᵢ = 0.

The MLE is **λ̂ = 1 / x̄**, the reciprocal of the sample mean.

Follow-up: is it unbiased? No. E[1/x̄] is larger than 1/E[x̄] by Jensen's inequality, so λ̂ is biased upwards in small samples.
</details>

---

### 2. Base rates and a diagnostic test 🟢

A test has 99% sensitivity and 99% specificity. The condition affects 1 in 1,000 people. A randomly chosen person tests positive. What is the probability they have the condition?

<details><summary>Solution</summary>

Apply Bayes' rule:

P(condition | positive) = (0.99 × 0.001) / (0.99 × 0.001 + 0.01 × 0.999) = 0.00099 / 0.01098 ≈ **9%**

The base rate dominates. Most positives are false positives, because the healthy population is so large. The same reasoning applies to a signal that fires rarely in a trading strategy: the frequency of true events matters as much as the accuracy of the signal.
</details>

---

### 3. Bias and variance 🟡

Write the expected squared prediction error of an estimator f̂ at a point x, for data with noise variance σ², and explain each term.

<details><summary>Solution</summary>

E[(y − f̂(x))²] = (Bias[f̂(x)])² + Var[f̂(x)] + σ²

- **Bias²:** the squared difference between the average prediction and the true function. A simple model has high bias.
- **Variance:** how much the prediction changes across training samples. A flexible model has high variance.
- **σ²:** irreducible noise. No model removes it.

Model complexity usually trades bias for variance. Regularisation moves the balance towards lower variance, at the cost of some bias.
</details>

---

### 4. Ridge versus ordinary least squares 🟡

Why might ridge regression give better out-of-sample predictions than ordinary least squares, even though its estimates are biased?

<details><summary>Solution</summary>

Ridge adds a penalty λ‖β‖² and solves (XᵀX + λI)⁻¹Xᵀy.

OLS is unbiased, but its variance is large when predictors are correlated or when there are many of them. Ridge introduces bias by shrinking the coefficients towards zero, which reduces variance. If the variance reduction is larger than the squared bias, the mean squared error falls.

The choice of λ is made by cross-validation, and for time series it must respect time order (see Problem 6).
</details>

---

### 5. What a p-value is not 🟡

A regression coefficient has p = 0.03. Which statement is correct?

(a) There is a 97% chance the coefficient is non-zero.
(b) If the true coefficient were zero, data at least this extreme would occur about 3% of the time.
(c) The effect is 97% likely to replicate.

<details><summary>Solution</summary>

Only **(b)** is correct. A p-value is the probability of data at least this extreme under the null hypothesis. It is not the probability that the null is true, and it says nothing about replication or effect size.

Follow-up: with many variables tested, some will have small p-values by chance. This is the multiple-testing problem, and it is why a research result needs a stated number of trials.
</details>

---

### 6. Why k-fold cross-validation leaks in time series 🔴

Explain why ordinary k-fold cross-validation with shuffling overstates performance for a model that predicts next-day returns from the past 20 days of data.

<details><summary>Solution</summary>

Three sources of leakage:

1. **Shuffling mixes time.** A training observation can come after a test observation. The model learns from the future relative to the test point.
2. **Overlapping features.** A 20-day feature window for one day shares 19 days with the window for the next day. Training and test sets share information.
3. **Overlapping labels.** If the label is a multi-day return, consecutive labels overlap and can appear on both sides of the split.

The remedy is time-ordered splits, with an embargo and purging of observations whose labels overlap the test period. See [Project 09](../projects/09-purged-cross-validation/).
</details>

---

### 7. Why divide by n − 1 🟡

The sample variance is s² = Σ(xᵢ − x̄)²/(n − 1). Why not divide by n?

<details><summary>Solution</summary>

Dividing by n gives a biased estimate of σ². Because x̄ is estimated from the same data, the deviations from x̄ are on average smaller than the deviations from the true mean. Exactly one degree of freedom is used up by estimating the mean.

With E[Σ(xᵢ − x̄)²] = (n − 1)σ², dividing by n − 1 gives an unbiased estimate of σ².

The bias disappears as n grows, but dividing by n − 1 is the standard convention for that reason.
</details>

---

### 8. Multicollinearity 🟡

Two regressors have correlation 0.98. What happens to the coefficient estimates, and how would you detect the problem?

<details><summary>Solution</summary>

The coefficients are individually unstable: small changes in the data move them a lot, and their standard errors are large. Their sum is often well estimated, because the data constrain it, but the split between them is not.

Detection:

- **Variance inflation factor:** VIF_j = 1 / (1 − R_j²), where R_j² comes from regressing predictor j on the others. A VIF above about 10 is a common warning sign.
- **Condition number** of XᵀX, or the singular values of X (see the [linear algebra cheat sheet](../cheatsheets/linear-algebra.md)).

Remedies include dropping or combining predictors, PCA, or ridge regression.
</details>

---

### 9. Confidence intervals 🟢

A 95% confidence interval for a mean is computed as [1.2, 3.4]. A colleague says there is a 95% probability the true mean lies in this interval. Are they right?

<details><summary>Solution</summary>

No. The true mean is fixed, and the interval either contains it or does not. The 95% refers to the procedure: across repeated samples, about 95% of intervals constructed this way contain the true value.

A Bayesian credible interval has the probabilistic reading the colleague describes, but it requires a prior.
</details>

---

### 10. Welch's test 🟡

Two groups have sample variances 4 and 25, and sizes 50 and 10. Which two-sample t-test should you use, and why?

<details><summary>Solution</summary>

Use **Welch's t-test**, which does not assume equal variances. The pooled-variance test assumes equal variances, and with unequal variances and unequal sizes its size is wrong. The Welch test uses a separate variance for each group and an approximate degrees-of-freedom formula.

Here the smaller group has the larger variance, so a pooled test would understate the uncertainty in the difference.
</details>
