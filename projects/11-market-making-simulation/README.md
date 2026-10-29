# 11 — Market-making simulation

**Proves:** inventory risk, adverse selection, the Avellaneda–Stoikov quoting model, and how quoting decisions change profit and risk under different assumptions
**Level:** 🔴 · **Time:** 2–3 weekends
**Prerequisites:** [QT roadmap](../../roadmaps/quant-trader.md) Phase 4; [Stochastic calculus cheat sheet](../../cheatsheets/stochastic-calculus.md); [Project 10](../10-limit-order-book-simulator/) is useful but not required

## Goal

Simulate a market maker that quotes a bid and an ask around a fair value that follows a random walk, and fills against arriving market orders. Implement the Avellaneda–Stoikov model, which shifts quotes to control inventory, and compare it with a fixed-spread quoter. The question: how does a market maker trade off spread income against inventory risk, and what does the optimal quote look like?

## Data

Synthetic. The fair value follows a Brownian motion with volatility σ. Market orders arrive as a Poisson process whose intensity falls with the distance of the quote from fair value, following the exponential form used in the Avellaneda–Stoikov paper. Fix the random seed and record all parameters.

## Steps

1. **Model the market.** Fair value S_t with drift zero and volatility σ. Market-order arrivals at distance δ from fair value have intensity λ(δ) = A e^(−κδ), with A and κ as parameters.
2. **Implement the fixed-spread quoter.** Quote symmetric bid and ask at fair value ± a constant half-spread. Record cash, inventory and mark-to-market P&L.
3. **Implement Avellaneda–Stoikov.** With risk aversion γ, inventory q and time to the end of the session T − t, the reservation price and optimal total spread are:
   - r(s, q, t) = s − q γ σ² (T − t)
   - δ_total = γ σ² (T − t) + (2/γ) ln(1 + γ/κ)
   Quote at r ± δ_total/2. Check these formulas against the paper before implementing them.
4. **Run many sessions.** Simulate at least 10,000 sessions per parameter set, and report the distribution of final P&L, not only the mean.
5. **Vary risk aversion.** Run γ over at least four values. Show how spread and inventory change.
6. **Adverse selection.** Add an informed trader who knows the next price move with some probability. Measure how the market maker's P&L changes, and whether widening the spread recovers it.
7. **Report risk.** Report the mean and the 5th percentile of final P&L, and the average absolute inventory during the session.

## Done when

- [ ] Fixed-spread and Avellaneda–Stoikov quoters are run under identical market and seed settings
- [ ] Final P&L is reported as a distribution over at least 10,000 sessions, with mean, 5th percentile and standard deviation
- [ ] The reservation price and spread formulas are implemented and tested against a hand-computed case
- [ ] A table shows how spread, average inventory and P&L change with γ
- [ ] Adverse selection is added, and the write-up states how much of the income it removes
- [ ] The write-up explains the quote shift in one paragraph, in terms a trader would accept

## Common pitfalls

- **Reporting only mean P&L.** A quoter with positive mean P&L can have a large tail loss. The 5th percentile matters.
- **Ignoring the end of the session.** Inventory must be liquidated at T. State how, and include its cost.
- **Mixing units.** κ is per unit of price, and γ is per unit of wealth per unit of variance. A different unit convention changes the spread by an order of magnitude.
- **Fill probability assumed constant.** The fill intensity depends on distance from fair value. A constant fill rate removes the trade-off the model is about.
- **Calibrating to the paper's numbers.** Run a sanity check: as γ → 0, the spread should approach the value implied by κ alone.

## Stretch goals

- Use a mean-reverting fair value instead of a random walk, and compare the optimal quotes.
- Add a second asset with correlated fair value, and quote both with a shared inventory limit.
- Replace the synthetic market with the order book from [Project 10](../10-limit-order-book-simulator/) and compare the quoter's fills.

## Further reading

- Avellaneda and Stoikov (2008), "High-frequency trading in a limit order book," *Quantitative Finance*. The model implemented here.
- Glosten and Milgrom (1985), "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders," *Journal of Financial Economics*. The adverse-selection argument.
- Kyle (1985), "Continuous Auctions and Insider Trading," *Econometrica*. Informed trading and price impact.
