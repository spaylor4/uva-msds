# Supervised Learning

Readings: ISL 1, 2.1; ESL 1, 2.1-2.4

- Statistical learning involves estimating the systematic information ($f(X)$) that some set of predictors/features ($X$) provide about a response ($Y$). 
- Estimating $f$ can be used for prediction (in which case the actual form of $f$ is not important) and for inference (in which the form of $f$ is used to answer questions about the relationship between the response and various predictors).
  - Linear models are usually more easily interpretable for inference, but may or may not provide the most accurate predictions. Generally, as models get more flexible, they also get less interpretable. Highly flexible models are also more susceptible to overfitting.
- *Parametric* statistical learning methods involve estimating parameters for an assumed form (e.g. linear) of a model $f$. *Non-parametric* methods do not make explicit assumptions about the form of $f$.
  - A downside of parametric methods is that if the chosen form of $f$ differs significantly from the true $f$, the model will not fit the data well.
  - A downside of non-parametric methods is that they require a much larger number of observations $n$ to accurately estimate $f$.
- *Supervised* learning problems have a response variable associated with the data, while *unsupervised* ones do not.
  - Clustering is one example of unsupervised learning.
- Generally, problems with a quantitative response variable are called *regression* problems, while those with a qualitative response are called *classification* problems.

### Linear Models

- Root mean squared error RMSE = $\sqrt{MSE} = \frac{\sqrt{RSS}}{\sqrt{n}}$
- Simple linear model doen't have very accurate predictions if relationship between variables is non-linear. Sometimes, this can be addressed by adding polynomials terms.
  - In R, the `poly()` function is convenient for modeling polynomial terms. For example, `poly(x, degree = 2)` creates an $x^2$ term.
  - The complexity (or effective degrees of freedom) of a model is the number of parameters that must be estimated. For example, a quadratic model has 3 parameters: intercept, slope, and quadratic term. For a polynomial model, the degree is a tuning parameter.

### K-Nearest Neighbor Models

- KNN is a non-parametric local model, meaning that it only uses the training data in the vicinity of $x$. Only the $k$ closest $y$'s are used to generate a prediction - the simple mean of the $k$ nearest observations.
  - If $k = n$, the estimate will be $\bar{y}$. This is an intercept-only model, the simplest KNN model possible.
  - If $k = 1$, the estimate will be the nearest observation. This is the most complex KNN model possible.
  - The complexity of a KNN model increases as $k$ decreases.