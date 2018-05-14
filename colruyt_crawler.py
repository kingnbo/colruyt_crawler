# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 09:33:47 2018

@author: Steve
"""
#This is a simple crawler that goes through the different pages of a food category on colruyt.be. This code still needs a bit of tweaking because it requires too much user input.
#
#To run this code:
#
#1.Choose the category you would like to get products from.
#
#2.Replace this category in line 37 of colruyt_crawler.py example : replace "Viande" with "Boisson"
#
#3.Perform a search on colruyt.be for the keyword Boisson and check at the bottom of the page the number of pages of results you have.
#
#4.Change the condition on line 80 to if n== the number of pages when searching for Boisson on colruyt.be + 1 (92+1=93)
#
#5.To see the prices on colruyt.be you need to be signed up. Create an account and change the credentials on line 29 with your username and line 31 with your password.
#
#6.run the code BUT make sure the chrome browser window that opens is full screen and that the cookies notification bar (grey bar at the bottom of the page) is hidden. (Click on "Masquer cette notification")
#
#7.The code should then run if you keep the chorme browser window visible on your screen.

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
import time
import re
import math


option = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path="C:/Users/Steve/Desktop/chromedriver.exe", chrome_options=option)
browser.get("https://www.colruyt.be/fr/rechercher/produits?searchterm=viandes#/recherche/viandes")      
WebDriverWait(browser, 20)         
button = browser.find_element(By.XPATH, '//button[text()="Se connecter"]')
button.click() 
WebDriverWait(browser, 20)
browser.switch_to.frame(0)
username = browser.find_element_by_xpath('.//input[@type = "text"][@name = "loginName" ]')
username.send_keys("cmiassist1@gmail.com")
password = browser.find_element_by_xpath('.//input[@type = "password"][@name = "password" ]')
password.send_keys("Intergang7602")
browser.find_element_by_xpath('.//button[@type = "submit"]').click()
wait = ui.WebDriverWait(browser,10)
wait.until(lambda browser: browser.find_element_by_xpath('.//main[@class = "container"]'))
browser.switch_to.default_content()
search = browser.find_element_by_xpath('.//input[@type = "text"]')
search.send_keys("Viande")
search.send_keys(Keys.RETURN)


title =[]
desc = []
price = []

n=2

while True:
    time.sleep(10)


    titles_element = browser.find_elements_by_xpath(".//span[@class='brand']")

    desc_element = browser.find_elements_by_xpath(".//span[@class='description']")

    price_element = browser.find_elements_by_xpath(".//span[@ng-class='{redPrice: product.redPrice}'][@class='piecePrice'or @class = 'piecePrice redPrice']")


    #use list comprehension to get the actual repo titles and not the selenium objects.
    titles = [x.text for x in titles_element]
    #print('titles:')
    #print(titles, '\n')

    descs =[y.text for y in desc_element]
    #print('description:')
    #print (desc, '\n')

    prices = [z.text for z in price_element]
    ## print out all the titles.
    #print('Price:')
    #print(price,'\n')

    title.append(titles)
    desc.append(descs)
    price.append(prices)
    link = browser.find_elements_by_xpath(".//a[@href='/fr/rechercher/produits?searchterm=Viande#/recherche/Viande']")
    number_product=[u.text for u in link ]
    total_pages =re.search(r'\((.*?)\)',number_product[0]).group(1)
    number_of_pages = math.ceil( int(total_pages)/len(titles))
    print(number_of_pages)
    if n==17:
        break;

    element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, ".//li[@ng-class = '{active: page === currentPage}'and contains(text(), "+str(n)+")]")))
    #browser.find_elements_by_xpath(".//li[@ng-class = '{active: page === currentPage}'and contains(text(), '2')]").click()
    browser.execute_script('arguments[0].scrollIntoView(false);', element)
    time.sleep(5)

    element.click()
    
    
    n=n+1    
#print(price)
browser.close()

