# Module 6: Regular Expressions and Introduction to Databases

### P vs NP

- Class so far has dealt with algorithms that are *solveable* in polynomial time, or complexity class $P$.
- Nondeterministic polynomial complexity class $NP$ consists of all algorithms that can be *verified* in polynomial time.
  - If a problem can be solved in polynomial time, it can also be verified in polynomial time ($P \sub NP$).
  - Some problems are easy to verify but hard to solve (e.g. number of colors for US map such that no bordering states are same color).
- $NP$-Complete are the hardest problems in complexity class $NP$.
  - 3-Satisfiability Problem: given $n$ Boolean variables $x_i$, $m$ three-clauses $l_i$ (combinations of the $x_i$'s' using and/or/complement), are there values such that $l_1 \and l_2 \and ... \and l_m$ is true?
    - Easy to verify but hard to find values - no polynomial-time method for finding values (brute force takes O($2^n$)).
  - 0-1 Knapsack Problem: given $n$ objects each with a value and weight, what is the maximum value of objects that can be put in a knapsack with a maximum weight capacity.
- A problem is $NP$-Hard if it can be reduced from a $NP$-complete problem. They are at least as hard as $NP$-complete.
  - In many cases, can approximate a solution in polynomial time.
  - Heuristics may give solutions in polynomial time, but not guaranteed as with approximate solutions.
  - K-means clustering is NP-hard, but heuristic k-means algorithm finds pretty good groups in polynomial time.
  - For $NP$-hard problems, even checking a solution is in class $NP$.

### Regular Expressions

- Regex provides a way to express how a computer should look for patterns in text.
- Useful in recognizing phone numbers, addresses, emails, etc.
- Metacharacters:
  - Square brackets indicate a range of characters.
  - Dot matches any single character (only when outside square brackets).
  - Caret inside square brackets excludes characters from match.
  - Question mark matches previous element zero or one times. Plus sign matches previous element one or more times. Asterisk matches previous element zero or more times.

### Intro to Databases

- Database Management System (DBMS) is software for managing databases: the data, the database engine (controls access), and the schema.
- Distributed database model (noSQL, Javascript-based) contain lots of redundancy.
- Databases have physical data independence: you are working with a model of the data that abstracts away stuff we don't want to deal with.
  - Can for the most part ignore which database engine is used.
- Schema is logical design of the database, while an instance is a snapshot of the data stored in the database at a particular time.
  - Schema : class in object oriented programming :: instance : variable in object oriented programming.
- A relation is the equivalent of a table in relational algebra and theoretical mathematical databases. Relations have no order and no duplicates, unlike tables.
  - Relations have tuples and attributes instead of rows and columns.
- A super key is any set of attributes that uniquely define a tuple. A candidate key is a minimal super key (i.e. no unnecessary attributes). A primary key is the candidate key chosen by the database admin to be used for a particular table.
- Data definition language (DDL) affects the schema (e.g. `CREATE` or `ALTER TABLE` statements). Data manipulation language (DML) affects an instance (e.g. `SELECT`, `INSERT`, or `UPDATE` statements).