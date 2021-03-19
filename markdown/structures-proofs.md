---
title: Proofs of theorems in Structures
...

This page contains proofs of theorems stated in [a summary of Structures](structures.html).

# Cardinality of Power Set

:::theorem
$\big|\mathcal P(S)\big|  = 2^{\big|S\big|}$
:::

:::proof
We proceed by induction on the cardinality of $S$.

Base case
:   $|S| = 0$
    
    In this case, $S = \{\}$ and $\mathcal P(S) = big\{\{\}\big\}$.
    Thus, $\big|P(S)\big| = 1 = 2^0$.

Inductive Step
:   Assume $|S| > 0$ and all sets of cardinality $|S|-1$ have $2^{|S|-1}$ elements in their powerset.
    Pick an arbitrary member $x$ of $S$ and define $T = S \setminus \{x\}$.
    
    For every member $y$ of $\mathcal P(T)$,
    we know that $\mathcal P(S)$ has two members: $y$ and $y \cup \{x\}$.
    We also know that 
    
    - those members are distinct because one contains $x$ and the other does not;
    - all members of $\mathcal P(S)$ can be generated in this way
    - no single member of $\mathcal P(S)$ is generated from two distinct $y$
    
    Thus, $\big|\mathcal P(S)\big| = 2 \big|\mathcal P(T)\big|$.
    
    Because $|T| = |S|-1$, $\big|\mathcal P(T)\big| = 2^{|S|-1}$.
    Thus, $\big|\mathcal P(S)\big| = 2${|S|}$.

By the principle of induction, the theorem holds for all sets with finite cardinality.
:::

Note that induction only covers sets with finite cardinality.
The cardinality of the powerset of infinite-cardinality sets is related to important proofs in the theory of computation showing that some finitely-expressible problems cannot be solved by any computer program,
but those proofs are beyond the scope of this class.


# Number of subsets

