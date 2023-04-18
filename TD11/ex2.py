import numpy as np
import matplotlib.pyplot as plt



def graphique1(exp:dict):
    l=len(exp["exp_0"])
    x=np.linspace(0,l,l)
    fig, axs = plt.subplots(len(exp), 1 , sharex=True)
    for i in range (0, len(exp)):
        axs[i].plot(x, exp[f"exp_{i}"])

    plt.show()

def graphique2(exp:dict):
    fig, ax=plt.subplots()
    for cle, valeur in exp.items():
        liste_x=np.arange(len(valeur))
        ax.plot(liste_x,valeur, label=cle)
    ax.legend()
    plt.show()

def affiche_stat(exp:dict):
    num_exp=0
    for experience in exp.values():
        print(f"Le maximum de l'experience {num_exp} est {max(experience)}")
        print(f"Le minimum de l'experience {num_exp} est {min(experience)}")
        print(f"La moyenne de l'experience {num_exp} est {np.mean(experience)}")
        print(f"L ecart type de l'experience {num_exp} est {np.std(experience)}")
        print("**************************************************************")
        num_exp+=1

def graphique3(exp:dict):
    liste=[]
    for  valeur in exp.values():
        liste.append(valeur)

    x=np.array(liste)
    abs=np.arange(0,x.shape[1],1)
    y1=x.mean(axis=0)
    y2=x.var(axis=0)
    y3=x.max(axis=0)
    y4=x.min(axis=0)
    fig, ax=plt.subplots()
    ax.plot(abs, y1, label="moyenne")
    ax.plot(abs, y2, label="variance")
    ax.plot(abs, y3, label="max")
    ax.plot(abs, y4, label="min")
    ax.legend()
    fig.show()


def exo2():
    nb_exp=int(input("Entre nbre d experiences : "))
    nb_val=int(input("Entre nbre de données par expériences : "))
    print()
    exp=dict()
    for i in range (0,nb_exp):
        exp[f"exp_{i}"]=np.random.rand(nb_val)
    #graphique1(exp)
    #graphique2(exp)
    #affiche_stat(exp)
    graphique3(exp)


if __name__=='__main__':
    exo2()
