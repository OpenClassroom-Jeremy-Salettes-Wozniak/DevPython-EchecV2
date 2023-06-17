
# Import des modules externes
import os

class ViewJoueur(object):

    def __init__(self):
        self.name = "ViewJoueur"

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

    # Demande de l'ID national 
    def demandeIDNational(self):
        return "Veuillez entrer l'ID national du joueur (ex: AA12345) : "
    
    def ErreurIDNational(self):
        message = "Erreur, veuillez entrer un ID national valide, deux premiers caractères en majuscul et les 5 suivant en chiffre"
        return message

    # Demande du nom du joueur
    def demandeJoueurNom(self):
        return "Veuillez entrer le nom du joueur : "

    def ErreurJoueurNom(self):
        message = "Erreur, veuillez entrer un nom valide, uniquement des lettres"
        return message

    # Demande du prénom du joueur
    def demandeJoueurPrenom(self):
        return "Veuillez entrer le prénom du joueur : "

    def ErreurJoueurPrenom(self):
        message = "Erreur, veuillez entrer un prénom valide, uniquement des lettres"
        return message

    # Demande de la date de naissance du joueur
    def demandeJoueurDateNaissance(self):
        return "Veuillez entrer la date de naissance du joueur (ex: JJ/MM/AAAA) : "

    def ErreurJoueurDateNaissance(self):
        message = "Erreur, veuillez entrer une date de naissance valide (ex: JJ/MM/AAAA)"
        return message

    def demandeJoueurClassementElo(self):
        return "Veuillez entrer le classement elo du joueur : "

    def ErreurJoueurClassementElo(self):
        message = "Erreur, veuillez entrer un classement elo valide (ex: 2000)"
        return message

    def demandeSexe(self):
        return "Veuillez entrer le sexe du joueur (H/F) : "

    def ErreurSexe(self):
        message = "Erreur, veuillez entrer un sexe valide (H/F)"
        return message
        