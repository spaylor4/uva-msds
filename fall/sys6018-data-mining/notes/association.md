# Association Analysis

Readings: MMDS 6.1-6.2; ITDM 5.1-5.3, 5.7-5.8; ESL 14.2; [Instacart Case](https://mdporter.github.io/SYS6018/other/instacart.html)

### Market-Basket Model

- In addition to traditional market-baset analysis, this technique can be used to find related concepts in documents, identify plagiarism, and compare biomarkers to locate possible diseases.
- Data consists of items and baskets, with each basket consisting of an itemset, usually a small subset of the total number of items.
- The *support* for a set of items $I$ is the number of baskets for which $I$ is a subset. We say $I$ is frequent if its support is greater than a given support threshold $s$.
  - A doubleton (set of two items) can only be frequent if both of its items are frequent by themselves. Similarly, to be a frequent triple, each pair of elements must be a frequent doubleton.
  - Support is fraction of total baskets containing both $I$ and $j$.
- Association rules are used to find an item $j$ that commonly appears in a basket when a set of items $I$ is in the basket. The *confidence* of an association rule $I \rightarrow j$ is defined as the fraction of baskets containing all $I$ items that also contain $j$.
  - Generally want to set threshold so there are a small number of high-support, high-confidence association rules in order to make the rules feasibly actionable.
  - Confidence is an estimate of the conditional probability of $j$ given $I$.
- The interest of an association rule is the difference between its confidence and the fraction of baskets that contain $j$.
  - Interest = 0 occurs when the fraction of baskets including both $I$ and $j$ is the same as the fraction of all baskets containing $j$.
  - Positive or negative interest can be useful (presence of $I$ encourages or discourages the presence of $j$).
- Market basket data can be represented in binary format with columns for each item and 0 or 1 for absence or presence of that item in each basket.
- Computing support and confidence for every possible association rule is prohibitively computationally expensive. Association rule algorithms generally first find itemsets meeting the support threshold, then find which of those also has high confidence.
- The Apriori principle states that if an itemset is frequent, all of its subsets must also be frequent. 
  - The reverse is also true: an infrequent itemset has all subsets also infrequent.
  - This is used to prune candidate itemsets to reduce computation (support-based pruning).
  - The Apriori algorithm first considers all 1-itemsets, then 2-itemsets only containing frequent 1-itemsets, and so on.
- The Apriori algorithm's computational complexity can be affected by several factors
  - Lowering the support threshold increases computational complexity, since more itemsets will be declared frequent, so more candidate sets will need to be evaluated at each level.
  - As the dimensionality (number of items) increases, more storage will be needed for the support counts.
  - More transactions will lead to longer runtimes.
  - Wider average transactions lead to longer runtimes.
- The interest factor (or lift) measures the support of a pair of items against the support if these items were independent, using $\frac{s(A, B)}{s(A) \times s(B)}$.
  - If $A$ and $B$ are independent, the interest factor is 1. If they are positively related, the interest factor will be > 1. If they are negatively related, it will be < 1.
  - Can reveal some meaningful relationships that confidence does not.
- The Piatesky-Shapiro (PS) measure is similar to the interest factor, but calculates $s(A, B) - s(A) \times s(B)$.
- Correlation of binary variables is defined as  $\phi = \frac{s(A, B) - s(A)s(B)}{\sqrt{s(A)(1-s(A))s(B)(1-s(B))}}$.
  - Essentially a normalized PS measure (value ranges from -1 to 1).
- The IS measure, $\sqrt{I(A, B)s(A, B)} = \frac{s(A, B)}{\sqrt{s(A)s(B)}}$, is the geometric mean between the interest factor and the support of a pattern.
  - IS is large when both the interest factor and support are large. If interest of two patterns is equal, IS will be larger for the one with higher support.
  - IS of 0 corresponds to no co-occurence of $A$ and $B$, and IS of 1 corresponds to perfect co-occurence.
- The interest factor, PS, correlation, and IS will not always rank relationships in the same order.
- The odds ratio is invariant to scaling of rows and columns (often done in medical analysis to account for differences in the population sample chosen for a study). Other metrics (interest factor, IS, etc.) are not invariant to scaling.
- The IS measure has the null addition property, meaning that it is unaffected by adding transactions that do not contain either itemset in a relationship.
  - Interest factor, PS, and odds ratio do not have this property.
- Confidence is asymmetric ($C(A \rightarrow B)$ and $C(B \rightarrow A)$ can differ).
- Simpson's Paradox occurs when hidden variables cause the relationship between a pair of variables to disappear or reverse direction.
  - To avoid this, data should be stratified by potentially confounding variables (e.g. store location or age/gender).

### Unsupervised as Supervised Learning

- One alternative method of density estimation involves transforming the problem into a classification problem.
- For unknown pdf $g(x)$, choose reference density function $g_0(x)$ and sample from it using Monte Carlo methods.
  - Often choose a uniform distribution for $g_0(x)$, but can choose others depending on the problem. Want $g_0(x)$ to be a distribution from which a deviation would be interesting.
- Assign $Y=1$ to points from $g(x)$ and $Y=0$ to those from $g_0(x)$. Then can estimate $\hat{g}(x) = g_0(x)\frac{\hat\mu(x)}{1 - \hat\mu(x)}$, where $\mu(x) = E(Y | x)$ estimated via supervised learning.

## Class Notes

*November 3, 2020*

- Association analysis seeks to find relationships of interest between items. Co-occurences of items may not be meaningful unless they co-occur more or less than expected.
  - Co-occurence =/= causality.
- Application to health data: baskets = patients, items = drugs and side effects.
- Data can be represented as a transaction list or a binary incident table/matrix.
  - R `arules` package uses matrix form behind the scenes.
- For association rules $I \rightarrow J$, $I$ and $J$ should be disjoint itemsets.
- Confidence is an estimate of the conditional probability of $J$ given $I$.
- Support and confidence are based on an expected uniform distribution. Lift, on the other hand, is based on statistical independence.
  - Lift can be large even when support is low, or can be small even when confidence is large.

*November 5, 2020*

- R `arules` package uses "transaction" data type.
- The `apriori` function will be the most-used for association analysis.
  - Output is not the best to work with; Professor Porter has written a function to convert the output to a data frame.
- `arulesViz` package helps visualize results in a network.
  - Red nodes represent rules; green represent items.
- If future transactions come from a different distribution than the observed data, you need to be careful.
  - Sometimes may want to weight more recent transactions more heavily.
- If transactions are not independent (e.g. repeat customers), confidence intervals may be too narrow.