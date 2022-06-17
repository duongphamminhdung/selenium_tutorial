import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/duongphamminhdung/Documents/GitHub/chromedriver")
# url = input('url? ')
url = 'https://sangtacviet.me/truyen/faloo/1/566332/1/'
driver.get(url)
time.sleep(5)

print("SLEPT")
contentBox = driver.find_element(By.CLASS_NAME,value= 'contentbox')
print("FOUND")
print(contentBox)