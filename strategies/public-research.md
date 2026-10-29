# Public research

*Last reviewed: Oct 2026*

Free datasets and public research to start from. Each entry says what it is, what it is for, and its status when checked. Read each source's terms before redistributing data.

## Datasets

| Source | What it is | Use it for | Checked | Link |
|---|---|---|---|---|
| AQR datasets | Factor and style return series, including momentum and betting against beta | Checking a factor implementation against a published series | 2026-10-29 | [aqr.com/Insights/Datasets](https://www.aqr.com/Insights/Datasets) |
| AQR Funds | Fund performance and research links | Reading published research alongside performance data | 2026-10-29 | [funds.aqr.com](https://funds.aqr.com/) |
| Kenneth French Data Library | US and international factor returns, including developed and emerging markets | The reference series for factor work | 2026-10-29 | [Data library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) |
| FRED and ALFRED | US macro series, with vintage data in ALFRED | Macro signals without look-ahead | 2026-10-29 | [FRED](https://fred.stlouisfed.org/), [ALFRED](https://alfred.stlouisfed.org/) |
| CBOE VIX history | Daily implied volatility of the S&P 500, from 1990 | Benchmark for volatility strategies | 2026-10-29 | [CBOE](https://www.cboe.com/tradable-products/vix/vix-historical-data/) |

For Indian data, see [data sources](../data/data-sources.md).

## Firm research

| Source | What it offers | Checked | Note |
|---|---|---|---|
| [Man Group](https://www.man.com/) | Corporate site and alternative investment research | 2026-10-29 | The homepage does not mention AHL. Check Man's pages for AHL research before citing it |
| [Two Sigma](https://www.twosigma.com/) | Corporate site describing quantitative research | 2026-10-29 | Public research pages should be checked for current papers |
| [Jane Street](https://www.janestreet.com/) | Corporate site with a research-driven description and a view on machine learning in trading | 2026-10-29 | The site is a starting point for understanding the firm, not a source of strategy detail |

## Academic papers

Papers cited in the strategy files are listed with full citations in [papers](../resources/papers.md). The most useful starting set for this folder:

- Jegadeesh and Titman (1993): cross-sectional momentum.
- Moskowitz, Ooi and Pedersen (2012): time-series momentum.
- Asness, Moskowitz and Pedersen (2013): value and momentum across markets.
- Fama and French (2015): the five-factor model.
- Gu, Kelly and Xiu (2020): machine learning for asset pricing.
- DeMiguel, Garlappi and Uppal (2009): why 1/N is hard to beat.
- Almgren and Chriss (2000): optimal execution.
- Avellaneda and Stoikov (2008): market making.

## How to use these sources

- Start with the dataset to check an implementation. A factor you cannot reproduce on the published series is a bug in your code or in your data.
- Read a paper's data and sample period before comparing its results with yours.
- Treat firm research as a description of the firm's views, not as a tested strategy. Test any idea yourself with the [evaluation framework](evaluation-framework.md).
