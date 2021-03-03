# Module 2: RDDs and Running Spark on a Cluster

Readings: Ch. 3, 4, & 7 of *Learning Spark*

### Ch. 3: Programming with RDDs

- An RDD is an immutable distributed collection of objects split into partitions that can be spread out over multiple nodes in a cluster.
  - RDDs can contain any type of object, including user-defined Python objects.
- **Transformations** are operations that create new RDDs from existing ones (e.g. `filter`), while **actions** are operations that compute some result from an RDD (e.g. `count`).
  - Transformations can operate on more than one RDD, e.g. `rdd1.union(rdd2)` to combine two RDDs.
  - Spark uses a lineage graph to map dependencies between RDDs that is used in their computation.
- Spark uses **lazy** evaluation: it computes new RDDs only as needed, to avoid reading in more data than is necessary.
  - Transformations and loading data are lazy, and they are executed when an action is called.
- Spark doesn't store RDDs persistently in memory unless explicitly specificied. By default, it recomputes an RDD each time an action is run on it.
  - To specify that an object should persist in memory, use `RDD.persist`
  - Can specify where to store data using `persist(StorageLevel.DISK_ONLY)` or `MEMORY_AND_DISK`, etc.
  - Can manually remove RDDs from the cache using `unpersist`
  - If you try to cache too much data to memory, partitions will be removed starting with the least recently used ones.
- RDDs are usually created from loading external datasets. They can also be created from an existing collection using `sc.parallelize(collection)`, but this requires that the entire collection first be in memory on one machine.

- Most transformations and some actions involve passing functions into Spark. These can be lambda, top-level, or user-defined functions.
  - Need to be careful about passing a function with references to fields or functions in an object (e.g. `self.property`). This sends the whole object to the nodes, not just the property in question, which can be slow or cause the operation to fail if Python can't pickle the object. 
- Some common transformations/actions that work with any RDD:
  - Element-wise transformations, including`map` and `filter`. 
    - `map` applies a function to each element of an RDD and does not require that the input and return types match.
    - A `flatMap` produces multiple output elements for each input element and combines (flattens) them into one RDD holding the elements from all the iterators.
  - Pseudo-set operations, like `distinct`, `union`, `intersection`, and `subtract`.
    - `distinct` is expensive because it involves lots of shuffling.
    - `union` includes duplicates if an item exists in both RDDs, but `intersection` does not.
    - `cartesian` calculates the Cartesian product between two RDDs.
  - `reduce` is one of the most common actions, and can be used to aggregate RDDs (sum, count, etc.). `fold` and `aggregate` work similarly, but take in a "zero value," and `aggregate` allows the return type to differ from the input type.
  - `collect` returns an RDD's entire contents to the driver node, which requires that it can all fit in a single machine's memory. `take(n)` returns $n$ elements from as few partitions as possible, so it may be a biased sample.
  - `foreach` performs an action on each element without returning a result to the driver program (e.g. posting data to a webserver).

### Ch. 4: Working with Key/Value Pairs

- Pair RDDs are those containing key/value pairs.
  - Often created from regular RDDs using a `map` that creates a tuple.
- Transformations operate on tuples, for example, `reduceByKey(func)` combines values with the same key according to a specified function.
- Other transformations can join two pair RDDs, such as `join`, `rightOuterJoin`, `subtractByKey`.
  - `join` performs an inner join.
- The `mapValue` function is convenient when we want to access just the values. This can also be accomplished via `map`, but is more concise with `mapValue` for pair RDDs.
- Can use `groupByKey` to return an RDD with an iterable for each key.
- Spark allows for advanced partitioning to specify functions that ensure that some set of keys will be partitioned onto the same node.
  - For example, hash partitioning an RDD will speed up joins by sending the second RDD's elements to the appropriate node according to hash, rather than having both RDDs hashed and shuffled on every call to join.
    - Should hash partition the larger RDD if possible.
  - `partitionBy` returns a new RDD that must be persisted/saved to take advantage of the partitioning.
  - Should make the number of partitions at least as large as the number of cores in your cluster.
  - Operations that involve shuffling and can benefit from partitioning include `cogroup`, `groupWith`, `join`, `rightOuterJoin`, `groupByKey`, `reduceByKey`, `combineByKey`, and `lookup`.
  - Some operations result in a partitioner being set on the resulting RDD, including all of the above except `lookup`, along with `sort` and `mapValues`.
  - Should use `mapValues` or `flatMapValues` whenever not changing an element's key in order to maximize partitioning optimizations.
  - Can write custom partitioners, for example to partition by domain name of a URL.
    - In Python, this is accomplished by passing a hash function to `RDD.partitionBy` in addition to the number of partitions.

### Ch. 7: Running on a Cluster

- In distributed mode, Spark consists of a driver and several executors or cluster workers. 
  - The driver converts a user program into tasks and schedules the tasks on the executors.
  - Executors run tasks and return results to the driver, and provide in-memory storage for cached RDDs.
- When submitting a spark job using `bin/spark-submit`, you can specify a cluster URL, e.g. `spark://host:7077` using the `--master` flag. The general format for spark-submit is `bin/spark-submit [options] <app jar | python script> [app options]`.
- The cluster manager determines how to share resources when multiple people are trying to run jobs on a cluster at the same time.
- Generally, Spark works better with fewer larger executors (more cores and memory), but sometimes the size of executors in a cluster is limited.

### Class Notes

*February 16, 2021*

- Some transformations are *narrow*: they can operate independently on each partition, then combine the results (e.g. `filter`). Other transformations are much more complex or *wide* (e.g. median, since it requires ordering all the data).
  - `distinct` is also expensive, so you should consider whether it is needed.
- `reduceByKey` reduces locally on each node as much as possible before combining globally by key.