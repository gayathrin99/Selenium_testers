import requests
import pandas as pd
import selenium
from selenium import webdriver
import time
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import xlsxwriter
import os
import functools
import re 
from functools import reduce 
import imagehash
from PIL import Image
import numpy as np
all_category_path="./"
url="https://www.facebook.com/ads/library/"
driver=webdriver.Chrome()
time.sleep(5)
ad_status=[]
ad_data=[]
ad_started_running_date=[]
def scroll_down(self):

    # Get scroll height.
    last_height = self.driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = self.driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height
def countries_list(country):
    country=country.upper()
    switch={"AFGHANISTAN":"AF","ALBANIA":"AL","ALGERIA":"DZ","AMERICAN SAMOA":"AS","ANDORRA":"AD","ANGOLA":"AO","ANTARCTICA":"AQ","ANTIGUA AND BARBUDA":"AG","ARGENTINA":"AR",
        "ARMENIA":"AM","ARUBA":"AW","AUSTRALIA":"AU","AUSTRIA":"AT","AZERBAIJAN":"AZ","BAHAMAS":"BS","BAHRAIN":"BH","BANGLADESH":"BD","BARBADOS":"BB",
        "BELARUS":"BY","BELGIUM":"BE","BELIZE":"BZ","BENIN":"BJ","BERMUDA":"BM","BHUTAN":"BT","BOLIVIA":"BO","BOSNIA AND HERZEGOVINA":"BA","BOTSWANA":"BW",
        "BOUVET ISLAND":"BV","BRAZIL":"BR","BRITISH INDIAN OCEAN TERRITORY":"IO","BRUNEI DARUSSALAM":"BN","BULGARIA":"BG","BURKINA FASO":"BF","BURUNDI":"BI",
        "CAMBODIA":"KH","CAMEROON":"CM","CANADA":"CA","CAPE VERDE":"CV","CAYMAN ISLANDS":"KY","CENTRAL AFRICAN REPUBLIC":"CF","CHAD":"TD","CHILE":"CL",
        "CHINA":"CN","CHRISTMAS ISLAND":"CX","COCOS ISLANDS":"CC",
        "KEELING ISLANDS":"CC","COLOMBIA":"CO","COMOROS":"KM","CONGO":"CG","CONGO, THE DEMOCRATIC REPUBLIC OF THE":"CD","COOK ISLANDS":"CK",
        "COSTA RICA":"CR","CÔTE D'IVOIRE":"CI","CROATIA":"HR","CUBA":"CU","CYPRUS":"CY","CZECH REPUBLIC":"CZ",
        "DENMARK":"DK","DJIBOUTI":"DJ","DOMINICA":"DM","DOMINICAN REPUBLIC":"DO","ECUADOR":"EC","EGYPT":"EG",
        "EL SALVADOR":"SV","EQUATORIAL GUINEA":"GQ","ERITREA":"ER","ESTONIA":"EE","ETHIOPIA":"ET",
        "FALKLAND ISLANDS":"FK","MALVINAS":"FK","FAROE ISLANDS":"FO","FIJI":"FJ","FINLAND":"FI","FRANCE":"FR",
        "FRENCH GUIANA":"GF","FRENCH POLYNESIA":"PF","FRENCH SOUTHERN TERRITORIES":"TF","GABON":"GA","GAMBIA":"GM",
        "GEORGIA":"GE","GERMANY":"DE","GHANA":"GH","GIBRALTAR":"GI","GREECE":"GR","GREENLAND":"GL","GRENADA":"GD",
        "GUADELOUPE":"GP","GUAM":"GU","GUATEMALA":"GT","GUINEA":"GN","GUINEA-BISSAU":"GW","GUYANA":"GY","HAITI":"HT",
        "HEARD ISLAND AND MCDONALD ISLANDS":"HM","HONDURAS":"HN","HONG KONG":"HK","HUNGARY":"HU","ICELAND":"IS",
        "INDIA":"IN","INDONESIA":"ID","IRAN":"IR","IRAQ":"IQ","IRELAND":"IE","ISRAEL":"IL","ITALY":"IT","JAMAICA":"JM",
        "JAPAN":"JP","JORDAN":"JO","KAZAKHSTAN":"KZ","KENYA":"KE","KIRIBATI":"KI","KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF":"KP",
        "KOREA, REPUBLIC OF":"KR","KUWAIT":"KW","KYRGYZSTAN":"KG","LAO PEOPLE'S DEMOCRATIC REPUBLIC":"LA",
        "LAOS":"LA","LATVIA":"LV","LEBANON":"LB","LESOTHO":"LS","LIBERIA":"LR","LIBYA":"LY","LIECHTENSTEIN":"LI",
        "LITHUANIA":"LT","LUXEMBOURG":"LU","MACAO":"MO","MACEDONIA":"MK","MADAGASCAR":"MG","MALAWI":"MW","MALAYSIA":"MY",
        "MALDIVES":"MV","MALI":"ML","MALTA":"MT","MARSHALL ISLANDS":"MH","MARTINIQUE":"MQ","MAURITANIA":"MR","MAURITIUS":"MU",
        "MAYOTTE":"YT","MEXICO":"MX","MICRONESIA":"FM","MOLDOVA":"MD","MONACO":"MC","MONGOLIA":"MN","MONTENEGRO":"ME",
        "MONTSERRAT":"MS","MOROCCO":"MA","MOZAMBIQUE":"MZ","MYANMAR":"MM","NAMIBIA":"NA","NAURU":"NR","NEPAL":"NP",
        "NETHERLANDS":"NL","NETHERLANDS ANTILLES":"AN","NEW CALEDONIA":"NC","NEW ZEALAND":"NZ","NICARAGUA":"NI",
        "NIGER":"NE","NIGERIA":"NG","NIUE":"NU","NORFOLK ISLAND":"NF","NORTHERN MARIANA ISLANDS":"MP","NORWAY":"NO",
        "OMAN":"OM","PAKISTAN":"PK","PALAU":"PW","PALESTINE":"PS","PANAMA":"PA","PAPUA NEW GUINEA":"PG","PARAGUAY":"PY",
        "PERU":"PE","PHILIPPINES":"PH","PITCAIRN":"PN","POLAND":"PL","PORTUGAL":"PT","PUERTO RICO":"PR","QATAR":"QA",
        "RÉUNION":"RE","ROMANIA":"RO","RUSSIAN FEDERATION":"RU","RWANDA":"RW","SAINT HELENA":"SH","SAINT KITTS AND NEVIS":"KN",
        "SAINT LUCIA":"LC","SAINT PIERRE AND MIQUELON":"PM","SAINT VINCENT AND THE GRENADINES":"VC","SAMOA":"WS",
        "SAN MARINO":"SM","SAO TOME AND PRINCIPE":"ST","SAUDI ARABIA":"SA","SENEGAL":"SN","SERBIA":"RS","SEYCHELLES":"SC",
        "SIERRA LEONE":"SL","SINGAPORE":"SG","SLOVAKIA":"SK","SLOVENIA":"SI","SOLOMON ISLANDS":"SB","SOMALIA":"SO",
        "SOUTH AFRICA":"ZA","SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS":"GS","SOUTH SUDAN":"SS","SPAIN":"ES","SRI LANKA":"LK",
        "SUDAN":"SD","SURINAME":"SR","SVALBARD AND JAN MAYEN":"SJ","SWAZILAND":"SZ","SWEDEN":"SE","SWITZERLAND":"CH",
        "SYRIAN ARAB REPUBLIC":"SY","TAIWAN":"TW","TAJIKISTAN":"TJ","TANZANIA":"TZ","THAILAND":"TH","TIMOR-LESTE":"TL",
        "TOGO":"TG","TOKELAU":"TK","TONGA":"TO","TRINIDAD AND TOBAGO":"TT","TUNISIA":"TN","TURKEY":"TR","TURKMENISTAN":"TM","TURKS AND CAICOS ISLANDS":"TC",
        "TUVALU":"TV","UGANDA":"UG","UKRAINE":"UA","UNITED ARAB EMIRATES":"AE","UNITED KINGDOM":"GB","UNITED STATES":"US",
        "UNITED STATES MINOR OUTLYING ISLANDS":"UM","URUGUAY":"UY","UZBEKISTAN":"UZ","VANUATU":"VU","VENEZUELA":"VE",
        "VIETNAM":"VN","BRITISH VIRGIN ISLANDS":"VG","VIRGIN ISLANDS":"VI","WALLIS AND FUTUNA":"WF","WESTERN SAHARA":"EH","YEMEN":"YE",
        "ZAMBIA":"ZM","ZIMBABWE":"ZW"}
    return switch.get(country,"IN")    
