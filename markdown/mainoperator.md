---
title: Operator Precedence
...

# Happens First *vs.* Main Operator

Consider the arithmetic expression $1 + 2 \times 3 \div -(4 + 5) - 6$.
When you were learning arithemtic, you were taught a rule for deciding which operation to do first.
That's a usable approach, but for more complicated mathematics (like logic) we'll prefer a different concept: main operators.

The **main operator** in an expression is the operator such that then entire expression can be described as that operator acting on subexpression operands.
If we correctly identified the main operator then we can put everything before it in parentheses, everything after it in parentheses, and not change the meaning of the expression.
Often, main operators are most easily found by fully parenthesizing the expression.

:::example
What is the *main operator* in $1 + 2 \times 3 \div -(4 + 5) - 6$?

1. Fully parenthesize as $\Big(1 + \big((2 \times 3) \div -(4 + 5)\big)\Big) - 6$?
2. The operator not in any parentheses is the last $-$, so that's the main operator
:::

The main operator can be thought of as "the thing you do last"
or as "a safe place to divide the problem into smaller problems".

# Main operators in first-order logic

Formal logic does not generally define a full order of operations for binary operators^[A *binary operator* is one with two operands, like $\times$ or $\lor$ or `/`. A *unary operator* has just one operand, like $\lnot$ or `!` or $-$ (when $-$ is used for negation instead of subtraction).].
Does $\lor$ or $\land$ happen first? Logicians have decided the question does not need to be asked: just add parentheses so it goes away.
However, when operators are associative, parentheses are unnecessary.

Thus "$P \land Q \lor W$" is invalid notation: it needs to be written as either "$(P \land Q) \lor W$" or "$P \land (Q \lor W)$".
However, "$P \land Q \land W$" is valid notation because $\land$ is associative.

:::aside
Programming languages have parallels to many logical operators and *do* have operator precedence for them, so sometimes when logic is written by computer scientists they omit a few required parentheses and assume programming precedence rules apply. We won't do this kind of omission in this class.
:::

Formal logic *does* have defined precedence for unary operators.

- $\lnot$ applies to the next thing only.
    For example, "$\lnot P \land Q$" means "$(\lnot P) \land Q$",
    not "$\lnot(P \land Q)$"

