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

- 