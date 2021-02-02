# Machine Learning Basics

Deep Learning Book [Ch. 5](https://www.deeplearningbook.org/contents/ml.html)

- Most deep learning algorithms are based on the stochastic gradient descent algorithm.
- The **capacity** of an algorithm is its ability to fit a wide variety of functions, and controls its likelihood of under and overfitting.
  - The **hypothesis space** is the set of all functions that the algorithm can select as being the solution.
  - The **Occam's razor** principle states that among competing hypotheses that explain observations equally well, we should choose the simplest one.
- **Regularization** involves modifying learning algorithms to express preferences for different solutions. It is intended to reduce an algorithm's generalization error (but not training error).
- Generally divide data into training and test sets, then subdivide training set into training and validation sets, with validation set used to "train" hyperparameters.

- Statistical **bias** is when the expected value of an algorithm's estimator ($E(\boldsymbol{\hat\theta})$) is not equal to the true value ($\boldsymbol{\theta}$). **Variance** measures how much we would expect an estimator to vary with independent resamples from the underlying data generating process.
  - Standard error is the square root of variance.
- **Consistency** of an estimator requires that the estimator converges to the true value as the number of training points goes to $\infty$.
- In the frequentist view of statistics, the true parameter value $\boldsymbol{\theta}$ is fixed but unknown, and the point estimate $\boldsymbol{\hat\theta}$ is a random variable that is a function of the (random) dataset. In the Bayesian view, $\boldsymbol{\theta}$ is a random variable while the dataset is viewed as not random (since it is observed).
- **Stochastic gradient descent** is the basis for most of deep learning. It uses a **minibatch** of data drawn uniformly from the training set to estimated the gradient (since the gradient is an expectation). This approach allows for efficient computation of the gradient at each step, even as the size of the training data grows very large.
  - Not guaranteed to find a local or global minimum in a reasonable amount of time, but can often find a low enough value to be useful.
- Deep learning arose to improve on simpler machine learning algorithms in high-dimensional spaces (which often have high computational costs) and to generalize to AI problems like speech and object recognition.
  - Deep learning allows for non-local generalization, which addresses the curse of dimensionality.
- A **manifold** is a connected region that in machine learning describes a connected set of points that can be approximated well by considering only a small number of degrees of freedom (dimensions) embedded in a higher-dimensional space.
- **Manifold learning** algorithms assume that most of $\R^n$ consists of invalid inputs and that interesting inputs occur only along a collection of manifolds containing a small subset of points.
  - For example, in images and text, random samples almost never form realistic images or sentences, even though it is theoretically possible that they could.