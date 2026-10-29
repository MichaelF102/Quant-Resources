# Tools and technologies

The software, libraries and workflow you need for the projects and roadmaps. Each file covers one area: what the tool is for, which parts you need first, the common pitfalls, and the phase of a roadmap where it matters.

This folder is about tools, not theory. For the maths, see the [cheat sheets](../cheatsheets/). For the order in which to study, see the [roadmaps](../roadmaps/).

## Files

| File | Covers | Needed for |
|---|---|---|
| [Python stack](python-stack.md) | Python environments, numerical libraries, testing, notebooks, Numba and pybind11 bridges | All roles; Projects 01–03 and most of the research track |
| [C++ toolchain](cpp-toolchain.md) | Compilers, CMake, sanitizers, static analysis, formatting, unit tests, benchmarks | Quant Developer roadmap, Phases 1–5; Project 10 |
| [Profiling and debugging](profiling-and-debugging.md) | perf, Valgrind, GDB, strace, and how to measure without fooling yourself | Quant Developer Phase 5; any project that claims a speed-up |
| [Linux and shell](linux-and-shell.md) | Shell skills, search, terminal multiplexing, scheduling daily jobs, time zones and CPU pinning | All roles; Quant Developer Phases 3–4; the data pipeline checkpoint |
| [Version control and CI](version-control-and-ci.md) | Git workflow, GitHub Actions, pre-commit hooks, handling secrets and vendor data | All projects; the link check in this repo |
| [Databases and storage](databases-and-storage.md) | PostgreSQL, DuckDB, Parquet and Arrow, choosing a format, idempotent loads | Research platform track; Projects 03, 09 and 12 |
| [Quant libraries](quant-libraries.md) | QuantLib, arch, cvxpy, statsmodels and scikit-learn, and the backtesting libraries | Roadmap checkpoints in Phases 3–6; read the warning before using a backtester |

## Setup order

Set these up in this order. Each step is a checkpoint you can verify.

1. **Terminal and shell.** Open a terminal, change directory, search a file tree with `rg`, and write a shell loop. See [Linux and shell](linux-and-shell.md).
2. **Git and a remote.** Create a repository, commit, push, and check that the CI runs. See [Version control and CI](version-control-and-ci.md).
3. **Python environment.** Create an isolated environment, install the numerical stack, and run one test with `pytest`. See [Python stack](python-stack.md).
4. **C++ toolchain** (Quant Developer track). Build a CMake project with warnings as errors, and run it under a sanitizer. See [C++ toolchain](cpp-toolchain.md).
5. **Profiler.** Run `perf stat` on any program. See [Profiling and debugging](profiling-and-debugging.md).
6. **Database.** Load one day of bhavcopy into PostgreSQL or DuckDB, and query it. See [Databases and storage](databases-and-storage.md).

## Which tools by role

| Role | Core | Also useful |
|---|---|---|
| Quant Researcher | Python stack, quant libraries, version control | Databases, Linux basics |
| Quant Developer (HFT) | C++ toolchain, profiling, Linux | Python for tooling, version control |
| Quant Developer (research platform) | Python stack, databases, Linux, version control and CI | C++ for performance-critical parts |
| Quant Trader | Python stack for analysis, spreadsheets for quick checks | Quant libraries for options and volatility |
| Risk and Model Validation | Python stack, quant libraries, databases | Version control for documentation and reproducibility |

## Principles

- **Reproducibility first.** A result you cannot rerun is not a result. Pin versions, record the data source and date, and keep the code in version control.
- **Learn a tool when a project needs it.** Don't install a stack for a phase that hasn't started.
- **Read a library's source before trusting its defaults.** A backtester that fills trades at the same close used to generate the signal will look profitable. See [Quant libraries](quant-libraries.md).
- **Keep secrets and vendor data out of the repository.** API keys go in environment variables. Raw exchange or vendor files stay outside version control. See [Version control and CI](version-control-and-ci.md).

## What to leave for later

These are real skills, but they are not on the critical path for any roadmap here:

- Kubernetes and container orchestration. Docker is enough for reproducible environments.
- Rust for low-latency code. Learn C++ first; the roadmaps assume it.
- FPGA toolchains. The Quant Developer roadmap treats FPGA as a specialist track inside a firm.
- Broker-specific trading APIs before you have a strategy worth running. Paper-trade first.
