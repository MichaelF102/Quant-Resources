# Options and derivatives problems

Try each for at least 10 minutes before opening the solution. Use the [Greeks cheat sheet](../cheatsheets/greeks.md) for formulas, but first try the argument without it: most of these reduce to no-arbitrage and a bound.

Difficulty: 🟢 warm-up · 🟡 standard · 🔴 hard

---

### 1. Put-call parity 🟢

A stock trades at 100. A European call and put, both with strike 100 and one year to expiry, have prices C and P. The risk-free rate is 5% continuously compounded, and there are no dividends. Express C − P.

<details><summary>Solution</summary>

Put-call parity: C − P = S − Ke^(−rT).

Here: C − P = 100 − 100e^(−0.05) = 100 − 95.12 = **4.88**.

The identity holds because a long call and a short put replicate a long forward, which costs the present value of the strike to settle.
</details>

---

### 2. Lower bound on a call 🟢

With the same setup, what is the lowest possible price for the call, and why?

<details><summary>Solution</summary>

C ≥ max(S − Ke^(−rT), 0) = max(100 − 95.12, 0) = **4.88**.

If the call were cheaper, buying it and shorting the stock would lock in a profit at expiry. The argument uses only no-arbitrage, not a model. The same reasoning gives a lower bound for a put: P ≥ max(Ke^(−rT) − S, 0).
</details>

---

### 3. Early exercise of an American call 🟡

Why is it never optimal to exercise an American call on a non-dividend-paying stock before expiry?

<details><summary>Solution</summary>

Exercising early gives S − K, which is less than S − Ke^(−rT) when r > 0. The second quantity is the value of the call's lower bound, which is also the value of holding the option. Holding keeps the strike's interest and the insurance against a fall in the stock.

Early exercise can be optimal for a call only when dividends are paid, because the stock price drops on the ex-dividend date and the option holder loses that value.
</details>

---

### 4. The forward price with a dividend yield 🟡

A stock pays a continuous dividend yield q. Its spot price is S, and the risk-free rate is r. What is the forward price for delivery at T?

<details><summary>Solution</summary>

**F = S e^((r − q)T)**

A holder of the forward has the stock's dividends, which reduce its growth. The cost of carrying the stock is r, and the dividend yield offsets part of it.

Check: with q = 0 this is S e^(rT), the usual cost-of-carry result.
</details>

---

### 5. Delta of a straddle at the money 🟡

A straddle is a long call and a long put with the same strike and expiry. What is its delta when the spot is at the strike, and why does that matter?

<details><summary>Solution</summary>

The call delta is about 0.5 and the put delta is about −0.5 at the money, so the straddle's delta is close to **0**.

Delta-neutral is not the same as risk-free. The straddle has large positive gamma and vega, and negative theta. It profits from movement in either direction, and loses if the stock stays still. This is the basis of the Greeks interpretation in [Greeks cheat sheet](../cheatsheets/greeks.md), section 9.
</details>

---

### 6. One-step binomial pricing 🟡

A stock is at 100. In one period it goes to 110 or 90. The risk-free rate is zero. A call with strike 100 pays max(S − 100, 0) at expiry. What is its price?

<details><summary>Solution</summary>

The call pays 10 in the up state and 0 in the down state.

The risk-neutral probability of an up move is q = (e^(rΔt) − d)/(u − d) = (1 − 0.9)/(1.1 − 0.9) = **0.5**.

The price is the discounted expected payoff: C = 0.5 × 10 + 0.5 × 0 = **5**.

Check by replication: hold Δ = (10 − 0)/(110 − 90) = 0.5 shares and borrow 45, which costs nothing at zero rates. The portfolio pays 0.5 × 110 − 45 = 10 in the up state and 0.5 × 90 − 45 = 0 in the down state. It costs 0.5 × 100 − 45 = 5. The two methods agree.
</details>

---

### 7. Vega at the money 🟡

For an at-the-money European option with small rates, roughly how does the option's value change for a one-point change in implied volatility, with S = 100, σ = 20%, T = 1?

<details><summary>Solution</summary>

The approximation ATM price ≈ 0.4 · S · σ · √T gives vega ≈ 0.4 · S · √T = 0.4 × 100 × 1 = 40 per unit of σ, or **0.40 per vol point**.

Check against the Black-Scholes vega, S φ(d₁) √T: with d₁ ≈ 0.1, φ ≈ 0.397, so vega ≈ 39.7, or about 0.40 per vol point. The approximation is accurate near the money.
</details>

---

### 8. Gamma and expiry 🔴

Why is the gamma of an at-the-money option largest just before expiry, and what does a trader do about it?

<details><summary>Solution</summary>

Near expiry, the option's delta must move from roughly 0 to roughly 1 over a narrow range of spot prices around the strike. That steep change in delta is gamma, which therefore peaks at the money as time to expiry shrinks.

A trader who is short this gamma faces large hedging costs near the strike, since the hedge must change quickly. A trader who is long it profits from those moves, but pays theta to hold the position. Managing this is one reason books are often closed or rolled before the last days.
</details>

---

### 9. A box spread 🔴

A call spread buys the call with strike K₁ and sells the call with strike K₂ > K₁. A box spread combines a bull call spread with a bear put spread on the same strikes. What is the payoff of the box at expiry, and what should it cost today?

<details><summary>Solution</summary>

At expiry the box always pays K₂ − K₁, whatever the stock price does. The payoff does not depend on S.

Today's value must therefore be the present value of K₂ − K₁, which is (K₂ − K₁) e^(−rT). Any other price is an arbitrage. This is the reason box spreads are used as a synthetic zero-coupon bond, and their implied rate is a benchmark for interest rates.
</details>
