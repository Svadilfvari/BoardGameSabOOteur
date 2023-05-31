from GameBoard import *
from Card import *
from Player import *
import SabOOteur

import random

from tkinter import * 
from tkinter.ttk import *
from tkinter.messagebox import *

def setNbPlayersTo3():
    global nbPlayers
    nbPlayers = 3
    creating_new_game_to_creating_players()

def setNbPlayersTo4():
    global nbPlayers
    nbPlayers = 4
    creating_new_game_to_creating_players()

def setNbPlayersTo5():
    global nbPlayers
    nbPlayers = 5
    creating_new_game_to_creating_players()

def setNbPlayersTo6():
    global nbPlayers
    nbPlayers = 6
    creating_new_game_to_creating_players()

def setNbPlayersTo7():
    global nbPlayers
    nbPlayers = 7
    creating_new_game_to_creating_players()

def setNbPlayersTo8():
    global nbPlayers
    nbPlayers = 8
    creating_new_game_to_creating_players()

def setNbPlayersTo9():
    global nbPlayers
    nbPlayers = 9
    creating_new_game_to_creating_players()

def setNbPlayersTo10():
    global nbPlayers
    nbPlayers = 10
    creating_new_game_to_creating_players()



def welcome():

    global window_welcome
    window_welcome = Tk()
    window_welcome.attributes('-fullscreen', True)

    saboBg = PhotoImage(file = "saboteurBG.png")
    limg = Label(window_welcome, i=saboBg)
    limg.place(x = 0, y = 0)

    Label(window_welcome, text="SabOOteurs").place(x = 1153, y = 200)

    Button(window_welcome, text="New Game", command=welcome_to_creating_new_game).place(x = 1150, y = 250)
    Button(window_welcome, text = "Quitt", command = window_welcome.destroy).place(x = 1150, y = 300)

    window_welcome.mainloop()



def welcome_to_creating_new_game():
    window_welcome.destroy()
    creating_new_game()

def creating_new_game_to_welcome():
    widow_creating_new_game.destroy()
    welcome()



def creating_new_game():
    global widow_creating_new_game
    widow_creating_new_game = Tk()
    widow_creating_new_game.attributes('-fullscreen', True)

    saboBg = PhotoImage(file = "saboteurBG.png")
    limg = Label(widow_creating_new_game, i = saboBg)
    limg.place(x = 0, y = 0)

    Label(widow_creating_new_game, text = "Creating new game").place(x = 1135, y = 200)
    Label(widow_creating_new_game, text = "How many players are we ?").place(x = 1114, y = 250)


    Button(widow_creating_new_game, text = "3", command = setNbPlayersTo3).place(x = 1150, y = 275)
    Button(widow_creating_new_game, text = "4", command = setNbPlayersTo4).place(x = 1150, y = 300)
    Button(widow_creating_new_game, text = "5", command = setNbPlayersTo5).place(x = 1150, y = 325)
    Button(widow_creating_new_game, text = "6", command = setNbPlayersTo6).place(x = 1150, y = 350)
    Button(widow_creating_new_game, text = "7", command = setNbPlayersTo7).place(x = 1150, y = 375)
    Button(widow_creating_new_game, text = "8", command = setNbPlayersTo8).place(x = 1150, y = 400)
    Button(widow_creating_new_game, text = "9", command = setNbPlayersTo9).place(x = 1150, y = 425)
    Button(widow_creating_new_game, text = "10", command = setNbPlayersTo10).place(x = 1150, y = 450)

    Button(widow_creating_new_game, text = "Cancel", command = creating_new_game_to_welcome).place(x = 1150, y = 550)

    widow_creating_new_game.mainloop()



def creating_new_game_to_creating_players():
    widow_creating_new_game.destroy()
    creating_players()

def creating_players_to_creating_new_game():
    widow_creating_players.destroy()
    creating_new_game()



def creating_players():

    global sabOOteur

    global widow_creating_players
    widow_creating_players = Tk()
    widow_creating_players.attributes('-fullscreen', True)

    saboBg = PhotoImage(file = "saboteurBG.png")
    limg = Label(widow_creating_players, i = saboBg)
    limg.place(x = 0, y = 0)    
    
    Label(widow_creating_players, text = "Creating players name").place(x = 1000, y = 200)
    Label(widow_creating_players, text = "Player #1 : ").place(x = 1000, y = 250)

    sabOOteur = SabOOteur.SabOOteur(nbPlayers)

    global Saisie
    Saisie = Entry(widow_creating_players)
    Saisie.place(x = 1000, y = 270)

    Button(widow_creating_players, text = "Create player", command = getPlayerName).place(x = 1000, y = 300)
    
    Button(widow_creating_players, text = "Cancel", command = creating_players_to_creating_new_game).place(x = 1000, y = 400)

    widow_creating_players.mainloop()



def getPlayerName():
    if len(sabOOteur.playerList) < nbPlayers:
        global playerName
        playerName = Saisie.get()
        for player in sabOOteur.playerList:
            if player.playerName == playerName:
                showwarning(title = ":(", message="This name is already used")
                return -1
        Label(widow_creating_players, text = "Player #" + str(len(sabOOteur.playerList) + 1) + " : " + playerName).place(x = 1200, y = 300-10*nbPlayers+20*len(sabOOteur.playerList))
        sabOOteur.addPlayer(playerName)
    if len(sabOOteur.playerList) < nbPlayers:
        Label(widow_creating_players, text = "Player #" + str(len(sabOOteur.playerList) + 1) + " : ").place(x = 1000, y = 250)
        
        

    if len(sabOOteur.playerList) == nbPlayers:
        Label(widow_creating_players, text = "Game's ready !").place(x = 1000, y = 350)
        Button(widow_creating_players, text = "PLAY", command = creating_players_to_lunch_game).place(x = 1000, y = 370)



def creating_players_to_lunch_game():
    widow_creating_players.destroy()
    lunch_game()

def lunch_game_to_creating_players():
    window_lunch_game.destroy()
    creating_players()





def show_roles():

    sabOOteur.randomizeRole()

    showinfo(message = "Role display")

    for i in range(nbPlayers):
        showwarning(message = "Click OK to see " + sabOOteur.playerList[i].playerName + "'s role")
        showinfo(message = sabOOteur.playerList[i].playerName + " is a " + sabOOteur.playerList[i].role)

    if askokcancel(message = "The game is about to start \n Click OK to continue"):
        creating_players_to_lunch_game()
    else:
        lunch_game_to_creating_players()



def displayCard(carte):
    if carte.cardName == "Start":
        pass



def lunch_game():
    global window_lunch_game
    window_lunch_game = Tk()
    window_lunch_game.attributes('-fullscreen', True)

    ### button allowing the player to play his turn ###

    for i in range(3):

        show_roles()

        winC, winS = play()
    
    window_lunch_game.mainloop()




def play():
    global window_lunch_game

    sabOOteur.numberOfGames += 1
    sabOOteur.startGame()

    winS = False
    winC = False

    while not(winS) and not(winC):

        ### display of the round number of the game number ###

        ### display of the mine in real time ###

        winC = sabOOteur.gameBoard.checkWin()
        winS = sabOOteur.gameBoard.checkDeck()

    return winC, winS

