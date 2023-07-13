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
        print("5 - Menu principal")
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


