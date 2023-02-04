import allure
import pytest
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

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_coutact_us_email_input_incorrect(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("beyenenigatu@.com")
        contact.enter_contact_name("nigatu")
        contact.write_message("let's start")
        contact.click_send_message()

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_coutact_us_name_input_incorrect(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("Beyene@gmail.com")
        contact.enter_contact_name("nsweosrs")
        contact.write_message("let's start")
        contact.click_send_message()

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_coutact_us_message_input_none(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("Beyene@gmail.com")
        contact.enter_contact_name("nigatu")
        contact.write_message("")
        contact.click_send_message()

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_coutact_us_email_input_none(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("")
        contact.enter_contact_name("nigatu")
        contact.write_message("let's start")
        contact.click_send_message()

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_coutact_us_name_input_none(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("beyene@gmail.com")
        contact.enter_contact_name("")
        contact.write_message("let's start")
        contact.click_send_message()

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_coutact_us_email_and_name_input_none(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("")
        contact.enter_contact_name("")
        contact.write_message("let's start")
        contact.click_send_message()

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_coutact_us_name_message_input_none(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("Beyene@gmail.com")
        contact.enter_contact_name("")
        contact.write_message("")
        contact.click_send_message()

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_coutact_us_email_message_input_none(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("")
        contact.enter_contact_name("nigatu")
        contact.write_message("")
        contact.click_send_message()

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_coutact_us_all_inputs_none(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("")
        contact.enter_contact_name("")
        contact.write_message("")
        contact.click_send_message()
