# Penalized Regression

Readings: ISL 6.1-6.4; ESL 3.3-3.6

### Subset Selection

- Best subset selection is a technique for selecting the best least squares regression that involves fitting all possible models from all possible combinations of the available predictors, then choosing the best one.
  - Generally choose the best model for each $k$ possible number of predictors using the one with the smallest RSS or largest $R^2$, then choose the best model among the different $k$'s using cross-validation prediction error, adjusted $R^2$, AIC, BIC, or $C_p$.
  - Same method can be applied to logistic regression using deviance instead of RSS. Deviance is -2 times maximized log-likelihood, and the best model is the one with the smallest deviance.
  - Computationally expensive, infeasible when number of predictors greater than around 40.
  - In high dimensions, there is a larger chance of finding a model with good training performance but poor predictive performance on future data.
- Stepwise selection addresses the downsides of best subset selection by considering a smaller subset of models, adding or removing one predictor at a time.
  - Forward stepwise selection starts with a model with no predictors and adds predictors one at a time based on which gives the greatest marginal improvement to the fit (greedy algorithm). Backward selection begins with all predictors and removes them one at a time based on which is least useful.
  - Forward stepwise selection will have lower variance but perhaps more bias than best subset selection.
  - Backward selection requires that the number of samples $n$ is greater than the number of predictors $p$, but forward selection does not.
  - Stepwise selection does not always find the best possible model out of all models containing a subset of the predictors.
  - Hybrid stepwise selection approaches allow predictors to be added or removed at each step.
  - Forward stagewise selection is similar to forward stepwise, but the coefficient for each additional coefficient is calculated on the current residuals, and none of the variables already in the model are adjusted when a new term is added. Forward stagewise can be inefficient, but becomes useful in high-dimensional problems.
- Subset selection can improve prediction accuracy compared to least squares by adding a little bias to significantly lower variance. It can improve interpretability by simplifying the model.

### Shrinkage Methods

- Shrinkage methods regularize coefficient estimates, shrinking them toward zero. Doing so can significantly reduce variance.
- Compared to subset selection methods, shrinkage methods have less variability, since it is a continuous rather than discrete (include/exclude) decision.
- Ridge regression minimizes RSS + $\lambda \sum \beta_j^2$, where $\lambda$ is a tuning parameter determining the relative importance of the two terms. This second term is called a shrinkage penalty, and its importance grows as $\lambda$ grows.
  - When $\lambda = 0$, this produces the same estimates as least squares. As $\lambda \rightarrow \infty$, the coefficient estimates converge to zero, or the null (intercept-only) model. Higher $\lambda$ leads to more shrinkage.
  - The intercept is not included in the shrinkage penalty.
  - Ridge regression works best in situations when the least squares estimates have high variance.
  - Ridge regression can be used even when the number of variables $p$ is close to or even greater than the number of observations $n$, while least squares doesn't have a unique solution when $p > n$ and is highly variable when $p$ is large relative to $n$.
  - Ridge regression is computationally much simpler than best subset selection.
  - Ridge regression will include all $p$ predictors in the final model, unlike stepwise selection or best subset.
- The lasso is an alternative to ridge regression that performs variable selection in addition to shrinking the coefficients toward zero. It minimizes RSS + $\lambda \sum | \beta_j |$.
  - This shrinkage penalty is an $\ell_1$ penalty, whereas ridge regression uses an $\ell_2$ penalty.
  - In two dimensions, the ridge regression contraint forms a circle, while the lasso constraint forms a diamond. The possible values of coefficients giving a certain RSS form an ellipse, and these ellipses intersect can intersect the diamond but not the circle at an axis-intercept.
  - Lasso produces simpler, more interpretable models than ridge.
  - Generally, lasso will perform better when the response is a function of a relatively small number of predictors, while ridge will perform better when the response is a function of many predictors. Since it isn't known how many predictors are truly related, cross-validation can be used to choose which approach to use. 
  - Cross-validation can be used to select the value of $\lambda$ used for both ridge and lasso.

### Dimension Reduction

- Dimension reduction methods transform the original predictors into $M$ linear combinations of the $p$ original predictors (where $M < p$), then fit a least squares model using the transformed predictors.
  - If $M = p$, no dimension reduction occurs, and the process is equivalent to performing least squares on the original predictors.
- Dimension reduction can bias coefficient estimates some, but can significantly reduce variance when $p$ is large relative to $n$ and $M << p$ is chosen.
- Principal components analysis (PCA) is one dimension reduction method. The first principal component is the direction of the data along which the observations vary the most.
  - The principal component loadings define the principal component direction and are the coefficients of the linear combination of the transformed variables.
  - The first principal component vector defines the line closest to the data.
  - The second principal component is a linear combination of variables uncorrelated with the first principal component. The second PC is perpendicular/orthogonal to the first PC.
  - For a dataset with $p$ predictors, there can be at most $p$ principal components.
