# Greeks cheat sheet

*Last reviewed: Oct 2026*

Notation: S spot, F forward or futures price, K strike, r continuously compounded rate, q continuous dividend yield, σ volatility, τ time to expiry in years, N(·) standard normal CDF, φ(·) standard normal PDF, V option value.

## 1. Black-Scholes model

Non-dividend-paying underlying:

d₁ = [ln(S/K) + (r + σ²/2)τ] / (σ√τ)  d₂ = d₁ − σ√τ

### First-order Greeks

| Greek | Definition | Call | Put | Intuition |
|---|---|---|---|---|
| **Delta** | ∂V/∂S | N(d₁) ∈ (0, 1) | N(d₁) − 1 ∈ (−1, 0) | Hedge ratio. The risk-neutral probability of finishing in the money is N(d₂), not N(d₁) |
| **Gamma** | ∂²V/∂S² | φ(d₁) / (Sσ√τ) | same | Rate of change of delta. Highest at-the-money near expiry. Long options are long gamma |
| **Vega** | ∂V/∂σ | Sφ(d₁)√τ | same | Sensitivity to volatility. Highest at-the-money and in long-dated options. Long options are long vega |
| **Theta** | ∂V/∂t (calendar time) | −Sφ(d₁)σ/(2√τ) − rKe^(−rτ)N(d₂) | −Sφ(d₁)σ/(2√τ) + rKe^(−rτ)N(−d₂) | Time decay. Usually negative for long options, the cost of holding gamma |
| **Rho** | ∂V/∂r | Kτe^(−rτ)N(d₂) | −Kτe^(−rτ)N(−d₂) | Sensitivity to rates. Usually the least important Greek for short-dated equity options |

### Second-order Greeks

| Greek | Definition | Formula (call and put) | Use |
|---|---|---|---|
| **Vanna** | ∂Δ/∂σ = ∂ν/∂S | −φ(d₁) d₂ / σ | Delta change when volatility moves. Relevant for skew books |
| **Volga** (vomma) | ∂ν/∂σ = ∂²V/∂σ² | ν · d₁d₂ / σ | Convexity of vega. Long-volatility exposure |
| **Charm** | ∂Δ/∂t (calendar time) | −φ(d₁)(2rτ − d₂σ√τ) / (2τσ√τ) | Delta decay over time. Matters when hedging near expiry |

### Behaviour by moneyness

| Position | Delta (call) | Gamma | Vega | Theta |
|---|---|---|---|---|
| Deep in the money | → 1 | → 0 | → 0 | Small in magnitude; mostly rate carry |
| At the money | ≈ 0.5 | Maximum | Maximum | Largest in magnitude |
| Deep out of the money | → 0 | → 0 | → 0 | Small in magnitude |

Near expiry, at-the-money gamma and theta grow without bound as τ → 0. Delta converges to the step function 1{S > K} for a call.

## 2. Units and conventions

Quoted Greeks are not always per unit change. Check the convention before comparing figures across sources or systems.

| Greek | Raw value | Common quoting convention |
|---|---|---|
| Vega | per 1.00 change in σ | per 1 vol point (0.01 in σ) |
| Theta | per year | per calendar day (÷ 365), or ÷ 252 for trading days |
| Rho | per 1.00 change in r | per 1% (0.01 in r) |

## 3. Worked example

S = 100, K = 105, r = 5%, σ = 25%, τ = 0.5 years, no dividends:

| Quantity | Raw | Quoted |
|---|---|---|
| Call price | 5.99 | 5.99 |
| Delta (call) | 0.4816 | 0.48 |
| Gamma | 0.0225 | 0.0225 |
| Vega | 28.18 | 0.28 per vol point |
| Theta (call) | −9.15 per year | −0.025 per day |
| Rho (call) | 21.08 | 0.21 per 1% |

## 4. Dividend-paying underlying (Merton)

With continuous dividend yield q, replace S by S·e^(−qτ) in the price, and use r − q in d₁:

d₁ = [ln(S/K) + (r − q + σ²/2)τ] / (σ√τ)

