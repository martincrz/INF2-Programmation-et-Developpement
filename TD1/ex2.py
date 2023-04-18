def creation_liste(a, liste):
    for i in range(2,16):
        k=i
        while a % k == 0:
            if k not in liste:
                liste.append(k)
            k=k*k

def main():
    liste_div_n=[1]
    liste_div_m=[1]

    n=int(input("Choisir n : "))
    m=int(input("Choisir m : "))
    creation_liste(n, liste_div_n)
    creation_liste(m, liste_div_m)

    liste_div_commun = [element for element in liste_div_n if element in liste_div_m]
    print("Voici la liste des diviseurs communs de ", n, " et de ", m," : ",liste_div_commun)

if __name__ == '__main__':
        main()
