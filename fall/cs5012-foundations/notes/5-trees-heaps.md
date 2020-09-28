# Module 5: Trees

Readings:

### Binary Search Trees

- Want to be able to find items quickly, handle inserts and deletes.
- Binary search trees store items in ordered fashion, with comparable keys: every node in the left branch is less than the root, and every node in the right branch is greater than the root.
  - In-order traversal visits nodes in sorted order.
- A balanced binary tree guarantees height of child subtrees differ by no more than 1.
  - Produces O(log n) runtimes, compared to O(n) for unbalanced binary trees.
- Binary search tree Find operation compares target value with root and traverses left if less than root and right otherwise, stopping when item found or at a leaf.
  - Similar to binary search.
  - Complexity O(log n), worst case height of tree.
- BST Insert operation performs a find operation for the value to insert, then add it to the left or right as appropriate.
- BST Delete operation more complicated, since a replacement node needs to be chosen.
  - If 0 children, delete node.
  - If 1 child, replace node with its child.
  - If 2 children, find next largest or smallest to fill in. Next largest is minimum (leftmost node) of right subtree, and next smallest is maximum (rightmost node) of left subtree.

### Binary Heaps

- A priority queue is an abstract data type, like a regular data structure but where each element has an associated priority.
  - High-priority elements served before low-priority ones.
  - Elements with the same priority are served according to their order in the queue.
  - Queues generally have a FIFO structure (first in first out), but sometimes this needs to be violated with a priority queue. For example, scheduling shorter jobs to be processed ahead of longer ones in a pre-emptive shortest job first scheduling technique improves average response time.
  - Operations: Construct a priority queue, Insert new elements, Remove largest or smallest element, Peek/return an element.
  - Elements have value and priority key (non-unique). Elements are entered in sequence but removed according to priority.
- An abstract data type (ADT) is a model for data structures with similar behavior.
  - Defined indirectly by operations that may be performed on it and mathematical constraints on those operations.
  - Purely theoretical entities used to simplify description of abstract algorithms and classify/evaluate data structures.
  - Often implemented by modules to simplify the implementation for the user.
- Priority queues can be implemented using arrays or heaps, but heap data structure is the preferred implementation option for priority queues.
  - Array implementation can be sorted or unsorted. Elements inserted at end for unsorted, and in order for sorted.
    - Unsorted priority queue insertion is fast (O(1)) but deletion is slow (O(n)), and the reverse is true for sorted lists.
- Binary heaps are balanced binary trees with two additional constraints: a shape property and an order (heap) property.
  - Shape: binary tree of height $i$, with all leaf nodes on level $i$ or $i-1$, and all leaves on level $i$ are as far to the left as possible. In other words, all leaves must be on the lowest two levels and are added on the lowest level from left to right.
  - Order: node value always less than or equal to values stored in its descendants (minheap). A maxheap has nodes greater than or equal to values in its descendants.
  - Unlike binary search trees, it doesn't matter which side children appear on.
- Two most important methods for heaps are inserting new values (maintaining the order & shape) and retrieving the smallest value (root), rebuilding the heap afterward.
  - Insert: add element to bottom level, compare with parent, swap if necessary to maintain correct order, repeating until new element in correct place. Complexity O(log n).
  - Delete: remove the root node and replace it with the last element on the last level, then swap the new root with its children until order is restored. Complexity O(log n).
    - Swap with smaller child in minheap and larger in maxheap (so that correct element winds up as new root).
  - Building an entirely new queue takes O(n log n) time, significantly faster than implementing via arrays.