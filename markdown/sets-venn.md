---
title: Venn Diagrams
...

Venn diagrams are often used to illustrate sets.

The basic concept of a Venn diagram is to draw overlapping shapes,
one for each set, and use the overlap to discuss various concepts.

There are three main techniques used within those shapes to illustrate additional ideas:

- The way shapes overlap can be adjusted to indicate some combinations are impossible
- Coloration can be used to indicate overlap that meets some property
- Labeled markers can be placed within shapes to show what sets specific ideas belong to
- Unlabeled markers can be placed within shapes to indicate possible patterns


: Set-Creating Operators

|Operator|New set highlighted|
|:------:|:-----------------:|
|$A \cap B$| ![](files/venn-cap.svg) |
|$A \cup B$| ![](files/venn-cup.svg) |
|$A \setminus B$| ![](files/venn-A-B.svg) |
|$B \setminus A$| ![](files/venn-B-A.svg) |


: Set-Limiting Predicates

|Predicate|Picture where true|
|:------:|:-----------------:|
|$A \subseteq B$| ![](files/venn-AsubB.svg) |
|$A \supseteq B$| ![](files/venn-AsupB.svg) |
|$A = B$| ![](files/venn-same.svg) |
|$A \cap B = \emptyset$| ![](files/venn-disjoint.svg) |


: Sets as Propositions

|Expression|Colored where true|Universally True|
|:--------:|:----------------:|:--------------:|
|$A$| ![](files/venn-A.svg) | ![](files/venn-allA.svg) |
|$B$| ![](files/venn-B.svg) | ![](files/venn-allB.svg) |
|$\lnot A$| ![](files/venn-nA.svg) | ![](files/venn-noA.svg) |
|$\lnot B$| ![](files/venn-nB.svg) | ![](files/venn-noB.svg) |
|$A \land B$| ![](files/venn-cap.svg) | ![](files/venn-allAB.svg) |
|$A \lor B$| ![](files/venn-cup.svg) | *no suitable image* |
|$A \leftrightarrow B$| ![](files/venn-eq.svg) | ![](files/venn-same.svg) |
|$A \oplus B$| ![](files/venn-xor.svg) | ![](files/venn-disjoint.svg) |
|$A \rightarrow B$| ![](files/venn-AiB.svg) | ![](files/venn-AsubB.svg) |
|$B \rightarrow A$| ![](files/venn-BiA.svg) | ![](files/venn-AsupB.svg) |
