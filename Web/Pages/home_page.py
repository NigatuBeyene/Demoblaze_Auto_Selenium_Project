import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locatores.locatores_home import *
from Web.Utils.utils import Utils


class home_menus():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.home_button = home_xpath.HOME_BUTTON
        self.contact_button = home_xpath.CONTACT_BUTTON
        self.login_button = home_xpath.LOGIN_BUTTON
        self.signup_button = home_xpath.SIGNUP_BUTTON
        self.categories_button = home_xpath.CATEGORIES
        self.phone_button = home_xpath.PHONE
        self.laptop = home_xpath.LAPTOP
        self.monitors = home_xpath.MONITORS
        self.product_store = home_xpath.PRODUCT_STORE
        self.samsung_galaxy = home_xpath.SAMSUNG_GALAXY
        self.next_button = home_xpath.NEXT_BUTTON
        self.previous_button = home_xpath.PREVIOUS_BUTTON

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_home_button(self):
        self.driver.find_element(By.XPATH, self.home_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_contact_button(self):
        self.driver.find_element(By.XPATH, self.contact_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_signup_button(self):
        self.driver.find_element(By.XPATH, self.signup_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_categories(self):
        self.driver.find_element(By.ID, self.categories_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_phone_category(self):
        self.driver.find_element(By.ID, self.phone_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_laptop_category(self):
        self.driver.find_element(By.XPATH, self.laptop).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_monitors_category(self):
        self.driver.find_element(By.XPATH, self.monitors).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_samsung_galaxyssword_link(self):
        self.driver.find_element(By.XPATH, self.samsung_galaxy).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_previous_button(self):
        self.driver.find_element(By.ID, self.previous_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)
