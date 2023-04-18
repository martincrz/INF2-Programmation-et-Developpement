
def nombre(f):
    def fonction_decore(n):
        if type(n)!=int:
            return f(n)

        if type(n)==str and n.isdigit():
            return f(int(n));

        else:
            raise TypeError("Fonction n'est ni un nombre ni une chaine de caractere")

    return fonction_decore()

@nombre
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

if __name__ == '__main__':
    main()
