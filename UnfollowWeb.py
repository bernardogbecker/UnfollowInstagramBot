from selenium import webdriver
from time import sleep
from UnfollowList import unFollow
import pyautogui

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Edge(path)
        self.username = username
        self.pw = pw
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
            .click()
        sleep(2)
        if not self.driver.find_elements_by_xpath("//button[contains(text(), 'Agora não')]") == []:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
            .click()
            sleep(2)
    def getUnfollow(self):
        DeixardeSeguir = unFollow(self.username, self.pw)
        for i in range (0, len(DeixardeSeguir)):
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')\
            .send_keys(DeixardeSeguir[i])
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a')\
            .click()
            sleep(4)
            try: 
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/span/span[1]/button')\
                .click()    
                sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]')\
                .click()
                sleep(2)
                print(f'NonFollowers: {len(DeixardeSeguir) - i}')
            except:
                print('erro')
            if i in range(10, len(DeixardeSeguir), 10):
                sleep(600)

USERNAME = '' #Write your USERNAME here
PASS = '' #Write your PASSWORD here
path = 'C:\Program Files\msedgedriver' #Write your path to msedgedriver, download at https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
x = InstaBot(USERNAME, PASS)
x.getUnfollow()

