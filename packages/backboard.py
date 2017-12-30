class Backboard():
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.reste_longueur = ""
        self.reste_largeur = ""

    @property
    def taille_panneau(self):
        return "largeur " + self.largeur + " cm " + " longueur " + self.longueur + " cm "

    @property
    def get_longueur(self):
        return self.longueur

    @property
    def get_largeur(self):
        return self.largeur

    def set_longueur(self, longueur):
        self.longueur = longueur

    def set_largeur(self, largeur):
        self.largeur = largeur
