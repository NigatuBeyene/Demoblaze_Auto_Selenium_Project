import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.home_page import Home_Tests
from Web.Utils.utils import *
from Web.Base_test.base_test import Base_test


class Test_Contact_Page(Base_test):

    @allure.description('contact page test')
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_valid(self):
        driver = self.driver
        home = Home_Tests(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()