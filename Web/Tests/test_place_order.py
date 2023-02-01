import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Web.Utils.utils import *
from Web.Base_test.base_test import Base_test
# from Web.Tests.test_add_to_cart import *
from Web.Pages.place_order_page import *


class Test_Place_Order(Base_test):

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_add_to_cart_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("nigatu")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_add_to_cart_name_field_null_E2E(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword_s7()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_add_to_cart_country_field_null_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("nigatu")
        order.insert_data_to_country_input("")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_add_to_cart_city_field_null_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("nigatu")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_add_to_cart_credit_card_null_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("nigatu")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_add_to_cart_month_field_null_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("nigatu")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_add_to_cart_year_field_null_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("nigatu")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_add_to_cart_name_and_country_null_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("")
        order.insert_data_to_country_input("")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_add_to_cart_name_and_city_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_add_to_cart_name_and_credit_card_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("nigatu")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_add_to_cart_name_and_month_null_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_add_to_cart_name_and_year_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_add_to_cart_country_and_city_null_E2E(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("nigatu")
        order.insert_data_to_country_input("")
        order.insert_data_to_city_input("")
        order.insert_data_to_credit_card_input("8765432")
        order.insert_data_to_month_input("2")
        order.insert_data_to_year_input("1980")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_close_button_clickable(self):
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
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.scrolling_the_page()
        order.verify_close_clickable()
