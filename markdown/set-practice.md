---
title: Practice problems with sets
...

Assume the following definitions:

notation            meaning
---------------     -------------------
$\mathbb{Z}$        The integers
$\mathbb{Z}^{+}$    The positive integers; i.e., $\big\{ x \; \big| \; x \in \mathbb{Z} \land x > 0 \big\}$
$\mathbb{N}$        The natural numbers; i.e., $\big\{ x \; \big| \; x \in \mathbb{Z} \land x \geq 0 \big\}$
$\mathbb{Z}^{-}$    The negative integers; i.e., $\big\{ x \; \big| \; x \in \mathbb{Z} \land x < 0 \big\}$
$\mathbb{R}$        The real numbers
$\mathbb{Q}$        The rational numbers; i.e., $\Big\{ \frac{x}{y} \; \Big| \; x \in \mathbb{Z} \land y \in \mathbb{Z}^{+} \Big\}$
$\pi$               The ratio of the circumference of a circle to its diameter; 3.1415926535...

Assume that $\mathbb Q^{+}$, $\mathbb Q^{-}$, $\mathbb R^{+}$, and $\mathbb R^{-}$ are defined similarly to $\mathbb Z^{+}$ and $\mathbb Z^{-}$.


# Membership

## Simple membership

Each of the following is either true or false; which one?

- $3 \in \mathbb Z$^[true]
- $3.5 \in \mathbb Z$^[false]
- $\pi \in \mathbb Z$^[false]
- $3 \in \mathbb Q$^[true]
- $3.5 \in \mathbb Q$^[true]
- $\pi \in \mathbb Q$^[false]
- $3 \in \mathbb R$^[true]
- $3.5 \in \mathbb R$^[true]
- $\pi \in \mathbb R$^[true]

- $3 \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$^[false]
- $\{3\} \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$^[false]
- $\{2, 3\} \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$^[true]

- $\{2, 3\} \in \mathcal{P}\big(\{2, 3\}\big)$^[true]
- $|\{2, 3\}| \in \{2, 3\}$^[true]
- $|\{2, 3\}| \in \mathcal{P}\big(\{2, 3\}\big)$^[false]
- $\infty \in \mathbb R$^[false]

## Closed sets

A set is said to be **closed over** an operation if applying that operation to members of the set always results in another member of that set.

- Which (if any, or all) of the following operators is $\mathbb Z$ closed over?
    - <label><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <label><input type="checkbox"></input> subtraction ($-$)</label>^[true]
    - <label><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <label><input type="checkbox"></input> division ($\div$)</label>^[false]
    - <label><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[mostly true, except for 0 divisors]
    - <label><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb N$ closed over?
    - <label><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <label><input type="checkbox"></input> subtraction ($-$)</label>^[false]
    - <label><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <label><input type="checkbox"></input> division ($\div$)</label>^[false]
    - <label><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[mostly true, except for 0 divisors]
    - <label><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb R^{-}$ closed over?
    - <label><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <label><input type="checkbox"></input> subtraction ($-$)</label>^[false]
    - <label><input type="checkbox"></input> multiplication ($\times$)</label>^[false]
    - <label><input type="checkbox"></input> division ($\div$)</label>^[false]
    - <label><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[false. At a minimum, $-1 \mod -1 = 0 \notin \mathbb Z^{-}$. Also, there are two interpretations of $-4 \mod -3$; either it is $-1$ or it is $2$. $-1$ is more common in programming languages, $2$ is more common in the mathematics used in encryption.]
    - <label><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb Q$ closed over?
    - <label><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <label><input type="checkbox"></input> subtraction ($-$)</label>^[true]
    - <label><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <label><input type="checkbox"></input> division ($\div$)</label>^[mostly true, except for 0 divisors]
    - <label><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[mostly true, except for 0 divisors]
    - <label><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb Q \setminus \{0\}$ closed over?
    - <label><input type="checkbox"></input> addition ($+$)</label>^[false]
    - <label><input type="checkbox"></input> subtraction ($-$)</label>^[false]
    - <label><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <label><input type="checkbox"></input> division ($\div$)</label>^[true]
    - <label><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[false; $1 \mod 1 = 0$]
    - <label><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb R$ closed over?
    - <label><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <label><input type="checkbox"></input> subtraction ($-$)</label>^[true]
    - <label><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <label><input type="checkbox"></input> division ($\div$)</label>^[mostly true, except for 0 divisors]
    - <label><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[mostly true, except for 0 divisors]
    - <label><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false because $\mathbb R$ contains negative numbers]



# Comparison

For each of the following, fill in the blank with the first element of the following list that applies:

- $=$ if the two are identical; otherwise
- $\subset$ or $\supset$ if those are true; otherwise
- $\subseteq$ or $\supseteq$ if those are true; otherwise
- "disjoint" if the intersection of the two is $\emptyset$; otherwise
- $\neq$

|Set 1 |  |Set 2|
|------|--|-----|
|$\mathbb R$ |<input></input>^[$\supset$] |$\mathbb Q$|
|$\mathbb N$ |<input></input>^[$\supset$] |$\mathbb Z^{+}$|
|even numbers |<input></input>^[disjoint] |odd numbers|
|prime numbers |<input></input>^[$\neq$] |odd numbers|
|$\{1, 3, 5\}$ |<input></input>^[disjoint] |$\{\{1\}, \{3\}, \{5\}\}$|
|$\{1, 3, 5\}$ |<input></input>^[=] |$\{5, 3, 1\}$|
|$\{1, 3, 5\}$ |<input></input>^[$\supset$] |$\{5, 3\}$|
|$\mathbb R \setminus \mathbb Z$|<input></input>^[$\supset$] |$\mathbb R \setminus \mathbb Q$|
|$\mathbb Q \setminus \mathbb Z$|<input></input>^[disjoint] |$\{1, 2, 4\}$|
|$\emptyset$|<input></input>^[$\subset$] |$\mathcal{P}(\emptyset)$|
|$\{1\}$|<input></input>^[disjoint] |$\mathcal{P}(\{1\})$|