- Call Delta = e^(−qτ) N(d₁); put Delta = e^(−qτ)(N(d₁) − 1)
- Gamma = e^(−qτ) φ(d₁) / (Sσ√τ)
- Vega = S e^(−qτ) φ(d₁) √τ

## 5. Black-76 (options on futures and forwards)

For an option written on a forward or futures price F, with discounting at r:

d₁ = [ln(F/K) + σ²τ/2] / (σ√τ)  d₂ = d₁ − σ√τ

- Call: C = e^(−rτ)[F·N(d₁) − K·N(d₂)]
- Put: P = e^(−rτ)[K·N(−d₂) − F·N(−d₁)]
- Delta with respect to F: call e^(−rτ)N(d₁); put e^(−rτ)(N(d₁) − 1)
- Gamma with respect to F: e^(−rτ) φ(d₁) / (Fσ√τ)
- Vega: e^(−rτ) F φ(d₁) √τ

Black-76 is the standard form for index futures options and the right model for implied volatility inversion on forward prices. See [Project 02](../projects/02-implied-vol-surface/).

## 6. Hedging and P&L

**Delta hedging.** Hold −Δ units of the underlying against one option. For a portfolio, the net hedge is −Σ(position × Δ).

**Gamma and theta.** A delta-hedged long option position earns gamma and pays theta. Over a small interval dt, the approximate P&L is

P&L ≈ ½ Γ S² (σ_R² − σ_I²) dt

where σ_R is the realised volatility and σ_I the implied volatility used to price the option. A long-gamma, delta-hedged position profits when realised volatility exceeds implied, and loses otherwise.

**Gamma scalping.** Rehedge delta at intervals as the spot moves. Each rehedge realises a gain when the market has moved away and back, which is how the gamma P&L is harvested in practice.

**Aggregation.** Portfolio Greeks are sums of position-weighted Greeks. Check that each Greek is quoted per contract and per unit of underlying, not per share, before summing.

## 7. Relationships worth memorising

- **Put-call parity:** C − P = S − Ke^(−rτ). Therefore Δ_call − Δ_put = 1, and gamma and vega are identical for calls and puts at the same strike.
- **Gamma–theta relation** (delta-hedged, from the Black-Scholes PDE): Θ + ½σ²S²Γ + rSΔ − rV = 0.
- **ATM approximation:** an at-the-money option with K = S and r ≈ 0 is worth approximately 0.4 · S · σ · √τ. The exact coefficient is 1/√(2π) ≈ 0.399.
- **Forward versus spot delta:** with F = S·e^((r − q)τ), the chain rule gives ∂V/∂S = e^((r − q)τ) · ∂V/∂F. Black-76 Delta therefore converts to the Merton Delta e^(−qτ)N(d₁) for any r and q.

## 8. Common mistakes

- Mixing units: τ in days where the formula expects years, or theta per year read as per day.
- Dropping the sign on put Delta. Put Delta is N(d₁) − 1, which is negative.
- Using simple rates where the formulas assume continuous compounding.
- Forgetting the dividend yield for index or single-stock options, which changes both d₁ and the forward.
- Quoting vega per 1.00 change in σ and comparing it with a figure quoted per vol point.
- Summing Greeks across positions with different multipliers (for example, contract size versus share count).

## 9. Interview favourites

- Why is gamma highest at-the-money near expiry? Delta moves from about 0 to about 1 over a narrow range of spot, so its rate of change peaks there.
- What happens to a deep in-the-money call's delta as expiry approaches? It goes to 1.
- You are long a straddle. Which Greeks are you long and short? Long gamma and vega, short theta, roughly delta-neutral.
- Vega is 0.28 for a 25% vol option. What does that mean? A one-point rise in implied volatility adds about 0.28 to the option price, all else equal.
- Why does a delta-hedged long option lose money when realised volatility is below implied? Gamma gains are smaller than the theta paid, so the hedged book bleeds.
- How does the Black-76 delta differ from the Black-Scholes delta on the spot? It is taken with respect to the forward, which already embeds carry, so no dividend term appears. The discount factor e^(−rτ) multiplies it.
