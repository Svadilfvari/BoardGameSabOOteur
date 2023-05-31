from GameBoard import *
from Card import *
from Player import *
import SabOOteur


def welcome():

    global sabOOteur

    while(True):

        print("\n===== Welcome to SabOOteur ! =====\n")
        print("How many players are we ? \n")

        nbPlayers = 0

        while (int(nbPlayers) < 3 or int(nbPlayers) > 10):
            nbPlayers = input("Number of players (between 3 and 10) : ")

            if len(nbPlayers) == 2:
                if ord(nbPlayers[0]) == 49 and ord(nbPlayers[1]) == 48:
                    nbPlayers = int(nbPlayers)

            elif (ord(nbPlayers) >= 48 and ord(nbPlayers) <= 57) or ord(nbPlayers):
                nbPlayers = int(nbPlayers)

            sabOOteur = SabOOteur.SabOOteur(nbPlayers)

        print("\nWhat are the names of the players?")

        while len(sabOOteur.playerList) < nbPlayers :

            pName = input(f"Player #{len(sabOOteur.playerList)+1} : ")

            if len(sabOOteur.playerList) == 0 :
                sabOOteur.addPlayer(pName)

            else :
                alreadyExist = 0
                for player in sabOOteur.playerList:

                    if player.playerName == pName:

                        print("! This name is already used !")
                        alreadyExist = 1
                        break

                if not(alreadyExist):
                    sabOOteur.addPlayer(pName)

        print("\nThe game is about to start")

        for i in range(3):

            winC, winS = play()

            if winS :
                print("\n! Wreckers has won !")
                print("\n === Gold distriution ===\n")

                n = 0
                for player in sabOOteur.playerList:
                    if player.role == "Wrecker":
                        player.goldPouch += sabOOteur.goldDeck[n]
                        print(f"{player.playerName} has won {sabOOteur.goldDeck[n]} gold")
                        n =+ 1

                sabOOteur.goldRefresh(n)
        
            if winC :
                print("\n! Searchers has won !")
                print("\n=== Gold distriution ===\n")

                n = 0
                for player in sabOOteur.playerList:
                    if player.role == "Miner":
                        player.goldPouch += sabOOteur.goldDeck[n]
                        print(f"{player.playerName} has won {sabOOteur.goldDeck[n]} gold")
                        n =+ 1

                sabOOteur.goldRefresh(n)
        print("\n! The game is over !\n")
        
        winer = sabOOteur.playerList[0]

        for player in sabOOteur.playerList :
            if player.goldPouch > winer.goldPouch:
                winer = player
        
        print(f"!!! {winer.playerName} has won with {winer.goldPouch} gold found !!!")



def play():

    sabOOteur.numberOfGames += 1

    print("\n=== Randomizing roles ===\n")
    print(f"This is the game #{sabOOteur.numberOfGames} !\n")
    
    sabOOteur.startGame()

    winS = False
    winC = False

    while not(winS) and not(winC):

        sabOOteur.gameBoard.nbRound += 1
        sabOOteur.gameBoard.currentPlayerNb += 1
        sabOOteur.gameBoard.currentPlayerNb = sabOOteur.gameBoard.currentPlayerNb % sabOOteur.numberOfPlayers

        print(f"\n=== Round #{sabOOteur.gameBoard.nbRound} ===\n")

        sabOOteur.gameBoard.printMine()

        print(f"\nThis is {sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].playerName}'s turn")
        print(f"Role : {sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].role}")

        sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].printToolKit()
        
        choice = "a"

        while ord(choice[0]) != 49 and ord(choice[0]) != 50:

            print("\n")
            sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].printPlayerHand()
            print("\n")

            hasPlayed = False

            while not(hasPlayed):

                print("0 -> reverse à card")
                print("1 -> play a card")
                print("2 -> pass my turn \n")
        
                choice = input("Choice ( 0 | 1 | 2 ) : ")

                if int(choice[0]) == 0:
                    hasPlayed = reverseAcard()
        
                if int(choice[0]) == 2:
                    hasPlayed = passTurn()

                if int(choice[0]) == 1 :
                    hasPlayed = playAcard()

        winC = sabOOteur.gameBoard.checkWin()
        winS = sabOOteur.gameBoard.checkDeck()
    
    return winC,winS



def askCard():
    choice = "a"

    while ord(choice) < 49 or ord(choice) > 48 + sabOOteur.playerHandLength:
        choice = input("Chose a valid card : ")
    choice = int(choice)-1

    return choice



def reverseAcard():

    print("\nYou've decided to reverse a card")
    choice = askCard()

    sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].playerHand[choice].reverse()

    return True



def playAcard():

    print("\nYou've decided to play a card")

    choice = askCard()
    selectedCard = sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].playerHand[choice]
    toolKit = sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].toolKit

    if selectedCard.cardType == "Gallery" and toolKit[0] and toolKit[1] and toolKit[2]:
        x = int(input("x : "))
        y = int(input("y : "))
        selectedCard.cardActivated(x,y,sabOOteur.gameBoard)
        sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].drawAcard(choice,sabOOteur.gameBoard)
        return True

    elif selectedCard.cardType == "Gallery" and not(toolKit[0] and toolKit[1] and toolKit[2]):
        print("\n! One of your tools is broken !\n")
        return False

    elif selectedCard.cardType == "Action":

        Cname = selectedCard.cardName

        if Cname == "Pike" or Cname == "Broken Pike" or Cname == "Light" or Cname == "Broken Light" or Cname == "Wagon" or Cname == "Broken Wagon":
            ok = False
            while not(ok):
                targetedPlayerName = input("Targeted player : ")
                for player in sabOOteur.playerList :
                    if player.playerName == targetedPlayerName:
                        ok = True
            selectedCard.cardActivated(targetedPlayerName,sabOOteur)

        elif Cname == "Rock Fall":

            print("Choose a valid card to destroy")
            x = int(input("x : "))
            y = int(input("y : "))
            targetedCardName = sabOOteur.gameBoard.mine[x][y].cardName
            selectedCard.cardActivated(x,y,sabOOteur.gameBoard)

            if targetedCardName == "End" or targetedCardName == "Start" or targetedCardName == "EndB" or targetedCardName == "Void":
                print("\n! You can destroy this card !\n")
                return False
            sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].drawAcard(choice,sabOOteur.gameBoard)
            return True

        elif Cname == "Secret Plan":
            targetedCardName = ""
            while targetedCardName != "End":
                print("Choose a goal to reveal")
                x = int(input("x : "))
                y = int(input("y : "))
                targetedCardName = sabOOteur.gameBoard.mine[x][y].cardName
            if sabOOteur.gameBoard.mine[x][y].isGoal :
                print("! You founded the treasure !")
            else :
                print("It is not the treasure :(")
        sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].drawAcard(choice,sabOOteur.gameBoard)
        return True



def passTurn():

    print("\nYou must discard a card")
    choice = askCard()

    sabOOteur.playerList[sabOOteur.gameBoard.currentPlayerNb].drawAcard(choice,sabOOteur.gameBoard)

    return True