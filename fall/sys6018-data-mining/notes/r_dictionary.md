# Data Mining R Dictionary

Keeping track of R functions, use cases, and interpretations learned throughout the course.

### Supervised Learning

- `poly()` is convenient for modeling polynomial terms. For example, `poly(x, degree = 2)` creates $x^2$, $x$, and intercept terms.
- `knn.reg()` from the `FNN` package fits a KNN model.
- `rnorm(n, mean = 0, sd = 1)` creates a vector of normal random variables of length $n$.

### Penalized Elastic Net

- The `glmnet()` function in the `glmnet` [package](https://glmnet.stanford.edu/articles/glmnet.html) fits generalized linear models (lasso, ridge).
  - `model.matrix(y ~ x, data)[,-1]` generates a matrix for the predictors needed in creating a `glmnet` model. It automatically transforms any qualitative variables into dummy variables. The `glmnetUtils` [package](https://cran.r-project.org/web/packages/glmnetUtils/vignettes/intro.html) provides the ability to supply functions to the model fitting call.
  - The parameter `alpha = 0` signifies ridge regression, while `alpha = 1` signifies lasso.
  - The function automatically standardizes variables to be on the same scale and centered, though this can be turned off with the parameter `standardize = FALSE`. Also translates output back to original units.

### Support Vector Machine

- `svm(formula, data, kernel = "linear", cost=num)` fits a linear SVM with a specified cost (from the `e1071` package (`LiblineaR` is another option).
  - Large cost means margins will be narrow and there will be few support vectors on or violating the margin. Small cost means wide margins and many support vectors on or violating the margin.
  - Must encode the response variable as a factor to get classification rather than regression.
  - If the result is stored as `svmfit`, then `svmfit$index` gives the indices of the support vectors.
  - `svm` uses one-vs-one approach for multi-class classification.
- `tune(svm, formula, data, kernel="linear", ranges = list(cost = c(0.01, 0.1, 1, 5, 10, 100)))` will perform cross-validation for the supplied values of cost.
  - `tune_result$best.model` gives the best resulting model from cross validation.
  - `predict(tune_result$best.model, test_data)` will give predictions for test data.
- Can use `kernel = "polynomial"` or `kernel = "radial"` to fit other types of kernels.
  - For radial kernels, use `gamma` parameter to specify the radial basis kernel.