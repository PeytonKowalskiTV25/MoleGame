from PyUI.Screen import Screen
from BuiltScreen import StartButton, QuitButton
from PyUI.PageElements import Label

class StartScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (181,26,58))
        self.state = {
            "status": "Welcome"
        }

    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((300, 200), 100, 100, self.state["status"], 14, (0,0,0)), #dynamic element needs arguments
            StartButton(),
            QuitButton(400, 200)
        ]