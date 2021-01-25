# Networks

Readings: Network Science [Book](http://networksciencebook.com/chapter/2) Ch. 2; MMDS 5.1-5.3, 5.5

### Graph Theory

- Network graphs consist of nodes (or vertices) and edges (or links). The number of nodes $N$ is called the *size* of the network, and the number of links $L$ represents the number of interactions between nodes.
- Links can be directed (e.g. phone calls) or undirected (e.g. power lines).
  - A network is called directed if all its links are directed and called undirected if all its links are undirected.
- The *degree* of a node is the number of links it has to other nodes, denoted $k_i$ for node $i$.
  - In an undirected network, the total number of links is equal to the sum of each node's degree divided by two (since each link will be counted once in each node's degree).
  - In directed networks, degree is distinguished between incoming degree $k_i^{in}$ and outgoing degree $k_i^{out}$. Total degree is $k_i = k_i^{in} + k_i^{out}$. The sum of $k_i^{out}$ over all nodes is equal to the sum of $k_i^{in}$ over all nodes and to the total number of links $L$.
  - The degree distribution $p_k$ is the proportion of nodes having degree $k$.
- An adjacency matrix represents a network with $N$ nodes in a $N$ by $N$ matrix where $A_{ij}$ = 1 if there is a link from node $j$ to node $i$ and is 0 otherwise.
  - An undirected network has a symmetric adjacency matrix.
  - In a directed network, the row sums equal the incoming degrees and the column sums equal the outgoing degrees.
  - For weighted networks, the weights of the links can be stored in the matrix in place of 1s.
- Many real networks are sparse, with very large numbers of nodes connected to relatively few other nodes.
  - In a complete graph, every node is connected to every other node.
- Metcalfe's Law: the value of a network grows quadratically ($N^2$), while the cost only grows linearly ($N$).
  - Idea that the more individuals use a network, the more valuable it becomes (e.g. when more of your friends have email, it becomes more useful to you).
  - Not true for sparse networks, for which value grows close to linearly.
  - Not all links have equal weights.
  - Used to justify internet boom stock valuations with the idea of "critical mass."
- Bipartite graphs have two different types of nodes ($U$ and $V$), in which edges connect nodes of different types (e.g. shoppers & items, movies & actors, etc).
  - Two projections can be generated from each bipartite graph, one with all $U$-nodes linked if they link to the same $V$-node and vice versa.
  - Can also define multipartite graphs with more than two types of nodes.
- Path length is the number of links in a path from one node to another.
  - The shortest path between two nodes is often called the distance between them.
  - The diameter is the longest shortest path in a graph.
  - A cycle is a path that starts and ends with the same node.
  - A Eulerian path traverses each link exactly once.
  - A Hamiltonian path visits each node exactly once.
  - The number of paths of length $d$ between each node can be found by entries in $A_{ij}^d$, the adjacency matrix to the power $d$.
  - Breadth-first search algorithm used to find distance between nodes in ($N+L$) time.
- A network is connected if each node is reachable from all other nodes via some path.
  - A bridge is a link that if cut, disconnects the network.
- Clustering coefficient is the degree to which neighbors of a given node link to each other.
  - Local clustering coefficient $C-i = \frac{2L_i}{k_i(k_i - 1)}$, where $L_i$ is the number of links between the $k_i$ neighbors of node $i$. $C_i$ is between 0 and 1.
  - The global clustering coefficient measure the number of closed triangles in a network.

### Page Rank

- The Web can be represented as a directed graph with pages as nodes and links between pages as edges.
- A random surfer moves from page to page randomly, with equal probability for each link on the current page. This can be represented by a transition matrix. The limiting distribution of this transition matrix gives the limiting probability of where a random surfer will be after a long time. The higher this probability, the more important the page is for PageRank.
  - In practice, 50-75 multiplications of the transition matrix will sufficiently converge. Due to the size of the matrix, MapReduce usually needed for computation (breaks matrix into vertical stripes).
  - Requires that the graph be strongly connected (any node reachable from any other node) and have no dead ends, which is not true in practice.
    - A spider trap is a set of nodes with no dead ends but no arcs out.
  - Transition matrix is very sparse, since there are billions of web pages, with an average of only ~10 links each. Often use edge list representation instead to save space.
- One method for dealing with dead ends involves removing all dead ends before computing the limiting probabilities, then calculating a PageRank for the dead end nodes based on their predecessors' PageRank (weighted by the number of descendants of the predecessor).
  - Probabilities will no longer sum to 1 but will give relative importance of pages.
- Another method that deals with both dead ends and spider traps involves "taxation," giving a small probability that the random surfer leaves the Web at each step.
- Topic-sensitive PageRank creates different ranking vectors for some small number of topics, then tries to classify users based on their degree of interest in each topic.
  - Topic-sensitive PageRank biases results toward a topic by starting new random surfers on pages within that topic.
- Hubs & authorities (or HITS: hyperlink-induced topic search) is an alternative to PageRank based on the idea that some webpages provide information (authorities) and others tell you where to go to find information (hubs). Good hubs link to good authorities and good authorities are linked to by good hubs.

## Class Notes

*November 10, 2020*

- Community detection for networks is clustering of nodes (or possibly edges).
  - Communities have more connections to others in the community than to nodes outside the community.
- Graphs are technically visual/mathematical representations of real-life networks, but the two terms used pretty interchangeably.
- Nodes and edges can have optional attributes. Can add attributes after creating a graph with `igraph` or `tidygraph`.
- `igraph::simplify` function will remove multiple edges and loops.
  - Need to be careful, since node attributes will be summed when doing so unless specified otherwise.
- Graph Laplacian matrix $L = D - A$, where $D$ is a diagonal matrix with the degree of each node along the diagonal and $A$ is the adjacency matrix.
- Ego-neighborhood of node $i$ is all nodes that $i$ is connected to.

*November 12, 2020*

- Homophily: when connected nodes are more similar to each other than nodes they are not connected to. If homophily is present, can make predictions about a node based on its neighbors.
- Laplace Smoothing: $p_0$ prior probability (of fraudster in class example), $\hat{p}_i = \sum y_i/d_i$ (MLE). New estimate is $\pi_i\hat{p}_i + (1 - \pi_i)p_0$ ($\pi$ specifies how much trust is placed in data; small $\pi$ if not much data). Set $\pi_i = \frac{d_i}{d_i + k}$, where $k$ is a chosen number of pseudo-nodes.
  - Smooths/shrinks estimate toward prior.
  - Can use resampling to choose $k$. Example in "node-predict.R" script.
- Link prediction: predict whether a link exists between two nodes based on their attributes.

- Degree of nodes is one measure of importance/centrality (most basic measure of centrality). Called degree centrality.
  - $c_i = \sum_j A_{ij}$ and $c = A * 1_{|V|}$, where $c$ is a vector of node centrality measures.
- Closeness centrality measures how close each node is to other nodes.
  - Only works for connected graphs.
- Betweenness centrality measures how many shortest paths pass through a given node.
- Eigenvalue centrality is related to the idea that important nodes are linked to other important nodes.
  - PageRank is very similar but with a few modifications. PageRank uses a dampening factor (small probability that random surfer exits and restarts at random page) to deal with friendless nodes, dead ends, and spider traps.