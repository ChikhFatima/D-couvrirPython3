#TP3 : Compter le nombre de consonne et voyelle dans une chaine de caracteres
#Exercice 1 : Open Class Room
#Src : https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/231260-apprenez-a-faire-des-boucles


def compt(chaine,list):
    res={"chaine": chaine,"voyelle" : 0 ,"consonne" : 0}
    for lettre in chaine :
        if lettre in "AEIOUYaeiouy":
            res["voyelle"]+=1
        else:
            res["consonne"]+=1

    list.append(res)

list=[]
nb_element=3
for i in range(nb_element):
    chaine =input("Entrer une chaine !!\n")
    compt(chaine,list)

for i in range(len(list)):
    print(list[i])

