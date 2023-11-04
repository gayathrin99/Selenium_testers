import selenium
from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
import time
import requests
url = "https://www.booking.com/searchresults.html?ss=Bangalore%2C+India&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Aua1mKoGwAIB0gIkZjhhMTU1MDgtOGFiNS00NzgxLThiMzctOTMwZDU3ZDJmZjY12AIF4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2090174&dest_type=city&checkin=2023-11-04&checkout=2023-11-06&group_adults=3&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
driver = webdriver.Chrome()
page = requests.get(url)
hotel_name = []
time.sleep(5)
body_list = []
soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())
body = soup.body
print(body.strings)
file = open("text.txt", "w+", encoding="utf-8")
for string in body.strings:
    print(string)
    file.write(string)
    body_list.append(string)
' '.join(body_list).split()
body.find_all(string=True, recursive=False)
headings = body.find_all("h3")

body_list = [x.replace('\n', "nul") for x in body_list]
body_list = body_list.remove('nul')
print(body_list)
for i in headings:
    if i is not "":
        hotel_name.append(i)

# print(hotel_name)
