import os


class ControllerRapport(object):

    def __init__(self):
        self.name = "ControllerRapport"
        os.system("cls")

    def gestionRapport(self, message = ""):
        self.view.gestionRapport()
        choix = input("Veillez faire un choix : ")
        match choix:
            case "1":
                print("Rapport de tournoi")
            case "2":
                print("Rapport de joueur")
            case "3":
                print("Rapport de round")
            case "4":
                print("Rapport de match")
            case "5":
                self.app.accueil()
            case _:
                self.gestionRapport("Veuillez faire un choix valide !")
