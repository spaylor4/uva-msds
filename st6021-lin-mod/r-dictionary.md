## R Dictionary

Keeping track of R functions and use cases covered in this course.

#### Module 0: Review of Statistical Inference

- `pnorm(z)` returns the percentile associated with a particular z-score z from a normal distribution. This percentile equals the area under the curve to the left of z.
- `qnorm(p)` returns the z-score associated with a given percentile p from a normal distribution.
- `qt(p, df)` returns the t-value for a given percentile p and degrees of freedom df. The q stands for quantile and the t indicates a t distribution (as previous two functions represent percentile and quantile for a normal distribution).
- `pt(t, df)` returns the percentile associated with a particular t-value t and degrees of freedom df. This percentile indicates the area under the curve to the left of the given t value.
  - For a two sided t-test of a regression coefficient, need `2*(1 - pt(t, df))` to get the two outer tail probabilities.

#### Module 1: Simple Linear Regression

- `lm(y ~ x, data = data)` performs a simple linear regression on the dataset with y as the response variable and x as the predictor variable.
- `summary(model)` returns several summary statistics for the given model object.
- `anova(model)` returns the analysis of variance table (including the F statistic, sum of squares, and mean squares) for a given fitted model object.

#### Module 2: Inference with Simple Linear Regression

- `confint(lin_mod, level = conf_level)` returns confidence intervals for all regression coefficients for a linear model at a given confidence level (equal to $1 - \alpha$).
- `predict.lm(lin_mod, newdata, level = conf_level, interval = "confidence")` gives a prediction interval for the mean response at predictor variable values passed in newdata (a data frame). Similarly, `predict.lm(lin_mod, newdata, level = conf_level, interval = "prediction")` gives a prediction interval for a single new response for predictor variable values passed in newdata.

#### Module 3: Model Diagnostics & Remedial Measures in SLR

- `acf(lin_mod$residuals, main = "ACF of Residuals")` creates an ACF plot for a linear model to test independence of error terms. The horizontal blue dotted lines indicate the significance level, so if any non-zero lags exceed those lines, there is evidence of correlation among error terms.

- To create a normal probability plot for a linear model, use these two lines:

  ```R
  qqnorm(lin_mod$residuals) #points
  qqline(lin_mod$residuals, col="red") #line
  ```

  The points come from the residuals, while the line represents the expected values under normality. If the points closely follow the line, the assumption of normality of error terms is met.

- `boxcox(lin_mod, lambda = seq(start, end, step))` creates a Box-Cox plot for a linear model. The optional lambda parameter specifies the range and step of lambda values to be included in the plot. The boxcox function is in the MASS package, so `library(MASS)` must be called first.

#### Module 4: Intro to Multiple Linear Regression

- `pairs(data, lower.panel = NULL)` generates a scatterplot matrix for all pairs of columns in some data. The `lower.panel = NULL` argument is optional and hides the bottom half of the matrix, since it's mirrored in the top half.
- `qf(1 - alpha, r, n - p)` returns the critical value for a partial F test with $\alpha$ significance level, $r$ number of terms to consider dropping, $n$ number of data points in sample, and $p$ number of parameters (number of regressors + 1 for intercept) in larger model.

#### Module 5: Sum of Squares & Multicollinearity

- `anova(reduced_model, full_model)` performs a partial F test to assess whether a set of predictors can be dropped. If the Pr(> F) is large, $H_0$ is supported (the predictors removed in the reduced model can be dropped), and if Pr(>F) is small (less than $\alpha$), $H_a$ is supported (the predictors cannot be dropped and the full model is supported).
- `vif(reg_mod)` will give the variance inflation factors (VIFs) for the given regression model. Must first call `library(faraway)` to load the function.

#### Module 6: Categorical Predictors

