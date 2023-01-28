import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.login_page import Login_Steps
from Web.Utils.utils import *
from Web.Base_test.base_test import Base_test


class Test_Contact_Page(Base_test):

    @allure.description('contact page test')
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_valid(self):
        driver = self.driver
        login = Login_Steps(driver)
        login.click_on_login_button()
        login.wait = WebDriverWait(self.driver, 10)
        login.enter_fist_name("nigatu")
        login.enter_password("beyene")
        login.click_login()





