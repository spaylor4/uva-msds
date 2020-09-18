# Data Mining R Dictionary

Keeping track of R functions, use cases, and interpretations learned throughout the course.

### Supervised Learning

- `poly()` is convenient for modeling polynomial terms. For example, `poly(x, degree = 2)` creates $x^2$, $x$, and intercept terms.
- `knn.reg()` from the `FNN` package fits a KNN model.
- `rnorm(n, mean = 0, sd = 1)` creates a vector of normal random variables of length $n$.
- The `glmnet()` function in the `glmnet` [package](https://glmnet.stanford.edu/articles/glmnet.html) fits generalized linear models (lasso, ridge).
  - `model.matrix(y ~ x, data)[,-1]` generates a matrix for the predictors needed in creating a `glmnet` model. It automatically transforms any qualitative variables into dummy variables. The `glmnetUtils` [package](https://cran.r-project.org/web/packages/glmnetUtils/vignettes/intro.html) provides the ability to supply functions to the model fitting call.
  - The parameter `alpha = 0` signifies ridge regression, while `alpha = 1` signifies lasso.
  - The function automatically standardizes variables to be on the same scale and centered, though this can be turned off with the parameter `standardize = FALSE`. Also translates output back to original units.