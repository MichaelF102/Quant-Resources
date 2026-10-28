# Probability & expectation problems

Try each for at least 10 minutes before opening the solution. Say your reasoning out loud — that's what interviewers grade.

Difficulty: 🟢 warm-up · 🟡 standard · 🔴 hard

---

### 1. Expected rolls for a six 🟢

How many times do you expect to roll a fair die until you get a 6?

<details><summary>Solution</summary>

Geometric with p = 1/6, so E = 1/p = **6**.

Via conditioning: E = 1 + (5/6)E ⇒ E = 6. The conditioning approach generalises to harder problems, so practise it.
</details>

---

### 2. Two children 🟢

A family has two children and at least one is a boy. What's the probability both are boys?

<details><summary>Solution</summary>

Sample space given at least one boy: {BB, BG, GB}. Answer **1/3**.

Contrast: if you're told "the older child is a boy", the answer is 1/2. The point is precisely what information you're conditioning on.
</details>

---

### 3. Consecutive heads 🟡

What's the expected number of fair coin flips to get two heads in a row?

<details><summary>Solution</summary>

Let E₀ = expected flips from scratch, E₁ = expected flips having just seen one H.

- E₀ = 1 + ½E₁ + ½E₀
- E₁ = 1 + ½·0 + ½E₀

Solving: E₁ = 1 + ½E₀ and E₀ = 2 + E₁ ⇒ E₀ = 3 + ½E₀ ⇒ **E₀ = 6**.

Follow-up they often ask: HT takes only 4 on average. Why? After a failed HH attempt you lose progress; after a failed HT attempt (flipping H again) you don't.
</details>

---

### 4. Broken stick 🟡

A stick is broken at two uniformly random points. What's the probability the three pieces form a triangle?

<details><summary>Solution</summary>

Pieces form a triangle iff every piece is shorter than ½. On the unit square of break points, the valid region is 1/4 of the area. Answer **1/4**.
</details>

---

### 5. Coupon collector 🟡

How many die rolls on average until you've seen all six faces?

<details><summary>Solution</summary>

After seeing k distinct faces, the wait for a new one is geometric with p = (6−k)/6.

E = 6/6 + 6/5 + 6/4 + 6/3 + 6/2 + 6/1 = 6 · H₆ = 6 × 2.45 = **14.7**.
</details>

---

### 6. Fixed points in a permutation 🟡

n people throw their hats in a pile and each picks one at random. Expected number who get their own hat?

<details><summary>Solution</summary>

Indicator Iᵢ = 1 if person i gets their own hat; E[Iᵢ] = 1/n. By linearity of expectation, E = n · 1/n = **1**, for any n.

Linearity doesn't need independence — that's the key insight interviewers want.
</details>

---

### 7. Bayes and a medical test 🟡

A disease affects 1% of people. A test is 99% sensitive and 95% specific. You test positive. Probability you have the disease?

<details><summary>Solution</summary>

P(D|+) = (0.99 × 0.01) / (0.99 × 0.01 + 0.05 × 0.99) = 0.0099 / 0.0594 ≈ **16.7%**.

Base rates dominate. The same logic applies to a backtest "passing" a significance test when true signals are rare.
</details>

---

### 8. Dice game with re-roll 🟡

You roll a die and win its face value in rupees. You may re-roll once and must take the second result. What's the optimal strategy and expected value?

<details><summary>Solution</summary>

A re-roll is worth 3.5. Keep 4, 5, 6; re-roll 1, 2, 3.

EV = (3/6)(5) + (3/6)(3.5) = 2.5 + 1.75 = **₹4.25**.

Follow-up: with two re-rolls, the threshold for the first roll rises — keep only 5 or 6 (EV = 14/3 ≈ 4.67).
</details>

---

### 9. Expected maximum of two uniforms 🟡

X, Y ~ Uniform(0, 1) independent. Find E[max(X, Y)].

<details><summary>Solution</summary>

P(max ≤ m) = m², so the density is 2m. E = ∫₀¹ m · 2m dm = **2/3**.

Generalisation: max of n uniforms has expectation n/(n+1).
</details>

---

### 10. Gambler's ruin 🔴

You start with ₹k and bet ₹1 on fair coin flips until you reach ₹N or go broke. Probability you reach N? Expected duration?

<details><summary>Solution</summary>

Let pₖ be the probability of reaching N. pₖ = ½pₖ₊₁ + ½pₖ₋₁ with p₀ = 0, p_N = 1 ⇒ linear ⇒ **pₖ = k/N**.

Duration Dₖ satisfies Dₖ = 1 + ½Dₖ₊₁ + ½Dₖ₋₁, D₀ = D_N = 0 ⇒ **Dₖ = k(N − k)**.

A fair game is a martingale: your expected wealth at the end equals your starting wealth, k = N·pₖ.
</details>
