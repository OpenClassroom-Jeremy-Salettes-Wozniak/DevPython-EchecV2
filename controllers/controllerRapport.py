# Authors: Jérémy Salettes-Wozniak 

# VIEWS
from views.viewRapport import ViewRapport

# EXTERNAL LIBRARIES
import os

class ControllerRapport(object):

    def __init__(self):
        self.name = "ControllerRapport"
        self.view = ViewRapport()

    def gestionRapport(self, message = ""):
        """
            Méthode permettant de gérer le menu de gestion des rapports.

            Paramètres :
            ------------
            message : str
                Message à afficher en cas d'erreur
        """
        # Nettoyage de la console
        os.system("cls")

        # Affichage du menu de gestion des rapports
        self.view.gestionRapport()

        # Logique de gestion du menu
        choix_valide = False
        while not choix_valide:
            # Choix de l'utilisateur
            choix = input("Veillez faire un choix : ")
            # Vérification de la validité du choix
            if choix in ["1", "2", "3", "4", "5"]:
                # Si choix est valide on renvoie la méthode correspondante
                choix_valide = True

                # Si choix "1" : Rapport de tournoi
                if choix == "1":
                    self.rapportTournoi()
                # Si choix "2" : Rapport de joueur
                elif choix == "2":
                    self.rapportJoueur()
                # Si choix "3" : Rapport de round
                elif choix == "3":
                    self.rapportRound()
                # Si choix "4" : Rapport de match
                elif choix == "4":
                    self.rapportMatch()
                # Si choix "5" : Menu principal
                elif choix == "5":
                    return False
            else:
                self.gestionRapport("Veuillez faire un choix valide !")
        return True

    def rapportTournoi(self):
        pass

    def rapportJoueur(self):
        pass

    def rapportRound(self):
        pass

    def rapportMatch(self):
        pass
