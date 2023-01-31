import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locatores.locator_add_to_cart import *
from Web.Utils.utils import Utils


class cart_steps():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.home_button = cart_xpath.HOME_BUTTON
        self.categories_button = cart_xpath.CATEGORIES
        self.phone_button = cart_xpath.PHONE
        self.samsung_galaxy = cart_xpath.SAMSUNG_GALAXY
        self.add_to_cart = cart_xpath.ADD_TO_CART



    @allure.step
    @allure.description("click_on_home_button")
    def click_on_home_button(self):
        self.driver.find_element(By.XPATH, self.home_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)


    @allure.step
    @allure.description('click_on_categories')
    def click_on_categories(self):
        self.driver.find_element(By.ID, self.categories_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('click_on_phone')
    def click_on_phone(self):
        self.driver.find_element(By.ID, self.phone_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)



    @allure.step
    @allure.description('click_on_samsung_galaxyssword')
    def click_on_samsung_galaxyssword(self):
        self.driver.find_element(By.XPATH, self.samsung_galaxy).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)


    @allure.step
    @allure.description('click_on_add_to_cart')
    def click_on_add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)




