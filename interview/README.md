# Interview prep

Start these in parallel with the roadmap from Phase 2. **20 minutes a day** beats a cram week — pattern recognition is the whole game.

## What each round actually tests

| Round | Common at | What they're looking for | Practise with |
|---|---|---|---|
| Online assessment (mental math, numerical) | HFTs, prop shops | Speed and accuracy under time pressure | [Zetamac](https://arithmetic.zetamac.com/) — aim for 50+ in 120s, then 70+ |
| Probability & brainteasers | All | Structured thinking out loud, not just the answer | [Probability set](probability.md) |
| Market-making / betting games | Prop shops, options market makers | Setting fair value, adjusting to information, sizing bets | Play with friends: make two-sided markets on unknowns (e.g. "sum of three dice") |
| Statistics & ML | QR roles, hedge funds | Regression assumptions, overfitting, CV for time series | [Pitfalls](../pitfalls.md), ISLR exercises |
| Coding | QD especially, all roles | Clean, correct code; complexity; C++ knowledge for HFT | LeetCode mediums; implement an order book |
| Finance concepts | Banks, derivatives desks | Black-Scholes intuition, Greeks, put-call parity, no-arbitrage | [Greeks cheat sheet](../cheatsheets/greeks.md), Hull |
| Behavioural / fit | All | Why quant, why this firm, a project you can defend in depth | Prepare 2 projects you can discuss for 20 minutes each |

## How to answer probability questions

1. **Restate** the problem and clarify assumptions out loud.
2. **Simplify**: try a small case (n = 2, 3) and look for a pattern.
3. **Name the tool**: symmetry, linearity of expectation, conditioning, recursion, complement.
4. **Sanity-check** the answer: is it between 0 and 1? Does it behave right at the extremes?

Interviewers will often give hints — taking them gracefully is part of the assessment.

## Problem sets

- [Probability & expectation](probability.md) — 10 classic problems with hidden solutions
- Brainteasers — *coming soon*
- Statistics & ML — *coming soon*
- Options & derivatives — *coming soon*

## Books

| Book | Verdict |
|---|---|
| Zhou, *A Practical Guide to Quantitative Finance Interviews* 💸 | The default prep book. Work every probability chapter problem. |
| Crack, *Heard on the Street* 💸 | Older, broader; good second pass. |
| Mosteller, *Fifty Challenging Problems in Probability* 💸 | Short, elegant classics — many interview questions derive from these. |
| Joshi et al., *Quant Job Interview Questions and Answers* 💸 | Stronger on derivatives and C++; best for bank/desk quant roles. |
