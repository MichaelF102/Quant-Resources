# Market-making and betting games

These games test fair value under uncertainty, sizing, and how you adjust to information. Say your quotes out loud, state your fair value, and explain how your quote would change if the other side knew more than you.

Difficulty: 🟢 warm-up · 🟡 standard · 🔴 hard

---

### 1. Fair value of three dice 🟢

A fair die is rolled three times. Make a two-sided market on the total.

<details><summary>Solution</summary>

Fair value is E[total] = 3 × 3.5 = **10.5**.

A reasonable market is something like 10 bid, 11 ask, with the spread reflecting how much you could lose to an informed counterparty. If someone trades you a lot at 11 after the first roll shows a 6, you should be willing to revise the fair value, which is the skill being tested.
</details>

---

### 2. Expected maximum of two dice 🟡

Two fair dice are rolled. Price a game that pays the larger of the two faces.

<details><summary>Solution</summary>

E[max] = Σ_(k=1)⁶ k · [(k/6)² − ((k − 1)/6)²] = Σ k(2k − 1)/36 = 161/36 ≈ **4.47**.

Use the complement: P(max ≤ k) = (k/6)², so E[max] = Σ_(k=0)⁵ P(max > k) = Σ_(k=0)⁵ (1 − (k/6)²) = 6 − 55/36 = 161/36. The complement method is faster to write on a whiteboard.
</details>

---

### 3. Expected heads in ten flips 🟢

A market is made on the number of heads in ten fair flips. Where should the midpoint be?

<details><summary>Solution</summary>

E[heads] = 10 × 0.5 = **5**.

The distribution is symmetric about 5, so the median and mode are also 5. Your spread should widen with the variance, which is 2.5 here. A market on the sum of ten dice would need a much wider spread, because its variance is larger.
</details>

---

### 4. Kelly fraction for a biased coin 🟡

A coin lands heads with probability 0.6. You can bet any fraction of your bankroll at even money. What fraction maximises the long-run growth rate?

<details><summary>Solution</summary>

For a bet paying b to 1 with win probability p, the Kelly fraction is f* = p − (1 − p)/b.

Here b = 1 and p = 0.6, so f* = 0.6 − 0.4 = **0.2**. Bet 20% of your bankroll.

Half Kelly is often used in practice, because the growth rate falls off slowly with overbetting, while the drawdowns grow quickly. Betting more than twice the Kelly fraction loses money in the long run.
</details>

---

### 5. Adjusting quotes to inventory 🟡

You have bought 50 units of a stock from a customer. How should your bid and ask change, and why?

<details><summary>Solution</summary>

You are long inventory, so you want to sell it. Lower both your bid and ask, which makes your ask more attractive to buyers and makes your bid less likely to be hit.

The principle is the one in the Avellaneda–Stoikov model (see [Project 11](../projects/11-market-making-simulation/)): the reservation price moves against your inventory, and the spread widens as inventory risk rises.
</details>

---

### 6. The St. Petersburg game 🔴

A coin is flipped until heads. You are paid 2^k if heads first appears on flip k. What is a fair price to play?

<details><summary>Solution</summary>

The expected payoff is infinite, as computed in [Brainteasers](brainteasers.md), Problem 4.

In practice, the answer is a price much lower than the expected value. A common argument is that utility is concave in wealth, so the value of the game to a person with finite wealth is finite. Another is that the game's value is bounded by the total money available to the banker.

Interviewers expect you to name the paradox, state the expected value, and explain why you would not pay an infinite price.
</details>

---

### 7. Two-sided market on a coin sequence 🟡

A fair coin is flipped until you see HT. Make a market on the number of flips.

<details><summary>Solution</summary>

Using the first-step method: let E_H be the expected flips from a state where the last flip was H, and E₀ from the start. Then E₀ = 1 + ½E₀ + ½E_H, and E_H = 1 + ½E_H + ½·0 (after H, a T ends the game; a further H keeps you in the state H).

Solving gives E_H = 2 and E₀ = **4**.

The market should centre around 4, with the spread reflecting the variance of the number of flips. The variance is 4 and the standard deviation is 2, which a simulation of 400,000 games confirms.
</details>
