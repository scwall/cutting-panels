class Cut_backboard:
    def __init__(self, backboard):
        self.coupe = {}
        self.calcul = ""
        self.backboard = backboard

    def calcul_coupe(self, longueur, largeur):
        self.coupe["longueur"] = longueur
        self.coupe["largeur"] = largeur

        calcul_1 = (int(self.backboard.get_longueur) / int(self.coupe["longueur"].values())) + \
                   (int(self.backboard.get_largeur) / int(self.coupe["largeur"].values()))
        calcul_2 = (int(self.backboard.get_longueur) / int(self.coupe["largeur"].values())) + \
                   (int(self.backboard.get_largeur) / int(self.coupe["longueur"].values()))

        if calcul_1 > calcul_2:
            self.calcul = "calcul_1"
            return calcul_1

        else:
            self.calcul = "calcul_2"
            return calcul_2


    def reste_coupe(self):
        if self.coupe.keys() == "calcul_1":
            self.backboard.set_longueur((int(self.backboard.get_longueur) % int(self.coupe["longueur"].values())))
            self.backboard.set_largeur((int(self.backboard.get_largeur) / int(self.coupe["largeur"].values())))

        if self.coupe.keys() == "calcul_2":
            self.backboard.set_longueur((int(self.backboard.get_longueur) / int(self.coupe["largeur"].values())))
            self.backboard.set_largeur((int(self.backboard.get_largeur) / int(self.coupe["longueur"].values())))
