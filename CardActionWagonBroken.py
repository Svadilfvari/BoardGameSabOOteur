from CardAction import *

#broken wagon
class CardActionWagonBroken(CardAction):

    def __init__(self):
        super().__init__("Broken Wagon")


    #method used when the card is activated
    def cardActivated(self,targetedPlayerName,game):
        rank = game.name2rank(targetedPlayerName)
        if rank == -1:
            return False

        game.playerList[rank].toolKit[2] = False
        return True


    #makes a card displayable
    def addToGUI(self, ligne1, ligne2, ligne3):
        ligne1 += "(   )"
        ligne2 += "(WB )"
        ligne3 += "(   )"