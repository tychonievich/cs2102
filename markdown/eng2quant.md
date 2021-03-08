---
title: English to Quantifiers
...

This page was based on a lecture from Spring 2020.

----------  -----------------------
   domain:  people
   $H(x)$:  $x$ is happy
   $C(x)$:  $x$ is in this class
 $A(x,y)$:  $x$ appreciates $y$
      $t$:  Luther Tychonievich
----------  -----------------------

Everyone is happy
:   $\forall x \;.\; H(x)$

Everyone in this class is happy
:   $\forall x \;.\; C(x) \rightarrow H(x)$

    Note that $\forall x \;.\; C(x) \land H(x)$ is wrong: it is only satisfied if every person is in the class and every person is happy.

Someone is happy
:   $\exists x \;.\; H(x)$

Someone in this class is happy
:   $\exists x \;.\; C(x) \land H(x)$

    Note that $\exists x \;.\; C(x) \rightarrow H(x)$ is wrong: it is satisfied if anyone is not in the class (happy or not), or anyone is happy (in the class or not).

Not everyone is happy
:   $\lnot \forall x \;.\; H(x)$
    
    See also the next sentence, which is equivalent to this.
    If done properly, any equivalent sentence in English translates into a logically equivalent predicate logic formula.

Someone is unhappy
:   $\exists x \;.\; \lnot H(x)$
    
    See also the previous sentence, which is equivalent to this.
    
    Sometimes it is important to distinguish between "unhappy" and "not happy", which can be different if there is a neither-happy-nor-unhappy state. We'll generally not deal with that nuance in this class.

Only one person is happy
:   This can be handled several ways:
    
    Someone is happy, and everyone other than them is unhappy
    :   $$\exists x \;.\; H(x) \land \forall y\;.\; \big((x \neq y) \rightarrow \lnot H(y)\big)$$
        
        Because $\forall$ is a bunch of "and"s, and "and" is commutative, we can commute the quantifiers over the and:
        
        $$\exists x \;.\; \forall y\;.\;  H(x) \land \big((x \neq y) \rightarrow \lnot H(y)\big)$$
        
        We cannot commute $\forall$ over operators other than $\land$ or over $\exists$ quantifiers.
        For example $\forall y\;.\; \exists x \;.\; H(x) \land \big((x \neq y) \rightarrow \lnot H(y)\big)$ means "Pick anyone you want and I can find someone who is happy such that either my person is your person or your person is unhappy"; this is trivially true because I can always pick the same person you picked.
    
    If two people are both happy, they are the same person
    :   $\forall x, y \;.\; \big(H(x) \land H(y)\big) \rightarrow (x = y)$
        
        Note that we commonly combine quantifiers of the same kind, and can commute them; the above is equivalent to both of the following:
        
        $$\forall x \;.\; \forall y \;.\; \big(H(x) \land H(y)\big) \rightarrow (x = y)$$

        $$\forall y \;.\; \forall x \;.\; \big(H(x) \land H(y)\big) \rightarrow (x = y)$$
        
        Note this does not include the claim "at least one person is happy"; we could add that with
        
        $\Big(\exists z \;.\; H(z)\Big) \land \Big(\forall x, y \;.\; \big(H(x) \land H(y)\big) \rightarrow (x = y)\Big)$

    If two people are distinct, at least one is unhappy
    :   $$\forall x, y \;.\; (x \neq y) \rightarrow \big(\lnot H(x) \lor \lnot H(y)\big)$$
        
        Like the previous, this does not include "at lease one person is happy" but that can be added

Only one person in this class is happy
:   Also has several forms
    
    Someone in the class is happy, and everyone in the class other than them is unhappy
    :   $$\exists x \;.\; \big(C(x) \land H(x)\big) \land \Big(\forall y \;.\; \big(C(y) \land (x \neq y)\big) \rightarrow \lnot H(y)\Big)$$
        
        Again, we can commute the $\forall y$ over the $\land$: $$\exists x \;.\; \forall y \;.\; \big(C(x) \land H(x)\big) \land \Big(\big(C(y) \land (x \neq y)\big) \rightarrow \lnot H(y)\Big)$$
    
    If two people are both in the class and both happy, they are the same person
    :   $$\forall x, y \;.\; \big(C(x) \land C(y) \land H(x) \land H(y)\big) \rightarrow (x = y)$$
        
