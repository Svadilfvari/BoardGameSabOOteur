from CardAction import *

#broken pike
class CardActionPikeBroken(CardAction):

    def __init__(self):
        super().__init__("Broken Pike")


    #method used when the card is activated
    def cardActivated(self,targetedPlayerName,game):
        rank = game.name2rank(targetedPlayerName)
        if rank == -1:
            return False

        game.playerList[rank].toolKit[1] = False
        return True


    #makes a card displayable
    def addToGUI(self, ligne1, ligne2, ligne3):
        ligne1 += "(   )"
        ligne2 += "(PB )"
        ligne3 += "(   )"