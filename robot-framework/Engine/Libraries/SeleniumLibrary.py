from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By


class NewSeleniumLibrary():
    EMAIL = ""

    @property
    def get_current_webdriver(self):
        selenium_library = BuiltIn().get_library_instance("SeleniumLibrary")
        return selenium_library.driver

    @property
    def get_current_appium_driver(self):
        appium_driver = BuiltIn().get_library_instance("AppiumLibrary").current_application()
        return appium_driver

    def get_email(self):
        return self.get_current_webdriver.find_element(By.CSS_SELECTOR, self.EMAIL).text
