import numpy as np
import matplotlib.pyplot as plt


#contenu final
#pile, file, csv, tkinter, tracer courbe, tracer histogramme, base cours web

def main():
    dim=4
    R=np.random.randn(dim,dim)
    print(R)
    print(R.ravel())
    #ravel rend un ndarray a ndimension à une seule
    plt.hist(R.ravel(), bins=100)
    plt.show()
    M=R@R.T
    #M=R.dot(R.T)
    M_1=np.linalg.inv(M)
    I=np.eye(dim)
    if np.allclose(M@M_1,M_1@M) and np.allclose(M@M_1, I):
        print("Vrai")

if __name__ == "__main__":
    main()
