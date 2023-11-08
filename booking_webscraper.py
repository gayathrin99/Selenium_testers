import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4
from bs4 import BeautifulSoup
import time
import requests
import xlsxwriter
url = "https://www.booking.com/searchresults.html?ss=Bangalore&ssne=Bangalore&ssne_untouched=Bangalore&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Aua1mKoGwAIB0gIkZjhhMTU1MDgtOGFiNS00NzgxLThiMzctOTMwZDU3ZDJmZjY12AIF4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-2090174&dest_type=city&checkin=2023-11-21&checkout=2023-11-23&group_adults=3&no_rooms=1&group_children=0"
driver = webdriver.Chrome()
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
body = soup.body
#headings=body.find_all("div",class_=['aaee4e7cd3','e7a57abb1e','d6767e681c'])
headings=body.find_all(["span","h3"], {'class':['bui-card__title']})
#headings=body.find_all("a"
reviewscore=body.find_all("div",['a3b8729ab1', 'd86cee9b25'])

hotelprice=body.find_all("div",['bui-price-display__value','bui-f-color-constructive','hotel-card__price', 'bui-spacer--small'])
details=body.find_all("div",class_=['c82435a4b8', 'a178069f51', 'a6ae3c2b40', 'a18aeea94d', 'd794b7a0f7', 'f53e278e95', 'c6710787a4'])
hotel_name = []
review_score=[]
price=[]
hotel_details=[]
time.sleep(5)
body_list = []

#print(soup.prettify())

#print(body.strings)
file = open("booking_trial.xlsx", "w+", encoding="utf-8")
workbook=xlsxwriter.Workbook("booking_trial.xlsx")
worksheet=workbook.add_worksheet()
worksheet.write(0,0,"Hotel Name")
worksheet.write(0,1,"Review Score")
worksheet.write(0,2,"Price")
worksheet.write(0,3,"Hotel Details")
"""for string in body.strings:
    print(string)
    
    body_list.append(string)
' '.join(body_list).split()"""
#body.find_all(string=True, recursive=False)
#headings = driver.find_elements(By.XPATH,"//div[@class= '']")
#headings = driver.find_elements(By.TAG_NAME,"h3")
count=1
for i in headings:
    
    hotel_name.append(i.text)
    worksheet.write(count,0,i.text)
    count+=1
print(hotel_name)
print(len(headings))
count=1
for i in reviewscore:
    
    review_score.append(i.text)
    worksheet.write(count,1,i.text)
    count=count+1
print(review_score)
print(len(reviewscore))
count=1
for i in hotelprice:
    
    price.append(i.text)
    worksheet.write(count,2,i.text)
    count=count+1
    print(count)
print(price)
print(len(price))
count=1
for i in details:
    
    hotel_details.append(i.text)
    worksheet.write(count,3,i.text)
    count=count+1
    print(count)
print(hotel_details)
print(len(hotel_details))
"""
body_list = [x.replace('\n', "") for x in body_list]
body_list = body_list.remove('')"""

# print(hotel_name)
workbook.close()
