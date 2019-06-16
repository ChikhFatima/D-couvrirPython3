#TP 7 : Les fonctions en python
#Exercice 1 : Des exemples de fonction en python
#Src : Vidéo : 661773_02_03_XR15_funcs.mp4 Fonrmation : Learning_Python

#Ex1 : Fonction basique
def functionBasic():
    print("i am a basic function ")

#Ex2 : Fonction avec des arguments
def functionArguments(arg1, arg2):
    print("i am a function with two arguments :", arg1,", ", arg2)

#Ex3 : Fonction avec une valeur de retour
def functionReturnValue():
    return "Value To Return"

#Ex : Fonction Cube
def cube(x):
    return x*x*x

#Ex4 : Fonction avec un argument par défaut
def power(num, default=1):
    result=1
    for i in range(default):
        result=result*num
    return result

#Ex5 : Fonction a plusieurs arguments
def functionMultiArguments(*args):
    result=0
    for x in args:
        result+=x
    return result

#Fonction main
if __name__=="__main__":
    functionBasic()
    functionArguments(10,40)
    print(functionReturnValue())
    print("Fonction cube :",cube(4))
    print(power(10))
    print(power(10,3))
    print("Inverser les arguments de la function power(): ",power(default=5,num=10))
    print("Fonction avec plusieurs arguments : ",functionMultiArguments(5,10,20,30))