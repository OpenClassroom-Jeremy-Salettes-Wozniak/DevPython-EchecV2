# Authors: Jérémy Salettes-Wozniak 

# VIEWS
import os
# EXTERNAL LIBRARIES
import re

# MODELS
from models.joueurs import Joueur
from views.viewJoueur import ViewJoueur


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
        self.view.gestionJoueur(message)

        # Logique de gestion du menu
        choix_valide = False
        while not choix_valide:
            # Choix de l'utilisateu
            choix = input(self.view.demandeMenu())
            # Vérification de la validité du choix
            if choix in ["1", "2", "3", "4"]:
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
                # Si choix "4" : Menu principal
                elif choix == "4":
                    return False
            else:
                self.gestionJoueur(self.view.erreurMenu())
        
        return True

    def createJoueur(self):
        # Nettoyage de la console
        os.system("cls")

        # JOUEUR DICTIONARY
        joueur = {}

        # ID NATIONAL
        choixIDNational = False
        while not choixIDNational:
            idNational = input(self.view.demandeIDNational())
            # REMATCH AD12345
            if re.match(r"^[A-Z]{2}[0-9]{5}$", idNational):
                choixIDNational = True
                joueur["idNational"] = idNational
            else:
                os.system("cls")
                print(self.view.erreurIDNational())


        # # NOM
        choixNom = False
        while not choixNom:
            nom = input(self.view.demandeJoueurNom())
            if re.match(r"^[A-Z]{1}[a-z]+$", nom):
                choixNom = True
                joueur["nom"] = nom
            else:
                os.system("cls")
                print(self.view.erreurJoueurNom())

        # # PRENOM
        choixPrenom = False
        while not choixPrenom:
            prenom = input(self.view.demandeJoueurPrenom())
            if re.match(r"^[A-Z]{1}[a-z]+$", prenom):
                choixPrenom = True
                joueur["prenom"] = prenom
            else:
                os.system("cls")
                print(self.view.erreurJoueurPrenom())

        # # DATE DE NAISANCE
        choixDateNaissance = False
        while not choixDateNaissance:
            dateNaissance = input(self.view.demandeJoueurDateNaissance())
            if re.match(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$", dateNaissance):
                choixDateNaissance = True
                joueur["dateNaissance"] = dateNaissance
            else:
                os.system("cls")
                print(self.view.erreurJoueurDateNaissance())

        # # CLASSEMENT ELO
        # ##
        # # Nouveau joueur : 2000 points
        # # En fonction de la partie gagnée ou perdue, le joueur gagne ou perd entre 5 et 30 points
        # # Selon le classement de l'adversaire, le joueur gagne ou perd entre 0 et 15 points
        # ##
        choixClassementElo = False
        while not choixClassementElo:
            classementElo = input(self.view.demandeJoueurClassementElo())
            if re.match(r"^[0-9]+$", classementElo):
                choixClassementElo = True
                joueur["classementElo"] = classementElo
            else:
                os.system("cls")
                print(self.view.erreurJoueurClassementElo())

        # SEXE
        choixSexe = False
        while not choixSexe:
            sexe = input(self.view.demandeJoueurSexe())
            if re.match(r"^[M|F]$", sexe):
                choixSexe = True
                joueur["sexe"] = sexe
            else:
                os.system("cls")
                print(self.view.erreurJoueurSexe())
        
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

        # RETOUR AU MENU DE GESTION DES JOUEURS
        self.gestionJoueur()

    def updateJoueur(self, message=""):
        choixIDNational = False
        # Choix de l'ID National
        while not choixIDNational:
            # On demande l'ID National
            idNational = input(self.view.demandeIDNational())
            # On vérifie que l'ID National est valide
            if re.match(r"^[A-Z]{2}[0-9]{5}$", idNational):
                # Si l'ID National est valide on vérifie qu'il existe dans la base de données
                if self.model.existeDansDB(self, "id_national", idNational) == True:
                    # Si l'ID National existe dans la base de données on demande les informations à modifier
                    choixIDNational = True
                    # Nettoyage de la console
                    os.system("cls")
                    # Affichage du menu de modification d'un joueur
                    self.view.updateJoueur()
                    # Logique de modification d'un joueur
                    choix_valide = False
                    while not choix_valide:
                        # Choix de l'utilisateur
                        choix = input(self.view.demandeMenu())
                        # Vérification de la validité du choix
                        if choix in ["1", "2", "3", "4", "5", "6"]:
                            # Si choix est valide on renvoie la méthode correspondante
                            choix_valide = True
                            # Si choix "1" : Modifier le nom
                            if choix == "1":
                                choixNom = False
                                while not choixNom:
                                    nom = input(self.view.demandeJoueurNom())
                                    if re.match(r"^[A-Z]{1}[a-z]+$", nom):
                                        choixNom = True
                                        self.model.setNom(self, idNational, nom)
                                        self.gestionJoueur("Le nom du joueur a bien été modifié !")
                                    else:
                                        os.system("cls")
                                        print(self.view.erreurJoueurNom())

                            # Si choix "2" : Modifier le prénom
                            elif choix == "2":
                                choixPrenom = False
                                while not choixPrenom:
                                    prenom = input(self.view.demandeJoueurPrenom())
                                    if re.match(r"^[A-Z]{1}[a-z]+$", prenom):
                                        choixPrenom = True
                                        self.model.setPrenom(self, idNational, prenom)
                                        self.gestionJoueur("Le prénom du joueur a bien été modifié !")
                                    else:
                                        os.system("cls")
                                        print(self.view.erreurJoueurPrenom())
                            # Si choix "3" : Modifier la date de naissance
                            elif choix == "3":
                                choixDateNaissance = False
                                while not choixDateNaissance:
                                    dateNaissance = input(self.view.demandeJoueurDateNaissance())
                                    if re.match(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$", dateNaissance):
                                        choixDateNaissance = True
                                        self.model.setDateNaissance(self, idNational, dateNaissance)
                                        self.gestionJoueur("La date de naissance du joueur a bien été modifiée !")
                                    else:
                                        os.system("cls")
                                        print(self.view.erreurJoueurDateNaissance())
                            # Si choix "4" : Modifier le classement Elo
                            elif choix == "4":
                                choixClassementElo = False
                                while not choixClassementElo:
                                    classementElo = input(self.view.demandeJoueurClassementElo())
                                    if re.match(r"^[0-9]+$", classementElo):
                                        choixClassementElo = True
                                        self.model.setClassementElo(self, idNational, classementElo)
                                        self.gestionJoueur("Le classement Elo du joueur a bien été modifié !")
                                    else:
                                        os.system("cls")
                                        print(self.view.erreurJoueurClassementElo())
                            # Si choix "5" : Modifier le sexe
                            elif choix == "5":
                                choixSexe = False
                                while not choixSexe:
                                    sexe = input(self.view.demandeJoueurSexe())
                                    if re.match(r"^[H|F]$", sexe):
                                        choixSexe = True
                                        self.model.setSexe(self, idNational, sexe)
                                        self.gestionJoueur("Le sexe du joueur a bien été modifié !")
                                    else:
                                        os.system("cls")
                                        print(self.view.erreurJoueurSexe())
                            # Si choix "6" : Menu précédent
                            elif choix == "6":
                                self.gestionJoueur()
                        else:
                            self.updateJoueur(self.view.erreurMenu())
                else:
                    # Si l'ID National n'existe pas dans la base de données on répète la demande de l'ID National
                    os.system("cls")
                    print(self.view.erreurIDNational())

            else:
                # Sinon on répète la demande de l'ID National
                os.system("cls")
                print(self.view.erreurIDNational())

    def deleteJoueur(self, message=""):
        # View : Demande de la personne à supprimer
        choix_valide = False
        while not choix_valide:
            # Si choix différent de "1" ou "2" on répète la demande
            choix = input(self.view.deleteJoueur())
            if choix in ["1", "2"]:
                choix_valide = True
                # Si choix "1" : Suppression d'une personne
                if choix == "1":
                    choixIDNational = False
                    while not choixIDNational:
                        # On demande l'ID National
                        idNational = input(self.view.demandeIDNational())
                        # On vérifie que l'ID National est valide
                        if re.match(r"^[A-Z]{2}[0-9]{5}$", idNational):
                            # Si l'ID National est valide on vérifie qu'il existe dans la base de données
                            if self.model.existeDansDB(self, "id_national", idNational) == True:
                                # Si l'ID National existe dans la base de données on supprime la personne
                                choixIDNational = True
                                self.model.delete(self, idNational)
                                self.gestionJoueur("Le joueur a bien été supprimé !")
                            else:
                                # Si l'ID National n'existe pas dans la base de données on répète la demande de l'ID National
                                os.system("cls")
                                print(self.view.erreurIDNational())
                else :
                    # Si choix "2" : Menu précédent
                    self.gestionJoueur()