- `factor(column)` converts the column to a factor type, which is how R designates categorical variables. To check whether a given column is a factor type, use `is.factor(column)`.
- `contrasts(column)` shows how R encodes a factor column with 0/1 dummy variables and shows which level is the reference class encoded as all zeros.
- `levels(column)` shows the classes of a categorical/factor variable column. These can be reset using `levels(column) <- c("level1", "level2", ...)`. Furthermore, the reference class can be reset using `column <- relevel(column, ref = "ref_class_name")`.
- `levene.test(response, categorical_pred)` performs a Levene test to check whether the variances of the categorical variable's classes are the same (null hypothesis) or not (alternative). If Levene's test returns a large p-value, fail to reject null and conclude that assumption of equal variances among classes is met. Need `library(lawstat)` to perform this test.
- `glht(lin_model, linfct = mcp(Region = "Tukey"))` performs a Tukey's multiple comparisons test on a regression model. Like with a regression model, this can be assigned to a variable and `summary(glht_var)` can be called to see the output. Need `library(multcomp)` to perform this test.
- `vcov(lin_model)` returns the variance-covariance matrix for a regression model.

#### Module 7: Model Selection

- `regsubsets(y ~ . , data, nbest)` fits all possible first-order regressions and returns the `nbest` number of best models with each possible number of regressors. Need `library(leaps)` to do this. To get various properties of the result stored in a variable `allreg`, can use

  ```R
  best <- as.data.frame(summary(allreg)$outmat)
  best$p <- as.numeric(substr(rownames(best),1,1))+1
  best$r2 <- summary(allreg)$rsq
  best$adjr2 <- summary(allreg)$adjr2
  best$mse <- (summary(allreg)$rss)/(dim(data)[1]-best$p)
  best$cp <- summary(allreg)$cp
  best$bic <- summary(allreg)$bic
  ```

  This creates a data frame showing the predictors considered, number of predictors $p$, $R^2$, $R^2_{adj}$, $SS_{Res}$, Mallows $C_p$, and BIC.

  - The `regsubsets` function does not check if the regression assumptions are met and does not guarantee that the best model will be identified.

- Can perform forward selection, backward elimination, and stepwise regression using `step(start_model, scope = list(lower = smallest_model, upper = largest_model), direction)`, where direction is "forward", "backward", or "both" and smallest_model and largest_model are the bounds of models under consideration, often an intercept-only model for the smallest and a model with all predictors for the largest. Steps are chosen based on which variables have the lowest AIC (textbook uses F statistic).

  - For forward selection, start_model will be the same as smallest_model. Similarly for backward elimination, start_model will be the same as largest_model.
  - To fit an intercept-only model, use `lm(y ~ 1, data)`
  - `step` function only considers first order models (no interactions or higher order terms). It also does not check if the regression assumptions are met and does not guarantee that the best model will be identified.
  - `step` can lead to different final models if the starting point is different.

#### Module 8: Model Diagnostics & Remedial Measures in MLR

- `rstandard(lin_model)` gives the studentized residuals for a given linear model.
- `rstudent(lin_model)` gives the externally studentized residuals for a given linear model.
  - Critical value using Bonferroni procedure for outliers in response variable based on externally studentized residuals is `qt(1-0.05/(2*n), n-p-1)`. Any externally studentized residuals with magnitude larger than this $t$ value are outliers.
- `lm.influence(lin_mod)$hat` gives leverages for a particular model.
  - Leverages greater than $\frac{2p}{n}$ are considered outlying in the predictor.
- `dffits(lin_mod)` gives the DFFITS of a given model. 
  - Observations are considered influential if the magnitude of their DFFITS is greater than $2\sqrt{\frac{p}{n}}$.
- `dfbetas(lin_mod)` gives the DFBETAS of a given model.
  - Observations are considered influential if the magnitude of their DFBETAS is greater than $\frac{2}{\sqrt{n}}$.
- `cooks.distance(lin_mod)` gives the Cook's distance for a given model.
  - Observations are considered influential if their Cook's distance is greater than `qf(0.5, p, n-p)`.