---
title: Why first-order logic?
...

Our goal in this writeup is to explain how first-order logic provides the necessary components to express useful claims about programs. We'll primarily work with the claim

> One of these apps passes every test

Our final representation will be

> $\exists a \in A \;.\; \forall t \in T \;.\; P(a,t)$

# Abstracting away details

When expressing claims in logic, we only include the logical components, not the domain-specific parts. This is something you've seen many times in other branches of mathematics: when discussing five apples we encode just "5", abstracting away the idea of an apple. While we might do some of that kind of discarding of data in logic, more often we'll use predicates and variables to preserve some of the abstracted-away pieces' structure.

We use **variables** to represent something outside of the scope of logic but important to the truth of our claim. We'll usually use variables to discuss several possible values at once, which makes them more like the idea of "random variable" from statistics than like the idea of variables in programming (which have one value at a time but can change value as the program runs) or variables in algebra (which have one unchanging value).
For our example claim

> One of these apps passes every test

we'll use variables any time we need to refer to "apps" or "tests" because apps and tests are not themselves concepts from logic, but they are important to the truth of the claim..

We use **predicates** to represent a claim about some variables which could be true or false, but the truth of falseness of which would need to be evaluated using something outside the scope of logic. We generally try to make predicates **atomic**, meaning we could not rewrite them using some logic and other simpler predicates.
For our example claim

> One of these apps passes every test

we'll use a predicate for the idea of "this app passes this test".

We write predicates as if they were function calls. There are several important things to understand about predicates as functions:

1. The predicate function always returns a boolean value, either true or false.
2. The predicate function can only take variables as arguments, never more complicated expressions.
3. Predicate names are always upper-case letters, optionally with a numeric subscript: $P$, $Q_23$, etc.
4. Variable names are always lower-case letters, optionally with a numeric subscript: $x$, $y_23$, etc.

We could thus define our example predicate as

> $P(a,t)$: $a$ passes $t$

The colon and subsequent text about is a common way to express the meaning of a predicate, but its syntax is not itself important to logic. We could equivalently have said

> Predicate     Meaning
> ----------    -------------------
> $P(x,y)$      $x$ passes $y$

or

> We define a two-argument predicate $P$ to be true if its first argument passes its second argument

etc.

# Types = predicates = sets

## Types = predicates

Our example claim

> One of these apps passes every test

includes the "passes" predicate, but it also makes assertions about datatypes: apps and tests.
Logic only uses two types: Booleans (true and false) and other (could be anything). We add the idea of datatypes with single-argument predicates of the form "$x$ is a member of this datatype." Let's add two such predicates to the one we already have so we can model the two datatypes this claim discusses:

Predicate     Meaning
----------    -------------------
$P(x,y)$      $x$ passes $y$
$A(x)$        $x$ is an app
$T(x)$        $x$ is a test

With these predicates we can fully encode "this app passes this test":

> $A(x) \land T(y) \land P(x,y)$

A straightforward symbol-to-English translation of the above would be

> $x$ is an app and $y$ is a test and $x$ passes $y$

That differs from "this app passes this test" in that it does not leave any cases undefined, even if not given an app and a test. Let's look at a few examples:

$x$         $y$         $A(x) \land T(y) \land P(x,y)$
----------- ----------- -----------------------------------
an app      a test      $\top \land \top \land P(x,y) \equiv P(x,y)$
a fast car  a slow car  $\bot \land \bot \land \top \equiv \bot$
a student   the final   $\bot \land \top \land P(x,y) \equiv \bot$
an app      an app      $\top \land \bot \land P(x,y) \equiv \bot$

In other words, we set up our logic so that it is false unless it is given the datatypes we want.

## Types = sets

The previous section showed how we can represent a datatype by a predicate that checks if a value is a member of that datatype.
That can be useful, but it is more common to want to represent a datatype as the set of all possible values that have that datatype.
For example, I might define the Boolean datatype as $B = \{\top,\bot\}$.

Sets and single-argument predicates can be converted to one another automatically.

- Predicate $Q(x)$ can be defined as "$x$ is a member of set $Q$", which is usually written as $x \in Q$ where $\in$ is the "membership operator" or "element-of operator".
- Set $Q$ can be defined as "the set of all $x$ that make predicate $Q(x)$ true", which is usually written as $\{x \;|\; Q(x)\}$, a notation called "set-builder notation"

Because of this, we could re-write "this app passes this test" as

> $x \in A \land y \in T \land P(x,y)$

where

