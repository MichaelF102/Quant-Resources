# C++ quick reference

*Last reviewed: Oct 2026*

A compact reference for the C++ facts that come up in the [Quant Developer roadmap](../roadmaps/quant-developer.md) and its interviews. It assumes C++17 or C++20. Check the exact behaviour in [cppreference.com](https://cppreference.com/) before relying on a detail.

## 1. Value categories and moves

- An **lvalue** has a name and an address. An **rvalue** is a temporary or an expression that has no name.
- `std::move` does not move anything. It casts its argument to an rvalue reference, which allows a move constructor or move assignment to run.
- A moved-from object must remain valid but may be in an unspecified state. Do not read it after a move, except to assign to it or destroy it.
- The **rule of five**: if you define a destructor, copy constructor, copy assignment, move constructor or move assignment, consider defining all five. If you need none of them, follow the **rule of zero** and use standard containers and smart pointers.
- Mark move constructors `noexcept` where possible. `std::vector` only uses a move constructor during reallocation if it is `noexcept`, or if no copy constructor is available.

## 2. Smart pointers

| Type | Ownership | Cost |
|---|---|---|
| `std::unique_ptr<T>` | Exclusive | Same as a raw pointer |
| `std::shared_ptr<T>` | Shared, via a reference count | Atomic increment and decrement; a control block allocation |
| `std::weak_ptr<T>` | Non-owning view of a `shared_ptr` | Does not keep the object alive |

- Create with `std::make_unique` and `std::make_shared`. `make_shared` allocates the object and its control block together.
- Avoid `shared_ptr` on hot paths. Its atomic reference count costs time even without contention.

## 3. Containers and complexity

| Container | Access | Insert or erase | Notes |
|---|---|---|---|
| `std::vector` | O(1) by index | O(1) amortised at the back; O(n) elsewhere | Contiguous; cache-friendly |
| `std::deque` | O(1) by index | O(1) at both ends | Not contiguous |
| `std::list` | O(n) | O(1) given an iterator | Poor cache behaviour |
| `std::map` / `std::set` | O(log n) | O(log n) | Balanced tree; ordered |
| `std::unordered_map` / `unordered_set` | O(1) average, O(n) worst | O(1) average | Iteration order is unspecified and can change |
| `std::priority_queue` | Top O(1) | O(log n) push and pop | Adapter over a vector |

For a limit order book, a sorted array of price levels or a flat array indexed by tick often beats `std::map` in practice, because of locality. Measure before choosing.

**Growth:** `std::vector` grows geometrically. `reserve` avoids reallocations when you know the size.

## 4. Undefined behaviour to recognise

- Signed integer overflow. Use unsigned types or checked arithmetic where wraparound matters.
- Use after free, and dangling references to temporaries or to elements after a reallocation.
- Out-of-bounds access through `operator[]`. Use `at()` in debug builds.
- Data races: two threads accessing the same non-atomic variable, with at least one write.
- Reading an uninitialised variable.

Run sanitizers (see [C++ toolchain](../tools-and-technologies/cpp-toolchain.md)) to catch most of these.

## 5. Virtual functions

- A virtual call is an indirect call through the vtable. The cost is usually small, but it blocks inlining.
- On a hot path, prefer templates or a concrete type over virtual dispatch, and measure the difference.
- Make a base class destructor `virtual` if objects are deleted through a base pointer.

## 6. Atomics and memory orders

| Order | Guarantee | Typical use |
|---|---|---|
| `relaxed` | Atomicity only, no ordering | Counters where order does not matter |
| `acquire` | Later reads and writes are not reordered before this load | Reading a published value |
| `release` | Earlier reads and writes are not reordered after this store | Publishing a value |
| `acq_rel` | Both, for read-modify-write | Lock-free updates |
| `seq_cst` | A single total order over all such operations | The default; the safest and the slowest |

A single-producer single-consumer queue needs one release store on the producer side and one acquire load on the consumer side. Test it with ThreadSanitizer.

## 7. Threads and locks

- `std::mutex` with `std::lock_guard` or `std::unique_lock` for scoped locking.
- `std::condition_variable` waits must be in a loop that rechecks the condition, because of spurious wakeups.
- Lock ordering: acquire locks in the same order everywhere to avoid deadlock.
- False sharing: two threads writing to different variables on the same cache line slow each other down. Pad hot per-thread variables to a cache-line size (typically 64 bytes).

## 8. Templates and constness

- `const` on a member function means it does not modify the object. Use it on every getter.
- `constexpr` evaluates at compile time when possible. Use it for constants and small pure functions.
- `auto` deduces the type. Use `const auto&` to avoid copies in range-based loops.
- `static_assert` checks a condition at compile time, with a message.

## 9. Allocation on the hot path

- Allocating memory on a hot path adds latency that varies unpredictably.
- Preallocate buffers and containers before the loop, and `reserve` vectors.
- Object pools reuse memory for orders or messages.
- Check with a profiler that allocation does not appear in the hot function.

## 10. Build flags that change behaviour

- `-O0` for debugging. `-O2` or `-O3` for benchmarks and releases.
- `-march=native` lets the compiler use the instruction set of the build machine. The binary may not run elsewhere.
- `-ffast-math` allows reassociation of floating-point operations. Results change, sometimes in ways that break comparisons.
- `-fno-exceptions` and `-fno-rtti` reduce overhead, but they are not compatible with all libraries.

## 11. Interview favourites

- What does `std::move` actually do? It casts to an rvalue reference. The move happens only if a move constructor or move assignment is then called.
- What happens when you call `push_back` on a full vector? It allocates a larger buffer, moves or copies the elements, and frees the old buffer. Pointers and iterators are invalidated.
- Why might `virtual` be slow? An indirect call through the vtable prevents inlining and can miss the branch predictor.
- Why is `std::shared_ptr` expensive on a hot path? Its reference count uses atomic operations on every copy.
- Explain `acquire` and `release`. A release store makes earlier writes visible to a thread that performs an acquire load of the same variable.