- "$\forall x \;.$" and "$\exists x\;.$" apply to everything that follows (but can't escape from parentheses).
    For example, "$\forall x \;.\; P \land Q$" means "$\forall x \;.\; (P \land Q)$", not "$(\forall x \;.\; P) \land Q$"
    
:::aside
There exists an alternative notation where quantifiers are followed by a "$($" instead of a "$.$" and have the same precedence as a function application. This notation is used in the $\forall x$ textbook (explained in chapter 23) but it is uncommon in computing so we'll not use it in this class.
:::

Thus, the main operator for a first-order logic expression is 

- Outside of any parentheses; if there are several
- The left-most quantifier if there is one; otherwise
- The binary operator (if there are several, they must be associative so pick any); otherwise
- The left-most logical negation

# Main operators and English

Identifying main operators is a useful way to convert between logic and English.

Logic           English
------          -----------------
$\forall$       A statement about all instances of something
$\exists$       A statement about the ability to find something
$\land$         A statement of two parts, asserting both are true
$\lor$          A statement of two parts, asserting at least one is true
$\rightarrow$   An if-then statement
...             ...


:::example
Convert "the best program is never the cheapest program" to logic

1. This is a statement about all programs.
    Hence, we have $\forall p$.
    
    We re-word what's left to be about a specific program $p$:
    "if $p$'s the cheapest, then $p$ is not the best"

2. This is an if-then statement.
    Hence, we have $\forall p\;.\; (\dots) \rightarrow (\dots)$
    
    The antecedent is "$p$ is the cheapest program".
    
    a. This is about the absence of something (nothing is cheaper than $p$).
        Hence, we have $\nexists c$.
        
        We re-word what's left (the thing that no $c$ can make true if "$p$ is cheapest) to be about a specific second program $c$:
        "$c$ is cheaper than $p$"
    b. This is about cost. Which is not part of logic. So we turn it into a predicate:
        
        Predicate   Meaning
        ----------  --------
        $C(x,y)$    $x$ is cheaper than $y$
        
        Hence, we have $\nexists c \;.\; C(c,p)$.
    
    The consequent is "$p$ is the best program".
    
    a. This is about the absence of something (nothing is better than $p$).
        Hence, we have $\nexists b$.
        
        We re-word what's left (the thing that no $b$ can make true if "$p$ is best) to be about a specific second program $b$:
        "$b$ is better than $p$"
    b. This is about goodness. Which is not part of logic. So we turn it into a predicate:

        Predicate   Meaning
        ----------  --------
        $B(x,y)$    $x$ is better than $y$
        
        Hence, we have $\nexists b \;.\; B(b,p)$.

3. Putting it all together:

    Predicate   Meaning
    ----------  --------
    $C(x,y)$    $x$ is cheaper than $y$
    $B(x,y)$    $x$ is better than $y$

    $\forall p\;.\; \big(\nexists c \;.\; C(c,p)\big) \rightarrow \big(\nexists b \;.\; B(b,p)\big)$
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
    so we have "Every $p$ ..."
    
    The remaining logic is $P(p) \rightarrow \Big(\exists i \;.\; I(i,p) \land\big(\forall j \;.\; I(j,p) \rightarrow Q(p,i,j)\big)\Big)$

1. The main operator is $\rightarrow$
    so we have "Every $p$, if ... then ..."
    
    The antecedent is $P(p)$, which is just "$p$ is a program";
    that means we have "Every $p$, if $p$ is a program then ..."
    We can simplify that English:
    "Every program $p$ ..."
    
    The consequent is $\Big(\exists i \;.\; I(i,p) \land\big(\forall j \;.\; I(j,p) \rightarrow Q(p,i,j)\big)\Big)$
    
1. The main operator is $\exists i$,
    so we have "For every program $p$, there is some $i$ ..."
    
    The remaining logic is $I(i,p) \land\big(\forall j \;.\; I(j,p) \rightarrow Q(p,i,j)\big)$
    
1. The main operator is $\land$,
    so we have "For every program $p$, there is some $i$ such that both ... and ..."
    
    The first conjunct is $I(i,p)$, which is just "$i$ is an input to $p$";
    that means we have "For every program $p$, there is some $i$ such that both $i$ is an input to $p$ and ..."
    We can simplify that English:
    "Every program $p$ has some input $i$ such that ..."
    
    The second conjunct is $\big(\forall j \;.\; I(j,p) \rightarrow Q(p,i,j)\big)$
    
1. The main operator is $\forall j$,
    so we have "Every program $p$ has some input $i$ such that for every $j$ ..."

    The remaining logic is $I(j,p) \rightarrow Q(p,i,j)$

1. The main operator is $\rightarrow$
    so we have "Every program $p$ has some input $i$ such that for every $j$ if ... then ..."
    
    The antecedent is $I(j,p)$, which is just "$j$ is an input to $p$";
    that means we have "Every program $p$ has some input $i$ such that for every $j$ if $j$ is an input to $p$ then ..."
    We can simplify that English:
    "Every program $p$ has some input $i$ such that for every input $j$ to $p$ ..."
    
    The consequent is $Q(p,i,j)$, which is "program $p$ solves input $i$ as part of working on input $j$";
    that means we have "Every program $p$ has some input $i$ such that for every input $j$ to $p$ solves input $i$ as part of working on input $j$."

1. We have a full English sentence: "Every program $p$ has some input $i$ such that for every input $j$ to $p$ solves input $i$ as part of working on input $j$."
    But we'd rather not use variable in English.
    
    The variable $p$ is the only program, so we can replace it with "the program" or the like:
    "Every program has some input $i$ such that for every input $j$ to the program solves input $i$ as part of working on input $j$."
    
    Since $i$ and $j$ are both inputs, the simple "the input" approach will not work, meaning we need more creativity in removing them from the phrase.
    A few examples:
    
    - Every program has an input that it solves along the way to solving every input.
    - For any program you care to pick, its has some "base" input: an input whose solution is part of every other inputs' solution.
    - Every program has an input it solves during the solution of every other input
:::
