# Module 3: Spark DataFrames and Spark SQL

Readings: *Learning PySpark* [Ch. 3](https://learning.oreilly.com/library/view/learning-pyspark/9781786463708/ch03.html)

- Spark DataFrames add a schema structure to the RDD, which allows for integration with Spark SQL and can improve performance.
- PySpark with RDDs requires some overhead due to mapping from Python to Java (via the JVM) before worker nodes process data.
- The Spark SQL Catalyst Optimizer determines the most efficient physical plan for executing queries.
  - PySpark DataFrames use the Catalyst Optimizer to put Python performance on par with SQL, Scala, R.
- Some DataFrame operations are lazy, but not as lazy as RDD operations due to the use of the Catalyst Optimizer.
- Can use `take(n)` or `show(n)` on either DataFrames or SQL queries to see $n$ rows.
- To run SQL, use `spark.sql(query)`.
  - In Databricks, can use `%sql` at the top of the cell and then just write regular SQL queries.
- `DataFrame.printSchema()` will show the column names and datatypes.
- To manually specify a schema, use `StructType([StructField("field1", LongType(), True), ..., StructField("fieldn", StringType(), True)])`, where each field has name, type, and nullable.
- `df.count()` returns the number of rows.
- Can execute SQL-like clauses in Python using clauses like `.filter()` and `.select()`.
- Parquet files are the most commonly-used with Spark SQL. Parquet files are columnar and automatically preserve the schema of the original data.

### Class Notes

*February 23, 2021*

- Schema consists of 3-tuples: `(column_name, data_type, nullable)`
  - Column name is a string
  - Data type is `StringType()`, `IntegerType()`, etc.
- Spark can infer the schema, but it takes more computation to do so and doesn't always work correctly.
- Converting from pandas to Spark DataFrame can be slow, so best to use Spark DFs from the beginning when possible. Spark 3.0 has koalas that mimics pandas.
- Can convert to an RDD using `df.rdd`
- Driver node usually needs less RAM than workers.
- Usually will be able to use DataFrames, but some ML stuff only works with RDDs, though this is shifting. Might use RDD rather than DF if your data is log files or another non-tabular data form.
- Resource overhead: some cores/memory/etc. will be taken up by OS, Hadoop Daemons, and resource manager. These will need to be accounted for when designing the instance.
- `df.where()` and `df.filter()` are equivalent.
- To write SQL queries on a DF, first do `df.createOrReplaceTempView('table_name')`, then can do `spark.sql(query)` referencing the temp view.
  - Replaces deprecated `.registerTempTable`
- Looping is sequential, not parallel, so should avoid looping whenever possible and use parallelizable functions, like `groupBy` and `agg`.
- Parquet files are columnar - useful if you don't care about all columns and only want to read in some.
- `SparkSession` is a context manager that incorporates the older SQL and Hive contexts.
- An application running more than 5 concurrent tasks usually doesn't perform well, so it's suggested to use `spark.executor.cores = 5` when setting up a cluster.
  - Uses all cores by default, but not always optimal.
- Partitioned tables can be used to make queries faster by limiting the scope of the query. Each partition is usually stored in a designated partition directory.