# Technical indicators cheat sheet

*Last reviewed: Oct 2026*

Notation: C_t close, H_t high, L_t low, V_t volume, N lookback length, α smoothing factor.

Each indicator lists its definition, default parameters, typical use, and a verdict. The verdict is a view on whether the indicator has earned a place in research, not a recommendation to trade it. **Every rule built on these indicators should be tested with [Project 15](../projects/15-technical-indicator-study/), using the honest backtester from [Project 03](../projects/03-honest-backtester/), with costs and out-of-sample evaluation.**

## 1. Notation and conventions

- Exponential smoothing: EMA_t = α C_t + (1 − α) EMA_(t−1). Use α = 2/(N + 1) for the usual EMA convention.
- Wilder smoothing: α = 1/N. It is slower than the standard EMA with the same N, so the two are not interchangeable.
- The first value of a smoothed series needs a seed, usually a simple average over the first N bars. Results depend on the seed for the first few multiples of N, so discard a warm-up period.

## 2. Trend indicators

### Simple moving average (SMA)

SMA_N = (1/N) Σ C_(t−i), i = 0 to N − 1

- Default: N = 20, 50, 200.
- Use: smoothing; trend direction; crossovers.
- Verdict: a smoothing device, not a signal. Crossover rules have been tested extensively and their historical results are sensitive to the sample period and to costs.
- Caveat: SMA lags price by about (N − 1)/2 bars. Crossovers therefore react late.

### Exponential moving average (EMA)

See the smoothing convention in Section 1.

- Default: N = 12, 26, 50.
- Verdict: same as SMA with less lag and more noise. Parameter choices are easily overfit.

### MACD

MACD = EMA₁₂ − EMA₂₆; signal = EMA₉ of MACD; histogram = MACD − signal.

- Use: trend momentum; signal-line crossovers.
- Verdict: a combination of two EMAs with a smoother. Adds parameters without adding information beyond the EMAs. Test it only as a benchmark for EMA crossover rules.
- Caveat: the 12/26/9 defaults were chosen decades ago for different markets. Check whether any choice is robust.

### Parabolic SAR

Trailing stop that accelerates towards price as a trend persists. Output is a stop level, not a directional signal.

- Verdict: a stop-loss rule. Its value depends on the exit logic, which needs its own test. Trailing stops in backtests often look better than they are, because they condition on the path of prices that was already observed.

### ADX and directional indicators

ADX measures trend strength from directional movement (+DI, −DI), using Wilder smoothing over N = 14.

- Verdict: useful as a filter for regime classification. Avoid using it to predict direction by itself.

### Ichimoku cloud

Tenkan = (max H + min L) over 9 bars; Kijun = same over 26 bars; Senkou A = (Tenkan + Kijun)/2 shifted 26 bars forward; Senkou B = (max H + min L) over 52 bars shifted 26 bars forward; Chikou = close shifted 26 bars back.

- Verdict: a bundle of trend and support measures with many parameters. The forward shifts mean the cloud is partly plotted in the future, so a naive backtest can introduce look-ahead by using shifted values before they are known. Check any implementation for this.

## 3. Momentum and oscillators

### Relative strength index (RSI)

RS = average gain / average loss over N periods, with Wilder smoothing. RSI = 100 − 100 / (1 + RS).

- Default: N = 14, with 30 and 70 as oversold and overbought levels.
- Use: mean-reversion entries; divergence analysis.
- Verdict: a bounded transform of recent returns. Overbought and oversold levels are arbitrary and their historical performance depends strongly on the regime. A test of RSI mean reversion should include a trend filter and out-of-sample periods.
- Caveat: in a strong trend RSI can stay above 70 or below 30 for long periods.

### Stochastic oscillator

%K = (C − LL_N) / (HH_N − LL_N) × 100, where LL and HH are the lowest low and highest high over N bars. %D = SMA₃ of %K.

- Default: N = 14, %D smoothing 3.
- Verdict: a rescaled version of where the close sits within the recent range. Largely redundant with RSI for most uses.

### Williams %R

%R = (HH_N − C) / (HH_N − LL_N) × (−100)

- Verdict: the stochastic oscillator reflected onto a different scale. Same caveats.

