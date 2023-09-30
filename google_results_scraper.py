import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options 
import time
chrome_options=Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windws NT 6.2; Win6; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.167.0 Safari/537.36')
browser=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
url ="https://www.google.com/search?q=companies+and+individuals+involved+in+truck+tarpaulin+repair+and+production%2C+tents%2C+and+PVC+in+Poland.&oq=companies+and+individuals+involved+in+truck+tarpaulin+repair+and+production%2C+tents%2C+and+PVC+in+Poland.&aqs=chrome..69i57.860j0j7&sourceid=chrome&ie=UTF-8"

browser.get(url)
soup=BeautifulSoup(browser.page_source,"html.parser")
items= soup.find_all