import regex
import pandas as pd
import numpy as np
import emoji
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
conversation = 'WhatsApp Chat with Shiv Shankar.txt'
Date=[]
Time=[]
Author=[]
Message=[]
file=open(conversation,"r",encoding='utf-8')
date_pattern = '^([0-9]+)(\/)([0-9]+)(\/)([0-9]+)'
time_pattern = '([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)?'
for i in file:
    #print(i)
    if regex.match(date_pattern,(i.split(",")[0])):
        Date.append(i.split(",")[0].strip())
        #print(i.split(",")[1].split("-")[0])
        Time.append(i.split(",")[1].split("-")[0].replace("\u202f"," ").strip())
        Author.append(i.split("-")[1].split(":")[0].strip())
        message=str(''.join([j for j in i.split("-")[1].split(":")[1:]]))
        #print(i.split("-")[1].split(":")[1])
        Message.append(message[:-1])    
df=pd.DataFrame(list(zip(Date,Time,Author,Message)),columns=["Date","Time","Author","Message"])
print(df)
print("Total Messages exchnged: ",format(len(Message)))
x_counter=0
y_counter=0
for i in range(len(df)):
    if df["Author"][i] == "Shiv Shankar":
        x_counter+=1
    else:
        y_counter+=1
print("Shiv Shankar sent ",format(x_counter)," messages.")
print("Gayathri sent ",format(y_counter)," messages.")
most_messages_date=df["Message"].groupby(df["Date"])
print("Date with most number of messages and their count:",most_messages_date.count().nlargest(1))
peak_time=df["Message"].groupby(df["Time"])