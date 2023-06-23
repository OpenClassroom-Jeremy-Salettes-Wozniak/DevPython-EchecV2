# Authors: Jérémy Salettes-Wozniak 

# VIEWS: 
from views.viewTournoi import ViewTournoi

# EXTERNAL LIBRARIES
import os

class ControllerTournoi:
    
    def __init__(self):
        self.name = "ControllerTournoi"
        self.view = ViewTournoi()

    def gestionTournoi(self, message = ""):
        """
            Méthode permettant de gérer le menu de gestion des tournois.

            Paramètres :
            ------------
            message : str
                Message à afficher en cas d'erreur
        """

        # Nettoyage de la console
        os.system("cls")

        # Affichage du menu de gestion des tournois
        self.view.gestionTournoi(message)

        # Logique de gestion du menu
        choix_valide = False
        while not choix_valide:
            # Choix de l'utilisateur
            choix = input("Veillez faire un choix : ")
            # Vérification de la validité du choix
            if choix in ["1", "2", "3", "4", "5", "6", "7"]:
                # Si choix est valide on renvoie la méthode correspondante
                choix_valide = True
                # Si choix "1" : Créer un tournoi
                if choix == "1":
                    self.createTournoi()
                # Si choix "2" : Modifier un tournoi
                elif choix == "2":
                    self.updateTournoi()
                # Si choix "3" : Supprimer un tournoi
                elif choix == "3":
                    self.deleteTournoi()
                # Si choix "4" : Afficher les tournois
                elif choix == "4":
                    self.showTournois()
                # Si choix "5" : Afficher un tournoi
                elif choix == "5":
                    self.showTournoi()
                # Si choix "6" : Lancer un tournoi
                elif choix == "6":
                    self.launchTournoi()
                # Si choix "7" : Menu principal
                elif choix == "7":
                    return False
            else:
                self.gestionTournoi("Veuillez faire un choix valide !")
        return True

    def createTournoi(self):
        pass

    def updateTournoi(self):
        pass

    def deleteTournoi(self):
        pass

    def showTournois(self):
        pass
        
    def showTournoi(self):
        pass

    def launchTournoi(self):
        pass

