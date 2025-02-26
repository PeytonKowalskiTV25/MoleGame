from PyUI.Screen import Screen
from PyUI.PageElements import *
from BuiltScreen import Enemy
from datetime import datetime, timedelta

class GameScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (181,26,58))
        self.state = {
            "status": "Game Started"
        }
        self.enemiesClicked = 0
        self.enemies = [self.createEnemy(), self.createEnemy(), self.createEnemy()]
        self.startTime = datetime.now()
        self.timeLimit = timedelta(seconds=30)

    def createEnemy(self):
        return Enemy(self.removeEnemy)
    
    def removeEnemy(self, enemy):
        self.enemies.remove(enemy)
        self.enemies.append(self.createEnemy())
        self.enemiesClicked += 1
        
    
    def elementsToDisplay(self):
        elapsedTime = datetime.now() - self.startTime
        remainingTime = self.timeLimit - elapsedTime
        self.elements = [
            Label((300, 0), 100, 100, "Gaming Time", 14, (0,0,0)),
            Label((200, 0), 100, 100, f"Kills: {self.enemiesClicked}", 14, (0,0,0)),
            Label((400, 0), 100, 100, f"Time: {remainingTime.seconds}", 14, (0,0,0))
        ] + self.enemies
        if remainingTime.seconds <= 0 or remainingTime.seconds > 30:
            self.state["status"] = "Game Over"