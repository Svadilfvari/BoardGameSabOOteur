import CardActionLight 
import CardActionPike 
import CardActionWagon 
import CardActionLightBroken
import CardActionPikeBroken 
import CardActionWagonBroken 
import CardActionRockFall 
import CardActionSecretPlan  
import CardGalleryEnd 
import CardGalleryEW 
import CardGalleryNE 
import CardGalleryES 
import CardGalleryE 
import CardGalleryN 
import CardGalleryNEWS 
import CardGalleryStart 
import CardGalleryEWS 
import CardGalleryNES 
import CardGalleryNS 
import CardGalleryVoid

import random

#class definition
class GameBoard:

    #constructor
    def __init__(self):

        self.dimX = 9
        self.dimY = 5
        self.mine = []
        self.deck = []
        self.discard = []
        self.nbRound = 0
        self.currentPlayerNb = -1

        #void table initialisation
        for i in range(self.dimX):
            self.mine.append([])

            for j in range(self.dimY):
                self.mine[i].append(CardGalleryVoid.CardGalleryVoid())

        #setup goals and starting point
        self.poseCard(CardGalleryStart.CardGalleryStart(), 0, 2)

        randomizeGoal = [False, False, True]
        random.shuffle(randomizeGoal)

        self.poseCard(CardGalleryEnd.CardGalleryEnd(randomizeGoal[0]), self.dimX-1, 0)
        self.poseCard(CardGalleryEnd.CardGalleryEnd(randomizeGoal[1]), self.dimX-1, int(self.dimY/2))
        self.poseCard(CardGalleryEnd.CardGalleryEnd(randomizeGoal[2]), self.dimX-1, self.dimY-1)

        #setup the deck
        for i in range(6):
            self.deck.append(CardGalleryNEWS.CardGalleryNEWS())
            self.deck.append(CardGalleryEWS.CardGalleryEWS())
            self.deck.append(CardGalleryNES.CardGalleryNES())
            self.deck.append(CardGalleryNE.CardGalleryNE())
            self.deck.append(CardActionSecretPlan.CardActionSecretPlan())

        for i in range(5):
            self.deck.append(CardGalleryNS.CardGalleryNS())
            self.deck.append(CardGalleryES.CardGalleryES())

        for i in range(4):
            self.deck.append(CardGalleryEW.CardGalleryEW())

        for i in range(3):
            self.deck.append(CardActionLight.CardActionLight())
            self.deck.append(CardActionPike.CardActionPike())
            self.deck.append(CardActionWagon.CardActionWagon())
            self.deck.append(CardActionLightBroken.CardActionLightBroken())
            self.deck.append(CardActionPikeBroken.CardActionPikeBroken())
            self.deck.append(CardActionWagonBroken.CardActionWagonBroken())
            self.deck.append(CardActionRockFall.CardActionRockFall())

        self.deck.append(CardGalleryN.CardGalleryN())
        self.deck.append(CardGalleryE.CardGalleryE())
    
        random.shuffle(self.deck)


    #place a card the board
    def poseCard(self, selectedCard, x, y):

        if not(selectedCard.poseOk(x, y, self)):
            return -1

        # cases when we have to extend the map to place the card

        #on right
        if x == self.dimX:

            self.dimX += 1
            self.mine.append([])

            for j in range(self.dimY):
                self.mine[x].append(CardGalleryVoid.CardGalleryVoid())  

        #on left
        if x == -1:

            self.dimX += 1
            self.mine.append([])

            for j in range(self.dimY):
                self.mine[self.dimX-1].append(CardGalleryVoid.CardGalleryVoid())

            for j in range(self.dimY):
                for i in range(self.dimX):
                    self.mine[self.dimX-1-i][j] = self.mine[self.dimX-2-i][j]

            for j in range(self.dimY):
                self.mine[0][j] = CardGalleryVoid.CardGalleryVoid()

            x = 0

        #at the bottom
        if y == self.dimY:

            self.dimY += 1

            for i in range(self.dimX):
                self.mine[i].append(CardGalleryVoid.CardGalleryVoid())

        #at the top
        if y == -1:

            self.dimY += 1

            for i in range(self.dimX):
                self.mine[i].append(CardGalleryVoid.CardGalleryVoid())

            for i in range(self.dimX):
                for j in range((self.dimY)):
                    self.mine[i][self.dimY-1-j] = self.mine[i][self.dimY-2-j]

            for i in range(self.dimX):
                self.mine[i][0] = CardGalleryVoid.CardGalleryVoid()

            y = 0

        self.mine[x][y] = selectedCard


    #display map
    def printMine(self):

        #outline of the game board
        ligne0 = "Current mine state:"
        print(ligne0)
        
        ligne0 = " |"
        for i in range(self.dimX):
            ligne0 += "  " + str(i) + "  "
        print(ligne0)

        ligne0 = "-+"
        for i in range(self.dimX):
            ligne0 += "-----"
        ligne0 += "+-"
        print(ligne0)

        #retrieves the display of the cards on each line, then displays the all line
        for j in range(self.dimY):

            ligne1 = ""
            ligne2 = ""
            ligne3 = ""

            l1 = list(ligne1)
            l2 = list(ligne2)
            l3 = list(ligne3)

            for i in range(self.dimX):
                self.mine[i][j].addToGUI(l1,l2,l3)

            ligne1 = " |"
            ligne2 = str(j) + "|"
            ligne3 = " |"

            ligne1 += "".join(l1)
            ligne2 += "".join(l2)
            ligne3 += "".join(l3)

            ligne1 += "|"
            ligne2 += "|" + str(j)
            ligne3 += "|"

            print(ligne1)
            print(ligne2)
            print(ligne3)

        ligne0 = "-+"
        for i in range(self.dimX):
            ligne0 += "-----"
        ligne0 += "+-"
        print(ligne0)

        ligne0 = " |"
        for i in range(self.dimX):
            ligne0 += "  " + str(i) + "  "
        print(ligne0)


    #check if the deck is empty
    def checkDeck(self):
        if len(self.discard) == 0 and len(self.deck) == 0:      #if it is and there are no more cards in the discard, the wreckers win
            return True
        elif len(self.discard) != 0 and len(self.deck) == 0:    #otherwise, the discard pile is shuffled into the deck
            self.deck = self.discard
            self.discard = []
            random.shuffle(self.deck)
        return False


    #deletes the drawn card from the deck
    def aCardHasBeenDrawn(self):
        newDeck = []

        for i in range(len(self.deck)-1) :
            newDeck.append(self.deck[i+1])
        
        self.deck = newDeck


    #check if a goal has been reached
    def checkWin(self):

        for j in range(self.dimY):
            for i in range(self.dimX):
                if self.mine[i][j].cardName == "End":
                    if i < self.dimX-1:
                        
                        if self.mine[i+1][j].cardName != "Void" :  
                            self.mine[i][j].cardName = "EndB"                         
                            if self.mine[i][j].isGoal:              #if it is but it is not the treasure it will be displayed with a zero
                                return True

                    if self.mine[i-1][j].cardName != "Void" :
                        self.mine[i][j].cardName = "EndB"
                        if self.mine[i][j].isGoal:
                            return True
                        
                    if j < self.dimY-1:
                        if self.mine[i][j+1].cardName != "Void" :
                            self.mine[i][j].cardName = "EndB"
                            if self.mine[i][j].isGoal:
                                return True

                    if j > 0:
                        if self.mine[i][j-1].cardName != "Void" :
                            self.mine[i][j].cardName = "EndB"
                            if self.mine[i][j].isGoal:
                                return True
        return False