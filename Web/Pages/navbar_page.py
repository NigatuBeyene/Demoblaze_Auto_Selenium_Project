# "" NavBar page, contain all the actions (links, search)"""

import allure
from Web.Utils.utils import Utils
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locators.Web_Locators.locators_navbar import NavBar_Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class NavBar:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.searchField = NavBar_Locators.SEARCH_FIELD
        self.cityNameCorrectly = NavBar_Locators.CITY_NAME
        self.cityNameIncorrectly = NavBar_Locators.CITY_ERROR_MESSAGE
        self.navBarLinks = NavBar_Locators.NAV_BAR_LINKS

    @allure.step
    @allure.description('The search method that included valid and invalid search')
    def searching(self, city_name):
        searching = self.driver.find_element(By.CLASS_NAME, self.searchField)
        searching.send_keys(city_name)
        Utils(self.driver).assertion(city_name, searching.get_attribute('value'))
        searching.send_keys(Keys.ENTER)

    @allure.step
    @allure.description('Validation - message when search is correctly')
    def city_name_correctly(self):
        return self.driver.find_element(By.XPATH, self.cityNameCorrectly).get_attribute('innerText')

    @allure.step
    @allure.description('Validation - message when search is incorrectly')
    def city_name_incorrectly(self):
        return self.driver.find_element(By.XPATH, self.cityNameIncorrectly).get_attribute('innerText')

    @allure.step
    @allure.description('Clicking on all the links in the navbar and return to the current page when user not connect')
    def click_navbar_links(self, page_name):
        driver = self.driver
        nav_bar_links = self.driver.find_elements(By.XPATH, self.navBarLinks)
        Utils(self.driver).assertion(4, len(nav_bar_links))

        for link in range(len(nav_bar_links)):
            if nav_bar_links[link].text == page_name:
                continue
            nav_bar_links[link].click()
            if link == 0:
                Utils(self.driver).assertion('Login', nav_bar_links[link].text)
                Utils(self.driver).assertion(driver.current_url, 'https://trip-yoetz.herokuapp.com/login')
            elif link == 1:
                Utils(self.driver).assertion('Register', nav_bar_links[link].text)
                Utils(self.driver).assertion(driver.current_url, 'https://trip-yoetz.herokuapp.com/register')
            elif link == 2:
                Utils(self.driver).assertion('About us', nav_bar_links[link].text)
                Utils(self.driver).assertion(driver.current_url, 'https://trip-yoetz.herokuapp.com/about')
            elif link == 3:
                Utils(self.driver).assertion('TripYoetz', nav_bar_links[link].text)
                Utils(self.driver).assertion(driver.current_url, 'https://trip-yoetz.herokuapp.com/')
            driver.back()

    @allure.step
    @allure.description('Clicking on all the links in the navbar and return to the current page when user is connect')
    def click_navbar_links_1(self, div_option: int):
        locator = f'//header/div[{div_option}]/a'
        link = self.driver.find_element(By.XPATH, locator)
        if div_option == 1:
            link.click()
            Utils(self.driver).assertion('/profile', link.get_attribute('pathname'))
        elif div_option == 3:
            link.click()
            Utils(self.driver).assertion('About us', link.get_attribute('innerText'))
        elif div_option == 4:
            link.click()
            Utils(self.driver).assertion("TripYoetz", link.get_attribute('innerText'))
        else:
            raise ValueError('div_position need to be 1,3,4')
        self.driver.back()