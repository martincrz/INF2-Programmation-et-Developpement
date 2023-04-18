import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


#image couleur
face_c= misc.face()
plt.imshow(face_c)
plt.show()
print(type(face_c), face_c.shape) # tableau 3D

face= misc.face(gray=True) #niveau de gris
plt.imshow(face, cmap=plt.cm.gray) # affiche en niveau de gris
plt.show()
print(type(face), face.shape) # tableau 2D

#q1

ligne, colonne=face.shape
c4=colonne//4
l4=ligne//4
zoom=face[l4:-l4, c4:-c4]
plt.imshow(zoom, plt.cm.gray)
plt.show()

#q2

contraste=np.copy(zoom)
contraste[zoom>210]=255
contraste[zoom<40]=0
plt.imshow(contraste, cmap=plt.cm.gray)
plt.show()

plt.hist(zoom.ravel(),bins=255, color='b')
plt.title("Histogramme des niveaux de gris")
plt.ylabel("Nb de pixels")
plt.xlabel("Niveau de gris")
plt.show()

#q3

val, nb = np.unique(zoom, return_counts=True)
#val est le tableau des différentes valeurs de zoom
#nb est le nbre d'occurences pour chaque valeur
somme_cum=np.cumsum(nb)
#somme_cum[i] est la valeur cumulée des i+1 premieres valeurs de nb
total_image=nb.sum()
total_classe=total_image//4
newval=somme_cum.copy()
#calculd de la nouvelle repartition
newval[somme_cum<total_classe]=0
newval[(somme_cum>=total_classe)&(somme_cum<total_classe*2)]=84
newval[(somme_cum>=total_classe*2)&(somme_cum<total_classe*3)]=168
newval[(somme_cum>=total_classe*3)]=255
#affectation des nouveaux niveaux de gris
contraste2=np.copy(zoom)
for i in range (0,zoom.shape[0]):
    for j in range (0,zoom.shape[1]):
        c=zoom[i,j]
        k=np.where(val==c)[0]
        contraste2[i, j]=newval[k]
