---
topic: English ambiguities
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
Phrase  **If** a number ends with 0, it is an even
Means   "ends in 0" and "not even" cannot both be true
Logic   $Z \rightarrow E$
------  -----------------------------------------

------  -----------------------------------------
Phrase  **If** you propose, I'll marry you
Means   "you propose" and "I'll marry" are either both true or neither is
Logic   $P \leftrightarrow M$
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
Means   "is Alan Turing" and "is not dead" cannot be true of the same person at this time
Logic   $T \rightarrow (A \rightarrow D)$
------  -----------------------------------------
