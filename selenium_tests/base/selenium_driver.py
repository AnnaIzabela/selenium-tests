from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.custom_logger as cl
import time
import os


class SeleniumDriver:
    log = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, locator_type=By.ID):

        try:
            element = self.driver.find_element(locator_type, locator)
            self.log.info("Element found by locator" + " and locator type " + locator_type)
            return element
        except:
            self.log.error("element not found by locator:" + locator + " and locator type " + locator_type)
        # return element

    def click_on_element(self, locator, locator_type=By.ID):
        try:
            self.get_element(locator, locator_type).click()
            self.log.info("clicked on element:" + locator + " and locator type " + locator_type)
        except:
            self.log.error("Cannot click on the element with locator: " + locator + " and locator type " + locator_type)

    def send_keys_to_element(self, keys, locator, locator_type=By.ID):
        try:
            self.get_element(locator, locator_type).send_keys(keys)
            self.log.info("Sent data on element with locator: " + locator + " and locator type " + locator_type)
        except:
            self.log.error("Cannot send data on element with locator: " + locator + " and locator type " + locator_type)

    def presence_of_the_element(self, locator, locator_type=By.ID):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element is present")
                return True
            else:
                self.log.error("Element is not present")
                return False
        except:
            self.log.error("element is not present")
            return False

    def presence_of_the_elements(self, locator, locator_type=By.ID):
        elements = self.driver.find_elements(locator, locator_type)
        if len(elements) > 0:
            self.log.info("elements found" + locator + " and locator type " + locator_type)
            return True
        else:
            self.log.error("elements not found" + locator + " and locator type " + locator_type)
            return False

    def element_is_enabled(self, locator, locator_type=By.ID):
        element = self.get_element(locator, locator_type)
        enabled = element.is_enalbed()
        if enabled:
            self.log.info("element enabled" + locator + " and locator type " + locator_type)
        else:
            self.log.error("element disabled" + locator + " and locator type " + locator_type)
        return enabled

    def wait_for_element(self, locator, locator_type=By.ID, timeout=10, pollFrequency=0.5):
        element = None
        try:
            self.log.info("Waiting for maximum " + str(timeout) +
                          " seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def screen_shot(self, result_message):
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("Exception Occurred when taking screenshot")
            print_stack()
