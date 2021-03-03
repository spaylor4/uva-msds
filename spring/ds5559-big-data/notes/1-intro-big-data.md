# Module 1: Intro to Big Data Analytics

Readings: Ch. 1 & 2 of *Learning Spark*

### Ch. 1: Intro to Data Analysis with Spark

- Spark is a computational engine that schedules, distributes, and monitors tasks computed on multiple machines within a cluster.
- Spark extends MapReduce to run computations on large data quickly. One way it accomplishes this is by running computations in memory.
- Spark integrates SQL, streaming data, machine learning, and graph processing.
- Spark does not require Hadoop but can create datasets from the Hadoop distributed filesystem (HDFS).

### Ch. 2: Downloading Spark and Getting Started

- Spark is written in Scala but includes APIs allowing it to be used with Python or Java as well.

- Spark can run in local mode (on a single machine) or distributed mode (through Mesos, YARN, or the Standalone Scheduler).

- Resilient distributed datasets (**RDDs**) are Spark's fundamental abstraction for distributed data and computation across a cluster.

- Spark applications contain a **driver program** that defines distributed datasets on a cluster and applies operations to them on multiple worker nodes/executors. Driver programs access Spark through a `SparkContext` object, which represents a connection to a computing cluster. 

  - In a shell, the driver program is the shell itself, and a SparkContext is automatically created. To create an application, you must create a SparkContext yourself.

  ```python
  from pyspark import SparkConf, SparkContext
  conf = SparkConf().setMaster("local").setAppName("My App") sc = SparkContext(conf = conf)
  ```

  - The `setMaster` method connects to a cluster (or a local machine).

### Class Notes

*February 9, 2021*

- MapReduce involves splitting some input data onto multiple workers, then mapping to create some key-value pair. Then shuffling puts like keys on the same machine, followed by reducing that performs some computation to produce the final result.
  - Want to avoid shuffling when possible, as it is the most expensive.
- DS5559 kernel in Rivanna has Spark installed.
- PySpark inherits a lot of Python functionality (e.g. `type`).
- PySpark commands can be chained together using dot (Need \ to continue to next line).
- RDDs are the most basic abstraction in Spark. Dataset and DataFrame objects released with Spark 2.0 that use RDDs under the hood.
- `collect` should only be used when you have a small amount of data (i.e. after reducing/aggregating).