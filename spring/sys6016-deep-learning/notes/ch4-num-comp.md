# Numerical Computation

Deep Learning Book [Ch. 4](https://www.deeplearningbook.org/contents/numerical.html)

- Because computers represent continuous numbers with a finite number of bits, computation errors can result from **underflow** (numbers near zero being rounded to zero) or **overflow** (large numbers approximated as $\infty$ or $-\infty$).
  - Theano and other libraries automatically deal with these issues.
- Deep learning often minimizes functions with multiple inputs, but still only with one scalar output. Because this makes optimization difficult, we often accept a very low value of $f$ that is not truly a minimum.
- The **gradient** of a function with multiple inputs is the vector of partial derivatives with respect to each input and is denoted $\Delta_x f(\boldsymbol{x})$.
  - Critical points in multiple dimensions occur when every element of the gradient equals zero.
- **Gradient descent** (or method of steepest descent) uses the derivative of a function to minimize $f(x)$ by moving $x$ in small steps in the opposite sign of the derivative.
  - Proposes new point $\boldsymbol{x' = x} - \epsilon\Delta_x f(\boldsymbol{x})$, where $\epsilon$ is the **learning rate**, a positive scalar determining the size of the step.
- When a function has vector input and vector output, the **Jacobian matrix** contains all the partial derivatives.
  - For a function $\boldsymbol{f}: \R^m \times \R^n$, the Jacobian matrix $\boldsymbol{J} \in \R^{n \times m}$ is defined as $J_{i, j} = \frac{\partial}{\partial x_j}f(\boldsymbol{x}_i)$.
- The **Hessian matrix** contains the second derivatives of a function with multiple input dimensions. It is defined as $\boldsymbol{H}(f)(\boldsymbol{x})_{i, j} = \frac{\partial^2}{\partial x_i \partial x_j} f(\boldsymbol{x})$.
  - The Hessian is the Jacobian of the gradient.
  - The differential operations $\partial x_i$ and $\partial x_j$ are commutative when the second partial derivatives are continuous, so $H_{i, j} = H_{j, i}$ (Hessian is symmetric) at such points.
  - The second derivative in a direction specified by a unit vector $\boldsymbol{d}$ is given by $\boldsymbol{d^T H d}$. When $\boldsymbol{d}$ is an eigenvector of $\boldsymbol{H}$, the  second derivative in that direction is equal to the corresponding eigenvalue. The maximum (or min) eigenvalue is the maximum (or min) second derivative.
  - The Hessian can be used to determine if critical points are local max/min or saddle points. If the Hessian is positive definite (all eigenvalues positive), the point is a local minimum. If it is negative definite, the point is a local max.
  - The condition number of the Hessian measures how much the multiple second derivatives at a point differ from each other. When the Hessian has a poor condition number, gradient descent performs poorly.
- **Newton's method** uses information from the Hessian to guide the search by using a second-order Taylor series expansion to approximate $f(\boldsymbol{x})$ near some point $\boldsymbol{x}^{(0)}$. This method solves the Taylor series expansion for the critical point $\boldsymbol{x}^* = \boldsymbol{x}^{(0)} - \boldsymbol{H}(f)(\boldsymbol{x}^{(0)})^{-1}\Delta_x f(\boldsymbol{x}^{(0)})$.
  - When $f$ is a positive definite quadratic function, applying this equation will jump to the minimum.
  - When $f$ can be locally approximated by a positive definite quadratic function, this function can be applied iteratively to update the approximation more quickly than with gradient descent.
  - Newton's method is only appropriate when near a minimum critical point (all values of Hessian are positive).
- Optimization algorithms that only use the gradient are called **first-order optimization algorithms**, while those that also use the Hessian are called **second-order optimization algorithms**.
- Functions that are **Lipschitz continuous** are those whose rate of change is bounded by a Lipschitz constant: $\forall\boldsymbol{x}, \forall\boldsymbol{y}, |f(\boldsymbol{x}) - f(\boldsymbol{y})| \le \mathcal{L}||\boldsymbol{x - y}||_2$.
  - Deep learning sometimes limits ourselves to these functions because they quantify the assumption that a small change in input will lead to a small change in output (i.e. in gradient descent).
- In **constrained optimization**, we wish to find the max/min value of a function over values of $\boldsymbol{x}$ in some set $\mathbb{S}$ (called feasible points) rather than over all possible values of $\boldsymbol{x}$.
  - Often impose a norm constraint, such as $||\boldsymbol{x}|| \le 1$.
- The **KKT** (Karush-Kuhn-Tucker) approach to constrained optimization involves the **generalized Lagrangian** (or generalized Lagrange function).
  - The set of feasible points is defined as $\mathbb{S} = \{\boldsymbol{x} | \forall i, g^{(i)}(\boldsymbol{x}) = 0 \text{ and } \forall j, h^{(j)}(\boldsymbol{x}) \le 0\}$, where $g^{(i)}$ are equality constraints and $h^{(j)}$ are inequality constraints. 
  - Each constraint gets a KKT multiplier $\lambda_i$ or $\alpha_j$, giving the generalized Lagrangian $L(\boldsymbol{x, \lambda, \alpha}) = f(\boldsymbol{x}) + \sum_i \lambda_i g^{(i)}(\boldsymbol{x}) + \sum_j \alpha_j h^{(j)}(\boldsymbol{x})$.
  - As long as at least one feasible point exists and $f(\boldsymbol{x})$ can't have value $\infty$, then $\text{min}_x \text{max}_\lambda \text{max}_{\alpha, \alpha \ge 0} L(\boldsymbol{x, \lambda, \alpha})$ has the same set of optimal points as $\text{min}_{\boldsymbol{x} \in \mathbb{S}} f(\boldsymbol{x})$.

### Video - Ian Goodfellow [Numerical Computation for Deep Learning](https://www.youtube.com/watch?v=XlYD8jn1ayE&feature=emb_title)

- Real numbers cannot be implemented in a finite computer (e.g. $\pi$).
- Gradient descent is an iterative algorithm used in much of deep learning. In 2-d, the gradient is the derivative, and gradient descent moves left when the derivative is positive and right when it is negative. In other words, the algorithm moves downhill.
  - In deep learning, finding a global minimum is often infeasible, and often don't even reach a local minimum due to numerical computation issues. Instead of stopping only when the gradient is 0, we stop when $f(x)$ is very small.
  - Often run from multiple random starting points to see if some give lower values.
- Saddle points can be an issue for iterative optimization algorithms. At these points, the gradient is zero, but they are a maximum one dimension. These points attract Newton's method.
- Curvature indicated by Hessian matrix, which along with a direction vector can give the second derivative in that direction.
- Taylor series expansion used to predict optimal gradient size: $\epsilon^* = \frac{\boldsymbol{g^Tg}}{\boldsymbol{g^T Hg}}$, where $\boldsymbol{g}$ is the gradient and $\boldsymbol{H}$ is the Hessian.
  - Derived from the Taylor series expansion of the next iterative point: $f(x^{(0)} - \epsilon\boldsymbol{g}) \approx f(x^{(0)}) - \epsilon\boldsymbol{g^Tg} + \frac{1}{2}\epsilon^2\boldsymbol{g^T Hg}$.
  - When we have positive curvature, numerator tells us that bigger gradients mean we can take bigger steps - speeds up algorithm.
  - When we have positive curvature, denominator tells us that big eigenvalues reduce step size if gradient aligns with the Hessian's eigenvectors - slows down algorithm. Otherwise you may jump past the minimum and to an uphill point.
- The condition number is the maximum ratio between any two eigenvalues of the Hessian, A large condition number requires that you keep the learning rate small.
- Be careful with logs, exponents, square roots, and division.
  - Log(sum(exp($x$))) is subject to under/overflow. To safely compute, can find the max value in array and subtract it from the array, then calculate max + log(sum(exp($x$ - max))).
- Softmax, sigmoid, and cross-entropy functions are very common and generally implemented safely in libraries.

