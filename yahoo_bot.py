import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("https://www.yahoo.com")
def login_with_username_password(browser, username, password):
    sign_in_button=browser.find_element("link text","Sign in")
    browser.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              sign_in_button, "border: {0}px solid {1};".format(5, "blue"))
    time.sleep(2)
    sign_in_button.click()
    email_input=browser.find_element("id",'login-username')
    email=username
    for letter in email:
        email_input.send_keys(letter)
        wait_time=random.randint(0,1000)/1000
        time.sleep(wait_time)
    next_button = browser.find_element("id",'login-signin')
    browser.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              next_button, "border: {0}px solid {1};".format(5, "red"))
    time.sleep(2)
    next_button.click()
    time.sleep(2)
   # password_input=browser.find_element("id",'login-passwd')
    password_input=browser.find_element("id",'login-passwd')
    time.sleep(2)
    password=password
    for letter in password:
        password_input.send_keys(letter)
        wait_time=random.randint(0,1000)/1000
        time.sleep(wait_time)

    next_button=browser.find_element("id","login-signin")
    time.sleep(2)
    next_button.click()
def compose_a_mail(browser,reciever_mail,message):
    mail_link=browser.find_element("xpath",'/html/body/header/div/div/div/div/div/div[4]/div/div/ul/li[1]/a')
    browser.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              mail_link, "border: {0}px solid {1};".format(5, "blue"))
    time.sleep(2)
    mail_link.click()
    compose_button=browser.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[2]/div/div[1]/nav/div/div[1]/a")
    time.sleep(1)
    compose_button.click()
    time.sleep(3)
    to_link=browser.find_element("xpath",'//*[@id="message-to-field"]')
    to_mail=reciever_mail
    for letter in to_mail:
        to_link.send_keys(letter)
        wait_time=random.randint(0,1000)/1000
        time.sleep(wait_time)
    #subject_line=browser.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[4]/div/div/input')
    subject_line=browser.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    for letter in "yahoo mail":
        subject_line.send_keys(letter)
        wait_time=random.randint(0,1000)/1000
        time.sleep(wait_time)
    #email_body=browser.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div')
    email_body=browser.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div')
    message=message
    for letter in message:
        email_body.send_keys(letter)
        wait_time=random.randint(0,1000)/1000
        time.sleep(wait_time)
    #send_button=browser.find_element("xpath",'//*[@id="mail-app-component"]/div[1]/div/div/div[2]/div[2]/div/button/span')
    send_button=browser.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/button')
    send_button.click()
login_with_username_password(browser,"gayathrin99","Varalakshmi@99")
compose_a_mail(browser,"gayathrin.bmsce@gmail.com","Yolo!")
