# Regularization

Deep Learning Book [Ch. 7](https://www.deeplearningbook.org/contents/regularization.html)

- Regularization aims to reduce test error (improve generalization to new input data), even if training error increases some.
  - Designed to reduce overfitting.
- One method of regularization involves parameter norm penalties (e.g. ridge regression with the $L^2$ norm). 
  - In neural nets, this penalty usually applies only to the weights, not the biases or activation functions.
  - Only directions along which the parameters contribute signiﬁcantly to reducing the objective function are preserved relatively intact. In directions that do not contribute to reducing the objective function, a small eigenvalue of the Hessian tells us that movement in this direction will not signiﬁcantly increase the gradient.
  - $L^2$ regularization is equivalent to MAP Bayesian inference with a Gaussian prior on the weights.
- Many linear models involve inverting $\boldsymbol{X^T X}$, which can be singular when the data-generating distribution has no variance in some direction, or when there is no observed variance in some direction due to fewer rows than columns in $\boldsymbol{X}$. Regularization can help by inverting $\boldsymbol{X^TX} + \alpha\boldsymbol{I}$, which is always invertible.
- Dataset augmentation (generating additional fake training data) is easiest for classification, as it can be done by transforming the $\boldsymbol{x}$ inputs from the existing training data.
  - Especially useful in object recognition, where transformations such as translation by a few pixels, rotation, and scaling can generate new training examples. Must be careful to avoid transformations that would prevent algorithm from distinguishing between 6 and 9, for example.
  - Another technique involves injecting random noise into neural net inputs and/or hidden unit.
    - Noise can also be added to the weights to reflect a Bayesian uncertainty in the model weights.
- Label smoothing assumes that in a training set, some small constant proportion $\epsilon$ of the labels will be incorrect. It addresses this by replacing hard 0/1 targets with softmax targets of $\frac{\epsilon}{k-1}$ and $1-\epsilon$ for a classification problem with $k$ classes and using standard cross-entropy loss.
- Semi-supervised learning assumes that examples that cluster tightly in the input space should be mapped to similar outputs.
- Multitask learning uses the prior assumption that among the factors that explain the variations observed in the data associated with the diﬀerent tasks, some are shared across two or more tasks (usually two predictions from the same input data).
- Early stopping is the most popular form of regularization in deep learning due to its effectiveness and simplicity.
  - Doesn't require changes to learning procedure, objective function, or allowable parameter values.
  - Requires a validation set.
  - Equivalent to $L^2$ regularization with a linear model with quadratic error and gradient descent.
- Parameters can also be regularized to be close to another set of parameters, either through a norm penalty or by forcing sets of parameters to be equal (parameter sharing).
  - CNNs use parameter sharing across image locations in order to identify an object regardless of where in the image it appears.
- Representational regularization imposes penalties that encourage sparsity in a representation of the data $\boldsymbol{x}$ rather than in the parameters.
- Ensemble methods like bagging (bootstrap aggregating) average several models to make predictions, which works because different models don't make all the same errors on the test set.
  - Bagging uses the same kind of model, objective function, and training algorithm, but uses different datasets sampled with replacement from the original dataset.
  - Randomness in neural net initialization makes model averaging beneficial.
  - Powerful and reliable method, but discouraged in benchmarking for scientific papers.
- Dropout involves training an ensemble consisting of subnetworks of a base network, where each subnetwork has some non-output units removed.
  - Units removed by multiplying by zero.
  - Less computationally expensive than bagging, which involves training multiple models and evaluating each on each test example.
  - Use minibatch approach such as SGD, and apply a different mask to units for each minibatch (different dropout units for each).
  - Probability of including each unit is a hyperparameter, usually 0.8 for input units and 0.5 for hidden units. This randomly selects a subnetwork.
  - Unlike bagging, dropout models are not all independent but share parameters.
  - Using the geometric mean allows for good approximation to predictions for the ensemble at the cost of only one forward propagation.
  - Weight scaling inference rule approximates ensemble predictions by multiplying weights by the probability of including the unit. Not exact for models with nonlinearities, but often works well in practice.
  - More effective than weight decay, filter norm constraints, and sparsity regularizations. May be combined with other techniques for better performance.
  - Works well with nearly any model that can be trained with SGD.
- Adversarial training regularizes by training on adversarially perturbed images from the training set.
  - Encourages model to be locally constant and to avoid sensitive locally linear behavior.
  - Virtual adversarial examples have labels provided by a trained model rather than a true label.
  - Assumes that different classes lie on different manifolds, and that small perturbations shouldn't result in jumping from one class manifold to another.
- The tangent distance algorithm is a nonparametric nearest neighbor algorithm that uses distance between manifolds rather than Euclidean distance. Approximates the manifold using the tangent plane at $\boldsymbol{x}_i$.
  - Based on the assumption that examples on the same manifold are from the same category.
- The tangent prop algorithm adds a constraint to a neural net to require the gradient to be orthogonal to the known manifold tangent vectors at $\boldsymbol{x}$.
  - Tangent vectors derived a priori from formal knowledge of the effects of transformations.
  - We expect the classiﬁcation function to change rapidly as it moves in the direction normal to the manifold, and not to change as it moves along the class manifold.
  - Closely related to dataset augmentation: prior knowledge encoded by specifying a set of transformations that shouldn't alter the output. Dataset augmentation works better with ReLUs since tangent prop regularizes against infinitesimal perturbations, and ReLU derivatives can only shrink by turning off or shrinking weights, not by shrinking derivatives.
  - Autoencoders can estimate manifold tangent vectors.

### Video: Regularization Strategies for Deep Learning

- Model capacity is its ability to fit a wide variety of functions. Low capacity may lead to underfitting, while high capacity may lead to overfitting.

- **Parameter Norm Penalties** limit model capacity by adding a parameter norm penalty to the loss function.

  $J(\boldsymbol{w; X, y}) = L(\boldsymbol{\hat y, y}) + \lambda \Omega(\boldsymbol{w})$, where $L$ is the regular loss function, $\Omega$ is the norm penalty term, and $\lambda$ is a hyperparameter controlling the amount of regularization (large $\lambda = more regularization).

  - $L^2$ regularization (aka ridge regression or weight decay) uses $\frac{\lambda}{2} ||\boldsymbol{w}||^2$ as the penalty term.
    - In a single gradient descent step, this shrinks the weight vector before the gradient update ($\boldsymbol{w}\leftarrow (1-\alpha\lambda)\boldsymbol{w} - \alpha \Delta_{\boldsymbol{w}}L(\boldsymbol{\hat y, y})$ ).
  - $L^1$ regularization (aka lasso regression or Manhattan distance) uses $\lambda ||\boldsymbol{w}||$ as the penalty term.
    - Makes the parameters become sparse (some set to zero). Causes a subset of network weights to become zero (dead neurons whose signal may be discarded).
  - Elastic net is a middle ground between ridge and lasso, containing both penalties and a ratio parameter specifying how much each factors in.

- **Dataset Augmentation** is a regularization strategy that trains a model on more ("fake") data.

  - Particularly effective in image object recognition, where "fake" data can be generated by rotating/cropping/etc images.
  - Can inject random noise into inputs.
  - Label smoothing regularizes a model on a softmax by discouraging hard classifications but encouraging correct classifications.

### Video: Regularization - Parameter Sharing, Early Stopping, Ensemble Learning

- **Multitask Learning** (aka parameter sharing) improves generalization by pooling examples arising out of several tasks.
  - When different supervised tasks share the same input. Lower layers capture generic params shared across tasks, while upper layers capture task-specific params.
- **Early Stopping** stops training when validation error begins to rise as number of epochs continues.
  - Patience parameter $p$ is how many times validation error can worsen before stopping (to allow for some noise).
    - Efficient hyperparameter selection algorithm.
    - Reduces computational cost and controls model capacity.
    - Can be used with other regularization strategies.
    - Analytically equivalent to $L^2$ regularization, but better because it doesn't require tuning of hyperparameter $\lambda$.
- **Ensemble Learning** (bagging) combines several models to reduce generalization error.
  - Works because different models don't usually make all the same mistakes. 
    - If errors of all models are perfectly correlated, the expected squared error of an ensemble is equal to the variance of each model, and the ensemble doesn't help at all. If errors are perfectly uncorrelated, ensemble error decreases linearly with number of members.
  - Neural nets can benefit from model averaging even if they are trained on the same data due to differences in random weight instantiation, random selection of training mini batches, etc.
  - Model averaging is discouraged in benchmarking algorithms for scientific papers.

### Video: Regularization - Dropout & Tangent Prop

- **Dropout** is an approximation to bagged ensemble of exponentially many neural nets that trains the ensemble consisting of all sub-networks that can be formed by removing non-output units from an underlying base network.
  - Alternative to bagging, which can be computationally and memory expensive when each model is large.
  - Dropout rate $p$ is probability at every training step that each neuron drops out and gets ignored until the next step ($p=0.5$ is common).
  - More effective than weight decay or sparsity constraints.
- **Tangent Prop** approximates the tangent distance algorithm using the tangent plane of a manifold at a point.
  - Tangent distance is a nonparametric nearest neighbor method in which the distance metric is derived from knowledge of the manifolds, based on the assumption that points on the same manifold are in the same class.
    - Many ML algorithms attempt to overcome the curse of dimensionality by assuming that data lies near a low-dimensional manifold.
  - Adds an extra penalty to make outputs of a neural net locally invariant to known factors of variation.
  - Also used in reinforcement learning.
  - Expect to quickly move away from the manifold when following the normal vector, but stay near the manifold when following the tangent.
  - Tangent prop is intellectual elegant, but dataset augmentation may work better in practice.

### Class Notes

*February 22, 2021*

- Horseshoe shrinkage (Bayesian method) is a constrained optimization designed to cause preferential shrinkage to only some parameters.
- Dropout attempts to get the same variance reduction as bagging. Dropout essentially performs bagging by forcing nodes to learn/cope with other nodes turned off.
  - Each pass trains a different model - different models share different subnetworks.
- Early stopping is not exactly the same as $L^2$ regularization for all models, but generally leads to the same result.