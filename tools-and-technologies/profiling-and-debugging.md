# Profiling and debugging

*Last reviewed: Oct 2026*

A performance claim without a measurement is a guess. A bug without a reproduction is a rumour. This page covers the tools for measuring speed, finding memory and concurrency errors, and stepping through a failing program.

## 1. Measure first

Before changing code, record a baseline:

- The input size and the data used.
- The build flags (`-O2` or `-O3`, with or without `-march=native`).
- The machine: CPU model, whether other programs are running, and whether frequency scaling is on.
- Several runs, with the mean and the spread, not a single number.

A speed-up that disappears on a second run is noise. A speed-up that appears only in a debug build is not real for the code you ship.

## 2. Profiling

| Tool | Use it for | Verdict |
|---|---|---|
| `perf` | Sampling the program and counting hardware events: cycles, instructions, cache misses, branch misses | The main tool on Linux. Start with `perf stat` for counters, then `perf record` and `perf report` for hotspots. Reference: the `perf` man pages and the kernel tools documentation. |
| Valgrind, Callgrind | Counting instructions and calls per function, deterministically | Slow, but repeatable. Good when `perf` results vary between runs. [Manual](https://valgrind.org/docs/manual/manual.html) |
| Valgrind, Cachegrind | Simulating cache hits and misses | Use it to test a hypothesis about data layout. It simulates the cache, so the numbers are an estimate. |
| Flame graphs | Showing where time goes across the call stack | Build them from `perf` output. They show the shape of a program's time at a glance. |

**Typical workflow for the order-book checkpoint:**

1. `perf stat -e cycles,instructions,cache-misses ./bench` to get a baseline.
2. `perf record -g ./bench` and `perf report` to find the hot function.
3. Change one thing, such as a flat array in place of a node-based map.
4. Rerun the same benchmark, and compare with the baseline.

## 3. Memory and concurrency errors

| Tool | Use it for | Verdict |
|---|---|---|
| Sanitizers | Errors found at run time with little overhead | The first tool to try. See [C++ toolchain](cpp-toolchain.md). |
| Valgrind, Memcheck | Memory errors in programs you can't rebuild | Slow. Use it when a sanitizer build isn't possible. |
| Valgrind, Helgrind | Data races and lock-order problems | Use it to cross-check ThreadSanitizer results. |

## 4. Debugging

| Tool | Use it for | Verdict | Link |
|---|---|---|---|
| GDB | Breakpoints, stepping, inspecting memory and threads | The standard debugger on Linux. Learn `break`, `run`, `bt`, `print`, `info threads` and `thread apply all bt`. | [Documentation](https://www.sourceware.org/gdb/documentation/) |
| `strace` | System calls: files, sockets, time | Use it to find unexpected I/O, such as a logger that writes on the hot path. |
| Core dumps | Post-mortem debugging | Set `ulimit -c unlimited` and inspect the core with GDB after a crash. |
| Logging | Recording what happened | Keep logging off the hot path. Buffer it, or log only on error. |

## 5. Common traps

- **Benchmarking a debug build.** Check the build type before you believe a number.
- **Dead-code elimination.** A benchmark whose result is never used may be removed by the compiler. Google Benchmark's `DoNotOptimize` guards against this.
- **Cold caches and warm-up.** The first run loads data and warms the caches. Discard the first run, or report it separately.
- **Measuring allocation as if it were compute.** Profile allocations separately from the algorithm.
- **Frequency scaling and background load.** Results on a laptop that throttles are not comparable. Note the conditions, and run the benchmark several times.
- **Optimising the wrong thing.** Profile before you optimise. The hotspot is usually not where you expect.

## 6. Learn when

| Phase | Learn |
|---|---|
| QD Phase 3 | GDB, sanitizers, `strace` |
| QD Phase 5 | `perf stat`, `perf record`, Callgrind, Cachegrind, Google Benchmark |
| QD Phase 7 | Deterministic replay and logging on the hot path |
| Any project with a speed claim | `perf stat` and a stated baseline |
