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
- SVM loss function is hinge loss: max$\{0, 1-\tilde{y}f\}$.
  - Some correct predictions still get penalized, but no penalty if $\hat f(x) \ge 1$ and $\tilde{y} = 1$ and vice versa.
  - Logistic regression uses log-loss.
- Also uses a ridge penalty ($x$'s should be standardized - most code implentations do so automatically).
- SVM has tuning parameters $\lambda$ for ridge penaly weight as well as other parameters related to the kernels.
  - $\frac{1}{c} = \frac{\lambda}{2}$, where $c$ is cost

*November 24, 2020*

- ISLR has implementations for this in R. 
- Professor Porter recommends trying to implement models we've covered in python via scikitlearn.
  - More consistent across models than R, where different models have different packages.
- What to do about unbalanced data for classification?
  - Weight observations to make total weight of positive class equal to total weight of negative class. This is one alternative to changing the threshold, as in logistic regression (default threshold is 0).
- Using 0-1 loss is equivalent to optimizing to accuracy. SVM instead uses hinge loss, which assigns a small penalty to some correct predictions (between 0 and absolute value equal to 1), and an increasing penalty for increasingly wrong predictions.
- Cost $C$ related to inverse of tuning parameter $\lambda$ (ridge penalty). $C$ is usually the tuning parameter in software implementations. Small $C$ corresponds to large $\lambda$ and vice versa.
  - $\frac{1}{C} = \frac{\lambda}{2}$
- Goals of SVM: create best separation of two classes; estimate basis function parameters.
  - In 2D example (textbook ch. 9), there are an infinite number of lines that separate the two classes. Want to select best separating line (or hyperplane in multiple dimensions). Equation for correct classifications can be written as $y_i f_i > 0$, since $y_i$ can be 1 or -1.
- Support vectors are observations closest to separating hyperplane (they determine the margin and boundary).
  - All other observations have no influence over boundary (not the case for logistic regression).
- Objective is to maximize margin subject to constraints that $\sum\beta_j^2 = 1$ (regularizing constraint) and all points must be on the correct side of the margin (even correctly classified observations can't be within the margin).
  - Problem: doesn't work for non-separable data; very hard constraint. Loosen this restriction by adding slack variables that allow some observations to be on the wrong side of the margin or hyperplane. Change constraint to $y_i f_i \ge M(1 - \epsilon_i)$, with $\sum\epsilon_i \le C$.
    - If $y_i f_i \ge M$, $\epsilon_i = 0$, else $\epsilon_i > 0$.
  - $C$ estimates slack variables ($C$ = 0 means data must be separable).
  - Bias-variance tradeoff: if $C$ is small, then $M$ is small, and we have a high variance, low bias solution.
- Support vector machines use a basis expansion of support vectors (allow for non-linear decision boundaries).
  - Instead of $f(x) = \sum_{i=1}^p x_i \beta_i$, SVM has $f(x) = \sum_{i = 1}^d h_d(x)\beta_i$
- Solution to SVM classifier problem involves inner products of observations (a type of distance)