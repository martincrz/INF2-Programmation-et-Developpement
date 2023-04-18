class Sommet:
    __nb_sommets = 0

    def __init__(self, id):
        if hash(id)!= None:
            self.__id=id
        Sommet.__nb_sommets += 1

    def get_id(self):
        return self.__id
    #on ne veut pas de setter
    #@property
    #def id(self):
        #return self.__id

    def __str__(self):
        return f"Id = {self.__id}"

    def __del__(self):
        Sommet.__nb_sommets -= 1

    #getter d'un attribut de classe : décorateur staticmethod facultatif
    @staticmethod
    def get_nb_sommets():
        return Sommet.__nb_sommets

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        return self.get_id()==other.get-id()

if __name__ == '__main__':
    n1 = Sommet("INF2")
    n2 = Sommet(26)
    n3 = Sommet("INF1")
    print(f"nb sommets={Sommet.get_nb_sommets()}")  # 3 sommets
    del (n2)  # destruction du sommet n2
    print(f"nb sommets={Sommet.get_nb_sommets()}")  # 2 sommets
    print(hash(n1))

    #1.4
    try :
        s1=Sommet([1,2,3])
        s2=Sommet("A")
        s3=Sommet("B")
        s4=Sommet(42)
    except TypeError as erreur:
        print("Les nombres doivent être hashuable")
    else:
        print("Sommets créés")
    finally:
        print("Continuez")
