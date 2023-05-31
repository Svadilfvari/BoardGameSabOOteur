from Player import *
import GameBoard

import random


class SabOOteur:

    def __init__(self, numberOfPlayers):

        self.gameBoard = GameBoard.GameBoard()
        self.playerList = []
        self.goldDeck = []
        self.numberOfPlayers = numberOfPlayers
        self.numberOfGames = 0
        self.nbC = 0
        self.nbS = 0
        self.playerHandLength = 0

        for i in range(4):
            self.goldDeck.append(3)
        for j in range(8):
            self.goldDeck.append(2)
        for k in range(16):
            self.goldDeck.append(1)
        random.shuffle(self.goldDeck)

        if self.numberOfPlayers == 3:
            self.nbS = 1
            self.nbC = 2
            self.playerHandLength = 6

        if self.numberOfPlayers == 4:
            self.nbS = 1
            self.nbC = 3
            self.playerHandLength = 6

        if self.numberOfPlayers == 5:
            self.nbS = 2
            self.nbC = 3
            self.playerHandLength = 6

        if self.numberOfPlayers == 6:
            self.nbS = 2
            self.nbC = 4
            self.playerHandLength = 5

        if self.numberOfPlayers == 7:
            self.nbS = 3
            self.nbC = 4
            self.playerHandLength = 5

        if self.numberOfPlayers == 8:
            self.nbS = 3
            self.nbC = 5
            self.playerHandLength = 4

        if self.numberOfPlayers == 9:
            self.nbS = 3
            self.nbC = 6
            self.playerHandLength = 4

        if self.numberOfPlayers == 10:
            self.nbS = 3
            self.nbC = 7
            self.playerHandLength = 4
        
    def addPlayer(self, playerName):
        self.playerList.append(Player(playerName, self.playerHandLength))


    def name2rank(self,playerName):
        for i in range(len(self.playerList)):
            if self.playerList[i].playerName == playerName:
                return i
        print("Player name not found")
        return -1

    def randomizeRole(self):
        randomizeRole = []

        for i in range(self.nbS):
            randomizeRole.append("Wrecker")

        for i in range(self.nbC):
            randomizeRole.append("Miner")

        random.shuffle(randomizeRole)

        for i in range(self.numberOfPlayers):
            self.playerList[i].role = randomizeRole[i]

    def startGame(self):

        self.gameBoard = GameBoard.GameBoard()
        self.randomizeRole()
        
        for player in self.playerList:
            for i in range(self.playerHandLength):
                player.drawAcard(i,self.gameBoard)
    
    def goldRefresh(self, n):
        newGoldDeck = []
        for i in range(len(self.goldDeck)-n):
            newGoldDeck.append(self.goldDeck[n+i])
        self.goldDeck = newGoldDeck
        

        

