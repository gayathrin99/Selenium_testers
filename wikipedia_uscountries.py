import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
#browser = webdriver.Chrome()
url ="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
#browser.get(url)
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
#print(soup.prettify())
table= soup.find_all('table')[1]
#table=browser.find_element(By.ByClassName,'wikitable sortable jquery-tablesorter')
#print(table)
world_titles=table.find_all('th')
#print(world_titles)
world_table_titles= [title.text.strip() for title in world_titles ]
#print(world_table_titles)
df = pd.DataFrame(columns=world_table_titles)
#print(df)
column_data= table.find_all('tr')
for row in column_data[1: ]:
    row_data= row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length]=individual_row_data

print(df)
#df.to_csv(r'D:\GAYATHRI\sample.txt')