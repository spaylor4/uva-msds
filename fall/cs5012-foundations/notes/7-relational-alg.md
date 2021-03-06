# Module 7: Relational Algebra

- Six fundamental operations of relational algebra, three unary (selection, project, rename) and three binary (union, set difference, and Cartesian product).
- **Selection**: select specific tuples (rows) from a relation (table).
  - Selection predicate is a comparison (can be compound of multiple comparisons) that determines what is selected.
  - Different from SQL `SELECT` statement (equivalent to `WHERE`).
- **Projection** returns specific attributes (columns) from a relation (as in SQL `SELECT`).
  - Duplicate tuples are removed in resulting relation.
- **Rename** renames the result of an expression and (optionally) its attributes.
- **Union** combines tuples from two relations.
  - Relations must have same number of attributes and compatible data types.
  - Equivalent to "or" and to a SQL `UNION ALL` operation.
  - **Intersect** is the similar, but combines tuples present in both relations (equivalent to "and").
- **Set difference** returns all tuples that are in one relation but not another.
  - Must meet same conditions as union/intersection, with same number of columns and same data types between relations.
  - Equivalent of SQL `EXCEPT` statement.
- **Cartesian/cross product** combines information from any two relations with combined schemas of the two relations. Result will have attributes of first relation followed by attributes of the second.
  - Equivalent to `CROSS JOIN` in SQL (not very common to want every combination).
- **Natural join** (inner join) takes the cross product of two relations and then selects rows with equal attributes that appear in both relations, removing duplicate attributes.
  - Also called `NATURAL JOIN` in SQL.
  - Theta join in relational algebra is equivalent to default SQL `JOIN` (gives more control).
- **Outer join** extends natural join to include tuples from one relation that do not match the other, padding with null values as necessary.
  - Left outer join keeps all relations in left table and matches from right table.
- The **division** operation takes two sets of attributes "AB" and returns list of "A" for all "B" when performing "AB $\div$ B."
- **Aggregate** functions take the min, max, sum, count, or average of an attribute in a relation.
- Relational algebra is the logic behind SQL. Relational algebra is procedural, while relational calculus is declarative.
- Query optimization involves thinking about the ordering of SQL statements to improve runtime (e.g. joining after filtering a table rather than the other way around).