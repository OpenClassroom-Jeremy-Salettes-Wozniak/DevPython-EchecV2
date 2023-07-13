# Authors: Jérémy Salettes-Wozniak 

# VIEWS: 
from views.viewTournoi import ViewTournoi

# MODELS:
from models.tournois import Tournoi

# EXTERNAL LIBRARIES
import os
import re
class ControllerTournoi:
    
    def __init__(self):
        self.name = "ControllerTournoi"
        self.view = ViewTournoi()
        self.model = Tournoi

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
                # Si choix "4" : Lance ou re
                elif choix == "4":
                    self.launchTournoi()
                # Si choix "7" : Menu principal
                elif choix == "5":
                    return False
            else:
                self.gestionTournoi("Veuillez faire un choix valide !")
        return True

    def createTournoi(self):
        # Nettoyage de la console
        os.system("cls")

        # Tournoi dictionary
        tournoi = {}

        # Nom du tournoi
        choixNom = False
        tournoiNom = input(self.view.demandeTournoiNom())
        while not choixNom:
            # Regex texte
            if re.match("^[A-Za-z0-9 ]*$", tournoiNom):
                choixNom = True
                tournoi["nom"] = tournoiNom
            else:
                tournoiNom = input(self.view.erreurTournoiNom())

        # Lieu du tournoi
        choixLieu = False
        tournoiLieu = input(self.view.demandeTournoiLieu())
        while not choixLieu:
            # Regex Majuscule au début
            if re.match("^[A-Z][a-z]*$", tournoiLieu):
                choixLieu = True
                tournoi["lieu"] = tournoiLieu
            else:
                tournoiLieu = input(self.view.erreurTournoiLieu())

        # Nombre de rondes du tournoi
        choixNombreRondes = False
        tournoiNombreRondes = input(self.view.demandeTournoiNombreRondes())
        while not choixNombreRondes:
            # Regex nombre entier
            if re.match("^[0-9]*$", tournoiNombreRondes):
                choixNombreRondes = True
                tournoi["nombreRondes"] = tournoiNombreRondes
            else:
                tournoiNombreRondes = input(self.view.erreurTournoiNombreRondes())

        # Description du tournoi
        choixDescription = False
        tournoiDescription = input(self.view.demandeTournoiDescription())
        while not choixDescription:
            # Regex texte
            if re.match("^[A-Za-z0-9 ]*$", tournoiDescription):
                choixDescription = True
                tournoi["description"] = tournoiDescription
            else:
                tournoiDescription = input(self.view.erreurTournoiDescription())

        # Sauvegarde du tournoi
        newTournoi = self.model(
            tournoi_nom = tournoi["nom"],
            tournoi_lieu = tournoi["lieu"],
            tournoi_nb_round = tournoi["nombreRondes"],
            tournoi_description = tournoi["description"]
        )
        newTournoi.saveTournoi()
        

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

