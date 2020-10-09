# Clustering

Readings: ISL 10.3, 10.5; ESL 14.3.1-14.3.8, 14.3.12; ESL 8.5.1; ITDM 7.1-7.3, 7.5; Gaussian Mixture Models 11.1-11.3

- Clustering seeks to separate data into distinct groups such that observations within groups are very similar to each other but very different from observations in other groups.
- Clustering is unsupervised, as it tries to discover structure in data (can be thought of as unsupervised classification).
  - Ex: market segmentation to find customers likely to purchase products.
- Need to decide whether or not to standardize/scale variables, as this will significantly alter results.
- Will always find clusters in clustering, regardless of whether there are any real clusters present in the data.
- Exclusive clustering assigns each observation to a single cluster, while overlapping (non-exclusive) clustering can be used to represent observations that may simultaneously belong to multiple groups. In fuzzy (probabilistic) clustering, every observation belongs to every cluster with a membership weight between 0 and 1.
- Complete clustering assigns every observation to a cluster, while partial clustering does not.

### $K$-Means Clustering

- Partitions data into a specified number of clusters $K$. Each data point is assigned to one (and only one) cluster.
- $K$-means clustering seeks to minimize the within-cluster variation $W(C_k)$ for all clusters $C_k$, in other words minimize $\sum_{k=1}^K W(C_k)$.
  - Most common choice for within-cluster variation is the sum of squared Euclidean distance between all points in a given cluster divided by the number of observations in that cluster.
- There are $K^n$ ways to partition $n$ points into $K$ clusters, so an algorithm is used to find local optimum or "pretty good" solutions:
  - Randomly assign a number to each observation to serve as the initial cluster.
  - Compute the centroid of each cluster. Assign each observation to the cluster with the closest centroid. Repeat until the cluster assignments stop changing.
  - Since this algorithm finds local rather than global optimum, it needs to be run multiple times with different random starting points and then choose the best clustering.

### Hierarchical Clustering

- Hierarchical clustering doesn't require choosing a number of clusters beforehand. It organizes observations into a tree shape, visualized as a dendrogram.
- The bottom of a dendrogram contains individual observations/leaves, and as you move up the tree, leaves gradually fuse into branches consisting of similar observations.
  - The lower in the tree fusions occur, the more similar the observations are.
  - The horizontal axis of dendrograms cannot be used to draw conclusions about similarity, only the vertical axis.
  - Clusters identified by slicing a dendrogram at a particular height. Any number of clusters can be assigned from the same dendrogram by choosing different heights.
- Hierarchical clustering can yield worse results than $K$-means clustering when there are different, non-hierarchical groupings present in data (for example two genders and three nationalities).
- The hierarchical clustering algorithm uses a measure of dissimilarity and fuses the two most similar clusters so that each level up has one fewer cluster, continuing until all observations belong to a single cluster.
  - The dissimilarity between the two fused clusters indicates the height in the dendrogram at which the fusion is placed.
  - The measure of dissimilarity for individual observations is usually Euclidean distance (correlation-based distance is another choice).
    - Customer purchase behavior is an example where correlation-based may be appropriate, as the most similar in Euclidean distance may be people who make few purchases, rather than people who purchase similar things.
  - The measure of dissimilarity for clusters is called linkage, for which there are four main types:
    - Complete: largest dissimilarity between all individual observations in one cluster and all observations in another cluster. "Farthest neighbor"
    - Single: smallest dissimilarity between all individual observations in one cluster and all observations in another cluster. "Nearest neighbor"
    - Average: mean pairwise dissimilarity between all observations in two clusters.
    - Centroid: dissimilarity between centroids of two clusters. Can result in undesirable inversions, when clusters are fused at height lower than either cluster.

## Class Notes

*October 8, 2020*

- Clustering can be used for summarizing or reducing the size/complexity of data.
- Two views of clustering: finding homogeneous subgroups (partition such that objects in same group are similar to each other and dissimilar to other groups) and statistical clustering (partition such that objects in same group are from same distribution).
- Clustering is very subjective analysis.
- Agglomerative (greedy) hierarchical clustering initially treats every observation as its own cluster, then sequentially merges closest two clusters.
- Ward's linkage is a cluster dissimilarity measure of the increase in sum of squared Euclidean distance if the clusters were merged. Similar to centroid linkage, but accounts for number of observations in each cluster.
  - Almost always better than centroid linkage due to this scaling factor.
- When implementing hierarchical clustering in R, need to supply a distance matrix.
  - Should always think about scaling when distances are used.
  - Packages such as `ggdendro` can be used for plotting dendrograms.
- How to choose number of clusters (hierarchical clustering)? Very subjective, but a few approaches:
  - Look for gaps in height between cluster merges.
  - Elbow method: consider points where slope of height vs. number of clusters changes.
- Choice of dissimilarity/distance measure and linkage type, deciding to scale/not, deciding whether to use all features or transformations such as PCA all will change the output and can have a substantial impact on resulting analysis.
- Clustering results should be viewed with skepticism, as they can change significantly with some observations held out.
- If you have labels to do classification, that's more useful than clustering (use all the info you have).
- Gaussian mixture models are (nearly) always better than $K$-means clustering, but $K$-means is very common and provides a good intro.