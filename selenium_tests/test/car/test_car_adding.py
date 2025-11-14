import pytest
import test_data.login_data
from pages.car.car_adding_page import AddCar
import unittest
from test_data.login_data import FakeData
import time
from ddt import data, unpack, ddt


@ddt
@pytest.mark.usefixtures("login_setup", "browser")
class AddCarTest(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.car_adding_page = AddCar(self.driver)
        self.fake_data = FakeData()
        self.car_adding_page.click_vehicle_database()

    @pytest.mark.run(order=6)
    def test_add_no_car(self):
        self.car_adding_page.click_add_car()
        result = self.car_adding_page.verify_empty_car_field()
        time.sleep(3)
        assert result is False
        self.car_adding_page.click_cancel_car_adding()

    @pytest.mark.run(order=9)
    def test_fill_form_with_fake_data(self):
        self.car_adding_page.click_add_car()
        self.car_adding_page.fill_car_form_with_fake_address(self.fake_data.caption, self.fake_data.phone_number,
                                                             self.fake_data.capacity, self.fake_data.weight_limit,
                                                             self.fake_data.distance_limit,
                                                             self.fake_data.house_number, self.fake_data.postal_code,
                                                             self.fake_data.street, self.fake_data.city)
        result = self.car_adding_page.verify_car_adding()
        assert result is True

    @pytest.mark.run(order=8)
    @data(*test_data.login_data.get_csv_data("./test_data/address_data.csv"))
    @unpack
    def test_fill_form_with_real_address_data(self, house_number, postal_code, street, city):
        self.car_adding_page.click_add_car()
        time.sleep(1)
        self.car_adding_page.fill_car_form_with_real_address(self.fake_data.caption, self.fake_data.phone_number,
                                                             self.fake_data.capacity,
                                                             self.fake_data.weight_limit,
                                                             self.fake_data.distance_limit, house_number, postal_code,
                                                             street, city)

        result = self.car_adding_page.verify_car_adding()
        assert result is True

    @pytest.mark.run(order=7)
    def test_fill_form_without_required_fields(self):
        self.car_adding_page.click_add_car()
        self.car_adding_page.fill_car_form_without_required_fields(self.fake_data.phone_number,
                                                                   self.fake_data.capacity,
                                                                   self.fake_data.weight_limit,
                                                                   self.fake_data.distance_limit,
                                                                   self.fake_data.house_number,
                                                                   self.fake_data.postal_code,
                                                                   self.fake_data.street)

        result = self.car_adding_page.verify_form_without_required_fields()
        assert result is False
        time.sleep(2)
        self.car_adding_page.click_cancel_car_adding()

    @pytest.mark.run(order=10)
    def test_fill_only_required_fields(self):
        self.car_adding_page.click_add_car()
        self.car_adding_page.fill_only_required_fields(self.fake_data.caption, self.fake_data.city)
        time.sleep(1)
        result = self.car_adding_page.verify_car_adding()
        assert result is True
