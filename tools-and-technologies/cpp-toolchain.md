# C++ toolchain

*Last reviewed: Oct 2026*

The C++ toolchain is the set of compilers, build tools, checkers and test frameworks used to build and test low-latency code. The [Quant Developer roadmap](../roadmaps/quant-developer.md) assumes it from Phase 0 onward.

## 1. Compilers

| Compiler | Verdict | Notes |
|---|---|---|
| GCC | Default on most Linux systems. Good diagnostics and wide support. | Use `g++` with `-std=c++20` (or the standard you target). |
| Clang | Clear diagnostics, good sanitizer and tooling support, and the same tools (clang-tidy, clang-format) used across the industry. | Use it as a second compiler to catch warnings GCC misses. |

Build with both, at least occasionally. A warning that appears in only one is worth reading.

**Warning flags to use by default:**

```
-Wall -Wextra -Wpedantic -Werror
```

`-Werror` turns warnings into errors, so the build fails when a warning appears. Keep it on from the first commit. Fixing warnings later is much harder.

**Optimisation levels:** use `-O2 -g` for benchmarks, so the code is optimised and still has debug symbols for profiling. Use `-O0 -g` when debugging.

## 2. Build system: CMake

CMake generates build files for make, Ninja and IDEs. Learn it once, and use it for every project.

- Use `CMakePresets.json` to store configurations for debug, release, and sanitizer builds, so a build is one command.
- Set the C++ standard with `target_compile_features`, not global flags.
- Put tests in a separate target, and run them with `ctest`.
- Use `FetchContent` or a package manager to pull in GoogleTest or Catch2, so the project builds on a clean machine.

Reference: [CMake documentation](https://cmake.org/documentation/).

## 3. Sanitizers

Sanitizers instrument the compiled code to find bugs at run time. They are the fastest way to find undefined behaviour and data races.

| Sanitizer | Finds | Flag | Notes |
|---|---|---|---|
| AddressSanitizer (ASan) | Out-of-bounds access, use after free, leaks | `-fsanitize=address` | Run the test suite under it regularly. |
| UndefinedBehaviorSanitizer (UBSan) | Signed overflow, misaligned access, bad shifts | `-fsanitize=undefined` | Combine with ASan in one build. |
| ThreadSanitizer (TSan) | Data races | `-fsanitize=thread` | Must be a separate build; it does not combine with ASan. |
| MemorySanitizer (MSan) | Reads of uninitialised memory | `-fsanitize=memory` | Clang only, and needs an instrumented standard library. |

Reference: [google/sanitizers wiki](https://github.com/google/sanitizers/wiki).

**Use TSan on the SPSC ring buffer from [Quant Developer Phase 3](../roadmaps/quant-developer.md).** It catches races that tests pass by chance.

## 4. Static analysis and formatting

| Tool | Use it for | Verdict |
|---|---|---|
| clang-tidy | Checks for bugs, performance issues and modern-C++ style | Run it in CI. Turn on a small set of checks at first, and add more as the code matures. [Docs](https://clang.llvm.org/extra/clang-tidy/) |
| clang-format | Consistent layout | Settle on one style, commit a `.clang-format` file, and format before each commit. [Docs](https://clang.llvm.org/docs/ClangFormat.html) |
| Compiler Explorer | Seeing the assembly for a line of code | Use it to check whether an inline function or a branch is what you think. [godbolt.org](https://godbolt.org/) |

## 5. Unit tests and benchmarks

| Tool | Use it for | Verdict | Link |
|---|---|---|---|
| GoogleTest | Unit tests, with mocks | Widely used in industry. A safe default. | [User's guide](https://google.github.io/googletest/) |
| Catch2 | Unit tests with a lighter syntax | Good for small projects and for learning. | [Repository](https://github.com/catchorg/Catch2) |
| Google Benchmark | Timing functions and comparing versions | Use it for every timing claim. It guards against dead-code elimination and reports variance. | [Repository](https://github.com/google/benchmark) |

Pick one test framework and use it throughout. GoogleTest is the more common choice in the industry; Catch2 is the easier starting point.

## 6. Reference

- [cppreference.com](https://cppreference.com/): the standard library reference. Check the behaviour of `std::vector` growth, move semantics and atomics here before relying on memory.
- Compiler Explorer, as above, for the assembly.

## 7. Setup checklist

- [ ] CMake project builds with `-Wall -Wextra -Wpedantic -Werror`
- [ ] Debug, release and sanitizer presets in `CMakePresets.json`
- [ ] One unit test runs under ASan and UBSan
- [ ] clang-format and clang-tidy run on the project
- [ ] A benchmark uses Google Benchmark and reports variance

## 8. Learn when

| Phase | Learn |
|---|---|
| QD Phase 0 | Compiler flags, CMake, GoogleTest, clang-format |
| QD Phase 1 | Compiler Explorer, cppreference |
| QD Phase 2 | Sanitizers on data-structure code |
| QD Phase 3 | ThreadSanitizer on the lock-free queue |
| QD Phase 5 | Google Benchmark, release-mode flags, clang-tidy performance checks |
