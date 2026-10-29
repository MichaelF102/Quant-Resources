# Linear algebra cheat sheet

*Last reviewed: Oct 2026*

Notation: A matrix, x vector, Aᵀ transpose, A⁻¹ inverse, λ eigenvalue, v eigenvector, Σ covariance matrix, X data matrix (n observations by p variables), ‖·‖ Euclidean norm.

## 1. Definitions to know without looking up

- A matrix is **symmetric** if A = Aᵀ. Covariance and correlation matrices are symmetric.
- A symmetric matrix is **positive semi-definite** (PSD) if xᵀAx ≥ 0 for all x, and **positive definite** (PD) if strictly greater than zero for all x ≠ 0.
- Covariance matrices are PSD. They are PD when no variable is an exact linear combination of the others.
- A matrix is **invertible** if and only if its determinant is non-zero, which is equivalent to full rank.
- The **rank** of a matrix is the number of linearly independent columns. Rank deficiency in a covariance matrix means the sample is too small or variables are redundant.

## 2. Eigendecomposition

For a symmetric matrix Σ:

Σ = V Λ Vᵀ, where V is orthogonal (VᵀV = I) and Λ is diagonal with eigenvalues λ₁ ≥ λ₂ ≥ … ≥ λ_p ≥ 0.

- The eigenvectors are orthogonal, and the eigenvalues are real.
- trace(Σ) = Σ λᵢ. For a correlation matrix, the eigenvalues sum to the number of variables.
- The largest eigenvalue gives the maximum variance achieved by a unit vector: max_‖x‖=1 xᵀΣx = λ₁, attained at v₁.
- Share of variance explained by component k: λₖ / Σ λᵢ.

## 3. Singular value decomposition (SVD)

Any real matrix X (n × p) can be written as

X = U Σ Vᵀ

- U (n × n) and V (p × p) are orthogonal. Σ is diagonal with singular values σ₁ ≥ σ₂ ≥ … ≥ 0.
- The columns of V are the principal directions. The eigenvectors of XᵀX are the columns of V, and its eigenvalues are σᵢ².
- SVD is the numerically stable way to compute PCA. Use it rather than forming XᵀX when X is large or ill-conditioned.
- Rank: the number of non-zero singular values. Condition number: σ₁ / σ_r (the ratio of largest to smallest non-zero singular value). A large condition number means inverting the matrix amplifies noise.

## 4. Principal component analysis

Given standardised data X (zero mean in each column):

- Covariance: S = XᵀX / (n − 1)
- Principal components: the eigenvectors of S, in decreasing eigenvalue order.
- Scores: Z = XV. Component k has variance λₖ.
- Proportion of variance explained by the first k components: (λ₁ + … + λₖ) / Σ λᵢ.

**Sign ambiguity:** an eigenvector is defined only up to sign. Fix a convention (for example, the largest absolute loading is positive) before interpreting signs.

**Noise:** for a sample correlation matrix of p variables from n observations, eigenvalues near the Marchenko–Pastur range are indistinguishable from noise. Compare with the random-matrix benchmark before interpreting small components.

## 5. Least squares and regression

Linear model y = Xβ + ε.

- Ordinary least squares: β̂ = (XᵀX)⁻¹Xᵀy, when XᵀX is invertible.
- Using the SVD X = UΣVᵀ: β̂ = V Σ⁻¹ Uᵀ y. This avoids forming XᵀX and is stable when the columns are nearly collinear.
- Fitted values: ŷ = Hy, with hat matrix H = X(XᵀX)⁻¹Xᵀ.
- Residual variance estimate: σ̂² = ‖y − ŷ‖² / (n − p).
- Covariance of the estimates: σ̂² (XᵀX)⁻¹.

**Ridge regression:** β̂_λ = (XᵀX + λI)⁻¹Xᵀy. The λI term makes the matrix invertible and shrinks the estimates towards zero.

## 6. Cholesky decomposition

For a symmetric positive definite matrix Σ:

Σ = L Lᵀ, where L is lower triangular with positive diagonal.

- Used to simulate correlated normal variables: if Z has independent standard normal entries, X = μ + LZ has covariance Σ.
- Faster and more stable than computing an inverse. Solve linear systems with the factors rather than inverting.
- Fails if Σ is not positive definite. A failure is a signal that the covariance estimate is not valid, not just a numerical nuisance.

## 7. Covariance estimation and shrinkage

When the number of assets p is large relative to the number of observations n, the sample covariance S is noisy and can be singular.

- **Shrinkage:** Σ̂ = δF + (1 − δ)S, with a structured target F (for example, a scaled identity or a constant-correlation matrix) and an intensity δ ∈ [0, 1].
- **Ledoit–Wolf:** chooses δ to minimise expected squared error under a stated loss. Implemented in `sklearn.covariance.LedoitWolf`.
- **Factor model:** Σ = B F Bᵀ + D, with B the factor loadings, F the factor covariance and D a diagonal matrix of idiosyncratic variances. Fewer parameters than the full sample covariance.

See [Project 06](../projects/06-covariance-shootout/) for the comparison.

## 8. Matrix calculus you will use

- ∂(aᵀx)/∂x = a
- ∂(xᵀAx)/∂x = (A + Aᵀ)x, which is 2Ax for symmetric A
- Gradient of the least-squares loss ‖y − Xβ‖²: −2Xᵀ(y − Xβ)

## 9. Portfolio applications

- Portfolio variance: wᵀΣw. Portfolio standard deviation with weights w.
- Minimum-variance portfolio (no constraints): w = Σ⁻¹1 / (1ᵀΣ⁻¹1).
- Risk contribution of asset i: wᵢ(Σw)ᵢ / (wᵀΣw). The contributions sum to 1.

## 10. Common mistakes

- Assuming a covariance matrix from a short sample is invertible. Check the rank and condition number first.
- Interpreting eigenvector signs without a convention.
- Forming XᵀX explicitly when X is ill-conditioned, which squares the condition number.
- Computing an inverse to solve a system. Solve it directly.
- Treating a sample eigenvalue as exact. Its estimation error is large when n is not much larger than p.

## 11. Interview favourites

- What is the trace of a matrix equal to? The sum of its eigenvalues.
- Why is the first principal component the direction of maximum variance? It is the eigenvector with the largest eigenvalue of the covariance matrix.
- Why does a correlation matrix's eigenvalue sum equal the number of variables? Its diagonal entries are all 1, and the trace equals the sum of the eigenvalues.
- When would you use SVD instead of the eigendecomposition of XᵀX? When X is ill-conditioned or large, because SVD avoids squaring the condition number.
