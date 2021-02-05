---
title: Sets and Sequences
...

In this class, we will deal with some atomic values: true, false, and numbers.
We will also deal with some composite values: sets and sequences.
We call them composite because they are made up of other values.

Both sets and sequences

- May contain any other value, including other sets and sequences
- Are [values, not entities](values.html)
- Are used to define other structures of interest in this course
- Are commonly written with their contained values separated by commas

However, sets and sequences differ in several important ways:

---------------------------------------------------------------
Set                             Sequence                      
------------------------------- -------------------------------
Written with curly braces,      Written with parentheses,
like $\{1,2\}$                  like $(1,2)$

Cannot contain the same value   Can contain the same value
more than once;                 any number of times;
writing $\color{darkred}        $(1,1)$ is a sequence and is
\{1,1\}$ doesn't make sense     distinct from $(1)$ and $(1,1,1)$

Members have no order;          Elements have order;
$\{2,3\} = \{3,2\}$             $(2,3) \ne (3,2)$

The number of members in a set  The number of elements in a
is called its "cardinality"     sequence is called its "length"

The empty set (the only set     The empty sequence (the only
with cardinality 0) is written  sequence with length 0) is
$\{\}$ or $\emptyset$           written $()$ or $\epsilon$
                                $\varepsilon$

Has many operators and special  Has no operators that are
notations like                  commonly used in computing
$\{1,2\} \cup \{x^2 \;|\; x \in
\mathbb N^{+}\}$

A singleton set is always       A singleton sequence is often
distinct from its member;       considered equal to its element;
$\{2\} \ne 2$                   $(2) = 2$

Always called "set"             Called "sequence" or "tuple",
                                with special words for some
                                lengths (e.g. "pair", "triple")
                                and some element types
                                (e.g. "string")

Contained values are called     Contained values are called
"members"; "element" is also    "elements"; "items" is also
sometimes used.                 sometimes used.
---------------------------------------------------------------
