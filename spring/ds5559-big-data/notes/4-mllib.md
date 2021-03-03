# Module 4: Machine Learning Using MLib - Overview and Classification Tasks

Reading: *Learning PySpark* Ch. 4, *Learning Spark* Ch. 11

### Prepare Data for Modeling

- `df.dropDuplicates()` will remove rows with all fields equal.
  - `subset` parameter takes a list of columns to use for comparison if some columns don't matter for checking duplicates.
- `.alias()` method allows for renaming an aggregation column (equivalent to SQL `AS`).
- `df.dropna()` drops rows where all columns are null.
  - `thresh` parameter allows you to drop rows with more than a set threshold of null values.
  - `.fillna()` can fill missing values, either with a string/int/float, or a dictionary mapping column names to fill values.
- `.toPandas()` functions similarly to `.collect()` in that it pulls all data to the driver.
- `rdd.first()` returns the first row - useful for extracting header info.
- `df.describe(column_list)` will return the count, mean, standard deviation, min, and max for each column.
- Bokeh uses D3 in the background to create interactive charts.

### Machine Learning with MLlib

- MLlib contains parallel ML algorithms that run well on clusters.
- Can parallelize over a list of parameters, but most useful when training on a large, distributed dataset.
- MLlib contains some special data types:
  - `Vector` is a mathematical vector, and can be dense or sparse.
    - Sparse preferable if < 10% of elements are nonzero.
    - In Python, numpy arrays can be passed directly to MLlib as dense vectors.
    - To create a sparse vector, use `Vectors.sparse(length, {index: value, ...})` or `Vectors.sparse(length, [indices], [values])`.
  - `LabeledPoints` stores a vector of features with a label.
  - `Rating` is a rating of a product by a user.
  - `Model` classes are results of training algorithms.
  - Usually use `map` to create `Vector`, `LabeledPoints`, or `Rating` objects from RDDs.
- Feature extraction algorithms:
  - TF-IDF: `HashingTF` and `IDF` algorithms are in `mllib.feature`.
    - `HashingTF` computes the term frequency from a document, hashing to match words to an index in a vector. Recommended to set desired vector size $S$ (`numFeatures` param) to between $2^{18}$ and $2^{20}$. Can run on a single document or iterable list of documents.
    - `IDF` computes the inverse document frequency (which can be multiplied with the term frequencies to get TF-IDF).
  - `Normalizer().transform(rdd)` normalizes vectors to length 1 (using the $L^2$ norm by default).
  - `Word2Vec` can be used to transform words into vectors for use in other algorithms. Similar words are close in the vector space.
- Statistics methods included in `mllib.stat.Statistics`:
  - `Statistics.corr(rdd, method)` computes the correlation matrix between columns, where method is `spearman` or `pearson`.
    - Can also take two RDDs of floats.
  - `Statistics.chiSqTest(rdd)` returns p-value, test statistic, and degrees of freedom for each feature.
- Classification and regression:
  - Both use `LabeledPoint` data type.
  - Linear regression options include `LinearRegressionWithSGD`, `LassoWithSGD`, and `RidgeRegressionWithSGD`.
  - Models include a `.predict()` method to make a prediction for a new vector (single data point).
  - Logistic regression options are `LogisticRegressionWithSGD` and `LogisticRegressionWithLBFGS`. LBFGS is generally recommended.
    - Can change prediction threshold using `model.setThreshold(threshold)`. Default is 0.5.
  - Other models include `SVMWithSGD`, `mllib.classification.NaiveBayes`, `mllib.tree.DecisionTree`, and `RandomForest`.
  - For classification, MLlib requires classes of 0/1 for binary or 0 to $C-1$ for multiclass classification with $C$ classes.
- Collaborative filtering is used for recommender systems for products. Takes in user ratings and product interactions.
  - Implemented in `mllib.recommendation.ALS` (Alternating Least Squares). Determines a feature vector for each user/product so that the dot product of a user's vector and a product's vector is close to their score.
    - Input RDD of `mllib.recommendation.Rating` objects. Requires userID and productID as 32-bit integers (may need to hash or convert string and large numeric IDs).
    - Can use explicit ratings (e.g. 1 to 5 stars) or implicit (e.g. confidence rating based on number of page visits).
- Useful to cache input datasets for models, since most algorithms are iterative and will go over the data multiple times.
  - If too large to fit in memory, can do `persist(StorageLevel.DISK_ONLY)`.
  - Python caches RDDs automatically when passing to Java, so don't need to explicitly call persist.
- Generally want at least as many partitions in input RDDs for models as cores in cluster to achieve full parallelism.
  - Too many partitions will lead to high communication cost.
- Pipeline API is a higher-level API for ML that allows you to create a series of algorithms to transform data and fit models.
  - Can be used to automatically search for best parameters.

### Class Notes

*March 2, 2021*

- ML and MLlib are two different APIs: MLlib uses RDDs, ML uses DataFrames. MLlib no longer in active development, but still able to be used.
- `.union()` is like `rbind` function (appends two objects together).
- Scaling doesn't matter as much for tree models, but for most other models (anything with distance), it can be important.
  - Be careful to not scale label too.
  - Two steps: `scaler1 = StandardScaler().fit(features)` and `scaler1.transform(features)` (similar to IDF calculation).