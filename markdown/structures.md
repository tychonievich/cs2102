---
title: Structures
...

This page attempts to provide a summary of all of the discrete structures that will be used in this class.

# Set

A **set** is a value whose only property is having other values as its **members**.
The most common representation of a set is as its members written between braces.
The members of a set have no position, order, number of times appearing in the set, or any other properties beyond being a member of the set.

The number of distinct members of a set $S$ is called the set's **cardinality** and is denoted $|S|$.

:::example
The set $\{2,3,5,7\}$ has cardinality 4; its members are $2$, $3$, $5$, and $7$.
This same set can equivalently be written $\{3,7,2,5\}$ or with its members in any other order.
:::

The empty set has no members and is denoted either $\{\}$ or $\emptyset$.
Note that $\emptyset$ is a different symbol than $0$ (zero) or $\phi$ (the Greek letter phi).

The expression $x \in S$ is true if and only if $x$ is a member of $S$ (and thus only if $S$ is a set).
$x \notin S = \lnot(x \in S)$.

A set can be defined based on any [predicate](#function)
using **set-builder notation**:
$\big\{ f(x) \;\big|\; P(x)\big\}$ is the set of all $f(x)$ where $P(x)$ is true.

:::example
$\{ x+2 \;|\; 1 < x \le 2 \}$ is the set of all numbers greater than 3 and no greater than 4.

$x \in \big\{x\;\big|\;P(x)\big\}$ is a long way of writing $x \in P(x)$.

$\big\{x\;\big|\;x \in S\big\}$ is a long way of writing $S$.
:::

The following set operators are defined:

Union
:   $S \cup T = \big\{x \;\big|\; (x \in S) \lor (x \in T)\big\}$

Intersection
:   $S \cap T = \big\{x \;\big|\; (x \in S) \land (x \in T)\big\}$

Set Difference
:   $S \setminus T = \big\{x \;\big|\; (x \in S) \land (x \notin T)\big\}$

The following set-comparison predicates are defined:

Subset
:   $S \subseteq T = \forall x \in S \;.\; x \in T$

Proper Subset
:   $S \subset T = (S \subseteq T) \land (S \ne T)$

Superset
:   $S \supseteq T = T \subseteq S$

Proper Subset
:   $S \supset T = T \subset S$

The **power set** of another set $S$ is the set of all the subsets of $S$.
The *power set* is denoted $\mathcal P(S)$ or pow($S$)
and can also be written $\{ T \;|\; T \subseteq S\}$.

$\big|S\big| = 2^{\big|\mathcal P(S)\big|}$.

The number of distinct $k$-member subsets of a $n$-member set is denoted $n \choose k$, read "$n$ choose $k$", and is equal to $n! \over (n-k)! k!$

:::example
The power set of $\{1,2,3\}$ is 
$\big\{ 
\{\},
\{1\},
\{2\},
\{3\},
\{1,2\},
\{1,3\},
\{2,3\},
\{1,2,3\}
\big\}$, which has $2^3 = 8$ members, each a subset of $\{1,2,3\}$.

The set of two-element subsets of $\{1,2,3,4,5\}$ has 
${5 \choose 2} = {5! \over 3! 2!} = {5 \cdot 4 \over 2} = 10$ members
and is
$\big\{
\{1,2\},
\{1,3\},
\{1,4\},
\{1,5\},
\{2,3\},
\{2,4\},
\{2,5\},
\{3,4\},
\{3,5\},
\{4,5\}
\big\}$
:::

# Sequence

A **sequence** or **tuple** is a value which contains zero or more other values inside it, commonly called its **elements**.
The *elements* of a *sequence* are in a specific order,
and each may appear any number of times.
The most common representation of a sequence is as its elements written in order, left to right, between parentheses.

In computing (only), it is somewhat more common to use the term "sequence" if all of the elements are taken from the same [set]
and "tuple" if they are taken from different sets.
However, this tradition is not universally observed.

The number of elements of a sequence is called the sequence's **length**.

The empty sequence can be denoted $()$, $\epsilon$, or $\varepsilon$.
Note that $\epsilon$ (Greek letter epsilon, the empty sequence) and $\in$ (the set member-of operator) are distinct symbols. 

:::example
The sequence $(2,1,0,2)$ has length 4.
It is a different  sequence than $(0,1,2,2)$.
:::

A sequence of length 2 is called a **pair**.
A sequence of length 3 is sometimes called a triple, but that term is not commonly used in computing
There are names for longer sequences too, but they are almost never used.

If two sequences have the same elements but in different order,
they are called **permutations** of one another.
The number of permutations of a sequence
if the factorial of the length of the sequence
divided by the product of the factorials of the number of copies of each value in the sequence.

:::example
The sequence $(2,1,0,2)$ has length 4.
It has ${4! \over 2! 1! 1!} = 12$ permutations:
$(0,1,2,2)$, 
$(0,2,1,2)$,
$(0,2,2,1)$,
$(1,0,2,2)$, 
$(1,2,0,2)$,
$(1,2,2,0)$,
$(2,0,1,2)$, 
$(2,0,2,1)$,
$(2,1,0,2)$,
$(2,1,2,0)$, 
$(2,2,0,1)$, and
$(2,2,1,0)$.

The sequence $\big(1,1,1,\{1\},\{1\},\{1\},\{1\},(1),(1),(1),(1),(1)\big)$
has ${12! \over 3! 4! 5!} = 27,720$ permutations.
:::

The **Cartesian product** of two sets $S \times T$ is the set of all pairs where the first element comes from $S$ and the second from $T$;
that is, $S \times T = \big\{(s,t) \;\big|\; s \in S \land t \in T\big\}$.
Cartesian product is commonly treated as a variable-arity operator,
such that $S \times T \times U$ is a set of triples
but $(S \times T) \times U$ and $S \times (T \times U)$ are both sets of pairs.

:::example
$\{1,2\} \times \{4,5,6\}$ contains $(2,4)$ but not $(4,2)$.

$\{1\} \times \{2\} \times \{3\}$ contains one triple, $(1,2,3)$.

$\big(\{1\} \times \{2\}\big) \times \{3\}$ contains one pair, $\big((1,2),3\big)$.

$\{1\} \times \big(\{2\} \times \{3\}\big)$ contains one pair, $\big(1,(2,3)\big)$.
:::

The **Cartesian power** is defined analogously to the power in mathematics: $S^k = \overbrace{S\times S\times\dots\times S}^{k\text{~}S\text{s}}$.
In other words, $S^k$ is the set of all sequences of length $k$
where all elements of each sequence in the set are members of $S$.

$|S^k| = |S|^k$

The **Kleene star** is the union of all Cartesian powers, $S^* = S^0 \cup S^1 \cup S^2 \cup \S^3 \cup dots$.
In other words, $S^*$ is the set of all sequences where all elements of each sequence in the set are members of $S$.
More formally, $S^* = \big\{x\;\big|\;\exists k \in \mathbb N \;.\; x \in S^k\big\}$.

:::example
$\{1,2\}^4$ contains $(1,1,1,1)$, $(2,2,1,1)$, and 14 other sequences.

$\{1,2\}^*$ contains $()$, $(1,1)$, $(2,2,1,1,2,1,2)$, and infinitely many other sequences.
:::

A sequence where all elements are symbols is called a **string**
and is commonly written with quotes and no commas
instead of in parentheses.

:::example
"`discrete`" = (`d`, `i`, `s`, `c`, `r`, `e`, `t`, `e`)

If $\Sigma$ is the set of all symbols,
then $\Sigma^*$ is the set of all strings.
:::

In most (but not all) contexts, a value and a sequence containing just that value are treated as being equal (i.e. $x = (x)$).
If some (but not most) contexts, a sequence of sequences is treated as being equal to a flattened version of the same sequence (e.g., $((x,y),z) = (x,y,z)$).
There is no standard way of determining which context is being used.

# Integer

The [set] of all integers is denoted $\mathbb Z$.

The [set] of all non-negative integers is denoted $\mathbb N$.

An integer $x$ is a **divisor** of an integer $y$ if and only if $y \div x$ is an integer. $y$ is said to be **divisible by** $x$.
**Factor** is a synonym for *divisor*.
Although both positive and negative integers can be divisors of both positive and negative integers, it is common to only list the positive factors.

If $x$ is a *divisor* of $y$, then $y$ is a **multiple** of $x$.

We can denote the concept "$x$ is a *divisor* of $y$" as "$x|y$", but this notation is unusual in computing because $|$ is already used for so many other concepts (e.g, for absolute values, set-builder notation, conditional probability, etc).

:::example
$2$ is a divisor of $2102$ because $2102 \div 2 = 1501$, an integer.
$5$ is not a divisor of $2102$ because $2102 \div 5 = 420.4$, which is not an integer.
$-1501$ is a divisor of $2102$ because $2102 \div -1501 = -1$, an integer.

$2102$ is a multiple of both $2$ and $-1501$.
:::

$0$ is not a divisor of any integer, not even itself.
Every other integer is a divisor of $0$.

The **trivial divisors** of any nonzero integer $x$ are $-x$, $-1$, $1$, and $x$.
An integer $x$ is **prime** if its greater than $1$ and has no non-trivial divisors.

:::example
$2102$ is not prime because it has non-trivial factors, including $2$.

$1051$ is prime because it has no non-trivial factors.

$1$ and $-1051$ also has no non-trivial factors, but neither is prime because neither is not greater than $1$.
:::

The **fundamental theorem of arithmetic** states that every positive integer $x$ has one and only one **prime factorization**, meaning a product of one or more prime numbers equaling $x$.

:::example
The prime factorization of 2102 is $2 \times 1051$
:::

A prime factorization may include the same prime number more than once; the number of times a prime number $p$ appears in the prime factorization of $x$ is called the **multiplicity** of $p$.

:::example
$1280 = 2^8 \times 5$
so in this prime factorization $2$ has multiplicity 8, $5$ has multiplicity 1, and all other primes (3, 7, 11, etc) have multiplicity 0.
:::

The **greatest common divisor** (GCD) of a set of integers is the largest integer that is a divisor of all of the integers in the set.
If the GCD of two integers is 1, then the integers are called **co-prime** or **relatively prime**.

The **least common multiple** (LCM) of a set of integer is the smallest integer that is a multiple of all integers in the set.

# Rational

Any number that can be constructed by dividing one [integer] by another is called a **rational number**.
The set of all rational numbers is denoted $\mathbb Q$.

Every rational number $q$ can be written as a unique $x \div y$,
where $y$ is a positive integer, $x$ is an integer, and $x$ and $y$ are co-prime.

:::example
$34 / -20$ is a rational number.
It can be written as $-17 \over 10$, where $-17$ and $10$ are co-prime.

$-2012 \div -1501$ is a rational number.
It can be written as $2 \over 1$, where $2$ and $1$ are co-prime.

Note that $x \over y$ and $x \div y$ and $x / y$ are all equivalent ways to write the same division operation.
:::

There are numbers that are not rational numbers, such as $\pi$.
We we occasionally used the set of **real** numbers, $\mathbb R$.

$\mathbb R \supset \mathbb Q \supset \mathbb Z \supset \mathbb N$.

The **floor** of any real number $x$, denoted $\lfloor x \rfloor$, is the largest integer that is not larger than $x$.
The **ceiling** of any real number $x$, denoted $\lceil x \rceil$, is the smallest integer that is not smaller than $x$.

:::example
$\lfloor 3\rfloor = \lfloor 3.1\rfloor = \lfloor 3.8\rfloor = 3$

$\lfloor -3.1\rfloor = \lfloor -3.8\rfloor = \lfloor -4\rfloor = -4$

$\lceil 3.1\rceil = \lceil 3.8\rceil = \lceil 4\rceil = 4$

$\lceil -3\rceil = \lceil -3.1\rceil = \lceil -3.8\rceil = -3$
:::

# Function

A **function** maps a [sequence] (or single value, which is treated as equivalent to a singleton sequence for this purpose) to a value.
It does this in a deterministic, single-valued way;
for example, if $f(2,3,4) = 11$ once, then (for that $f$) $f(2,3,4)$ only and always is 11.

Each function is defined with a **domain**, the [set] of sequences two which it may be applied; and a **co-domain**, the set of values it may result in. That function $f$ is defined with domain $D$ and co-domain $C$ can be denoted $f:D\rightarrow C$.

A function need not be defined for all values in its domain, nor be able to produce all values in its co-domain.
If a function is defined with a domain, co-domain, and formula then it is defined only for that subset of the domain where the formula produces a member of the co-domain.
The subset of the co-domain that is mapped to by at least one element of the domain is called the **range** of the function.

:::example
Consider a function $g$ defined as $g:\mathbb Z \times \mathbb Z \rightarrow \mathbb Z$ where $g(x,y) = x \div y$.
The function is defined for $g(12,2) = 6$ but is not defined for the following:

- $g(1,2)$ (because the formula would produce a value not in the co-domain)
- $g(3,0.5)$ (because the value is not in the domain)
- $g(3,0)$ (because the formula is not defined for these values)
:::

A function is called a **predicate** if its co-domain is the set $\{\top,\bot\}$, where $\top$ represents the concept "true" and $\bot$ represents the concept "false".

A **relation** can equivalently be considered as any of

- a generalization of functions that allows a single domain value to map to more than one co-domain value
- an interpretation of the meaning of a predicate
- a set of sequences

A *relation* is called **functional** if it is a function; that is, each element of the domain is related to at most one element in co-domain.

:::example
|Function-like|Predicate|Set|Functional?|
|:-|:-|:-|:-:|
|$f(x) = x^2$|$P(x,y) = (y = x^2)$|$\big\{ (x,y) \;\big|\; x^2 = y \big\}$|Yes|
|$f(x) = \pm \sqrt{x}$|$P(x,y) = (y^2 = x)$|$\big\{ (x,y) \;\big|\; x = y^2 \big\}$|No|
:::

A **binary relation** is a relation that resembles a single-argument function or two-argument predicate. Binary relations are by far the most common type of non-functional relation in computing.

Binary relations are often written as a formula defining their predicate, but with a special symbol instead of an equals sign, like $R(x,y): x < y$ or $R(x,y) \Coloneqq x<y$ for the less-than relation.
Many different symbols are used, though only one per text;
the most common are $:$, $\triangleq$, $\coloneqq$, $\Coloneqq$, and $\overset{\text{def}}{=}$.


There are a large number of vocabulary terms to know about functions and relations.

A *function* $f:D\rightarrow C$ is

- **total** if $f(x)$ is defined for all $x \in D$.
- **partial** means "either total or not total" and is used in contexts where most functions are assumed to be total to identify subcontexts where that assumption does not apply.
- **injective** or **1-to-1** if $f(x) = f(y)$ implies $x = y$.
- **surjective** or **onto** if the *co-domain* is equal to the *range*.
- **bijective**, **invertible**, or a **1-to-1 correspondence** if it is *total* and *injective* and *surjective*.

:::example
For $f : \mathbb Z \rightarrow \mathbb Z$,

- $f(x) = x + 2$ is total, injective, surjective, and bijective
- $f(x) = x \div 2$ is injective and surjective but not total
- $f(x) = x \times 2$ is total and injective but not surjective
- $f(x) = \lfloor x \div 2 \rfloor$ is total and surjective but not injective
:::

A *binary relation* $R(x,y)$ is

- **reflexive** if every $x$ is related to itself; that is, $\forall x\;.\; R(x,x)$
- **irreflexive** if no $x$ is related to itself; that is, $\forall x\;.\; \lnot R(x,x)$
- **transitive** if $\forall x,y,z\;.\; \big(R(x,y) \land R(y,z)\big) \rightarrow R(x,z)$
- **symmetric** if $\forall x,y\;.\; R(x,y) \rightarrow R(y,x)$
- **asymmetric** if $\forall x,y\;.\; R(x,y) \rightarrow \lnot R(y,x)$
- **antisymmetric** if $\forall x,y\;.\; \big((x \ne y) \land R(x,y)\big) \rightarrow \lnot R(y,x)$

Several combinations of the above properties have special names:

- an **equivalence relation** is reflexive, transitive, and symmetric
- a **partial order** is transitive and antisymmetric
    - a **strict** partial order is also irreflexive, implying it is also asymmetric
    - a **non-strict** partial order is also reflexive
    - Note (confusingly) that it is possible for a partial order to be neither strict nor non-strict
- a **total order** is a partial order such that every pair of values is either related or is related in the reverse order; that is, $\forall x,y\;.\; R(x,y) \lor R(y,x)$.
    - total orders also have strict and non-strict variants.


:::example
For $R(x,y) : \mathbb Z^2 \rightarrow \{\bot,\top\}$,

- $R(x,y) \coloneqq \big(x = y\big)$ is an equivalence relation: that is, reflexive, transitive, and symmetric
- $R(x,y) \coloneqq \big(x < y\big)$ is a strict total order: that is, irreflexive, transitive, antisymmetric, and $\forall x,y\;.\; R(x,y) \lor R(y,x)$
- $R(x,y) \coloneqq$ "$x$ is a factor of $y$" is a non-strict partial order: that is, reflexive, transitive, and antisymmetric
- $R(x,y) \coloneqq 2x = 3y$ is antisymmetric but has none of the other above properties
    - it is not reflexive because 2 is not related to 2
    - it is not irreflexive because 0 is related to 0
    - it is not transitive because $R(9,6)$ and $R(6,4)$ but not $R(9,4)$
    - it is antisymmetric because the system of equations $2x=3y$ and $2y=3x$ has only one solution: $x=y=0$
:::
