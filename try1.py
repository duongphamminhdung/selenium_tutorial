import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

osUsing = input("mac or window?")
if osUsing == 'mac':
    PATH = "/Users/duongphamminhdung/Documents/GitHub/chromedriver"
else:
    PATH = "D:\Documents\GitHub\chromedriver_win32\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")  
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
url_goc = input("url ?")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
driver.get(url_goc)
numberOfChapter = int(driver.find_element(By.ID, "noofchapter").text)
title = driver.find_element(By.ID, "book_name2").text
print("Downloading " + title + ", has " + str(numberOfChapter) + " chapters")
driver.close()
for i in range(numberOfChapter):
    f = open(title + ".txt", "a", encoding='utf-8')
    url = url_goc + str(i + 1) + '/'
    print(url)
    print("Downloading chapter " + str(i + 1))
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
    driver.get(url)
    content = driver.find_elements(By.CLASS_NAME, 'contentbox')[1].text
    chaptername = driver.find_elements(By.ID, "bookchapnameholder")[0].text 
    time.sleep(50)
    driver.close()
    f.close()
    
print("DONE "*10)