Everyone appreciates someone
:   For everyone, there is someone they appreciate:
    
    $$\forall x \;.\; \exists y \;.\; A(x,y)$$
    
    Note again we cannot commute the different quantifiers across each other. $\exists y \;.\; \forall x \;.\; A(x,y)$ means "there is someone that everyone appreciates".


Everyone appreciates someone else
:   For everyone, there is someone (not them) that they appreciate:
    
    $$\forall x \;.\; \exists y \;.\; (x \neq y) \land A(x,y)$$
    

Everyone appreciates someone who appreciates them
:   There is ambiguity in the English: is this an observation that among those we each appreciate is someone who reciprocates that appreciation; or is it a universal rule that everyone reciprocates all appreciation?

    For everyone, there is someone that they appreciate and appreciates them
    :   $$\forall x \;.\; \exists y \;.\; A(x,y) \land A(y,x)$$

    For everyone, they appreciate everyone who appreciates them
    :   $$\forall x, y \;.\; A(x,y) \rightarrow A(y,x)$$
        which can also be written
        $$\forall x, y \;.\; A(x,y) \leftrightarrow A(y,x)$$
    
Everyone appreciates someone else who appreciates them
:   For everyone, there is someone (not them) that they appreciate and appreciates them:
    
    $$\forall x \;.\; \exists y \;.\; (x \neq y) \land A(x,y) \land A(y,x)$$
    
    This also has the same ambiguity noted for the previous item, leading to

    $$\forall x, y \;.\; (x \neq y) \rightarrow \big(A(x,y) \leftrightarrow A(y,x)\big)$$

Everyone appreciates a person who appreciates them
:   There is ambiguity in this sentence, as with the two before.

    If "a person" means "everyone", we have
    
    $$\forall x, y \;.\; A(x,y) \rightarrow A(y,x)$$
    $$\forall x, y \;.\; A(x,y) \leftrightarrow A(y,x)$$
    
    If "a person" means "someone",  we have
    
    $$\forall x \;.\; \exists y \;.\; A(x,y) \land A(y,x)$$

Everyone in this class appreciates someone in this class
:   For everyone, if they are in the class then is someone who in this class and they appreciate them:
    
    $$\forall x \;.\; C(x) \rightarrow \big(\exists y \;.\; C(y) \land A(x,y)\big)$$
    $$\forall x \;.\; \exists y \;.\; C(x) \rightarrow \big(C(y) \land A(x,y)\big)$$

There's someone in this class that everyone in the class appreciates
:   $$\exists x \;.\; C(x) \land \big(\forall y \;.\; C(y) \rightarrow A(x,y)\big)$$
    $$\exists x \;.\; \forall y \;.\; C(x) \land \big(C(y) \rightarrow A(x,y)\big)$$

Those in this class only appreciate people in this class
:   There are several ways to go:

    For anyone, if you are in the class then for anyone, if they are not in the class you don't appreciate them
    :    $$\forall x \;.\; C(x) \rightarrow \big(\forall y \;.\; \lnot C(y) \rightarrow \lnot A(x,y)\big)$$
         $$\forall x \;.\; \forall y \;.\; C(x) \rightarrow \big(\lnot C(y) \rightarrow \lnot A(x,y)\big)$$
    
    For any two people, if one appreciates the other and one is in the class, so is the other
    :    $$\forall x,y \;.\; A(x,y) \rightarrow \big(C(x) \rightarrow C(y)\big)$$
    :    $$\forall x,y \;.\; \big(A(x,y) \land C(x)\big) \rightarrow C(y)$$

Tychonievich only appreciates those who appreciate someone in this class
:   There is an ambiguity in the English.
    Does it mean there is one special person in the class who you have to appreciate to get Tychonievich's appreciation, or that you may appreciate anyone in the class you wish?
    Let's look at one version for each:
    
    For anyone, if Tychonievich appreciates them then there is someone in the class they appreciate
    :   $$\forall x \;.\; A(t,x) \rightarrow \big(\exists y \;.\; C(y) \land A(x,y)\big)$$
        $$\forall x \;.\; \exists y \;.\; A(t,x) \rightarrow \big(C(y) \land A(x,y)\big)$$
    
    There's someone in the class such that anyone Tychonievich appreciates appreciates that person
    :   $$\exists y \;.\; C(y) \land \big(\forall x \;.\; A(t,x) \rightarrow A(x,y)\big)$$
        $$\exists y \;.\; \forall x \;.\; C(y) \land \big(A(t,x) \rightarrow A(x,y)\big)$$
    
