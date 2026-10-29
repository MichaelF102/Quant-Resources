# 10 — Limit order book simulator (C++)

**Proves:** a matching engine with price-time priority, order-book data structures with constant-time cancellation, deterministic replay, and measurement of latency and throughput
**Level:** 🔴 · **Time:** 3–4 weekends
**Prerequisites:** [QD roadmap](../../roadmaps/quant-developer.md) Phases 1–3 (C++, data structures, concurrency); [C++ toolchain](../../tools-and-technologies/cpp-toolchain.md); [Profiling and debugging](../../tools-and-technologies/profiling-and-debugging.md)

## Goal

Build a limit order book and matching engine in C++ that accepts limit and market orders, cancels and replaces orders, and matches incoming orders by price-time priority. Drive it from a replayable stream of events, and measure its throughput. The question: what data structures make a matching engine fast and correct, and where does the time go when it runs?

## Data

- **Synthetic:** a generator that produces add, cancel and execute events with a configurable arrival rate and price distribution. Use a fixed random seed, and save the event file so every run is identical.
- **Real (optional):** a sample of LOBSTER data, as described in [data sources](../../data/data-sources.md). Check its license before using it in a public repository.

## Steps

1. **Define the order and event types.** Use fixed-width integers for prices (ticks) and quantities. Keep the order struct small.
2. **Build the book.** Store price levels in a sorted structure, with a FIFO queue at each level. Keep a hash map from order ID to its node, so a cancel is constant time.
3. **Implement matching.** A marketable limit order matches against the best opposite levels in price-time order. Partially filled orders keep their place in the queue.
4. **Implement cancel and replace.** A replace that changes the price loses time priority; a replace that only reduces quantity keeps it. Test both cases.
5. **Replay.** Read the event file, apply each event, and write the resulting trades to an output file. Two runs on the same file must produce identical output.
6. **Test.** Unit tests for each event type, and a property test that checks the total quantity in the book after random sequences of events.
7. **Measure.** Report events per second and the latency distribution (median, 99th percentile) on one machine, with the build flags and the hardware stated.
8. **Profile.** Run `perf` on the replay and report the top three functions by time.

## Done when

- [ ] Price-time priority is tested, including partial fills and replace behaviour
- [ ] Cancel is constant time in the number of orders at a level, and this is stated and tested
- [ ] Replay of the same event file produces byte-identical output across runs
- [ ] Sanitizer build (ASan and UBSan) passes the test suite, with no reports
- [ ] Throughput and latency percentiles are reported, with build flags and hardware
- [ ] A profile shows the top hotspots, and the write-up says which one you would change first

## Common pitfalls

- **Using floating-point prices.** Comparing prices as floats causes missed matches. Use integer ticks.
- **Losing time priority on quantity reduction.** Reducing the size of a resting order keeps its place in the queue. Moving it to the back of the queue is a bug.
- **Node allocation on the hot path.** Each new order allocating a node makes latency unpredictable. Measure it, then consider an object pool.
- **Unstable iteration order.** A hash map's iteration order can change between runs and break replay. Do not iterate over it to produce output.
- **Benchmarking a debug build.** Check the build type before recording any number.

## Stretch goals

- Add a multicast market-data publisher that emits the book's top-of-book changes, and a subscriber that rebuilds the book from them and detects gaps.
- Replace the price-level map with a flat array indexed by tick, and compare throughput.
- Add a pre-trade risk check (maximum order size and position) and measure its cost on the hot path.

## Further reading

- Harris, *Trading and Exchanges* 💸, on order types and priority rules.
- Cook, "When a Microsecond Is an Eternity" (CppCon 2017), and Gross, "Trading at Light Speed" (CppCon 2022), both named in the [QD roadmap](../../roadmaps/quant-developer.md).
- Nasdaq TotalView-ITCH specification, for the message semantics used in the real-data stretch goal.
