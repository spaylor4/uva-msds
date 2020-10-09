# Module 6: Databases in Python

Readings: [History of Databases](https://clutejournals.com/index.php/IJMIS/article/view/7587/7653), [A Relational Model of Data for Large Shared Data Banks](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf), [SQLite vs MySQL vs PostgreSQL](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems)

- A database is a self-describing (via metadata) collection of integrated records.
- Early databases (1960s) were navigational: data was accessed by following pointers from one record to another.
  - Drawback: would need to know physical structure of database to query it.
- Relational databases developed (1970s) to search for data by content rather than using links.
- NoSQL databases are non-relational, distributed data stores (e.g. BigTable) optimized for retrieve and append operations. Main function is data storage.
- Distributed databases can be stored in multiple locations
- SQLite doesn't take up much space, is user friendly, and is stored in a single file, making it easily portable.
  - Not well-suited for concurency and high-volume data.
- MySQL is most popular, prioritizes speed, and allows for user management/security (unlike SQLite).
  - Not fully SQL compliant (e.g. can't do `FULL JOIN`).
  - Good for websites/web apps; not good for concurrency/high-volume data.
- PostgreSQL is open source and extensible.
  - Good for concurrency/complex operations.
  - Not good when speed is most important factor. May be overkill for simple setups.