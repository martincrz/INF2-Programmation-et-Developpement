import collections
import random

def elimination(list):

    while len(list)!=1:
        nb_passes = random.randint(0, 10)
        list.rotate(-nb_passes)
        print(f"Joueur {list[0]} eliminé")
        list.popleft()
    print(f"\nLe vainqueur est {list[0]}\n")

def elimination2(list):
    compteur = random.randint(5, 60)
    print(f"La partie commence : vous avez {compteur} secondes\n")
    while len(list)!=1:
        while compteur >0:
            nb_secondes = random.randint(1, 4)
            list.rotate(-1)
            compteur-=nb_secondes
        print(f"Joueur {list[0]} eliminé")
        list.popleft()
    print(f"Le vainqueur est {list[0]}")

def exo4():
    list_noms=collections.deque(["Pierre", "Luc", "Marie", "Yvan", "Eva","Jason","Agathe"])
    elimination(list_noms)
    print("***********************")
    list_noms2 = collections.deque(["Pierre", "Luc", "Marie", "Yvan", "Eva", "Jason", "Agathe"])
    elimination2(list_noms2)
    print("***********************")


if __name__ == '__main__':
    exo4()
