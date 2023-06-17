class ViewMenu(object):

    def __init__(self):
        self.viewMenu = "viewMenu"


    def selectionMenu(self, message=''):
        print("Bienvenue dans le gestionnaire de tournoi !")
        print("--------------------------------------------")
        print("1 - Gestionnaire des tournois")
        print("2 - Gestionnaire des joueurs")
        print("3 - Gestionnaire des rapport")
        print("--------------------------------------------")
        if message != "":
            print(message)
