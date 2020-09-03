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
- Bootstrap is non-parametric, allowing us to estimate sampling distributions of a statistic without making assumptions about the form of the population.
  - For adaptive, nonlinear techniques (e.g. trees), estimating the number of effective parameters is difficult, so bootstrapping or cross-validation is preferable to AIC/BIC.

### Cross-Validation

## Class Notes

