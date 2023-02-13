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
driver.get("https://www.archanaskitchen.com/recipes?output=322")
driver.implicitly_wait(5)

elem=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/a')
/html/body/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/div/a
/html/body/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div/div/a
all_li=elem.find_elements(By.TAG_NAME,'li')
i=1
for li in all_li:
    j=1
    category=driver.find_element(By.XPATH,'/html/body/nav/div/div/ul/li[{}]/a'.format(i))
    i=i+1
    category.click()
    recipe=driver.find_elements(By.TAG_NAME,'article')
    for article in recipe:
        name=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/main/article[{}]/div/header/h2/a'.format(j))
        print(name.text)
        j=j+1
        driver.implicitly_wait(10)
        name.click()
        
        div_containing_uls=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/main/article/div/div')
        uls=div_containing_uls.find_elements(By.TAG_NAME,'ul')
        templist=[]
        for ul in uls:
            second_li=ul.find_elements(By.TAG_NAME,'li')
            for a in second_li:
                driver.implicitly_wait(10)
                
                print(a.text)
        
        driver.execute_script("window.history.go(-1)")
        




