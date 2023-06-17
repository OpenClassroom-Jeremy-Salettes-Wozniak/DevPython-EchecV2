import os

class ViewRapport(object):

    def __init__(self):
        self.name = "ViewRapport"
        

    def gestionRapport(self, message = ""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de Rapport !")
        print("---------------- Tournoi ------------------")
        print("1 - Rapport de tournoi")
        print("2 - Rapport de joueur")
        print("3 - Rapport de round")
        print("4 - Rapport de match")
        print("5 - Menu principal")
        print("-------------------------------------------")
        if message != "":
            print(message)