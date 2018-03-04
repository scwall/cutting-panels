import tkinter as tk


class CanvasPanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.taillePanneau = tk.LabelFrame(parent)
        self.taillePanneau.pack(fill="both", expand="yes")
        self.test = ""
        self.affichageTailleDuPanneau = tk.Label(self.taillePanneau, text='')
        self.affichageTailleDuPanneau.pack(side='top')
        self.canvas = tk.Canvas(self.taillePanneau, width=400, height=200, background='brown')
        self.canvas.pack()


class SizePanelHeightWidth(tk.Frame):
    def __init__(self, parent, canvas_panel, *args, **kwargs):
        self.canvas_panel = canvas_panel
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.box = tk.LabelFrame(parent, text="Taille de la planche")
        self.box.pack(fill="both", expand="yes")
        self.taillePanneauLongueurFrame = tk.LabelFrame(self.box, text="longueur", padx=2, pady=2)
        self.taillePanneauLongueurFrame.pack()
        self.taillePanneauLargeurFrame = tk.LabelFrame(self.box, text="largeur", padx=2, pady=2)
        self.taillePanneauLargeurFrame.pack()
        self.TaillePanneauvalueLongueur = tk.StringVar()
        self.TaillePanneauvalueLargeur = tk.StringVar()
        self.TaillePanneauentree = tk.Entry(self.taillePanneauLongueurFrame,
                                            textvariable=self.TaillePanneauvalueLongueur, width=30)
        self.TaillePanneauentree.pack()
        self.TaillePanneauentree = tk.Entry(self.taillePanneauLargeurFrame, textvariable=self.TaillePanneauvalueLargeur,
                                            width=30)
        self.TaillePanneauentree.pack()
        bouton = tk.Button(self.box, text="Valider", command=self.taille_panneau)
        bouton.pack()

    def taille_panneau(self):
        self.size_print = "largeur " + str(self.TaillePanneauvalueLargeur.get()) + " cm " + " longueur " + str(
            self.TaillePanneauvalueLongueur.get()) + " cm "
        self.canvas_panel.affichageTailleDuPanneau.config(text=self.size_print)


class CutSizePanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.box = tk.LabelFrame(parent, text="taille des coupes")
        self.box.pack(fill="both", expand="yes")

        self.longueurFrame = tk.LabelFrame(self.box, text="longueur", padx=2, pady=2)
        self.longueurFrame.pack()
        self.largeurFrame = tk.LabelFrame(self.box, text="largeur", padx=2, pady=2)
        self.largeurFrame.pack()
        self.valueLongueur = tk.StringVar()
        self.valueLargeur = tk.StringVar()

        self.entree = tk.Entry(self.longueurFrame, textvariable=self.valueLongueur, width=30)
        self.entree.pack()
        self.entree = tk.Entry(self.largeurFrame, textvariable=self.valueLargeur, width=30)
        self.entree.pack()

        self.listbox = tk.Listbox(self.box)
        self.bouton = tk.Button(self.box, text="Ajouter", command=self.recupere_mesure)
        self.bouton.pack()
        self.listbox.pack(fill="both", expand="yes")
        self.boutonn = tk.Button(self.box, text="Valider", command='validation')
        self.boutonn.pack()

    def recupere_mesure(self):
        if self.valueLargeur.get() != "" and self.valueLongueur.get() != "":
            test = " longueur " + self.valueLongueur.get() + " cm " + " largeur " + self.valueLargeur.get() + " cm "
            self.listbox.insert('end', test)

class MainApplication(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent, width=768, height=576)
        self.parent = parent
        self.canvas_panel = CanvasPanel(self)
        self.canvas_panel.pack(fill="y", expand="yes")
        self.size_panel_height_width = SizePanelHeightWidth(self, self.canvas_panel)
        self.size_panel_height_width.pack()
        self.cut_size_panel = CutSizePanel(self)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack()
    root.mainloop()
