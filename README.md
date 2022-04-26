# OptimalPoker
Poker related code, not really sure yet

## Steps

### Step 1: Create a Poker Hand Ranker
- Assign a numeric encoding to each card
    - Ideas for this: if card is "x", need x % 4 = suit (0 -> club, 1 -> diamond, 2 -> heart, 3 -> spade), and x % 13 = card value (0 -> 2, ... 8->10, 9->J, 10 -> Q, 11 -> K, 12 -> A)
- Create a five best card evaluator that takes a hand (5 cards) -> integer value representing strength (this seems rather difficult but cool if possible)
    - Fleshing out some more, we have 5 cards, __a__, __b__, __c__, __d__, __e__. 
    - *a* could be any of 52, *b* could be any of 51, *c* any of 50, *d* any of 49, *e* any of 48 so a total of 52 x 51 x 50 x 49 x 48 possible hands or 311875200 = 52 **p** 5 = 52!/47!
    - But since ordering of the hand does not actually matter, let us assume that we use combinations instead 52 **c** 5 = 52! / (5! * 47!) = 2598960 hands
        - We will ensure this is a steady ordering by making sure __a__ < __b__ < ... < __e__
    - With only roughly 2.6 million possible outputs each hand can be assigned a value from 0 to 2598960 showing its value.
    - Even less if you account for the fact that some hands are considered equal
- Ranker will just take hands **x** vs **y**, calculate integer value for **x** and **y** and then compare.
<details>
<summary> Step 1 Details </summary>

### Step 1.1: Unique Numeric Card Encodings
Calculate using the Chinese Remainder Theorem
Output stored in card_trans.csv

Rather than perform this calculation everytime, we will just store this in a statically defined variable to save computation time.

### Step 1.2: Best 5 Card Evaluator
For every part below, assume the hand is [a,b,c,d,e]
Assume \fch = \forall cards in hand
We will need to check in descending order if the following exist:
- Straight Flush
    - First Check Flush == True : \fch c % 4 == x (so all suits must match)
    - Second Check Straight == True : 
        - Method to verify a straight: 
        [a,b,c,d,e] % 13 -> [i,j,k,l,m] sort that -> [q,r,s,t,u] then compare [q, q+1, q+2,q+3,q+4] to [q,r,s,t,u]. If true then it is straight, else it is not (Exception for A low straight [q, q+1, q+2, q+3, q+12])
    - Third Check : Verify strength
        - Take the top card from the straight to represent hand strength
        - (Optional maybe suit as back-up???)
- Four of a Kind
    - Check if 4 parts of the hand match [a,a,a,a,b] or [b,a,a,a,a]
    - Compare to other hands by comparing 'a' then 'b'
- Full House
    - Check if 3 of a kind and a pair exist
- Flush
    - Reference above flush method
- Straight
    - Reference above straight method
- Three of a Kind
    - Check if [a,a,a,c,b] or [c,a,a,a,b] or [c,b,a,a,a]
    - Compare by 'a', then 'c', then 'c'
- Two Pair
    - Check if [b,b,a,a,c] or [b,b,c,a,a] or [c,b,b,a,a]
    - Compare by 'a' then 'b' then 'c'
- Pair
    - Check if [a,a,d,c,b] or [d,a,a,c,b] or [d,c,a,a,b] or [d,c,b,a,a]
    - Compare by 'a' then 'b', then 'c', then 'd'
- High Card
    - Hand is already sorted so [e,d,c,b,a]
    - Compare by a, b, c, d, e

The number returned will be formatted as such
- (1 << 30) | Hand_Encoding
- Left-Shift 30 for 9 types of hand + 20 = 5*4 where bin(13) = 1101 = 4 bits
</details>

### Step 2: Create a actual Poker Game
- Model this as a python class with the following features
    - Deal/Reset Hands
    - Shuffle the Deck
    - Flop, Run, River
    - Calculate Winner
    - Restart
    - Start
    - Bet per turn (later)
