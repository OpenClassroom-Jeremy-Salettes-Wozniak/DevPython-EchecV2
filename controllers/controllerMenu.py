# Authors: Jérémy Salettes-Wozniak

# CONTROLLERS
from controllers.controllerTournoi import ControllerTournoi
from controllers.controllerJoueur import ControllerJoueur
from controllers.controllerRapport import ControllerRapport

# VIEWS
from views.viewMenu import ViewMenu

# EXTERNAL LIBRARIES
import os


class ControllerMenu:
    """
        Classe ControllerMenu :
        -----------------------
        Classe permettant de gérer le menu principal de l'application.

        Méthodes :
        ----------
        gestionAccueil(self) : Méthode permettant de gérer le menu principal de l'application.
        gestionJoueur(self) : Méthode permettant de gérer le menu de gestion des joueurs.
        gestionTournoi(self) : Méthode permettant de gérer le menu de gestion des tournois.
        gestionRapport(self) : Méthode permettant de gérer le menu de gestion des rapports.
        run(self) : Méthode permettant de lancer le menu principal de l'application.

        Attributs :
        -----------
        name : str
            Nom de la classe
        view : ViewMenu
            Instance de la classe ViewMenu

        Exemple :
        ---------
        >>> ControllerMenu()
    """

    def __init__(self):
        """ 
            Constructeur de la classe ControllerMenu

            Paramètres :
            ------------
            Aucun
        """
        self.name = "ControllerMenu"
        self.view = ViewMenu()
        self.controllerTournoi = ControllerTournoi()
        self.controllerJoueur = ControllerJoueur()
        self.controllerRapport = ControllerRapport()

    def gestionAccueil(self, message=""):
        """
            Méthode permettant de gérer le menu principal de l'application.

            Paramètres :
            ------------
            message : str
                Message à afficher en cas d'erreur

            Retour :
            --------
            True

            Exemple :
            ---------
            >>> ControllerMenu().gestionAccueil()
        """
        # Nettoyage de la console
        os.system("cls")


        # Affichage de la vue
        self.view.selectionMenu(message)

        # Logique de gestion du menu
        choix_valide = False
        while not choix_valide:
            # Choix de l'utilisateur
            choix = input("Veuillez faire un choix : ")
            # Vérification de la validité du choix
            if choix in ["1", "2", "3"]:
                # Si choix est valide on renvoie la méthode correspondante
                choix_valide = True
                # Si choix "1" : Gestion des tournois
                if choix == "1":
                    self.gestionTournoi()
                # Si choix "2" : Gestion des joueurs
                elif choix == "2":
                    self.gestionJoueur()
                # Si choix "3" : Gestion des rapports
                elif choix == "3":
                    self.gestionRapport()
            else:
                # Sinon on réaffiche le menu avec un message d'erreur
                self.gestionAccueil("Veuillez faire un choix valide !")

        # Retour de la méthode
        return True

    # TODO: Implémenter la logique de gestion des tournois
    def gestionTournoi(self):
        accueil = self.controllerTournoi.gestionTournoi()
        if accueil == False:
            self.gestionAccueil()
        

    # TODO: Implémenter la logique de gestion des joueurs
    def gestionJoueur(self):
        accueil = self.controllerJoueur.gestionJoueur()
        if accueil == False:
            self.gestionAccueil()
        
    # TODO: Implémenter la logique de gestion des rapports
    def gestionRapport(self):
        accueil = self.controllerRapport.gestionRapport()
        if accueil == False:
            self.gestionAccueil()
