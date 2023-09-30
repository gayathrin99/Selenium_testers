import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
import xlrd
import xlsxwriter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import os
nltk.download('punkt')
input_df=pd.read_excel('D:\GAYATHRI\Microsoft VS Code\Input.xlsx')
workbook = xlsxwriter.Workbook(os.path.join(os.path.dirname(os.path.abspath(__file__)),"result.xlsx"))
worksheet1=workbook.add_worksheet()
positive_words=[]
negative_words=[]
stop_words_final=[]
stop_words=[]
def all_lower(text_list):
    return [x.lower() for x in text_list]
def sentiment_analysis():
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Names.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Geographic.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_GenericLong.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Generic.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_DatesandNumbers.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Currencies.txt','r').read().replace("|","\n").split('\n'))
    stop_words.append(open('D:\GAYATHRI\Microsoft VS Code\StopWords_Auditor.txt','r').read().replace("|","\n").split('\n'))
    global stop_words_final
    stop_words_final=list(filter(lambda j: j.isupper(),stop_words[0]))
    stop_words_final=stop_words_final+list(filter(lambda j: j.isupper(),stop_words[1]))
    stop_words_final+= stop_words[2]
    stop_words_final+=stop_words[3]
    stop_words_final+=list(filter(lambda j: j.isupper(),stop_words[4]))
    stop_words_final+=list(filter(lambda j: j.isupper(),stop_words[5]))
    stop_words_final+=stop_words[6]
    stop_words_final=all_lower(stop_words_final)
    global positive_words
    positive_words=open('D:\GAYATHRI\Microsoft VS Code\positive-words.txt','r').read().replace("|","\n").split('\n')
    global negative_words
    negative_words=open('D:\GAYATHRI\Microsoft VS Code\\negative-words.txt','r').read().replace("|","\n").split('\n')
sentiment_analysis()
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("ed") or word.endswith("es"):
        count -= 1
    return count

#print(stop_words_final)
'''for i in positive_words:
    print(i)
for i in negative_words:
    print(i)'''
def assign_scores(test_text):
    print(test_text)
    positive_score=0
    negative_score=0
    pronoun_count=0
    complex_word_count=0
    len_of_word=0
    test_text=test_text.lower()
    #print(sent_tokenize(test_text))
    test_list=word_tokenize(test_text)
    number_of_sentences=0
    #print(stop_words_final)
    for i in test_list:
        print(i)
        if i in stop_words_final:
           #print("found a stop word")
           test_list.remove(i)
        elif i in [",","&","<",">","?","/"]:
            test_list.remove(i)
        elif i in ["."]:
            test_list.remove(i)
            number_of_sentences=number_of_sentences+1
        elif i in positive_words:
            positive_score=positive_score+1
        elif i in negative_words:
            negative_score=negative_score+1
        elif i in ["i","us","we","our","my"]:
            print("found a pronoun")
            pronoun_count=pronoun_count+1
        elif (syllable_count(i) > 2):
            complex_word_count+=1
        len_of_word=len(i)+len_of_word
    print(positive_score)
    print(negative_score)

    number_of_words=len(test_list)
    return [positive_score,negative_score,pronoun_count,number_of_words,number_of_sentences,complex_word_count,len_of_word]
    
    

    #if positive_words


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
    scores=[0,0,0,0,0,0,0]
    for data in soup.find_all('p'):
        article_text=data.text
        file.write(article_text)
        scores=[sum(i) for i in zip(scores,assign_scores(article_text))]    
    print(scores)
    polarity_score=(scores[0]-scores[1])/((scores[0]+scores[1])+0.000001)
    print(polarity_score)
    subjectivity_score=(scores[0]+scores[1])/(scores[3]+0.000001)
    print(subjectivity_score)
    average_sentence_length=scores[3]/scores[4]
    percentage_of_complex_words=scores[5]/scores[3]
    fog_index=0.4*(average_sentence_length+percentage_of_complex_words)
    worksheet1.write(0,0,"URL ID")
    worksheet1.write(0,1,"URL")
    worksheet1.write(0,2,"Positive Score")
    worksheet1.write(0,3,"Negtve Score")
    worksheet1.write(0,4,"Polarity score")
    worksheet1.write(0,5,"Subjectivity score")
    worksheet1.write(0,6,"Average sentence length")
    worksheet1.write(0,7,"percentage of complex words")
    worksheet1.write(0,8,"Fog index")
    worksheet1.write(0,9,"Average number of words per sentence")
    worksheet1.write(0,10,"Complex word count")
    worksheet1.write(0,11,"Wod count")
    worksheet1.write(0,12,"Syllable per word") #unclear instruction
    worksheet1.write(0,13,"Personal pronouns")
    worksheet1.write(0,14,"Average word length")
    worksheet1.write(ind+1,0,url_id)
    worksheet1.write(ind+1,1,url)
    worksheet1.write(ind+1,2,scores[0])
    worksheet1.write(ind+1,3,scores[1])
    worksheet1.write(ind+1,4,polarity_score)
    worksheet1.write(ind+1,5,subjectivity_score)
    worksheet1.write(ind+1,6,average_sentence_length)
    worksheet1.write(ind+1,7,percentage_of_complex_words)
    worksheet1.write(ind+1,8,fog_index)
    worksheet1.write(ind+1,9,average_sentence_length)
    worksheet1.write(ind+1,10,scores[5])
    worksheet1.write(ind+1,11,scores[3])
    worksheet1.write(ind+1,12,"2")
    worksheet1.write(ind+1,13,scores[2])
    worksheet1.write(ind+1,14,scores[6])

workbook.close()

    #article_text=soup.find("div",{"class":["td-post-content tagdiv-type","tdb-block-inner td-fix-index"]}).text
