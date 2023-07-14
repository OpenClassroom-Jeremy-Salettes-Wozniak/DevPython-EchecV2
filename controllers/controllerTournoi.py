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
        choixNomTournoi = False
        # Choix du nom du tournoi
        while not choixNomTournoi:
            # On demande le nom du tournoi à modifier
            nomTournoi = input(self.view.demandeTournoiNom())
            # On vérifie que le nom du tournoi existe
            if self.model.existeDansDB(self, nomTournoi) == True:
                # Si le nom du tournoi n'existe pas on affiche un message d'erreur
                print('Le nom du tournoi existe')
                choixNomTournoi = True
                #  Nettoyage de la console
                os.system("cls")
                # On affiche le menu de modification du tournoi
                self.view.updateTournoi()
                # Logique de gestion du menu
                choix_valide = False
                while not choix_valide:
                    # Choix de l'utilisateur
                    choix = input(self.view.demandeMenu())
                    # Vérification de la validité du choix
                    if choix in ["1", "2", "3", "4", "5", "6", "7"]:
                        # Si choix est valide on renvoie la méthode correspondante
                        choix_valide = True
                        # Si choix "1" : Modifier le nom du tournoi
                        if choix == "1":
                            choixNom = False
                            while not choixNom:
                                nomUpdate = input(self.view.demandeTournoiNom())
                                # Regex texte
                                if re.match("^[A-Za-z0-9 ]*$", nomTournoi):
                                    choixNom = True
                                    self.model.setNomTournoi(self, nomTournoi, nomUpdate)
                                    choix_valide = False
                                else:
                                    tournoiNom = input(self.view.erreurTournoiNom())
                        elif choix == "2":
                            choixLieu = False
                            while not choixLieu:
                                lieuUpdate = input(self.view.demandeTournoiLieu())
                                # Regex Majuscule au début
                                if re.match("^[A-Z][a-z]*$", lieuUpdate):
                                    choixLieu = True
                                    self.model.setLieuTournoi(self, nomTournoi, lieuUpdate)
                                    choix_valide = False
                                else:
                                    lieuUpdate = input(self.view.erreurTournoiLieu())
                        elif choix == "3":
                            choixNombreRondes = False
                            while not choixNombreRondes:
                                nombreRondesUpdate = input(self.view.demandeTournoiNombreRondes())
                                # Regex nombre entier
                                if re.match("^[0-9]*$", nombreRondesUpdate):
                                    choixNombreRondes = True
                                    self.model.setNombreRondesTournoi(self, nomTournoi, nombreRondesUpdate)
                                    choix_valide = False
                                else:
                                    nombreRondesUpdate = input(self.view.erreurTournoiNombreRondes())
                            
                        # Si choix "4" : Modifier la description du tournoi
                        elif choix == "4":
                            choixDescription = False
                            while not choixDescription:
                                descriptionUpdate = input(self.view.demandeTournoiDescription())
                                # Regex texte
                                if re.match("^[A-Za-z0-9 ]*$", descriptionUpdate):
                                    choixDescription = True
                                    self.model.setDescriptionTournoi(self, nomTournoi, descriptionUpdate)
                                    choix_valide = False
                                else:
                                    descriptionUpdate = input(self.view.erreurTournoiDescription())
                        elif choix == "5":
                            choix_valide = False
                    else:
                        self.gestionTournoi("Veuillez faire un choix valide !")
            else:
                choixNomTournoi = False
                
    def deleteTournoi(self):
        choixNomTournoi = False

        while not choixNomTournoi:
            choixNomTournoi = input(self.view.demandeTournoiNom())
            if self.model.existeDansDB(self, choixNomTournoi) == True:
                # On demande si il veut vraiment supprimer le tournoi
                choixConfirmation = input(self.view.confirmationTournoiDelete())
                if choixConfirmation == "O":
                    self.model.deleteTournoi(self, choixNomTournoi)
                    choixNomTournoi = True
                elif choixConfirmation == "N":
                    choixNomTournoi = False
                else:
                    choixNomTournoi = False


    def launchTournoi(self):
        choixNomTournoi = False
