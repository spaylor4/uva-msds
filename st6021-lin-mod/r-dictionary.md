## R Dictionary

Keeping track of R functions and use cases covered in this course.

#### Module 0: Review of Statistical Inference

- `pnorm(z)` returns the percentile associated with a particular z-score z from a normal distribution. This percentile equals the area under the curve to the left of z.
- `qnorm(p)` returns the z-score associated with a given percentile p from a normal distribution.
- `qt(p, df)` returns the t-value for a given percentile p and degrees of freedom df.
- `pt(t, df)` returns the percentile associated with a particular t-value t and degrees of freedom df.

#### Module 1: Simple Linear Regression

- `lm(y ~ x, data = data)` performs a simple linear regression on the dataset with y as the response variable and x as the predictor variable.
- `summary(model)` returns several summary statistics for the given model object.
- `anova(model)` returns the analysis of variance table (including the F statistic, sum of squares, and mean squares) for a given fitted model object.