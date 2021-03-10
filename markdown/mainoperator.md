---
title: English ←main–operator→ Logic
...

In any expression system with more than one operator, there is a need to clarify the meaning of a multi-operator system. For example, is $2-3+4$ equal to $3$ ($2-3$ plus $4$) or $-5$ ($2$ minus $3+4$)?

In arithmetic, an order of operations is sufficient to clarify meaning. However, as more complicated structures appear it no longer suffices. For example, in the code

<table><thead><tr><th>Java</th></th>Python</th></tr></thead>
<tbody><tr><td><pre>for(int x : numbers) {
    sum += x;
}</pre></td><td><pre>for x in numbers:
    sum += x</pre></td></tr></tbody></table>

which operator happens first: `+=` or `for`? The answer is neither: they work together iteratively.

A versatile tool for understanding expressions, even complicated ones with components like loops, is the notion of a **main operator**.
Any expression with an operator in it can be expressed as a single main operator with smaller expressions as its operands.

# Scope and main operators

Every operator has some **scope**: a portion of the expression that it directly modifies.
Logic has operators with three different ways of determining scope.

Binary operators
:   These have two operands, which comprise the operators scope.
    Examples include $\land$, $\lor$, $\rightarrow$, $\oplus$, etc.
    
    Logic does not define an order of operations for binary operators: $P \land Q \lor R$ is invalid notation; you must write either $(P \land Q) \lor R$ or $P \land (Q \lor R)$.
    The only time parentheses can be omitted is when the operators are associative^[
        Some associative operator sequences are non-intuitive; for example, $P \rightarrow (Q \lor R)$ and $(P \rightarrow Q) \lor R$ are equivalent
        and hence can be written as $P \rightarrow Q \lor R$.
        You don't need to knwo this, though, as it is always permitted to include parentheses even with associative operators.
    ], as for example in $P \oplus Q \oplus R$.

    {.aside...}
    Programming languages have parallels to many logical operators and *do* have operator precedence for them, so sometimes when logic is written by computer scientists they omit a few required parentheses and assume programming precedence rules apply. We won't use that kind of omission in this class.
    {/}

Not
:   The scope of $\lnot$ is the term that immediately follows it.
    Thus $\lnot A \lor B$ means $(\lnot A) \lor B$, not $\lnot (A \lor B)$.

Quantifiers
:   The scope of a q quantifier is the entire expression that follows its terminating dot, though its scope cannot escape from parentheses.
    Thus, $\forall x \;.\; A \land B$ means $\forall x \;.\; (A \land B)$ not $(\forall x \;.\; A) \land B$.

    {.aside ...}
    There are actually two competing notations for quantifiers.
    [MCS](files/mcs.pdf) and most other computing texts use a dot after the quantifier and the "from here until the end" scope, as described above.
    [∀x](files/forallx.pdf) and some other formal logic texts write the quantifier like a function instead, following it with parentheses that define its scope.

    We only use the dot-notation quantifiers in this class.
    {/}

The main operator of any expression is the operator whose scope is the entire expression.

# Logic to English with main operators

When turning logic into English, the following process will always work:

1. Identify the main operator
2. Write the English for that operator, with place-holders for the operands
3. Convert each operand to English using this process
4. Simplify the resulting English, removing variables if possible.

Logic                   Example English template
------------------      ---------------------------------
$\lnot x$               it is not the case that $x$
$x \land y$             both $x$ and $y$
$x \lor y$              either $x$ or $y$ or both
$x \oplus y$            either $x$ or $y$ but not both
$x \rightarrow y$       if $x$ then $y$
$x \leftrightarrow y$   $y$ if and only if $x$
$\forall x \;.\; y$     for each $x$ it is the case that $y$
$\exists x \;.\; y$     there exists some $x$ such that $y$
$\nexists x \;.\; y$    there is no $x$ such that $y$

:::exercise
Identify the main operators in each of the following:

- $(A \land B) \lor (C \land D)$ ^[$\lor$]
- $(A \rightarrow B) \land (C \lor D)$ ^[$\land$]
- $\big((A \land B) \lor (C \land D)\big)$ ^[$\lor$]
- $(A \land B) \lor \lnot(C \land D)$ ^[$\lor$]
- $\lnot(A \land B) \lor \lnot(C \land D)$ ^[$\lor$]
- $\lnot\big((A \land B) \lor (C \land D)\big)$ ^[first $\lnot$]
- $\lnot A \rightarrow B$ ^[$\rightarrow$]
- $\lnot (A \rightarrow B)$ ^[$\lnot$]
- $\forall x \;.\; \lnot A(x) \rightarrow B(x)$ ^[$\forall x$]
- $\lnot \forall x \;.\; A(x) \rightarrow B(x)$ ^[$\lnot$]
- $\exists x \;.\; \lnot A(x) \rightarrow B(x)$ ^[$\exists x$]
- $\lnot \exists x \;.\; A(x) \rightarrow B(x)$ ^[$\lnot$]
- $\nexists x \;.\; A(x) \rightarrow B(x)$ ^[$\nexists x$]
- $\forall x \;.\; \exists y \;.\; \lnot A(x) \rightarrow B(y)$ ^[$\forall x$]
- $\exists y \;.\; \forall x \;.\; \lnot A(x) \rightarrow B(y)$ ^[$\exists y$]
:::