def get_ad_details(url):
    url="https://www.facebook.com/ads/library/"
    page=requests.get(url)
    no_results=driver.find_element(By.XPATH,"//div[@class= 'x8t9es0 x1uxerd5 xrohxju x108nfp6 xq9mrsl x1h4wwuj x117nqv4 xeuugli']").text
    print(no_results)
    itemTargetCount=int(''.join([i for i in no_results if i.isdigit()]))
    print(itemTargetCount)
    #soup=BeautifulSoup(page.content,"html.parser")
    last_height=driver.execute_script("return document.body.scrollHeight")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    #print(soup.find("body"))  
    #ad_details=soup.find_all("div",class_="x1ywc1zp x78zum5 xl56j7k x1e56ztr x1277o0a")
    
    src_number=0
    src=[]
    while itemTargetCount > len(ad_status):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        images=driver.find_elements(By.TAG_NAME,"img")
        print(len(images))
        time.sleep(1)
        new_height=driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height=new_height
        path1 = "All type"
        path2 = "Issues, Politics and Elections"
        # Check whether the specified path exists or not
        isExist = os.path.exists(path1)
        if not isExist:
            os.makedirs(path1)
            print("The new directory is created!")
        isExist = os.path.exists(path2)
        if not isExist:
            os.makedirs(path2)
            print("The second directory is created!")
        for img in images:
            src.append(img.get_attribute('src'))
            #print(img.get_attribute('src'))
        if ad_category == "2":
            parent_directory=os.getcwd()
            os.chdir(parent_directory+"\Issues, Politics and Elections\\")
            print(parent_directory+"\Issues, Politics and Elections\\")
            for i in range(src_number,src_number+len(src)-1):
                print (str(i)+"/"+str(len(src)))
                urllib.request.urlretrieve(str(src[i]),"{}.jpg".format(i))
        else:
            parent_directory=os.getcwd()
            print(parent_directory)
            os.chdir(parent_directory+"\All type\\")
            print(parent_directory+"\All type\\")
            for i in range(src_number,src_number+len(src)-1):
                print (str(i)+"/"+str(len(src)))
                urllib.request.urlretrieve(str(src[i]),"{}.jpg".format(i))

        src_number=src_number+len(src)-1
        print("src number"+ str(src_number))
        ad_statuses=driver.find_elements(By.XPATH,"//span[@class='x8t9es0 xw23nyj xo1l8bm x63nzvj x108nfp6 xq9mrsl x1h4wwuj xeuugli x1i64zmx']")
        for i in ad_statuses:
            ad_status.append(i.text)
        ad_text=driver.find_elements(By.XPATH,"//div[@class= '_4ik4 _4ik5']")
        for i in ad_text:
            ad_data.append(i.text)
        ad_dates=driver.find_elements(By.XPATH,"//span[@class='x8t9es0 xw23nyj xo1l8bm x63nzvj x108nfp6 xq9mrsl x1h4wwuj xeuugli']")
        for i in ad_dates:
            ad_started_running_date.append(i.text)
        file=open("ad data.xlsx","w+",encoding='utf-8')
        workbook=xlsxwriter.Workbook("ad data.xlsx")
        worksheet1=workbook.add_worksheet()
        worksheet1.write(0,0,"Ad Text")
    
        for i in range(len(ad_data)-1):
            worksheet1.write(i+1,0,ad_data[i])
        workbook.close()
    print(len(ad_status))
    print(len(ad_data))
    print(len(ad_started_running_date))
    #print(ad_details)
    #images=soup.find_all("img", alt=True)
    '''for i in ad_details:
        images=i.find()
        
    for image in images:
        print(image)
        #img=Image.open(image)
        #img.show()'''
