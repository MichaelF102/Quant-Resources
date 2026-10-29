# Quant Developer roadmap

*Last reviewed: Oct 2026 · Total time: ~8–10 months at 10–15 hrs/week*

A Quant Developer builds the systems everything else runs on: market data handlers, backtesters, order management and, at HFT firms, trading engines where microseconds matter. Interviews lean heavily on **C++, data structures, operating systems and performance**, far more than on stochastic calculus.

Two flavours of the role, and this roadmap covers both:

- **Low-latency / HFT developer:** C++, Linux internals, networking, hardware awareness. Phases 0–7.
- **Research platform developer** (hedge funds, banks): Python and C++, data pipelines, backtesting infrastructure. Phases 0–3, then 6–7, then the [research platform track](#research-platform-track). Lighter on Phases 4–5.

```mermaid
flowchart LR
    P0[Phase 0<br/>Tooling<br/>1–2 wks] --> P1[Phase 1<br/>Modern C++<br/>6–8 wks]
    P1 --> P2[Phase 2<br/>DSA for trading<br/>4–6 wks]
    P2 --> P3[Phase 3<br/>OS, Linux &<br/>Concurrency<br/>5–6 wks]
    P3 --> P4[Phase 4<br/>Networking<br/>3–4 wks]
    P4 --> P5[Phase 5<br/>Performance &<br/>Hardware<br/>4–5 wks]
    P5 --> P6[Phase 6<br/>Market Structure &<br/>Protocols<br/>3–4 wks]
    P6 --> P7[Phase 7<br/>Trading Systems<br/>Design<br/>4–6 wks]
    P7 --> RP[Research platform track<br/>3–4 wks]
```

Each phase lists **one primary resource** and **one backup**, then a **checkpoint** you must build before moving on.

## Time budget

| Phase | Weeks | Hours per week | Total hours (approx.) |
|---|---|---|---|
| 0 Tooling | 1–2 | 5 | 5–10 |
| 1 Modern C++ | 6–8 | 12 | 70–95 |
| 2 DSA for trading | 4–6 | 12 | 45–70 |
| 3 OS, Linux & concurrency | 5–6 | 12 | 60–70 |
| 4 Networking | 3–4 | 12 | 35–50 |
| 5 Performance & hardware | 4–5 | 12 | 45–60 |
| 6 Market structure | 3–4 | 12 | 35–50 |
| 7 Trading systems design | 4–6 | 12 | 45–70 |
| Research platform track | 3–4 | 10 | 30–40 |

LeetCode-style practice (see Phase 2) runs alongside the phases, at about 20 minutes a day.

---

## Phase 0 — Tooling 🟢 · 1–2 weeks

You'll spend most of your time in a terminal and a compiler. Set up the environment first.

- Linux (or WSL) with a shell you're comfortable in: `grep`, `find`, `strace`, `gdb`.
- `git` with a GitHub repository per project.
- A C++ toolchain: GCC or Clang with `-Wall -Wextra -Werror` as the default.
- CMake for builds. Build one project with CMake, not hand-written Makefiles.
- A unit-test framework (GoogleTest or Catch2). Write a failing test before the fix.
- `clang-tidy` or `clang-format` for consistent style.

✅ **Checkpoint:** a CMake project that builds with warnings as errors, runs one unit test, and is pushed to GitHub with a README.

---

## Phase 1 — Modern C++ 🟢→🟡 · 6–8 weeks

The non-negotiable foundation for HFT roles. Interviewers probe *why* the language works the way it does, not just syntax.

| | Resource | Verdict |
|---|---|---|
| **Primary** | [learncpp.com](https://www.learncpp.com/) 🆓 | The best free structured C++ course. Do it in order up to and including move semantics and smart pointers. |
| **Then** | Scott Meyers, *Effective Modern C++* 💸 | 42 items on C++11/14 idioms. Items on move semantics, `auto`, smart pointers and lambdas are classic interview material. |
| **Backup** | Bjarne Stroustrup, *A Tour of C++* (3rd ed.) 💸 | Short, authoritative overview if you already program in another language. |

**Must be solid on:** RAII, value versus reference semantics, copy and move constructors and the rule of five, smart pointers and their costs, template basics, `const` correctness, the STL containers and their complexity, undefined behaviour, virtual functions and the vtable cost.

**Skip for now:** template metaprogramming beyond the basics, C++20 modules and coroutines.

✅ **Checkpoint:** implement your own `vector<T>` with correct copy and move semantics, a growth strategy and iterators. Test it with a type that counts copies and moves.

---

## Phase 2 — Data structures & algorithms for trading 🟡 · 4–6 weeks

Standard interview DSA, plus the structures trading systems actually use.

| | Resource | Verdict |
|---|---|---|
| **Primary** | [NeetCode](https://neetcode.io/) and LeetCode 🆓 | Work the core patterns to medium level. Solve in C++ to build fluency. |
| **Backup** | Skiena, *The Algorithm Design Manual* 💸 | Better than CLRS for practical intuition; the "war stories" are memorable. |

**Must be solid on:** hash maps (and their worst cases), heaps, balanced trees versus sorted arrays, ring buffers, intrusive linked lists, why cache-friendly flat structures often beat theoretically faster ones.

**Trading-specific:** how a limit order book is stored. Price levels live in a map or array, with a FIFO queue per level and O(1) cancel via a hash map from order ID to node.

✅ **Checkpoint:** the core of [Project 10 — Limit order book simulator](../projects/README.md): add, cancel and match orders with price-time priority, with unit tests.

---

## Phase 3 — Operating systems, Linux & concurrency 🟡→🔴 · 5–6 weeks

| | Resource | Verdict |
|---|---|---|
| **Primary** | Arpaci-Dusseau, [*Operating Systems: Three Easy Pieces*](https://pages.cs.wisc.edu/~remzi/OSTEP/) 🆓 | Clear, free, and covers what interviews ask: processes, scheduling, virtual memory, concurrency. |
| **Primary (concurrency)** | Anthony Williams, *C++ Concurrency in Action* (2nd ed.) 💸 | The reference for `std::thread`, atomics and the memory model. Chapters 2–5 and 7 are essential. |
| **Reference** | Michael Kerrisk, *The Linux Programming Interface* 💸 | Don't read it cover to cover. Look up syscalls, signals, sockets and shared memory as needed. |

**Must be solid on:** processes versus threads, context switches and their cost, virtual memory and page faults, mutexes versus spinlocks, condition variables, `std::atomic` and memory ordering (acquire and release), false sharing, the four deadlock conditions.

**Skip for now:** kernel module development, filesystem internals.

✅ **Checkpoint:** a **lock-free single-producer single-consumer ring buffer** using `std::atomic` with acquire and release ordering. Benchmark it against a mutex-guarded `std::queue` and explain the difference.

---

## Phase 4 — Networking 🟡 · 3–4 weeks

| | Resource | Verdict |
|---|---|---|
| **Primary** | [*Beej's Guide to Network Programming*](https://beej.us/guide/bgnet/) 🆓 | Practical sockets programming in C. Short, and enough to build real things. |
| **Backup** | Kurose & Ross, *Computer Networking: A Top-Down Approach* 💸 | The theory behind TCP congestion control and routing. |

**Must be solid on:** TCP versus UDP, and why market data uses UDP multicast. Nagle's algorithm and `TCP_NODELAY`, blocking versus non-blocking I/O, `epoll`, what kernel bypass means and why firms use it.

✅ **Checkpoint:** a UDP multicast publisher and subscriber pair that sends sequenced messages and detects gaps (dropped packets) on the receiving side.

---

## Phase 5 — Performance & hardware awareness 🔴 · 4–5 weeks

This is what separates HFT developers from general software engineers.

| | Resource | Verdict |
|---|---|---|
| **Primary** | Bryant & O'Hallaron, *Computer Systems: A Programmer's Perspective* 💸. Read the chapters on program optimisation, the memory hierarchy, and virtual memory. | Optimising programs from the programmer's side. |
| **Primary (talks)** | Carl Cook, *When a Microsecond Is an Eternity* (CppCon 2017) 🆓 | The best introduction to how HFT C++ is actually written. Watch it twice. |
| **Talk** | David Gross, *Trading at Light Speed* (CppCon 2022) 🆓 | Low-latency design patterns from a practitioner. |
| **Reference** | Ulrich Drepper, *What Every Programmer Should Know About Memory* 🆓 | Dense. Read the cache sections. |
| **Reference** | [Agner Fog's optimisation manuals](https://www.agner.org/optimize/) 🆓 | For instruction latencies and microarchitecture details. |
| **Tooling** | [Google Benchmark](https://github.com/google/benchmark) 🆓 | Use it for every timing claim. Read its guidance on avoiding dead-code elimination and measurement noise. |

**Must be solid on:** cache lines, locality and prefetching, branch prediction and why branchless code can win, heap allocation costs (and avoiding allocation on the hot path), inlining, measuring with `perf`, and benchmarking without fooling yourself.

**Skip for now:** FPGA development. It's a specialist track, worth exploring once you're inside a firm that uses it.

✅ **Checkpoint:** profile your order book from Phase 2 with `perf`. Make it at least 2× faster through data layout changes (for example arrays instead of node-based maps, or object pools), and document each change with before and after benchmarks.

---

## Phase 6 — Market structure & exchange protocols 🟡 · 3–4 weeks

You can't build a trading system without understanding what it trades on.

| | Resource | Verdict |
|---|---|---|
| **Primary** | Larry Harris, *Trading and Exchanges* 💸 | The standard text on how markets work: order types, market makers, liquidity. Read parts I–III. |
| **Spec** | Nasdaq TotalView-ITCH specification 🆓 (search the Nasdaq Trader technical specifications; confirm the version you use) | A real binary market-data protocol. Short and readable. |
| **Spec** | [FIX Trading Community](https://www.fixtrading.org/) 🆓 | The order-entry protocol most firms use. Learn message structure and the session layer. |
| **Backup** | NSE's published circulars on co-location and trading systems 🆓 | India-specific context on how the exchange operates. |

**Must be solid on:** order types (limit, market, IOC, FOK), price-time priority, maker and taker fees, tick sizes, auction phases, and how a market data feed reconstructs the book from add, modify and delete messages.

✅ **Checkpoint:** an ITCH 5.0 parser that reads a sample file, reconstructs the order book for one symbol, and prints top-of-book at intervals. Measure messages per second.

---

## Phase 7 — Trading systems design 🔴 · 4–6 weeks

Bringing it together: how the components of a trading stack fit.

| | Resource | Verdict |
|---|---|---|
| **Primary** | Build it: an end-to-end event-driven backtester 🆓 | Nothing teaches system design faster than building one and hitting its limits. |
| **Backup** | Martin Kleppmann, *Designing Data-Intensive Applications* 💸 | For research-platform roles: storage, streaming and pipelines. Chapters 3, 5 and 11. |

**Must be solid on:** event-driven architecture, the path from market data to strategy to risk checks to order gateway, why backtest and live code should share logic, pre-trade risk controls, logging without slowing the hot path, deterministic replay for debugging.

✅ **Checkpoint:** [Project 03 — Honest backtester](../projects/03-honest-backtester/), then extend it into an event-driven design where the same strategy class runs against historical replay or a simulated live feed.

---

## Research platform track

For hedge fund and bank research-platform roles, add this track after Phase 7. It replaces Phases 4 and 5 for those roles.

| | Resource | Verdict |
|---|---|---|
| **Primary (SQL)** | [PostgreSQL documentation](https://www.postgresql.org/docs/) 🆓 | Read the SQL tutorial and the sections on joins, window functions and indexes. Use it with a local database and a real dataset. |
| **Backup (pipelines)** | Kleppmann, *Designing Data-Intensive Applications* 💸, chapters 10–11 | Batch and stream processing, and why reproducibility matters. |
| **Python packaging** | Official Python packaging guide 🆓 | Package your backtester so another person can install and run it without editing code. |

**Must be solid on:** writing non-trivial SQL joins and window functions, versioning datasets, designing an idempotent data pipeline, storing results so they can be reproduced.

✅ **Checkpoint:** a daily data pipeline that loads raw bhavcopy files into a database, applies corporate actions, and produces a table that [Project 03](../projects/03-honest-backtester/) can read. Rerunning it produces identical output.

---

## Interview focus for QD roles

- **C++ deep dives:** "What happens when you call `push_back` on a full vector?", "Why might `virtual` be slow?", "Explain `std::move`. What does it actually do?"
- **Systems:** "What happens between a packet arriving at the NIC and your code seeing it?", "How would you avoid allocations in a hot loop?"
- **Design:** "Design an order book", "Design a market data handler that never drops messages".
- **Coding:** LeetCode-medium under time pressure, in C++.
- **Some probability:** less than QR or QT roles, but expect a few questions from the [probability set](../interview/probability.md).

## Portfolio checklist

By the end you should have, on GitHub, with READMEs and benchmarks:

- [ ] Custom `vector<T>` with tests
- [ ] Limit order book with price-time priority, profiled and optimised
- [ ] Lock-free SPSC queue with benchmarks
- [ ] ITCH parser reconstructing a real book
- [ ] Event-driven backtester
- [ ] (Research track) Data pipeline with reproducible output

## Other paths

[Quant Researcher](quant-researcher.md), [Quant Trader](quant-trader.md), [Risk and Model Validation](risk-model-validation.md). See the [roadmap index](README.md) to compare them.
