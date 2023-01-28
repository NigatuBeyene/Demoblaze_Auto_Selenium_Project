import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from allure_commons.types import AttachmentType

class Utils:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step
    @allure.description('This validation method, if the assert failed screenshot is taken')
    def assertion(self, expected_chrome, actual, expected_firefox=None):
        driver = self.driver
        try:
            assert expected_chrome == actual
        except AssertionError:
            try:
                assert expected_firefox == actual
            except AssertionError:
                allure.attach(driver.get_screenshot_as_png(), name='screenShot',
                              attachment_type=AttachmentType.PNG)
                raise AssertionError

    @allure.description('This function will get text and a end value, cut the text from the end value to the end')
    def slicing(self, text, end):
        new_text = ''
        for i in range(len(text)):
            if text[i] == end:
                new_text = text[i + 1:]
        return new_text