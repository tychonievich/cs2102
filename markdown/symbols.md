---
title: Symbols we'll use
...

# Logic symbols

Concept          Java/C      Python      This class                      Bitwise    Other
--------        --------    --------    ---------------------------     ---------   ------
true            `true`      `True`      $\top$ or $1$                   `-1`        T, tautology
false           `false`     `False`     $\bot$ or $0$                   `0`         F, contradiction
not $P$         `!p`        `not p`     $\lnot P$ or $\overline{P}$     `~p`
$P$ and $Q$     `p && q`    `p and q`   $P \land Q$                     `p & q`     $P Q$, $P \cdot Q$
$P$ or $Q$      `p || q`    `p or q`    $P \lor Q$                      `p | q`     $P + Q$
$P$ xor $Q$     `p != q`    `p != q`    $P \oplus Q$                    `p ^ q`     $P ⊻ Q$
$P$ implies $Q$                         $P \rightarrow Q$                           $P \supset Q$, $P \Rightarrow Q$
$P$ iff $Q$     `p == q`    `p == q`    $P \leftrightarrow Q$                       $P \Leftrightarrow Q$, $P$ xnor $Q$

Concept          Symbol         Meaning
--------        --------        --------------
equivalent      $\equiv$        "$A \equiv B$" means "$A \leftrightarrow B$ is a tautology"
entails         $\vDash$        "$A \vDash B$" means "$A \rightarrow B$ is a tautology"
provable        $\vdash$        "$A \vdash B$" means "$A$ proves $B$"; it means both "$A \vDash B$" and "I know $B$ is true because $A$ is true"<br/>"$\vdash B$" (without $A$) means "I know $B$ is true"
therefore       $\therefore$    "$\therefore A$" means "the lines above this $\vdash A$"<br/>"$\therefore A$" also connotes "$A$ is the thing we wanted to show"

# Math symbols

Concept      Symbol                             Meaning
--------    --------                            --------------
floor       $\lfloor x \rfloor$                 the largest integer not larger than $x$<br/>$x$ rounded down to an integer
ceiling     $\lceil x \rceil$                   the smallest integer not smaller than $x$<br/>$x$ rounded up to an integer
exponent    $x^y$                               $x$ multiplied by itself $y$ times
factorial   $x!$                                $\displaystyle \prod_{i=1}^{x} i$<br/>The product of all positive integers less than or equal to $x$
sum         $\displaystyle \sum_{x \in S} f(x)$ the sum of all members of $\{ f(x) \;|\; x \in S\}$
sum         $\displaystyle \sum_{x=a}^{b} f(x)$ the sum of all members of $\{ f(x) \;|\; (x \in \mathbb Z) \land (a \le x \le b)\}$
product     $\displaystyle \prod_{x \in S} f(x)$ the product of all members of $\{ f(x) \;|\; x \in S\}$
product     $\displaystyle \prod_{x=a}^{b} f(x)$ the product of all members of $\{ f(x) \;|\; (x \in \mathbb Z) \land (a \le x \le b)\}$
