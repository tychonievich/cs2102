---
title: Set Quantifiers
...

# Quantifiers and Sets

Quantifiers are often used with sets. Set-notation quantifiers and domain-bound quantifiers can each be defined in terms of the other.
Note that one of our textbooks uses only domain-bound quantifiers and the other only set-notation quantifiers.

## Core notation

The notation "$\forall x \in S \;.\; P(x)$" means "The predicate $P(x)$ is true for every $x$ in the set $S$". It does not say anything about the truth or falsehood of $P(x)$ for $x$ not in $S$, nor does it assert that there are any members of $S$.

The notation "$\exists x \in S \;.\; P(x)$" means "There is at least one element of $S$, and at least one element of $S$ makes the predicate $P(x)$ true". It does not say anything about the truth or falsehood of $P(x)$ for $x$ not in $S$, nor if there are more (or even all) members of $S$ that also make $P(x)$ true.

The notation "$\forall x,y \in S$" is shorthand for "$\forall x \in S \;.\; \forall y \in S$".

The notation "$\exists x,y \in S$" is shorthand for "$\exists x \in S \;.\; \exists y \in S$".

## Converting "$\forall x \in S\;.\; \cdots$" to "$\forall x\;.\; \cdots$"

Re-write "$\forall x \in S \;.\; \cdots$" as "$\forall x \;.\; x \in S \rightarrow \cdots$".

If a domain is not specified and all quantifiers are given with sets, the implicit domain is union of all such sets or any superset containing that union.

## Converting "$\forall x\;.\; \cdots$" to "$\forall x \in S\;.\; \cdots$"

Define a set $U$ representing the entire domain. The symbol $U$ is not required, but is often used with the intent that it suggest the "universal set" or the "universe of discourse". In handwriting, $U$ and $\cup$ are easily confused so a different letter should be used instead.

Replace all "$\forall x \;.\; \cdots$" with "$\forall x \in U \;.\; \cdots$"



