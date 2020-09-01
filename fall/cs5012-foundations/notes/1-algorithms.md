# Module 1: Introduction to Algorithms

- An **algorithm** is a detailed step-by-step method for solving a problem.
  - Steps are precisely stated and determined based on inputs & previous steps.
- **Data structures** are logical relationships among data elements designed to support specific manipulations. Ex: array, table, etc.
- Compare the algorithms that implement operations in order to compare the operations' efficiency. Time is usually the most-relevant measure of efficiency (others include memory and CPU usage).
  - Efficiency usually depends on the size and nature of the input.
  - **Benchmarking** = timing of algorithm for some specific input. Inadequate for predicting performance on other data sets.
- The processing time can be expressed as a function of $n$, the problem size. **Asymptotic analysis** examines the behavior of $f(n)$ as $n$ gets large (since that is when differences in performance become apparent and matter more). This gives an estimate of the scalability of the program.
  - The slower the asymptotic growth rate, the more efficient the algorithm (e.g. linear is better than quadratic).
- Asymptotic analysis focuses on the **order** of $f(n)$: exponential, quadratic, log-linear, linear, etc. The **order class** labels all functions with the same highest-order term using "Big-O" notation.
  - The order class O($f(n)$) is an upper bound on efficiency. Less-frequently used notation $\Theta(f(n))$ is more precise and is the set of all functions that grow at exactly the same rate.
  - When an algorithm is of a lower order than another, it is asymptotically superior. For small $n$, a more complex algorithm may perform better, but there is a value of $n$ after which the lower order algorithm always performs better.
  - Common order classes:
    - O(1): constant time (e.g. insert/remove in queue, variable declaration)
    - O(lg n): logarithmic time (e.g. binary search)
    - O(n): linear time (e.g. traversal of list/array, find min/max element in list)
    - O(n lg n): log-linear time (e.g. best sorting algorithms like Quicksort and Mergesort)
    - O(n$^2$): quadratic time (e.g. poorer sorting algorithms, double-nested loops)
    - O(2$^n$): exponential time (e.g. recursive Fibonacci implementation, generating all permutations of $n$ symbols)