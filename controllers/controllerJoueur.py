# Authors: Jérémy Salettes-Wozniak 

# VIEWS
from views.viewJoueur import ViewJoueur

# MODELS
from models.joueurs import Joueur

# EXTERNAL LIBRARIES
import re
import os

class ControllerJoueur(object):

    def __init__(self):
        self.name = "ControllerJoueur"
        self.view = ViewJoueur()
        self.model = Joueur

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
        # Nettoyage de la console
        os.system("cls")

        # JOUEUR DICTIONARY
        joueur = {}

        # ID NATIONAL
        choixIDNational = False
        while not choixIDNational:
            idNational = input("Veuillez saisir l'ID national du joueur : ")
            # REMATCH AD12345
            if re.match(r"^[A-Z]{2}[0-9]{5}$", idNational):
                choixIDNational = True
                joueur["idNational"] = idNational
            else:
                os.system("cls")
                print("Veuillez saisir un ID national valide !")


        # # NOM
        choixNom = False
        while not choixNom:
            nom = input("Veuillez saisir le nom du joueur : ")
            if re.match(r"^[A-Z]{1}[a-z]+$", nom):
                choixNom = True
                joueur["nom"] = nom
            else:
                os.system("cls")
                print("Veuillez saisir un nom valide !")

        # # PRENOM
        choixPrenom = False
        while not choixPrenom:
            prenom = input("Veuillez saisir le prénom du joueur : ")
            if re.match(r"^[A-Z]{1}[a-z]+$", prenom):
                choixPrenom = True
                joueur["prenom"] = prenom
            else:
                os.system("cls")
                print("Veuillez saisir un prénom valide !")

        # # DATE DE NAISANCE
        choixDateNaissance = False
        while not choixDateNaissance:
            dateNaissance = input("Veuillez saisir la date de naissance du joueur : ")
            if re.match(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$", dateNaissance):
                choixDateNaissance = True
                joueur["dateNaissance"] = dateNaissance
            else:
                os.system("cls")
                print("Veuillez saisir une date de naissance valide ! au format JJ/MM/AAAA")

        # # CLASSEMENT ELO
        # ##
        # # Nouveau joueur : 2000 points
        # # En fonction de la partie gagnée ou perdue, le joueur gagne ou perd entre 5 et 30 points
        # # Selon le classement de l'adversaire, le joueur gagne ou perd entre 0 et 15 points
        # ##
        choixClassementElo = False
        while not choixClassementElo:
            classementElo = input("Veuillez saisir le classement ELO du joueur : ")
            if re.match(r"^[0-9]+$", classementElo):
                choixClassementElo = True
                joueur["classementElo"] = classementElo
            else:
                os.system("cls")
                print("Veuillez saisir un classement ELO valide !")

        # SEXE
        choixSexe = False
        while not choixSexe:
            sexe = input("Veuillez saisir le sexe du joueur : ")
            if re.match(r"^[M|F]$", sexe):
                choixSexe = True
                joueur["sexe"] = sexe
            else:
                os.system("cls")
                print("Veuillez saisir un sexe valide ! au format M ou F")
        
        # CREATION DU JOUEUR
        #self, id_national, joueur_nom, joueur_prenom, joueur_date_naissance, classement_elo, sexe
        newJoueur = self.model(
            joueur["idNational"],
            joueur["nom"],
            joueur["prenom"],
            joueur["dateNaissance"],
            joueur["classementElo"],
            joueur["sexe"]
        )
        newJoueur.save()

    def updateJoueur(self):
        pass

    def deleteJoueur(self):
        pass

    def showJoueurs(self):
        pass

    def showJoueur(self):
        pass
