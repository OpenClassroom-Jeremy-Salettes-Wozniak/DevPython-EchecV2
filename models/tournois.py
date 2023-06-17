class Tournoi(object):

    def __init__(
        self, 
        tournoi_nom, 
        tournoi_description,
        tournoi_lieu,
        tournoi_date_debut,
        tournoi_date_fin,
        tournoi_heure_debut,
        tournoi_heure_fin,
        tournoi_round= 0,
        tournoi_nb_round = 4,
        tournoi_joueurs = [],
        tournoi_rounds_list = [],
        tournoi_etat = "Non lancé"
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

        # NOM
        def getTournoiNom(self):
            return self.tournoi_nom
        def setTournoiNom(self, tournoi_nom):
            self.tournoi_nom = tournoi_nom

        # DESCRIPTION
        def getTournoiDescription(self):
            return self.tournoi_description
        def setTournoiDescription(self, tournoi_description):
            self.tournoi_description = tournoi_description

        # LIEU
        def getTournoiLieu(self):
            return self.tournoi_lieu
        def setTournoiLieu(self, tournoi_lieu):
            self.tournoi_lieu = tournoi_lieu

        # DATE DEBUT
        def getTournoiDateDebut(self):
            return self.tournoi_date_debut
        def setTournoiDateDebut(self, tournoi_date_debut):
            self.tournoi_date_debut = tournoi_date_debut

        # DATE FIN
        def getTournoiDateFin(self):
            return self.tournoi_date_fin
        def setTournoiDateFin(self, tournoi_date_fin):
            self.tournoi_date_fin = tournoi_date_fin

        # HEURE DEBUT
        def getTournoiHeureDebut(self):
            return self.tournoi_heure_debut
        def setTournoiHeureDebut(self, tournoi_heure_debut):
            self.tournoi_heure_debut = tournoi_heure_debut

        # HEURE FIN
        def getTournoiHeureFin(self):
            return self.tournoi_heure_fin
        def setTournoiHeureFin(self, tournoi_heure_fin):
            self.tournoi_heure_fin = tournoi_heure_fin
            
        # ROUND ACTUEL
        def getTournoiRound(self):
            return self.tournoi_round
        def setTournoiRound(self, tournoi_round):
            self.tournoi_round = tournoi_round

        # NOMBRE DE ROUNDS
        def getTournoiNbRound(self):
            return self.tournoi_nb_round
        def setTournoiNbRound(self, tournoi_nb_round):
            self.tournoi_nb_round = tournoi_nb_round

        # JOUEURS LIST
        def getTournoiJoueurs(self):
            return self.tournoi_joueurs
        def setTournoiJoueurs(self, tournoi_joueurs):
            self.tournoi_joueurs = tournoi_joueurs

        # ROUNDS LIST
        def getTournoiRoundsList(self):
            return self.tournoi_rounds_list
        def setTournoiRoundsList(self, tournoi_rounds_list):
            self.tournoi_rounds_list = tournoi_rounds_list