:::example
Convert the following to simple clear English

Predicate   Meaning
----------  --------
$P(x)$      $x$ is a program
$I(x,p)$    $x$ is an input to program $p$
$Q(p,x,y)$  program $p$ solves input $x$ as part of working on input $y$

$\forall p \;.\; P(p) \rightarrow\Big(\exists i \;.\; I(i,p) \land\big(\forall j \;.\; I(j,p) \rightarrow Q(p,i,j)\big)\Big)$

1. The main operator is $\forall p$,
    
    "For each $p$ it is the case that ..."
    
    The remaining logic is $P(p) \rightarrow \Big(\exists i \;.\; I(i,p) \land\big(\forall j \;.\; I(j,p) \rightarrow Q(p,i,j)\big)\Big)$

1. The main operator is $\rightarrow$
    
    "For each $p$ it is the case that if ... then ..."
    
    The antecedent is $P(p)$, which is just "$p$ is a program"
    
    "For each $p$ it is the case that if $p$ is a program then ..."

    We can simplify that English:

    "For each program $p$ it is the case that ..."
    
    The consequent is $\Big(\exists i \;.\; I(i,p) \land\big(\forall j \;.\; I(j,p) \rightarrow Q(p,i,j)\big)\Big)$
    
1. The main operator is $\exists i$,

    "For each program $p$ it is the case that there exists some $i$ such that ..."

    We can simplify that English:

    "For each program $p$ there exists some $i$ such that ..."

    The remaining logic is $I(i,p) \land\big(\forall j \;.\; I(j,p) \rightarrow Q(p,i,j)\big)$
    
1. The main operator is $\land$,

    "For each program $p$ there exists some $i$ such that both ... and ..."

    The first conjunct is $I(i,p)$, which is just "$i$ is an input to $p$"
    
    "For each program $p$ there exists some $i$ such that both $i$ is an input to $p$ and ..."

    We can simplify that English:

    "For each program $p$ has some input $i$ such that ..."

    The second conjunct is $\big(\forall j \;.\; I(j,p) \rightarrow Q(p,i,j)\big)$
    
1. The main operator is $\forall j$,

    "For each program $p$ has some input $i$ such that for each $j$ it is the case that ..."

    The remaining logic is $I(j,p) \rightarrow Q(p,i,j)$

1. The main operator is $\rightarrow$

    "For each program $p$ has some input $i$ such that for each $j$ it is the case that if ... then ..."

    The antecedent is $I(j,p)$, which is just "$j$ is an input to $p$";

    "For each program $p$ has some input $i$ such that for each $j$ it is the case that if $j$ is an input to $p$ then ..."

    We can simplify that English:

    "For each program $p$ has some input $i$ such that for each input $j$ it is the case that ..."

    The consequent is $Q(p,i,j)$, which is "program $p$ solves input $i$ as part of working on input $j$";

    "For each program $p$ has some input $i$ such that for each input $j$ it is the case that program $p$ solves input $i$ as part of working on input $j$."

    We can simplify that English:

    "For each program $p$ has some input $i$ such that for each input $j$ program $p$ solves input $i$ as part of working on input $j$."

1. We have a full English sentence: "For each program $p$ has some input $i$ such that for each input $j$ program $p$ solves input $i$ as part of working on input $j$."
    But we'd rather not use variable in English.
    
    The variable $p$ is the only program, so we can replace it with "the program" or the like:
    "Every program has some input $i$ such that for every input $j$, the program solves $i$ as part of working on $j$."
    
    Since $i$ and $j$ are both inputs, the simple "the input" approach will not work, meaning we need more creativity in removing them from the phrase.
    A few examples:
    
    - Every program has an input that it solves along the way to solving every input.
    - For any program you care to pick, its has some "base" input: an input whose solution is part of every other inputs' solution.
    - Every program has an input it solves during the solution of every other input.
:::

# English to logic with main operators

When turning English, the following process will always work:

1. Identify the main operator implied by the English
2. Write that operator as a symbol with its scope in parentheses
3. Re-word the English to fit in the parentheses
4. Convert each parenthesized English to logic

When doing this, be sure to look for implicit quantifiers.
$\forall$ is often omitted by making a "general statement" instead,
which $\exists$ may be as subtle as the user of "a" instead of "the".

Also be careful about adding $\exists$ and if-then statements.
"I'll marry someone who proposes" means "$\exists x$ . I'll marry $x$ **and** $x$ proposes" not "$\exists x$ . I'll marry $x$ **if** $x$ proposes"; the latter is trivially true as long as there is someone somewhere who will never propose.

:::exercise
Identify the main operator of each of the following and re-write the sentence to use that operator as a symbol.

