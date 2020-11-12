# Module 10: Transactions, Distributed Databases, and NoSQL

### Transactions and Concurrency Control

- ACID properties define what makes a good database. Guarantee that database transactions are processed reliably.
- A **transaction** is a single logical operation on the data, usually consisting of multiple queries.
- **Atomicity**: either all of a query runs or none of it.
  - "All or nothing"
- **Consistency**: want databases that accurately represent the world. Database must remain in a constant state before and after transactions are run. 
  - "Models the real world"
  - Accomplished through the use of primary/foreign keys, constraints, triggers, etc.
  - Requirements modeling of the database.
- **Isolation**: every query runs as if it is the only query running (queries can't interfere with each other).
  - "As if you're the only one"
- **Durability**: ability to recover the database if something goes wrong.
  - "Recoverability"
- ACID properties are related/intertwined. Atomicity, Isolation, and Durability all can be viewed as enforcing Consistency.
  - NoSQL and distributed databases are not ACID compliant.
- **Transaction safe databases** are those that guarantee ACID properties will hold and that you can't mess up the database by running queries.
- Transactions have different states: active state (a transaction begins), partially committed state (queries have executed but not yet been committed), end state (commit is called and changes are written to memory).
- **Logging**: good databases record all queries in active and partially committed states, making it possible to **rollback** transactions if execution fails.
- Isolation and concurrency control: how to determine order of queries when multiple users query the same data?
  - In a **serial schedule**, every transaction appears to run independently (one transaction runs to completion before the next starts).
    - Single-thread, single-execution environment.
    - Can be very slow.
  - **Pre-emptive scheduling** allows non-conflicting operations to be reordered (**conflict serializable**).
    - ACID-compliant databases must be able to generate conflict serializable schedules to fulfill the Isolation property.
    - Doesn't improve raw performance but reduces average response times.
  - **Deadlocks** occur when two queries try to access the same data at the same time.
  - Want to avoid **cascading rollbacks** where subsequent queries have to be undone due to a prior query aborting.

### Distributed Databases

- Database architecture styles: centralized, parallel, or distributed systems.
- **Centralized systems** run on a single computer and have no concurrency.
  - Will run different queries on different processors, but won't split parts of the same query among different processors.
- **Parallel systems** have multiple CPUs to improve speed (ability to run more queries) and scale (ability to execute more complex queries).
  - Shared-memory architecture: all processors and disks have access to common memory on a bus. The bus speed will be the bottleneck.
  - Shared-disk architecture: all processors access all disks via a network, but have private memory. The connection will be the bottleneck.
  - Shared-nothing architecture: use a network to communicate. Non-local disk access will be the bottleneck.
- **Distributed systems** use shared-nothing architecture in which machines are in different physical locations.
  - Scalable, less danger of single-point failure due to replication of data.
  - Homogeneous strategy: all sites have identical software and similar schema. Heterogeneous strategy: sites may have different softwares and schemas. Heterogeneous strategy causes problems with query/transaction processing.
  - Data storage utilizes replication (storing multiple copies of data in different sites for faster retrieval and fault tolerance) and fragmentation (vertical and horizontal partitioning).
  - Distributed systems trade consistency for availability.
- CAP Theorem: can have at most two of Consistency, Availability, and Partitions.
  - Large systems will partition, so choose either C/P. Traditional databases choose consistency, while most web apps choose availability.
- **BASE** properties replace ACID for distributed systems: "basically available, soft state, eventually consistent."
  - Much more relaxed than ACID.
  - Databases may not all be in the same state at the same time.

### NoSQL

- Not all data can be expressed in a relational format, and sometimes want horizontal scaling to clusters of machines (or the cloud).
- NoSQL originated from JSON.
- NoSQL good for hierarchical and unstructured data; SQL good for standard interface, transactional data, and complex query-intensive environments. NoSQL also good for very large data that needs to be partitioned.
- Can start with SQL and migrate to NoSQL later if needed.
- Types of NoSQL databases:
  - Key-Value Store: contains many key spaces, each of which can have multiple identifiers to store key-value pairs.
    - Simple, highly available applications.
    - Amazon DynamoDB, Redis, etc.
  - Document Oriented Collections: database comprised of collections (analagous to tables), each of which can contain many documents (analagous to rows).
    - Web-based applications and RESTful services.
    - MongoDB, Couchbase, etc.
  - Column-Based Store: wide tables with column families, each of which contains multiple columns. Column values sparsely distributed with key-value pairs.
    - Data warehousing and OLAP applications.
    - HBase, Cassandra, BigTable, etc.
  - Graph-Based Databases: network of notes and edges.
    - Social media and network problems involving complex queries with many joins.
    - Neo4J, OrientDB, etc.