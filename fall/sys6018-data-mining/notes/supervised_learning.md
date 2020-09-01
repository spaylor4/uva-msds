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
- *Qualitative* variables are typically represented numerically by codes, often 0/1 or -1/1 for binary qualitative variables. These codes are sometimes referred to as *targets*.
- Linear least squares model fits $\hat{Y} = X^T\hat\beta$ to minimize the residual sum of squares RSS($\beta$) = $\sum_{i=1}^{N}(y_i - x_i^T\beta)^2$.
  - The least squares estimates of the coefficients are $\hat\beta = (X^TX)^{-1}X^Ty$.
- $k$-nearest neighbor models use the $k$ observations in the training set nearest to $x$ to predict $\hat{Y}$ using $\hat{Y}(x) = \frac1k\sum_{x_i\in N_k(x)}y_i$, where $N_k(x)$ is the neighborhood of the $k$ closest points to $x$.
  - The closeness metric is often defined as Euclidean distance.
  - The case of $k=1$ classification corresponds to a *Voronoi tesselation* of the training data, where each observation has an associated tile bounding the region for which it is the closest input point.
  - Error on training data set will always be 0 for $k=1$, and will increase as $k$ increases. Therefore the use of an independent test data set is important for comparing methods.
  - Although KNN has a single parameter $k$, the effective number of parameters is $N/k$. If neighborhoods were non-overlapping, there would be $N/k$ neighborhoods, each with one parameter fit (the mean of the neighborhood).
- Linear least square vs. $k$-nearest neighbors:
  - Linear model yields stable but possibly inaccurate predictions (due to assumptions about structure), while KNN often makes accurate predictions that can be unstable.
  - Linear model has low variance and potentially high bias, while KNN has high variance and low bias. Linear decision boundary is very smooth, while KNN can be very wiggly.
  - KNN's effective number of parameters $N/k$ is generally larger than the $p$ parameters in a least squares linear fit.
  - Linear least squares assumes $f(x)$ is well-approximated by a globally linear function. KNN assumes $f(x)$ is well-approximated by a locally constant function.
- Kernal methods, local regression fits, and neural networks are enhanced procedures that draw from linear least squares and KNN.
- Generally for developing models, we need a loss function for penalizing errors in prediction.
- By far the most common loss function for regression is squared error loss, defined as $L(Y, f(X)) = (Y - f(X))^2$, sometimes called the $L_2$ loss function. The function that minimizes the expected value of squared error loss is the conditional expectation $f(x) = E(Y | X = x)$.
  - *Mean squared error* (MSE) is the most commonly used measure of fit for regression. MSE = $\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{f}(x_i))^2$.
    - Usually care about test MSE rather than training MSE, and select model with lowest test MSE. 
    - Test MSE can be much larger than training MSE, in which case the model is overfitting the data. This is because training MSE always decreases as model flexibility increases, but test MSE does not.
  - KNN approximates the expectation by averaging over sample data and approximates conditioning at a point to conditioning on some region "close" to a point, since there is often only one observation at each point $x$. KNN uses $\hat{f}(x) = Ave(y_i | x_i \in N_k(x))$.
  - Least squares does not condition on $X$, but rather uses our knowledge of a functional relationship to pool over values of $X$.
  - For the $L_1$ loss function $L(Y, f(X)) = E(|Y - f(X)|)$, the solution that minimizes loss is $\hat{f}(x) = median(Y | X=x)$. $L_1$ loss is used less due to discontinuities in its derivatives.
- Most commonly-used loss function for classification is the zero-one loss function, where each misclassification is penalized one unit. Called the *error rate* and is equal to $\frac{1}{n}\sum_{i=1}^{n}I(y_i \not= \hat{y}_i)$. As with regression, the a low test error rate indicates a better model fit.
- The *Bayes classifier* for a categorical variable $G$ that can assume values in $\mathcal{G}$ using the 0-1 loss function is $\hat{G}(x) = \mathcal{G}_k$ if Pr$(\mathcal{G}_k |X=x) = max_{g \in \mathcal{G}}$Pr$(g|X=x)$. 
  - The error rate of this classifier is called the *Bayes rate* or *Bayes error rate*, which is the lowest possible test error rate. The Bayes error rate is analogous to the irreducible error. 
  - The *Bayes decision boundary* is the dividing line between the different class predictions.
  - Don't know the Bayes classifier for real data. KNN is one method that atttempts to estimate the conditional distribution of $Y$ given $X$ and classify accordingly.
- Bias-variance tradeoff: variance is the amount by which $\hat{f}$ would change if estimated with a different training set, while bias refers to error introduced by approximating a real-life problem with a model (since a model likely oversimplifies the problem). More flexible models generally have higher variance and lower bias.
  - The expected test MSE is equal to variance + bias$^2$ + variance of error terms. The variance of error terms is irreducible, so the best test MSE will have the lowest combination of bias and variance.
  - It is easy to find a model with either low bias or low variance, but much harder to find one with both.
  - Training MSE always declines as flexibility increases, but test MSE follows a U-shape.

## Class Notes

*August 25, 2020*

#### Linear Models

- Root mean squared error RMSE = $\sqrt{MSE} = \frac{\sqrt{RSS}}{\sqrt{n}}$
- Simple linear model doen't have very accurate predictions if relationship between variables is non-linear. Sometimes, this can be addressed by adding polynomials terms.
  - In R, the `poly()` function is convenient for modeling polynomial terms. For example, `poly(x, degree = 2)` creates an $x^2$ term.
  - The complexity (or effective degrees of freedom) of a model is the number of parameters that must be estimated. For example, a quadratic model has 3 parameters: intercept, slope, and quadratic term. For a polynomial model, the degree is a tuning parameter.

#### K-Nearest Neighbor Models

- KNN is a non-parametric local model, meaning that it only uses the training data in the vicinity of $x$. Only the $k$ closest $y$'s are used to generate a prediction - the simple mean of the $k$ nearest observations.
  - If $k = n$, the estimate will be $\bar{y}$. This is an intercept-only model, the simplest KNN model possible.
  - If $k = 1$, the estimate will be the nearest observation. This is the most complex KNN model possible.
  - The complexity of a KNN model increases as $k$ decreases.
  - Must choose a suitable distance measure (e.g. Euclidean).
- Curse of dimensionality: with more features, distance to neighbors grows exponentially. In high dimensions, most neighbors aren't very "local."
- `knn.reg()` function from `FNN` package fits a KNN model.
- Effective degrees of freedom (edf) of a KNN model is $n/k$.
  - Measure of complexity used to compare to parametric models (edf is approx. number of parameters estimated).