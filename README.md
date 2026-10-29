# Quant Resources — the practical edition

> A curated, opinionated, **build-first** path into quantitative finance.
> Fewer links, clearer order, real projects, real data.

[![Link check](https://github.com/MichaelF102/quant-resources/actions/workflows/link-check.yml/badge.svg)](https://github.com/MichaelF102/quant-resources/actions/workflows/link-check.yml)
![Last reviewed](https://img.shields.io/badge/last%20reviewed-Oct%202026-blue)
![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green)

---

## What this is (and isn't)

**This is** a guided route: pick a role, follow a phased roadmap, prove each phase by building something, then prepare for interviews with real problem sets.

**This isn't** a list of every quant link on the internet. Every resource here has a one-line verdict, a difficulty level and, where it matters, the exact chapters worth your time. If something isn't here, that's usually on purpose.

---

## 1. Start here: pick your role

| Role | What you actually do | Core skills | Your path |
|---|---|---|---|
| **Quant Researcher (QR)** | Find and validate predictive signals; build models | Probability, statistics, time series, ML, research hygiene | [Roadmap →](roadmaps/quant-researcher.md) |
| **Quant Trader (QT)** | Price, quote and manage risk in real time | Mental math, probability, options intuition, game theory | [Roadmap →](roadmaps/quant-trader.md) |
| **Quant Developer (QD)** | Build the trading systems, backtesters and data pipelines | C++/Python, systems, data structures, low latency | [Roadmap →](roadmaps/quant-developer.md) |
| **Risk / Model Validation** | Measure, stress and challenge models | Statistics, derivatives pricing, regulation (FRTB, Basel) | [Roadmap →](roadmaps/risk-model-validation.md) |

Not sure? Start with the **QR roadmap, Phase 1**. Probability and statistics are shared by every role.

---

## 2. Navigate

| Section | Use it for |
|---|---|
| 🗺️ [Roadmaps](roadmaps/) | Phased plans for four roles, with time budgets, checkpoints and "skip for now" notes. [Compare them](roadmaps/README.md) |
| 🛠️ [Projects](projects/) | A difficulty-ordered ladder of projects that prove each concept |
| 📊 [Data sources](data/data-sources.md) | Where to get prices, option chains, factors, macro and tick data — with caveats |
| 🧠 [Interview prep](interview/) | Problem sets with hidden solutions, round-by-round expectations |
| 💼 [Careers (India)](careers/india.md) | Firms by type, entry routes, competitions and timing |
| 📄 [Cheat sheets](cheatsheets/) | One-page references (Greeks, distributions, …) |
| 🧰 [Tools and technologies](tools-and-technologies/) | Python, C++, profiling, Linux, version control, databases and quant libraries |
| ⚠️ [Pitfalls](pitfalls.md) | Why most backtests lie — and how to make yours honest |

---

## 3. How to use this repo

1. **Pick a role** above and open its roadmap.
2. **Work phase by phase.** Each phase names one primary resource and one backup — finish the primary before reaching for more.
3. **Close every phase with a project** from the [ladder](projects/). If you can't build it, you don't know it yet.
4. **Read [Pitfalls](pitfalls.md) before your first backtest**, not after.
5. **Drill interviews in parallel** from Phase 2 onwards — 20 minutes a day beats a cram week.

### Legend

| Tag | Meaning |
|---|---|
| 🟢 | Beginner — no prerequisites beyond school maths |
| 🟡 | Intermediate — assumes the previous phase |
| 🔴 | Advanced — graduate level or specialist |
| 💸 | Paid · 🆓 Free |

---

## 4. Contributing

Suggestions are welcome — but every resource must earn its place. Read [CONTRIBUTING.md](CONTRIBUTING.md) first; submissions without a verdict and difficulty level won't be merged.

Found a dead link? [Open an issue](../../issues/new?template=dead-link.md). A weekly workflow also checks every link automatically.

---

## License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Code in `projects/` is MIT.

Maintained by [Michael Fernandes](https://michaelfernandes.netlify.app) · [@MichaelF102](https://github.com/MichaelF102)
