import os

class ControllerTournoi:
    
    def __init__(self):
        self.name = "ControllerTournoi"

    def gestionTournoi(self, message = ""):
        os.system("cls")
        choix = input("Veillez faire un choix : ")
        match choix:
            case "1":
                print("Créer un tournoi")
            case "2":
                print("Modifier un tournoi")
            case "3":
                print("Supprimer un tournoi")
            case "4":
                print("Afficher les tournois")
            case "5":
                print("Afficher un tournoi")
            case "6":
                print("Lancer un tournoi")
            case "7":
                print("Retour au menu principal")
            case _:
                print("Veuillez faire un choix valide")

