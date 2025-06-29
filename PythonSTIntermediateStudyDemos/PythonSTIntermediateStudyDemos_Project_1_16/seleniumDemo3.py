from os import link
from selenium.webdriver.common.by import By
from githubUserInfo import userName, password
from selenium import webdriver
import time

didNotGetYetXPathLogin = "" # This variable should be taken from website
didNotGetYetXPathPassword = "" # This variable should be taken from website
didNotGetYetXPathLogInButton = "" # This variable should be taken from website
didNotGetYetCssSelectorFollowers = "" # This variable should be taken from website
didNotGetYetCssSelectorSingleFollower = "" # This variable should be taken from website
didNotGetYetClassNamePreviousNext = "" # This variable should be taken from website
didNotGetYetTagNameNextButton = "" # This variable should be taken from website

class Github:
    def __init__(self, userName, password):
        self.browser = webdriver.Chrome()
        self.userName = userName
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        
        self.browser.find_element(By.XPATH, didNotGetYetXPathLogin).send_keys(self.userName)
        self.browser.find_element(By.XPATH, didNotGetYetXPathPassword).send_keys(self.password)
        time.sleep(2)

        self.browser.find_element(By.XPATH, didNotGetYetXPathLogInButton).click()

    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, didNotGetYetCssSelectorFollowers)

        for item in items:
            itemText = item.find_element(By.CSS_SELECTOR, didNotGetYetCssSelectorSingleFollower).text
            self.followers.append(itemText)

    def getFollowers(self):
        self.browser.get(f"https://github.com/{userName}?tab=followers")
        time.sleep(2)

        self.loadFollowers()

        while True:
            links = self.browser.find_element(By.CLASS_NAME, didNotGetYetClassNamePreviousNext).find_elements(By.TAG_NAME, didNotGetYetTagNameNextButton)
            if(len(links) == 1):
                if(links[0] == "Next"):
                    links[0].click()
                    time.sleep(2)
                    self.loadFollowers()
                    time.sleep(2)
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(2)
                        self.loadFollowers()
                        time.sleep(2)
                    else:
                        continue

github = Github()
github.signIn()
github.getFollowers()
print(github.followers)