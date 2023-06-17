from tinydb import TinyDB, Query
import os

class Joueur(object):

    def __init__(self, id_national, joueur_nom, joueur_prenom, joueur_date_naissance, classement_elo, sexe):
        self.id_national = id_national
        self.joueur_nom = joueur_nom
        self.joueur_prenom = joueur_prenom
        self.joueur_date_naissance = joueur_date_naissance
        self.classement_elo = classement_elo
        self.sexe = sexe
    
    # DATABASE JOUEUR
    def dbJoueur(self):
        # Si le dossier data n'existe pas on le crée et on crée le fichier joueurs.json
        if not os.path.exists('data'):
            os.makedirs('data')

        # On crée la base de donnée
        db = TinyDB('data/joueurs.json')
        return db

    # SAVE JOUEUR EN JSON
    def save(self):
        # On crée la base de donnée
        db = self.dbJoueur()
        # On nomme la table joueurs
        table = db.table('joueurs')
        # On insert les données dans la table joueurs
        table.insert({
            'id_national': self.id_national,
            'joueur_nom': self.joueur_nom,
            'joueur_prenom': self.joueur_prenom,
            'joueur_date_naissance': self.joueur_date_naissance,
            'classement_elo': self.classement_elo
        })

    # RECHERCHE DANS LA DB
    def rechercheDansDB(self, champ, valeur):
        ###
        # champ = champ de la table
        # valeur = valeur recherchée
        # return = résultat de la recherche
        ##
        # Permet de rechercher dans la base de donnée de la table joueurs
        # Query() permet de faire des requêtes dans la base de donnée
        # search() permet de faire une recherche dans la base de donnée
        ###
        db = self.dbJoueur()
        table = db.table('joueurs')
        query = Query()
        resultats = table.search(query[champ] == valeur)
        return resultats

    # UPDATE DB
    def updateDB(self, champ, valeur, id):
        ###
        # champ = champ de la table
        # query.id == id =  c'est l'id de la ligne à modifier
        # update({champ: valeur} = on modifie la valeur du champ
        ##
        # Permet de rechercher dans la base de donnée de la table joueurs
        # Query() permet de faire des requêtes dans la base de donnée
        # search() permet de faire une recherche dans la base de donnée
        ###
        db = self.dbJoueur()
        table = db.table('joueurs')
        query = Query()
        table.update({champ: valeur}, query.id == id)

    # RECHERCHE JOUEUR PAR ID
    def getJoueurByID(self, id):
        resultats = self.rechercheDansDB('id', id)
        return resultats

    # RECHERCHE JOUEUR PAR ID NATIONAL
    def getIDNational(self, id_national):
        resultats = self.rechercheDansDB('id_national', id_national)
        return resultats
        
    def setIDNational(self, id_national, id):
        self.updateDB('id_national', id_national, id)

    # RECHERCHE JOUEUR PAR NOM
    def getJoueurNom(self, joueur_nom):
        resultats = self.rechercheDansDB('joueur_nom', joueur_nom)
        return resultats
    
    def setJoueurNom(self, joueur_nom, id):
        self.updateDB('joueur_nom', joueur_nom, id)

    # RECHERCHE JOUEUR PAR PRENOM
    def getJoueurPrenom(self, joueur_prenom):
        resultats = self.rechercheDansDB('joueur_prenom', joueur_prenom)
        return resultats

    def setJoueurPrenom(self, joueur_prenom, id):
        self.updateDB('joueur_prenom', joueur_prenom, id)

    # RECHERCHE JOUEUR PAR DATE DE NAISSANCE
    def getJoueurDateNaissance(self, joueur_date_naissance):
        resultats = self.rechercheDansDB('joueur_date_naissance', joueur_date_naissance)
        return resultats
    
    def setJoueurDateNaissance(self, joueur_date_naissance, id):
        self.updateDB('joueur_date_naissance', joueur_date_naissance, id)

    # RECHERCHE JOUEUR PAR CLASSEMENT ELO
    def getClassementElo(self, classement_elo):
        resultats = self.rechercheDansDB('classement_elo', classement_elo)
        return resultats

    def setClassementElo(self, classement_elo, id):
        self.updateDB('classement_elo', classement_elo, id)

    def getSexe(self, sexe):
        resultats = self.rechercheDansDB('sexe', sexe)
        return resultats
    
    def setSexe(self, sexe, id):
        self.updateDB('sexe', sexe, id)
        