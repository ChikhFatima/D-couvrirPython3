#TP5 : Afficher une grille
#Exercice 3 : Developpez.com
#Src : https://allen-downey.developpez.com/livres/python/pensez-python/?page=fonctions#L3-12

import os

import numpy as np


def remplir_grille(n):

    a = [[' '] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j] = '+'
            elif i==0 & j!=j :
                a[i][j] = '-'

    for row in a:
        print(' '.join([str(elem) for elem in row]))

    return a


if __name__=="__main__":

    remplir_grille(5)






