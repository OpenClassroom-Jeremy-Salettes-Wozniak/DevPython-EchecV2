import os

class ViewTournoi(object):

    def __init__(self):
        self.name = "ViewTournoi"
        

    def gestionTournoi(self, message = " "):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Tournoi ------------------")
        print("1 - Créer un tournoi")
        print("2 - Modifier un tournoi")
        print("3 - Supprimer un tournoi")
        print("4 - Lancer un tournoi")
        print("5 - Gestion des joueurs du tournoi")
        print("6 - Menu principal")
        print("-------------------------------------------")
        if message != "":
            print(message)

    def demandeTournoiNom(self, message = ""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Tournoi ------------------")
        print("Veuillez entrer le nom du tournoi : ")
        print("-------------------------------------------")
        if message != "":
            print(message)

    def erreurTournoiNom(self):
        message = "Veuillez entrer un nom valide !(ex: Tournoi A)"
        self.demandeTournoiNom(message)

    def demandeTournoiLieu(self, message = ""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Tournoi ------------------")
        print("Veuillez entrer le lieu du tournoi : ")
        print("-------------------------------------------")
        if message != "":
            print(message)

    def erreurTournoiLieu(self):
        message = "Veuillez entrer un lieu valide !(ex: Paris)"
        self.demandeTournoiLieu(message)


    def demandeTournoiNombreRondes(self, message = ""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Tournoi ------------------")
        print("Veuillez entrer le nombre de rondes du tournoi : ")
        print("-------------------------------------------")
        if message != "":
            print(message)

    def erreurTournoiNombreRondes(self):
        message = "Veuillez entrer un nombre valide !(ex: 4)"
        self.demandeTournoiNombreRondes(message)
    
    def demandeTournoiDescription(self, message = " "):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Tournoi ------------------")
        print("Veuillez entrer la description du tournoi : ")
        print("-------------------------------------------")
        if message != "":
            print(message)

    def erreurTournoiDescription(self):
        message = "Veuillez entrer une description valide !(ex: Tournoi de Paris)"
        self.demandeTournoiDescription(message)


    def erreurTournoiExistePas(self):
        message = "Ce tournoi n'existe pas !"
        self.gestionTournoi(message)

    def updateTournoi(self, message = ""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Modifier un tournoi ------------------")
        print("1 - Modifier le nom du tournoi")
        print("2 - Modifier le lieu du tournoi")
        print("3 - Modifier le nombre de rondes du tournoi")
        print("4 - Modifier la description du tournoi")
        print("5 - Retour au menu précédent")
        print("--------------------------------------------------------")
        if message != "":
            print(message)

    def demandeMenu(self, message = ""):
        message
        return message

    def confirmationTournoiDelete(self, message = ""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Supprimer un tournoi ------------------")
        print("Voulez-vous vraiment supprimer ce tournoi ? (O/N)")
        print("--------------------------------------------------------")
        if message != "":
            print(message)

    def confirmationTournoiLaunch(self, message = ""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Lancer un tournoi ------------------")
        print("Voulez-vous vraiment lancer ce tournoi ? (O/N)")
        print("--------------------------------------------------------")
        if message != "":
            print(message)

    def gestionJoueurTournoi(self, message=""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Gestion des joueurs du tournoi ------------------")
        print("1 - Ajouter un joueur au tournoi")
        print("2 - Supprimer un joueur du tournoi")
        print("3 - Retour au menu précédent")
        print("------------------------------------------------------------------")
        if message != "":
            print(message)

    def demandeJoueurNom(self, message=""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Gestion des joueurs du tournoi ------------------")
        print("Veuillez entrer le nom du joueur : ")
        print("------------------------------------------------------------------")
        if message != "":
            print(message)

    def demandeResultatMatch(self, match,  message=""):
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("---------------- Gestion des joueurs du tournoi ------------------")
        print("Veuillez entrer le résultat du match : ")
        print(match)
        print("------------------------------------------------------------------")
        if message != "":
            print(message)