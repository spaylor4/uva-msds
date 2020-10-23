# Module 8: Entity-Relationship Diagrams

- E-R is like object-oriented programming for databases.
- An **entity** is an object distinguishable from other objects (like an instance of a class). An **entity set** is a set of entities of the same type that share the same properties (like a class).
- Entitities have **attributes** or properties, each of which have **domains**.
- E-R diagrams represent entities as rectangles and attributes as ovals.
  - Some attributes can be multivalued, represented by concentric ovals.
  - Some attributes are composite attributes, consisting of multiple component attributes.
- A **relationship** is an association among entities.
  - Represented by diamonds in E-R diagrams.
  - Attributes can be attached to a relationship set via a dotted line. These attributes are only relevant to the relationship, not to either of the entity sets on their own.
  - Self-referential relationships are when occurences of an entity set play different "roles" in a relationship (e.g. course ID and pre-req ID).
- **Total participation** means that all entities in an entity set participate in a relationship.
  - Represented by a double line in E-R diagram.
- **Cardinality** (one-to-one, one-to-many, etc.) represented by arrows: the line said represents the "many" side, while the arrow side represents the "one" side.
  - If the relationship is 1:1, pick one of the two primary keys to be the primary key of the relationship.
  - If the relationship is m:m, both of the primary keys form the primary key of the relationship.
  - If the relationship is 1:m or m:1, the primary key on the many side is the primary key of the relationship.
- A **weak entity set** doesn't have sufficient attributes to form a primary key and is dependent on an associated strong entity set through an identifying relationship.
  - Identified by a discriminator (primary key is primary key of strong identity set + discriminator).
  - Must be total participation between weak entity set and it's identifying relationship.
  - The table will include the primary key of the corresponding identifying strong set along with all attributes from the weak entity set.
- A strong entity set has a primary key and attributes as columns.
  - If there are composite attributes, only the separate components become columns (the combined higher-level component doesn't).
  - Multivalued attributes are stored in a separate table with primary key of entity set and multivalued attribute columns.
- **Generalizations** and **specializations** are like superclasses and subclasses - they have an "is a" relationship, and the specialization has the more info than the generalization.
  - When choosing how to create tables for generalizations and specializations, want to minimize duplication.
- Each entity set and relationship set correspond to one table in a database (and corresponding ER diagram).

### Class Notes

- A schema is like a contract between you and a database that helps make the database more efficient.