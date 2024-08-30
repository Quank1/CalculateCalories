import requests
import sqltools
import math
from bs4 import BeautifulSoup # type: ignore



headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

main_url = "https://health-diet.ru"
count = 0
count_page = 0


all_urls = {}

all_products = []



# Записує html-код сайту в файл
def WriteInFile():

    url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

    req = requests.get(url, headers=headers)

    src = req.text

    with open("date/index.html", "w") as file:
        file.write(src)


# Читає html-код основної сторінки сайту з файлу
def ReadInFile():

    with open("date/index.html", "r") as file:
        return file.read()
    

# Витягує силки на групу продуктів з сайту
def FindUrl(data):

    src = BeautifulSoup(data, "lxml")

    all_url = src.find_all("a", class_="mzr-tc-group-item-href")

    for url in all_url:
        all_urls[url.text] = f"{main_url}{url.get("href")}"


#Виводить всі url адреса з назвами на яку групу продуктів вони йдуть
def PrintAllUrl():
    for NameProduct, UrlProduct in all_urls.items():
        print(f"{NameProduct} - {UrlProduct}")


#Вертає html-код другої сторінки
def ReadSecondPageInFIle():

    with open(f"date/{count_page}IndexPage.html", "r") as file:
        return file.read()

CountPage = 0

#Записує html-код другої сторінки в файл
def WriteSecondPageInFile(url):

    req = requests.get(url, headers=headers)

    with open(f"date/{count_page}IndexPage.html", "w") as file:
        file.write(req.text)    

    return ReadSecondPageInFIle()    
    


# Дістає з сайту кбжу продуктів
def AllWorkInSecondPage():

    coun = 0 
    for urlp in all_urls.values():
        
        data = WriteSecondPageInFile(urlp)
        soup = BeautifulSoup(data, "lxml")

        try: 
            table = soup.find("table", class_="uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed")

            tbody = table.find("tbody")  # type: ignore

            findtr = tbody.find_all("tr") # type: ignore
        except:
            print("Сторінка пуста...")
            continue
        for tr in findtr:
                

                
            alltd = tr.find_all("td")

            name = alltd[0].text
            calories = alltd[1].text
            squirrels = alltd[2].text
            fats = alltd[3].text
            carbohydrates = alltd[4].text

            name = name.replace(", ", "_")
            name = name.replace(" ", "_")
            name = name.replace("\n", "")

            calories = calories.replace(" кКал", "")
            calories = calories.replace(",", ".")
                
            squirrels = squirrels.replace(" г", "")
            squirrels = squirrels.replace(",", ".")


            fats = fats.replace(" г", "")
            fats = fats.replace(",", ".")


            carbohydrates = carbohydrates.replace(" г", "")
            carbohydrates = carbohydrates.replace(",", ".")


            product = (name.lower(), float(calories), float(squirrels), float(fats), float(carbohydrates))

            all_products.append(product)
                
        

#Записує все AllProducts.db
def WriteInDB():
    sqltools.CreateDB(all_products)