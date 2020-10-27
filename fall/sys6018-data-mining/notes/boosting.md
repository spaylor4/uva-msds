# Boosting

Readings: ESL 10.10-10.14; XGBoost [paper](https://arxiv.org/pdf/1603.02754.pdf)

- Gradient boosting approximates the prediction function that minimizes loss. Numerical optimization does so through a series of incremental computational steps $\mathbf{h}_m$, summing the component vectors to get $\mathbf{f}_M = \sum_{m=0}^M \mathbf{h}_m$, where $\mathbf{f}$ is a vector containing $f(x_i)$ for all $i$ data points.

- Steepest descent is a greedy strategy that chooses $\mathbf{h}_m = -\rho_m \mathbf{g}_m$ where $\rho_m$ is a scalar and $\mathbf{g}_m$ is the gradient of the loss function evaluated at the previous stage $\mathbf{f}_m$. 

  - Will minimize loss on the training data, but since the gradient is defined only for training data points, doesn't generalize to new data.
  - Gradient boosting addresses this issue by fitting a tree to the negative gradient values at each iteration.

- The gradient boosting algorithm has the following steps:

  1. Initialize $f_0(x)=$arg min$_\gamma \sum_{i=1}^N L(y_i, \gamma)$

  2. For $m = 1$ to $M$:

     a. For $i=1$ to $N$: compute the gradient $r_{im} = -[\frac{\partial L(y_i, f(x_i))}{\partial f(x_i)}]_{f = f_{m-1}}$

     b. Fit a regression tree to the targets $r_{im}$ giving terminal regions $R_{jm}, j = 1, 2, ..., J_m$

     c. For $j$ in 1 to $J_m$, compute $\gamma_{jm} =$arg min$_\gamma \sum_{x_i \in R_{jm}} L(y_i, f_{m-1}(x_i) + \gamma)$

     d. Update $f_m(x) = f_{m-1}(x) + \sum_{j=1}^{J_m} \gamma_{jm} I(x \in R_{jm})$

  3. Output $\hat{f}(x) = f_M(x)$

- The gradient boosting algorithm for classification is similar, but repeats step 2 one time for each of the $K$ classes.

- Tree size $J_m$ is a tuning parameter. 

  - $J=2$ gives single split stumps. 
  - Interactions of $J-1$ variables are possible for tree size $J$. 
  - Generally $J$ between 4 and 8 works well, so 6 is a good starting point.

- Number of boosting iterations $M$ is the other tuning parameter.

  - $M$ subject to overfitting on training data, so usually want to use a validation set to choose optimal value of $M$.
  - Alternately can use shrinkage to regularize estimates by scaling each tree's contributions by a factor of $\nu$, changing step 2d in the algorithm to $f_m(x) = f_{m-1}(x) + \nu\sum_{j=1}^{J_m} \gamma_{jm} I(x \in R_{jm})$.
    - Smaller values of $\nu$ require larger values of $M$, but produce better test error.

- Stochastic gradient boosting builds the tree at each step using a fraction $\eta$ (often $\eta=1/2$) of the training observations (a subsample without replacement). Doing so reduces computing time and can sometimes give more accurate models.

  - Can be used in averaging of boosting models where improved computation speed is needed.

- Boosting is much less interpretable than a single tree, but does provide a measure of relative importance of the predictor variables.

  - Customary to scale these relative values so that the largest is equal to 100.

- Partial dependence plots can be used to look for interaction effects between variables.

- Gradient boosting implemented in R's `gbm` package.

## Class Notes

*October 27, 2020*

- Boosting fits base models sequentially and is primarily a bias reducer.
- Boosting models will overfit as number of iterations increases past a certain point.
  - When misclassification is the error metric, overfitting may not matter for performance (can sometimes get away with overfitting). Exponential loss overfits very quickly as number of iterations increases.
- AdaBoost was original boosting algorithm.
  - Models that fit best receive largest ensemble/model weights.
  - Observation weights updated at each stage to increase weights of misclassified observations.
- R `ada` package implements AdaBoost.
- Gradient boosting sequentially fits to pseudo residuals (negative functional gradient of the loss function) rather than to weighted observations as in AdaBoost.
  - Can be used with many different loss functions.
  - Can be used for classification, regression, survival analysis, ranking, etc.
- $L_2$ boosting is based on the squared error loss function.
  - The negative gradients are the residuals in this case.