from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
from base.base_page import BasePage
import time


class LoginPage(BasePage):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ 
    Locators  
    """

    _login_ = "login"
    _password_ = "password"
    _login_button_ = "//button[@type='submit']"
    _login_pass_ = "//div[@class='logo-container']"
    _login_failed_ = "//mat-error[text()='Login lub hasło jest nieprawidłowe']"
    _empty_login_ = '''//mat-error[text()="Pole 'login' jest wymagane"]'''
    _empty_password_ = '''//mat-error[text()="Pole 'hasło' jest wymagane"]'''

    def enter_login(self, user_name):
        self.send_keys_to_element(user_name, self._login_)

    def enter_password(self, password):
        self.send_keys_to_element(password, self._password_)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self._login_button_)

    def click_login_button(self):
        self.click_on_element(self._login_button_, By.XPATH)

    def login(self, user_name="", password=""):
        self.driver.refresh()
        self.enter_login(user_name)
        self.enter_password(password)
        time.sleep(1)
        self.click_login_button()

    def first_login(self, user_name="", password=""):
        self.enter_login(user_name)
        self.enter_password(password)
        self.click_login_button()

    def clear_fields(self):
        login = self.get_element(self._login_)
        login.clear()
        password = self.get_element(self._password_)
        password.clear()

    def verify_login_passed(self):
        self.driver.implicitly_wait(3)
        logo = self.presence_of_the_element(self._login_pass_, By.XPATH)
        return logo

    def verify_login_failed(self):
        failed_message = self.presence_of_the_element(self._login_failed_, By.XPATH)
        return failed_message

    def verify_empty_login(self):
        no_login_message = self.presence_of_the_element(self._empty_login_, By.XPATH)
        return no_login_message

    def verify_empty_password(self):
        no_password_message = self.presence_of_the_element(self._empty_password_, By.XPATH)
        return no_password_message

    def verify_no_login_data(self):
        element_01 = self.get_element(self._empty_login_, By.XPATH)
        element_02 = self.get_element(self._empty_password_, By.XPATH)
        if element_01 and element_02:
            return True
