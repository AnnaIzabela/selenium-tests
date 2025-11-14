from selenium import webdriver


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        url_address = "http://example.com/login"
        if self.browser == "Firefox":
            driver = webdriver.Firefox()
        elif self.browser == "Chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Edge()

        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(url_address)
        return driver
