import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
import selenium
from selenium import webdriver
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
#page=requests.get(url)
Location=[]
Category=[]
Parent_JD_Link=[]
Vendor_Name=[]
Phone_Number=[]
Email=[]
Website=[]
Vendor_JD_link=[]

def web_scraping(city,job_category):
    driver=webdriver.Chrome()
    url="https://www.justdial.com/"+"/"+city+"/"+job_category+"/"
    page=requests.get(url)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #soup=BeautifulSoup(page.text,"html.parser")
    #print(soup.prettify())
    #print(driver.find_elements(By.TAG_NAME, "h2"))
    #time.sleep(2)
    Location.append(city)
    Category.append(job_category)
    Parent_JD_Link.append(url)
    vendor_names=driver.find_elements(By.TAG_NAME,"h2")
    for vendor in vendor_names:
        print(vendor.text)
        Vendor_Name.append(vendor.text)
    
    print(Location)
    print(Category)
    print(Parent_JD_Link)
    print(Vendor_Name)

web_scraping(input("Enter the city name: "),input("Enter the job category: "))
