# Classification

Readings: ISL 4.1-4.6; ESL 4.1-4.4, 6.6.3

### Logistic Regression

- Estimates the probability that the response belongs to a particular class. Preferable to attempting linear regression for classification because it will only give predictions between 0 and 1.
  - A threshold is used to turn the predicted probabilities into classifications.
  - Logistic function $P(X) = \frac{e^{\beta_0 + \beta_1x}}{1 + e^{\beta_0 + \beta_1x}}$ forms an S-shaped curve between 0 and 1 over the range of $X$ (for a single predictor variable).
  - Odds = $\frac{p(X)}{1 - p(X)}$ and log-odds/logit = log($\frac{p(X)}{1 - p(X)}$). The logit is a linear function of $X$.
- Maximum likelihood estimation used to estimate regression coefficients for logistic regression (as opposed ot least squares estimation used in simple linear regression).
- Logistic regression has extensions for more than two classes, but is generally only used for a two-class prediction. Can be split into a set of binary classifications ("one-vs-rest").

### Linear Discriminant Analysis

- Popular for classification when there are more than two categories.
- Assumes that observations within each class come from Gaussian distributions with different mean vectors and the same variance (or variance-covariance matrix in the case with multiple predictors).
- Bayesian approach: model $P(Y = k | X = x)$ using Bayes theorem by first modeling $P(X | Y)$.
- LDA is more stable than logistic regression.
  - Parameter estimates can vary in logistic regression with small changes in data when classes are well-defined and when $n$ is small and the distribution of the predictors is approx. normal.
- Estimate of the prior is the fraction of observations in the training data in a particular class.
- Bayes classifier assigns an observation to the class with the largest posterior probability. LDA approximates the Bayes classifier.
- For rare events (unbalanced data), a null classifier (classifying all observations as one class) will have a low error rate, so it is often helpful to look at a confusion matrix. May need to adjust threshold in case of unbalanced data.
  - Bayes classifier has lowest total error rate, so LDA needs to be modified by changing the threshold when certain errors are worse than others.

- Quadratic discriminant analysis is a similar method to LDA, but assumes that each class has its own variance-covariance matrix.
  - LDA less flexible than QDA, so it has lower variance and higher bias.
  - LDA generally better when there are relatively few training observations; QDA generally better when training data is large or when the assumption of a common variance-covariance matrix is clearly not met.
- Both LDA and logistic regression produce linear decision boundaries, but with different fitting procedures: logistic regression uses maximum likelihood, while LDA uses the estimated mean and variance from a normal distribution.
- KNN works well when decision boundary is very non-linear (since it is a non-parametric method). QDA is a compromise between KNN and LDA in terms of flexibility.

### Naive Bayes Classifier

- Assumes that for a given class, the features $X_k$ are independent.
  - Generally not true, but simplifies estimation dramatically, making Naive Bayes especially suitable for high-dimensional feature spaces.
  - This assumption may increase bias, but saves variance.
- Similar form to generalized additive model. Naive Bayes relationship to generalized additive model is analogous to the relationship between LDA  and logistic regression.

## Class Notes

*September 17, 2020*

- Linear regression is appropriate in some cases for binary classification. Can be faster to compute for large datasets.
- $k$ nearest neighbors can be used for classification with continuous predictors.
  - Larger $k$ gives a smoother decision boundary.
  - Can use categorical variables with some transformations and scaling to make distance measurement applicable.
  - Works well in multi-class scenario (natural fit).
- Can use penalized logistic regression (ridge, lasso, best subsets, elastic net) similarly to with linear regression.
  - Need parameter `family = "binomial"` in `glm` and `glmnet` functions.
- Logistic regression estimates the posterior probability $P(Y = 1 | X = x)$.
- Evaluating classification models: risk is expected loss (expected prediction error); want to minimize EPE on test data.
- In some binary classification settings (e.g. cancer diagnosis), a false negative is much worse than a false positive.
  - Zero-one loss treats false positives and false negatives the same.
- Squared error: linear regression; absolute error: quantile regression; Bernoulli negative log-likelihood: logistic regression.