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

    return ProductInfoList
    conn.commit()
    conn.close()
