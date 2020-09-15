# Penalized Regression

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

## Class Notes

*September 10, 2020*

#### Ridge Regression

- Some software defines the loss function as MSE, others as SSE (sum or squared error, equal to $n$*MSE).
- Important to scale the predictor variables because if magnitude of coefficients differs, they will be penalized differently. Scaling makes standard deviation the same, since magnitude of coefficients is related to the variance of the variables.
  - Scaling usually done for you by software applications.
- Ridge regression theoretically always has a lower MSE than OLS (but you have to find the $\lambda$.

