# Greeks cheat sheet

Black-Scholes, non-dividend-paying underlying. Notation: S spot, K strike, r rate, σ vol, τ time to expiry, N(·) normal CDF, φ(·) normal PDF.

d₁ = [ln(S/K) + (r + σ²/2)τ] / (σ√τ)  d₂ = d₁ − σ√τ

| Greek | Measures | Call | Put | Intuition |
|---|---|---|---|---|
| **Delta** Δ = ∂V/∂S | Price sensitivity to spot | N(d₁) ∈ (0, 1) | N(d₁) − 1 ∈ (−1, 0) | Hedge ratio; loosely, the risk-neutral-ish chance of finishing in the money (strictly that's N(d₂)) |
| **Gamma** Γ = ∂²V/∂S² | How fast Delta changes | φ(d₁) / (Sσ√τ) | same | Highest at-the-money near expiry. Long options = long gamma |
| **Vega** ν = ∂V/∂σ | Sensitivity to volatility | S φ(d₁) √τ | same | Highest at-the-money, long-dated. Long options = long vega |
| **Theta** Θ = ∂V/∂t | Time decay | −Sφ(d₁)σ/(2√τ) − rKe^(−rτ)N(d₂) | −Sφ(d₁)σ/(2√τ) + rKe^(−rτ)N(−d₂) | Usually negative for long options — the cost of holding gamma |
| **Rho** ρ = ∂V/∂r | Sensitivity to rates | Kτ e^(−rτ) N(d₂) | −Kτ e^(−rτ) N(−d₂) | Usually the least important Greek for short-dated equity options |

## Relationships worth memorising

- **Put-call parity:** C − P = S − Ke^(−rτ). So Δ_call − Δ_put = 1, and gamma and vega are identical for calls and puts at the same strike.
- **Gamma–theta trade-off** (delta-hedged, from the BS PDE): Θ + ½σ²S²Γ + rSΔ − rV = 0. Being long gamma means paying theta — you profit only if realised volatility exceeds implied.
- **ATM rule of thumb:** an at-the-money option is worth roughly 0.4 · S · σ · √τ.

## Interview favourites

- Why is gamma highest at-the-money near expiry? Delta flips from ~0 to ~1 over a tiny price range.
- What happens to a deep in-the-money call's delta as expiry approaches? It goes to 1.
- You're long a straddle. Which Greeks are you long and short? Long gamma and vega, short theta, roughly delta-neutral.
