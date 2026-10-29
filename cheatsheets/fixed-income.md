# Fixed income cheat sheet

*Last reviewed: Oct 2026*

Notation: F face value, c annual coupon rate, n number of coupon periods remaining, y yield to maturity per period, t_i time of cash flow i in periods, CF_i cash flow i, P price, r(t) continuously compounded zero rate, d(t) discount factor.

## 1. Bond pricing

A plain coupon bond with annual coupons pays c·F each year and F at maturity:

P = Σ_(t=1)ⁿ (cF) / (1 + y)ᵗ + F / (1 + y)ⁿ

Price and yield move in opposite directions. A bond priced at par has yield equal to its coupon rate; a premium bond has yield below the coupon; a discount bond has yield above it.

### Clean and dirty price

- Dirty (full) price = clean price + accrued interest.
- Accrued interest = coupon × (days since last coupon / days in the coupon period), under the bond's day-count convention.
- Quoted prices are usually clean. Cash flows settle at the dirty price.

### Day-count conventions

| Convention | Used for | Accrual fraction |
|---|---|---|
| Actual/365 | Many government bonds | Actual days / 365 |
| 30/360 | Many corporate bonds | (360·ΔY + 30·ΔM + ΔD) / 360 |
| Actual/Actual | US Treasuries | Actual days / days in the coupon period |

Check the market's convention before comparing yields. Using the wrong one changes accrued interest and therefore the dirty price.

## 2. Yield measures

- **Yield to maturity (YTM):** the single rate y that equates the dirty price to the present value of the cash flows.
- **Current yield:** annual coupon / clean price. Ignores capital gain or loss.
- **Yield to call and yield to worst:** the yield assuming the issuer calls the bond at the earliest call date (or the lowest of the yields to each call date, for the worst case).
- **Zero-coupon yield:** the yield of a bond with a single cash flow at maturity. The zero curve is built from these.

## 3. Duration and convexity

### Macaulay duration

D_Mac = Σ t_i CF_i (1 + y)^(−t_i) / P

For a zero-coupon bond, Macaulay duration equals maturity. The duration of a coupon bond is less than its maturity.

### Modified duration

D_Mod = D_Mac / (1 + y)

Percentage price change for a small yield move: ΔP / P ≈ −D_Mod · Δy.

### DV01 (price value of a basis point)

DV01 = D_Mod · P · 0.0001

The dollar change in price for a 1 bp move in yield. Used for hedge sizing: the notional of a hedge instrument equals the target DV01 divided by its DV01 per unit of notional.

### Convexity

Convexity = (1/P) Σ t_i (t_i + 1) CF_i (1 + y)^(−t_i − 2)

Second-order price approximation:

ΔP / P ≈ −D_Mod · Δy + ½ · Convexity · (Δy)²

Convexity is positive for plain bonds. Positive convexity means the price rises more than duration predicts when yields fall, and falls less when yields rise. Callable bonds can have negative convexity near the call price.

### Worked example

5-year bond, 6% annual coupon, face 100, yield 5%: price 104.33, Macaulay duration 4.48, modified duration 4.26, convexity 23.44, DV01 0.0445 per 1 bp.

For a +100 bp move, the duration-plus-convexity estimate gives 100.003 against an exact price of 100.000.

### Key rate duration

Sensitivity to a shift in one point of the curve, holding the others fixed. Summing key rate durations across the curve gives the effective duration. Use key rate duration when the position's exposure is concentrated in one maturity.

## 4. Term structure

### Discount factors and zero rates

With continuous compounding, d(t) = e^(−r(t) t), so r(t) = −ln d(t) / t.

### Bootstrapping

Build the zero curve from par bond or swap rates, one maturity at a time:

1. Solve for the discount factor at the shortest maturity from its par rate.
2. For each longer maturity, use the coupon and the known discount factors of earlier payments to solve for the new discount factor.
3. Interpolate the zero rates between knots, with log-linear or cubic interpolation on discount factors. Document the choice, because forward rates depend on it.

### Forward rates

The forward rate from t₁ to t₂ implied by spot rates:

f(t₁, t₂) = [r(t₂) t₂ − r(t₁) t₁] / (t₂ − t₁)

Equivalently, f = ln(d(t₁) / d(t₂)) / (t₂ − t₁) under continuous compounding.

### Nelson–Siegel curve

r(τ) = β₀ + β₁ (1 − e^(−τ/λ)) / (τ/λ) + β₂ ((1 − e^(−τ/λ)) / (τ/λ) − e^(−τ/λ))

Four parameters: level (β₀), slope (β₁), curvature (β₂), and decay (λ). Widely used for smooth curve fitting. Extensions such as Svensson add a second curvature term.

### Curve shapes

- **Normal (upward sloping):** long rates above short rates, reflecting term premium and expected rate increases.
- **Flat or inverted:** short rates at or above long rates. Often read as a signal of expected easing or recession, though the signal is noisy.
- **Steepening and flattening:** changes in the slope, often described as bull or bear steepeners and flatteners depending on whether short or long rates move.

## 5. Swaps and money markets

- **Interest rate swap:** exchange fixed for floating payments. The par swap rate is the fixed rate that makes the swap value zero at inception.
- **Forward rate agreement (FRA):** fix a rate for a future period; settles in cash on the difference.
- **Swap spread:** swap rate minus the government bond yield of the same maturity. Reflects credit, liquidity and supply.

## 6. Common mistakes

- Comparing yields quoted under different compounding or day-count conventions.
- Using modified duration as if it were Macaulay duration, or the reverse.
- Applying duration to a large yield move without convexity, which overstates losses on bonds with large convexity.
- Hedging a curve position with a single duration, which ignores differences in shape risk.
- Bootstrapping without checking that the resulting forward curve is smooth and positive.
- Ignoring embedded options: callable and putable bonds need option-adjusted duration and convexity.

## 7. Interview favourites

- What is the duration of a zero-coupon bond? Its maturity.
- A bond has duration 4 and yield 5%. What is its approximate price change for a 10 bp rise in yield? About −0.4% (4 × 0.001).
- Why does convexity matter for a hedge? Duration hedges are accurate only for small moves; convexity drives the error for larger shifts.
- Why is a callable bond's convexity negative near the call price? As yields fall, the issuer is more likely to call, so price gains are capped.
- How do you hedge a 1-year bond position using 5-year bonds? Match DV01, not notional, and recognise that the hedge leaves curve-shape risk exposed.
