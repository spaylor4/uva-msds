# Discrete Math Review

Readings: *Discrete Mathematics and its Applications* chapters 1.1-1.5, 2.1-2.3, 9.1

Useful [link](https://rstudio-pubs-static.s3.amazonaws.com/100749_6b0f55153e71461fa382fd2a2db66507.html#select-symbols-and-operators) and [guide](http://davidagler.com/teaching/logic/handouts/supplemental_material/MarkdownForSymbolicLogic.html) with markdown for various logical operator symbols.

- What is logic? Logic is a science that deals with the principles of the validity of inference, and it has well-defined syntax (symbols & rules), semantics (meaning), and proof-theory.
- Why study logic? Improve the quality of arguments, communication, and thinking; computer languages and AI depend heavily on logic.

### Logic & Proofs

- A **proposition** is a declarative statement that is either true or false.

- The **negation** of a proposition $p$ is the statement "It is not the case that $p$", denoted $\neg p$.  A negation is a type of compound proposition, because it is a proposition constructed from another proposition.

- The **conjunction** of two propositions $p$ and $q$ is the proposition "$p$ and $q$", denoted $p \wedge q$ and true only when both $p$ and $q$ are true.

- The **disjunction** of two propositions $p$ and $q$ is the proposition "$p$ or $q$", denoted $p \vee q$ and true when either $p$ or $q$ (or both) is true.

- The exclusive or of two propositions $p$ and $q$ is the proposition that is true when exactly one of $p$ and $q$ is true and false otherwise.

- An **implication** or conditional statement $p \rightarrow q$ is false only when $p$ is true and $q$ is false, and is true otherwise. Implications do not imply causation.

  - Helpful to think of an implication as a promise - it can only be false (broken) if the first statement happens but the second does not.
  - The **converse** of $p \rightarrow q$ is $q \rightarrow p$.
  - The **contrapositive** of $p \rightarrow q$ is $\neg q \rightarrow \neg p$.
  - The **inverse** of $p \rightarrow q$ is $\neg p \rightarrow \neg q$.

- A **biconditional** ($p \leftrightarrow q$) means "$p$ if and only if $q$" and is true when $p$ and $q$ have the same truth value (both true or both false).

- A compound proposition that is always true is called a **tautology**, a compound proposition that is always false is called a **contradiction**, and a compound proposition that is neither a tautology nor a contradiction is called a **contingency**.

- Propositions are logically equivalent ($p \equiv q$) if their truth values in all cases are the same.

- **DeMorgan's Laws**: 

  $\neg(p \wedge q) \equiv \neg p \vee \neg q$  "Not p and q is equivalent to not p or not q"

  $\neg(p \vee q) \equiv \neg p \wedge \neg q$  "Not p or q is equivalent to not p and not q"

- $\exists$ is the existential quantifier. $\exists x P(x)$ means "there exists an $x$ such that $P(x)$."
- $\forall$ is the universal quantifier. $\forall x P(x)$ means "$P(x)$ for all values of $x$ in the domain."
  - Note: $\exists x \forall y$ is not the same as $\forall y \exists x$. For an example function Loves($x, y$), the former is "there exists a person who loves everyone in the world," while the latter is "for everyone in the world, there exists a person who loves them."
- The uniqueness quantifier, usually denoted $\exists !$ or $\exists 1$, means "there exists a unique $x$ such that $P(x)$ is true."
- An argument consists of a sequence of premises and a conclusion.
  - A valid argument is true whenever the premises are all true.
- Operator order of preference: $\neg$ is evaluated first, then $\vee$ and $\wedge$, then $\rightarrow$ and $\leftrightarrow$.

### Sets & Functions

- A set is an unordered collection of elements. $a \in A$ means that $a$ is an element of set $A$, and $a \notin A$ means that $a$ is not an element of set $A$.
  - Sets are typically denoted by uppercase letters with the elements in curly braces. For example, the set of all vowels in English can be written $V = \{a, e, i, o, u\}$.
  - The empty set has no elements and is usually denoted by $\emptyset$ or {}.
  - The universal set has all possible elements related to the subject and is usually denoted by $U$.
- The set $A$ is a **subset** of $B$ ($A \subseteq B$) if and only if every element of $A$ is also in $B$.
  - If $A \subseteq B$ and $B \subseteq A$, then $A$ and $B$ are equal.
  - A proper/strict subset ($A \subset B$) must have fewer elements than the comparison set.
  - If $A$ is a subset of $B$, then $B$ is a superset of $A$ ($B \supseteq A$).
- The **union** of $A$ and $B$ ($A \cup B$) is the set that contains elements that are in $A$, $B$, or both.
- The **intersection** of $A$ and $B$ ($A \cap B$) is the set that contains elements that are in both $A$ and $B$.
  - Two sets are called disjoint if their intersection is the null set.
- A binary relation R on a set A is **symmetric** if for all a, b $\in$ A, (a, b) $\in$ R implies that (b, a) $\in$ R.
- A binary relation R on a set A is **transitive** if for all a, b, c $\in$ A, if (a, b) $\in$ R and (b, c) $\in$ R then (a, c) $\in$ R.
- A binary relation R on a set A is **reflexive** if (a, a) $\in$ R for all a $\in$ A.

### Predicate Logic

- Predicate logic is an enhanced version of propositional logic that can handle a greater variety of real-life statements, relations, and functions. Predicate logic uses quantifiers ($\exists$, $\forall$, etc.) to indicate how frequently a statement is true.
- A predicate is a property that a variable or finite collection of variables can have, and it becomes a proposition when specific values are assigned to the variables. Often used to create loops in programming and to query databases.
- The domain/universe of discourse may affect the truth value of logical arguments.