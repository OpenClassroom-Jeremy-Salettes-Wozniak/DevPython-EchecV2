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
        tournoi_nb_round = "4",
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

    # DELETE TOURNOI EN JSON
    def deleteTournoi(self, nomTournoi):
        # On crée la base de données
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.remove(Query().tournoi_nom == nomTournoi)


    def existeDansDB(self, nom):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        if table.search(Query().tournoi_nom == nom):
            return True
        else:
            return False

    def setNomTournoi(self, nomTournoi, nomUpdate):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_nom': nomUpdate
        }, Query().tournoi_nom == nomTournoi)
                
    def setLieuTournoi(self, nomTournoi, lieuUpdate):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_lieu': lieuUpdate
        }, Query().tournoi_nom == nomTournoi)

    def setNombreRondesTournoi(self, nomTournoi, nbRondesUpdate):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_nb_round': nbRondesUpdate
        }, Query().tournoi_nom == nomTournoi)

    def setDescriptionTournoi(self, nomTournoi, descriptionUpdate):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_description': descriptionUpdate
        }, Query().tournoi_nom == nomTournoi)

    def addJoueurTournoi(self, nomTournoi, joueur):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_joueurs': joueur
        }, Query().tournoi_nom == nomTournoi)

    def deleteJoueurTournoi(self, nomTournoi, joueur):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_joueurs': joueur
        }, Query().tournoi_nom == nomTournoi)

    def checkJoueursTournoi(self, nomTournoi):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        return table.search(Query().tournoi_nom == nomTournoi)[0]['tournoi_joueurs']
    
    def checkJoueursTournoiByIDNatinal(self, idNational, listeJoueurs):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        print(idNational)
        if idNational in listeJoueurs:
            return True
        else:
            return False
    
    
    def setTournoiStatus(self, nomTournoi, status):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_etat': status
        }, Query().tournoi_nom == nomTournoi)

    def getTournoiRound(self, nomTournoi):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        return table.search(Query().tournoi_nom == nomTournoi)[0]['tournoi_round']
    
    def setTournoiRound(self, nomTournoi, round):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_round': round
        }, Query().tournoi_nom == nomTournoi)

    def setTournoiDateDebut(self, nomTournoi, dateDebut):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_date_debut': dateDebut
        }, Query().tournoi_nom == nomTournoi)

    def setTournoiHeureDebut(self, nomTournoi, heureDebut):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_heure_debut': heureDebut
        }, Query().tournoi_nom == nomTournoi)

    def getTournoiId(self, nomTournoi):
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        return table.search(Query().tournoi_nom == nomTournoi)[0].doc_id
    
    def saveMatch(self, nomTournoi, round_name, id_tournoi_rounds, matchs_turple):
        # On ajoute chaque element à tournoi_rounds_list pour le sauvegarder dans la base de données
        db = TinyDB('data/tournois.json')
        table = db.table('tournois')
        table.update({
            'tournoi_rounds_list': {
                'round_name': round_name,
                'id_tournoi_rounds': id_tournoi_rounds,
                'matchs_turple': matchs_turple
            }
        }, Query().tournoi_nom == nomTournoi)
        
