from ast import dump
from asyncore import file_dispatcher
from time import time
import requests as req
from bs4 import BeautifulSoup
import json
import tqdm

data={
    "data":[]
}

for page in range(1,41):
    url=f"https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&area=1&page=(page))&hhtmFrom=vacancy_search_list"
    resp=req.get(url)

    soup=BeautifulSoup(resp.text, "lxml")
    tags=soup.find_all(attrs={"data-maker":"item-title"})
    for iter in tags:
        time.sleep(2)
        #print(iter.text, iter.attrs["href"])
        url_object="https://www.avito.ru"+iter.attrs["href"]
        resp_object=req.get(url)
        soup_object=BeautifulSoup(resp.text, "lxml")
        tags=soup.find_all(attrs={"data-maker":"item-title"}) 
        tag_price=soup_object.find(attrs={"itemprop":"offers"}).find(attrs={"itemprop":"price"}).text
        #print(tag_price)

        tag_region=soup_object.find(attrs={"itemtype":""}).find_all(attrs={"itemprop":"name"})
        #print(tag_region)
        #data["data"].append({"Title":)
        with open("data.json", "w") as file:
            json.dump(data.file)        
