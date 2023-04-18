def somme_ligne(mat: list[list[int]], i :int) -> int:
    return sum(mat[i])

def somme_colonne(mat: list[list[int]], j :int) -> int:
    somme=0
    for ligne in mat:
        somme += ligne[j]
    return somme
# ou return sum([ligne[j] for ligne in mat])

def somme_diag1(mat: list[list[int]])-> int:
    return sum([mat[i][i] for i in range(len(mat))])

def somme_diag2(mat: list[list[int]]) -> int:
    return sum([mat[i][-i-1] for i in range(len(mat))])

def magique(mat_c: list[list[int]]) -> bool:
    test = somme_ligne(mat_c,1)
    for i in range(1, len(mat_c)):
        if somme_ligne(mat_c,i)!=test or somme_colonne(mat_c,i)!=test:
            return False
        elif somme_diag1(mat_c)!=test or somme_diag2(mat_c)!=test:
            return False
        else:
            return True

def affiche_test_cm(*args):
    for mat in args:
        if magique(mat):
            print('Magique')
        else:
            print('Normal')



if __name__ == "__main__":
    Carre= [ [21, 7, 17] , [11, 15, 19] , [13, 23, 9] ]
    C1 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    C2 = [[21, 7, 17], [11, 15, 19], [13, 23, 9]]
    C3 = [[30, 39, 48, 1, 10, 19, 28], [38, 47, 7, 9, 18, 27, 29],
          [46, 6, 8, 17, 26, 35, 37], [5, 14, 16, 25, 34, 36, 45],
          [13, 15, 24, 33, 42, 44, 4], [21, 23, 32, 41, 43, 3, 12],
          [22, 31, 40, 49, 2, 11, 20]]

    print(somme_ligne(Carre, 1))
    print(somme_colonne(Carre, 1))
    print(somme_diag1(Carre))
    print(somme_diag2(Carre))

    if magique(Carre):
        print("C'est bien un carré magique")
    else:
        print("Matrice normal")

    affiche_test_cm(C1, C2, C3)




