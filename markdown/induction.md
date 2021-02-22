---
title: Induction
...

MCS discusses induction in chapter 5. This text is intended to supplement, not replace, that text.

# The idea, programmer's version

Suppose I have a loop that iterates over some list.
How do I know what the results will be after the loop is over?
The most common reasoning goes like this:

1. I know what's true before the loop starts
2. I know it stays true each pass through the loop
    a. because it starts true
    b. and one step of the loop does not make it false
3. So I know it must be true at the end

This outline may make intuitive sense, but we need to formalize it to make it into a proof strategy.

1. We need some starting place. We call that the **base case**.
    It can be as complicated as we need, though often it will be quite simple.

2. We need some loop-like way of getting from one truth to the next.
    We call that the **inductive step**. It generally works as follows
    
    a. we assume it starts true; this assumption is called the **inductive hypothesis**
    b. we use that assumption to prove that it will still be true one step later

3. We conclude it must always be true. This step is not a proof, it's a rule called the **principle of induction**.

# The idea, formal logic version

The **principle of induction** is a proof rule that looks like:

$$\begin{aligned}
&P(0)\\
&P(n) \rightarrow P(n+1)\\
\therefore\;&\forall x \in \mathbb N \;.\; P(x)
\end{aligned}$$

Thus, to use it, we first prove $P(0)$; then prove $P(n) \rightarrow P(n+1)$ by assuming $P(n)$ and proving $P(n+1)$; then state that by the principle of induction, $\forall x \in \mathbb N \;.\; P(x)$.

In this approach "first prove $P(0)$" is called the **base case**;
"then prove $P(n) \rightarrow P(n+1)$" is called the **inductive step**;
and "by assuming $P(n)$" is called the **inductive hypothesis**.

What if your base case is more involved than $P(0)$?
The formal answer is "define a different $P$"

{.example ...}
Let's try proving the following by induction:

:::theorem
All Fibonacci numbers are positive
:::

A fairly high-level proof might look like

:::proof
We proceed by induction.

Base case
:   The first two Fibonacci numbers are both 1, a positive number.

Inductive step
:   Assume that the $k$^th^ and $(k+1)$^th^ Fibonacci number are both positive.
    Then the $(k+2)$^th^ Fibonacci number must also be positive because it is the sum of two positive numbers.

By the principle of induction, it follows that all Fibonacci numbers are positive.
:::

All well and good. But how do we make this fit the formal definition of induction?
We define a special $P(n)$ to mean "the $(n+1)$^th^ and $(n+2)$^th^ Fibonacci number are both positive".
With this special predicate, our base case becomes just $P(0)$ (i.e., the 1^st^ and 2^nd^ are positive) and our inductive step becomes a proof that $P(n) \rightarrow P(n+1)$.
{/}

Although we *can* convert arbitrary induction into a formal variation, we won't in this class or anywhere else outside of formal logic.

# Examples

{.example ...}
Consider this code:

<table><tr><th>Java</th><th>Python</th></tr><tr><td valign="top">
```java
double babylonian(double x) {
    double y = 1;
    for(int i=0; i<20; i+=1) {
        y = (y + x/y)/2;
    }
    return y;
}
```                          
</td><td valign="top">
```python
def babylonian(x):
    y = 1
    for i in range(20):
      y = (y + x/y)/2
    return y
```
</td></tr></table>

How could we verify that the end result is between 1 and `x`?

:::proof
Initially, `y` is between `1` and `x` (in particular, it is `1`).
Each pass through the loop `y` is updated to be the average of two values: `y` and `x/y`.
We know one of those (`y`) is between `1` and `x`; but is the other?

Consider `x/y`. We proceed by cases.

Case 1: `x` < 1
:   In this case, "`y` is between 1 and `x`" means "`x` ≤ `y` ≤ 1".
    Because `x` ≤ `y`, `x/y` ≤ 1.
    Because `y` ≤ 1, `x` ≤ `x/y`.
    Thus, `x` ≤ `x/y` ≤ 1, meaning it is between 1 and `x`.

Case 2: `x` ≥ 1
:   In this case, "`y` is between 1 and `x`" means "1 ≤ `y` ≤ `x`".
    Because `y` ≤ `x`, 1 ≤ `x/y`.
    Because 1 ≤ `y`, `x/y` ≤ `x`.
    Thus, 1 ≤ `x/y` ≤ `x`, meaning it is between 1 and `x`.

Because `x/y` is between 1 and `x` in both cases, it is between them in general.

Thus, the loop replaces `y` with the average of two numbers, both between 1 and `x`, so it keeps `y` between 1 and `x`.

Because we start between 1 and `x` and that does not change, `y` ends up (and thus the function returns a value that is) between 1 and `x`.
:::

Incidentally, the functions actually return $\sqrt{x}$, though proving that is beyond the scope of this course.
{/}

