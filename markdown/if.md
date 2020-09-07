---
title: "If" and Logic
...

"If" and related words are used in many logical and beyond-logic ways. This writeup is an effort to explore them.

# If

## If it rains, I'll get wet

Logical part
:   $R \rightarrow W$
    
     Raining?       Wet?            Consistent with phrase?
    -------------- --------------  -------------------------
    No              No              Yes
    No              Yes             Yes
    Yes             No              No
    Yes             Yes             Yes
    
Beyond logic
:   There's a temporal implication (rain starts shortly before wetness) which propositional logic cannot encode.
    
    There's a causal implication (rain creates the wetness) which propositional logic cannot encode.


## If you earn 93% or more, you get an A

Logical part
:   $E \leftrightarrow A$
    
     Earned 93?     Get A?          Consistent with phrase?
    -------------- --------------  -------------------------
    No              No              Yes
    No              Yes             No
    Yes             No              No
    Yes             Yes             Yes
    
Beyond logic
:   There's a temporal implication (93% precedes A) which propositional logic cannot encode.
    
    The $\leftarrow$ part is "fuzzy": a 92.8% might get an A, but a 81% won't.
    The $\rightarrow$ part is implicitly "or more": an A+ would not be a problem.
    Propositional logic cannot encode this "fuzz".

## This program crashes it you type Ctrl+Q

Logical part
:   $C \leftarrow Q$

     It crashes?    Ctrl+Q?         Consistent with phrase?
    -------------- --------------- -------------------------
    No              No              Yes
    No              Yes             No
    Yes             No              Yes
    Yes             Yes             Yes

Beyond logic
:   This one is close to just logic. ☺


# When

## I love it when it rains

Logical part
:   $L \leftarrow R$

     I love it?     It rains?       Consistent with phrase?
    -------------- --------------- -------------------------
    No              No              Yes
    No              Yes             No
    Yes             No              Yes
    Yes             Yes             Yes

Beyond logic
:   "When" implies that the truth of $R$ comes and goes.
    It also implies that rain *will* happen;
    "if" in this phrase would have the same *logical* meaning,
    but would imply doubt that rain would ever occur.


## I sing when in the shower

Logical part
:   $\top$

     I sing?        Showering?      Consistent with phrase?
    -------------- --------------- -------------------------
    No              No              Yes
    No              Yes             Yes
    Yes             No              Yes
    Yes             Yes             Yes

Beyond logic
:   This means that there exist some times when I am both in the shower and singing, but does not rule out either singing outside the shower nor that I might have some in-shower time when I'm not singing.
    We can encode that with first-order logic (i.e. $\exist t \;.\; S(t) \land H(t)$) but not with just propositional logic.


# Only

## It only rains at night

Logical part
:   $R \rightarrow N$

     It rains?      It's night?     Consistent with phrase?
    -------------- --------------- -------------------------
    No              No              Yes
    No              Yes             Yes
    Yes             No              No
    Yes             Yes             Yes

Beyond logic
:   This one is close to just logic. ☺


## I only love my spouse

Logical part
:   $L \leftrightarrow S$

     I love it?     It's my spouse?     Consistent with phrase?
    -------------- ------------------- -------------------------
    No              No                  Yes
    No              Yes                 No
    Yes             No                  No
    Yes             Yes                 Yes

Beyond logic
:   The use of "only" implies "love" means something more specific than it would in a phrase like "I love cake" and possibly more specific than even "I love my spouse".




