# Authors: Jérémy Salettes-Wozniak 

# CONTROLLERS
from controllers.controllerMenu import ControllerMenu

class App:
    def __init__(self):
        self.name = "App"
        self.controller = ControllerMenu()   
        self.run()

    def run(self):
        self.controller.gestionAccueil()
        
if __name__ == "__main__":
    App()
