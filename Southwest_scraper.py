import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver=webdriver.Chrome()
business_select=[]
anytime=[]
wanna_get_away=[]
wanna_get_away_plus=[]
driver=driver.get('https://www.southwest.com/')
def enter_arrive_and_departure(origin,destination,date):
    

