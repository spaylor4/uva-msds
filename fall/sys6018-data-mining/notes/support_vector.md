# Support Vector Machines

Readings: ISL 9.1-9.7, ESL 12.1-12.3 or MMDS 12.3

### Maximal Margin Classifier

- In a $p$ dimensional space, a hyperplane is a $p-1$ dimensional subspace (e.g. a line in 2D, plane in 3D, etc.).
- A hyperplane is defined mathematically as $\beta_0 + \beta_1 X_1 + ... + \beta_p X_p = 0$.
- A hyperplane can be used as a decision rule for classification, such that $\beta_0 + \beta_1 X_1 + ... + \beta_p X_p < 0$ is classified as -1 and $\beta_0 + \beta_1 X_1 + ... + \beta_p X_p > 0$ is classified as 1.
  - If the two classes can be perfectly separated, there are an infinite number of hyperplanes that can separate the two. 
  - The maximal margin hyperplane (or optimal separating hyperplane) is furthest from the observations, using margin (minimum perpendicular distance from point to hyperplane). Can lead to overfitting when $p$ is large.
  - Support vectors are observations in $p$-dimensional space close to the hyperplane that, if moved, would cause the maximal margin hyperplane to move. The maximal margin hyperplane depends on a small subset of all observations.

### Support Vector Classifier

- If no separating hyperplane exists between classes, there is no maximal margin hyperplane, but the concept can be extended using a "soft margin" to create a support vector classifier.
  - A hyperplane that does not perfectly separate the two classes can give sometimes give greater robustness to individual observations and better classification of most training observations.
  - A support vector classifier allows some training observations to be on the wrong side of the margin or the hyperplane.
  - Classifier has a tuning parameter $C$, a "budget" for the amount the margin can be violated by $n$ observations.
    - Small $C$ tends to have low bias but high variance and vice versa.
    - Due to this, only observations on the margin or on the wrong side of the margin are support vectors (affect the classifier). Small $C$ leads to fewer support vectors.

### Support Vector Machine

- The support vector machine extends the support vector classifier using kernels, allowing for non-linear classifiers to be fit.
- Polynomial kernels essentially fit a support vector classifier in a higher-dimensional space involving polynomials of degree $d$, rather than the original feature space. They lead to much more flexible decision boundaries.
- The radial kernel essentially classifies a circle as one class and everything outside that circle as the other class.
- Kernels are computationally much simpler than expanding the original feature space using functions.
- SVMs separating hyperplanes don't generalize well to classification with more than two classes.
  - One-vs-one (all pairs) classification involves constructing $k\choose{2}$ SVMs, each of which compares two classes. The final classification assigns each observation to the class it was assigned to most frequently in the pairwise classifications.
  - One-vs-all classification fits $k$ SVMs, each comparing one class to all remaining $k-1$ classes. Then each observation $x^*$ is assigned to the class for which $\beta_{0k} + \beta_{1k}x_1^* + ... + \beta_{pk}x_p^*$ is largest, as this indicates a high level of confidence that the observation belongs to the $k$th class rather than any others.
- SVMs use hinge loss, which is closely related to the loss function used in logistic regression. They tend to give similar results due to the similarities in their loss functions.
  - SVMs tend to behave better than logistic regression when the classes are well separated; logistic regression is often preferable when more overlap is present. 

## Class Notes

*September 24, 2020*

- SVM similar to penalized logistic regression, but uses a different loss function. SVM conventionally uses -1 and 1 for classes, rather than 0 and 1 used in logistic regression. SVM uses 0 as threshold.
- Linear SVM has same model (predictor function) as logistic regression: $f(x; \beta) = \beta_0 + \sum_{j=1}^p h_j(x)\beta_j$.
  - Basis expansion (e.g. polynomial) is connected to kernels, which we'll discuss later.
- SVM loss function is hinge loss: max${0, 1-\tilde{y}f}$.
  - Some correct predictions still get penalized, but no penalty if $\hat f(x) \ge 1$ and $\tilde{y} = 1$ and vice versa.
  - Logistic regression uses log-loss.
- Also uses a ridge penalty ($x$'s should be standardized - most code implentations do so automatically).
- SVM has tuning parameters $\lambda$ for ridge penaly weight as well as other parameters related to the kernels.
  - $\frac{1}{c} = \frac{\lambda}{2}$, where $c$ is cost

