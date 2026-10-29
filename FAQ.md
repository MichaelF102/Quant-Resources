# Frequently asked questions

*Last reviewed: Oct 2026*

## Which roadmap should I start with?

Start with the Quant Researcher roadmap, Phase 1. Probability and statistics are shared by every role, so the first months are useful whichever path you choose. Use the [roadmap comparison](roadmaps/README.md) to decide when you have finished Phase 1.

If you already know that you want to build systems, start the Quant Developer roadmap at Phase 0 instead, and work on probability in parallel from Phase 2.

## How long will it take?

The roadmaps are built for 10–15 hours a week. Each one lists a time budget per phase. Expect roughly 6 to 10 months for a single roadmap, depending on your starting point. Phases that you already know well can be shorter; the checkpoint projects do not get shorter.

## Do I need a maths or computer science degree?

No, but you need the material the roadmaps name. Calculus, linear algebra and probability are used throughout. For the developer track, you need a working knowledge of programming and a willingness to learn C++ in depth. The roadmaps say what to skip for now.

## What should I install first?

Follow the setup order in [Tools and technologies](tools-and-technologies/README.md): a shell, git and a remote, a Python environment, and then the C++ toolchain if you are on the developer track. Do not install a stack for a phase that has not started.

## Can I do this without paying for books?

Yes, for the first phases. Several recommended resources are free: the MIT OpenCourseWare courses, *An Introduction to Statistical Learning*, *Operating Systems: Three Easy Pieces*, learncpp.com, and the Forecasting text. The [books list](resources/books.md) marks which resources are free and which are paid. Paid books are useful for specific phases, but the checkpoint projects do not depend on them.

## Do I need real market data?

Most projects work on synthetic data or on public Indian end-of-day files. The [data sources](data/data-sources.md) page lists where to get each dataset and what its caveats are. Do not use vendor data that you are not licensed to use, and do not commit it to a repository.

## How do I know I have finished a phase?

Build the checkpoint project for that phase. A phase is finished when its checkpoint is built and you can explain its results, including what failed. The "done when" checklist in each project tells you what to verify.

## Are the projects graded?

No. The done-when checklists are for you to check your own work. If you publish a project, the checklist is what a reviewer will look for.

## What if a result I get does not match the textbook?

Check the conventions first: continuous or simple rates, per-period or annualised units, and calendar or trading days. Then check the data for corporate actions and look-ahead. The [pitfalls](pitfalls.md) page lists the usual causes.

## How do I get interview-ready?

Work the [interview problem sets](interview/README.md) daily from Phase 2 of your roadmap. Solve each problem for at least ten minutes before opening the solution, and say your reasoning out loud. Use the [careers page](careers/india.md) for the firms that hire in India, and the [Indian markets guide](careers/india-markets.md) for the market context.

## How can I contribute?

Read [CONTRIBUTING.md](CONTRIBUTING.md). Every resource needs a verdict, a difficulty level and a cost tag. Projects use the [spec template](projects/TEMPLATE.md). Changes that add links need a working URL, so please check it before opening a pull request.

## Where do I report a broken link?

Use the dead-link issue template, or open a pull request with the replacement. A scheduled workflow also checks every Markdown link each week.
