import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.signUp_page import SignUp_Steps
from Web.Utils.utils import *
from Web.Base_test.base_test import Base_test


class Test_Contact_Page(Base_test):

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_valid(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_login_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_fist_name("nigatu")
        signin.enter_password("beyene")
        signin.click_login()