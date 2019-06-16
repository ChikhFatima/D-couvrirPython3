#TP4 : Table de Multiplication
#Exercice 1 : Open Class Room
#Src : https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/231442-avancez-pas-a-pas-vers-la-modularite-1-2

import os

def multipl(number,max=11):
    """
        docstring de la fonction multipl :
        Table de multiplication
        Taper : help(multipl)
    """
    for i in range(max):
        print(i," * ",number," = ",i*number)



#test de la fonction table
if  __name__=="__main__":
    number=int(input("Entrer un nombe !!\n"))
    multipl(number)

