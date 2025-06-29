from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://www.dizibox.so"
driver.get(url)

searchInput = driver.find_element(By.NAME, 's') # .find_element_by_name('s')
time.sleep(1)
searchInput.send_keys("vampire")
time.sleep(5)
searchInput.send_keys(Keys.ENTER)
time.sleep(5)

'''
result = driver.page_source
print(result)
'''

result = driver.find_elements(By.CSS_SELECTOR, ".detailed-article-container h3 a")
for element in result:
	print(element.text)


driver.close()
