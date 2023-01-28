# from selenium.webdriver.chrome import webdriver
#
#
# class Base_test():
#
#     def initial(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://www.demoblaze.com/")
#         self.driver.maximize_window()
#         return self.driver
#
#     def window_close(self):
#         self.driver.quite()
#         self.driver.close()

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


class Base_test:
    driver = None
    @pytest.fixture(autouse=True)
    def set_up(self):

        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.demoblaze.com/index.html")
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.quit()