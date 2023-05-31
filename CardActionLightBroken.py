from CardAction import *

#broken light
class CardActionLightBroken(CardAction):

    def __init__(self):
        super().__init__("Broken Light")


    #method used when the card is activated
    def cardActivated(self,targetedPlayerName,game):
        rank = game.name2rank(targetedPlayerName)
        if rank == -1:
            return False

        game.playerList[rank].toolKit[0] = False
        return True


    #makes a card displayable
    def addToGUI(self, ligne1, ligne2, ligne3):
        ligne1 += "(   )"
        ligne2 += "(LiB)"
        ligne3 += "(   )"