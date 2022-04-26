import random

from hands import RankHand

class Game:
    def __init__(self, numberOfPlayers : int):
        self.numberOfPlayers = numberOfPlayers
        self.playerRange = range(self.numberOfPlayers)
        self.Shuffle()
        self.ResetHands()
        self.house : list[int] = []
    def ResetHands(self):
        self.hands : dict[int, list[int]] = {i: [] for i in self.playerRange}
    def Shuffle(self):
        self.deck = [i for i in range(52)]
        random.shuffle(self.deck)
    def DealHands(self):
        # Deal first card
        for i in self.playerRange:
            self.hands[i].append(self.deck.pop())
        # Deal second card
        for i in self.playerRange:
            self.hands[i].append(self.deck.pop())
    def Flop(self):
        # Flop the first 3 cards
        self.house.append(self.deck.pop())
        self.house.append(self.deck.pop())
        self.house.append(self.deck.pop())
    def Run(self):
        # Run the 4th card
        self.house.append(self.deck.pop())
    def River(self):
        # River the 5th card
        self.house.append(self.deck.pop())
    def GenBest5_Set(self, best7 : list[int]) -> set[tuple[int,int,int,int,int]]:
        genSet : set[tuple[int,int,int,int,int]] = set()
        for i in range(7):
            for j in range(i + 1, 7):
                for k in range(j + 1, 7):
                    for l in range(k + 1, 7):
                        for m in range(l + 1, 7):
                            genSet.add(tuple([best7[i],
                                              best7[j],
                                              best7[k],
                                              best7[l],
                                              best7[m]]))
        return genSet

    def PickWinner(self) -> tuple[int, int, list[int]]:
        # For each of the hands, we need to calculate the best possible hand
        # 7 cards, choose 5 so 7 c 5 -> 7! / 5!*2! -> 21 choices per player
        playerHandCombos : dict[int, set[tuple[int,int,int,int,int]]]= {
            i : set() for i in self.playerRange
        }
        for playerNum in self.playerRange:
            best_7_cards = self.hands[playerNum] + self.house
            playerHandCombos[playerNum] = self.GenBest5_Set(best_7_cards)
        playerBestHand : dict[int, tuple[int, list[int]]] = {
            i : (0,[]) for i in self.playerRange
        }
        # Foreach player, pick best hand they could make
        for playerNum in self.playerRange:
            for hand in playerHandCombos[playerNum]:
                handVal = RankHand(list(hand))
                # If hand is better than previous best, set as best
                if handVal > playerBestHand[playerNum][0]:
                    playerBestHand[playerNum] = (handVal, list(hand))
        # Pick best overall player's hand
        bestPlayer, handCode, bestHand = -1, -1, []
        for playerNum in self.playerRange:
            if playerBestHand[playerNum][0] > bestPlayer:
                bestPlayer, (handCode, bestHand) = playerNum, playerBestHand[playerNum]
        return (bestPlayer, handCode, bestHand)
