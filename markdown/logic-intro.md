---
title: Logic as a Language
...

# The need for formal languages

Human languages like English are very flexible in what they can express. However, some of that flexibility comes at the cost of ambiguity.
In computer science, ambiguity is something we cannot deal with.
So we design our own languages, or borrow those of other fields, that do not admit ambiguity or that relegate it to specific places within the language.
This language-level limitation of ambiguity comes with a limitation of expressiveness.

You have already completed at least one course teaching you an unambiguous language for describing information and actions involving information: in other words, a "programming language."
Programming languages are unambiguous, but also limited in what they can say.
They describe actions to take on information, and nothing else.
Simple every-day expressions like "that was fun, but it wore me out" are completely outside their scope.

In this class, we'll teach you another language that, like programming languages, was designed to be unambiguous in describing a particular subset of things we might wish to express.
This language is older than any programming language, and is designed to express claims or assertions: statements that could be true or false but nothing in between.
Like programming languages, this language comes with a set of rules describing what its expressions mean and how you can evaluate them.

The language we will spend the most time on is called First-Order Logic.

We'll also discuss a few other languages from the broader space of Mathematics, such as set theory and discrete structures, but first-order logic will take the bulk of our time and attention.

# Values, Operators, Predicates, and Quantifiers

We'll divide our conversation between two subsets of logic: propositional logic and predicate logic.

## Propositional logic

In programming, you learned about values. `3` was a value; so was `"hi"` and `2.5`.
In logic there are only two values:
**true** (written "$\top$" or "1")
and **false** (written "$\bot$" or "0").

In programming, you learned about variables. They had names, stored values, and could change what value they stored as the program executed.
In logic, the equivalent idea is a **proposition**. A proposition has a name, which is always a single capital letter with an optional numeric subscript, and cannot change value: its either true everywhere, or it is false everywhere.
Confusingly, logic *also* has an idea called a "variable" which means something else, discussed below.

In programming, you learned about operators. `*` and `==` were operators, taking in two values and producing a new third value.
In logic we have **operators** as well. The most common are

- $\land$: $\top \land \top$ creates $\top$, any other use of $\land$ creates $\bot$
- $\lor$: $\bot \lor \bot$ creates $\bot$, any other use of $\lor$ creates $\top$
- $\rightarrow$: $\top \rightarrow \bot$ creates $\bot$, any other use of $\rightarrow$ creates $\top$
- $\lnot$: $\lnot \bot$ creates $\top$, $\lnot \top$ creates $\bot$

There are other operators too, which we'll explore during the semester.
Note that since there are only two values, we can describe each operators' behavior exhaustively by listing all of the ways it can create each of those two values.

Hopefully, the above seems familiar: programming languages almost always include most of propositional logic within its Boolean datatype and operators.
However, we'll go beyond what you did with those in programming; in particular, we'll discuss notions of equivalence and entailment:
how to identify the similarity of meaning between distinct logic expressions, and how to convert to other, more useful, expressions.

## Predicates

Formal languages are more useful if they have some way to discuss things outside their own formalism.
In programming, this is done through input and output, abstractions about how humans interact with the computer.
In logic, this is done with propositions and variables.

A predicate is an abstraction of a true/false statement *about* something external to logic itself, where the "thing" may be unknown or changeable. We take these expressions into logic by using a **predicate** to represent the statement as a whole and **variables** to represent the "things" being discussed.

:::example
The English expression "I like you" can be thought of as a true/false statement, but also has placeholders "I" and "you" which could refer to different people in different contexts.
We thus represent the statement "<u>     </u> likes <u>     </u>" as a predicate (let's use $L$ as its symbol) and variables for the blanks (let's used $x$ and $y$) to get $L(x,y)$.
:::

In general, we write a predicate as a capital letter followed by a set of variables (represented as lower-case letters) in parentheses, a notation that is intended to resemble function application notation from mathematics and computing.

A predicate is like a function or method in a programming language that accepts arguments of various types and always returns a boolean value.
In programming classes we worry about how to write such functions; this course will focus on how to reason about them without knowing the details of how they work.

:::example
Consider the expression $G(x) \land L(x,y)$.
This expression could have many meanings, depending on how we define $G$ and $L$. Some example meanings:

- $G(z)$ means "$z$ is a program in the Go language." $L(p,q)$ means "$p$ is longer than $q$". The expression means "$x$ is a Go program and is longer than $y$."
- $G(z)$ means "$z$ is a ghost." $L(p,q)$ means "$p$ loves $q$". The expression means "$x$ is a ghost that loves $y$."
:::


## First-order predicate logic

Predicates allow us to bring in some of the complexity of the real world into logic. However, before we can operate without ambiguity we need to remove that complexity again. Since variables represent the complexity, we remove the complexity by adjusting our logic so that every variable has a known meaning.

The principle way we remove dependence on the meaning of a specific variable is to **quantify** the variable.
There are two main quantifiers:

- $\forall x \;.\; P(x)$ is read "for all $x$, $P(x)$".
    It is defined to be true if $P(x)$ is true for every possible $x$, and false if there is any $x$ that makes $P(x)$ false.
    
    You can think of this as an extension of $\land$.
    $\forall x\;.\; P(x)$ means $x_1 \land x_2 \land x_3 \land \dots$ where every possible value of $x$ is represented by some $x_i$.

