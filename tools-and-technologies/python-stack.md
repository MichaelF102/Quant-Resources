# Python stack

*Last reviewed: Oct 2026*

Python is the working language for most of this program: data handling, research, backtesting and tooling. This page covers the environment, the core libraries, and the pitfalls that cause wrong results.

## 1. Environment

Use an isolated environment for every project. Never install into the system Python.

| Tool | Use it for | Verdict | Cost | Link |
|---|---|---|---|---|
| `venv` | Built-in virtual environments | Always available. Enough for small projects. | 🆓 | [Python docs](https://docs.python.org/3/library/venv.html) |
| uv | Fast environment and dependency management, with a lock file | Good default for new projects. Faster than pip, and it manages Python versions. | 🆓 | [uv docs](https://docs.astral.sh/uv/) |
| pip with `requirements.txt` | Installing packages | Works everywhere. Pin exact versions when you need reproducibility. | 🆓 | — |

**Setup for a new project:**

1. Create the environment in the project folder, and add it to `.gitignore`.
2. Install only the libraries the project needs.
3. Pin the versions in a lock file or `requirements.txt`, and commit it.
4. Record the Python version in the README.

A pinned environment is what makes a result reproducible six months later.

## 2. Core numerical libraries

| Library | Use it for | Notes | Link |
|---|---|---|---|
| NumPy | Arrays, vectorised maths, random numbers | The base of everything else. Use `np.random.default_rng` for reproducible random numbers, as [Project 01](../projects/01-monte-carlo-pricer/) does. | [docs](https://numpy.org/doc/stable/) |
| SciPy | Root-finding, optimisation, statistical distributions | Use `scipy.stats` for distributions and `brentq` for implied-volatility inversion in [Project 02](../projects/02-implied-vol-surface/). | — |
| pandas | Tabular and time-series data | The most common source of silent errors in this program. See the pitfalls below. | [docs](https://pandas.pydata.org/docs/) |
| statsmodels | Regression, time-series models, hypothesis tests | Prefer it over scikit-learn for inference and diagnostics. See [Quant libraries](quant-libraries.md). | [docs](https://www.statsmodels.org/stable/) |
| scikit-learn | Machine learning and cross-validation | Use it for models; write your own purged splitter for time series ([Project 09](../projects/README.md)). | [docs](https://scikit-learn.org/stable/) |
| matplotlib | Plots | Enough for most work. Use it for the volatility surface and the drawdown plots. | — |

## 3. Speed in Python

Vectorise first. A loop over a pandas column is usually the bottleneck, and vectorised NumPy removes most of it.

| Tool | Use it for | Verdict |
|---|---|---|
| Vectorised NumPy and pandas | Most numerical work | Try this first. |
| Numba (`@njit`) | Tight numerical loops that can't be vectorised, such as a Crank–Nicolson time step or an order-book replay | Compiles to machine code. The first call includes compile time, so benchmark after a warm-up. Only a subset of Python is supported. [Docs](https://numba.readthedocs.io/en/stable/) |
| pybind11 | Calling C++ from Python | Use it when a C++ kernel is the right tool, for example to time a C++ order book from Python. [Docs](https://pybind11.readthedocs.io/en/stable/) |

## 4. Testing and quality

| Tool | Use it for | Verdict | Link |
|---|---|---|---|
| pytest | Unit tests | The default. Test every function that returns a number a reader might trust. | [docs](https://docs.pytest.org/en/stable/) |
| Type hints and a checker such as mypy or pyright | Catching interface mistakes | Optional. Useful in larger projects, such as the honest backtester. | — |
| Ruff | Linting and formatting | Fast, and one tool for both. | — |

Write tests for the things that fail silently: the sign of a return, the alignment of two series, the unit of a rate, and whether a signal used future data.

## 5. Notebooks

Jupyter is good for exploration and for presenting results. Keep the logic in modules and import them into notebooks. A notebook that holds the only copy of a calculation cannot be tested or rerun reliably.

## 6. Pitfalls that produce wrong results

- **Look-ahead in pandas.** `rolling(..., center=True)` uses future values. A signal computed from the day's close and traded at that close is also look-ahead. Use `shift(1)` before you trade a signal.
- **Index alignment.** pandas aligns on the index, not on position. Two series with different dates produce NaNs or silently wrong sums when combined. Check `reindex` and `join` results.
- **Missing values.** Decide explicitly how NaNs propagate. `sum()` skips them and `dot()` may not. A silent NaN can turn a return into zero.
- **Time zones.** Exchange data is in IST. Store timestamps in one zone (UTC is a good choice), convert for display, and check that daily bars close at the right time.
- **Floating-point equality.** Compare with a tolerance, not `==`, when checking a price or a Greek.
- **Version changes.** pandas and NumPy change default behaviour between major versions. Read the release notes for the version you pinned, and rerun your tests after an upgrade.
- **Random seeds.** A seed that is set once at import time makes results depend on the order of imports. Pass a generator explicitly.

## 7. Learn when

| Phase | Learn |
|---|---|
| QR Phase 0 | Environment, pytest, git |
| QR Phases 1–3 | NumPy, SciPy, pandas, statsmodels |
| QR Phase 5 | scikit-learn, cross-validation for time series |
| QD research track | Packaging, pandas at scale, pinned environments |
| QT Phase 3 | NumPy and SciPy for option calculations |
| Risk Phases 1–3 | statsmodels, scipy.stats, and the backtesting tests |
