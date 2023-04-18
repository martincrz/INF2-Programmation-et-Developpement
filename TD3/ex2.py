class Horaire:

    def __init__(self, heure, minute):
        self.heures = heure
        self.minutes = minute
    # PLUS D UNDERSCORE : sinon on peut mettre ce qu'on veut dedans, sans verif conditions
    #si on ne veut pas de setter, faire le getter et mettre les underscores ici

    #notes annales : afficher les erreures > print, relever les erreur > raise Exception (erreur gen)

    @property
    def heures(self):
        return self.__heures
    @heures.setter
    def heures(self, h):
        if type(h)!=int : #not isinstance(h, int):
            raise TypeError("Il faut des entiers pour initialiser une horaire")
        if h<0 or h>23:
            raise ValueError("Heure incorrect")
        self.__heures=h

    @property
    def minutes(self):
        return self.__minutes
    @minutes.setter
    def minutes(self, m):
        if type(m)!=int :
            raise TypeError("Il faut des entiers pour initialiser une horaire")
        if m<0 or m>60:
            raise ValueError("Minutes incorrect")
        self.__minutes=m

    def __str__(self):
        return f"{self.heures}h{self.minutes}"
    # PLUS D UNDERSCORE

    def __add__(self, duree):
        tot_min= (duree.heures + self.heures) * 60 + self.minutes + duree.minutes
        return Horaire((tot_min //60)%24, tot_min % 60)

class Duree:

    def __init__(self, heure, minute):
        self.heures = heure
        self.minutes = minute

    @property
    def heures(self):
        return self.__heures
    @heures.setter
    def heures(self, h):
        if type(h)!=int : #not isinstance(h, int):
            raise TypeError("Il faut des entiers pour initialiser une horaire")
        if h<0:
            raise ValueError("Heure incorrect")
        self.__heures=h

    @property
    def minutes(self):
        return self.__minutes
    @minutes.setter
    def minutes(self, m):
        if type(m)!=int :
            raise TypeError("Il faut des entiers pour initialiser une horaire")
        if m<0 or m>60:
            raise ValueError("Minutes incorrect")
        self.__minutes=m

    def __str__(self):
        return f"{self.heures}h{self.minutes}"

class Vol:
    def __init__(self, nom, h_dep, duree):
        self.nom=nom              #pas obliger de les mettre en prive mias on peut
        self.h_dep=h_dep
        self.duree=duree
        self.h_arr=h_dep + duree

    def __str__(self):
        return f"Vol : {self.nom}  \nDépart : {self.h_dep} \nArrivée : {self.h_arr} \n"

def main():
    print ("Choisir les caractéristiques du vol")
    nom=str(input("Nom: "))
    print("Horaire de départ")
    h_deph=int(input("Heure:"))
    m_depm=int(input("Minute: "))
    h_dep=Horaire(h_deph,m_depm)
    print("Durée :")
    d_deph=int(input("Heure:"))
    d_depm=int(input("Minute: "))
    d_vol=Duree(d_deph,d_depm)
    vvvol=Vol(nom, h_dep,d_vol)
    print(vvvol)

    h1 = Horaire(10,35)
    d1 = Duree(15,10)
    d_fin = h1 + d1 #MARCHE QUE DANS UN SENS, IL FAUT DEF LE ADD DANS LES DEUX CLASSES SINON
    print(f"{d_fin.heures}h{d_fin.minutes}")

    vol=Vol("AZBUINK02BKABD", h1, d1)
    vol.nom #nom du vol
    vol.h_dep # Horaire de départ (classe horaire)
    vol.h_dep.heures #heures de l'horaire de départ
    print(vol)


if __name__ == '__main__':
    main()
