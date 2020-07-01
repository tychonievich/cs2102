---
title: On logarithms
...

Logarithms are pervasive in computing.
They are not strictly a discrete mathematics topic, being continuous in form,
and were once taught extensively in pre-college algebra courses;
however, we have observed that fewer and fewer students come in to UVA already knowing them each year,
and thus have decided to cover them in this course.

As a summary, your should know that

- $\displaystyle \log_b(x) = w \equiv b^w = x$ 
    - which implies that $\displaystyle b^{\log_b(x)} = x$
- $\displaystyle \log_x(y)$ is approximately the number of digits needed to represent $y$ in base-$x$
    - The exact number is $\displaystyle 1 + \big\lfloor \log_x(y) \big\rfloor$
- $\displaystyle \log_b(x y) = \log_b(x) + \log_b(y)$ and its related identities: 
    - $\displaystyle \log_a(b^n) = n \log_a(b)$ and 
    - $\displaystyle \log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)$
- $\displaystyle \log_b(x) = {\log_a(x) \over \log_a(b)}$ -- i.e., changing base is multiplying by a constant


# Definitions

The **log base $b$ of $x$** is written $\log_b(x)$ and means "the power to which $b$ must be raised to result in $x$".

{.example} $\log_3(81) = 4$ because $3^4 = 81$

The **log base 10 of $x$** is a continuous parallel to the number of digits needed to write $x$ as a decimal (base-10) integer.

{.example} $\log_{10}(81) = 1.908405\dots$, a number a bit smaller than 2 because $81$ is a bit smaller than the largest 2-digit number.

{.example} $\log_{10}(99.999999\dots) = 2$ because it is as big as 2-digit numbers can be. This also means that $\log_{10}(100.0000\dots) = 2$ because $100.000\dots - 99.999\dots = 0$.

The **log base 2 of $x$** is a continuous parallel to the number of digits needed to write $x$ as a binary (base-2) integer.

{.example} $\log_{2}(81) = 6.3395\dots$ because the binary for 81 is 1010001, more than you can fit in 6 bits but less than you can fit in 7.

$\ln(x)$ means $\log_e(x)$, where $e$ is [2.71828182845904523536…](https://oeis.org/A001113) and is sometimes called Euler's number or Napier's constant.

$\lg(x)$ means $\log_2(x)$

$\log(x)$ means either $\log_2(x)$ (common in computing) or $\log_{10}(x)$ (common in engineering) or $\log_e(x)$ (common in mathematics).

# Defining properties

## Change of base

How important is the base used in a logarithm? It matters, but only by a fixed constant factor.

{.example} $\log_3(81) = 4$ because $3^4 = 81$; $3^4 = (3^2)^2 = 9^2$ so $\log_9(81) = 2$. But the same reasoning works for other values: if $\log_3(x) = y$ then $3^y = x$, meaning $(3^2)^{y\div 2} = x$, meaning $\log_9(x) = \frac{y}{2}$.

{.example ...} Suppose a number used 24 digits to write in base 10. How many digits does it take to write in base 1000? 8: each cluster of 3 digits in base 10 turns into one digit in base 1000, so $\log_{1000}(x) = \frac{1}{3}\log_{10}(x)$.

Arguably, this is what the thousands separators do: they take a too-big-to-read decimal numbers like 23276820784381 and re-write them as more readable milial numbers like 23,276,820,784,381
where 784 is a single "digit" in this base-1000 representation.
{/}

This leads to the change of base identity: 

:::theorem
$\boxed{\displaystyle \log_b(x) = {\log_a(x) \over \log_a(b)}}$
:::

This identity shows up often enough in computing that it is worth memorizing.

{.example} $\log_2(x) = \log_2(10) \log_{10}(x)$, and $\log_2(10) = 3.321928\dots$. Thus, a 10-digit number is a $33.21928\dots$-bit number.

{.example} The most common representation of non-integer numbers in computers is the IEEE-754 double-precision floating-point number, which is represented with 53 bits of precision. Dividing by $\log_2(10) = 3.321928\dots$, we find this is $15.95\dots$ digits of precision.

:::corollary
$\displaystyle \log_a(b) = \frac{1}{\log_b(a)}$
:::

This corollary is somewhat interesting, but probably not worth memorizing.

:::proof
$\displaystyle \log_a(b) = \frac{\log_b(b)}{\log_b(a)}$; since $b^1 = b$, $\log_b(b) = 1$ meaning $\displaystyle \log_a(b) = \frac{1}{\log_b(a)}$.
:::

## Logs of multiples

How much larger is the log of $x$ than the log of $1000 x$? It is larger, but only by a fixed additive amount.

{.example} Since $\log_{10}(x)$ is the number of digits needed to represent $x$, and $1000 \times x$ requires exactly three more digits, it must be the case that $\log_{10}(1000 \times x) = 3 + \log_{10}(x) = \log_{10}{1000} + \log_{10}{x}$

{.example} If $\log_{3}(81 \times x) = y$ then $3^y = 81 \times x = 3^4 \times x$ meaning $3^{y-4} = x$; thus $\log_{3}(x) = y-4 = \log_{3}(81 \times x) - 4 = \log_{3}(81 \times x) - \log_3{81}$

:::theorem
$\boxed{\displaystyle \log_b(x y) = \log_b(x) + \log_b(y)}$
:::

This identity shows up often enough in computing that it is worth memorizing.
In fact, logarithms are sometimes used in algorithm design specifically for this property of changing multiplications into additions^[For one example algorithm of this kind that has figured prominently in debates about software patents see [Karmarkar's Algorithm](https://en.wikipedia.org/wiki/Karmarkar%27s_algorithm)].

{.example} $\ln(77) = 4.3438\dots = \ln(7 \times 11) = \ln(7) + \ln(11) = 1.9459\dots + 2.397895\dots$ 

:::corollary
$\boxed{\displaystyle \log_a(b^n) = n \log_a(b)}$
:::

This corollary is important enough to be worth memorizing in its own right.

:::proof
$b^n$ means $b \times b \times \dots \times b$ with $n$ $b$s.
By theorem 2, the log of that is $\log_a(b) + \log_a(b) + \dots + \log_a(b)$ with $n$ $\log_a(b)$s.
Since $x + x + \dots + x$ with $n$ $x$s is the definiton of $nx$, we arrive at
$n\log_a(b)$.
:::

:::corollary
$\boxed{\displaystyle \log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)}$
:::

This corollary is important enough to be worth memorizing in its own right.

:::proof
$\displaystyle \log_b\left(\frac{x}{y}\right) = \log_b(x \times y^{-1})$; by theroem 2 that is $\log_b(x) + \log_b(y^{-1})$; by corollary 2 that becomes $\log_b(x) + -1 \log_b(y) = \log_b(x) - \log_b(y)$.
:::

# Other math you may have missed learning

- $\lfloor x \rfloor$ is called the "floor of $x$" and means "the largest integer not larger than $x$"; thus $\lfloor 3.8 \rfloor = 3$, $\lfloor 3 \rfloor = 3$, and $\lfloor -2.2 \rfloor = -3$.

- $\lceil x \rceil$ is called the "ceiling of $x$" and means "the smallest integer not smaller than $x$"; thus $\lceil 3.2 \rceil = 4$, $\lceil 3 \rceil = 3$, and $\lceil -2.8 \rceil = -2$.

- $x \mod y$ means "the remainder of $x$ divided by $y$" and is similar to the computing operator `%`.
    
    Sometimes mod is applied to entire equations; for example, $7 = 11 \mod 4$.
    
    If either $x$ or $y$ is negative, sources differ on if $x \mod y$ should be positive or negative.
