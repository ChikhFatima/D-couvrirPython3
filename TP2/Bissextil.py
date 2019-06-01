#TP2 : Vérifier si une anée est bisextil !!
#Exercice 1 : Open Class Room
#Src : https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/231174-creez-des-structures-conditionnelles

def check_bissextil(year):
    if year % 400== 0:
        return True
    elif year %100== 0:
        return False
    elif year %4 == 0:
        return  True
    else:
        return False


def check_bissextil_opt(year):
    if year % 400 == 0 or( year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

if __name__=="__main__" :
    try:
        year=int(input("Please enter a year on the keyboard for verification !\n"))
        assert year > 0
    except ValueError :
        print("Attention : Vous n'avez pas saisi un nombre !!")
    except AssertionError :
        print("Attention : L'année saisie doit être supérieure à 0 !!")
    else:
        print("The year :",year)
        print("Is it bissextil year ? The answer is :",check_bissextil(year))
