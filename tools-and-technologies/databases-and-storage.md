# Databases and storage

*Last reviewed: Oct 2026*

A backtest reads the same data many times, and a data pipeline writes it every day. Storing that data well — in a format that is fast to read, a database that answers questions quickly, and a load process that can be rerun safely — saves more time than most modelling choices. This page covers the options, the trade-offs, and the rules for loading data correctly.

## 1. Choosing a store

| Option | Use it for | Verdict | Link |
|---|---|---|---|
| CSV | Small files you inspect by hand, and exchanging data | Easy to read, slow, and loses types (dates, precision). Fine for a single day's bhavcopy; avoid it for years of history. | — |
| Parquet | Columnar files for analysis: years of daily bars, option chains | Compact, typed, and fast to read a few columns. The default for analytical files. | [Apache Arrow](https://arrow.apache.org/docs/python/) |
| DuckDB | Querying Parquet and CSV files with SQL, on one machine | Embedded and fast for analysis. Reads Parquet directly, so you rarely need to load data first. Good for the research track. | [Docs](https://duckdb.org/docs/) |
| PostgreSQL | Shared, multi-user storage with transactions and constraints | The reliable choice for a pipeline that other people or programs use. Heavier to run than DuckDB. | [Documentation](https://www.postgresql.org/docs/) |
| SQLite | Small local databases and tests | Simple and built into Python. Not for large analytics. |

**A practical rule:** store raw files as they arrived, convert them to Parquet for analysis, and use PostgreSQL when more than one program needs to write to the same data.

## 2. SQL that you'll use

For the research track and for DuckDB or PostgreSQL work, learn:

- `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, and `ORDER BY`.
- Joins: `INNER`, `LEFT`, and how a join multiplies rows when the key is not unique. Check row counts before and after every join.
- Window functions: `ROW_NUMBER`, `LAG`, `LEAD`, and `AVG(...) OVER (ORDER BY date ROWS BETWEEN ...)`. These compute returns, rolling means and rank-based signals.
- Indexes: what they speed up (lookups on the indexed column) and what they cost (slower writes).
- Transactions: a load that fails halfway should roll back.

Read the relevant PostgreSQL documentation sections when you need them; they are thorough and current.

## 3. Schema and types

- **Dates and times.** Store timestamps with a time zone (`timestamptz` in PostgreSQL, or UTC in Parquet). Keep trading dates separate from timestamps, since a session date and a bar timestamp are different things.
- **Prices.** Use decimal types for prices in a database, or a fixed number of decimal places in Parquet. Binary floats cause small rounding differences that accumulate in P&L.
- **Identifiers.** Keep a symbol-mapping table with valid-from and valid-to dates. Symbols change, merge and reuse names. See [data sources](../data/data-sources.md).
- **Corporate actions.** Store them in their own table, with the adjustment factor, so the adjustment can be recomputed and audited.

## 4. Loading data safely

A load job will be rerun, so it must be **idempotent**: rerunning it with the same input produces the same output, with no duplicates.

Three patterns that achieve this:

1. **Overwrite a partition.** Write each date to its own file or partition, and overwrite that partition on rerun.
2. **Upsert on a key.** In PostgreSQL, `INSERT ... ON CONFLICT (symbol, trade_date) DO UPDATE` keeps one row per key.
3. **Load to staging, then swap.** Load to a temporary table, validate it, then replace the target in one transaction.

Validate before publishing:

- Row count against the expected number of symbols and trading days.
- No duplicate keys.
- No prices that are zero, negative, or far outside the previous day's range without a corporate action.
- Dates are trading days, and no weekend or holiday rows are present unless the source includes them.

## 5. Scale and performance

- Store by date partition, so a query for one month reads only those files.
- Keep the columns you query most in the front of the schema and in the sort order.
- Measure before indexing. A full scan of a well-partitioned Parquet directory is often faster than an index on a small table.
- Use `EXPLAIN` in PostgreSQL and `EXPLAIN ANALYZE` to see the plan before tuning.

## 6. Checklist for the data pipeline checkpoint

- [ ] Raw files are stored unchanged, with a manifest (source, date, checksum)
- [ ] Analysis data is in Parquet or a database, typed, with UTC timestamps
- [ ] Load is idempotent: rerun gives identical output
- [ ] Validation checks run before the data is published
- [ ] Corporate actions and symbol changes are in their own tables
- [ ] A query reproduces a number from the Project 03 backtester

## 7. Learn when

| Phase | Learn |
|---|---|
| QR Phase 3 | CSV and Parquet, DuckDB for queries over Parquet |
| QR Phase 5 | Window functions for signal construction |
| QD research track | PostgreSQL, joins, transactions, idempotent loads |
| Risk Phases 3–4 | Storing VaR and exposure results with their inputs |
