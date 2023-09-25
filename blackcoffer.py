import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
import xlrd

input_df=pd.read_excel('D:\GAYATHRI\Microsoft VS Code\Input.xlsx')
#print(input_df)
for ind in input_df.index:
    url=input_df['URL'][ind]
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    url_id=str(input_df['URL_ID'][ind])
    file_name=url_id+".txt"
    file=open(file_name,"w+",encoding='utf-8')
    try:
        article_title=soup.find("h1").text
    except:
        continue
    print(ind)
    file.write(article_title)
    file.write("\n")
    for data in soup.find_all('p'):
        article_text=data.text
        file.write(article_text)

    #article_text=soup.find("div",{"class":["td-post-content tagdiv-type","tdb-block-inner td-fix-index"]}).text
   

    #print(article_text)
    
