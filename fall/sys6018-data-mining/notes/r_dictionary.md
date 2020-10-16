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

### Kernel Density Estimation

- `kde(data, h)` performs univariate kernel density estimation for data with bandwidth `h`.
  - Can choose `h` using `hpi` (plug-in; default method) `hscv` (smoothed cross-validation), `hucv` (unbiased cross-validation), or `hlscv` (least squares cross-validation) functions.
  - Can do multivariate KDE with `kde(data, H)`.
    - `H` can be chosen similarly to in the univariate case, but using `Hpi`, `Hscv`, `Hucv`, or `Hlscv` functions.

### Clustering

- `kmeans(data, k, nstart=num)` performs $K$-means clustering.
  - The `nstart` argument specifies how many multiple random assignments to use in step one of the algorithm before reporting the best results. Values of at least 20-50 are recommended.
  - The resulting object, say `km_out`, has  `km_out$cluster` with the cluster assignments and`km_out$tot.withinss` with the total within-cluster sum of squares.
- `hclust(dist(data), method = "complete")` performs hierarchical clustering, where method can be `"complete"`, `"average"`, `"single"`.
  - The `dist()` function computes the inter-observation distance matrix. Can be Euclidean, Manhattan, or a few other measures of distance. 
    - Manhattan distance is distance in $x$ direction plus distance in $y$ direction (often useful for human movement problems).
  - Can use `cutree(hc_out, n_clusts)` to get the cluster labels for a given number of clusters.

### Tree-Based Methods

- `tree(y ~ eq, data)` fits a regression or classification tree (using basically the same syntax as `lm`). The `tree` function comes from the `tree` package.
  - Calling `summary(tree_result)` outputs info including variables used, number of terminal nodes, and training misclassification error rate (for classification) or deviance (for regression, equivalent to sum of squared error).
  - Can use `predict(tree_result)` to make predictions. Need argument `type = "class"` for classification to get a hard class decision.
- `cv.tree(tree_result)` performs cross-validation to determine the optimal level of tree complexity.
  - Default metric is deviance, but can be changed using `FUN` argument. For example, `FUN = prune.misclass` uses the misclassification error rate.
  - The resulting `k` attribute is the $\alpha$ complexity penalty used.
  - The resulting `dev` attribute is the value of the error metric (deviance, misclassification error rate, or other specified metric) for each tree.
- After choosing an optimal size with `cv.tree`, can then prune the original tree using `prune.tree(tree_result, best = opt_size)` or `prune.misclass(tree_result, best = opt_size)` as appropriate.
- Both bagging and random forest can be performed with using `randomForest(response ~ eq, data = data, mtry = mtry, importance = TRUE, subset = train)` function (from the `randomForest` package).
  - `mtry` argument specifies $m$ parameter of number of variables to consider at each split. Specifying $m$ equal to the total number of predictors results in bagging rather than random forest. Default is $p/3$ for regression and $\sqrt p$ for classification.
  - `importance(rf_result)` shows the importance of each variable.
- Boosting can be done with `gbm(response ~ eq, data = data, distribution = "gaussian", n.trees = n.trees, interaction.depth = depth)` from the `gbm` package. Parameter `distribution = "gaussian"` used for regression; would use `distribution = "bernoulli"` for classification.
  - Can specify values of the shrinkage parameter $\lambda$ using the `shrinkage` argument (default is 0.001).

 