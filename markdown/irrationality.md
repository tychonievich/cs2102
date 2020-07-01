---
title: Proofs of irrationality
...

The following are example proofs by contradiction that particular values are not part of particular sets.

# Non-integral numbers

:::theorem
${2 \over 3} \notin \mathbb Z$ 
:::

:::proof
Assume that ${2 \over 3} \in \mathbb Z$.
That means $\exists x \in \mathbb Z \;.\; x = {2 \over 3}$; i.e., $3 x = 2$.
By the fundamental theorem of arithmetic, each number has a unique prime factorization,
which means that both $3x$ and $2$ must have the same prime factors.
But $3$ is a factor of $3x$ and not a factor of $2$, which is a contradiction.

Because assume that ${2 \over 3} \in \mathbb Z$ led to a contradiction, it must be the case that ${2 \over 3} \notin \mathbb Z$.
:::

# Irrational roots

:::theorem
$\sqrt{2} \notin \mathbb Q$
:::

:::proof
Assume that $\sqrt{2} \in \mathbb Q$.
That means $\exists x,y \in \mathbb Z \;.\; {x \over y} = \sqrt{2}$ where $x$ and $y$ are relatively prime.
Rearranging, we have $x^2 = 2 y^2$.
By the fundamental theorem of arithmetic, each number has a unique prime factorization,
which means that both $x^2$ and $2 y^2$ must have the same prime factors.

Because $x$ and $y$ are relatively prime, at most one of $x$ and $y$ can have 2 in its prime factorization; we thus proceed by cases:

Case 1: 2 is a factor of $x$
:   Then $x^2$ has 2 as a factor with multiplicity $\ge 2$.
    Because 2 is not a factor of $y$, $2y^2$ has 2 as a factor with multiplicity $1$.
    But $1 < 2$, which is a contradiction.

Case 2: 2 is not a factor of $x$
:   Then $x^2$ also does not have 2 as a factor, but $2y^2$ does, which is a contradiction.

Because both cases led to a contradiction, assuming $\sqrt{2} \in \mathbb Q$ leads to a contradiction in general, which means it must be the case that $\sqrt{2} \notin \mathbb Q$.
:::

# Irrational logs

:::theorem
$\log_2(3) \notin \mathbb Q$
:::

:::proof
Assume that $\log_2(3) \in \mathbb Q$.
That means $\exists x,y \in \mathbb Z \;.\; {x \over y} = \log_2(3)$ where $x$ and $y$ are relatively prime.
Rearranging, we have $x = \log_2(3) y = \log_2(3^y)$, or $2^x = 3^y$.
By the fundamental theorem of arithmetic, each number has a unique prime factorization,
which means that both $2^x$ and $3^y$ must have the same prime factors. But all of $2^x$'s prime factors are 2s and none of $3^y$'s are, which is a contradiction.

Because assuming $\log_2(3) \in \mathbb Q$ leads to a contradiction it must be the case that $\log_2(3) \notin \mathbb Q$.
:::
