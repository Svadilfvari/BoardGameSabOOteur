from abc import ABC, abstractmethod

#abstract class definition
class Card(ABC):

    #constructor
    @abstractmethod
    def __init__(self, cardType, cardName):
        self.cardType = cardType
        self.cardName = cardName

    #toString
    def toString(self):
        return (self.cardType + " : " + self.cardName)
        