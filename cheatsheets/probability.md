# Probability cheat sheet

*Last reviewed: Oct 2026*

Notation: P probability, E expectation, Var variance, Cov covariance, X, Y random variables, 1_A indicator of event A, n number of trials, p success probability.

Use this sheet for identities and standard results. For worked problems, see the [probability set](../interview/probability.md).

## 1. Basic rules

- P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
- P(A | B) = P(A ∩ B) / P(B), when P(B) > 0
- Independence: P(A ∩ B) = P(A)P(B). Independent events are not the same as mutually exclusive events; disjoint events with positive probability are dependent.
- Complement: P(Aᶜ) = 1 − P(A)

## 2. Bayes' rule and base rates

P(A | B) = P(B | A) P(A) / P(B), with P(B) = P(B | A) P(A) + P(B | Aᶜ) P(Aᶜ)

Worked example: a test with 99% sensitivity and 99% specificity, for a condition with prevalence 1 in 1,000.

- P(positive) = 0.99 × 0.001 + 0.01 × 0.999 = 0.01098
- P(condition | positive) = 0.00099 / 0.01098 ≈ 9.0%

The low prevalence, not the test accuracy, dominates the result.

## 3. Expectation and variance

- Linearity: E[aX + bY] = aE[X] + bE[Y], with no independence required.
- Variance: Var(X) = E[X²] − (E[X])²
- Variance of a sum: Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y)
- Tower property (law of total expectation): E[X] = E[E[X | Y]]
- Law of total variance: Var(X) = E[Var(X | Y)] + Var(E[X | Y])
- Indicator trick: for an event A, E[1_A] = P(A). Counting expected events with indicators avoids dependence arguments.

## 4. Common discrete distributions

| Distribution | pmf | Mean | Variance |
|---|---|---|---|
| Bernoulli(p) | p^x (1 − p)^(1 − x), x ∈ {0, 1} | p | p(1 − p) |
| Binomial(n, p) | C(n, k) p^k (1 − p)^(n − k) | np | np(1 − p) |
| Geometric(p) (trials to first success) | (1 − p)^(k − 1) p, k ≥ 1 | 1/p | (1 − p)/p² |
| Poisson(λ) | e^(−λ) λ^k / k! | λ | λ |

Memorylessness: only the geometric and the exponential distributions have it.

## 5. Common continuous distributions

| Distribution | Mean | Variance | Note |
|---|---|---|---|
| Uniform(a, b) | (a + b)/2 | (b − a)²/12 | Density 1/(b − a) |
| Normal(μ, σ²) | μ | σ² | Sum of independent normals is normal |
| Exponential(λ) | 1/λ | 1/λ² | Memoryless |

## 6. Expectations of extremes

For n independent Uniform(0, 1) variables, the maximum has E[max] = n/(n + 1) and the minimum has E[min] = 1/(n + 1).

For two fair dice, E[max] = 161/36 ≈ 4.47, and E[min] = 91/36 ≈ 2.53.

## 7. Waiting times and runs

- Expected trials until the first success: 1/p (geometric).
- Expected trials until a specific pattern appears: depends on overlaps. A pattern that overlaps itself takes longer. HH takes 6 flips on average, HT takes 4. Use the conditioning method: write an equation for the expected remaining time from each state.
- Expected number of successes in n trials: np, whatever the dependence between trials.

## 8. Random walks and gambler's ruin

- Symmetric simple random walk starting at k, with absorbing barriers at 0 and N: P(reach N before 0) = k/N.
- Asymmetric walk with up-probability p ≠ 1/2, with r = (1 − p)/p: P(reach N before 0) = (1 − r^k) / (1 − r^N).
- A symmetric walk returns to its start with probability 1 in one dimension, but the expected time to return is infinite.

## 9. Conditioning and information

- Conditioning on less information gives a different answer from conditioning on more. "At least one child is a boy" and "the older child is a boy" give different probabilities of two boys (1/3 and 1/2).
- Always write down the sample space that the condition defines.

## 10. Inequalities

- Markov: P(X ≥ a) ≤ E[X] / a for X ≥ 0
- Chebyshev: P(|X − μ| ≥ kσ) ≤ 1 / k²
- Jensen: for convex f, f(E[X]) ≤ E[f(X)]. For example, E[e^Y] ≥ e^(E[Y]).

## 11. Limit results

- Law of large numbers: the sample mean converges to E[X] when E[|X|] is finite.
- Central limit theorem: √n (X̄ − μ) / σ converges in distribution to N(0, 1), when Var(X) is finite.
- Heavy tails break both: if E[|X|] is infinite, the sample mean does not converge (the Cauchy distribution).

## 12. Quick results

- Birthday problem: with n people, P(all birthdays distinct) ≈ exp(−n(n − 1)/(2 · 365)). The probability of a shared birthday exceeds 50% at 23 people.
- Probability that the maximum of two independent Poisson variables is at most k: product of their CDFs.
- Expected number of fixed points of a random permutation of n items: 1, for any n.

## 13. Common mistakes

- Multiplying probabilities of dependent events as if they were independent.
- Confusing P(A | B) with P(B | A).
- Taking the expectation of a ratio as the ratio of expectations.
- Assuming a sample average converges when the variance is infinite.
- Treating "at least one" conditions as if they were "a specific one".
