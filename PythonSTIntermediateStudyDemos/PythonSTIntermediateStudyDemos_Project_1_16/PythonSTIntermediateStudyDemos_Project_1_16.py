from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://google.com"
driver.get(url)
time.sleep(3)

print(driver.title)
time.sleep(3)

driver.maximize_window()
driver.save_screenshot("google.com-home.png")
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)
time.sleep(3)

driver.back()
time.sleep(3)

driver.close()

# url = "https://en.wikipedia.org/wiki/Main_Page"