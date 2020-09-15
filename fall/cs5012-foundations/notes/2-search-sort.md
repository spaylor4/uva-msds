# Module 2: Searching & Sorting

### Searching

- Search algorithms take a list of items and target item, then find if/where the target is in the list. For arrays, search algorithms usually return the index of the target if it is in the list, or a sentinel value (e.g. -1) if it is not.
- **Brute-force**/exhaustive algorithms involve systematically enumerating all possible candidates for the solution and checking each.
  - Simple to implement, but can be costly when size of the problem is large. Typically used when problem size is limited or when simplicity is more important than speed.
  - **Heuristics** can speed up brute-force search by reducing the size of the search space. A heuristic is like an educated guess, and it allows you to explore the most likely scenarios rather than all possible states of a problem.
- **Linear search** (examining all elements of a table or list sequentially) is a brute-force search method.
  - Order class O(n)
  - Advantages: simple to code and understand; makes no assumptions about the list.
- **Binary search** requires a sorted list and involves eliminating half of the items to search in one comparison ("divide and conquer" strategy).
  - Complexity O(lg n)
  - Very efficient, but depends on list being sorted. If searching will be done many times, it is worth the additional time to sort once before searching. Worst-case binary search time is equal to average linear search time.
- **Best-first search** uses an evaluation function (heuristic) to estimate the desirability of each node, then expand the most desirable unexpanded node.
- **Greedy search** is a special case of best-first search that makes the locally optimal choice at each stage in hopes of finding the global optimum. 
  - Does not generally produce an optimal solution, but may approximate the global optimal solution in a reasonable amount of time.
  - Complexity O(b$^m$) in terms of nodes and branches. Good heuristic dramatically improves speed.
- **A\* search** is another special case of best-first search noted for its performance and accuracy (generates more optimal solutions than greedy search).
  - Widely-used in path finding and graph traversal (finding efficient path between nodes).
  - Evaluates cost so far to reach point plus estimated cost from point to goal.
  - Optimality requirement: A* needs an admissable heuristic to estimate cost from current point to goal, one that is greater than or equal to 0 but less than or equal to the true cost from the current point to the goal. 
    - If this requirement is satisfied, A* tree search never returns a non-optimal solution.

### Sorting

- **Internal sorting** is used when all data is already available or can be loaded all at once in the computer memory.
- **External sorting** is used when the data (array/vector) cannot fit into the computer's memory.
  - Hadoop can handle large amounts of data in a distributed system.
- A sorting algorithm is **stable** if elements with the same key appear in output in the same order as they do in the input array (when sorting on the value). Stable sorting algorithms are preferred.
- Sorting algorithms that operate in place (without creating a new array) are preferred to those that do not.
- Sorting is required to make many other algorithms work well (e.g. binary search).
- **Bucket sort** creates an array of length equal to the largest element of the original array, then places each element at the index equal to the element's value.
  - Can store duplicates in a linked list at the duplicate's index, or can use a counter at each index.
  - Drawbacks: must know max ahead of time; must have enough memory to declare an array of length equal to max value.
  - Complexity O(n), although in some cases worst case is O(n$^2$) if each bucket needs to be sorted.
- **Merge sort** divides and conquers: divides an array into two arrays of size $n/2$, sorts the two subarrays recursively using merge sort, and then merges the two sorted subarrays. To merge the two sorted subarrays, the smallest elements of each are compared and placed from smallest to largest.
  - Very efficient and stable; relatively simple to code.
  - O(n log n) complexity.
- **Insertion sort** is simple and appropriate for small inputs (e.g. hand of cards). Each item is inserted into a sorted subarray (the "left hand") one at a time.
  - Worst case run time is O(n$^2$). Insertion sort is good when problem size is small or when data is already sorted or nearly sorted.
  - Does not require additional memory; can be fast if list is already almost sorted.
  - Insertion sort is stable.
- **Loop invariants** used to prove algorithm correctness. Checks whether properties hold true at initialization, maintenance, and termination.
- **Quicksort** divides & conquers by splitting an array into two parts, recursively sorting each, and concatenating the two pieces.
  - Requires reordering so that all values less than a particular element (called the pivot) come before the pivot and all values greater than the pivot come after it.
  - Best and average case is O(n log n), worst case is O(n$^2$). Often faster in practice than other O(n log n) algorithms (works well with a cache).
  - Not stable in efficient implementations.
- **Selection sort** works by selecting the smallest unsorted item and swapping it with the item in the next position to be filled, continuing until sorting is complete.
  - Complexity O(n$^2$) for best, worst, and average case.
  - Selection sort is not stable but is in-place.
  - Might want to use selection sort if we desire minimal data movement, but generally not good due to complexity.
  - Selection sort [animation](https://www.toptal.com/developers/sorting-algorithms/selection-sort) shown in class.