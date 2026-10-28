"""Project 01 — Monte Carlo pricer for a European call option.

Compares plain Monte Carlo, antithetic variates and a control variate
against the Black-Scholes closed form.

Run:  python mc_pricer.py
"""

from dataclasses import dataclass

import numpy as np
from scipy.stats import norm


@dataclass
class Option:
    s0: float = 100.0   # spot
    k: float = 100.0    # strike
    r: float = 0.065    # risk-free rate (continuous)
    sigma: float = 0.20 # volatility
    t: float = 1.0      # maturity in years


def black_scholes_call(o: Option) -> float:
    """Closed-form Black-Scholes price of a European call."""
    d1 = (np.log(o.s0 / o.k) + (o.r + 0.5 * o.sigma**2) * o.t) / (o.sigma * np.sqrt(o.t))
    d2 = d1 - o.sigma * np.sqrt(o.t)
    return o.s0 * norm.cdf(d1) - o.k * np.exp(-o.r * o.t) * norm.cdf(d2)


def terminal_prices(o: Option, z: np.ndarray) -> np.ndarray:
    """Risk-neutral GBM terminal prices. Note the drift is r, not mu,
    and the -sigma^2/2 Ito correction."""
    return o.s0 * np.exp((o.r - 0.5 * o.sigma**2) * o.t + o.sigma * np.sqrt(o.t) * z)


def _estimate(samples: np.ndarray) -> tuple[float, float]:
    """Return (mean, standard error) of the discounted payoff samples."""
    return samples.mean(), samples.std(ddof=1) / np.sqrt(len(samples))


def mc_plain(o: Option, n: int, rng: np.random.Generator) -> tuple[float, float]:
    z = rng.standard_normal(n)
    payoff = np.maximum(terminal_prices(o, z) - o.k, 0.0)
    return _estimate(np.exp(-o.r * o.t) * payoff)


def mc_antithetic(o: Option, n: int, rng: np.random.Generator) -> tuple[float, float]:
    """Pair each Z with -Z; average within pairs so the samples stay i.i.d.
    Uses n/2 normal draws for n payoff evaluations."""
    z = rng.standard_normal(n // 2)
    disc = np.exp(-o.r * o.t)
    pay_pos = np.maximum(terminal_prices(o, z) - o.k, 0.0)
    pay_neg = np.maximum(terminal_prices(o, -z) - o.k, 0.0)
    return _estimate(disc * 0.5 * (pay_pos + pay_neg))


def mc_control_variate(o: Option, n: int, rng: np.random.Generator) -> tuple[float, float]:
    """Control variate: discounted S_T, whose expectation is exactly S0."""
    z = rng.standard_normal(n)
    st = terminal_prices(o, z)
    disc = np.exp(-o.r * o.t)
    y = disc * np.maximum(st - o.k, 0.0)
    x = disc * st
    cov = np.cov(y, x, ddof=1)
    beta = cov[0, 1] / cov[1, 1]
    adjusted = y - beta * (x - o.s0)
    return _estimate(adjusted)


def main() -> None:
    o = Option()
    bs = black_scholes_call(o)
    print(f"Black-Scholes price: {bs:.4f}\n")

    methods = {
        "Plain MC": mc_plain,
        "Antithetic": mc_antithetic,
        "Control variate": mc_control_variate,
    }

    header = f"{'N':>10} | " + " | ".join(f"{m:>32}" for m in methods)
    print(header)
    print("-" * len(header))
    for n in (1_000, 10_000, 100_000, 1_000_000):
        cells = []
        for fn in methods.values():
            rng = np.random.default_rng(42)  # same seed => fair comparison
            price, se = fn(o, n, rng)
            flag = "" if abs(price - bs) <= 2 * se else " !"
            cells.append(f"{price:8.4f} ± {se:.4f} (err {price - bs:+.4f}){flag}")
        print(f"{n:>10,} | " + " | ".join(f"{c:>32}" for c in cells))

    print("\n'!' marks an estimate more than 2 standard errors from Black-Scholes.")
    print("Expect SE to fall ~sqrt(10)x per row, and variance-reduced SEs to be lower.")


if __name__ == "__main__":
    main()
