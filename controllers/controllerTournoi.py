# Authors: Jérémy Salettes-Wozniak 

# VIEWS: 
from views.viewTournoi import ViewTournoi
from views.viewJoueur import ViewJoueur
# MODELS:
from models.tournois import Tournoi
from models.joueurs import Joueur

# EXTERNAL LIBRARIES
import os
import re
import datetime
class ControllerTournoi:
    
    def __init__(self):
        self.name = "ControllerTournoi"
        self.view = ViewTournoi()
        self.viewJoueur = ViewJoueur()
        self.model = Tournoi
        self.modelJoueurs = Joueur

    def gestionTournoi(self, message = ""):
        """
            Méthode permettant de gérer le menu de gestion des tournois.

            Paramètres :
            ------------
            message : str
                Message à afficher en cas d'erreur
        """

        # Nettoyage de la console
        os.system("cls")

        # Affichage du menu de gestion des tournois
        self.view.gestionTournoi(message)

        # Logique de gestion du menu
        choix_valide = False
        while not choix_valide:
            # Choix de l'utilisateur
            choix = input("Veillez faire un choix : ")
            # Vérification de la validité du choix
            if choix in ["1", "2", "3", "4", "5", "6"]:
                # Si choix est valide on renvoie la méthode correspondante
                choix_valide = True
                # Si choix "1" : Créer un tournoi
                if choix == "1":
                    self.createTournoi()
                # Si choix "2" : Modifier un tournoi
                elif choix == "2":
                    self.updateTournoi()
                # Si choix "3" : Supprimer un tournoi
                elif choix == "3":
                    self.deleteTournoi()
                # Si choix "4" : Lance ou re
                elif choix == "4":
                    self.launchTournoi()
                # Si choix "5" : Gestion des joueurs du tournoi
                elif choix == "5":
                    self.gestionJoueurTournoi()
                # Si choix "6" : Menu principal
                elif choix == "6":
                    return False
            else:
                self.gestionTournoi("Veuillez faire un choix valide !")
        return True

    def createTournoi(self):
        # Nettoyage de la console
        os.system("cls")

        # Tournoi dictionary
        tournoi = {}

        # Nom du tournoi
        choixNom = False
        tournoiNom = input(self.view.demandeTournoiNom())
        while not choixNom:
            # Regex texte
            if re.match("^[A-Za-z0-9 ]*$", tournoiNom):
                choixNom = True
                tournoi["nom"] = tournoiNom
            else:
                tournoiNom = input(self.view.erreurTournoiNom())

        # Lieu du tournoi
        choixLieu = False
        tournoiLieu = input(self.view.demandeTournoiLieu())
        while not choixLieu:
            # Regex Majuscule au début
            if re.match("^[A-Z][a-z]*$", tournoiLieu):
                choixLieu = True
                tournoi["lieu"] = tournoiLieu
            else:
                tournoiLieu = input(self.view.erreurTournoiLieu())

        # Nombre de rondes du tournoi
        choixNombreRondes = False
        tournoiNombreRondes = input(self.view.demandeTournoiNombreRondes())
        while not choixNombreRondes:
            # Regex nombre entier
            if re.match("^[0-9]*$", tournoiNombreRondes):
                choixNombreRondes = True
                tournoi["nombreRondes"] = tournoiNombreRondes
            else:
                tournoiNombreRondes = input(self.view.erreurTournoiNombreRondes())

        # Description du tournoi
        choixDescription = False
        tournoiDescription = input(self.view.demandeTournoiDescription())
        while not choixDescription:
            # Regex texte
            if re.match("^[A-Za-z0-9 ]*$", tournoiDescription):
                choixDescription = True
                tournoi["description"] = tournoiDescription
            else:
                tournoiDescription = input(self.view.erreurTournoiDescription())

        # Sauvegarde du tournoi
        newTournoi = self.model(
            tournoi_nom = tournoi["nom"],
            tournoi_lieu = tournoi["lieu"],
            tournoi_nb_round = tournoi["nombreRondes"],
            tournoi_description = tournoi["description"]
        )
        newTournoi.saveTournoi()

        # Retourne au menu gestion du tournois 
        self.gestionTournoi()
        
    def updateTournoi(self):
        choixNomTournoi = False
        # Choix du nom du tournoi
        while not choixNomTournoi:
            # On demande le nom du tournoi à modifier
            nomTournoi = input(self.view.demandeTournoiNom())
            # On vérifie que le nom du tournoi existe
            if self.model.existeDansDB(self, nomTournoi) == True:
                # Si le nom du tournoi n'existe pas on affiche un message d'erreur
                print('Le nom du tournoi existe')
                choixNomTournoi = True
                #  Nettoyage de la console
                os.system("cls")
                # On affiche le menu de modification du tournoi
                self.view.updateTournoi()
                # Logique de gestion du menu
                choix_valide = False
                while not choix_valide:
                    # Choix de l'utilisateur
                    choix = input(self.view.demandeMenu())
                    # Vérification de la validité du choix
                    if choix in ["1", "2", "3", "4", "5", "6", "7"]:
                        # Si choix est valide on renvoie la méthode correspondante
                        choix_valide = True
                        # Si choix "1" : Modifier le nom du tournoi
                        if choix == "1":
                            choixNom = False
                            while not choixNom:
                                nomUpdate = input(self.view.demandeTournoiNom())
                                # Regex texte
                                if re.match("^[A-Za-z0-9 ]*$", nomTournoi):
                                    choixNom = True
                                    self.model.setNomTournoi(self, nomTournoi, nomUpdate)
                                    choix_valide = False
                                else:
                                    tournoiNom = input(self.view.erreurTournoiNom())
                        elif choix == "2":
                            choixLieu = False
                            while not choixLieu:
                                lieuUpdate = input(self.view.demandeTournoiLieu())
                                # Regex Majuscule au début
                                if re.match("^[A-Z][a-z]*$", lieuUpdate):
                                    choixLieu = True
                                    self.model.setLieuTournoi(self, nomTournoi, lieuUpdate)
                                    choix_valide = False
                                else:
                                    lieuUpdate = input(self.view.erreurTournoiLieu())
                        elif choix == "3":
                            choixNombreRondes = False
                            while not choixNombreRondes:
                                nombreRondesUpdate = input(self.view.demandeTournoiNombreRondes())
                                # Regex nombre entier
                                if re.match("^[0-9]*$", nombreRondesUpdate):
                                    choixNombreRondes = True
                                    self.model.setNombreRondesTournoi(self, nomTournoi, nombreRondesUpdate)
                                    choix_valide = False
                                else:
                                    nombreRondesUpdate = input(self.view.erreurTournoiNombreRondes())
                            
                        # Si choix "4" : Modifier la description du tournoi
                        elif choix == "4":
                            choixDescription = False
                            while not choixDescription:
                                descriptionUpdate = input(self.view.demandeTournoiDescription())
                                # Regex texte
                                if re.match("^[A-Za-z0-9 ]*$", descriptionUpdate):
                                    choixDescription = True
                                    self.model.setDescriptionTournoi(self, nomTournoi, descriptionUpdate)
                                    choix_valide = False
                                else:
                                    descriptionUpdate = input(self.view.erreurTournoiDescription())
                        elif choix == "5":
                            choix_valide = False
                    else:
                        self.gestionTournoi("Veuillez faire un choix valide !")
            else:
                choixNomTournoi = False
                
    def deleteTournoi(self):
        choixNomTournoi = False

        while not choixNomTournoi:
            choixNomTournoi = input(self.view.demandeTournoiNom())
            if self.model.existeDansDB(self, choixNomTournoi) == True:
                # On demande si il veut vraiment supprimer le tournoi
                choixConfirmation = input(self.view.confirmationTournoiDelete())
                if choixConfirmation == "O":
                    self.model.deleteTournoi(self, choixNomTournoi)
                    choixNomTournoi = True
                elif choixConfirmation == "N":
                    choixNomTournoi = False
                else:
                    choixNomTournoi = False

    def gestionJoueurTournoi(self, message = ""):
        choixNomTournoi = ""
        while not choixNomTournoi:
            choixNomTournoi = input(self.view.demandeTournoiNom(message))
            existeDansDB = self.model.existeDansDB(self, choixNomTournoi)
            if existeDansDB:
                choix = input(self.view.gestionJoueurTournoi())
                if choix in ['1', '2', '3']:
                    if choix == '1':
                        self.ajouterJoueur(choixNomTournoi)
                    elif choix == '2':
                        self.supprimerJoueur(choixNomTournoi)
                    elif choix == '3':
                        self.gestionTournoi()

    def ajouterJoueur(self, choixNomTournoi):
        choixIDNational = ""
        joueurInTournoi = self.model.checkJoueursTournoi(self, choixNomTournoi)
        while not choixIDNational:
            # On demande l'ID national du joueur
            choixIDNational = input(self.viewJoueur.demandeIDNational())
            # On vérifie que l'ID national est valide
            if re.match("^[A-Z]{2}[0-9]{5}$", choixIDNational):
                # On vérifie que le joueur existe dans la base de données
                existeDansDB = self.modelJoueurs.existeDansDB(self, "id_national", choixIDNational)
                if existeDansDB:
                    if len(joueurInTournoi) == 8:
                        self.gestionJoueurTournoi('Il y a déjà 8 joueurs dans le tournoi !')
                    else:
                        # Verifier que le joueur que j'ai rentrer n'est pas déja dans la liste
                        # Si il est dans la liste on affiche un message d'erreur
                        # Sinon on l'ajoute dans la liste
                        if self.model.checkJoueursTournoiByIDNatinal(self, choixIDNational, joueurInTournoi):
                            self.gestionJoueurTournoi('Le joueur est déjà dans le tournoi !')
                        else:
                            joueurInTournoi.append(choixIDNational)
                            self.model.addJoueurTournoi(self, choixNomTournoi, joueurInTournoi)
            else:
                self.gestionJoueurTournoi('Veuillez entrer un ID national valide !')
    
    # Supprimer un joueur du tournoi
    def supprimerJoueur(self, choixNomTournoi):
        # On recupère la liste des joueurs du tournoi
        listJoueurTournoi = self.model.checkJoueursTournoi(self, choixNomTournoi)
        # On demande quel joueur supprimer
        choixIDNational = ""
        while not choixIDNational:
            choixIDNational = input(self.viewJoueur.demandeIDNational())
            # On vérifie que l'ID national est valide
            if re.match("^[A-Z]{2}[0-9]{5}$", choixIDNational):
                # On vérifie que le joueur existe dans la base de données
                existeDansDB = self.modelJoueurs.existeDansDB(self, "id_national", choixIDNational)
                if existeDansDB:
                    # On vérifie que le joueur est bien dans la liste des joueurs du tournoi
                    if self.model.checkJoueursTournoiByIDNatinal(self, choixIDNational, listJoueurTournoi):
                        # On supprime le joueur de la liste
                        listJoueurTournoi.remove(choixIDNational)
                        # On met à jour la liste des joueurs du tournoi
                        self.model.addJoueurTournoi(self, choixNomTournoi, listJoueurTournoi)
                    else:
                        self.gestionJoueurTournoi('Le joueur n\'est pas dans le tournoi !')
            else:
                self.gestionJoueurTournoi('Veuillez entrer un ID national valide !')

    def launchTournoi(self, message = ""):
        choixNomTournoi = False
        while not choixNomTournoi:
            choixNomTournoi = input(self.view.demandeTournoiNom(message))
            if self.model.existeDansDB(self, choixNomTournoi) == True:
                # On demande si il veut vraiment lancer le tournoi
                choixConfirmation = input(self.view.confirmationTournoiLaunch(message))
                if choixConfirmation == "O":
                    # TODO: Il ne veut pas me retourner la liste des joueurs du tournoi
                    # On verifie qu'il y a bien 8 joueurs dans le tournoi
                    listJoueurTournoi = self.model.checkJoueursTournoi(self, choixNomTournoi)
                    if len(listJoueurTournoi) < 8:
                        self.launchTournoi('Il n\'y a pas 8 joueurs dans le tournoi !')
                    else:
                        # On lance le tournoi
                        self.tournoi(choixNomTournoi)
                elif choixConfirmation == "N":
                    self.gestionTournoi()
                else:
                    self.launchTournoi('Veuillez resaisir le nom du tournoi et O ou N lorsqu\'on vous le demande !')
            else:
                choixNomTournoi = False
                self.launchTournoi('Veuillez entrer un nom de tournoi valide !')

    def tournoi(self, choixNomTournoi):
        datetime_complete = datetime.datetime.now()
        # On créer tournoi_date_debut juste la date sans l'heure
        date = datetime_complete.strftime("%d/%m/%Y")
        self.model.setTournoiDateDebut(self, choixNomTournoi, date)
        # On créer tournoi_heure_debut
        heure = datetime_complete.strftime("%H:%M:%S")
        self.model.setTournoiHeureDebut(self, choixNomTournoi, heure)
        # On met à jour tournoi_status à "En cours"
        self.model.setTournoiStatus(self, choixNomTournoi, "En cours")

        # On verifie le round actuel du tournoi
        tournoi_round = self.model.getTournoiRound(self, choixNomTournoi)
        if tournoi_round == 0: 
            # On initialise le round 1
            self.round_one(choixNomTournoi, tournoi_round)
        else:
            # On initialise les autres rounds
            self.other_round(tournoi_round)

    def round_one(self, choixNomTournoi, tournoi_round):
        datetime_complete = datetime.datetime.now()
        # On créer tournoi_date_debut juste la date sans l'heure
        date = datetime_complete.strftime("%d/%m/%Y")
        self.model.setTournoiDateDebut(self, choixNomTournoi, date)
        # On créer tournoi_heure_debut
        heure = datetime_complete.strftime("%H:%M:%S")
        self.model.setTournoiHeureDebut(self, choixNomTournoi, heure)
        # On met à jour tournoi_status à "En cours"
        self.model.setTournoiStatus(self, choixNomTournoi, "En cours")
        # incrementer le round
        # On met à jour tournoi_round à 1
        self.model.setTournoiRound(self, choixNomTournoi, 1)
        # On Separe les joueurs en 2 groupes 
        # On récupère la liste des joueurs du tournoi
        listJoueurTournoi = self.model.checkJoueursTournoi(self, choixNomTournoi)
        self.separate_joueurs(listJoueurTournoi, "round_one", choixNomTournoi)

    def other_round(self, round_name):
        pass

    def separate_joueurs(self, listJoueurTournoi, round_name, choixNomTournoi):
        # Création des deux groupes de 4 joueurs
        groupe1 = []
        groupe2 = []
        # Répartition des joueurs dans les groupes
        for i in range(0, 4):
            groupe1.append(listJoueurTournoi[i])
        for i in range(4, 8):
            groupe2.append(listJoueurTournoi[i])
        # Création des matchs entre les joueurs des deux groupes
        matchs = []
        if (round_name == "round_one"):
            for i in range(0, 4):
                # Prend le premier joueur du groupe 1 et le dernier du groupe 2
                matchs.append([groupe1[i], groupe2[3-i]])
        else :
            pass
        self.saveMatch(matchs, round_name, choixNomTournoi)

    def saveMatch(self, matchs, round_name, choixNomTournoi):
        ###
        # tournoi_rounds_list = [
        #   round_name, 
        #   id_tournoi_rounds, 
        #       (
        #           id_match, 
        #           [player1, resultat_player1], 
        #           [player2, resultat_player2]
        #       )
        # ]
        ###
        # TODO: Phase 1
        # On récupère l'id du tournoi
        id_tournoi = self.model.getTournoiId(self, choixNomTournoi)
        
        # On créer l'id du round a partir de l'id du tournoi
        id_tournoi_rounds = id_tournoi +  id_tournoi
        # TODO: Phase 2
        matchs_turple = ()
        # On créer la turple qui contient les matchs
        i = 0
        for match in matchs:
            # Incrémente i
            i += 1
            # On créer l'id du match
            id_match = int(id_tournoi_rounds) + i
        
        # TODO: Phase 3
        # On créer les listes des matchs
            player1 = match[0]
            player2 = match[1]
            # On demande le résultat du match
            print("Une victoire vaut 1 point, une défaite 0 point et un match nul 0.5 point")
            resultat_player1 = input("Quel est le résultat du match entre " + player1 + " ?")
            resultat_player2 = input("Quel est le résultat du match entre " + player2 + " ?")
            # On créer deux liste du match
            match_player1 = [player1, resultat_player1]
            match_player2 = [player2, resultat_player2]

            # On ajoute à la turple les listes des matchs avec l'id du match
            matchs_turple += (id_match, match_player1, match_player2)

            # On sauvegarde le round_name, l'id du round et la turple qui contient les resultats des matchs
            self.model.saveMatch(self, choixNomTournoi, round_name, id_tournoi_rounds, matchs_turple)



        pass
        # # Pour chaque match on demande le résultat
        # for match in matchs:
        #     # Un match contient les joueurs qui s'affrontent
        #     # On demande le résultat du match
        #     player1 = match[0]
        #     player2 = match[1]
        #     print("Une victoire vaut 1 point, une défaite 0 point et un match nul 0.5 point")
        #     resultat_player1 = input("Quel est le résultat du match entre " + player1 + " ?")
        #     resultat_player2 = input("Quel est le résultat du match entre " + player2 + " ?")
        #     # On créer deux liste du match
        #     match_player1 = [player1, resultat_player1]
        #     match_player2 = [player2, resultat_player2]

        #     # O
        #     # On ajoute les résultats du match dans la base de données
        #     self.model.addMatch(self, round_name, match_player1, match_player2)