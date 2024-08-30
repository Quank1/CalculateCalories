from itertools import count
import sys
import os

sys.path.append(os.path.abspath('../LessonScraping'))

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


#Передає номера продуктів в бд
def WhoNumberProduct():

    NumberList = []

    def WhoNum():

        def Ask():
            def Num():
                try: 
                    num = int(input("Напишіть номер продукту якого ви хочете порахувати: "))
                except ValueError:
                    print("Введіть число!")
                    Num()

                return num
                
            
            def YorNm():
                try:
                    YorN = str(input("Вибираєм більше продуктів [Д/н]: "))

                except ValueError:
                    print("Введіть \"Д\" або \"Н\"!")
                    YorNm()

                if YorN.lower() == "д" or YorN.lower() == "н":
                    return YorN
                else:
                    print("Введіть один  з варіантів!")
                    YorNm()



            return Num(), YorNm()



        def AskRespond(num, YorN):  
            if YorN.lower() == "д" or YorN.lower() == "y":
                NumberList.append(num)
                PrintProductsForFirstLetter(AskLetter())
                WhoNum()
            elif YorN.lower() == "н" or YorN.lower() == "n":
                NumberList.append(num)
                
            
        num, YorN = Ask()
        AskRespond(num, YorN)
    
    WhoNum()
    return NumberList
        
        

# Рахує калорії 
def AskWeight(ListInfoPrducts):
    count = 0
    calories = 0

    def AskWeight(name):
        try:
            weight = int(input(f"Скільки грам ви зїли {name}?: "))
        except ValueError:
            print("Введіть цифру! Без \"г.\" і т.д.")
            AskWeight(name)

        return weight

    for products in ListInfoPrducts:
        for product in products:
            name = product[1]
            cal = product[2]
            Weight = AskWeight(name)

        calories = calories + ( (int(round(cal)) * Weight) / 100 )

    count = count + 1

    return calories 


def GetCalories(calories):
    print(f"Калорій - {calories}")