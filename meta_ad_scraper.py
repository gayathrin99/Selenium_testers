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
import tqdm
from tqdm import tqdm
all_category_path="./"
url="https://www.facebook.com/ads/library/"
driver=webdriver.Chrome()
time.sleep(5)
ad_status=[]
ad_data=[]
ad_started_running_date=[]
path1 = "All type"
path2 = "Issues, Politics and Elections"
isExist = os.path.exists(path1)
if not isExist:
    os.makedirs(path1)
    print("The new directory for ad type is created!")
isExist = os.path.exists(path2)
if not isExist:
    os.makedirs(path2)
    print("The second directory for ad type is created!")
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
def alpharemover(image):
    if image.mode != 'RGBA':
        return image
    canvas = Image.new('RGBA', image.size, (255,255,255,255))
    canvas.paste(image, mask=image)
    return canvas.convert('RGB')
def with_ztransform_preprocess(hashfunc, hash_size=8):
    def function(path):
        image = alpharemover(Image.open(path))
        image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)
        data = image.getdata()
        quantiles = np.arange(100)
        quantiles_values = np.percentile(data, quantiles)
        zdata = (np.interp(data, quantiles_values, quantiles) / 100 * 255).astype(np.uint8)
        image.putdata(zdata)
        return hashfunc(image)
    return function
dhash_z_transformed = with_ztransform_preprocess(imagehash.dhash, hash_size = 8)
def get_ad_details(url):
    url="https://www.facebook.com/ads/library/"
    page=requests.get(url)
    time.sleep(5)
    no_results=driver.find_element(By.XPATH,"//div[@class= 'x8t9es0 x1uxerd5 xrohxju x108nfp6 xq9mrsl x1h4wwuj x117nqv4 xeuugli']").text
    print("FB Directory has "+no_results+" for this brand")
    itemTargetCount=int(''.join([i for i in no_results if i.isdigit()]))
    #print(itemTargetCount)
    screen_height=driver.execute_script("return window.screen.height;")
    j=1
    time.sleep(5)
    src_number=0
    file=open("ad data.xlsx","w+",encoding='utf-8')
    workbook=xlsxwriter.Workbook("ad data.xlsx")
    worksheet1=workbook.add_worksheet()
    worksheet1.write(0,0,"Sl No.")
    worksheet1.write(0,1,"Ad Text")
    worksheet1.write(0,3,"Image file Name")
    cumulative_ad_length=0
    while True:
        driver.execute_script("window.scrollTo(0,{screen_height}*{j});".format(screen_height=screen_height, j=j))
        j = j+1
        time.sleep(2)
        scroll_height = driver.execute_script("return document.body.scrollHeight;") 
        if (screen_height) * j > scroll_height:
            break           
            #print(img.get_attribute('src'))
        ads=driver.find_elements(By.XPATH,"//div[@class= 'x6s0dn4 x78zum5 xdt5ytf xl56j7k x1n2onr6 x1ja2u2z x19gl646 xbumo9q']")
        cumulative_ad_length+=len(ads)
        src_number=0
        data_row_number=1
        image_row_number=1
        print(str((cumulative_ad_length/itemTargetCount)*100)+"% done.")
        x=0
        for ad in ads:
            src=[]
            images= ad.find_elements(By.XPATH,"//img[@class= 'x1ll5gia x19kjcj4 xh8yej3']")
            ad_text=ad.find_elements(By.XPATH,"//div[@class= '_4ik4 _4ik5']")
            for img in images:
                src.append(img.get_attribute("src"))
            #src_number=src_number+len(src)-1
            #print("src_numer="+str(src_number))
            for i in ad_text:
                ad_data.append(i.text)
            #print("length of src="+str(len(src)))
            worksheet1.write(x+1,0,x+1)
            ad_data_string="\n".join(ad_data)
            worksheet1.write(x+1,1,str(ad_data_string))
            src_number_list=[]
            for i in range(0,len(src)):
                #print (str(i)+"/"+str(len(src)))
                urllib.request.urlretrieve(str(src[i]),"{}.jpg".format(src_number))
                src_number=src_number+1
                src_number_list.append("{}.jpg".format(src_number))
            worksheet1.write(x+1,3,str("\n".join(src_number_list)))
            x=x+1
        #print("src number "+ str(src_number)
        
        workbook.close()
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
    if ad_category == "2":
        parent_directory=os.getcwd()
        os.chdir(parent_directory+"\Issues, Politics and Elections\\"+path+"\\")
    else:
        parent_directory=os.getcwd()
        os.chdir(parent_directory+"\All type\\")
    path=ad_brand
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    parent_directory=os.getcwd()
    os.chdir(parent_directory+"\\"+path+"\\")
    get_ad_details(urllatest)
    time.sleep(1)

ad_country=input("Enter the country name: ")
ad_category=input("To choose ad category.Enter 1 for {All Ads} and 2 for {Issues,elections or politics}: ")
ad_brand=input("Enter the brand name or the ad category: ")
enter_main_inputs(ad_country,
                  ad_category,
                  ad_brand)
time.sleep(5)


