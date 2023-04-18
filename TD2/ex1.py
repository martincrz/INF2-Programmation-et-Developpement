def somme_chiffres(nbre):
    somme=0
    quotient=-2
    reste=0
    while quotient!=0 :
        quotient=nbre//10
        reste=nbre%10
        somme+= reste
        nbre=quotient
    return(somme)


#ou

def somme_chiffres(x:int) -> int:
    somme = 0
    x = str(x)
    for chiffre in x:
        somme += int(chiffre)
    return somme

#ou

def somme_chiffres(x:int) -> int:
    somme=0
    while x>0:
        somme+= x%10
        x=x//10
    return somme

def nombre_chiffres( nbre : int) -> int :
    return len(str(nbre))





def separe_nombre(x:int) -> tuple[int, int]:
    x_car=str(x)
    partie_g= int(x_car[0 : len(x_car) // 2])
    partie_d= int(x_car[len(x_car)//2 : len(x_car)])
    return(partie_g, partie_d)

if __name__ == "__main__":
    nombre = int(input('Saisir un entier : '))
    print(f"La somme de ses chiffres vaut {somme_chiffres(nombre)}")
    print(f"Le nombre de chiffre est de :  {nombre_chiffres(nombre)}")
    partie_g, partie_d =separe_nombre(nombre)
    print(f"On divise ce nombre en {partie_g} à gauche et {partie_d} à droite")

    if nombre_chiffres(nombre)%2 ==0 and somme_chiffres(partie_g)==somme_chiffres(partie_d):
        print('couicable')
