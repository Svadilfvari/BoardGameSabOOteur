from CardAction import *

class CardActionSecretPlan(CardAction):

    def __init__(self):
        super().__init__("Secret Plan")


    #the card is activated directly on the interface or in text
    def cardActivated(self):
        pass


    #makes a card displayable
    def addToGUI(self, ligne1, ligne2, ligne3):
        ligne1 += "(   )"
        ligne2 += "(MAP)"
        ligne3 += "(   )"