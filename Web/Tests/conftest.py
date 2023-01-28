# import ChromeDriver
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
import os
from time import sleep
from Web.Utils.utils import Utils
import pytest

class Web_Fixtures:

    @staticmethod
    def gh_token():
        path = 'C://Users//yossi//PycharmProjects//python_Lessons/gh_token.txt'
        token = open(path).read()
        return token

    @pytest.fixture(autouse=True)
    def set_up(self, browser):
        if browser == 'chrome':
            print('\n----------------------')
            print('Initialing Chrome Driver')
            # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriver().install()))
            self.driver = webdriver.Chrome()
            print('----------------------')
            print('\n----------------------')
            print('Test is Started')
            print('------------------------')

        elif browser == 'firefox':
            print('\n----------------------')
            os.environ['GH_TOKEN'] = self.gh_token()
            print('Initialing FireFox Driver')
            # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            self.driver = webdriver.Firefox()
            print('----------------------')
            print('\n----------------------')
            print('Test is Started')
            print('------------------------')
        else:
            raise ValueError('Please insert valid Driver.')
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            print("\n----------------------------")
            print("Test is Finished")
            print('------------------------------')
            self.driver.close()
            self.driver.quit()

    @pytest.fixture(name='pre_condition')
    def login_successfully(self):
        driver = self.driver
        login = Login_Page(driver)
        login.login_page()
        login.enter_email('Yosf@gmail.com')
        login.enter_password('123456')
        login.login_button()
        login.accept_alert()
        sleep(0.5)
        driver.forward()
        login.click_profile_link()
        Utils(driver).assertion('YOUR INFORMATION', login.login_validation_message())

    @pytest.fixture(name='search')
    def search_correctly(self, city_name):
        NavBar(driver=self.driver).searching(city_name)
        Utils(driver=self.driver).assertion(f'Discover {city_name}', NavBar(driver=self.driver).city_name_correctly())


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox"
                    )

@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption("--browser")