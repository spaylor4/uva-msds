# Tree-Based Methods

Readings: ISL 8.1-8.3; ESL 9.2, 15

#### Regression & Classification Trees

- Tree-based methods involve segmenting the predictor space into a number of distinct, non-overlapping regions and using the mean response of the training samples in the region as the prediction.
- Bagging, boosting, and random forests involve combining several trees to generate more accurate predictions.
- Regression trees divide the feature space using a top-down, greedy approach called recursive binary splitting that selects the best split at each step.
  - Susceptible to overfitting.
- Tree pruning addresses the overfitting problem by growing a very large subtree, then using cost complexity/weakest link pruning to select a subtree.
  - Cost complexity pruning uses a tuning parameter $\alpha$ to choose a set of best subtrees, from which the best is chosen using $k$-fold cross validation.
  - Similar to lasso regression, $\alpha$ penalizes the complexity (in this case number of terminal/leaf nodes).
- Classification trees work like regression trees, but use the proportion of training observations from each class in each region as the predictions (instead of the mean response for regression). Instead of squared error, there are three commonly-used loss metrics:
  - Training classification error rate: for $\hat p_{mk}$ proportion of observations from $k$th class in $m$th region, the classification error is 1 - max$_k (\hat p_{mk})$. Other two options generally better.
  - Gini index: $\sum_{k=1}^K \hat p_{mk}(1 - \hat p_{mk})$ is a measure of total variance across $K$ classes.
  - Entropy: $-\sum_{k=1}^K \hat p_{mk}$log $\hat p_{mk}$ is very similar to Gini index, in that it measures the purity of each node, since it is small when $\hat p_{mk}$ is near 0 or 1.
- Compared to classical regression, trees tend to perform better when the relationship between features and response is non-linear and complex. Trees are also very easy to interpret/explain.
- Trees aren't very robust: can change significantly with small changes in data.

#### Bagging

- Bagging involves bootstrap aggregation of trees in order to reduce the variance of estimates. Done by constructing $B$ regression trees from $B$ bootstrapped training sets, then averaging the resulting predictions.
  - For classification problems, can predict class having the maximum number of predictions among the $B$ tree predictions.
- Can use out-of-bag samples to calculate MSE or classification error, which can be used to estimate test error without performing cross-validation.
  - When $B$ sufficiently large, OOB error is nearly equivalent to LOOCV error.
- Bagging is more difficult to interpret than a single tree, but can measure variable importance by calculating the decrease in RSS (or Gini index for classification) due to splits over that variable, averaged over the $B$ trees.
- Bagging can be used for many statistical regression/classification methods in addition to trees.

#### Random Forests

- Random forests are very similar to bagging, but consider a random sample of $m$ predictors (out of the total $p$ predictors) at each split point in order to decorrelate the trees.
  - When there is one strong predictor, bagging trees will be similar, meaning that variance doesn't decrease as much as for uncorrelated trees
  - Usually choose $m \approx \sqrt p$. Choosing $m = p$ is equivalent to bagging.
  - Using a small value of $m$ is generally helpful when data has a large number of correlated predictors.

#### Boosting

- Similarly to bagging, boosting can be used for many statistical regression/classification methods in addition to trees.
- Boosting grows trees sequentially, unlike bagging, which grows them independently. Each new tree is fit to the current residuals, rather than to the response. This model learns slowly, as opposed to fitting a single large tree to the data.
- Boosting has three tuning parameters:
  - Number of trees $B$ (select using cross-validation). Can overfit if $B$ too large, unlike bagging/random forests.
  - Shrinkage parameter $\lambda$ controls the speed at which boosting learns. Generally choose 0.01 or 0.001, but too small can require very large $B$ to achieve good performance.
  - Number of splits in each tree $d$ (also called interaction depth) controls the complexity. Often use $d=1$, making each tree a stump with a single split. A tree with $d$ splits can involve at most $d$ variables.

## Class Notes

*October 15, 2020*

- Boosted trees are generally the best starting point for  supervised learning problems (will cover boosting in a couple weeks).
- Don't generally use trees on their own (use random forest, bagging, boosting instead), but conceptually important for understanding these more complex methods.
- Transforming the response (as in the baseball example with log of salary) means that you're not minimizing squared error loss of the original response, but of the transformed response.
- Trees can do variable selection, and R function shows  importance of each variable.
- Plot of tree using `prp` in R shows average of observations at each node and number of observations in that group.
- Each leaf node corresponds to a region in the predictor space, and only one prediction value used for entire region. Ensemble of trees or more sophisticated fitting method than average at each region are two options for obtaining more complex predictions, since regression tree produces just a constant in each region.
- Complexity of tree is related to number of leaf nodes that it has (more leaves = more complex).
  - Complexity is a tuning parameter, can be adjusted using `cp` argument in `rpart` function. Low `cp` equals high complexity.
  - The `minsplit` argument determines the minimum number of points required in a node in order to split it.
  - Same predictor can be used to split multiple times.
- Regression trees always use binary splits (computationally simpler).
- Determine split points according to maximum gain of making splits, i.e. the biggest decrease in SSE.
- Categorical features with $k$ levels can be split $2^{k-1}-1$ ways.
  - The CART approach sorts categories by mean response in each category, then splits like a numeric feature.
  - Features with many levels are prone to overfitting, since many possible split points means one is likely to be good for the training data. Recommended to not use these variables, use alternative encodings (one-hot or dummy encoding), or use XGBoost or CatBoost.
  - Usually want to split categorical variables based on cross-entropy/deviance, as that is generally used as loss metric.
- Pruning is like backward stepwise selection: grow a full tree and cut off leaf nodes that don't add much to the model.
  - Tree-building is greedy, so bad initial split could lead to good final split.
- Recommended to use $\lambda$ rather than tree size as tuning parameter.