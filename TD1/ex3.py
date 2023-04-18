
liste=[]
nb_valeurs=int(input("Choisir le nbre de valeurs à entrer : "))
for i in range(1, nb_valeurs+1):
    print("entrer la valeur ",i," : ",end="")
    n=float(input(""))
    liste.append(n)
print(liste)


somme=0
maximum=0
minimum=100
for i in range(0, len(liste)):
    somme=somme+liste[i]
    if liste[i]>maximum:
        maximum=liste[i]
    if liste [i]<minimum:
        minimum=liste[i]
print("La moyenne de cette liste est de ", (somme)/len(liste),".")
print("La moyenne centrée de cette liste est de ", (somme - maximum - minimum) / (len(liste)-2), ".")

proche=40
for i in range(0, len(liste)):
    if abs(liste[i])<abs(proche):
        proche=liste[i]
print("La valeur la plus proche de 0 est", proche," .")

