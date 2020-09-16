from selenium import webdriver
from time import sleep
from FollowList import Follow
import pyautogui

class InstaBot:
    def __init__(self, username, pw, usernameToFollow):
        self.driver = webdriver.Edge(path)
        self.username = username
        self.pw = pw
        self.usernameToFollow = usernameToFollow
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
            .click()
        sleep(2)
        if not self.driver.find_elements_by_xpath("//button[contains(text(), 'Agora não')]") == []:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")\
            .click()
            sleep(2)
    def getfollow(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')\
            .send_keys(self.usernameToFollow)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a')\
            .click()
        Seguir = Follow(self.driver)
        for i in range (0, len(Seguir)):
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')\
            .send_keys(Seguir[i])
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a')\
            .click()
            sleep(4)
            try: 
                self.driver.find_element_by_xpath("//button[contains(text(), 'Seguir')]")\
                .click()    
                sleep(2)
                print(f'Seguindo: {i}')
            except:
                print('erro')
            if i in range(10, len(Seguir), 20):
                sleep(600)

USERNAME = 'petma_ufsc' #Write your USERNAME here
PASS = 'madruGa10' #Write your PASSWORD here
USERNAMETOFOLLOW = 'neo.empresarial' #Write the user you want to steal all the following
path = 'C:\Program Files\msedgedriver' #Write your path to msedgedriver, download at https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
x = InstaBot(USERNAME, PASS, USERNAMETOFOLLOW)
x.getfollow()

