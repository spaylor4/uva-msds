# Module 5: Regression and Clustering in MLlib

### MLlib Statistics

- `Statistics.colStats()` computes the mean, variance, count, min, max, number non-zero, etc. for an RDD of vectors.
  - `from Pyspark.mllib.stat import Statistics`
- `Statistics.corr()` calculates the Pearson (default) or Spearman correlation.
- `rdd.sampleByKey(False, fractions)` creates a stratified sample, where fractions is a dictionary containing the keys and fraction of the sample that should come from that key.

### Recommender System

Reading: [Prototyping a Recommender System](https://towardsdatascience.com/prototyping-a-recommender-system-step-by-step-part-2-alternating-least-square-als-matrix-4a76c58714a1)

- Item-based collaborative filteriing suffers from three main problems:
  - Popularity bias: can recommend items with most interactions with no personalization.
  - Item cold-start problem: when new items added they have very few interactions, and the recommender relies on these interactions.
  - Scalability: doesn't work as well with very large sets of users and items.
- Matrix of users and items (e.g. movies) is very sparse. Matrix factorization decomposes the user-item matrix into the product of two lower-dimensionality matrices (a user and item matrix).
  - User matrix: rows represent users, columns represent latent factors.
  - Item matrix: columns represent items, rows represent latent factors.
  - Latent factors intended to represent user preferences or item topics in a much lower-dimensional space.
  - Increasing the number of latent factors improves personalization to a point, after which overfitting occurs.
- Alternating Least Square (ALS) is a parallelizable matrix factorization algorithm.
  - Uses $L^2$ regularization.
  - Alternates between holding user matrix fixed and running gradient descent with item matrix, then holding item matrix fixed and running gradient descent with user matrix.
  - Runs gradient descent in parallel using multiple partitions of training data.
  - Hyperparameters include `maxIter` (maximum number of iterations, default 10), `rank` (number of latent factors, default 10), and `regParam` (regularization parameter, default 1.0).
  - Implemented in PySpark `from pyspark.ml.recommendation import ALS`.
    - Can implement using `als = ALS().setMaxIter(maxIter).setRank(rank).setRegParam(reg)` then `model=als.fit(train_data)`.

### Class Notes

*March 16, 2021*

- Linear regression has closed-form solution (normal equations), but this is slow for very large data, so use Spark uses SGD instead.
- Kmeans requires numeric features; if you have categorical they'll need to be converted.