# Listing members and cardinality

For each of the following, list the members of the set:

- $\mathcal P \big(\mathcal P(\emptyset)\big)$^[$\Big\{ \{\}, \big\{\{\}\big\} \Big\}$]
- $\mathcal P \Big(\mathcal P \big(\mathcal P(\emptyset)\big)\Big)$^[$\bigg\{ \{\}, \big\{\{\}\big\}, \Big\{\big\{\{\}\big\}\Big\}, \Big\{\{\}, \big\{\{\}\big\}\Big\} \bigg\}$]
- Assume that $A = \{25,0,1\}$; $A \cup \mathcal P(A)$^[$\big\{25, 0, 1, \emptyset, \{25\}, \{0\}, \{1\}, \{25,0\}, \{25,1\}, \{0,1\}, \{25,0,1\}\big\}$]
- Assume that $A$ is the set of all 2-digit numbers; $|\mathcal{P}(A)|$^[$2^{90}$ which is 1,237,940,039,285,380,274,899,124,224]
- Assume that $A$ is the set of all 2-digit numbers; $|\mathcal{P}(A) \cap A|$^[$0$]
- Assume that $A$ is the set of all 2-digit numbers; $|\mathcal{P}(A) \cup A|$^[$2^{90}+90$ which is 1,237,940,039,285,380,274,899,124,314]

# Set-builder notation

Assume $A = \{1,2,3\}$ and $B = \{2,3,5\}$.
Write out each of the following in full.

Note that
"$\land$" means "and" (like `and`{.py} in Python or `&&` in Java);
"$\lor$" means "or" (like `or`{.py} in Python or `||` in Java); and
"$\lnot$" means "not" (like `not`{.py} in Python or `!` in Java).


- $\big\{ x \;\big|\; x \in A \big\}$ ^[$\{1,2,3\}$]
- $\big\{ x \;\big|\; x+1 \in A \big\}$ ^[$\{0,1,2\}$]
- $\big\{ x \;\big|\; x \in A \land x \in B \big\}$ ^[$\{2,3\}$]
- $\big\{ x \;\big|\; x \in A \lor x \in B \big\}$ ^[$\{1,2,3,5\}$]
- $\big\{ x \;\big|\; x \in A \land x \notin B \big\}$ ^[$\{1\}$]
- $\big\{ x+1 \;\big|\; x \in A \big\}$ ^[$\{2,3,4\}$]
- $\big\{ x+y \;\big|\; x \in A \land y \in B \big\}$ ^[$\{3,4,5,6,7,8\}$]
- $\big\{ \{x\} \;\big|\; x \in A \big\}$ ^[$\big\{ \{1\}, \{2\}, \{3\} \big\}$]
- $\big\{ \{x,y\} \;\big|\; x \in A \land y \in B \land x \ne y \big\}$ 
    ^[$\big\{\{1,2\}, \{1,3\}, \{1,5\}, \{2,3\}, \{2,5\}, \{3,5\}\big\}$]
- $\big\{ \{x,y\} \;\big|\; x \in A \land y \in B \big\}$ 
    ^[$\big\{\{1,2\}, \{1,3\}, \{1,5\}, \{2\}, \{2,3\}, \{2,5\}, \{3\}, \{3,5\}\big\}$]
- $\big\{ x \;\big|\; x \subseteq A \big\}$ 
    ^[$\big\{ \{\}, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\} \big\}$]
- $\big\{ x \;\big|\; x \subset A \big\}$ 
    ^[$\big\{ \{\}, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\} \big\}$]
- $\big\{ x \;\big|\; x \subseteq A \land x \subseteq B \big\}$ 
    ^[$\big\{ \{\}, \{2\}, \{3\}, \{2,3\}, \big\}$]
- $\big\{ x \;\big|\; x \subseteq (A \cap B) \big\}$ 
    ^[$\big\{ \{\}, \{2\}, \{3\}, \{2,3\}, \big\}$]
- $\big\{ x \;\big|\; x \subseteq A \lor x \subseteq B \big\}$ 
    ^[$\big\{ 
    \{\}, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\},
    \{5\}, \{2,5\}, \{3,5\}, \{2,3,5\}
    \big\}$]
- $\big\{ x \;\big|\; x \subseteq (A \cup B) \big\}$ 
    ^[$\big\{ 
    \{\},
    \{1\}, \{2\}, \{3\}, \{5\}, 
    \{1,2\}, \{1,3\}, \{1,5\}, \{2,3\}, \{2,5\}, \{3,5\},
    \{1,2,3\}, \{1,2,5\}, \{1,3,5\}, \{2,3,5\},
    \{1,2,3,5\},
    \big\}$]
- $\Big\{ \mathcal P\big(\{x\}\big) \;\Big|\; x \in A\Big\}$ 
    ^[$\Big\{ 
    \big\{\{\},\{1\}\big\},
    \big\{\{\},\{2\}\big\},
    \big\{\{\},\{3\}\big\}
    \Big\}$]
- $\big\{ x \;\big|\; x \notin A \big\}$ ^[An ill-defined set; as written, would contain "everything except 1, 2, and 3" but "everything" is not a mathematically valid concept.]
- $\big\{ x \;\big|\; x \in \mathbb Z \land x \notin A \big\}$ ^[all integers except 1, 2, and 3. Roughly, $\{\dots, -3, -2, -1, 0, 4, 5, 6, 7, \dots\}$, though $\dots$ is not a mathematically rigorous symbol.]
