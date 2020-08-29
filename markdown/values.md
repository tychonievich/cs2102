---
title: Entities, Identities, and Values
...

In mathematics, we discuss and name values.
In (imperative) programming, we discuss and name entities.

# By example

[7](https://en.wikipedia.org/wiki/7) is a value.
[James E. Ryan](https://en.wikipedia.org/wiki/James_E._Ryan_%28educator%29) is an entity.

Let $x$ and $y$ both refer to the number 7.
Let "Jim Ryan" and "UVA's President" both refer to James E. Ryan.

If I make $x$ a little bigger, $x$ is no longer 7.
It might be 7.1 or 8 or the like, but it can't be bigger than it was and still be 7.
This is because 7 is a value: an unchanging Platonic ideal.
It is impossible, by definition, to make 7 itself bigger.

If I make "Jim Ryan" bigger,
perhaps by feeding him huge amounts of fatty foods and preventing him from exercising,
he's still James E. Ryan.
This is because James E. Ryan is an entity:
something that retains its identity even if details about it change.
He can get bigger, smaller, richer, poorer, older, wiser, ill, well: none of this changes his identity.

Because $x$ and $y$ refer to a value,
changing $x$ means changing which value $x$ refers to and thus has no impact on $y$.
Because  "Jim Ryan" and "UVA's President" refer to an entity,
changing that entity changes the entity both refer to:
if I give UVA's President some money, Jim Ryan's gets richer.

# Entities and values in this course

This is a mathematics course.
We discuss mathematical topics, meaning we discuss values.
In that context, you should know the following:

## A value can be written in multiple ways.

Whether distinct writings describe the same value or not
is determined by the properties of the value type.
For example, "$3+4$" and "$7$" represent the same *integer*.
However, "$3+4$" and "$7$" represent different *arithmetic expressions*.

## Variables name just one value within a given context.

In programing, `x` might be `2` one time you look at it and `3` the next.
That can't happen in math; if $x$ is $2$, then $x$ is $2$.

In programming, the name `x` can appear in several scopes to refer to different variables.
This can also happen in mathematics; in each problem $x$ might refer to a different value.
However, within a single problem $x$ cannot change.

We will learn about quantifiers in this class, which will add another kind of mathematical scope beyond just problems.

## Discrete math values have related programming entities

We'll learn about sets in this class.
Sets are values in discrete mathematics, just like numbers are:
unchangeable Platonic ideals.
Most programming languages have a datatype they call a set
which is not a value but an entity:
changeable objects with durable identity.

This can be confusing, so we'll try to point this out from time to time.
Which means you'll hear us say "a set is just a value, it can't change"
and so on.
Know that these assertions are trying to contrast math from programming,
not one math concept from another.
Everything in this class (sets, sequences, strings, relations, functions, sums, permutations, logarithms, ...) is a mathematical construct
and thus a value, not an entity.