----------    -------------------
$P(x,y)$      $x$ passes $y$
$A$           the set of all apps
$T$           the set of all tests
----------    -------------------

# Binding variables

In a logical expression, each variable is considered either **bound** or **unbound**.
To be a fully defined claim, every variable must be bound.
In rare instances a variable may be bound to a single value (e.g. "by $x$ I mean 123.4"),
but more commonly we bind variables using quantifiers.

First-order logic (which is what we're learning in this class) has two main quantifiers:

------------------------------------------------------------------------
Idea        $\forall x \;.\; P(x)$          $\exists x \;.\; P(x)$
----------- --------------------------      ----------------------------
Read as     For all $x$, $P(x)$             There exists an $x$ such 
                                            that $gamma$
    
True iff    $P(x)$ is always true           There's at least one $x$
            regardless of $x$'s value       that makes $P(x)$ true
    
Ellipsis    $P(x_1) \land P(x_2) \land$     $P(x_1) \lor P(x_2) \lor$
            \dots                           \dots
    
Negation    $\lnot \forall x$               $\nexists x$

Equivalent  $\nexists x \;.\; \lnot P(x)$   $\lnot \forall x\;.\; \lnot P(x)$
to
------------------------------------------------------------------------

These are the two kinds of quantification first-order logic uses:
"true of everything" and "true of at least one thing."

Let's go back to our example claim

> One of these apps passes every test

and our incomplete logical expression

> $A(x) \land T(y) \land P(x,y)$

The logic is incomplete because it has unbound variables, so lets bind them with quantifiers.
Before we do that, though, we have an ambiguity to resolve:
does "one of these apps" mean "exactly one of these apps" or "at least one of these apps"?
If I find that two of the apps pass every test, was the claim true or false?
Unfortunately, English grammar does not fully answer that question.
Let's pick one (we'll look at the other later):

> At least one of these apps passes every test

Because "at least one" is written $\exists$ and the variable for apps is $x$, we have $\exists x$.
Because "every" is written $\forall$ and $y$ is the variable for tests, we have $\forall y$.
Because quantifiers have to precede the predicates that use their quantified variables that means we have one of the following:

> $\forall y \;.\; T(y) \rightarrow \exists x \;.\; A(x) \land P(x,y)$

> $\exists x \;.\; A(x) \land \forall y \;.\; T(y) \rightarrow P(x,y)$

Note the change of "$\land$" into "$\rightarrow$" for $y$ but not $x$. This is because

- "There is a $P$ that is $Q$" means the same thing as "there is something that is both $P$ **and** $Q$."
- "Every $P$ is $Q$" means the same thing as "for everything, **if** it is $P$ **then** it is also $Q$."

Converting this to set notation, we have

> $\forall y \;.\; y \in T \rightarrow \exists x \;.\; x \in A \land P(x,y)$

> $\exists x \;.\; x \in A \land \forall y \;.\; y \in T \rightarrow P(x,y)$

As a common shorthand, we can

- replace "$\forall q \;.\; q \in Q \rightarrow$" with "$\forall q \in Q \;.$
- replace "$\exists q \;.\; q \in Q \land$" with "$\exists q \in Q \;.$

to get the two options

> $\forall y \in T \;.\; \exists x \in A \;.\; P(x,y)$

> $\exists x \in A \;.\; \forall y \in T \;.\; P(x,y)$

Only one of these is a correct representation of "at least one of these apps passes every test"; to decide which one, we'll need to consider the meaning of the order of quantifiers.

## Order of quantifiers

The order of quantifiers is very important.
Even in English, the ideas "every test", "at least one app", and "app passes test" can be combined in two very different ways:

> At least one of these apps passes all tests

> Each test is passed by at least one of these apps

Both of the above have $\forall$ on the tests and $\exists$ on the apps.
But the first is only true if there is one single app that passes all tests,
while the second can be satisfied if each test is passed by a different app.

Some other examples:

- "Each nation has a government" (a possibly true statement today, depending on how loose your definition of government is) vs "there's a government over all nations" (you could maybe argue that the UN satisfies this, but it would be a hard argument to win)
- "Each student will get a grade" (true if no one drops) vs "There's a grade all students will get" (only true if all students end up with the same grade)
- "There's someone in every building" is ambiguous; do it mean "each building is occupied by at least one person" or "there's one person that is in all the buildings at once"?

Unfortunately, English is not consistent in how it separates these two kinds of meaning: is uses a mixture of word choice (all/each/every/any/some/one/a/the), word order, connecting words, and context. We need a simpler rule for logic so we don't have ambiguity, and the rule is this:

