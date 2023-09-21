import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
import selenium
from selenium import webdriver
url ="https://www.magicbricks.com/owner-property-for-sale-in-bangalore-pppfs"
owner_title=[]
society_name=[]
summary_title=[]
summary_value=[]
this_dict={}
main_dict={}

#browser = webdriver.Chrome()
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
#browser.get(url)
house_details=soup.find_all("div",class_="mb-srp__card__info mb-srp__card__info-withoutburger")
#print(house_details)
for houses in house_details:
    owner_title.append(houses.find("h2",class_="mb-srp__card--title").text)
    summary=houses.find_all("div",class_="mb-srp__card__summary__list--item")
    this_dict={}
    for each_item in summary:
        print(each_item.find("div",class_="mb-srp__card__summary--label").text)
        summary_title.append(each_item.find("div",class_="mb-srp__card__summary--label").text)
        summary_value.append(each_item.find("div",class_="mb-srp__card__summary--value").text)
        this_dict[each_item.find("div",class_="mb-srp__card__summary--label").text]=each_item.find("div",class_="mb-srp__card__summary--value").text
        print(this_dict)
    main_dict[houses.find("h2",class_="mb-srp__card--title").text]=this_dict
#print(main_dict)
df=pd.DataFrame(main_dict)
#print(df)
df.to_csv("test.csv")
#print(owner_title)
#print(summary_title)
#print(summary_value)

