# Module 3: Hashing & Indexing

Readings: *Introduction to Algorithms* ch. 11 (esp. 11.1-11.2)

### Hashing

- A **hash table** or hash map is a data structure that maps keys to values. It uses a **hash function** to place an index into an array of buckets/slots.
  - A hash function produces an integer which can be used as an address in a hash table.
  - Hash tables allow us to directly find an item by it's key in O(1) time.
    - Hash tables allow us to find any element using RAM with no latency.
    - In a well-dimensioned hash table, the average cost of each lookup is independent of the number of elements in the table.
  - Ex: python dictionary implements hash tables. Hash functions can also be useful in cryptography, DNA analysis, and privacy measures, among others.
  - A **hash index** is an array of buckets in which search keys and their associated pointers are organized. Multiple items can be associated with one index/bucket through linked lists.
  - The values returned by a hash function are called **hash codes**, sums, or integers.
  - Hash functions first create an original hash code for the key ("prehash"), then transfer this number to a smaller number (often using modulo function).
    - Just using the prehash as the hash code is wasteful (longer array than needed) or may cause multiple values to be assigned to same spot.
  - Ideally, hash function will assign/map keys to a unique index/bucket, but this rarely occurs in practice (unless new entries are never added). **Hash collisions** occur when different keys are assigned to the same bucket.
  - Good hash functions are unlikely to return the same hash code for different keys, but must return the same code for the same key. A perfect hash function will never return the same code for different keys (rare).
- Two basic methods for handling hashing collisions: chaining and linear probing.
  - Chaining stores incoming duplicate entries in an overflow list chained to that bucket index.
    - Rule of thumb for minimizing collisions is to make size of hash table $m$ about 33% larger than the number of keys $n$.
  - In linear probing, when a collision occurs, look through subsequent hash elements until a free space is found.
    - Must have $m > n$ so that some empty slots are available.
    - Each bucket has a flag: empty, occupied, or deleted ("lazy probing"). When looking for a key, if its hash has a "deleted" flag, must continue looking, in case it was a collision and was pushed to a subsequent bucket.
    - Linear probing has more misses per lookup as the load factor increases.
- A **direct access table** acts like a hash table, but with no hash function, instead using an integer index corresponding to each slot.
  - Effective when keys are drawn from a small universe of keys of integers.

- Hashing functions are not invertible (good for security/privacy).

### Indexing

- An **index** is a simple signal used to facilitate searching and improve the speed of data retrieval.
  - Especially useful for databases when tables are large.
- Most databases use an **ordered index**, which organizes records using a pointer chain so they are in "cluster" order. Some databases use a **hash index** as opposed to an ordered index.
- **Primary** and **secondary** indices: a primary (clustering) index is the search key that specifies the order of the file. A secondary (non-clustering) index specifies an order different from the sequential order of the file. 
  - A secondary index must contain pointers to all records for that search key (must be a dense index), since other records with that search-key value could be anywhere in the table.
  - Secondary indices improve the performance of queries on non-primary keys, but impose serious overhead on database modification, since every index must be updated whenever a file is updated.
- A **dense index** has an index record for every search key value in the file, while a **sparse index** has index records for only some keys.
  - To find a record in a table with a sparse index, find the index record with the largest search-key value less than or equal to the search-key of interest, then proceed sequentially.
  - Dense index on an ordered table is redundant, so a primary index on an ordered table is always sparse. Unordered tables use dense or secondary indices.
  - Dense indices generally faster, but require more space and more maintenance for insertions/deletions.
  - When designing a database, can index a lot for a read-heavy database, but want to index sparingly for a write-heavy database.
  - Multi-level indices (sparse index on the index) can be used when a sparse index grows too large.
  - If index is too large to be kept in memory, a search will require several disk reads. An index with overflow blocks will require sequential search, while one without overflow can use binary search.