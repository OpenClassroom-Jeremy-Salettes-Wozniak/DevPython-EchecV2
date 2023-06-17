import os

class ViewTournoi(object):

    def __init__(self):
        self.name = "ViewTournoi"
        

    def gestionTournoi(self, message = ""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Tournoi ------------------")
        print("1 - Créer un tournoi")
        print("2 - Modifier un tournoi")
        print("3 - Supprimer un tournoi")
        print("4 - Afficher les tournois")
        print("5 - Afficher un tournoi")
        print("6 - Lancer un tournoi")
        print("7 - Menu principal")
        print("-------------------------------------------")
        if message != "":
            print(message)