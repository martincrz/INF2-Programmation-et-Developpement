import os
import PIL

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
    try:
        n1 = Note("Ma note 1")
        a1 = Article("Mon article 1", "Texte de l'article")
        img1 = Image("Titre image", "Description image",
                     "D:\\Users\\jumelloi\\Documents\\Cours\\INF2\\A21\\TD8\\data\\ma_photo.png")
        doc1 = Document("Mon doc 1")
        doc1.ajouter_note(n1)
        doc1.ajouter_note(a1)
        doc2 = Document("Sous doc 1")
        doc2.ajouter_note(Note("Note de sous doc"))
        doc2.ajouter_note(Note("Note de sous doc 2"))
        doc2.ajouter_note(img1)
        doc1.ajouter_note(doc2)
        doc1.print()
        for note in doc1:
            print("debut for")
        print(note.titre)
        print("Fin for")
    except Exception as e:
        print(e)
