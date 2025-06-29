from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from instagramUserInfo import userName, password
from selenium import webdriver
import time

didNotGetYetXPathUserName = "" # This variable should be taken from website
didNotGetYetXPathPassword = "" # This variable should be taken from website
XpathFollowers = "//*[@id='mount_0_0_yk']/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span"

class Instagram:

    def __init__(self, userName, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages' : 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.userName = userName
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        self.browser.find_element(By.XPATH, didNotGetYetXPathUserName).send_keys(self.userName)
        self.browser.find_element(By.XPATH, didNotGetYetXPathPassword).send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH, didNotGetYetXPathPassword).send_keys(Keys.ENTER)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.userName}")
        time.sleep(2)
        self.browser.find_element(By.XPATH, XpathFollowers).click()
        time.sleep(3)

        dialog = self.browser.find_element(By.CSS_SELECTOR, "div[role=dialog] ul")
        followersCount = len(dialog.find_elements(By.CSS_SELECTOR, "li"))

        print(f"First Count..: {followersCount}")

        actionOne = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            actionOne.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements(By.CSS_SELECTOR, "li"))

            if(followersCount != newCount):
                followersCount = newCount
                print(f"Count..: {followersCount}")
                time.sleep(2)
            else:
                break
        
        followers = dialog.find_elements(By.CSS_SELECTOR, "li")
        followerList = []
        for user in followers:
            link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            followerList.append(link)

        with open("followers.txt", "w", encoding="utf-8") as file:
            for follower in followerList:
                file.write(follower + "\n")

    def followUser(self, username):
        self.browser.get(f"https://www.instagram.com/{self.userName}")
        time.sleep(2)

        followButton = self.browser.find_element(By.TAG_NAME, "button")
        if(followButton.text != "Following"):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following")

    def unFollowUser(self, username):
        self.browser.get(f"https://www.instagram.com/{self.userName}")
        time.sleep(2)

        followButton = self.browser.find_element(By.TAG_NAME, "button")
        if(followButton.text == "Following"):
            followButton.click()
            time.sleep(2)

            confirmButton = self.browser.find_element(By.XPATH, '//button[text()="Unfollow"]')
            confirmButton.click()
        else:
            print("Ypu already don't follow the user")

instagram = Instagram(userName, password)
instagram.getFollowers()
