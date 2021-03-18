---
title: Symbols we'll use
...

: Propositions

Concept          Java/C      Python      This class                      Bitwise    Name            Other
--------        --------    --------    ---------------------------     ---------   ------          ---------
true            `true`      `True`      $\top$ or $1$                   `-1`        tautology       T
false           `false`     `False`     $\bot$ or $0$                   `0`         contradiction   F
not $P$         `!p`        `not p`     $\lnot P$ or $\overline{P}$     `~p`        negation
$P$ and $Q$     `p && q`    `p and q`   $P \land Q$                     `p & q`     conjunction     $P Q$, $P \cdot Q$
$P$ or $Q$      `p || q`    `p or q`    $P \lor Q$                      `p | q`     disjunction     $P + Q$
$P$ xor $Q$     `p != q`    `p != q`    $P \oplus Q$                    `p ^ q`     parity          $P ⊻ Q$, 
$P$ implies $Q$                         $P \rightarrow Q$                           implication     $P \supset Q$, $P \Rightarrow Q$
$P$ iff $Q$     `p == q`    `p == q`    $P \leftrightarrow Q$                       bi-implication  $P \Leftrightarrow Q$, $P$ xnor $Q$


: Proofs

Concept          Symbol         Meaning
--------        --------        --------------
equivalent      $\equiv$        "$A \equiv B$" means "$A \leftrightarrow B$ is a tautology"
entails         $\vDash$        "$A \vDash B$" means "$A \rightarrow B$ is a tautology"
provable        $\vdash$        "$A \vdash B$" means "$A$ proves $B$"; it means both "$A \vDash B$" and "I know $B$ is true because $A$ is true"<br/>"$\vdash B$" (without $A$) means "I know $B$ is true"
therefore       $\therefore$    "$\therefore A$" means "the lines above this $\vdash A$"<br/>"$\therefore A$" also connotes "$A$ is the thing we wanted to show"
proof done      ∎<br>q.e.d.     marks the end of a written (prose) proof
hypothesis                      something we expect is true
theorem                         something we've proven is true
corollary                       small theorem that builds off of the main theorem
lemma                           small theorem that helps set up the proof of the main theorem


: Arithmetic

Concept      Symbol                             Meaning
--------    --------                            --------------
floor       $\lfloor x \rfloor$                 the largest integer not larger than $x$<br/>$x$ rounded down to an integer
ceiling     $\lceil x \rceil$                   the smallest integer not smaller than $x$<br/>$x$ rounded up to an integer
exponent    $x^y$                               $x$ multiplied by itself $y$ times
sum         $\displaystyle \sum_{x \in S} f(x)$ the sum of all members of $\{ f(x) \;|\; x \in S\}$<br/>By definition, 0 if $S = \{\}$
sum         $\displaystyle \sum_{x=a}^{b} f(x)$ $\displaystyle \sum_{x\in S} f(x)$ where $S = \{ x \;|\; (x \in \mathbb Z) \land (a \le x \le b)\}$<br/>the sum of $f(x)$ applied to integers between $a$ and $b$ inclusive
product     $\displaystyle \prod_{x \in S} f(x)$ the product of all members of $\{ f(x) \;|\; x \in S\}$<br/>By definition, 1 if $S = \{\}$
product     $\displaystyle \prod_{x=a}^{b} f(x)$ $\displaystyle \prod_{x\in S} f(x)$ where $S = \{ x \;|\; (x \in \mathbb Z) \land (a \le x \le b)\}$<br/>the product of $f(x)$ applied to integers between $a$ and $b$ inclusive
factorial   $x!$                                $\displaystyle \prod_{i=1}^{x} i$<br/>the product of all positive integers less than or equal to $x$<br/>the number of permutations of a length-$x$ sequence with distinct members
choose      $\displaystyle {n \choose k}$       $\displaystyle {n! \over (n-k)! k!}$<br/>the number of $k$-member subsets of an $n$-element set
