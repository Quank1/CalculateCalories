from itertools import count
import requests
from bs4 import BeautifulSoup
import sys, os

sys.path.append(os.path.abspath('../CaloriesCalc'))

import sqltools


headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

Gen_Url = "https://www.povarenok.ru/recipes/cat/"

all_links = []
all_products = []

#Силки на рецепти
def GetUrlResipes(url):

    req = requests.get(url, headers=headers)

    src = req.text

    soup = BeautifulSoup(src, "lxml")

    GenBlock = soup.find("div", class_="rubrics-bl")

    CatList = GenBlock.find_all("ul", class_="cat-list") # type: ignore

    for el in CatList:
        Url = el.find_all("a")
        for i in Url:
            all_links.append(i.get("href"))



def WriteRecipeInDB():

    ListLinkInPage = []
    count = 0

    for link in all_links:


        req = requests.get(link, headers=headers)

        data = req.text

        soup = BeautifulSoup(data, "lxml")

        LinkBlock = soup.find_all("article", class_="item-bl")

        
        for Block in LinkBlock:

            UrlBlock = Block.find("h2")

            name = UrlBlock.text
            
            name = name.replace(", ", "_")
            name = name.replace(" ", "_")
            name = name.replace("\n", "")
            name = name.replace("\t", "")
            name = name.replace("\r", "")
            name = name.replace("\xa0", "")
            name = name.replace("_______", "")

            url = UrlBlock.find("a").get("href")

            date = (str(name), str(url))


            print("Запис в словарь")
            all_products.append(date)
            count += 1
            if count >= 5:
                print("Кoнец цикла")
                count = 0
                break
        
                

GetUrlResipes(Gen_Url)
#WriteRecipeInDB()

def CreateBd():

    sqltools.CreateSecondBD(all_products)
