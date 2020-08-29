---
title: Practice problems with sets and quantifiers
...

This is an extension to [sets practice](sets-practice.html).

# Logic in set-builder notation

Each of the following is either true or false; which one?

- $3 \in \big\{x + y \;\big|\; x,y \in \mathbb{Z}^{+} \land x > y \big\}$^[true]
- $3.5 \in \big\{x + y \;\big|\; x \in \mathbb{Z}^{+} \land y \in \mathbb{R}^{+} \big\}$^[true]
- $0 \in \big\{x + y \;\big|\; x,y \in \mathbb{Z}^{+} \land x > y \big\}$^[false]
- $0 \in \big\{x - y \;\big|\; x,y \in \mathbb{R} \land x > y \big\}$^[false]



# Qualified membership

Each of the following is either true or false; which one?

- $\forall x \in \mathbb R \;.\; x \in \mathbb Q$^[false]
- $\forall x \in \mathbb Q \;.\; x \in \mathbb R$^[true]
- $\forall x \in \mathbb Z^{+} \;.\; \exists y \in \mathbb Z^{-} \;.\; x + y = 0$^[true]
- $\forall x \in \mathbb R^{+} \;.\; \exists y \in \mathbb Z^{+} \;.\; 1 \leq \frac{x}{y} \leq 2$^[false (consider 0.00001)]
- $\exists x \in \mathbb R \;.\; x \in \mathbb N$^[true]
- $\exists x \in \mathbb R^{+} \;.\; x \notin \mathbb Q^{+}$^[true]
- $\exists x,y \in (\mathbb R \setminus \mathbb N) \;.\; (x \neq y) \land \big((x - y) \in \mathbb N\big)$^[true]
- $\forall x \in \mathbb R \;.\; (x \in \mathbb N) \rightarrow (x \in \mathbb Z)$^[true]
- $\forall x \in \mathbb Z \;.\; (x \in \mathbb Z^{+}) \lor (x \in \mathbb Z^{-})$^[false]
- $\forall x \in \mathbb N \;.\; (x < 0) \rightarrow \bot$^[true]
- $\forall x \in \mathbb N \;.\; x \in \big\{ \lfloor y \rfloor \;\big|\; y \in \mathbb R^{+} \big\}$^[true]
- $\forall x \in \mathbb N \;.\; x + 1 \in \mathbb N$^[true]
- $\forall S \in \{\mathbb Z, \mathbb Q, \mathbb R\}\;.\; \forall x \in S \;.\; x + 1 \in S$^[true]
- $\forall x \in \{3, 1, 4, 5\} \;.\; x^{x} \in \{0, 1, 4, 27, 256, 3125, 46656\}$^[true]
- $0 \in \big\{x \;\big|\; \exists y \in \mathbb Z \;.\; y^{y} = x \big\}$^[false]
- $\Big|\big\{ x \;\big|\; (x \in \mathbb R) \land (\forall y \in \mathbb N \;.\; x > y) \big\}\Big| \in \{0,1,2\}$^[true]
- $8 \in \big\{x^3 \;\big|\; \exists y \in \mathbb Z \;.\; y^2 = x \big\}$^[false]
- $1 \in \big\{x^3 \;\big|\; \exists y \in \mathbb Z \;.\; y^2 = x \big\}$^[true]
- $64 \in \big\{x^3 \;\big|\; \exists y \in \mathbb Z \;.\; y^2 = x \big\}$^[true]


# Comparison

For each of the following, fill in the blank with the first element of the following list that applies:

- $=$ if the two are identical; otherwise
- $\subset$ or $\supset$ if those are true; otherwise
- $\subseteq$ or $\supseteq$ if those are true; otherwise
- "disjoint" if the intersection of the two is $\emptyset$; otherwise
- $\neq$

|Set 1 |  |Set 2|
|------|--|-----|
|$\{0, 1\}$ |<input></input>^[=] |$\big\{ x \;\big|\; x \in \mathbb{R} \land x^2 = x\big\}$|
|$R^{+} \cup \{0\}$|<input></input>^[=] |$\big\{ x \;\big|\; x \in \mathbb R \land \sqrt{x^2} = x \big\}$|
|$\mathbb R \setminus \mathbb Z$|<input></input>^[=] |$\Big\{ x \;\Big|\; (x \in \mathbb R) \land \big(\forall y \in \mathbb Z \;.\; x \neq y\big) \Big\}$|
|even numbers |<input></input>^[=] |$\big\{x \;\big|\; \exists y \in \mathbb Z \;.\; 2y = x\big\}$|
|$\mathbb{N}$ |<input></input>^[$\supset$ (would be = if $\mathbb Z^{+}$ instead of $\mathbb N$] |$\Big\{ x \;\Big|\; x \in \mathbb{R}^{+} \land \big(x - \lfloor x \rfloor = 0\big)\Big\}$|




# Listing members and cardinality

For each of the following, list the members of the set:

- $\big\{\frac{x}{y} \;\big|\; x\in\{0,1,2\} \land y\in\{1,2,4\} \big\}$^[$\big\{0, \frac{1}{4}, \frac{1}{2}, 1, 2\big\}$]
- $\Big\{ x + y \;\Big|\; (x,y \in \mathbb Z) \land (1 < x < y < 10)$ $\land$ $\big(\forall w \in \mathbb Z^{+} \setminus \{1\} \;.\; (x \neq w \rightarrow 0 \neq x \mod{w}) \land (y \neq w \rightarrow 0 \neq y \mod{w}) \big) \Big\}$^[$\{5,7,8,9,10,12\}$]
