#Afficher sur un graphique le résultat de la fonction 3D : z = sin(r) avec r la distance du point (x,y) à l'origine

import numpy as np
import matplotlib.pyplot as plt
from math import*

#contenu final
#pile, file, csv, tkinter, tracer courbe, tracer histogramme, base cours web

def main():
    x = np.linspace(0, 2, 10)
    y = x ** 2
    plt.plot(x, y)
    plt.show()

    plt.scatter(x, y)
    plt.show()

    figure=plt.figure()
    ax=figure.add_subplot(projection="3d")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    #plages de valeurs pour x, y
    #deux ndarray 1D (-5 a 5 pas 0.1)
    x=np.arange(-5,5.1,0.1)
    #pour 200 points entre -5 et 5 : np.linspace(-5,5,200)
    y=np.arange(-5,5.1,0.1)


    #conversion de x et y pour le miallage de plot_surface en 2D
    X,Y=np.meshgrid(x,y)

    #calculer valeur de z pour chaque point
    Z=np.sin(np.sqrt(X**2 + Y**2))


    ax.plot_surface(X,Y,Z, cmap='plasma')


    plt.show()

if __name__ == "__main__":
    main()
