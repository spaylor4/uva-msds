# Linear Algebra

Deep Learning Book [Ch. 2](https://www.deeplearningbook.org/contents/linear_algebra.html)

- A **scalar** is a single number, usually named with a lowercase letter written in italics, e.g. $s$.
- A **vector** is an array of numbers, usually named with lowercase letters written in bold, e.g. $\boldsymbol{v}$.
- A **matrix** is a 2-d array of numbers, usually named with uppercase letters written in bold, e.g. $\boldsymbol{M}$.
- A **tensor** is an array with more than two dimensions/axes, usually named with uppercase letters written in bold, not italic font, e.g. **A**.
- The **transpose** of a matrix is its mirror image, with rows and columns switched. The transpose of a matrix $\boldsymbol{A}$ is written $\boldsymbol{A}^T$.
- Matrices can be added if they have the same shape by adding each corresponding element.
- Matrices can be multiplied by scalars or have scalars added to them by applying the operation to each element.
- In deep learning, vectors can be added to matrices, $\boldsymbol{C} = \boldsymbol{A} + \boldsymbol{b}$ by implicitly copying (or *broadcasting*) $\boldsymbol{b}$ to be added to each row of $\boldsymbol{A}$.
- Two matrices $\boldsymbol{A}$ and $\boldsymbol{B}$ can be multiplied if the number of columns in $\boldsymbol{A}$ is the same as the number of rows in $\boldsymbol{B}$. The resulting elements are found by $C_{i, j} = \sum_k A_{i, k}B_{k, j}$.
  - Matrix multiplication is distributive ($\boldsymbol{A(B + C)} = \boldsymbol{AB + AC}$) and associative($\boldsymbol{A(BC)} = \boldsymbol{(AB)C}$) , but not commutative ($\boldsymbol{AB} \not= \boldsymbol{BA}$ necessarily) .
  - The transpose of a matrix product is $(\boldsymbol{AB})^T = \boldsymbol{B}^T \boldsymbol{A}^T$.
- A system of linear equations can be written in matrix notation as $\boldsymbol{Ax = b}$.
- The inverse of a matrix is the matrix such that $\boldsymbol{A^{-1}A = I}$, where $\boldsymbol{I}$ is the identity matrix.
  - The solution to a system of linear equations is $\boldsymbol{x = A^{-1}b}$, if $\boldsymbol{A}$ is invertible.
- The **span** of a set of vectors is the set of all points obtainable by linear combination of the original vectors.
  - If $\boldsymbol{b}$ is in the span of the columns of $\boldsymbol{A}$, then $\boldsymbol{Ax = b}$ has a solution.
  - The span of the columns of $\boldsymbol{A}$ is called the **column space** or **range** of $\boldsymbol{A}$.
- A set of vectors is **linearly independent** if no vector is a linear combination of the other vectors.
  - In order for the column space of a matrix to encompass $\R^m$, it must contain at least one set of $m$ linearly independent columns.
  - A square matrix with linearly dependent columns is **singular**.
- **Norms** are functions that measure the size of a vector. The $L^p$ norm is defined as $||\boldsymbol{x}||_p = (\sum_i |x_i|^p)^{1/p}$.
  - Norms must satisfy three properties: $f(\boldsymbol{x}) = 0 \rightarrow \boldsymbol{x} = 0$; $f(\boldsymbol{x + y}) \le f(\boldsymbol{x}) + f(\boldsymbol{y})$ (the triangle inequality); $\forall \alpha \in \R, f(\alpha \boldsymbol{x}) = |\alpha|f(\boldsymbol{x})$.
  - The $L^2$ norm is Euclidean distance. The squared $L^2$ norm is equal to $\boldsymbol{x^T x}$ and is often used due to its computational convenience.
  - The $L^2$ norm increases very slowly near the origin, so the $L^1$ norm ($||\boldsymbol{x}||_1 = \sum_i |x_i|$) is preferred when trying to discriminate between elements that are zero and those that are small but nonzero.
  - The $L^\infty$ norm or **max norm** is defined as $||\boldsymbol{x}||_\infty = \text{max}_i |x_i|$. This is equivalent to the absolute value of the element with the largest magnitude in the vector.
  - The dot product of two vectors can be written in terms of norms as $\boldsymbol{x}^T\boldsymbol{y} = ||\boldsymbol{x}||_2 ||\boldsymbol{y}||_2 \text{cos}\theta$, where $\theta$ is the angle between the two vectors.
- A **symmetric** matrix is one that is equal to its transpose, $\boldsymbol{A} = \boldsymbol{A}^T$.
- A **unit vector** has a norm of 1.
- Two vectors are **orthogonal** if $\boldsymbol{x^T y} = 0$. **Orthonormal** vectors are orthogonal and have unit norm. An **orthogonal matrix** is a square matrix with both rows and columns being mutually orthonormal.
  - For an orthogonal matrix, $\boldsymbol{A}^{-1} = \boldsymbol{A}^T$.
- An **eigenvector** of a square matrix $\boldsymbol{A}$ is a nonzero vector $\boldsymbol{v}$ such that multiplication by $\boldsymbol{A}$ alters only the scale of $\boldsymbol{v}$: $\boldsymbol{Av} = \lambda \boldsymbol{v}$.
  - $\lambda$ is a scalar known as the **eigenvalue** corresponding to that eigenvector.
  - Any scalar multiple of $\boldsymbol{v}$ is also an eigenvector of $\boldsymbol{A}$ with the same eigenvalue, so we usually only look for unit eigenvectors.
- The **eigendecomposition** of $\boldsymbol{A}$ is given by $\boldsymbol{A = V}\text{diag}(\boldsymbol{\lambda})\boldsymbol{V}^{-1}$, where $\boldsymbol{V}$ is the matrix with one linearly independent eigenvector per column and $\boldsymbol{\lambda}$ is a vector with the corresponding eigenvalues.
  - A matrix is singular iff any of the eigenvalues are zero.
  - A matrix whose eigenvalues are all positive is called **positive definite**, one whose values are all greater than or equal to zero is **positive semidefinite**, one whose values are all less than zero is **negative definite**, and one whose values are all less than or equal to zero is **negative semidefinite**.
- The **singular value decomposition** is an alternative way of factorizing matrices that works for all matrices, unlike eigendecomposition, which only works for square matrices. SVD breaks a matrix down into the product of three matrices, $\boldsymbol{A = UDV}^T$. 
  - If $\boldsymbol{A}$ is a $m \text{x} n$ matrix, then $\boldsymbol{U}$ is $m \text{x} m$, $\boldsymbol{D}$ is $m \text{x} n$, and $\boldsymbol{V}$ is $n\text{x} n$.
  - $\boldsymbol{U}$ and $\boldsymbol{V}$ are orthogonal matrices with columns of **left-singular vectors** and **right-singular vectors**, respectively.
    - Left-singular vectors are the eigenvectors of $\boldsymbol{AA}^T$, and right-singular vectors are the eigenvectors of $\boldsymbol{A^TA}$.
  - $\boldsymbol{D}$ is a diagonal matrix (not necessarily square) with diagonal elements that are the **singular values** of $\boldsymbol{A}$.
    - The singular values are the square roots of the eigenvalues of $\boldsymbol{A^TA}$.
- The singular value decomposition can be used to compute the pseudo inverse of a non-square matrix, using $\boldsymbol{A}^+ = \boldsymbol{VD^+U}^T$, where $\boldsymbol{D}^+$ is generated by taking the reciprocal of the nonzero elements of $\boldsymbol{D}$ and then taking the transpose of the result.
- The **trace** operator gives the sum of all diagonal elements of a matrix and is denoted Tr($\boldsymbol{A}$).
  - The trace of a matrix is equal to the trace of its transpose.
  - Traces are invariant to cyclic permutations (moving the last matrix in a product to the beginning of the product) if the matrix product is defined after the permutation.
  - A scalar is its own trace, $a = \text{Tr}(a)$.
- The **determinant** of a square matrix det($\boldsymbol{A}$) is equal to the product of all eigenvalues of the matrix.
  - If the determinant is 0, multiplying by the matrix contracts space completely along at least one dimension. If the determinant is 1, multiplying by the matrix preserves volume.

### Video - [The Applications of Matrices](https://www.youtube.com/watch?v=rowWM-MijXU&feature=emb_title)

- Multiplying a vector by a matrix *scales* and/or *rotates* the vector.
  - Different input vectors will be scaled/rotated differently, but the transformations are linear, so any input in the same direction as another input will be output in the same direction.
  - Any vector that is only scaled (not rotated) by a matrix is an eigenvector of that matrix. The scale factor (change in length) is the eigenvalue.
- The eigenvector is the equilibrium point (zombie example) of a Markov matrix in the long run.
- In image processing, *kernels* are matrices multiplied with images (in a moving window) to blur, sharpen, find edges, or perform other processing tasks.
- Squaring an adjacency matrix gives the number of paths of length two between any two nodes. Likewise cubing the matrix gives the number of paths of length three between any two nodes.
- Hill cypher uses matrices to encrypt/decrypt information.

### Class Notes

*Feb 3, 2021*

- Rotations (with no scaling) involve orthogonal matrices with determinant 1.
- A real symmetric matrix is Hermitian, so all of its eigenvalues are real.
- The determinant of a matrix is equal to the product of its eigenvalues.
- The condition number is the largest eigenvalue divided by the smallest eigenvalue. Large condition number leads to instability, as small changes in input will lead to large changes in ourput when multiplied by the matrix.
- A matrix of eigenvectors is orthonormal.
  - When an orthonormal matrix is multiplies by its transpose, the result is the identity matrix.
- Some classmates recommended 3Blue1Brown for review, especially the [eigenvectors and eigenvalues video](https://www.youtube.com/watch?v=PFDu9oVAE-g).