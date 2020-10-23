# Ensembles

Readings: ESL 10.1-10.9; LogitBoost [paper](https://web.stanford.edu/~hastie/Papers/AdditiveLogisticRegression/alr.pdf)

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