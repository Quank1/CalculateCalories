from itertools import count
import sys
import os

sys.path.append(os.path.abspath('../CaloriesCalc'))

import sqltools

con = 0

# Запитує першу букву в назві страви для пошуку в бд
def AskLetter():
    return input("Перша буква в назві страви: ")


# Виводить інформацію про продукти
def PrintProductsForFirstLetter(first_letter):
    
    LIstProduct = sqltools.SearchByTheFirstLetterOfTHeAplhaber(first_letter.lower()) # type: ignore

    for InfoProduct in LIstProduct:
        num = InfoProduct[0]
        name = InfoProduct[1]
        print(f"Продукт: {name}\n\tНомер продукта: {num}\n")


def Num():
    try: 
        num = int(input("Напишіть номер продукту якого ви хочете порахувати: "))
    except ValueError:
        print("Введіть число!")
        Num()

    return num


def AskRespond(num, YorN, NumberList, Func):  
    if YorN.lower() == "д" or YorN.lower() == "y":
        NumberList.append(num)
        PrintProductsForFirstLetter(AskLetter())
        Func()
    elif YorN.lower() == "н" or YorN.lower() == "n":
        NumberList.append(num)


def YorN():
    try:
        YorNAns = str(input("Вибираєм більше продуктів [Д/н]: "))

    except ValueError:
        print("Введіть \"Д\" або \"Н\"!")
        YorN()


    if YorNAns.lower() == "д" or YorNAns.lower() == "н":
        return YorNAns
    else:
        print("Введіть один  з варіантів!")
        YorN()



def Ask():
    return Num(), YorN()

NumberList = []

def Return():
    
    num, YorN = Ask()
    AskRespond(num, YorN, NumberList, Return)
    return NumberList


#Передає номера продуктів в бд
def WhoNumberProduct():

    NumberList = Return()
    
    return NumberList
        


def AskWeights(name):
    try:
        weight = int(input(f"Скільки грам ви зїли {name}?: "))
    except ValueError:
        print("Введіть цифру! Без \"г.\" і т.д.")
        AskWeight(name)

    return weight


# Рахує калорії 
def AskWeight(ListInfoPrducts):
    count = 0
    calories = 0


    for products in ListInfoPrducts:
        for product in products:
            name = product[1]
            cal = product[2]
            Weight = AskWeights(name)

        calories = calories + ( (int(round(cal)) * Weight) / 100 )

    count = count + 1

    return calories 


def GetCalories(calories):
    print(f"Калорій - {calories}")