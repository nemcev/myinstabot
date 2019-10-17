from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from settings import username, password


""" Bot body """

class Instabot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closebrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        login = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login.click()
        time.sleep(2)
        usrnm_elem = driver.find_element_by_xpath("//input[@name='username']")
        usrnm_elem.clear()
        usrnm_elem.send_keys(self.username)
        time.sleep(2)
        passwrd_elem = driver.find_element_by_xpath("//input[@name='password']")
        passwrd_elem.clear()
        passwrd_elem.send_keys(self.password)
        passwrd_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        no_notification = driver.find_element_by_xpath("//button[@tabindex='0']")
        no_notification.click()
        time.sleep(2)

        

activate = Instabot(username, password)
activate.login()

# <a href="/accounts/login/?source=auth_switcher">Вход</a>
# <button class="aOOlW   HoLwm " tabindex="0">Не сейчас</button>