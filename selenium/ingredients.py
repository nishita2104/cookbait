'''
from selenium import webdriver
from webdriver_manager. import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.indianfoodforever.com/")
print("application title",driver.title)
print("application url",driver.current_url)
driver.quit()'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "C:/Users/dell/Desktop/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument('--ignore-certificate-errors-spki-list')
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(driver_path, options=option)
browser.maximize_window()

browser.get("https://hebbarskitchen.com/")
browser.implicitly_wait(5) #time.sleep(30)
# head = driver.find_element(By.XPATH, driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div[1]/div/div[2]/div[1]/div/h3/a"))
# print(head, "\n")

first_element = browser.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[3]/div/div/div[2]/div/div[3]/div/div/div/ul/li[2]/a")
print(first_element.text)
first_element.click()

browser.implicitly_wait(5) #time.sleep(30)

second_element = browser.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div[1]/div/div[2]/div[1]/div/h3/a")
print(second_element.text)
second_element.click()


third_element = browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[1]/header/h1")
print("Dish : ", third_element.text)
# third_element.click()

fourth_element = browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[2]/div[8]/div/div[11]/div[1]/span[3]")
print("Prep-Time : ", fourth_element.text)

fifth_element = browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[2]/div[8]/div/div[11]/div[2]/span[3]")
print("Cook-Time : ", fifth_element.text)

sixth_element = browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[2]/div[8]/div/div[11]/div[3]/span[3]")
print("Total-Time : ", sixth_element.text)


seventh_element = browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[2]/div[8]/div/div[13]/div[2]/div[2]/div[2]/span[3]")
print("Calories : ", seventh_element.text)


eighth_element = browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[2]/div[8]/div/div[15]")
print("Ingredients : ", "\n",  eighth_element.text)


ninth_element = browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[1]/div/article/div[2]/div[8]/div/div[17]")
print("Recipe : ", "\n", ninth_element.text)