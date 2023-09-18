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
driver.get('https://www.southwest.com/')
def enter_arrive_and_departure(origin,destination,date,return_date):
    arrive_link=driver.find_element("id",'LandingAirBookingSearchForm_originationAirportCode')
    origin=origin
    for letter in origin:
        arrive_link.send_keys(letter)
        wait_time=random.randint(0,1000)/1000
        time.sleep(wait_time)
    departure_link=driver.find_element("id",'LandingAirBookingSearchForm_destinationAirportCode')
    destination=destination
    for letter in destination:
        departure_link.send_keys(letter)
        wait_time=random.randint(0,1000)/1000
        time.sleep(wait_time)
    depart_datelink=driver.find_element("id",'LandingAirBookingSearchForm_departureDate')
    date=date
    depart_datelink.clear()
    for letter in date:
        depart_datelink.send_keys(letter)
        wait_time=random.randint(0,1000)/1000
        time.sleep(wait_time)
    return_datelink=driver.find_element('id','LandingAirBookingSearchForm_returnDate')
    return_date=return_date
    for letter in return_date:
        return_datelink.send_keys(letter)
        wait_time=random.randint(0,1000)/1000
        time.sleep(wait_time)
    search_button=driver.find_element("id",'LandingAirBookingSearchForm_submit-button')
    search_button.click()
def web_scraper():
    content=driver.page_source
    soup=BeautifulSoup(content,features="html.parser")
    #print(soup.prettify())
    for a in soup.findAll('u1',attrs={'id':'air-search-results-matrix-0'}):
        departtime=a.find('div',attrs={'class':'air-operations-time-status air-operations-time-status_booking-primary select-detail--time'})
        depart_time.append(departtime.text)


enter_arrive_and_departure("LAX","NYC","9/20","9/23")
web_scraper()