### Rate of change (ROC)

ROC_N = (C_t / C_(t−N) − 1) × 100

- Verdict: a plain return over N bars. Useful as a momentum input in research; test it as a cross-sectional or time-series momentum signal rather than as a chart pattern.

### Commodity channel index (CCI)

CCI = (TP − SMA_N(TP)) / (0.015 · MeanDeviation_N), with typical price TP = (H + L + C)/3.

- Default: N = 20. The 0.015 constant scales the index so that typical values fall in a range around ±100.
- Verdict: a normalised deviation from a moving average. Treat it like a z-score; its thresholds carry the same overfitting risk as RSI levels.

## 4. Volatility and range

### Bollinger Bands

Middle band = SMA₂₀(C); upper and lower = middle ± 2 · σ₂₀(C).

- Default: N = 20, k = 2.
- Use: mean reversion when price touches a band; breakout when price closes outside a band.
- Verdict: a z-score band on price. The two uses are opposite bets on the same geometry, and which one works depends on the regime. Test both explicitly.
- Caveat: standard deviation is computed on prices, which are not stationary. A z-score on returns or on a stationary spread is more defensible.

### Average true range (ATR)

TR_t = max(H_t − L_t, |H_t − C_(t−1)|, |L_t − C_(t−1)|). ATR = Wilder smoothing of TR over N = 14.

- Verdict: the most useful indicator on this sheet for risk management. Use it to size positions and set stops in volatility units, not to generate entries.

### Keltner channels

Middle = EMA₂₀(C); bands = middle ± k · ATR₁₀ (k commonly 2).

- Verdict: an ATR-based envelope. Differs from Bollinger Bands only in the width measure.

### Chaikin volatility

Percentage change of an EMA of (H − L) over a lookback. Measures whether the range is expanding or contracting.

- Verdict: a regime descriptor. Useful as a filter; weak as a standalone signal.

## 5. Volume

### On-balance volume (OBV)

OBV_t = OBV_(t−1) + V_t if C_t > C_(t−1); − V_t if C_t < C_(t−1); unchanged otherwise.

- Verdict: a cumulative volume sign. Its information is mostly contained in returns and volume separately. Test it against a plain volume-weighted return before claiming any edge.

### Volume-weighted average price (VWAP)

VWAP = Σ(TP · V) / Σ V over the session.

- Verdict: an intraday benchmark for execution quality. Not a predictive indicator for daily strategies. Relevant to market microstructure work.

## 6. Pitfalls common to all indicators

- **Parameter search on the full sample.** Choosing N = 17 because it looked best overfits. Fix parameters before looking at out-of-sample data, or choose them in-sample only.
- **Look-ahead in the calculation.** Centred windows (pandas `center=True`), forward-shifted series, or signals computed with the day's close used to trade at the same close.
- **Costs.** Oscillator rules often trade frequently. Turnover, not gross return, decides whether an edge survives.
- **Multiple testing.** Testing many indicators and parameter sets inflates the apparent best result. Count trials and apply the deflated Sharpe ratio from [Performance metrics](performance-metrics.md).
- **Regime dependence.** Mean reversion and momentum rules have opposite exposure to trending markets. Report results by regime.

## 7. Further reading

- Brock, Lakonishok and LeBaron (1992), "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns." Reported profitable moving-average rules on US index data. Later studies that correct for data snooping and transaction costs found much weaker evidence. Read both.
- Sullivan, Timmermann and White (1999), "Data-Snooping, Technical Trading Rule Performance, and the Bootstrap." Shows that the apparent profitability of many rules disappears once the number of rules tested is accounted for.

## 8. Interview favourites

- Why does an SMA crossover lag price? The average uses past prices, so the crossover happens after a trend has already moved.
- An RSI below 30 is a buy signal. What would you check first? Whether the rule has been tested out of sample, net of costs, and whether it works in trending regimes.
- What is the difference between an EMA with N = 20 and Wilder smoothing with N = 20? The Wilder α = 1/20 is slower than the EMA α = 2/21, so Wilder smoothing reacts more slowly.
- Why might an Ichimoku rule look profitable in a naive backtest? The cloud is shifted forward in time; using its values before they are available is look-ahead.
