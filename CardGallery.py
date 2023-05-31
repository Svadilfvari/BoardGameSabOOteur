from Card import *

#inheritance of the abstract class
class CardGallery(Card):
    
    #constructor
    def __init__(self, cardName, cN, cE, cW, cS):

        self.connectNorth = cN
        self.connectEast  = cE
        self.connectWest  = cW
        self.connectSouth = cS

        super().__init__("Gallery", cardName)



    #rotate a card
    def reverse(self):

        tempN = self.connectNorth
        tempE = self.connectEast

        self.connectNorth = self.connectSouth
        self.connectEast  = self.connectWest
        self.connectWest  = tempE
        self.connectSouth = tempN
    


    #makes a card displayable
    def addToGUI(self, ligne1, ligne2, ligne3):

        #case: there is no card
        if self.cardName == "Void":
            ligne1 += "     "
            ligne2 += "     "
            ligne3 += "     "

        #adapts the display according to the path
        else:
            ligne1 += "( | )" if self.connectNorth else "(   )"
            ligne3 += "( | )" if self.connectSouth else "(   )"
            ligne2 += "(-"    if self.connectWest else "( "
       
            
            if self.cardName == "EndB":
                ligne2 += "0"
            elif self.cardName == "End":
                ligne2 += "?"
            elif self.cardName == "Start":
                ligne2 += "S"
            elif (self.connectWest or self.connectEast) and (self.connectNorth or self.connectSouth):
                ligne2 += "+"
            elif self.connectWest and self.connectEast and not(self.connectNorth or self.connectSouth):
                ligne2 += "-"
            elif not(self.connectWest or self.connectEast) and self.connectNorth and self.connectSouth:
                ligne2 += "|"
            else:
                ligne2 += "x"

            ligne2 += "-)" if self.connectEast else " )"


    #check position
    def poseOk(self, x, y, game_board):

        if self.cardName == "Start" or self.cardName == "End" or self.cardName == "Void" or self.cardName == "EndB":
            return True

        if x < -2 or y < -2 or x > game_board.dimX + 1 or y > game_board.dimY + 1:
            print("This position is too far from the mine")
            return False

        if x>=0 and y>=0 and x<game_board.dimX and y<game_board.dimY:
            if not (game_board.mine[x][y].cardName == "Void"):
                print("This position is already occupied")
                return False

        if x < game_board.dimX-1:
            if self.connectEast and not(game_board.mine[x+1][y].connectWest) and not(game_board.mine[x+1][y].cardName == "Void"):
                print("Error: connection with a wall")
                return False

        if x>0:
            if self.connectWest and not(game_board.mine[x-1][y].connectEast) and not(game_board.mine[x-1][y].cardName == "Void"):
                print("Error: connection with a wall")
                return False
        
        if y<game_board.dimY-1:
            if self.connectSouth and not(game_board.mine[x][y+1].connectNorth) and not(game_board.mine[x][y+1].cardName == "Void"):
                print("Error: connection with a wall")
                return False

        if y>0:
            if self.connectNorth and not(game_board.mine[x][y-1].connectSouth) and not(game_board.mine[x][y-1].cardName == "Void"):
                print("Error: connection with a wall")
                return False

        if x<game_board.dimX-1:
            if self.connectEast and game_board.mine[x+1][y].connectWest:
                return True

        if x>0:
            if self.connectWest and game_board.mine[x-1][y].connectEast:
                return True
        
        if y<game_board.dimY-1:
            if self.connectSouth and game_board.mine[x][y+1].connectNorth:
                return True

        if y>0:
            if self.connectNorth and game_board.mine[x][y-1].connectSouth:
                return True

        print("Error : no connection possible")
        return False

    #method used when the card is activated
    def cardActivated(self,x,y,gameBoard):
        gameBoard.poseCard(self, x, y)