:::theorem
The number of distinct $k$-member subsets of a $n$-member set is denoted $\displaystyle{ n \choose k }$, read "$n$ **choose** $k$", and is equal to $\displaystyle{ n! \over (n-k)! k! }$,
where $x!$ is the [factorial](#summation) of $x$.
:::

:::proof
We use universal instantiation on $n$ and proceed by induction on $k$.

Base case $k=0$
:   There is only one empty set, so ${n \choose 0} = 1$.
    ${{n!} \over {k!}{(n-k)!}} = {{n!} \over {n!}} = 1$,
    so the formula applies here.

Inductive step
:   Assume ${n \choose k} = {{n!} \over {k!}{(n-k)!}}$ for some $k < n$.
    We consider the case of $k+1$.

    Then ${n \choose {k+1}}$ is the number of $k+1$-element subsets of an $n$-element set.
    We can construct these as follows:
    for each of the $n \choose k$ $k$-element subsets, there are $n-k$ possible additional elements we could add, giving $(n-k){n \choose k}$.
    But each such $k+1$-element set will be generated $k+1$ times: for an arbitrary ordering of its elements, it will be generated from one $k$-element set by adding the first element, from a different $k$-element set by adding the second element, and so on to the $k+1$st element.
    Thus, we actually have ${n \choose {k+1}} = \frac{n-k}{k+1}{n \choose k}$.
    
    By definition, $\frac{n-k}{k+1}{n \choose k} = \frac{n-k}{k+1} \frac{n!}{k!(n-k)!}$.
    Canceling the two $n-k$ terms gives $\frac{1}{k+1} \frac{n!}{k!(n-k-1)!}$;
    multiplying through gives $\frac{n!}{(k+1)!(n-(k+1))!}$,
    which is the definition of $n \choose {k+1}$.
    
By the principle of induction, it holds that the number of $k$-element subsets of an $n$-element set is $n \choose k$ for all integer $k$ between 0 and $n$.

By the principle of universal instantiation, it holds that the number of $k$-element subsets of an $n$-element set is $n \choose k$ for all non-negative integer $n$ and all integer $k$ between 0 and $n$.
:::



# Counting Permutations

:::theorem
The number of permutations of a sequence
is the factorial of the length of the sequence
divided by the product of the factorials of the number of copies of each value in the sequence.
:::

This is a complicated enough theorem, we'll do it in several steps.

:::lemma
The number of permutations of a sequence with $n$ distinct elements
is $n!$.
:::

:::proof
We proceed by induction on $n$.

Base case $n=0$
:   There is only one empty sequence: $()$.
    By definition, $0! = 1$.

Base case $n=1$
:   There is only one permutation of a singleton sequence,
    and $1! = \prod_{i=1}^{1} i = 1$.

Inductive step
:   Assume that a $n-1$-element sequence with distinct elements has $(n-1)!$ permutations.
    Then we construct and count all permutations of an $n$-element sequence, $s_n$, a follows:
    
    1. Consider the $(n-1)$-element sequence $s_{n-1}$ defined as all elements of $s_n$ except the last.
    2. Create the $(n-1)!$ permutations of $s_{n-1}$
    3. From each permutation of $s_{n-1}$, generate $n$ permutations of $s_n$ , where the $i$th permutation generated from $s'$ is $s'$ with the last element of $s_n$ in the $i$th spot
    
    Because all elements of $s_n$ are unique, each resulting permutation is unique.
    We generated $n$ permutations for each of $(n-1)!$ sub-permutations,
    for a total of $n \times (n-1)! = n!$ permutations.
    
By the principle of induction, it holds that the number of permutations of any sequence of $n$ distinct elements is $n!$.
:::

With that lemma, we can now proceed to prove the full theorem.
Rather than a formal proof, we provide only a proof outline:

> Given a sequence of $n$ elements, by the lemma you can permute the sequence $n!$ ways.
> But if some element appears $k$ times, permuting those $k$ elements has no impact on the sequence, suggesting we only need one of those $k!$ variants, giving $n! / k!$ distinct permutations.
> And if there other repeated elements, we'd need to divide by their permutations as well.


# Counting Cartesian Powers

:::theorem
For all finite sets $S$, $|S^k| = |S|^k$
:::

:::proof
We proceed by induction on $k$

Base case
:   $k = 0$.
    Then $S^k = \big\{()\big\}$ (regardless of what set $S$ is),
    a set with one member; and $|S|^0 = 1$.

Inductive step
:   Assume that $|S^{k-1}| = |S|^{k-1}$.
    Then we can enumerate the elements of $S^k$ as follows:
    for each element $x$ of $S^{k-1}$, create $|S|$ sequences of length $k$:
    each starts with a different element of $S$ and then is followed by the elements of $x$ in order.
    This results in $|S| |S^{k-1}| = |S|^k$ elements in total.

By the principle of induction, it follows that $|S^k| = |S|^k$ for all $k \in \mathbb N$.
:::


# Irrational Numbers

:::theorem
There are numbers that are not rational numbers
:::

:::proof
Because this is an existence theorem, it suffices to show one irrational number.
For the sake of this proof, we pick $\sqrt{2}$ as our example number
and proceed by contradiction.

Assume $\sqrt{2} \in \mathbb Q$; that is, $\exists x,y \in \mathbb Z \;.\; \sqrt{2} = {x \over y}$.
Instantiating $x$ and $y$ we have $\sqrt{2} = {x \over y}$;
squaring both sides and multiplying by the denominator gives us $2 y^2 = x^2$, where both sides are integers.

By the fundamental theorem of arithmetic, each integer has a unique prime factorization. The multiplicity of the prime factor 2 in $x$ must be an integer, so the multiplicity of prime factor 2 in $x^2$ must be even.
The multiplicity of the prime factor 2 in $y$ must be an integer, so the multiplicity of prime factor 2 in $y^2$ must be even,
meaning the multiplicity of prime factor 2 in $2 y^2$ must be odd.
But $2 y^2 = x^2$, so the multiplicity cannot be both odd and even, resulting in a contradiction.

Because assuming that $\sqrt{2} \in \mathbb Q$ led to a contradiction, it must be the case that $\sqrt{2} \notin \mathbb Q$.

Because $\sqrt{2} \notin \mathbb Q$ and $\sqrt{2}$ is a number, there are numbers that are not rational numbers.
:::

# Function properties

:::theorem
For $f : \mathbb Z \rightarrow \mathbb Z$,

- $f(x) = x + 2$ is total, injective, surjective, and bijective
- $f(x) = x \div 2$ is injective and surjective but not total
- $f(x) = x \times 2$ is total and injective but not surjective
- $f(x) = \lfloor x \div 2 \rfloor$ is total and surjective but not injective
:::

We provide only a proof outline for each claim:

- $f(x) = x + 2$
    - $f(x) = x + 2$ is total because $x+2$ is defined for all integers and always results in an integer.
    - $f(x) = x + 2$ is bijective because its inverse is a function: $f^{-1}(x) = x-2$
    - $f(x) = x + 2$ is injective and surjective because it is bijective
- $f(x) = x \div 2$
    - $f(x) = x \div 2$ is not total because $f(1) \notin \mathbb Z$.
    - $f(x) = x \div 2$ is injective and surjective because its inverse $f^{-1}(x) = 2x$ is total
        - $f^{-1}(x) = 2x$ is total because $2x$ is  defined for all integers and always results in an integer.
- $f(x) = x \times 2$
    - $f(x) = x \times 2$ is total because $2x$ is  defined for all integers and always results in an integer.
    - $f(x) = x \times 2$ is injective because $(2x \ne 2y) \leftrightarrow (x \ne y)$ (by the algebraic rule of division of 2 on both sides)
    - $f(x) = x \times 2$ is not surjective because $f^{-1}(1) \notin \mathbb Z$
- $f(x) = \lfloor x \div 2 \rfloor$
    - $f(x) = \lfloor x \div 2 \rfloor$ is total because all integers can be divided by 2 and the floor of any number is an integer
    - $f(x) = \lfloor x \div 2 \rfloor$  is surjective because $\forall y \in \mathbb Z \;.\; f(2y) = y$ and $2y \in \mathbb Z$.
    - $f(x) = \lfloor x \div 2 \rfloor$ is not injective because $f(2) = f(3)$ but $2 \ne 3$.


# Binary relation properties

:::theorem
$R(x,y) \coloneqq$ "$x$ is a factor of $y$" for $x,y \in \mathbb Z^+$ is a partial order.
:::

:::proof
A partial order is reflexive, transitive, and antisymmetric.
We prove each property independently.

Reflexive
:   Consider an arbitrary $x \in \mathbb Z^+$.
    Because $x \ne 0$, we have $x \div x = 1 \in \mathbb Z$,
    which by the definition of "factor" means that $x$ is a factor of $x$; i.e., $R(x,x)$.
    By universal instantiation it follows that $\forall x \in \mathbb Z^+ \;.\; R(x,x)$, meaning $R$ is reflexive.

Transitive
:   Consider arbitrary $x,y,z \in \mathbb Z^+$.
    Assume $R(x,y)$ and $R(y,z)$; that is, $x$ is a factor of $y$ and $y$ is a factor of $z$.
    Then $z = k y$ and $y = c x$ for some integers $c$ and $k$,
    meaning $z = k c x$; because $kc$ is also an integer, $x$ is a factor of $z$; that is, $R(x,z)$.
    Because assuming $R(x,y)$ and $R(y,z)$ allowed us to prove $R(x,z)$,
    we know that $\big(R(x,y) \land R(y,z)\big) \rightarrow R(x,z)$.
    By universal instantiation it follows that 
    $\forall x,y,z \in \mathbb Z^+ \;.\; \big(R(x,y) \land R(y,z)\big) \rightarrow R(x,z)$ meaning $R$ is transitive.

Antisymmetric
:   Consider arbitrary $x,y \in \mathbb Z^+$.
    Assume $x \ne y$ and $R(x,y)$.
    Because $R(x,y)$ and both $x$ and $y$ are positive, $y = k x$ for some positive integer $k$;
    and because $x \ne y$, $k \ne 1$, which means that $y > x$.
    That in turn means that $0 < (x \div y) < 1$, meaning $\lnot R(y,x)$.
    Because assuming $x \ne y$ and $R(x,y)$ allowed us to prove $\lnot R(y,x)$,
    we know that $\big((x \ne y) \land R(x,y)\big) \rightarrow \lnot R(y,x)$.
    By universal instantiation it follows that 
    $\forall x,y \in \mathbb Z^+ \;.\; \big((x \ne y) \land R(x,y)\big) \rightarrow \lnot R(y,x)$ meaning $R$ is antisymmetric.

Because $R$ is reflexive, transitive, and antisymmetric,
$R$ is a partial order.
:::

----

:::theorem
$R(x,y) \coloneqq 2x = 3y$ for $x,y \in \mathbb Z$ is antisymmetric
:::

:::proof
We proceed by contradiction.

Assume that $R$ is not antisymmetric; that is, $\lnot \forall x,y \in \mathbb Z \;.\;  \big((x \ne y) \land R(x,y)\big) \rightarrow \lnot R(y,x)$.
Applying De Morgan's law to the quantifier and simplifying with Boolean algebra, the assumption can be re-written as
$\exists x,y \in \mathbb Z \;.\; (x \ne y) \land R(x,y) \land R(y,x)$.

Instantiating with an unknown $x$ and $y$ from $\mathbb Z$, we have
$R(x,y) \land R(y,x)$, which by the definition of $R$ is 
$(x \ne y) \land (2x = 3y) \land (2y = 3x)$.
The system of equations $(2x = 3y)$ and $(2y = 3x)$
has $(x,y) = (0,0)$ as its only solution.
But that entails that $x = y$, which contradicts $x \ne y$.

Because assuming that $R$ is not antisymmetric entailed a contradiction, it must be that $R$ is antisymmetric
:::


<!--

# Summation

The notation $\displaystyle{ \sum_{x \in S} f(x) }$
is called **summation notation**
and means "the sum of all $f(x)$ where $x$ is an element of $S$".

:::example
Let $S = \{0,1,2,4\}$.
Then $\displaystyle{ \sum_{n\in S} 2^n = 2^0 + 2^1 + 2^2 + 2^4 = 23 }$.
:::

By definition, the sum of an empty set is 0.

The notation $\displaystyle{ \sum_{x = a}^{b} f(x) }$
is shorthand for $\displaystyle{ \sum_{x \in S} f(x) }$
where $S = \big\{ x \;\big|\; (x \in \mathbb Z) \land (x \ge a) \land (x \le b) \big\}$.

:::example
$\displaystyle{ \sum_{n=0}^{3} 2^n = 2^0 + 2^1 + 2^2 + 2^3 = 15 }$

$\displaystyle{ \sum_{n=3}^{0} 2^n = 0 }$ because there are no integers $x$ such that both $x\ge 3$ and $x \le 0$.
:::

The notation $\displaystyle{ \prod_{x \in S} }$ and $\displaystyle{ \prod_{x=a}^{b} }$ are defined similarly but as products, not sums, of their elements.
The product of an empty set is defined to be 1.

$n!$ is called the **factorial** of $n$ and is defined to be
$\displaystyle{ \prod_{x=1}^{n} x }$.
Thus, $0! = 1$ because it is the product of an empty set.

# Logarithm

*note: logarithms are not technically part of _discrete_ mathematics, being instead a topic within continuous mathematics. However, they are widely used in computing and not universally understood by entering students, so we'll cover them in this course.*

The logarithm is a family of functions that are the inverses of exponentiation.
It is defined by the following identity:
$$\big(x^y = z\big) \equiv \big(\log_x(z) = y\big)$$
The expression $\log_x(y)$ is read "the log base $x$ of $y$".

Logarithms are defined for all positive bases except 0,
though we almost always assume the base is greater than 1.

For any given base $b > 1$,

- $\log_b : \mathbb R^+ \rightarrow \mathbb R$ is bijective
- $\log_b$ is monotonically increasing; that is $(x > y) \equiv \big(\log_b(x) > \log_b(y)\big)$
    - (note if $0 < b < 1$, $\log_b$ is monotonically decreasing instead)
- $\displaystyle{ \log_b(b^x) = x }$
- $\displaystyle{ b^{\log_b(x)} = x }$
- $\displaystyle{ \log_b(x y) = \log_b(x) + \log_b(y) }$
- $\displaystyle{ \log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y) }$
- $\displaystyle{ \log_b(x^y) = y \log_b(x) }$
- $\displaystyle{ \log_b(x) = \frac{\log_a(x)}{\log_a(b)} }$
- $\displaystyle{ \log_{a^c}(x) = c^{-1}\log_a(x) }$

Logarithms have many other interesting properties and show up in many areas of computing; the above identities will be sufficient for this class.

-->
