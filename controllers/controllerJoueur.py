# Authors: Jérémy Salettes-Wozniak 

# VIEWS
from views.viewJoueur import ViewJoueur

# EXTERNAL LIBRARIES
import re
import os

class ControllerJoueur(object):

    def __init__(self):
        self.name = "ControllerJoueur"
        self.view = ViewJoueur()

    def gestionJoueur(self, message=""):
        """
            Méthode permettant de gérer le menu de gestion des joueurs.

            Paramètres :
            ------------
            message : str
                Message à afficher en cas d'erreur
        """
        
        # Nettoyage de la console
        os.system("cls")

        # Affichage du menu de gestion des joueurs
        self.view.gestionJoueur()

        # Logique de gestion du menu
        choix_valide = False
        while not choix_valide:
            # Choix de l'utilisateu
            choix = input("Veillez faire un choix : ")
            # Vérification de la validité du choix
            if choix in ["1", "2", "3", "4", "5", "6"]:
                # Si choix est valide on renvoie la méthode correspondante
                choix_valide = True
                # Si choix "1" : Créer un joueur
                if choix == "1":
                    self.createJoueur()
                # Si choix "2" : Modifier un joueur
                elif choix == "2":
                    self.updateJoueur()
                # Si choix "3" : Supprimer un joueur
                elif choix == "3":
                    self.deleteJoueur()
                # Si choix "4" : Afficher les joueurs
                elif choix == "4":
                    self.showJoueurs()
                # Si choix "5" : Afficher un joueur
                elif choix == "5":
                    self.showJoueur()
                # Si choix "6" : Menu principal
                elif choix == "6":
                    return False
            else:
                self.gestionJoueur("Veuillez faire un choix valide !")
        
        return True

    def createJoueur(self):

        # ID NATIONAL
        while True:
            id_national = input(self.view.demandeIDNational())
            if re.match("^[A-Z]{2}[0-9]{5}$", id_national):
                return id_national
            print(self.view.ErreurIDNational())

        # NOM
        while True:
            joueur_nom = input(self.view.demandeJoueurNom())
            if re.match("^[A-Za-z]+$", joueur_nom):
                return joueur_nom
            print(self.view.ErreurJoueurNom())

        # PRENOM
        while True:
            joueur_prenom = input(self.view.demandeJoueurPrenom())
            if re.match("^[A-Za-z]+$", joueur_prenom):
                return joueur_prenom
            print(self.view.ErreurJoueurPrenom())

        # DATE DE NAISSANCE
        while True:
            joueur_date_naissance = input(self.view.demandeJoueurDateNaissance())
            if re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$", joueur_date_naissance):
                return joueur_date_naissance
            print(self.view.ErreurJoueurDateNaissance())

        # CLASSEMENT ELO
        ##
        # Nouveau joueur : 2000 points
        # En fonction de la partie gagnée ou perdue, le joueur gagne ou perd entre 5 et 30 points
        # Selon le classement de l'adversaire, le joueur gagne ou perd entre 0 et 15 points
        ##
        while True:
            joueur_classement_elo = input(self.view.demandeJoueurClassementElo()) 
            if re.match("^[0-9]{4}$", joueur_classement_elo):
                return joueur_classement_elo
            print(self.view.ErreurJoueurClassementElo())

        # SEXE
        while True:
            joueur_sexe = input(self.view.demandeJoueurSexe())
            if re.match("^[A-Za-z]+$", joueur_sexe):
                return joueur_sexe
            print(self.view.ErreurJoueurSexe())

        id_national = self.demandeIDNational()
        joueur_nom = self.demandeJoueurNom()
        joueur_prenom = self.demandeJoueurPrenom()
        joueur_date_naissance = self.demandeJoueurDateNaissance()
        joueur_classement_elo = self.demandeJoueurClassementElo()
        joueur_sexe = self.demandeJoueurSexe()
        
        # CREATION DU JOUEUR
        joueur = self.model(
            id_national = id_national,
            joueur_nom = joueur_nom,
            joueur_prenom = joueur_prenom,
            joueur_date_naissance = joueur_date_naissance,
            joueur_classement_elo = joueur_classement_elo,
            joueur_sexe = joueur_sexe
        )
        joueur.save()

    def updateJoueur(self):
        pass

    def deleteJoueur(self):
        pass

    def showJoueurs(self):
        pass

    def showJoueur(self):
        pass