- I'll buy it if it works ^[(it works) $rightarrow$ (I'll buy it)]
- I'll buy anything that works ^[$\forall x$ . (I'll buy $x$ if $x$ works)]
- I'll buy something that works ^[$\exists x$ . (I'll buy $x$ and $x$ works)]
- I'll buy one that works ^[$\exists x$ . (I'll buy $x$ and $x$ works)]
- If a program passes all tests, it's ready for release ^[$\forall p$ . (if $p$ passes all tests then $p$ is ready for release]
- If a program passes all tests, you are missing some tests ^[(a program passes all tests) $\rightarrow$ (you are missing some tests)]
- Every good program passes at least one test ^[$\forall p$ . (if $p$ is good then $p$ passes at least one test)]
- There's a test that every good program passes ^[$\exists t$ . (every good program passes $t$)]
- You'll need an IDE or debugger to solve this ^[(You'll need an IDE to solve this) $\lor$ (You'll need a debugger to solve this)]
- A floating-point value is either normalized, denormalized, infinite, or NaN ^[$\forall n$ . (if $n$ is a floating-point value then $n$ is either normalized, denormalized, infinite, or NaN)]
- This variable is either normalized, denormalized, infinite, or NaN ^[(this variable is normalized) $\oplus$ (this variable is denormalized) $\oplus$ (this variable is infinite) $\oplus$ (this variable is NaN)]
- A floating-point value is a number ^[$\forall n$ . (if $n$ is a floating-point value then $n$ is a number)]
- A floating-point value is missing ^[$\exists n$ . (if $n$ is a floating-point value and $n$ is missing)]
- Using a floating-point value is a mistake ^[(using a float-point value) $\rightarrow$ (a mistake)]
:::



:::example
Convert "the best program is never the cheapest program" to logic

1. This is a statement about all programs.

    $\forall p\;.$ if $p$'s the cheapest, then $p$ is not the best
    
2. This is an if-then statement.

    $\forall p\;.$ ($p$'s the cheapest) $\rightarrow$ ($p$ is not the best)

    The antecedent is "$p$ is the cheapest program".
    
    a. This is about the absence of something (nothing is cheaper than $p$).
        
        $\nexists c\;.$ $c$ is cheaper than $p$
        
    b. This is about cost. Which is not part of logic. So we turn it into a predicate:
        
        Predicate   Meaning
        ----------  --------
        $C(x,y)$    $x$ is cheaper than $y$
        
        $\nexists c \;.\; C(c,p)$.
        
    The consequent is "$p$ is not the best program".
    
    a. This is about the existence of something (something is better than $p$).
        
        $\exists b\;.$ $b$ is better than $p$

    b. This is about goodness. Which is not part of logic. So we turn it into a predicate:

        Predicate   Meaning
        ----------  --------
        $B(x,y)$    $x$ is better than $y$
        
        $\exists b \;.\; B(b,p)$.

3. Putting it all together:

    Predicate   Meaning
    ----------  --------
    $C(x,y)$    $x$ is cheaper than $y$
    $B(x,y)$    $x$ is better than $y$

    $\forall p\;.\; \big(\nexists c \;.\; C(c,p)\big) \rightarrow \big(\exists b \;.\; B(b,p)\big)$
:::


:::example
Convert "the best program is never the cheapest program" to logic

1. This is a statement about all programs.

    $\forall p\;.$ "$p$'s the best" and "$p$ is not the cheapest" are never both true
    
2. This is an not-and statement.

    $\forall p\;.\; \lnot\big(p$'s the best $\land$ $p$ is the cheapest$\big)$

    The first conjunct is "$p$ is the best program".
    
    a. This is about the absence of something (nothing is better than $p$).
        
        $\nexists b\;.$ $b$ is better than $p$
        
    b. This is about goodness. Which is not part of logic. So we turn it into a predicate:
        
        Predicate   Meaning
        ----------  --------
        $B(x,y)$    $x$ is better than $y$
        
        $\nexists b \;.\; B(b,p)$.
        
    The second conjunct is "$p$ is cheapest program".
    
    a. This is about the absence of something (nothing is cheaper than $p$).
        
        $\nexists c\;.$ $c$ is cheaper than $p$
        
    b. This is about cost. Which is not part of logic. So we turn it into a predicate:
        
        Predicate   Meaning
        ----------  --------
        $C(x,y)$    $x$ is cheaper than $y$
        
        $\nexists c \;.\; C(c,p)$.

3. Putting it all together:

    Predicate   Meaning
    ----------  --------
    $C(x,y)$    $x$ is cheaper than $y$
    $B(x,y)$    $x$ is better than $y$

    $\forall p\;.\; \lnot\Big(\big(\nexists b\;.\; B(b,p)\big) \land \big(\nexists c\;.\; C(c,p)\big)\Big)$

4. We could optionally apply De Morgan and double negation:

    $\forall p\;.\; \lnot\big(\nexists b\;.\; B(b,p)\big) \lor \lnot\big(\nexists c\;.\; C(c,p)\big)$

    $\forall p\;.\; \big(\exists b\;.\; B(b,p)\big) \lor \big(\exists c\;.\; C(c,p)\big)$
    
    to get "every program either has another better than it or another cheaper than it", which is also equivalent to our starting statement.
:::


