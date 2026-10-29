# Version control and CI

*Last reviewed: Oct 2026*

Version control records what changed, when, and why. For this program it also makes your work reviewable, since a portfolio of projects is only useful if others can read and rerun it. This page covers the git workflow, the automated checks that run on every change, and the rules for keeping secrets and vendor data out of the repository.

## 1. Git

Learn git well enough to recover from mistakes. The [Pro Git book](https://git-scm.com/book/en/v2) is free and covers everything below.

**Core commands:** `status`, `diff`, `add`, `commit`, `log`, `restore`, `branch`, `switch`, `merge`, `rebase`, `stash`, `reflog`.

**Workflow for a project:**

1. Create a branch for each piece of work: `git switch -c add-garch-forecast`.
2. Make small commits, each with one purpose.
3. Write a commit message in the imperative mood, with a short subject line, for example `Add block bootstrap for Sharpe confidence intervals`.
4. Push the branch and open a pull request, even if you're the only reviewer. Reading your own diff catches mistakes.
5. Merge when the checks pass.

**Recovering:** `git reflog` lists every state the repository has been in. Almost nothing is lost permanently once it has been committed.

## 2. What to commit

| Commit | Do not commit |
|---|---|
| Source code and tests | Raw vendor data or exchange archives |
| Configuration and lock files (`pyproject.toml`, `uv.lock`, `requirements.txt`, `CMakePresets.json`) | Virtual environments |
| READMEs and results summaries | Build outputs and binaries |
| Small sample data you have the right to share | API keys, passwords, tokens |

Add the ignored paths to `.gitignore` before the first commit. If a secret is committed by mistake, treat it as leaked: revoke it, then remove it from history.

## 3. Secrets

Broker API keys, database passwords and tokens belong in environment variables or a local file that is ignored by git.

```
export KITE_API_KEY=...   # set in your shell, never in code
```

Read them with `os.environ` (Python) or `getenv` (C++). Include a `.env.example` file with the variable names but no values.

## 4. Continuous integration with GitHub Actions

GitHub Actions runs a workflow on each push or pull request. This repository already uses one for link checking. Add one per project for tests.

A minimal Python workflow:

1. Check out the code.
2. Set up the Python version the project pins.
3. Install the locked dependencies.
4. Run `pytest`.

A C++ workflow adds a CMake configure and build, then `ctest`, and ideally one sanitizer job.

Reference: [GitHub Actions documentation](https://docs.github.com/en/actions).

**Keep CI fast.** A run that takes ten minutes gets ignored. Put slow benchmarks in a separate, manually triggered job.

## 5. Pre-commit hooks

[pre-commit](https://pre-commit.com/) runs checks on your machine before a commit is made. Use it for formatting, linting and trailing-whitespace fixes, so CI doesn't fail on style.

Configure hooks in a `.pre-commit-config.yaml` file, install them once with `pre-commit install`, and run them on all files with `pre-commit run --all-files`.

## 6. Reproducibility checklist for each project

- [ ] Repository has a README with the command to reproduce the main result
- [ ] Dependencies are pinned and committed
- [ ] Data source, download date and adjustments are recorded (see [data sources](../data/data-sources.md))
- [ ] Random seeds are fixed and documented
- [ ] CI runs the tests on each push
- [ ] No secrets or raw vendor data are in the history

## 7. Learn when

| Phase | Learn |
|---|---|
| QR Phase 0 | git basics, branches, `.gitignore`, the first pull request |
| QR Phase 5 | CI for tests, pre-commit hooks |
| QD Phase 0 | Same, plus CMake in CI |
| QD research track | Reproducible pipelines and pinned environments |
| Risk Phase 7 | Versioned validation documents and reproducibility records |
