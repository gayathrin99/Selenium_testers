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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import xlsxwriter
#page=requests.get(url)
Location=[]
Category=[]
Parent_JD_Link=[]
Vendor_Name=[]
Phone_Number=[]
Email=[]
Website=[]
Vendor_JD_link=[]
def scroll_down(self):

    # Get scroll height.
    last_height = self.driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = self.driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height
        

def web_scraping(city,job_category):
    city=city
    job_category=job_category
    driver=webdriver.Chrome()
    url="https://www.justdial.com/"+"/"+city+"/"+job_category+"/"
    file=open(city+"_"+job_category+".xlsx","w+",encoding='utf-8')
    workbook=xlsxwriter.Workbook(city+"_"+job_category+".xlsx"+".xlsx")
    worksheet1=workbook.add_worksheet()
    worksheet1.write(0,0,city)
    worksheet1.write(1,0,job_category)
    worksheet1.write(2,0,url)
    worksheet1.write(3,0,"Vendor Name")
    worksheet1.write(3,1,"Phone Number")
    worksheet1.write(3,2,"Vendor JD Link")
    driver.get(url)
    screen_height=driver.execute_script("return window.screen.height;")
    j=1
    time.sleep(5)
    Location.append(city)
    Category.append(job_category)
    Parent_JD_Link.append(url)
    no_of_results=driver.find_element(By.XPATH,"//li[@class= 'jsx-8019251d22823f16 breadcrumb_item font11 fw400 color777  bls']")
    print(no_of_results.text)
    #soup=BeautifulSoup(page.text,"html.parser")
    #print(driver.find_elements(By.TAG_NAME, "h2"))
    #time.sleep(2)
    while True:
        driver.execute_script("window.scrollTo(0,{screen_height}*{j}*2);".format(screen_height=screen_height, j=j))
        j=j+1
        time.sleep(10)
        driver.page_source
        scroll_height = driver.execute_script("return document.body.scrollHeight;") 
        if (screen_height) * j > scroll_height:
            break
        vendor_names=driver.find_elements(By.TAG_NAME,"h2")
        phone_numbers=driver.find_elements(By.XPATH,"//span[@class= 'jsx-3349e7cd87e12d75 callcontent callNowAnchor']")
        vendor_jd_webpage_link_click=driver.find_elements(By.XPATH,"//h2[@class= 'jsx-3349e7cd87e12d75 resultbox_title font22 fw500 color111 complist_title']")
        print(len(phone_numbers))
        for vendor in vendor_names:
            print(vendor.text)
            Vendor_Name.append(vendor.text)
        for phone in phone_numbers:
            print(phone.text)
            Phone_Number.append(phone.text)
        for link in vendor_jd_webpage_link_click:
            Vendor_JD_link.append(link.get_attribute("href"))
    workbook.close()    
    
    print(Location)
    print(Category)
    print(Parent_JD_Link)
    print(len(Vendor_Name))
    print(Phone_Number)
    print(Vendor_JD_link)

web_scraping(input("Enter the city name: "),input("Enter the job category: "))
