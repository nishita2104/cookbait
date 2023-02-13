

'''from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())'''
from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions


#object of ChromeOptions class
o = webdriver.ChromeOptions()
#adding Chrome Profile Path
o.add_argument = {'user-data-dir':'C:/Users/dell/AppData/Local/Google/Chrome/User Data/Default'}
o.add_experimental_option('excludeSwitches', ['enable-logging'])
o.headless=True
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path="C:/Users/dell/Desktop/chromedriver.exe", options=o)

driver.maximize_window()
driver.get("https://www.indianfoodforever.com/")
driver.implicitly_wait(5)

elem=driver.find_element(By.XPATH,'/html/body/nav/div/div/ul')
all_li=elem.find_elements(By.TAG_NAME,'li')
i=1
file=open('data.txt','w')
for li in all_li:
    j=1
    category=driver.find_element(By.XPATH,'/html/body/nav/div/div/ul/li[{}]/a'.format(i))
    i=i+1
    category.click()
    recipe=driver.find_elements(By.TAG_NAME,'article')
    wb = load_workbook('data.xlsx')
    ws = wb.active
    k=1
    for article in recipe:
        name=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/main/article[{}]/div/header/h2/a'.format(j))
        print(name.text)
        j=j+1
        driver.implicitly_wait(10)
        Table_dict={
            'Recipe':name.text
        }
        name.click()
        try:
            ul=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/main/article/div/div/div[4]/div/div[14]/div/ul')
            second_li=ul.find_elements(By.TAG_NAME,'li')
        
            for a in second_li:
                driver.implicitly_wait(10)
                file.write(a.text)
                file.write('\n')
                print(a.text)
        except NoSuchElementException:
            pass
        
        driver.execute_script("window.history.go(-1)")
        




