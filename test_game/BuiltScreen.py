import sys
import pygame
from PyUI.Screen import Screen #will need a screen object to extend
from PyUI.PageElements import * #will need the base element classes to extend
from random import randint

##create the custom screen class
class ExampleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0)) ##use the parents constructor
        ##give the screen a state for updating values and labels----
        self.state = {
            "status": "onGoing"
        }
        ##----------------------------------------------------------

    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((300, 200), 100, 100, self.state["status"], 14, (255,255,255))
        ]
        

##Add custom page elements
class StartButton(Button):
    def __init__(self):
        super().__init__((400, 100), 100, 100, "Start")
    
    def onClick(self, screen):
        screen.state["status"] = "Game Started"

class QuitButton(Button):
    def __init__(self, xCoord, yCoord):
        super().__init__((xCoord, yCoord), 100, 100, "Quit")

    def onClick(self, screen):
        pygame.quit()
        sys.exit()   

class Enemy(Image):
    def __init__(self, removeEnemy):
        super().__init__((randint(0, 500), randint(0,500)), 100, 100, "./imgus/EvilMole.jpg")
        self.hp = 1
        self.removeEnemy = removeEnemy

    def isAlive(self):
        return self.hp > 0

    def takeDamage(self, damage):
        self.hp -= damage
    
    def onClick(self, screen):
        self.takeDamage(1)
        if not self.isAlive():
            self.removeEnemy(self)
