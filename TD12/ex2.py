import numpy as np
import matplotlib.pyplot as plt


#contenu final
#pile, file, csv, tkinter, tracer courbe, tracer histogramme, base cours web

def main():
    image=plt.imread("Photo.png")
    dimension=image.shape
    print(dimension)
    #3 dimension
    #3 eme dimension = 3 pour les 3 courbes : vert, rouge, bleu
    #si =4, la 4 eme couche c est le degre de transparance

    hauteur, largeur, profondeur=image.shape
    cadre= np.zeros((hauteur*2, largeur*2, profondeur))


    #image jaune, couche bleu à zero
    img_jaune=image.copy()
    img_jaune[:,:,2]=0
    cadre[0:hauteur,0:largeur,:]=img_jaune

    #image bleu, couches vert et rouge a zero
    img_bleu=image.copy()
    img_bleu[:, :, 1] = 0
    img_bleu[:, :, 0] = 0   #ou en une fois 0:2 (2 non inclus)
    cadre[0:hauteur,largeur : 2* largeur,:]=img_bleu

    #image rouge, couches vert et jaunes
    img_rouge=image.copy()
    img_rouge[:, :, 1] = 0
    img_rouge[:, :, 2] = 0
    cadre[hauteur:2*hauteur, 0:largeur, :] = img_rouge

    #image verte
    img_verte=image.copy()
    img_verte[:, :, 0] = 0
    img_verte[:,:,2]=0  #en 1 fois : (0,2)
    cadre[hauteur:2*hauteur, largeur:2*largeur, :] = img_verte

    plt.imshow(cadre)
    plt.show()

if __name__ == "__main__":
    main()
