class Graphe:


    def __init__(self, nom):
        self.__nom=nom
        self.__succ=dict()
            #dictionnaire : clé=Sommet, valeur = ensemble (set) de sommets

    def get_nom(self):
        return self.__nom

    def get_nb_sommets(self):
        return len(self.__succ)

    def get_nb_arcs(self):
        n = 0
        for s, e in self.__succ.items():
            n += len(e)
        return n

    def __str__(self):
        g = f"Graphe {self.get_nom()}: {self.get_nb_sommets()} sommets, {self.get_nb_arcs()} arcs\n"

        for sommet, succ in self.__succ.items():
            g += f"{sommet} : "
            for item in succ:
            g += f"{item} "
        g += "\n"
        return g

    def __iadd__(self, x):
        # On vérifie le type passé en paramètres
        if isinstance(x, Sommet):
            if not self.__succ.get(x, False):
                self.__succ[x] = set()  # on ajoute le sommet x[0] en l'associant à un ensemble vide
        elif isinstance(x, tuple):
            if len(x) != 2:
                raise ValueError("Erreur : un arc est un tuple de deux sommets")
        i, j = x
        if not isinstance(i, Sommet) or not isinstance(j, Sommet):
            raise TypeError("Les éléments d'un arc doivent être des sommets")
        # ajout de j dans la liste des successeurs de i
        if not self.__succ.get(i, False):
            self.__succ[i] = {j}  # 1ère entrée dans les successeurs de i
        else:
            self.__succ[i].add(j)  # ajout de j dans les successeurs de j
        if not self.__succ.get(j, False):  # si j n'a pas encore d'entrée, on en crée une
            self.__succ[j] = set()
        else:
            raise TypeError("Erreur : on peut seulement ajouter un Sommet ou un arc dans le graphe")
        return self  # ne pas oublier sinon ça marche pas



if __name__ == '__main__':
    g = Graphe("G1", {"A": ["C", "D"]})
    print(g)

