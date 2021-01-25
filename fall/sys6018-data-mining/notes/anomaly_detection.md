# Anomaly Detection

Readings: [Hypothesis Testing](https://mdporter.github.io/SYS6018/other/HypTesting.pdf), [The Law of Anomalous Numbers](https://mdporter.github.io/SYS6018/other/(Benford)%20The%20Law%20of%20Anomalous%20Numbers.pdf), Benford's Law [Wikipedia](https://en.wikipedia.org/wiki/Benford%27s_law), [Mahalanobis Distance](https://stats.stackexchange.com/questions/62092/bottom-to-top-explanation-of-the-mahalanobis-distance), [Detecting Spatial Clusters](https://mdporter.github.io/SYS6018/other/Neill-Moore_biosurv.pdf)

### Hypothesis Testing

- A $P$-value is the probability that chance alone would produce a test statistic as extreme as the observed test statistic if the null hypothesis were true. A result is statistically significant if it would rarely occur by chance (small $P$-value).
- Permutation tests can be used to test the differences between groups. To do so, pool values from all groups, create permutation resamples of sizes equal to the original group sizes, and calculate the statistic of interest (e.g. difference of means). The $P$-value is the fraction of times the random statistic is greater than or equal to the original statistic (multiply by 2 for a 2-sided statistic).
  - Works even for unbalanced and very skewed data.
  - No assumption that samples are drawn from a normal distribution.
  - Can be used to compare robust statistics (median, trimmed mean, etc.) as well as proportions or variances.
- If data do not come from independent populations (e.g. divers' scores in semifinal vs. final rounds), use a matched pairs test rather than permutation test.

### Benford's Law

- In many real-life data sets, the leading digit is more likely to be large than small (also called law of anomalous numbers).
  - Generally most accurate when values are distributed across multiple orders of magnitude.
  - Law states that leading digit is $d \in \{1, ..., 9\}$ with probability $P(d) = log_{10}(1 + 1/d) = log_{10}(\frac{d + 1}{d})$.
- Law holds when logarithms of values are uniformly and randomly distributed (lognormally distributed).
- Stock prices closely follow Benford's law due to the fact that the price changes by a multiplicative factor each day and the logarithm of stock price undergoes a random walk.
- Kolmogorov-Smirnov and Kuiper hypothesis tests can be used to test compliance with Benford's law.
- Fibonnaci numbers, factorials, and powers of 2 follow Benford's law exactly. Generally, distributions that are expected to follow Benford's law:
  - When the mean is greater than the median and the skew is positive.
  - Number that result from mathematical combinations of numbers (e.g. quantity times price).
  - Transaction level data (e.g. sales).
- Distributions that do not span several orders of magnitude (such as height and weight) will not follow Benford's law. Generally, distributions that are not expected to follow Benford's law:
  - Where numbers are assigned sequentially (e.g check numbers).
  - Where numbers are influenced by human thought (e.g. prices, since prices ending in .99 are very common).
  - Accounts with a built-in minimum or maximum.
- The probability of encountering a number starting with a string of digits *n* is $log_{10}(1 + 1/n)$.

### Mahalanobis Distance

- Mahalanobis distance measures the distance in the scaled principle directions of data.
  - The origin is the centroid of the data, and the axes are the (perpendicular) principle directions (starting with the direction in which variance is greatest).
  - The axes are scaled so that one unit is one standard deviation along that direction.
- Calculated using $D(x, y) = \sqrt{(x - y)'C^{-1}(x - y)}$, where $C$ is the covariance function, gives the distance between two vectors $x$ and $y$.