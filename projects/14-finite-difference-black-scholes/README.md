# 14 — Finite-difference solver for the Black-Scholes PDE

**Proves:** the Black-Scholes PDE as a numerical problem, explicit and implicit time-stepping, stability and convergence, and pricing of an option with early exercise
**Level:** 🟡 · **Time:** 1 weekend
**Prerequisites:** [Project 01](../01-monte-carlo-pricer/); [Stochastic calculus cheat sheet](../../cheatsheets/stochastic-calculus.md) (Black-Scholes PDE); [Greeks cheat sheet](../../cheatsheets/greeks.md)

## Goal

Solve the Black-Scholes PDE on a grid, backward in time from the payoff, and check the result against the closed-form price from [Project 01](../01-monte-carlo-pricer/). Then price an American put, which has no closed form, and read its early-exercise boundary from the grid. The question it answers: how do the numerical method's choices (grid size, time step, scheme) change accuracy and stability, and when do they break the answer?

## Data

None. Use the parameters from Project 01:

- K = 100, r = 6.5%, σ = 20%, T = 1 year, no dividends.
- Reference European call prices from the closed form at S = 80, 100 and 120: **2.1096, 11.2639, 27.3927**.

## Steps

1. **Set up the grid.** Use S ∈ [0, S_max] with M spatial intervals and time from 0 to T with N steps. Pick S_max well above the strike (for example 4K). Record the grid so that results can be reproduced.
2. **Boundary and terminal conditions.**
   - Terminal condition at t = T: V(S, T) = max(S − K, 0) for a call, max(K − S, 0) for a put.
   - Lower boundary: V(0, t) = 0 for a call; V(0, t) = K e^(−r(T − t)) for a put.
   - Upper boundary for a call: V(S_max, t) ≈ S_max − K e^(−r(T − t)). For a put: V(S_max, t) = 0.
3. **Discretise the spatial operator.** Use central differences for ∂V/∂S and ∂²V/∂S², which gives a tridiagonal system at each time step.
4. **Implement the θ-scheme.** Solve (I − θΔt L) Vⁿ⁺¹ = (I + (1 − θ)Δt L) Vⁿ, where L is the spatial operator. Use θ = 0 (explicit), θ = 1 (implicit) and θ = ½ (Crank–Nicolson). Solve the tridiagonal systems with a banded solver (`scipy.linalg.solve_banded`) rather than a dense inverse.
5. **Convergence study.** Hold the ratio of grid sizes fixed, halve Δx and Δt together, and record the maximum error at S = 80, 100 and 120 against the closed form.
6. **Stability study.** Use the explicit scheme with increasing N for fixed M. Find where the solution stops being stable and explain why in terms of the time step relative to the spatial grid.
7. **Greeks from the grid.** Estimate Delta and Gamma by finite differences on the solution, and compare them with the closed-form Greeks in the cheat sheet.
8. **American put.** Solve the linear complementarity problem: at each time step, take V = max(V, payoff). Use this projection after each implicit solve; a projected SOR solver is the more accurate alternative. Report the exercise boundary S*(t), the lowest spot at which exercising is optimal for each time.
9. **Check the American put against the European put.** The American put must be at least as valuable as the European put at every point, and the difference should be largest near the strike and shrink to zero deep in the money.

## Done when

- [ ] Crank–Nicolson with M = N = 400 matches the closed form to within 0.01 at S = 80, 100 and 120. Expect about 0.0025 maximum error.
- [ ] Crank–Nicolson error falls by about a factor of four when M and N are both doubled. The implicit scheme falls more slowly, since it is first-order in time.
- [ ] The explicit scheme's instability threshold is demonstrated and explained, with the time step and grid size at which the solution oscillates or blows up.
- [ ] Delta and Gamma from the grid agree with the closed form to a stated tolerance, with the grid used reported.
- [ ] American put price is at least the European price at every grid point, and the early-exercise boundary is plotted against time.
- [ ] Results reproduce from one command, and the grid, boundary, and scheme choices are written at the top of the code.

## Common pitfalls

- **Boundary too close.** A small S_max distorts prices near the strike and contaminates Greeks. Test with a larger S_max.
- **Time direction.** Solve backward from the payoff at T. A forward solve with the payoff as an initial condition solves the wrong problem.
- **Greeks from a coarse grid.** Finite differences of a coarse solution are much noisier than the price. Compute Greeks on the finest grid you can afford.
- **Interpolation at the spot.** Interpolating the grid to S₀ adds error of the same order as the grid spacing. Choose the grid so that S₀ falls on a node when possible.
- **Trusting one grid.** A single good match can be luck. Always run the convergence study.

## Stretch goals

- Use a log-transformed grid, x = ln S, which places more points near the money and makes the grid uniform in log-returns.
- Price a barrier option with the same solver by imposing the barrier as a boundary condition, and compare with the closed form.
- Price an option under a constant dividend yield q by changing the drift term, and check against the Merton formula in the Greeks cheat sheet.
- Extend to a two-dimensional problem, such as a basket option, and discuss why memory and time grow quickly with dimension.

## Further reading

- Wilmott, Howison and Dewynne, *The Mathematics of Financial Derivatives* 💸 — the standard treatment of finite-difference methods for option pricing.
- Duffy, *Finite Difference Methods in Financial Engineering* 💸 — a practical, code-oriented reference with worked schemes, including the θ-scheme and the American option treatment.
- Tavella and Randall, *Pricing Financial Instruments: The Finite Difference Method* 💸 — a focused text on finite differences for derivatives, with stability analysis.
