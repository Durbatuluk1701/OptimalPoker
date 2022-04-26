from typing import List, Tuple


def flush(hand : List[int][5]) -> int:
    """
    Determines if a hand has a flush 
    Assumes hand sorted and modded!

    Return: suit key (int) or -1 if not a flush
    """
    [i,j,k,l,m] = hand

    if (i == j == k == l == m):
        return i
    else:
        -1

def straight(hand : List[int][5]) -> int:
    """
    Determines if a hand has a straight
    Assumes hand sorted and modded

    Return: straight high card key (int) or -1 if not a straight
    """
    [i, j, k, l, m] = hand

    if (i + 4 == j + 3 == k + 2 == l + 1 == m) or ((i + 3 == j + 2 == k + 1 == l) and ()):
        return m
    else:
        return -1

def four_of_a_kind(hand: List[int][5]) -> Tuple[int, int]:
    """
    Determines if a hand has a four of a kind
    Assumes hand sorted and modded

    Return: (four of a kind key, other key) (int, int) or (-1, -1) if not a four of a kind
    """
    [i, j, k, l, m] = hand

    if (i == j == k == l):
        return (i, m)
    elif (j == k == l == m):
        return (j, i)
    else:
        return (-1, -1)

def full_house(hand: List[int][5]) -> Tuple[int, int]:
    """
    Determines if a hand has a full house
    Assumes hand sorted and modded

    Return: full house keys (a,b) a full of b (int, int) or (-1, -1) if not a full house
    """
    [i, j, k, l, m] = hand

    if (i == j) and (k == l == m):
        return (k,i)
    elif (i == j == k) and (l == m):
        return (i, l)
    else:
        return (-1,-1)

def three_of_a_kind(hand: List[int][5]) -> Tuple[int, int, int]:
    """
    Determines if a hand has a three of a kind
    Assumes hand sorted and modded

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

def two_pair(hand: List[int][5]) -> Tuple[int, int, int]:
    """
    Determines if a hand has a two pair
    Assumes hand sorted and modded

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

def pair(hand: List[int][5]) -> Tuple[int, int, int, int]:
    """
    Determines if a hand has a pair
    Assumes hand sorted and modded

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
