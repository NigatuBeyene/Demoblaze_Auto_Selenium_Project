import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locatores.locatores_contact_us import *
from Web.Utils.utils import Utils


class Contact_Detail:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.contact_button = Contact_Id.CONTACT_BUTTON
        self.emailID = Contact_Id.EMAIL
        self.nameID = Contact_Id.NAME
        self.messageID = Contact_Id.MESSAGE_FIELD
        self.Send_messageXPath = Contact_Id.SEND_MESSAGE

    @allure.step
    @allure.description('click_on_contact_button')
    def click_on_contact_button(self):
        self.driver.find_element(By.XPATH, self.contact_button).click()
        # self.driver.implicitly_wait(100)
        time.sleep(2)

    @allure.step
    @allure.description('enter_user_email')
    def enter_user_email(self, User_email):
        email = self.driver.find_element(By.ID, self.emailID)
        email.clear()
        email.send_keys(User_email)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        Utils(self.driver).assertion(User_email, email.get_attribute('value'))
        return email

    @allure.step
    @allure.description("enter_contact_name")
    def enter_contact_name(self, User_name):
        username = self.driver.find_element(By.ID, self.nameID)
        username.clear()
        username.send_keys(User_name)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        return username

    @allure.step
    @allure.description('write_message')
    def write_message(self, User_message):
        message = self.driver.find_element(By.ID, self.messageID)
        message.clear()
        message.send_keys(User_message)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        return message

    @allure.step
    @allure.description('click_send_message')
    def click_send_message(self):
        self.driver.find_element(By.XPATH, self.Send_messageXPath).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)
