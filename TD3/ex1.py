class Date:

    def __init__(self, jour, mois, annee):
        self.setDate(jour,mois,annee)

    def __str__(self):
        return f"{self.__jour}/{self.__mois}/{self.__annee}"

    def setDate(self, j, m, a):
        if type(j)!=int or type(m)!=int or type(a)!=int:
            raise TypeError("Il faut 3 entiers pour initialiser une date")
        if m<=0 or m>12:
            raise ValueError("Mois incorrect")
        if m==2:
            if (a%100!=0 and a%4==0) or (a%400==0): #annee bissextile
                if j<=0 or j > 29:
                    raise ValueError(" Date incorrecte ")
            else:
                if j <= 0 or j > 28:
                    raise ValueError(" Date incorrecte ")
        elif (m in {4, 6, 9, 11} and j > 30) or (m in {1, 3, 5, 7, 8, 10, 12} and j > 31):
            raise ValueError("Date incorrecte")

        self.__jour = j
        self.__mois = m
        self.__annee = a


    def getJ(self):
        return self.__jour
    def getM(self):
        return self.__mois
    def getA(self):
        return self.__annee


    def setJ(self, j):
        self.__jour = j
    def setM(self,m):
        self.__mois = m
    def setA(self, a):
        self.__annee = a


    def jourDuLendemain(self):
        if self.__mois in {4, 6, 9, 11} and self.__jour==30 : #mois à 30jrs
            self.__jour=1
            self.__mois=self.__mois+1
        elif self.__mois in {1, 3, 5, 7, 8, 10} and self.__jour==31 : #mois à 31jrs
            self.__jour = 1
            self.__mois = self.__mois + 1
        elif self.__mois ==12 and self.__jour == 31: #cas 31 decembre
            self.__jour = 1
            self.__mois = self.__mois + 1
            self.__annee=self.annee+1
        elif self.__mois==2:    #cas février
            if ((self.__annee % 100 != 0 and self.__annee % 4 == 0) or (self.__annee % 400 == 0)) and self.__jour==29:
                self.__jour = 1
                self.__mois = self.__mois + 1
            elif self.__jour==28:
                self.__jour = 1
                self.__mois = self.__mois + 1
        else:
            self.__jour=self.__jour+1
        return(f"{self.__jour}/{self.__mois}/{self.__annee}")


def main():
    aujourdhui=Date(31,3,2022)
    print(aujourdhui)
    if isinstance(aujourdhui, Date):
        print(f"{aujourdhui} est bien une instance de date")
    print(aujourdhui.jourDuLendemain())

    print("\n\n")
    d=Date(1,1,2022)
    print(d, end=" ")

    while (d.getM()!=12 and d.getJ()!=31):
        print(d.jourDuLendemain(), end=" ")
        if (d.getM() in {1, 3, 5, 7, 8, 10}) and (d.getJ()==31) :
            print()
        if (d.getM() in {4, 6, 9, 11}) and (d.getJ()==30) :
            print()



if __name__ == '__main__':
    main()
