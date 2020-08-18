## Module 10: Aggregates with NumPy and Pandas

- `np.min()` and `np.max()` are far more efficient than the built-in `min()` and `max()` functions.
  - `np.argmin()` and `np.argmax()` return the index of the min/max.
- For numpy aggregate functions, the axis keyword specifies the dimension of the array that will be collapsed, rather than the dimension that will be returned. So, specifying axis=0 means that the first axis will be collapsed. For two-dimensional arrays, this means that the values within each column will be aggregated. 
- In Pandas groupby `df.groupby('key1')['data1']`  is equivalent to  `df['data1'].groupby(df['key1'])`.
  - Can also group by functions, not just values.
  - Can include `as_index=False` argument to avoid hierarchical groupings.
- Further [reading](https://nikgrozev.com/2015/07/01/reshaping-in-pandas-pivot-pivot-table-stack-and-unstack-explained-with-pictures/) on groupings.