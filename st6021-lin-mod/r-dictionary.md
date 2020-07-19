## R Dictionary

Keeping track of R functions and use cases covered in this course.

#### Module 0: Review of Statistical Inference

- `pnorm(z)` returns the percentile associated with a particular z-score z from a normal distribution. This percentile equals the area under the curve to the left of z.
- `qnorm(p)` returns the z-score associated with a given percentile p from a normal distribution.
- `qt(p, df)` returns the t-value for a given percentile p and degrees of freedom df. The q stands for quantile and the t indicates a t distribution (as previous two functions represent percentile and quantile for a normal distribution).
- `pt(t, df)` returns the percentile associated with a particular t-value t and degrees of freedom df. This percentile indicates the area under the curve to the left of the given t value.

#### Module 1: Simple Linear Regression

- `lm(y ~ x, data = data)` performs a simple linear regression on the dataset with y as the response variable and x as the predictor variable.
- `summary(model)` returns several summary statistics for the given model object.
- `anova(model)` returns the analysis of variance table (including the F statistic, sum of squares, and mean squares) for a given fitted model object.

#### Module 2: Inference with Simple Linear Regression

- `confint(lin_mod, level = conf_level)` returns confidence intervals for all regression coefficients for a linear model at a given confidence level (equal to $1 - \alpha$).
- `predict.lm(lin_mod, newdata, level = conf_level, interval = "confidence")` gives a prediction interval for the mean response at predictor variable values passed in newdata (a data frame). Similarly, `predict.lm(lin_mod, newdata, level = conf_level, interval = "prediction")` gives a prediction interval for a single new response for predictor variable values passed in newdata.

#### Module 3: Model Diagnostics & Remedial Measures in SLR

- `acf(lin_mod, main = "ACF of Residuals")` creates an ACF plot for a linear model to test independence of error terms. The horizontal blue dotted lines indicate the significance level, so if any non-zero lags exceed those lines, there is evidence of correlation among error terms.

- To create a normal probability plot for a linear model, use these two lines:

  ```R
  qqnorm(lin_mod$residuals) #points
  qqline(lin_mod$residuals, col="red") #line
  ```

  The points come from the residuals, while the line represents the expected values under normality. If the points closely follow the line, the assumption of normality of error terms is met.

- `boxcox(lin_mod, lambda = seq(start, end, step))` creates a Box-Cox plot for a linear model. The optional lambda parameter specifies the range and step of lambda values to be included in the plot. The boxcox function is in the MASS package, so `library(MASS)` must be called first.