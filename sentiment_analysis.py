import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
import xlrd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def sentiment_analysis():
    stop_words=[]
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Names.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Geographic.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_GenericLong.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Generic.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_DatesandNumbers.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Currencies.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Auditor.txt','r').read().replace("|","\n").split('\n'))
    
    stop_words_final=list(filter(lambda j: j.isupper(),stop_words[0]))
    stop_words_final+=list(filter(lambda j: j.isupper(),stop_words[1]))
    stop_words_final+= stop_words[2]
    stop_words_final+=stop_words[3]
    stop_words_final+=list(filter(lambda j: j.isupper(),stop_words[4]))
    stop_words_final+=list(filter(lambda j: j.isupper(),stop_words[5]))
    stop_words_final+=stop_words[6]
   # print(len(stop_words_final))
    positive_words=[]
    positive_words.append(open('D:\GAYATHRI\Microsoft VS Code\positive-words.txt','r').read().replace("|","\n").split('\n'))
    #print(positive_words)
    negative_words=[]
    negative_words.append(open('D:\GAYATHRI\Microsoft VS Code\\negative-words.txt','r').read().replace("|","\n").split('\n'))
   # print(negative_words)

    #print(article_text)




    
    #print(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Names.txt','r').read().replace(" | ","\n").split('\n'))
  
sentiment_analysis()   