# Ensembles

Readings: ESL 10.1-10.9; LogitBoost [paper](https://web.stanford.edu/~hastie/Papers/AdditiveLogisticRegression/alr.pdf)

### Boosting Methods

- Combines the outputs of many weak classifiers sequentially to produce a powerful committee.
  - Even a classifier (e.g. a stump) that alone is worse than random guessing can have a low error rate with boosting.
  - More generally, boosting fits an additive expansion of elementary basis functions. Mathematically this is represented as $f(x) = \sum_{m=1}^M \beta_m b(x; \gamma_m)$, where $\beta_m$ are the expansion coefficients and $b(x; \gamma_m)$ are usually simple functions of $x$ with parameters $\gamma$.
    - Same general technique used in regression splines and neural nets.
    - Generally fit by minimizing a loss function on training data.
- Most popular boosting algorithm is AdaBoost.M1, sometimes called "Discrete AdaBoost."
  - Classifiers are trained on weighted versions of the dataset (uses -1 and 1 instead of 0 and 1 classes) and combined using a weighted majority vote (more accurate classifiers get higher weights).
  - At each iteration, the misclassified observations from the previous step are weighted more heavily (and vice versa).
  - "Real AdaBoost" is modified to return a real number between -1 and 1 rather than a discrete classification.

- Forward stagewise additive modeling sequentially adds new basis functions based on which minimizes loss at the current step, without adjusting parameters and coefficients of previously-added basis functions.
  - Squared error loss is generally not good for classification.
- AdaBoost.M1 is forward stagewise additive modeling with exponential loss $L(y, f(x)) = exp(-y f(x))$.
  - Exponential loss with AdaBoost continues to decline with number of boosting iterations even after the misclassification rate hits zero. Exponential loss is more sensitive to changes in estimated class probabilities.
- The population minimizer of exponential loss is $f^* (x) = \frac{1}{2}$log$\frac{P(Y=1 | x)}{P(Y = -1 | x)}$, or one-half the log-odds of $P(Y=1 | x)$. The deviance (cross-entropy/binomial negative log-likelihood) loss function has the same population minimizer.
  - Exponential loss and deviance do not have the same solution for finite (not full population) data sets.
  - Both penalize increasingly negative margin values (incorrect predictions) more heavily than they reward increasingly positive margins (correct predictions), but exponential loss increases this penalty exponentially instead of linearly.
    - As a result, deviance is a more robust loss metric to noisy settings (or to misspecification of class labels in training data) than exponential loss.
    - Squared error loss is inappropriate for classification because it is not monotone decreasing (like deviance and exponential loss are), which penalizes increasing certainty of correctly classified observations.
- For regression, absolute loss is more robust than squared error loss to outliers and long-tailed error distributions.
  - Huber loss criterion is one alternative to squared error loss that is very robust to outliers.
  - While absolute loss and deviance are more robust loss metrics, there are no simple, fast algorithms for solving them.
- Among predictive data mining techniques, trees are the best-suited for "off the shelf" use without significant pre-processing, since they are able to scale, handle mixed data types and missing values, perform feature selection, and be robust to outliers, while still being relatively easily interpretable. However, they aren't as accurate as some methods.
  - Boosting improves the accuracy of trees but sacrifices some speed, interpretability, and (for AdaBoost) robustness to overlapping class distributions.
  - Gradient boosted models address the sacrifices of boosting to provide an effective off-the-shelf model.

## Class Notes

*October 22, 2020*

- Ensemble models combine predictions from several individual models (also called base learners). 
  - Bagging and random forests (variance reducers) and boosting (bias reducer) are examples of ensemble models.
- Ensemble approaches differ in which base models are used and how they are combined.
  - Helpful to think about how each of these two decisions affect bias and variance.
- Sub-bagging is a variation of bagging that uses sub-samples without replacement. Can be good with large data to speed up computation.
- Bragging is like bagging but using median instead of mean to combine predictions. Bumping chooses best model instead of averaging (essentially finding training data with lowest loss, i.e. that best represents the full data).
- Model selection is equivalent to model averaging with all weights equal to 0 except for one weight equal to 1.
- BIC is a very good approximation of -2 times Bayesian log likelihood (convenient for simplifying computation). Bayesian Model Averaging uses these BIC/AIC estimates as weights for combining models.
  - If prediction is the goal, generally want to use AIC.
- Stacking combines base models as a weighted sum where the weights don't need to be non-negative or sum to 1.
  - Weights found using out-of-sample predictions.
  - Helps prevent overfitting, as overfit models should receive a low weight.