from GameBoard import *
from Card import *

from CardGalleryVoid import *

class Player:

    def __init__(self, playerName, handLength):
        self.role = ""
        self.playerName = playerName
        self.goldPouch = 0
        self.playerHand = [CardGalleryVoid] * handLength
        self.toolKit = [True,True,True]
        
    def toString(self):
        return "it's " + self.playerName + "'s turn and he/she is a (SPOILER Alert) " + self.role


    def printToolKit(self):
            res = "My toolkit -> Light : "
            if self.toolKit[0] : 
                res += "OK"
            else:
                res += "Broken"

            res += " | Pike : "
            if self.toolKit[1] : 
                res += "OK"
            else:
                res += "Broken"

            res += " | Wagon : "
            if self.toolKit[2] : 
                res += "OK"
            else:
                res += "Broken"

            print(res)

    def printPlayerHand(self):

        n = 1
        
        ligne1 = ""
        ligne2 = ""
        ligne3 = ""

        l1 = list(ligne1)
        l2 = list(ligne2)
        l3 = list(ligne3)

        for i in range(len(self.playerHand)):

            l1 += "   "
            l2 += " " + str(n) + ":"
            l3 += "   "

            n += 1

            self.playerHand[i].addToGUI(l1,l2,l3)

        ligne1 += "".join(l1)
        ligne2 += "".join(l2)
        ligne3 += "".join(l3)

        print(ligne1)
        print(ligne2)
        print(ligne3)

    def drawAcard(self, choice, gameBoard):

        # MESSAGE TO LEO /!\ I suppose that the deck is an array
        # the function choice returns a random element from the array deck

        gameBoard.discard.append(self.playerHand[choice])

        newCardFromDeck = gameBoard.deck[0]
        self.playerHand[choice] = newCardFromDeck

        gameBoard.aCardHasBeenDrawn()

        #supp la carte ajouter du deck (refaire la list sans la carte tirée)


























