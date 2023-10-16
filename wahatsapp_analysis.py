import regex
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import emoji
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
nltk.download('all')
conversation = 'WhatsApp Chat with X.txt'
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
    if df["Author"][i] =="X":
        x_counter+=1
    else:
        y_counter+=1
print("X sent ",format(x_counter)," messages.")
print("Y sent ",format(y_counter)," messages.")
most_messages_date=df["Message"].groupby(df["Date"])
print("Date with most number of messages and their count:",most_messages_date.count().nlargest(1))
peak_time=df["Message"].groupby(df["Time"])
def preprocess_text(text):
    tokens = word_tokenize(text)
    filtered_tokens= [token for token in tokens if token not in stopwords.words("english")]
    lemmatizer=WordNetLemmatizer()
    lemmatized_tokens=[lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_text=' '.join(lemmatized_tokens)
    return processed_text
df["Message"]=df["Message"].apply(preprocess_text)
print(df)
analyzer=SentimentIntensityAnalyzer()
def get_sentiment(text):
    scores=analyzer.polarity_scores(text)
    sentiment= 1 if scores['pos'] > 0 else 0
    return sentiment
df['sentiment']=df['Message'].apply(get_sentiment)
pos_by_x=0
pos_by_y=0
for i in range(len(df)):
    if df["Author"][i] == "X" and df["sentiment"][i] == 1:
        pos_by_shiv=pos_by_x+1
    elif df["Author"][i] == "Y" and df["sentiment"][i] == 1:
        pos_by_gaya3=pos_by_y+1
print("Positives by X: ",pos_by_x)
print("Positives by Y: ",pos_by_y)
print(df)