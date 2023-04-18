import os
import PIL

#import TD5.py
class Note:
    def __init__(self, titre):
        #il faut un constructeur qui initie cette attribut
        self.titre=titre

    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, titre):
        if not type(titre) == str:
            raise TypeError("Le titre doit être une chaîne de caractères")
        self.__titre = titre

    def print(self):
        print(f"Titre = {self.titre}")
class Article(Note):
    def __init__(self, titre, txt):
        Note.__init__(self, titre) #ou super().__init__(titre)

        self.texte=txt
    @property
    def texte(self):
        return self.__texte

    @texte.setter
    def texte(self, texte):
        if not type(texte) == str:
            raise TypeError("Le texte doit être une chaîne de caractères")

        self.__texte = texte

    def print(self):
        super().print()

        print(f" Texte = {self.texte}")
class Image(Note):
    def __init__(self, titre, description, fichier):
        super().__init__(titre)
        self.description = description
        self.fichier = fichier

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        if not type(description) == str:
            raise TypeError("La description doit être une chaîne de caractères")
        self.__description = description

    @property
    def fichier(self):
        return self.__fichier
    @fichier.setter
    def fichier(self, fichier):
        if not os.path.isfile(fichier):
            raise FileNotFoundError("Le fichier n'existe pas")
        self.__fichier = fichier

    def print(self):
        super().print()
        print(f" Description : {self.description}")
        img = PIL.Image.open(self.fichier)
        img.show()
class Document(Note):
    def __init__(self, titre):
        super().__init__(titre)
        self.__grp_notes = []
    def ajouter_note(self, note):
        if note == self:
            raise ValueError("Récursion")
        if not isinstance(note, Note):
            raise TypeError("L'objet doit être de type Note ou en hériter")
        self.__grp_notes.append(note)
    def supprimer_note(self, note):
        self.__grp_notes.remove(note)
    def print(self):
        super().print()
        for note in self.__grp_notes:
            note.print()

if __name__ == '__main__':
    #try:
        list_note=[]
        with open("fichier.txt", "r") as f:
            texte=f.readlines()
            for ligne in texte:
                elem=ligne.split(";")
                if elem[0]=="Note":
                    note=Note(elem[1])
                    list_note.append(note)
                if elem[0]=="Article":
                    note=Article(elem[1], elem[2])
                    list_note.append(note)
                if  elem[0]=="Image":
                    note=Image(elem[1], elem[2], elem[3])
                    list_note.append(note)
                if elem[0] == "Document":
                    note = Document(elem[1])
                    for i in range (2,len(elem)-1):
                        note.ajouter_note(list_note(i-1)) #je pense erreur:list_note[elem(i-1)]
                        #on ajoute dans le document la note de la ligne 1 et ligne 3
                    list_note.append(note)
            for objet in list_note:
                objet.print()



