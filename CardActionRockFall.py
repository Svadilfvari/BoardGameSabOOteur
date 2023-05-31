from CardAction import *
from CardGalleryVoid import *

class CardActionRockFall(CardAction):

    def __init__(self):
        super().__init__("Rock Fall")


    #method used when the card is activated
    def cardActivated(self, x, y, gameBoard):
        targetedCardName = gameBoard.mine[x][y].cardName
        if targetedCardName == "End" or targetedCardName == "Start" or targetedCardName == "Void":
            return False
        gameBoard.poseCard(CardGalleryVoid(), x, y)


    #makes a card displayable
    def addToGUI(self, ligne1, ligne2, ligne3):
        ligne1 += "(   )"
        ligne2 += "(RoF)"
        ligne3 += "(   )"
