from typing import List


cards_trans = {
    "2C": 0,
    "3C": 40,
    "4C": 28,
    "5C": 16,
    "6C": 4,
    "7C": 44,
    "8C": 32,
    "9C": 20,
    "10C": 8,
    "JC": 48,
    "QC": 36,
    "KC": 24,
    "AC": 12,
    "2D": 13,
    "3D": 1,
    "4D": 41,
    "5D": 29,
    "6D": 17,
    "7D": 5,
    "8D": 45,
    "9D": 33,
    "10D": 21,
    "JD": 9,
    "QD": 49,
    "KD": 37,
    "AD": 25,
    "2H": 26,
    "3H": 14,
    "4H": 2,
    "5H": 42,
    "6H": 30,
    "7H": 18,
    "8H": 6,
    "9H": 46,
    "10H": 34,
    "JH": 22,
    "QH": 10,
    "KH": 50,
    "AH": 38,
    "2S": 39,
    "3S": 27,
    "4S": 15,
    "5S": 3,
    "6S": 43,
    "7S": 31,
    "8S": 19,
    "9S": 7,
    "10S": 47,
    "JS": 35,
    "QS": 23,
    "KS": 11,
    "AS": 51,
}

nested_card_trans = {
    "C": {
        "2": 0,
        "3": 40,
        "4": 28,
        "5": 16,
        "6": 4,
        "7": 44,
        "8": 32,
        "9": 20,
        "10": 8,
        "J": 48,
        "Q": 36,
        "K": 24,
        "A": 12
    },
    "D": {
        "2": 13,
        "3": 1,
        "4": 41,
        "5": 29,
        "6": 17,
        "7": 5,
        "8": 45,
        "9": 33,
        "10": 21,
        "J": 9,
        "Q": 49,
        "K": 37,
        "A": 25
    },
    "H": {
        "2": 26,
        "3": 14,
        "4": 2,
        "5": 42,
        "6": 30,
        "7": 18,
        "8": 6,
        "9": 46,
        "10": 34,
        "J": 22,
        "Q": 10,
        "K": 50,
        "A": 38
    },
    "S": {
        "2": 39,
        "3": 27,
        "4": 15,
        "5": 3,
        "6": 43,
        "7": 31,
        "8": 19,
        "9": 7,
        "10": 47,
        "J": 35,
        "Q": 23,
        "K": 11,
        "A": 51,
    }
}

def RankHand(hand : List[str][5]):
    # Sort the hand
    hand.sort()
    