> The entire expression with a quantified variable is evaluated independently for each value that variable could take on.

Consider $\forall y \in T \;.\; \exists x \in A \;.\; P(x,y)$ with this rule. This expression starts with $\forall y \in T$ so we need to consider each test, and something needs to be true of every single one. What is that thing that needs to be true? $\exists x \in A \;.\; P(x,y)$: that is, we can find an app that passes the test. In other words, "each test is passed by at least one of these apps."

Consider $\exists x \in A \;.\; \forall y \in T \;.\; P(x,y)$ with this rule. This expression starts with $\exists x \in A$ so we need to consider each app, and something needs to be true of at least one of the apps. What is that thing that needs to be true? $\forall y \in T \;.\; P(x,y)$: that is, the app passes every test. Putting that together, we have, "at least one of these apps passes all tests."

When constructing logic from claims like this, it can help to ask "is this a claim about everything or one thing?" If the claims is about everything, start with $\forall$, otherwise with $\exists$, and then re-phrase the rest of the claim to be about a specific thing and repeat.

Examples:

- "Each test is passed by at least one of these apps."
    - That is a claim about all tests, so we start $\forall$. 
        
        $\forall t \in T \;.\;$
    - Rephrasing the rest for a specific test we have "the test is passed by at least one app."

        $\forall t \in T \;.\;$ test $t$ is passed by at least one app
    - That is a claim about one app, so we then have $\exists$.
        
        $\forall t \in T \;.\; \exists a \in A \;.\;$
    - Rephrasing the rest for a specific app we have "the test is passed by the app."

        $\forall t \in T \;.\; \exists a \in A \;.\;$ test $t$ is passed by app $a$
    - Since there's no "all"s or "at least one"s in that, we write it with a predicate

        $\forall t \in T \;.\; \exists a \in A \;.\; P(a,t)$

- "At least one of these apps passes all tests"
    - That is a claim about one app, so we start with $\exists$.
    
        $\exists a \in A \;.\;$
    - Rephrasing the rest for a specific app we have "the app passes all tests."
    - That is a claim about all tests, so we then have $\forall$. 

        $\exists a \in A \;.\; \forall t \in T \;.\;$
    - Rephrasing the rest for a specific test we have "the app passes the test."
    - Since there's no "all"s or "at least one"s in that, we write it with a predicate

        $\exists a \in A \;.\; \forall t \in T \;.\; P(a,t)$

- "Each nation has a government"
    - $\forall n \in N \;.\;$ nation $n$ has a government
    - $\forall n \in N \;.\; \big(\exists g \in G \;.\;$ nation $n$ is ruled by $g\big)$
    - $\forall n \in N \;.\; \big(\exists g \in G \;.\; R(g,n)\big)$

- "There's a government over all nations"
    - $\exists g \in G \;.\;$ all nations are under government $g$
    - $\exists g \in G \;.\; \big(\forall n \in N \;.\;$ nation $n$ is ruled by $g\big)$
    - $\exists g \in G \;.\; \big(\forall n \in N \;.\; R(g,n)\big)$

- "Each student will get a grade"
    - $\forall s \in S \;.\;$ student $s$ will get a grade
    - $\forall s \in S \;.\; \big(\exists g \in G \;.\;$ student $s$ gets grade $g\big)$
    - $\forall s \in S \;.\; \big(\exists g \in G \;.\; P(s,g)\big)$

- "There's a grade all students will get"
    - $\exists g \in G \;.\;$ every student gets grade $g$
    - $\exists g \in G \;.\; \big(\forall s \in S \;.\;$ student $s$ gets grade $g\big)$
    - $\exists g \in G \;.\; \big(\forall s \in S \;.\; P(s,g)\big)$

- "Each building is occupied by at least one person"
    - $\forall b \in B \;.\;$ there's a person in building $b$
    - $\forall b \in B \;.\; \big(\exists p \in P \;.\;$ person $p$ is in building $B\big)$
    - $\forall b \in B \;.\; \big(\exists p \in P \;.\; I(p,b)\big)$

- "There's one person that is in all the buildings at once"
    - $\exists p \in P \;.\;$ person $p$ is in every building
    - $\exists p \in P \;.\; \big(\forall b \in B \;.\;$ person $p$ is in building $B\big)$
    - $\exists p \in P \;.\; \big(\forall b \in B \;.\; I(p,b)\big)$


