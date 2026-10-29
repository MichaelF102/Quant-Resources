# Stochastic calculus cheat sheet

*Last reviewed: Oct 2026*

Notation: W_t, B_t standard Brownian motions, μ drift, σ volatility, r risk-free rate, λ market price of risk, κ mean-reversion speed, θ long-run mean, ρ correlation, Q risk-neutral measure, P real-world measure.

## 1. Brownian motion

- W₀ = 0; independent increments; W_t − W_s ~ N(0, t − s) for s < t.
- Paths are continuous but nowhere differentiable.
- Quadratic variation: (dW)² = dt, while (dt)² and dt·dW are treated as zero.
- Covariance: Cov(W_s, W_t) = min(s, t).

### Brownian bridge

Conditional on W_T = b, the path W_t for 0 ≤ t ≤ T is Gaussian with

- mean (t/T) b
- variance t(T − t)/T

Used in simulation for stratified and path-dependent sampling.

## 2. Stochastic integrals

- Itô integral: ∫₀ᵀ H_t dW_t, with H adapted and square-integrable.
- Mean zero: E[∫₀ᵀ H_t dW_t] = 0.
- Itô isometry: E[(∫₀ᵀ H_t dW_t)²] = E[∫₀ᵀ H_t² dt].
- Itô integral is a martingale. It differs from a Stratonovich integral by a ½ correction term.

## 3. Itô's lemma

For dX = μ dt + σ dW and a twice-differentiable f(t, X):

df = (∂f/∂t + μ ∂f/∂x + ½σ² ∂²f/∂x²) dt + σ ∂f/∂x dW

The ½σ² ∂²f/∂x² term is the Itô correction. Dropping it is the most common error in simulation and pricing exercises.

### Multidimensional form

For f(t, X, Y) with dX = μ₁ dt + σ₁ dW₁ and dY = μ₂ dt + σ₂ dW₂, where dW₁ dW₂ = ρ dt:

df = (f_t + μ₁f_x + μ₂f_y + ½σ₁²f_xx + ρσ₁σ₂f_xy + ½σ₂²f_yy) dt + σ₁f_x dW₁ + σ₂f_y dW₂

### Product rule

d(XY) = X dY + Y dX + dX dY

The last term is the covariation. For the Itô product, dX dY = σ_X σ_Y ρ dt.

## 4. Geometric Brownian motion

dS = μS dt + σS dW

- Solution: S_t = S₀ exp((μ − σ²/2)t + σW_t)
- Mean: E[S_t] = S₀e^(μt)
- Variance: Var(S_t) = S₀² e^(2μt) (e^(σ²t) − 1)
- Median: S₀e^((μ − σ²/2)t), below the mean because of right skew
- Log-returns are normal: ln(S_t / S₀) ~ N((μ − σ²/2)t, σ²t)

The −σ²/2 term comes directly from applying Itô's lemma to ln S.

## 5. Changing measure

### Girsanov theorem

Let λ_t be an adapted process. Define

dQ/dP = exp(−∫₀ᵀ λ_t dW_t − ½∫₀ᵀ λ_t² dt)

Under Q, W^Q_t = W_t + ∫₀ᵗ λ_s ds is a Brownian motion. A sufficient condition for the density to be a true martingale is Novikov's condition: E[exp(½∫₀ᵀ λ_t² dt)] < ∞.

### Risk-neutral pricing

- Market price of risk: λ = (μ − r)/σ.
- Under Q: dS = rS dt + σS dW^Q. The drift is r, not μ.
- Discounted prices are Q-martingales: e^(−rt) S_t.
- Option price: V₀ = e^(−rT) E^Q[payoff].

## 6. Pricing PDE and Feynman–Kac

For V(S, t) with no dividends:

∂V/∂t + ½σ²S² ∂²V/∂S² + rS ∂V/∂S − rV = 0, with V(S, T) = payoff.

The Feynman–Kac formula gives the general solution: for dX = a(t, X) dt + b(t, X) dW, the function

u(t, x) = E[e^(−∫ₜᵀ r ds) g(X_T) | X_t = x]

solves ∂u/∂t + a ∂u/∂x + ½b² ∂²u/∂x² − r u = 0, with u(T, x) = g(x).

## 7. Correlated Brownian motions

If W and B are independent and dW₂ = ρ dW₁ + √(1 − ρ²) dB, then W₁ and W₂ have correlation ρ. This is the construction used in simulating correlated assets.

## 8. Common stochastic models

| Model | SDE | Notes |
|---|---|---|
| Arithmetic Brownian motion | dX = μ dt + σ dW | Can go negative; used for rates in some settings |
| Geometric Brownian motion | dS = μS dt + σS dW | Lognormal prices; Black-Scholes |
| Ornstein–Uhlenbeck (Vasicek) | dX = κ(θ − X) dt + σ dW | Mean-reverting; can go negative |
| Cox–Ingersoll–Ross | dr = κ(θ − r) dt + σ√r dW | Non-negative; stays positive if 2κθ ≥ σ² (Feller condition) |
| Heston | dS = rS dt + √v S dW₁; dv = κ(θ − v) dt + ξ√v dW₂ | Stochastic volatility; dW₁ dW₂ = ρ dt |

### Ornstein–Uhlenbeck

- E[X_t] = θ + (X₀ − θ)e^(−κt)
- Var(X_t) = σ²(1 − e^(−2κt)) / (2κ)
- Stationary variance: σ² / (2κ)
- Half-life of a deviation from θ: ln 2 / κ

Used for mean-reverting spreads, such as [Project 05](../projects/README.md), and interest-rate models.

## 9. Numerical simulation

### Euler–Maruyama

For dX = a(X) dt + b(X) dW on a grid with step Δt:

X_(n+1) = X_n + a(X_n) Δt + b(X_n) √Δt Z_n, with Z_n ~ N(0, 1)

- Strong order 1/2; weak order 1.
- Exact simulation of GBM avoids discretisation error: S_(n+1) = S_n exp((μ − σ²/2)Δt + σ√Δt Z_n).

### Milstein

X_(n+1) = X_n + a Δt + b √Δt Z + ½ b b′ (Z² − 1) Δt

Strong order 1. The extra term comes from the Itô correction.

## 10. Common mistakes

- Using μ instead of r when pricing under the risk-neutral measure.
- Forgetting the −σ²/2 term when simulating GBM, which biases the simulated price.
- Applying the ordinary chain rule to a Brownian path without the Itô term.
- Treating an Itô integral as a Riemann–Stieltjes integral. Its value depends on the choice of evaluation point.
- Using Euler discretisation for a CIR process without guarding against negative values, or using a discretisation that yields negative variance.

## 11. Interview favourites

- Why does GBM have a drift of μ − σ²/2 in the log? Itô's lemma applied to ln S gives a −σ²/2 correction.
- Why is the expected value of S_T equal to S₀e^(μT), but the median smaller? Lognormal skew: the mean is pulled up by the right tail.
- What is the Black-Scholes PDE for a forward contract on S? The same PDE with the forward's terminal condition. The solution is V = S − Ke^(−r(T−t)).
- What does the Feller condition guarantee? That the CIR process stays strictly positive.
- Why does the Girsanov drift λ equal the market price of risk? It is the amount by which the real-world drift exceeds the risk-free rate, per unit of volatility.
