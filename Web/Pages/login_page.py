import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locatores.locatores_login import *
from Web.Utils.utils import Utils


class Login_Steps():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.login_button = Login_Id.LOGIN_BUTTON
        self.nameID = Login_Id.NAME
        self.passwordID = Login_Id.PASSWORD
        self.login_click = Login_Id.LOGIN_CLICK

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def enter_fist_name(self, User_name: str):
        username = self.driver.find_element(By.ID, self.nameID)
        username.clear()
        username.send_keys(User_name)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        Utils(self.driver).assertion(User_name, username.get_attribute('value'))
        return username

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def enter_password(self, User_password: str):
        userpassword = self.driver.find_element(By.ID, self.passwordID)
        userpassword.clear()
        userpassword.send_keys(User_password)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        Utils(self.driver).assertion(User_password, userpassword.get_attribute('value'))
        return userpassword

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_click).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        title = self.driver.title
        assert title == "STORE"
