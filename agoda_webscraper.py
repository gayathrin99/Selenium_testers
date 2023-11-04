import selenium
from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
import requests
import time
from selenium.webdriver.common.by import By
url = "https://www.agoda.com/search?guid=9d87c1a3-142e-40a7-afa9-07950aae8e5e&asq=NQVGXW6jsE3tbdY9S%2BqUCpufa9Vwpz6XltTHq4n%2B9gPt6Sc9VYM%2BOtJvOdzFsuZ%2FQHsxV%2Fa6ZlGeW1yk89QKLVFcygV4CXzeo11i%2BlN77csdP3Fv0UbjSfHYVIw8lGWfzproRGbgCLxTzRaDD5QGcm0t3c82nJ%2Fp%2B0GXkwK5hQ84uUE8oRa1jEBYCfIz%2FxkbPTqQxhyYixfDuUGdcaLaFw%3D%3D&city=4923&tick=638346401604&locale=en-us&ckuid=dacc4bde-76df-40f7-92d5-90dd06030580&prid=0&currency=INR&correlationId=eb2963cf-e487-4e48-be31-82ca841caa15&analyticsSessionId=7853228146228769539&pageTypeId=1&realLanguageId=1&languageId=1&origin=IN&cid=1844104&userId=dacc4bde-76df-40f7-92d5-90dd06030580&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=27&currencyCode=INR&htmlLanguage=en-us&cultureInfoName=en-us&machineName=sg-pc-6g-acm-web-user-7f4d774559-47nm4&trafficGroupId=1&sessionId=5rycay4i2ykh4fimysdyxh2b&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&cdnDomain=agoda.net&checkIn=2023-11-15&checkOut=2023-11-18&rooms=1&adults=3&children=0&priceCur=INR&los=3&textToSearch=Bangalore&travellerType=1&familyMode=off&ds=kpYt6TZNKFVVjP7K&productType=-1"
driver = webdriver.Chrome()
page = driver.get(url)
time.sleep(5)
rating = []
search_box_text = []
search_box = driver.find_elements(
    By.XPATH, "//div[@class='Box-sc-kv6pi1-0 hRUYUu IconBox__wrapper']")
for i in search_box:
    search_box_text.append(i.text)
print(search_box_text)
# first = search_box_text[0]
# number = int(''.join([i for i in first if i.isdigit()]))
# print(number)
# num_of_choices = search_box.find_element(
# By.XPATH, "./div[@class='SearchBoxTextDescription__desc']")

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
screen_height = int(driver.execute_script(
    "return document.documentElement.scrollHeight"))
print(screen_height)
"""for i in range(0, 1000):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height"""

# Wait to load page

# Calculate new scroll height and compare with last scroll height
#
ratings = driver.find_elements(
    By.XPATH, "//div[@class='Box-sc-kv6pi1-0 ggePrW']")
for i in ratings:
    print(i.text)
print(len(ratings))
