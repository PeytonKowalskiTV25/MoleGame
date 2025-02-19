from PyUI.Window import Window
from GameScreen import GameScreen
from startScreen import StartScreen
from EndScreen import EndScreen
from GameScreen import enemiesClicked


window = Window("Start Screen", (0,255,0)) ##Create the window to work with

##Create Screen Objects for use------
startScreen = StartScreen(window)
gameScreen = GameScreen(window)
endScreen = EndScreen(window, enemiesClicked)
##-----------------------------------

screen = startScreen ##set screen to be the starting screen

while True: ##Game loop
    ##Enter code here to handle changes between screens---
    if screen.state["status"] == "Game Started":
        # window = Window("Game Screen", (0,255,0))
        screen = gameScreen

    if screen.state["status"] == "Game Over":
        # window = Window("End Screen", (0,255,0))
        screen =  endScreen


    ##----------------------------------------------------

    window.checkForInput(screen) #checks for inputs on the screen
    screen.update() #updates the screen
    window.update(screen) #updates the window to reflect the new screen
