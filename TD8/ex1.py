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

        self.configure(bg="gold")
        self.titile=("Exercice1")
        self.__label_welcome=Label(self, text="Bienvenue en INF2")
        self.__label_welcome.pack()
        self.__button_quit=Button(self, height=5,width=10,bg="red",fg="white",text="Quitter", command=self.destroy)
        self.__button_quit.pack()
        #self.button_quit.pack()

def main_exo1():
    largeur=int(input("Saisir la largeur : "))
    longueur=int(input("Saisir la longueur : "))
    fenetre=Fenetre(largeur, longueur)
    fenetre.mainloop()

if __name__ == '__main__':
    main_exo1()
