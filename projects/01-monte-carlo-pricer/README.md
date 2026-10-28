# 01 — Monte Carlo option pricer

**Proves:** risk-neutral pricing, geometric Brownian motion, Monte Carlo convergence, variance reduction
**Level:** 🟢 · **Time:** 1 weekend
**Prerequisites:** [QR roadmap Phase 1](../../roadmaps/quant-researcher.md)

## Goal

Price a European call by simulation, check it against the Black-Scholes closed form, then make the simulation converge faster using variance reduction. You'll come away understanding *why* the price is a discounted risk-neutral expectation, not just that it is.

## Data

None — synthetic parameters. Defaults: S₀ = 100, K = 100, r = 6.5%, σ = 20%, T = 1 year.

## Run it

```bash
pip install numpy scipy
python mc_pricer.py
```

## Steps

1. Implement the Black-Scholes call price as your ground truth.
2. Simulate terminal prices under the risk-neutral measure:
   S_T = S₀ · exp((r − σ²/2)T + σ√T · Z), Z ~ N(0, 1)
3. Price = e^(−rT) · mean(max(S_T − K, 0)). Report the standard error.
4. Add **antithetic variates**: pair each Z with −Z.
5. Add a **control variate**: use S_T itself, whose expectation S₀e^(rT) is known.
6. Compare standard errors at the same path count.

## Done when

- [ ] Plain MC price is within 2 standard errors of Black-Scholes
- [ ] Standard error shrinks roughly as 1/√N (check at N = 10³, 10⁴, 10⁵, 10⁶)
- [ ] Antithetic and control-variate estimators show a lower standard error than plain MC at equal N
- [ ] You can explain in one sentence why we drift at *r*, not at the stock's expected return

## Common pitfalls

- Using drift μ instead of r — that's real-world simulation, not risk-neutral pricing.
- Forgetting the −σ²/2 Itô correction, which biases the price upward.
- Comparing estimators with different random seeds and reading noise as improvement.

## Stretch goals

- Price an Asian (average-price) option, where no simple closed form exists — this is where Monte Carlo earns its keep.
- Estimate Delta by pathwise differentiation and by finite differences; compare their variance.
- Vectorise further or port the inner loop to C++ with `pybind11` and time it.

## Further reading

- Glasserman, *Monte Carlo Methods in Financial Engineering*, ch. 4 💸 — the standard reference on variance reduction.
