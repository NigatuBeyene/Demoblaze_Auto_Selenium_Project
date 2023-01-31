import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.contact_page import Contact_Detail
from Web.Utils.utils import *
from Web.Base_test.base_test import Base_test


class Test_Contact_Page(Base_test):

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_coutact_us_valid(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("Beyene@gmail.com")
        contact.enter_contact_name("nigatu")
        contact.write_message("let's start")
        contact.click_send_message()










