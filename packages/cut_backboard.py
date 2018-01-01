class Cut_backboard:
    def __init__(self, backboard):
        self.coupe = {}
        self.calcul = ""
        self.backboard = backboard

    def calcul_coupe(self, longueur, largeur):

        self.coupe["longueur"] = float(longueur)
        self.coupe["largeur"] = float(largeur)
        global calcul_1
        global calcul_2
        calcul_total_1 = 0
        calcul_total_2 = 0
        nombre_inutile_coupe = lambda x: 1 if int(x) == 1 else x
        if  self.backboard.get_longueur >= self.coupe["longueur"] :

            calcul_1 = (float(self.backboard.get_longueur) / float(self.coupe["longueur"]))
            calcul_2 = nombre_inutile_coupe(float(self.backboard.get_largeur) / float(self.coupe["largeur"]))
            #print(calcul_1)
            #print(calcul_2)
            calcul_total_1 = int(calcul_1) * int(calcul_2)


        if self.backboard.get_largeur >= self.coupe["longueur"] :

            calcul_1 = (float(self.backboard.get_longueur) / float(self.coupe["largeur"]))
            calcul_2 = nombre_inutile_coupe(float(self.backboard.get_largeur) / float(self.coupe["longueur"]))
            #print(calcul_1)
            #print(calcul_2)
            calcul_total_2 = int(calcul_1) * int(calcul_2)



        if calcul_total_1 > calcul_total_2:
            self.calcul = "calcul_1"
            return calcul_total_1

        else:
            self.calcul = "calcul_2"
            return calcul_total_2



    def reste_coupe(self):
        nombre_inutile_reste = lambda x, total: total if int(x) == 0 else x
        if self.calcul == "calcul_1":
            self.backboard.set_longueur(nombre_inutile_reste((float(self.backboard.get_longueur) % float(self.coupe["longueur"])),self.backboard.get_longueur))
            self.backboard.set_largeur(nombre_inutile_reste((float(self.backboard.get_largeur) % float(self.coupe["largeur"])),self.backboard.get_largeur))

        if self.calcul == "calcul_2":
            self.backboard.set_longueur(nombre_inutile_reste((float(self.backboard.get_longueur) % float(self.coupe["largeur"])),self.backboard.get_longueur))
            self.backboard.set_largeur(nombre_inutile_reste((float(self.backboard.get_largeur) % float(self.coupe["longueur"])),self.backboard.get_largeur))



