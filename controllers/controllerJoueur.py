import re
import os


class ControllerJoueur(object):

    def __init__(self):
        self.name = "ControllerJoueur"

    def gestionJoueur(self, message=""):
        self.view.gestionJoueur()
        choix = input("Veillez faire un choix : ")
        match choix:
            case "1":
                self.createJoueur()
            case "2":
                print("Vous avez choisi de modifier un joueur")
            case "3":
                print("vous avez choisi de supprimer un joueur")
            case "4":
                print("Vous avez choisi d'afficher les joueurs")
            case "5":
                print("Vous avez choisi d'afficher un joueur")
            case "6":
                self.app.accueil()
            case _:
                self.gestionJoueur("Veuillez faire un choix valide !")

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

        
