
# Import des modules externes
import os
import prettytable

class ViewJoueur(object):

    def __init__(self):
        self.name = "ViewJoueur"
        self.table = prettytable.PrettyTable()

    def gestionJoueur(self, message=""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de joueurs !")
        print("---------------- Joueurs ------------------")
        print("1 - Créer un joueur")
        print("2 - Modifier un joueur")
        print("3 - Supprimer un joueur")
        print("4 - Afficher les joueurs")
        print("5 - Afficher un joueur")
        print("6 - Retour au menu principal")
        print("--------------------------------------------")
        if message != "":
            print(message)
    
    def showJoueurs(self, joueurs):
        # Nettoyage de la console
        os.system("cls")

        # Création du tableau
        self.table.field_names = ["ID", "Nom", "Prénom", "Date de naissance", "Classement Elo", "Sexe"]
        for joueur in joueurs:
            self.table.add_row([joueur.id, joueur.nom, joueur.prenom, joueur.date_naissance, joueur.classement_elo, joueur.sexe])
        print(self.table)
        


    def updateJoueur(self, message=""):
        os.system("cls")
        print("Bienvenue dans le gestionnaire de joueurs !")
        print("--------------- Modifier -------------------")
        print("1 - Modifier le nom")
        print("2 - Modifier le prénom")
        print("3 - Modifier la date de naissance")
        print("4 - Modifier le classement elo")
        print("5 - Modifier le sexe")
        print("6 - Retour au menu précédent")
        print("--------------------------------------------")
        if message != "":
            print(message)

    # Demande de l'ID national 
    def demandeIDNational(self):
        return "Veuillez entrer l'ID national du joueur (ex: AA12345) : "
    
    def erreurIDNational(self):
        message = "Erreur, veuillez entrer un ID national valide, deux premiers caractères en majuscul et les 5 suivant en chiffre"
        return message

    # Demande du nom du joueur
    def demandeJoueurNom(self):
        return "Veuillez entrer le nom du joueur : "

    def erreurJoueurNom(self):
        message = "Erreur, veuillez entrer un nom valide, uniquement des lettres"
        return message

    # Demande du prénom du joueur
    def demandeJoueurPrenom(self):
        return "Veuillez entrer le prénom du joueur : "

    def erreurJoueurPrenom(self):
        message = "Erreur, veuillez entrer un prénom valide, uniquement des lettres et Majuscule au début"
        return message

    # Demande de la date de naissance du joueur
    def demandeJoueurDateNaissance(self):
        return "Veuillez entrer la date de naissance du joueur (ex: JJ/MM/AAAA) : "

    def erreurJoueurDateNaissance(self):
        message = "Erreur, veuillez entrer une date de naissance valide (ex: JJ/MM/AAAA)"
        return message

    def demandeJoueurClassementElo(self):
        return "Veuillez entrer le classement elo du joueur : "

    def erreurJoueurClassementElo(self):
        message = "Erreur, veuillez entrer un classement elo valide (ex: 2000)"
        return message

    def demandeJoueurSexe(self):
        return "Veuillez entrer le sexe du joueur (H/F) : "

    def erreurJoueurSexe(self):
        message = "Erreur, veuillez entrer un sexe valide (H/F)"
        return message
        
    def demandeMenu(self):
        return "Veuillez faire un choix : "

    def erreurMenu(self):
        message = "Erreur, veuillez faire un choix valide !"
        return message