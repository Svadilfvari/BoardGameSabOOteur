from Card import *

#action
class CardAction(Card):

    def __init__(self, cardName):
        super().__init__("Action", cardName)



    def reverse(self):
        pass    #an action can'b be reversed