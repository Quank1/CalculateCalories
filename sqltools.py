import sqlite3
import os


namebd = "AllProducts.db"
folder_path = "db/"



#Створення бд
def CreateDB(add_list):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    db_path = os.path.join(folder_path, namebd)

    conn = sqlite3.connect(db_path)

    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            calories FLOAT,
            squirrels FLOAT,
            fats FLOAT,
            carbohydrates FLOAT      
        )    
    ''')

    cur.executemany('''INSERT INTO Products (name, calories, squirrels, fats, carbohydrates) VALUES (?, ?, ?, ?, ?)''', add_list)

    conn.commit()
    conn.close()



def table_is_empty(db_path):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute('''SELECT 1 FROM Recipes LIMIT 1''')

    res = cur.fetchall()

    conn.close()

    return res is not None



def CreateSecondBD(Add_list):



    if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    db_path = os.path.join(folder_path, namebd)

    
    conn = sqlite3.connect(db_path)

    cur = conn.cursor()


    cur.execute('''
        CREATE TABLE IF NOT EXISTS Recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT    
        )    
    ''')

    if table_is_empty(db_path):
        pass
    else:
        cur.executemany('''INSERT INTO Recipes (name, url) VALUES (?, ?)''', Add_list)

    conn.commit()
    conn.close()



#Пошук їжі в бд, по першій букві в слові
def SearchByTheFirstLetterOfTHeAplhaber(letter):
    if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    db_path = os.path.join(folder_path, namebd)

    conn = sqlite3.connect(db_path)

    cur = conn.cursor()

    cur.execute(f'''SELECT * FROM Products WHERE LOWER(name) LIKE "{letter}%" ''')
    
    return cur.fetchall()

    conn.commit()
    conn.close()


#Пошук продукта по id в бд
def SearchProdyctForNum(NumberList):
    
    ProductInfoList = []

    if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    db_path = os.path.join(folder_path, namebd)


    conn = sqlite3.connect(db_path)
    cur = conn.cursor()


   
    for num in NumberList:
        cur.execute('''SELECT * FROM Products WHERE id = ?''', (num, ))

        ProductInfoList.append(cur.fetchall())

    conn.commit()
    conn.close()

    return ProductInfoList


def SearchRecipe(name):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    db_path = os.path.join(folder_path, namebd)

    conn = sqlite3.connect(db_path)

    cur = conn.cursor()

    cur.execute(f''' SELECT * FROM Recipes WHERE name LIKE "%{name}%"''')

    res = cur.fetchall()

    if res:
        return res

    else:
        print("В нас нема рецепту цього блюда :(")
    
            

    conn.commit()
    conn.close()

