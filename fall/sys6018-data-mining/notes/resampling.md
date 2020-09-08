# Resampling

### Bootstrap

Readings: ISL 5.2, ESL 7.11, [Bootstrapping Regression Models](https://socialsciences.mcmaster.ca/jfox/Books/Companion-1E/appendix-bootstrapping.pdf)

- The bootstrap can be used to quantify the uncertainty of an estimate or statistical learning method, and can be applied to a wide range of methods, even some for which measuring variability is otherwise difficult.
- Boostrapping involves repeatedly sampling observations from the original dataset (with replacement), estimating the parameter of interest, and calculating the standard error of those bootstrap estimates. The size of the bootstrap sample is the same as the size of the original training set.
  - For a parameter $\alpha$ and $B$ bootstrap samples, the standard error is calculated as $SE_B(\hat\alpha) = \sqrt{\frac{1}{B-1}\sum_{r=1}^{B}(\hat\alpha^{*r} - \frac{1}{B}\sum_{r'=1}^{B}\hat\alpha^{*r'})^2}$, where $\hat\alpha^{*r}$ is the $r^{th}$ bootstrap estimate of $\alpha$.
  - Bootstrap seeks to estimate conditional error, but typically only estimates prediction error well.
- If error is calculated based on how well bootstrap estimates predict the original training set, there is overlap between the train and test sets, making overfit predictions look better than they should.
  - One solution is the leave-one out bootstrap method, in which only predictions from bootstrap samples not containing that observation are tracked. The leave-one out bootstrap estimate of prediction error is defined as $\hat{Err}^{(1)} = \frac{1}{N}\sum_{i=1}^{N}\frac{1}{|C^{-i}|}\sum_{b \in C^{-i}}L(y_i, \hat{f}^{*b}(x_i))$. This approach suffers from upward training-set-size bias (similar to two-fold cross-validation).
  - The .632 estimator tries to alleviate the bias in the leave-one out bootstrap approach and is defined as $\hat{Err}^{(.632)} = 0.368\bar{err} + 0.632\hat{Err}^{(1)}$. This estimator works well in "light-fitting" situations, but not in overfit ones.
  - Due to the problems with the .632 estimator, the .632+ estimator is used to take the amount of overfitting into account. It is defined as $\hat{Err}^{(.632+)} = (1 - \hat{w})\bar{err} + \hat{w}\hat{Err}^{(1)}$, where $w = \frac{0.632}{1-0.368\hat{R}}$, $\hat{R} = \frac{\hat{Err}^{(1)} - \bar{err}}{\hat\gamma - \bar{err}}$, $\hat\gamma = \hat{p_1}(1 - \hat{q_1}) + (1 - \hat{p_1})\hat{q_1}$, $\hat{p_1}$ is the observed proportion of responses $y_i$ equaling 1, and $q_i$ is the observed proportion of predictions $\hat{f}(x_{i'})$ equaling 1.
- Bootstrap allows us to estimate sampling distributions of a statistic without making assumptions about the form of the population.
  - For adaptive, nonlinear techniques (e.g. trees), estimating the number of effective parameters is difficult, so bootstrapping or cross-validation is preferable to AIC/BIC.

### Cross-Validation

- Training error rate can dramatically underestimate the test error rate, but a designated test data set is not usually available. Cross-validation addresses this by holding out some observations during training, then calculating the error rate for those observations.
- The validation set approach splits the data into two sets: training and validation/test/holdout set.
  - Drawbacks: estimate of test error rate can be highly variable depending on which observations are in validation set; only a subset of observations used to fit the model.
- Leave one out cross-validation fits the model on all observations except one, calculates the test error rate for the held out observation, and repeats the process for all $n$ observations.
  - LOOCV has far less bias than validation set approach, and there is no randomness since it is performed for each observation.
- $k$-fold cross validation divides data into $k$ groups of equal size, and the model is fit on $k-1$ folds and tested on the remaining fold. The process is then repeated $k$ times.
  - LOOCV is the case when $k = n$. $k$-fold is computationally simpler than LOOCV.
  - $k$-fold cross-validation often gives more accurate estimates of test error rate than LOOCV due to bias-variance tradeoff. LOOCV is approx. unbiased, but has higher variance because the outputs are highly correlated. For small training sets, $k$-fold cross-validation tends to overestimate error (biased upward)
  - K-fold validation with $k$ = 5 or 10 is usually chosen to achieve the optimum balance of bias and variance.
- Cross-validation can be used for regression (with MSE) or classification (with number of misclassified observations).
- Cross-validation must be applied to the entire sequence of modeling steps: samples must be "left out" before any selection or filtering steps are applied.

## Class Notes

*September 3, 2020*

- Goal of bootstrap is to understand uncertainty in a test statistic.
- Traditional confidence intervals ($\hat{p} \pm$ margin of error) assume that $\hat{p}$ is normally distributed with mean equal to unknown true parameter $p$ (frequentist approach). Bayesian approach uses prior to generate a posterior distribution for the parameter given the data. Bootstrap provides a third approach using resampling.
  - Bootstrap result will be very similar to Bayesian result with uninformative priors.
- Bootstrap assumes that observed data (training data) are independent.
- Important to sample $n$ observations (same number as original data set) because the uncertainty in the test statistic is a function of $n$.
- Bootstrapped samples can be used to estimate the distribution of $\hat{p}$, or properties of the distribution like standard deviation.
  - Distribution will be centered on original $\hat{p}$ estimated from training data.

#### Basis Function Modeling

- A linear basis expansion is a sum of coefficients times basis functions. For example, a polynomial regression can be expressed as the sum of $\hat\beta_j x^j$ terms.
- Splines are a more flexible alternative than polynomial models that often provide better predictions. 
- Splines use basis expansion somewhat like dummy coding categorical variables to expand a single variable $x$ into $df$ new variables. Splines also have a degree and number of knots (knots = df - degree).

*September 8, 2020*

- Out-of-bag samples: observations not included in the bootstrap sample are called "out-of-bag." 
  - Out-of-bag error estimates performance of model.
  - What is expected number of observations that will not be in bootstrap sample (assume $n$ total observations)? 0.368$n$, when $n > \sim500$
- Tuning parameters are the "control knobs" of models, usually controlling the complexity of the model.
  - For KNN, the tuning parameter is $k$, the number of neighbors.
  - Model parameters are estimated given a certain value of the tuning parameters.
  - Optimal tuning parameters minimize the expected prediction error.
- Training data is not a good for estimating prediction error. Training error always decreases as complexity increases.
- Model selection is estimating the performance of different models to choose the best one. Model assessment is estimating prediction error on new data once a best model is chosen.
  - If enough data is available, it can be separated into training, validation (selection), and testing (assessment) sets. Training used to estimate model parameters, validation used to estimate tuning parameters, and testing used to estimate final predictive performance.
  - Not enough training data leads to high variance in estimates of model parameters. Not enough testing data leads to poor performance estimation and model selection.
  - After validation/selection of optimal tuning parameters, refit model trained on training+validation data, then test on assessment data.
    - Alternative to refitting on training+validation is to create an ensemble model from the $k$ fold models.
- Three approaches to estimating prediction error: predict on hold-out data, make a mathematical adjustment to training error to better estimate test error, or use resampling methods (cross-validation, bootstrap).
  - Single holdout sets may result in a split that poorly represents the data generating process. The chance of bad split is reduced when $n-m$ and $m$ are both large.
  - AIC/BIC, adjusted $R^2$, and Mallow's $C_p$ are methods that adjust the training error to account for potential overfitting. AIC & BIC use log likelihood (loss function) plus a penalty according to the complexity of the model, and want to minimize loss+penalty. General guideline: use AIC when interested in predictive performance and BIC when interested in inference.
  - Cross-validation is a repeated holdout-set analysis that allows you to use more data for both training & testing.
- Repeated cross-validation and repeated train/test splits give better accuracy/more confidence in estimate of model performance.