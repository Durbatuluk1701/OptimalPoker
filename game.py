import random

from hands import DecodeHand, RankHand
from utils import clear_screen, pretty_print_hand_array

DEBUG = True

HOUSE_FORM = "~~~~~~~\t\t{}\t\t~~~~~~~"

class Game:
    def __init__(self, numberOfPlayers : int):
        if numberOfPlayers < 2:
            raise Exception("Require at least 2 players")
        self.numberOfPlayers = numberOfPlayers
        self.playerRange = range(self.numberOfPlayers)
        self.Shuffle()
        self.ResetHands()
        self.house : list[int] = []
        self.pot = 0
        self.current_bet = 0
        # Default dealer to player 0
        self.dealer = 0
        self.playerPurses = { i : 0 for i in self.playerRange }
        self.playerStakes = { i : 0 for i in self.playerRange }
    def Reset(self):
        self.house = []
        self.pot = 0
        self.current_bet = 0
        self.playerStakes = { i : 0 for i in self.playerRange}
        self.ResetHands()
        self.Shuffle()
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
    def Card_Flop(self):
        # Flop the first 3 cards
        self.house.append(self.deck.pop())
        self.house.append(self.deck.pop())
        self.house.append(self.deck.pop())
    def Card_Run(self):
        # Run the 4th card
        self.house.append(self.deck.pop())
    def Card_River(self):
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
            if DEBUG:
                print(f"Player {playerNum} Best Hand Val: {playerBestHand[playerNum]}")
            if playerBestHand[playerNum][0] > handCode:
                bestPlayer, (handCode, bestHand) = playerNum, playerBestHand[playerNum]
        return (bestPlayer, handCode, bestHand)
    
    def ProcessBet(self, playerNum : int) -> int:
        """
        Processes a bet for player "playerNum"
        Automatically withdraws from purse and adds to pot
        Return values (-1 = Fold, 0 = Call, 1 = Raise)
        """
        while True:
            try:
                bet = input(f"Player {playerNum} Bet (F to Fold): ")
                if (bet.upper() == "F" or bet.upper() == "FOLD"):
                    # self.FoldPlayer(playerNum)
                    return -1
                betAmount = int(bet)
                if (betAmount < self.current_bet):
                    # They are trying to bet under current call
                    # 1. They have insufficent funds so must go all-in
                    # 2. They must fold
                    if (self.playerPurses[playerNum] == betAmount):
                        # They are going all in
                        # TODO because of this we neeed to be able to pay side pots
                        self.playerPurses[playerNum] -= betAmount
                        self.pot += betAmount
                        return 0
                    else:
                        print(f"Invalid bet, must call current bet '{self.current_bet}' to stay in")
                elif (self.playerPurses[playerNum] >= betAmount):
                    self.playerPurses[playerNum] -= betAmount
                    self.pot += betAmount
                    if (betAmount == self.current_bet):
                        # It was a call
                        return 0
                    else:
                        # it was a raise
                        self.current_bet = betAmount
                        return 1
                else:
                    print("Invalid Bet, insufficient funds in purse")
            except ValueError:
                print("Please input a valid bet as an integer")

    def FoldPlayer(self, playerNum : int):
        raise Exception("TODO")

    def CollectAllBets(self):
        # TODO make betting order proper, make sure calls occur
        betQueue = [i for i in self.playerRange]
        # Keep going until everyone has done betting
        while len(betQueue) > 0:
            # Want to pop in front order
            playerNum = betQueue.pop(0)
            self.ShowPot()
            self.ShowHouse()
            self.ShowHand(playerNum)
            self.ShowPlayerPurse(playerNum)
            playerAction = self.ProcessBet(playerNum)
            if (playerAction == -1):
                self.FoldPlayer(playerNum)
            elif (playerAction == 0):
                # Call - no appending needed
                pass
            elif (playerAction == 1):
                # Raised, must append all the old players to re-bet
                tempQueue = [i for i in self.playerRange]
                tempQueue = tempQueue[:tempQueue.index(playerNum)]
                betQueue = betQueue + tempQueue
            else:
                raise Exception("How")
            # Keep info hidden? idk
            # clear_screen()
            pass
    def ShowPlayerPurse(self, playerNum : int):
        print(f"Player {playerNum} Purse: {self.playerPurses[playerNum]}")
    def ShowPot(self):
        print(HOUSE_FORM.format(f"Pot: {self.pot}"))
    def ShowHouse(self):
        print("House: ", end="")
        pretty_print_hand_array(self.house)
    def ShowHand(self, playerNum : int):
        print(f"Player {playerNum} Hand: ", end="")
        pretty_print_hand_array(self.hands[playerNum])


    def BankruptPlayer(self, playerNum : int):
        # When player "playerNum" goes bankrupt, the show must go on
        raise Exception("TODO")
    def Run_Game(self, buyIn : int):
        # Set all purses to default buy in
        self.playerPurses = { i : buyIn for i in self.playerRange }
        # Start-up a game
        while True:
            self.Reset()
            # TODO: Collect and assign blinds
            self.DealHands()
            # Process first betting
            self.CollectAllBets()
            print(HOUSE_FORM.format("FLOP"))
            self.Card_Flop()
            self.CollectAllBets()
            print(HOUSE_FORM.format("RUN"))
            self.Card_Run()
            self.CollectAllBets()
            print(HOUSE_FORM.format("RIVER"))
            self.Card_River()
            self.CollectAllBets()
            (wPlayer, wHandVal, wHand) = self.PickWinner()
            print(HOUSE_FORM.format("WINNERS!"))
            print(f"Player {wPlayer} Won with: {DecodeHand(wHandVal)}")
            # TODO Transfer money
            playAgain = input("Play Again (y/n): ")
            if (playAgain.upper() == "N"):
                return
            clear_screen()

game = Game(2)
game.Run_Game(100)