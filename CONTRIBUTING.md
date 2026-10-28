# Contributing

This repo stays useful only if it stays curated. Every addition must earn its place.

## Adding a resource

Open a pull request that adds the resource to the most relevant section using this format:

```markdown
| Resource name with [link](https://full-url.com) 🆓/💸 | One-line verdict: why it's worth time, and the best chapters or parts |
```

Your PR **must** include:

- [ ] A full, visible URL (no link shorteners such as `lnkd.in` or `bit.ly`)
- [ ] A verdict explaining what it's good for and who it's for
- [ ] A difficulty level (🟢 / 🟡 / 🔴) and cost tag (🆓 / 💸)
- [ ] Which existing resource it beats, or what gap it fills

PRs that only add links without verdicts will be closed.

## Adding a project

Use the spec template in [projects/README.md](projects/README.md). Starter code should:

- Run with `pip install` of listed packages and one command
- Use synthetic or freely downloadable data
- Not include vendor data files in the repo

## Fixing a dead link

Open a [dead-link issue](../../issues/new?template=dead-link.md) or a PR with the replacement.

## Style

- British or American spelling is fine — be consistent within a file.
- Prefer one strong recommendation over five weak ones.
- Update the "Last reviewed" date on any page you substantially change.
