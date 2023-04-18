import numpy as np
import matplotlib.pyplot as plt
import random

def question1_1(n, m):
    M= np.random.randint(0, 10, [n, m])
    N=np.ones((n,1))
    C=np.concatenate((M,N), axis=1) #C=np.hstack((M,N))
    print(C)

def question1_2(n):
    #A=np.zeros((n,n))
    #for i in range (3,n-3):
    #    for j in range (3,n-3):
    #        A[i,j]=random.random()
    R=np.random.randint(0,255,[n,n])
    Z=np.zeros((n+6,n+6))
    Z[3:n+3,3:n+3]=R
    plt.imshow(Z, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

def question2_1():
    print("slt")


def main_td11():
    question1_2(78)

if __name__=='__main__':
    main_td11()
