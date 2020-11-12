# Module 9: SQL

- `WHERE` statements apply to individual records, whereas `HAVING` statements apply to summarized `GROUP BY` results.
  - Can have `WHERE` and `HAVING` in the same query.
  - `HAVING` comes after the `GROUP BY` statement.
- To perform the division operation in MySQL, a double-negative approach is needed.
  - `SELECT <A> WHERE NOT EXISTS <B> WHERE NOT EXISTS <C>` gives entries for which there is not an instance where they do not match all `C` entries.
  - Can be thought of as a double for-loop.
- Can `ORDER BY` multiple attributes in different orders (e.g. `ORDER BY col1 ASC, col2 DESC`).
- High-end SQL queries vary among different database systems (MySQL, SQLite, etc.).
- Checks are truth statements for one field in one table checked upon insert, update, or delete operations. If the check fails, the operations are not allowed.
- Assetion statements are very similar to checks, but involve multiple attributes (and can compare to another table).
- Triggers are queries run upon an action (update, delete, or insertion).
  - Assertions and triggers are powerful but can be complicated. 
  - Involve more overhead than simpler operations, like data type and integrity checks, since they are performed every time a table is updated. If your database is write-heavy, these operations should be used sparingly.