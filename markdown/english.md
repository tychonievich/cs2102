---
title: English ambiguities
...

# Or

------  -----------------------------------------
Phrase  Would you like salt **or** pepper?
Means   2 options: "yes" (you get both salt and pepper) or "no" (you get neither)
Logic   say "yes" if $S \lor P$
Logic   you'll be given as if $S \leftrightarrow P$
------  -----------------------------------------

------  -----------------------------------------
Phrase  Would you like that for here **or** to go?
Means   2 options: "here" (not to go) or "to go" (not here)
Logic   presupposes $H \oplus G$
------  -----------------------------------------

------  -----------------------------------------
Phrase  Do you speak Hindi **or** Mandarin?
Means   4 options: "no", "Hindi", "Mandarin", "both"
Logic   "no" means $\lnot(H \lor M)$
------  -----------------------------------------

------  -----------------------------------------
Phrase  Do you speak first **or** second?
Means   2 options: "first", "second"
Logic   presupposes $F \oplus S$
------  -----------------------------------------

# Not

------  -----------------------------------------
Phrase  I'm not doing nothing
Means   Nothing is what I am doing
Logic   $N$
Means   There is no action that I am doing
Logic   $\nexists s \;.;\; D(a)$
------  -----------------------------------------

------  -----------------------------------------
Phrase  I'm not doing anything
Means   Anything is not what I am doing
Logic   $\lnot A$
Means   There is no action that I am doing
Logic   $\nexists s \;.;\; D(a)$
------  -----------------------------------------

# When

------  -----------------------------------------
Phrase  I love it **when** it rains
Means   "raining" and "not loving it" cannot both be true
Logic   $R \rightarrow L$
------  -----------------------------------------

------  -----------------------------------------
Phrase  It unlocks **when** you turn the key
Means   "unlocking" and "turning key" either both happen or neither does
Logic   $R \leftrightarrow L$
------  -----------------------------------------

# If

------  -----------------------------------------
Phrase  **If** a number ends with 0, it is even
Means   "ends in 0" and "not even" cannot both be true
Logic   $Z \rightarrow E$
------  -----------------------------------------

------  -----------------------------------------
Phrase  **If** you propose, I'll marry you

Means   "you propose" and "I'll marry" are either both true or neither is

Logic   $P \leftrightarrow M$

Note    Implies neither married nor proposed-to yet: $\lnot P \land \lnot M$;\
        Also implies proposed-to will precede marriage, but "precede" is better handled by a temporal logic, not the first-order logic we use in this class
------  -----------------------------------------

# Is

------  -----------------------------------------
Phrase  3 **is** an integer
Means   "is 3" and "is not an integer" cannot both be true
Logic   $T \rightarrow I$
Math    $3 \in \mathbb Z$
------  -----------------------------------------

------  -----------------------------------------
Phrase  Alan Turing **is** the most famous computer scientist
Means   "Alan Turing" and "the most famous computer scientist" are synonyms
Logic   $A \leftrightarrow M$
------  -----------------------------------------

------  -----------------------------------------
Phrase  Alan Turing **is** dead
Means   "is Alan Turing" and "is not dead" cannot be true of the same person
Logic   $A \rightarrow D$
Means   "is Alan Turing" and "is not dead" cannot be true of the same person since 1954
Logic   $(y > 1954) \rightarrow (A \rightarrow D)$
------  -----------------------------------------

# All

------  -----------------------------------------
Phrase  There's a shirt that fits **all** of us
Means   Pick any one of us you want; that one can fit in the shirt
Logic   $\exists$ shirt . $\forall$ people in set "us" . shirt fits person
------  -----------------------------------------

------  -----------------------------------------
Phrase  There's a bus that fits **all** of us
Means   You can put us all in the bus at the same time
Logic   $\exists$ bus . bus fits the set "us"
------  -----------------------------------------

# Each

------  -----------------------------------------
Phrase  There's a shirt that fits **each** of us
Means   Pick any one of us you want; that one can find at least one of the shirts that fits
Logic   $\forall$ people in set "us" . $\exists$ shirt . shirt fits person
------  -----------------------------------------

------  -----------------------------------------
Phrase  There's a bus that fits **each** of us
Means   Pick any one of us you want; that one can fit in the bus
Logic   $\exists$ bus . $\forall$ people in set "us" . bus fits person
------  -----------------------------------------

# Every

------  -----------------------------------------
Phrase  I love the beak of **every** bird
Means   Pick any bird beak you want; I love that beak
Logic   $\forall b \in B \;.\; L(b)$
------  -----------------------------------------

------  -----------------------------------------
Phrase  I love the commander of **every** soldier
Means   There's a person who commands all soldiers, and I love that person
Logic   $\exists p \in P \;.\; \forall s \in S \;.\; C(p,s) \land L(p)$
------  -----------------------------------------

------  -----------------------------------------
Phrase  I've met the author of **every** good book
Means   A book's only good if I've met the person who wrote it
Logic   $\forall a \in A, b \in B\;.\; W(a,b) \rightarrow \big( G(b) \rightarrow M(a) \big)$
------  -----------------------------------------

