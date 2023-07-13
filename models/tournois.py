from tinydb import TinyDB, Query
import os
class Tournoi(object):

    def __init__(
        self, 
        tournoi_nom, 
        tournoi_description,
        tournoi_lieu,
        tournoi_date_debut = "",
        tournoi_date_fin = "",
        tournoi_heure_debut = "",
        tournoi_heure_fin = "",
        tournoi_round= 0,
        tournoi_nb_round = 4,
        tournoi_joueurs = [],
        tournoi_rounds_list = [],
        tournoi_etat = "Non lance"
        ):
        self.tournoi_nom = tournoi_nom
        self.tournoi_description = tournoi_description
        self.tournoi_lieu = tournoi_lieu
        self.tournoi_date_debut = tournoi_date_debut
        self.tournoi_date_fin = tournoi_date_fin
        self.tournoi_heure_debut = tournoi_heure_debut
        self.tournoi_heure_fin = tournoi_heure_fin
        self.tournoi_round = tournoi_round
        self.tournoi_nb_round = tournoi_nb_round
        self.tournoi_joueurs = tournoi_joueurs
        self.tournoi_rounds_list = tournoi_rounds_list
        self.tournoi_etat = tournoi_etat

    # DATABASE Tournoi
    def dbTournoi(self):
        # Si le dossier data n'existe pas, on le crée et on crée le fichier tournois.json
        if not os.path.exists('data'):
            os.makedirs('data')

        # On crée la base de données
        db = TinyDB('data/tournois.json')

        return db

    # SAVE TOURNOI EN JSON
    def saveTournoi(self):
        # On crée la base de données
        db = self.dbTournoi()
        
        # On nomme la table Tournois
        table = db.table('tournois')

        # On récupère les données du tournoi
        tournoi = self.__dict__

        # On insère les données dans la base de données
        table.insert(tournoi)





                