- $\exists x \;.\; P(x)$ is read "there exists an $x$ such that $P(x)$".
    It is defined to be true if $P(x)$ is true for at least one possible $x$, and false if there is no $x$ that makes $P(x)$ true.
    
    You can think of this as an extension of $\lor$.
    $\exists x\;.\; P(x)$ means $x_1 \lor x_2 \lor x_3 \lor \dots$ where every possible value of $x$ is represented by some $x_i$.

In rare circumstances, a variable may also be assigned to a single specific value (e.g., "by variable $x$, we always mean the number 123").

An expression is part of **first-order logic** if

- it contains predicates (and optionally also propositions) connected with operators
- every variable is **bound** (by a quantifier or assignment), and none are bound more than once

:::example
Below are various expressions, some of which are first-order logic and some of which are not, with notes as to why not if not.

| Expression | First-order? |
|:-----|:-------------|
| $P \land Q$ | Propositional, as it contains no predicates. Some sources call propositional logic a subset of predicate, others do not. |
| $P(x) \land Q(x)$ | No: has an unbound variable ($x$) |
| $\forall x\;.\; P(x)$ | Yes |
| $\forall x\;.\; P(x) \land Q(x)$ | Yes |
| $\forall x\;.\; P(x) \land Q(y)$ | No: has an unbound variable ($y$) |
| $\forall x\;.\; P(x) \land \forall x\;.\; Q(x)$ | No: $x$ is quantified twice |
| $\big(\forall x\;.\; P(x)\big) \land \big(\forall x\;.\; Q(x)\big)$ | Technically yes, because parentheses change variable bindings, but confusingly re-uses $x$; should be written as next row instead |
| $\big(\forall x\;.\; P(x)\big) \land \big(\forall y\;.\; Q(y)\big)$ | Yes |
| $\forall x\;.\; P(x) \land \forall y\;.\; Q(y)$ | Yes |
| $\forall x\;.\; \forall y\;.\; P(x) \land Q(y)$ | Yes |
| $\forall x,y\;.\; P(x) \land Q(y)$ | Yes |
| $P(x) \land \forall x,y\;.\; Q(y)$ | No; $x$ has not been quantified by the time it is used in $P(x)$ |
| $\forall x\;.\; \exists y\;.\; P(x) \land Q(y)$ | Yes |
| $\forall x\;.\; \exists y\;.\; P(x) \land Q(x)$ | No; quantifies $y$ but never uses it in a predicate |
| $\forall x\;.\; \exists Q\;.\; P(x) \land Q(x)$ | No; you can only quantify variables, not predicates |
| $\forall x\;.\; P(x) \land Q(x,x)$ | Yes |
| $\forall x\;.\; P(Q(x),R(x))$ | No; predicates can only have variables inside, not subexpressions |
:::

# The importance of order

What is the difference between the following three phrases?

> "Someone loves everyone"

> "Everyone is loved by someone"

> "Everyone loves someone"

> "There is someone that everyone loves"

To explore this, let's re-wite them in first-order logic. Let $L(x,y)$ be a predicate meaning "$x$ loves $y$".
Then the fours above are all written as $L(x,y)$ with one $\forall$ and one $\exists$:


English                                 Math
-----------------------------------     ---------------
Someone loves everyone                  $\exists x \;.\; \forall y \;.\; L(x,y)$
Everyone is loved by someone            $\forall y \;.\; \exists x \;.\; L(x,y)$
Everyone loves someone                  $\forall x \;.\; \exists y \;.\; L(x,y)$
There is someone that everyone loves    $\exists y \;.\; \forall x \;.\; L(x,y)$

Once you've fully understood this one table, you'll have made a huge step in understanding first-order logic.
First, some rules

1. The order of different quantifiers matters.
2. The binding of the left-most quantifier is fixed for all the subsequent quantifiers.
3. Inner quantifiers are re-done for each valuation of outer quantifiers.

Let's look at each of the four more closely given these rules:

- $\exists x \;.\; \forall y \;.\; L(x,y)$
    
    First up: $\exists x$.
    This means the expression is true if there is even just *one* $x$ that makes it true.
    Let's just guess that $x$ can be me: we can revisit if that was a good choice later.
    
    Next up: $\forall y$.
    This means the expression is true only if it is true for *every* possible $y$.
    So, given our pick of $x$ as me, that means that $\forall y \;.\; L(x,y)$ is only true if I love absolutely everyone.
    
    Now, sad though it is to admit, there are people I don't love, so if $x$ is me then the statement would be false.
    But the statement is "does there exist any $x$", not just "if $x$ means me",
    so I now need to check every other person there is
    looking for one who loves everyone.

- $\forall y \;.\; \exists x \;.\; L(x,y)$
    
    First up: $\forall y$.
    This means the expression is true only if it is true for *every* possible $y$.
    It need to be true if $y$ is me, and if $y$ is you, and if $y$ is Grace Hopper, and if $y$ is Skip Ellis, and ...

    Next up: $\exists x$.
    This means the expression is true if there is even just *one* $x$ that makes it true:
    as long as $y$ is loved by *someone*, the expression is true.
    
    So let's try this out.
    If $y$ is me, can I find some $x$ who loves me? Yes, my parents love me. Pick one of them as $x$ and we've shown that $y$'s OK.
    If $y$ is you, can you find some $x$ who loves you? Note that it doesn't need to be the same $x$ who loved me; *anyone* is OK. Perhaps you mother? If so, 
    
    Now, sad though it is to admit, there are people I don't love, so if $x$ is me then the statement would be false.
    But the statement is "does there exist any $x$", not just "if $x$ means me",
    so I now need to check every other person there is
    looking for one who loves everyone.
