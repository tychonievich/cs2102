---
title: Why Logic?
...

A major goal of this class is to teach you to speak with sets and first-order logic. Just as programming languages provide an unambiguous language for describing actions, so sets and logic provide an unambiguous language for describing facts.

# Example 1

Suppose we want to express the fact

> This test suite is incomplete

That's a very ambiguous statement; we need to define "this test suite" and "incomplete" before we know what is being said.

## Logic: if, and, or, not

In your introduction to programming course you learned about the "logical operators", which might have been spelled as `and`{.py}, `or`{.py}, and `not`{.py} or as `&&`{.java}, `||`{.java}, and `!`{.java}, or as `&`{.c}, `|`{.c}, and `~`{.c}, or ...

Also, all your life you have been used to people using words like "and" and "both" and "if" and so on to combine multiple claims into one. However, single words can be used in several different ways depending on context, making English a poor language for this in general. For example,

Phrase                                      Commonly means
-----------------------------------         ------------------------------------
Would you like salt **or** pepper?          2 options: "yes" (you get both salt and pepper) or "no" (you get neither)
Would you like that for here **or** to go?  2 options: "here" (not to go) or "to go" (not here)
Do you speak Hindi **or** Mandarin?         4 options: "no", "Hindi", "Mandarin", "both"
I love it **when** it rains                 Of the four options (loving/not weather that is rainy/not), one is ruled out (raining + not loving)
It unlocks **when** you turn the key        Of the four options (unlocking/not + turning key/not), two are ruled out (unlocking + not turning key; turning key + not unlocking)
**If** you propose, I'll marry you          Of the four options (proposing/not we marry/not), two are ruled out (proposing + not marrying; marrying + not proposing)
**If** a number ends with 0, it is an even  Of the four options (ending with 0/not, being even/not), one is ruled out (ending with 0 + not even)

Because neither English nor code give us a single correct well-defined set of operators, we borrow those from formal logic: $\land$, $\lor$, $\lnot$, $\rightarrow$, $\oplus$, and $\leftrightarrow$. Each of these will be defined, but none of them will fit as a replacement for every instance of a particular word because words have different meanings in different contexts.

## Sets: this, not that

A set divides "the universe of discourse" -- a formal notion of "everything we can talk about" -- into two parts: members of the set and non-members of the set. We use sets to refer to a specific group of things.

Sometimes it is useful to describe sets explicitly;
for example, "this test suite" is very likely a known collection of tests.
The usual notation for an explicit set is to put the elements in braces; for example, if our tests are noted as $t_i$ for $1 \le i \le 4$ then our test suite would be written as $\{t_1, t_2, t_3, t_4\}$.

Other times it is useful to describe sets implicitly by describing some computation which results in "true" if and only if a value is in a set.
The usual notation for an implicit set has two parts:
a template for describing an element and an expression to determine if a value is in the set.
These are traditionally placed inside braces and separated with a pipe.
For example the set of valid (latitude, longitude) pairs could be written as
$\big\{ (x,y) \;\big|\; (-180 < x \le 180) \text{~and~} (-90 \le y \le 90) \big\}$

We'll also see how to create sets from other sets, with operators to provide "the set of things in both of these two other sets" and so on.

Sometimes we don't need to specify the specific meaning of a set to but will refer to them simply by a variable name.
It is traditional, but not strictly required, to use an upper-case letter to represent a set.

Idea                Math
----------------    ------------
This test suite     $T$

## Quantifiers: All, some, or none

Many of the facts we want to express are structurally claims about whether all, some, or none of the elements of a set have a particular property.
Specific numbers are much less commonly needed: usually we just need "all", "at least one", and "none".

Let's consider "incomplete": a test suite is incomplete if there's a broken program that passes all the tests.
That is, there is **at least one** program that is both (a) broken and (b) passes **all** tests.

The way we write all, some, and none are with quantifiers, special expressions we put in front of logic to change what a variable means within that logic.

Math                        English
-----------                 ---------------------------------------------
$\forall x \;.\; \Gamma$    $\Gamma$ is true no matter which value $x$ has
$\exists x \;.\; \Gamma$    There's at least one value $x$ could have that makes $\Gamma$ true
$\nexists x \;.\; \Gamma$   There's no value $x$ could have that makes $\Gamma$ true<br/>  — *or, equivalently* —<br/>$\Gamma$ is false no matter which value $x$ has

These get more confusing when we combine them, and again English starts to fail us. For example, all three of the following have the general structure "there's a $x$ that fits every $y$", meaning $\exists x$ and $\forall y$, but each has a different meaning:

Phrase                                  Commonly means
-----------------------------------     ------------------------------------
There's a shirt that fits all of us     Pick any one of us you want; that one can fit in the shirt
There's a shirt that fits each of us    Pick any one of us you want; that one can find at least one of the shirts that fits
There's a bus that fits all of us       You can put us all in the bus at the same time
There's a bus that fits each of us      Pick any one of us you want; that one can fit in the bus

In logic, we distinguish these meanings in part by the order of quantifiers:

Phrase                                  Quantifiers
-----------------------------------     ------------------------------------
There's a shirt that fits all of us     $\exists$ shirt . $\forall$ people in set "us" . shirt fits person
There's a shirt that fits each of us    $\forall$ people in set "us" . $\exists$ shirt . shirt fits person
There's a bus that fits all of us       $\exists$ bus . bus fits the set "us"
There's a bus that fits each of us      $\exists$ shirt . $\forall$ people in set "us" . bus fits person



