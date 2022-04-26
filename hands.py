from typing import Tuple

from utils import mod_hand

def flush(hand : list[int]) -> int:
    """
    Determines if a hand has a flush 
    Assumes hand sorted and modded 4

    Return: suit key (int) or -1 if not a flush
    """
    [i,j,k,l,m] = hand

    if (i == j == k == l == m):
        return i
    else:
        -1

def straight(hand : list[int]) -> int:
    """
    Determines if a hand has a straight
    Assumes hand sorted and modded 13

    Return: straight high card key (int) or -1 if not a straight
    """
    [i, j, k, l, m] = hand

    if (i + 4 == j + 3 == k + 2 == l + 1 == m) or ((i + 3 == j + 2 == k + 1 == l) and ()):
        return m
    else:
        return -1

def four_of_a_kind(hand: list[int]) -> Tuple[int, int]:
    """
    Determines if a hand has a four of a kind
    Assumes hand sorted and modded 13

    Return: (four of a kind key, other key) (int, int) or (-1, -1) if not a four of a kind
    """
    [i, j, k, l, m] = hand

    if (i == j == k == l):
        return (i, m)
    elif (j == k == l == m):
        return (j, i)
    else:
        return (-1, -1)

def full_house(hand: list[int]) -> Tuple[int, int]:
    """
    Determines if a hand has a full house
    Assumes hand sorted and modded 13

    Return: full house keys (a,b) a full of b (int, int) or (-1, -1) if not a full house
    """
    [i, j, k, l, m] = hand

    if (i == j) and (k == l == m):
        return (k,i)
    elif (i == j == k) and (l == m):
        return (i, l)
    else:
        return (-1,-1)

def three_of_a_kind(hand: list[int]) -> Tuple[int, int, int]:
    """
    Determines if a hand has a three of a kind
    Assumes hand sorted and modded 13

    Return: (a,b,c) such that 3 a's, b > c or (-1, -1, -1) if not a a 3 of a kind
    """
    [i, j, k, l, m] = hand

    if (i == j == k):
        return (i, m, l)
    if (j == k == l):
        return (j, m, i)
    if (k == l == m):
        return (k, j, i)
    else:
        return (-1, -1, -1)

def two_pair(hand: list[int]) -> Tuple[int, int, int]:
    """
    Determines if a hand has a two pair
    Assumes hand sorted and modded 13

    Return: (a,b,c) 2 a's, 2 b's; a > b, c = high card or (-1, -1) if not a 2 pair
    """
    [i, j, k, l, m] = hand

    if (i == j):
        if (k == l):
            return (k, i, m)
        elif (l == m):
            return (l, i, k)
        else:
            return (-1,-1,-1)
    elif (j == k) and (l == m):
        return (l, j, i)
    else:
        return (-1, -1, -1)

def pair(hand: list[int]) -> Tuple[int, int, int, int]:
    """
    Determines if a hand has a pair
    Assumes hand sorted and modded 13

    Return: (a,b,c,d) 2 a's, b > c > d or (-1, -1, -1, -1) if not a pair
    """
    [i, j, k, l, m] = hand

    if i == j:
        return (i, m, l, k)
    if j == k:
        return (j, m, l, i)
    if k == l:
        return (k, m, j, i)
    if l == m:
        return (l, k, j, i)
    return (-1, -1, -1, -1)

# TODO: Can likely reduce size of return int. Requires further investigation
def RankHand(hand: list[int]) -> int:
    """
    Returns the "value" of the hand, high => better hand

    Assume hand received in non-modded, unsorted form
    """
    # Sort the hand
    hand.sort()
    mod4_hand = mod_hand(4, hand)
    mod4_hand.sort()
    mod13_hand = mod_hand(13, hand)
    mod13_hand.sort()

    # Check Straight Flush
    # -- First check flush
    suit_key = flush(mod4_hand)
    if (suit_key != -1):
        # -- Second check straight
        straight_key = straight(mod13_hand)
        if (straight_key != -1):
            # -- Third verify strength
            # Strength = highest card = straight_key
            # << 30 for straight flush, | straight key so A > K > ... > 2
            return (1 << 30) | straight_key

    # Check Four of a kind
    (four_key, other) = four_of_a_kind(mod13_hand)
    if (four_key != -1):
        # << 29 for four of a kind
        return (1 << 29) | (four_key << 4) | other

    # Check full house (where 3 a's, 2 b's)
    (a, b) = full_house(mod13_hand)
    if (a != -1):
        # << 28 for full house
        return (1 << 28) | (a << 4) | b

    # Check Flush
    # Re-use old suit_key logic from above TODO Condense possibly? flush => !four && !full
    if (suit_key != -1):
        # We now need the highest cards so | in reverse order
        # << 27 for flush
        return (1 << 27) | (mod13_hand[4] << 16) | (mod13_hand[3] << 12) | (mod13_hand[2] << 8) | (mod13_hand[1] << 4) | (mod13_hand[0])

    # Check Straight
    high_key = straight(mod13_hand)
    if (high_key != -1):
        return (1 << 26) | high_key

    # Check Three of a kind (3 a's, b > c)
    (a, b, c) = three_of_a_kind(mod13_hand)
    if (a != -1):
        return (1 << 25) | b << 4 | c

    # Check two-pair (2 a's, 2 b's, c; a > b)
    (a, b, c) = two_pair(mod13_hand)
    if (a != -1):
        return (1 << 24) | a << 8 | b << 4 | c

    # Check pair (2 a's, b, c, d; b > c > d)
    (a, b, c, d) = pair(mod13_hand)
    if (a != -1):
        return (1 << 23) | a << 12 | b << 8 | c << 4 | d

    # Check high card/default case
    [e, d, c, b, a] = hand
    return (a << 16) | (b << 12) | (c << 8) | (d << 4) | e

def CompareHands(handA, handB) -> bool:
    """
    Takes 2 hands 'a' and 'b'
    Returns true if 'a' is better than 'b' and would win
    False otherwise
    """
    return RankHand(handA) > RankHand(handB)