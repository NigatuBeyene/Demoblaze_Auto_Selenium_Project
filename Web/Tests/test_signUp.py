import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.signUp_page import SignUp_Steps
from Web.Utils.utils import *
from Web.Base_test.base_test import Base_test


class Test_Contact_Page(Base_test):

    @allure.description('signin page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_signin_valid(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signin_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_fist_name("nigatu")
        signin.enter_password("beyene")
        signin.click_signin()

    @allure.description('signin page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_signin_invalid_fist_name_input_none(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signin_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_fist_name("")
        signin.enter_password("beyene")
        signin.click_signin()

    @allure.description('signin page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_signin_invalid_password_input_none(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signin_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_fist_name("nigatu")
        signin.enter_password("")
        signin.click_signin()

    @allure.description('signin page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_signin_invalid_both_fist_name_and_last_input_none(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signin_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_fist_name("")
        signin.enter_password("")
        signin.click_signin()

