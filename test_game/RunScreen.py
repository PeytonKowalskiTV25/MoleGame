from PyUI.Window import Window
from GameScreen import GameScreen
from startScreen import StartScreen
from EndScreen import EndScreen

window = Window("Start Screen", (0,255,0)) ##Create the window to work with

##Create Screen Objects for use------
startScreen = StartScreen(window)
gameScreen = GameScreen(window)
endScreen = None
##-----------------------------------

screen = startScreen ##set screen to be the starting screen

while True: ##Game loop
    ##Enter code here to handle changes between screens---
    if screen.state["status"] == "Game Started":
        screen = gameScreen

    if screen.state["status"] == "Game Over":
        enemiesClicked = gameScreen.enemiesClicked
        endScreen = EndScreen(window, enemiesClicked)
        screen = endScreen
        
    ##----------------------------------------------------

    window.checkForInput(screen) #checks for inputs on the screen
#    screen.update() #updates the screen
    window.update(screen) #updates the window to reflect the new screen
