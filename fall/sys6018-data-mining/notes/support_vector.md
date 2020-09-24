# Support Vector Machines

Readings: ISL 9.1-9.7, ESL 12.1-12.3 or MMDS 12.3

### Class Notes

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

