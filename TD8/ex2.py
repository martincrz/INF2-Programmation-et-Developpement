from tkinter import*



class Fenetre(Tk):
    def __init__(self, largeur=100, longueur=100):
        Tk.__init__(self)
        self.largeur=largeur
        self.longueur=longueur

        ecran_x = self.winfo_screenwidth()
        ecran_y = self.winfo_screenheight()
        pos_x = ecran_x // 2 - largeur // 2
        pos_y = ecran_y // 2 - longueur // 2

        geometrie = f"{largeur}x{longueur}+{pos_x}+{pos_y}"
        self.geometry(geometrie)

        #self.configure(bg="grey")
        self.title=("Exercice2")
        self.creation_labels()
        self.creation_boutons()
        self.creation_entry()

        # appel valider dès qu on modifie un des parametres
        #self.__txt_prenom.trace('w', self.valider)
        #self.__txt_nom.trace('w', self.valider)
        #self.__txt_domaine.trace('w', self.valider)

        #photo
        self.__photo=Canvas(self, width=60, height=60)
        self.__p=PhotoImage(file="lien photo")
        self.__photo.create_image(60,60, image=self.__p)
        self.__photo.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

    def creation_labels(self):
        self.__prenom=Label(self, text="Prénom : ")
        self.__prenom.grid(row=1, column=1, padx=10, pady=10)
        self.__nom = Label(self, text="Nom : ")
        self.__nom.grid(row=2, column=1, padx=10, pady=10)
        self.__domaine = Label(self, text="Domaine : ")
        self.__domaine.grid(row=3, column=1, padx=10, pady=10)

        self.__txt_prenom = StringVar()
        self.__lab_prenom = Label(self, textvariable=self.__txt_prenom)
        self.__txt_nom = StringVar()
        self.__lab_nom = Label(self, textvariable=self.__txt_nom)
        self.__txt_domaine = StringVar()
        self.__lab_domaine = Label(self, textvariable=self.__txt_domaine)
        self.__txt_adresse=StringVar()
        self.__lab_adresse = Label(self, textvariable=self.__txt_adresse)
        self.__lab_adresse.grid(row=4, column=1, columnspan=3)

    def creation_entry(self):
        self.__entry_prenom=Entry(self, textvariable=self.__txt_prenom)
        self.__entry_prenom.grid(row=1, column=2,padx=10, pady=10)
        self.__entry_nom = Entry(self, textvariable=self.__txt_nom)
        self.__entry_nom.grid(row=2, column=2, padx=10, pady=10)
        self.__entry_domaine = Entry(self, textvariable=self.__txt_domaine)
        self.__entry_domaine.grid(row=3, column=2, padx=10, pady=10)

    def creation_boutons(self):
        self.__button_valid = Button(self, text="Valider",command=self.valider)
        self.__button_valid.grid(row=5, column=1, padx=10, pady=10)
        self.__button_reinit = Button(self, text="Réinitialiser", command=self.reinit)
        self.__button_reinit.grid(row=5, column=2, padx=10, pady=10)
        self.__button_quit=Button(self,text="Quitter", command=self.destroy)
        self.__button_quit.grid(row=5, column=3, padx=10, pady=10)

    def valider(self):
        self.__txt_adresse.set(f"{self.__txt_prenom.get()}.{self.__txt_nom.get()}@{self.__txt_domaine.get()}")

    def reinit(self):
        self.__txt_prenom.set("")
        self.__txt_nom.set("")
        self.__txt_domaine.set("")
        self.__txt_adresse.set("")

def main_exo1():
    #largeur=int(input("Saisir la largeur : "))
    #longueur=int(input("Saisir la longueur : "))
    fenetre=Fenetre(400, 400)
    fenetre.mainloop()

if __name__ == '__main__':
    main_exo1()