- Principal components regression (PCR) involves constructing the first $M$ principal components, then using these components as the predictors in a least squares regression model.
  - Assumes that the directions in which **$X$** vary the most are the directions that are associated with $Y$. If this assumption holds, PCR leads to better results than standard least squares regression, as it is less susceptible to overfitting.
  - As more PCs are used, bias decreases and variance increases. Number of PCs usually chosen using cross-validation.
  - PCR will tend to do well in cases when the first few PCs sufficiently capture most of the variation in the predictors and the relationship with the response.
  - Not a feature selection model; closely related to ridge regression.
  - Recommended to standardize predictors prior to generating PCs.
  - PCs identified in an unsupervised way ($Y$ has no influence in determining PCs).
- Partial least squares (PLS) is a supervised alternative to PCR that attempts to find linear combinations of the original predictors that explain both the response and the predictors.
  - The first direction $Z_1$ is the linear combination of the original predictors times the coefficient of the simple linear regression of $Y$ onto $X_j$, so the coefficient is proportional to the correlation between $Y$ and $X_j$.
  - Subsequent directions are computed by regressing each variable on the previous directions, finding the residuals, and computing the next direction on the residuals in the same way as the first direction was calculated. The residuals are remaining information that has not been explained by the previous PLS directions.
  - Generally standardize predictors and response before performing PLS.

### High-Dimensional Data

- High-dimensional has a large number of predictors $p$ compared to the number of observations $n$.
- Many classical approaches (including least squares linear regression, logistic regression, and linear discriminant analysis) are not appropriate in high dimensions when $p>n$.
  - Least squares will perfectly estimate the training data (residuals = 0) when $p>n$, leading to overfitting (model is too flexible).
  - Ridge, lasso, PCA, and forward stepwise selection are useful in the high-dimensional setting, as they are less flexible than least squares.
- Regularization/shrinkage is important in high-dimensional problems.
- Appropriate tuning parameter selection is crucial for good predictive performance.
- Curse of dimensionality: if additional predictors are not truly associated with response, test error increases with increased dimensions (predictors).
  - Adding "signal" features will improve the fitted model, but adding "noise" features will negatively impact the fitted model.
  - Even adding relevant features may harm the model if their addition increases variance more than it reduces bias.
- In high-dimensions, multicollinearity is always a problem.

## Class Notes

*September 10, 2020*

#### Ridge Regression

- Some software defines the loss function as MSE, others as SSE (sum or squared error, equal to $n$*MSE).
- Important to scale the predictor variables because if magnitude of coefficients differs, they will be penalized differently. Scaling makes standard deviation the same, since magnitude of coefficients is related to the variance of the variables.
  - Scaling usually done for you by software applications.
- Ridge regression theoretically always has a lower MSE than OLS (but you have to find the $\lambda$).
- When predictors are highly correlated, ridge regression tends to set their coefficients nearly equal to each other.
  - OLS with multicollinearity doesn't impact prediction too much, but does impact inference.
  - Ridge regression reduces variance.
- $\lambda$ is the tuning parameter: $\lambda = 0$ gives least squares estimates, $\lambda = \infty$ gives coefficients = 0 (intercept-only model).
  - Large $\lambda$ may underfoot, small $\lambda$ may overfit.
- The effective degrees of freedom df($\lambda$) is the trace of the hat matrix $H_{\lambda}$, equal to the sum of the diagonals of the hat matrix.
  - Edf always between 1 and $p+1$ (assuming a non-penalized intercept is in the model).
- Ridge tends to shrink correlated predictors' coefficients together, while lasso tends to choose one of the correlated predictors and drop the other.

#### Lasso

- Lasso = least absolute shrinkage and selection operator. Can remove predictors from model, but in a continuous fashion.
  - Lasso and elastic net models have replaced stepwise selection procedures in popularity recently.
- Lasso effective degrees of freedom is equal to number of non-zero coefficients.
- Elastic net combines ridge and lasso.
  - Ridge generally performs better with less noise, since it keeps all predictors in the model.
  - Elastic net has a parameter $\alpha$ that defines the tradeoff between ridge and lasso.
  - Elastic net does do variable selection, but once the predictor is in the model, the coefficients generally more closely follow the ridge path.
- Categorical predictors: dummy coding uses $k-1$ columns for $k$ categories; one-hot encoding uses $k$ columns for $k$ categories/levels.
  - Lasso/ridge generally use one-hot encoding, so that each column is penalized equally.
  - Can't use one-hot in OLS regression.
  - Lasso/ridge also penalize interaction terms and basis expansion of polynomials equally by default.
  - Group lasso penalizes whole groups together, so that all levels are included/excluded from the model together.

