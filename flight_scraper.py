import selenium
from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
start_time=[]
arrival_time=[]
starting_station=[]
destination_station=[]
ticket_price=[]
ticket_price_new=[]
airline=[]
def flight_scraper(url):
    url=url
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    div=soup.find_all('ul')
    for data in div:
        for s_time in data.findAll('div',{'class':'wtdjmc YMlIz ogfYpf tPgKwe'}):
            #print(s_time.text)
            start_time.append(s_time.text)
        for a_time in data.findAll('div',{'class':'XWcVob YMlIz ogfYpf tPgKwe'}):
            #print(a_time.text)
            arrival_time.append(a_time.text)
        for s_station in data.findAll('div',{'class':'G2WY5c sSHqwe ogfYpf tPgKwe'}):
           # print(s_station.text)
            starting_station.append(s_station.text)
        for d_station in data.findAll('div',{'class':'c8rWCd sSHqwe ogfYpf tPgKwe'}):
            #rint(d_station.text)
            destination_station.append(d_station.text)
        for t_cost in data.findAll('div',{'class':['YMlIz FpEdX jLMuyc','YMlIz FpEdX']}):
            #print(t_cost.text)
            ticket_price.append(t_cost.text)
        for flight in data.findAll('span',{'class':'h1fkLb'}):
            airline.append(flight.text)
    
    print((start_time))
    print((ticket_price))
    #your URL
flight_scraper("https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDIzLTEwLTAxagwIAhIIL20vMGRjbGdyDQgDEgkvbS8wMTk1cGQaKRIKMjAyMy0xMC0zMWoNCAMSCS9tLzAxOTVwZHIMCAISCC9tLzBkY2xnQAFIAXABggELCP___________wGYAQE")
previous_value=None
for i in range(0,len(ticket_price),3):
    ticket_price_new.append(ticket_price[i])
print((ticket_price_new))
print(len(start_time))
print(len(arrival_time))
print(len(starting_station))
print(len(destination_station))
print(len(ticket_price_new))
d={'Start time':start_time,'Arrival time':arrival_time,'Starting Station':starting_station,'Destination':destination_station,'Ticket Price':ticket_price_new}
df=pd.DataFrame(data=d)
print(df)