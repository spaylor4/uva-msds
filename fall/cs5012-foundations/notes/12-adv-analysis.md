# Module 12: Advanced Analysis Techniques

- **Dynamic programming** involves solving complex problems by dividing them into simpler sub-problems and combining those solutions to achieve an overall optimal solution.
  - Sub-problem results are stored (in a table) to eliminate repetition (called memoization). Can reduce complexity from exponential to cubic or quadratic (or sometimes better).
  - Dynamic programming requires overlapping sub-problems (some sub-problems occur more than once) and an optimal substructure (must be possible to calculate the optimal solution to a subproblem).
  - Divide and conquer sub-problems are independent, but dynamic programming sub-problems are not.
  - Greedy algorithms are usually faster than dynamic programming, but do not guarantee an optimal solution.
  - "Upside-down recursion"
  - Applications include matrix multiplication, DNA analysis, and operations research. Algorithms include longest common subsequence, Floyd's algorithm for all-pairs shortest paths, and Viterbi algorithm for HMM.

- Longest common subsequence: given two strings, find the longest sequence of characters that appear left-to-right in both (though not necessarily contiguous, there can be other letters in the middle).
  - Used in approximate string matching,  computational biology (gene sequences), and file comparison.
  - Worst-case/brute force method takes exponential time.
- Matrix multiplication is associative, and the order of multiplication (e.g. via parenthesis) can significantly change the complexity of the calculation. Dynamic programming can be used.
- Recursive vs. dynamic programming: recursive function calls itself, but may lead to repetition for some problems. Dynamic programming stores results to avoid repeated calculations.
  - Should use dynamic programming when there are overlapping subproblems. For example, merge sort subproblems do not overlap, so it uses a recursive but not dynamic programming solution.
  - https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2G1pAq0OO0