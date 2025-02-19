from PyUI.Screen import Screen
from PyUI.PageElements import Label
from BuiltScreen import QuitButton

class EndScreen(Screen):
    def __init__(self, window, kills):
        super().__init__(window, (0,0,0))
        self.state = {
            "status": "Game Over"
        }
        self.kills = kills

    def elementsToDisplay(self):
        self.elements = [
            Label((300, 200), 100, 100, "Game Over", 14, (255,255,255)),
            Label((300, 250), 100, 100, f"Total Kills: {self.kills}", 14, (255,255,255)),
            QuitButton(300, 800)
        ]