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
        self.laptop_button = cart_xpath.LAPTOP
        self.monitor_button = cart_xpath.MONITORS
        self.samsung_galaxy_s6 = cart_xpath.SAMSUNG_GALAXY_s6
        self.samsung_galaxy_s7 = cart_xpath.SAMSUNG_GALAXY_s7
        self.sony_vaio = cart_xpath.SONY_VAIO
        self.asus_full_hd = cart_xpath.ASUS_FULL_HD
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
    @allure.description('click_on_samsung_galaxyssword_s6')
    def click_on_samsung_galaxyssword_s6(self):
        self.driver.find_element(By.XPATH, self.samsung_galaxy_s6).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('click_on_samsung_galaxyssword_s7')
    def click_on_samsung_galaxyssword_s7(self):
        self.driver.find_element(By.XPATH, self.samsung_galaxy_s7).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('click_on_laptop')
    def click_on_laptop(self):
        self.driver.find_element(By.XPATH, self.laptop_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('click_on_sony_vaio')
    def click_on_sony_vaio(self):
        self.driver.find_element(By.XPATH, self.sony_vaio).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('click_on_monitor')
    def click_on_monitor(self):
        self.driver.find_element(By.XPATH, self.monitor_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('click_on_asus_full_hd')
    def click_on_asus_full_hd(self):
        self.driver.find_element(By.XPATH, self.asus_full_hd).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('click_on_add_to_cart')
    def click_on_add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)
