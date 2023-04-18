from tkinter import*
from tkinter import messagebox
import random

class Fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        #Centrer et taille fenetre
        largeur=300
        longueur=240
        ecran_x = self.winfo_screenwidth()
        ecran_y = self.winfo_screenheight()
        pos_x = ecran_x // 2 - largeur // 2
        pos_y = ecran_y // 2 - longueur // 2
        geometrie = f"{largeur}x{longueur}+{pos_x}+{pos_y}"
        self.geometry(geometrie)

        self.title = "Exo 2"
        self.creation_labels_boutons()
        #self.ma_version()
        self.__nb_c = 0
        self.afficher_coup()


    def creation_labels_boutons(self):
        self.__titre = Label(self, text="Jeu du 421 ")
        self.__titre.grid(row=0, column=1)

        #POUR EVITER LES REPETITIONS ON PEUT UTILISER LAMBDA, UNE BOUCLE FOR ET DICTIONNAIRES
        #EXEMPLE AVEC BOUCLE FOR, DICTIONNAIRES, ET LAMBDA (LAMBDA AUSSI DANS CORRECTION TP CALCULATRICE)

        self.__but_lancer_de = dict() #boutons de lancés
        self.__valeur_de = dict() #valeurs des dés
        self.__valeur_str_de = dict() #StringVar égale à la valeur des dés
        self.__lab_valeur_de = dict() #labels qui affichent la valeur des dés
        self.__appel = dict() #fonctions à appeler quand on clique sur les boutons

        self.__appel[1] = lambda: (self.lancer(1))
        self.__appel[2] = lambda: (self.lancer(2))
        self.__appel[3] = lambda: (self.lancer(3))
        self.__nb_coups=0
        self.__nb_coups_str=StringVar()
        self.__lab_nb_coups=Label(self, textvariable=self.__nb_coups_str, fg='blue').grid(row=4, column=0, padx=10, pady=10)


        # creation des éléments pour le dé num i
        for i in range(1, 4):
            self.__but_lancer_de[i] = Button(self, text=f"Lancé dé {i}", command=self.__appel[i]).grid(row=i, column=0, padx=10, pady=10)
            self.__valeur_de[i]=0
            self.__valeur_str_de[i]=StringVar()
            self.__valeur_str_de[i].set("-->")
            self.__lab_valeur_de[i] = Label(self, textvariable=self.__valeur_str_de[i], fg='red').grid(row=i, column=1, padx=10, pady=10)

        self.__button_quit = Button(self, text="Quitter", command=self.destroy)
        self.__button_quit.grid(row=4, column=1, padx=10, pady=10)

    def lancer(self, i):
        self.__valeur_de[i]=random.randint(1,6)
        self.__valeur_str_de[i].set(f"-->{self.__valeur_de[i]}")
        self.__nb_coups+=1
        self.__nb_coups_str.set(f"Nb coups= {self.__nb_coups}")
        chiffres=set()
        for i in range(1,4):
            chiffres.add(self.__valeur_de[i])
        if chiffres == {1,2,4}:
            messagebox.showinfo("Bravo : 421")



    def ma_version(self):
        self.__titre = Label(self, text="Jeu du 421 ")
        self.__titre.grid(row=1, column=2)

        self.__lancerde1=Button(self, text="lancer dé 1",command=self.lancerde1)
        self.__lancerde1.grid(row=2, column=1, padx=10, pady=10)
        self.__lancerde2 = Button(self, text="lancer dé 2", command=self.lancerde2)
        self.__lancerde2.grid(row=3, column=1, padx=10, pady=10)
        self.__lancerde3 = Button(self, text="lancer dé 3", command=self.lancerde3)
        self.__lancerde3.grid(row=4, column=1, padx=10, pady=10)
        self.__button_quit = Button(self, text="Quitter", command=self.destroy)
        self.__button_quit.grid(row=5, column=2, padx=10, pady=10)

        self.__result1=StringVar()
        self.__r1 = Label(self, textvariable=self.__result1)
        self.__entry_r1 = Entry(self, textvariable=self.__result1)
        self.__entry_r1.grid(row=2, column=2, padx=10, pady=10)

        self.__result2 = StringVar()
        self.__r2 = Label(self, textvariable=self.__result2)
        self.__entry_r2 = Entry(self, textvariable=self.__result2)
        self.__entry_r2.grid(row=3, column=2, padx=10, pady=10)

        self.__result3 = StringVar()
        self.__r3 = Label(self, textvariable=self.__result3)
        self.__entry_r3 = Entry(self, textvariable=self.__result3)
        self.__entry_r3.grid(row=4, column=2, padx=10, pady=10)

    def afficher_coup(self):
        self.__nb_coup = StringVar()
        self.__nb_coup.set(f"Nb coups = {self.__nb_c}")
        self.__nb= Label(self, textvariable=self.__nb_coup)
        self.__entry_nb_coup = Entry(self, textvariable=self.__nb_coup)
        self.__entry_nb_coup.grid(row=5, column=1, padx=10, pady=10)

    def lancerde1(self):
        self.__nb_c+=1
        self.__nb_coup.set(f"Nb coups = {self.__nb_c}")
        self.__result1.set("-->" + str(random.randint(1,6)))
        self.test()


    def lancerde2(self):
        self.__nb_c += 1
        self.__nb_coup.set(f"Nb coups = {self.__nb_c}")
        self.__result2.set("-->" + str(random.randint(1, 6)))
        self.test()

    def lancerde3(self):
        self.__nb_c += 1
        self.__nb_coup.set(f"Nb coups = {self.__nb_c}")
        self.__result3.set("-->" + str(random.randint(1,6)))
        self.test()

    def test(self):
        if self.__result.get()=="-->4" and self.__result2.get()=="-->2" and self.__result3.get()=="-->1":
            self.__victoire=Label(self, text="VICTOIRE")
            self.__victoire.grid(row=1, column=2, rowspan=5, columnspan=5)
            print("Victoire")
        print("Test")

def main_exo3():
    fenetre = Fenetre()
    fenetre.mainloop()

if __name__ == '__main__':
    main_exo3()
