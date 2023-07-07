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
        # Si le dossier data n'existe pas, on le crée et on crée le fichier joueurs.json
        if not os.path.exists('data'):
            os.makedirs('data')

        # On crée la base de données
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
            'classement_elo': self.classement_elo,
            'sexe': self.sexe
        })

    def getJoueurs(id_national):
        resultats = table.search(query.id_national == id_national)
        return resultats
        
    # RECHERCHE TOUS LES JOUEURS
    def getAllJoueurs():
        db = TinyDB('data/joueurs.json')
        table = db.table('joueurs')
        resultats = table.all()
        return resultats
    
    # EXISTE DANS LA DB
    def existeDansDB(self, champ, valeur):
        db = TinyDB('data/joueurs.json')
        table = db.table('joueurs')
        query = Query()
        resultats = table.search(query[champ] == valeur)
        if len(resultats) == 0:
            return False
        else:
            return True