def enter_main_inputs(country,ad_type,ad_name):
    if ad_type == "1":
        ad_type_string="all"
    else:
        ad_type_string="political_and_issue_ads"
    country=country
    country_code=countries_list(country)
    url_full=url+"?active_status=all&ad_type="+ad_type_string+"&country="+country_code+"&q="+ad_name
    driver.get(url_full)
    print(url_full)
    wait = WebDriverWait(driver,30)
    urllatest=driver.current_url
    get_ad_details(urllatest)
    time.sleep(1)
    #ad_category=Select(ad_category).select_by_index[0]
    '''ad_name_input=driver.find_element(By.CLASS_NAME,"//div[contains(@class,'x76ihet xwmqs3e x112ta8 xxxdfa6 xhk9q7s x1otrzb0 x1i1ezom x1o6z2jb ximmm8s x1rg5ohu x1f6kntn x3stwaq xdj266r x11i5rnm xat24cr x1mh8g0r x1a2a7pz x6ikm8r x10wlt62 x1y1aw1k x1pi30zi xwib8y2 x1swvt13 x1n2onr6 xlyipyv xh8yej3 xhtitgo x1hxswl6;)]")
    ad_name = ad_name
    ad_name_input.send_keys(ad_name)
    time.sleep(2)
    '''
ad_country=input("Enter the country name: ")
ad_category=input("To choose ad category.Enter 1 for {All Ads} and 2 for {Issues,elections or politics}: ")
ad_brand=input("Enter the brand name or the ad category: ")
enter_main_inputs(ad_country,
                  ad_category,
                  ad_brand)
time.sleep(5)


