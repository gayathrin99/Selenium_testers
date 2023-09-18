import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import random
import time
import datetime
from datetime import timedelta
from datetime import datetime
driver = webdriver.Chrome()
depart_time=[]
reach_time=[]
business_select=[]
anytime=[]
wanna_get_away=[]
wanna_get_away_plus=[]
driver.get('https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&adultsCount=1&departureDate=2023-09-20&departureTimeOfDay=ALL_DAY&destinationAirportCode=LGA&fareType=USD&int=HOMEQBOMAIR&originationAirportCode=LAX&passengerType=ADULT&reset=true&returnDate=2023-09-23&returnTimeOfDay=ALL_DAY&tripType=roundtrip')
def web_scraper():
    search_button=driver.find_element("id",'form-mixin--submit-button')
    search_button.click()
    time.sleep(2)
    content=driver.page_source
    soup=BeautifulSoup(content,features="html.parser")
    #print(soup.prettify())
    for a in soup.findAll('u1',attrs={'id':'air-search-results-matrix-0'}):
        departtime=a.find('div',attrs={'class':'air-operations-time-status air-operations-time-status_booking-primary select-detail--time'})
        depart_time.append(departtime.text)
        reachtime=a.find('div',attrs={'class':'air-operations-time-status air-operations-time-status_booking-primary select-detail--time'})
        reach_time.append(reachtime.text)
        
web_scraper()
print(depart_time)
