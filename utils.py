suits = ["C", "D", "H", "S"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

reverse_card_trans = {0: '2C', 40: '3C', 28: '4C', 16: '5C', 4: '6C', 44: '7C', 32: '8C', 20: '9C', 8: '10C', 48: 'JC', 36: 'QC', 24: 'KC', 12: 'AC', 13: '2D', 1: '3D', 41: '4D', 29: '5D', 17: '6D', 5: '7D', 45: '8D', 33: '9D', 21: '10D', 9: 'JD', 49: 'QD', 37: 'KD',
                      25: 'AD', 26: '2H', 14: '3H', 2: '4H', 42: '5H', 30: '6H', 18: '7H', 6: '8H', 46: '9H', 34: '10H', 22: 'JH', 10: 'QH', 50: 'KH', 38: 'AH', 39: '2S', 27: '3S', 15: '4S', 3: '5S', 43: '6S', 31: '7S', 19: '8S', 7: '9S', 47: '10S', 35: 'JS', 23: 'QS', 11: 'KS', 51: 'AS'}

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

def val_to_str(val):
    if (val == "J"):
        return "Jack"
    elif (val == "Q"):
        return "Queen"
    elif (val == "K"):
        return "King"
    elif (val == "A"):
        return "Ace"
    else:
        return str(val)

def suit_to_string(suit):
    if (suit == "C"):
        return "Club"
    elif (suit == "D"):
        return "Diamond"
    elif (suit == "H"):
        return "Heart"
    else:
        return "Spade"

def pretty_print_int_card(card_int : int, end = "\n"):
    (val, suit) = (cards[card_int % 13], suits[card_int % 4])
    print(f"{val_to_str(val)} of {suit_to_string(suit)}s", end=end)

def pretty_print_str_card(card_str : str, end = "\n"):
    (val, suit) = (card_str[:-1], card_str[-1])
    print(f"{val_to_str(val)} of {suit_to_string(suit)}s", end=end)

def print_str_hand(hand : list[str]):
    for i in hand:
        pretty_print_str_card(i)

def print_int_hand(hand : list[int]):
    for i in hand:
        pretty_print_int_card(i)

def mod_hand(mod_class, hand):
    return [a % mod_class for a in hand]

def hand_to_number_hand(hand: list[str]) -> list[int]:
    return [cards_trans[x] for x in hand]

def hand_to_card_hand(hand: list[int]) -> list[str]:
    return [reverse_card_trans[x] for x in hand]
