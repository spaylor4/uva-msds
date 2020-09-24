# Module 4: Trees & Tree Traversal

Readings: *Modern Software Development Using Java*, ch. 6, 7.1-7.3

### Trees

- **Recursive data structures** are those that contain references to instances of their same type.
- **Linked lists** are recursive data structures that consist of a string of nodes, each containing data and a reference to the next node (singly linked list).
  - Doubly linked lists have the same structure, but also a reference to the previous node.
  - Linked lists have a distinguished node called the head.
- **Trees** are composite, hierarchical, graph-like data structures.
  - Trees grow down, so predecessors are "up" the tree and successors are "down."
  - Trees are composed of nodes that hold data. Each node has a single parent (predecessor) and zero or more children (successors).
    - **Leaf** nodes have no children.
    - **Root** nodes have no parent. The **height** of a tree is the longest path from root to leaf.
    - **Internal** nodes are nodes with children (non-terminal nodes).
    - The **degree** tells how many children a node has.
    - **Edges** link parent and children nodes.
  - Trees are recursive data types that exhibit principles of abstraction and delegation. Recursion: each node is the root of a subtree.
  - Examples include file systems, taxonomy (kingdom, phylum, species), and parse trees (e.g. language processing).
  - A **binary tree** is one in which each node has at most two children.
- Recursive data structures often defined using a two-class system: one "top" class for the general structure (e.g. tree) and one for the nodes.

### Tree Traversal

- A **tree traversal** is a specific way to visit every node in a tree once.
- Three common methods for binary tree traversal: pre-order, in-order, and post-order.
  - All three traverse the left and right subtrees recursively and visit the root node of that subtree. "Pre," "in," and "post" describe when the node is visited and processed.
  - **Pre-order**: visit root, traverse left subtree, traverse right subtree.
  - **In-order**: traverse left subtree, visit root, traverse right subtree.
  - **Post-order**: traverse left subtree, traverse right subtree, visit root.
  - Pre-order traversal is also simple depth-first search.
- Applications of tree traversal: processing tree elements, making a clone (deep copy) of a tree, determining tree height and size (number of nodes), searching.
- Tree traversals can be breadth-first or depth-first.
  - **Depth-first search** goes deeply into the tree and backtracks when it reaches the leaves.
    - Often used when simulating games, e.g. chess. Enormous number of applications.
  - **Breadth-first search** visits all nodes on the same level before going to the next level.
    - Harder to do recursively.
    - Can be used to find shortest path between nodes (Dijkstra's algorithm).
    - Similar to A* search.

### Graph Representation

- Adjacency matrix: entries of 1 for edges between nodes $i, j$ and 0 for unconnected nodes.
  - Can be generalized to weighted cases where edges not equal to 1.
  - If number of edges $m \in O(n^2)$, it is a dense graph. If $m \in O(n)$, it is a sparse graph.
- Graphs can also be represented as a vertex-indexed array or a list of edges (pairs).