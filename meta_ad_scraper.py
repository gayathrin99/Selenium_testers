import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
import selenium
from selenium import webdriver
import random
import time
import urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
url="https://www.facebook.com/ads/library/?active_status=all&ad_type=political_and_issue_ads&country=IN&media_type=all"
driver=webdriver.Chrome()
def get_ad_details(url):
    url=url
    page=requests.get(url)
    print(url)
    soup=BeautifulSoup(page.content,"html.parser")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    print(soup.find("body"))  
    ad_details=soup.find_all("div",class_="x1ywc1zp x78zum5 xl56j7k x1e56ztr x1277o0a")
    images=driver.find_elements(By.TAG_NAME,"img")
    print(len(images))
    src=[]
    for img in images:
        src.append(img.get_attribute('src'))
        print(img.get_attribute('src'))
    for i in range(20):
        urllib.request.urlretrieve(str(src[i]),"{}.jpg".format(i))
    #print(ad_details)
    #images=soup.find_all("img", alt=True)
    '''for i in ad_details:
        images=i.find()
        
    for image in images:
        print(image)
        #img=Image.open(image)
        #img.show()'''
def enter_main_inputs(ad_name):
    driver.get(url=url)
    wait = WebDriverWait(driver,30)
    adbtn = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Ad category']")))
    adbtn.click()
    alladds = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='All ads']")))
    alladds.click()
    search = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search by keyword or advertiser']")))
    search.send_keys(ad_name)
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    urllatest=driver.current_url
    get_ad_details(urllatest)
    time.sleep(1)
    #ad_category=Select(ad_category).select_by_index[0]
    '''ad_name_input=driver.find_element(By.CLASS_NAME,"//div[contains(@class,'x76ihet xwmqs3e x112ta8 xxxdfa6 xhk9q7s x1otrzb0 x1i1ezom x1o6z2jb ximmm8s x1rg5ohu x1f6kntn x3stwaq xdj266r x11i5rnm xat24cr x1mh8g0r x1a2a7pz x6ikm8r x10wlt62 x1y1aw1k x1pi30zi xwib8y2 x1swvt13 x1n2onr6 xlyipyv xh8yej3 xhtitgo x1hxswl6;)]")
    ad_name = ad_name
    ad_name_input.send_keys(ad_name)
    time.sleep(2)
    '''
enter_main_inputs("titan")

