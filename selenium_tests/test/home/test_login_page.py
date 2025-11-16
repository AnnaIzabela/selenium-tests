import time
import test_data.login_data
from pages.home.login_page import LoginPage
import unittest
import pytest
from ddt import ddt, data, unpack
from test_data.login_data import FakeData


@ddt
@pytest.mark.usefixtures("browser_setup", "browser")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login_page = LoginPage(self.driver)
        self.login_data = FakeData()

    @data(*test_data.login_data.get_csv_data("./test_data/login_data.csv"))
    @unpack
    @pytest.mark.run(order=5)
    def test_valid_login(self, user_name, password):
        self.login_page.login(user_name, password)
        time.sleep(1)
        result = self.login_page.verify_login_passed()
        assert result is True

    @pytest.mark.run(order=4)
    def test_invalid_login_data(self):
        self.login_page.login(self.login_data.email, self.login_data.password)
        time.sleep(1)
        result = self.login_page.verify_login_failed()
        assert result is True

    @pytest.mark.run(order=2)
    def test_no_login_entered(self):
        self.login_page.login("", self.login_data.password)
        time.sleep(1)
        result = self.login_page.verify_empty_login()
        assert result is True

    @pytest.mark.run(order=3)
    def test_no_password_entered(self):
        self.login_page.login(self.login_data.email, "")
        time.sleep(1)
        result = self.login_page.verify_empty_password()
        assert result is True

    @pytest.mark.run(order=1)
    def test_no_login_data(self):
        self.login_page.first_login()
        time.sleep(1)
        result = self.login_page.verify_no_login_data()
        assert result is True
