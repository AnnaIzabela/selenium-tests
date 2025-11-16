from pages.home.login_page import LoginPage
from base.webdriver_factory import WebDriverFactory
import pytest

@pytest.fixture(scope="class")
def login_setup(request, browser):
    webdriver_factory = WebDriverFactory(browser)
    driver = webdriver_factory.get_webdriver_instance()

    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    login_page.first_login("user_email@example.com", "user_login")
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser_setup(request, browser):
    webdriver_factory = WebDriverFactory(browser)
    driver = webdriver_factory.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
