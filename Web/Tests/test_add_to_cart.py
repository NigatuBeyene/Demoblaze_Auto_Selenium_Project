
import allure
import pytest
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.add_to_cart_page import cart_steps
from Web.Pages.place_order_page import place_order
from Web.Utils.utils import *
from Web.Base_test.base_test import Base_test


class Test_Cart_Page(Base_test):

    @allure.description('add to cart page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_add_to_cart(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword_s6()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()


    @allure.description('add to cart page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_add_to_cart_more_than_two_product(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword_s6()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        driver.execute_script("window.history.go(-2)")
        home.click_on_samsung_galaxyssword_s7()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        driver.execute_script("window.history.go(-2)")
        order = place_order(driver)
        order.varify_cart_clickable()
        time.sleep(2)


