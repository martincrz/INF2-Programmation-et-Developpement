from tkinter import*

class Echiquier(Tk):
    def __init__(self, n=8, c=40):
        Tk.__init__(self)

        largeur_cadre=20

        largeur = n*c + 2*largeur_cadre
        longueur = n*c + 2*largeur_cadre
        pos_x = self.winfo_screenwidth() // 2 - largeur // 2
        pos_y = self.winfo_screenheight() // 2 - longueur // 2
        geometrie = f"{largeur}x{longueur}+{pos_x}+{pos_y}"
        self.geometry(geometrie)

        canvas=Canvas(self, width=n*c, height=n*c, bg='white', highlightthickness=largeur_cadre, highlightcolor='skyblue')
        canvas.pack()

        #creation des rectangles
        for i in range(n):
           for j in range(n):
                if (i+j)%2==0:
                    couleur="black"
                else :
                    couleur="white"
                canvas.create_rectangle(j*c+largeur_cadre,i*c+largeur_cadre,(j+1)*c+largeur_cadre,(i+1)*c+largeur_cadre,fill=couleur, width=2)

def main_exo4():
    echiquier=Echiquier()
    echiquier.mainloop()

if __name__ == '__main__':
    main_exo4()
