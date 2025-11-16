from base.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import logging
import utilities.custom_logger as cl


class AddCar(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    """
    Locators
    
    """

    _vehicle_database_ = "//div[@class='navigation-items']/button[3]"
    _add_car_ = "//button[contains(@class,'mat-flat-button')]/span[text()=' Dodaj pojazd ']"
    _submit_car_button_ = "custom-form-submit-button"
    _caption_ = "input-caption"
    _phone_number_ = "input-phoneNumber"
    _street_ = "input-street"
    _house_number_ = "input-houseNumber"
    _postal_code_ = "input-postcode"
    _city_ = "input-city"
    _capacity_ = "input-capacity"
    _weight_limit_ = "input-weightLimit"
    _distance_limit_ = "input-distanceLimit"
    _get_car_colour_ = "//input[@class='custom-input-field-color ng-untouched ng-pristine ng-valid']"
    _slider_ = "//div[@class='hue']//div[@class='cursor']"
    _slider02_ = "//div[@class='saturation-lightness ng-star-inserted']//div[@class='cursor']"
    _access_time_ = (
        "//div[@class='custom-form-dialog custom-box-form-dialog form-dialog-boxes ng-star-inserted']//button[@class='mat-icon-button mat-primary']")
    _access_hours_ = "//div[@class='hours']/div[@class='option ng-star-inserted']"
    _access_minutes_ = "//div[@class='minutes']/div[@class='option ng-star-inserted']"
    _vehicle_added_successfully_ = "//span[contains(text(),'Pomyślnie dodano pojazd')]"
    _cancel_car_add_ = "//div[@class='custom-form-dialog custom-box-form-dialog form-dialog-boxes ng-star-inserted']//a[text()='Anuluj']"
    _confirm_car_cancel_ = "//div[@class='button-row mat-dialog-actions ng-star-inserted']//button[text()='Tak']"

    def click_vehicle_database(self):
        time.sleep(1)
        car = (WebDriverWait(self.driver, 10, 1).until(
            EC.visibility_of_element_located((By.XPATH, self._vehicle_database_))).click())

    def click_add_car(self):
        car = (WebDriverWait(self.driver, 10).until
               (EC.visibility_of_element_located((By.XPATH, self._add_car_))).click())

    def get_submit_car_button(self):
        button = self.get_element(self._submit_car_button_)
        return button

    def get_vehicle_form(self):
        self.click_vehicle_database()
        self.click_add_car()

    def send_keys_to_caption(self, caption):
        self.send_keys_to_element(caption, self._caption_)

    def send_keys_to_phone_number(self, phone_number):
        self.send_keys_to_element(phone_number, self._phone_number_)

    def send_keys_to_street(self, street):
        self.send_keys_to_element(street, self._street_)

    def send_keys_to_house_number(self, house_number):
        self.send_keys_to_element(house_number, self._house_number_)

    def send_keys_to_postal_code(self, postal_code):
        self.send_keys_to_element(postal_code, self._postal_code_)

    def send_keys_to_city(self, city):
        self.send_keys_to_element(city, self._city_)

    def send_keys_to_capacity(self, capacity):
        self.send_keys_to_element(capacity, self._capacity_)

    def send_keys_to_weight_limit(self, weight_limit):
        self.send_keys_to_element(weight_limit, self._weight_limit_)

    def send_keys_to_distance_limit(self, distance_limit):
        self.send_keys_to_element(distance_limit, self._distance_limit_)

    def click_cancel_car_adding(self):
        self.get_element(self._cancel_car_add_, By.XPATH).click()
        time.sleep(1)
        self.get_element(self._confirm_car_cancel_, By.XPATH).click()

    def cancel_car_adding(self):
        button = self.get_submit_car_button()
        result = button.is_enabled()
        if not result:
            self.click_cancel_car_adding()

    def get_address_data(self, house_number, postal_code, street, city):
        self.send_keys_to_house_number(house_number)
        self.send_keys_to_postal_code(postal_code)
        self.send_keys_to_street(street)
        self.send_keys_to_city(city)

    def start_working_time(self):
        buttons = self.driver.find_elements(By.XPATH, self._access_time_)
        buttons[0].click()
        hours = self.driver.find_elements(By.XPATH, self._access_hours_)
        random.choice(hours).click()
        minutes = self.driver.find_elements(By.XPATH, self._access_minutes_)
        random.choice(minutes).click()

    def end_working_time(self):
        buttons = self.driver.find_elements(By.XPATH, self._access_time_)
        buttons[1].click()
        time.sleep(1)
        hours = self.driver.find_elements(By.XPATH, self._access_hours_)
        random.choice(hours).click()
        minutes = self.driver.find_elements(By.XPATH, self._access_minutes_)
        random.choice(minutes).click()

    def choose_car_colour(self):
        self.click_on_element(self._get_car_colour_, By.XPATH)
        slider = self.get_element(self._slider_, By.XPATH)
        actions = ActionChains(self.driver)
        a = list(range(1, 200))
        position = random.choice(a)   #random.randint(1,200)
        actions.drag_and_drop_by_offset(slider, xoffset=position, yoffset=0).perform()

        slider02 = self.get_element(self._slider02_, By.XPATH)
        actions.drag_and_drop_by_offset(slider02, xoffset=position, yoffset=position).perform()
        self.driver.find_element(By.XPATH, "//div[@class='custom-form-dialog-title']").click()

    def verify_empty_car_field(self):
        # self.click_add_car()
        button = self.get_submit_car_button()
        result = button.is_enabled()
        print(result)
        return result

    def verify_form_without_required_fields(self):
        button = self.get_submit_car_button()
        result = button.is_enabled()
        print(result)
        return result

    def fill_inputs_with_id(self, caption, phone_number, capacity, weight_limit, distance_limit):
        self.send_keys_to_caption(caption)
        self.send_keys_to_phone_number(phone_number)
        self.send_keys_to_capacity(capacity)
        self.send_keys_to_weight_limit(weight_limit)
        self.send_keys_to_distance_limit(distance_limit)

    def fill_car_form_with_fake_address(self, caption, phone_number, capacity, weight_limit, distance_limit, house_number,
                                   postal_code, street, city):
        self.fill_inputs_with_id(caption, phone_number, capacity, weight_limit, distance_limit)
        self.get_address_data(house_number, postal_code, street, city)
        self.choose_car_colour()
        self.start_working_time()
        self.end_working_time()
        self.get_submit_car_button().click()

    def verify_car_adding(self):
        successful = WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element((By.XPATH, self._vehicle_added_successfully_),
                                             "Pomyślnie dodano pojazd"))
        if successful:
            return True

    def fill_car_form_with_real_address(self, caption, phone_number, capacity, weight_limit, distance_limit, house_number,
                                   postal_code, street, city):
        self.fill_inputs_with_id(caption, phone_number, capacity, weight_limit, distance_limit)
        self.get_address_data(house_number, postal_code, street, city)
        self.choose_car_colour()
        self.start_working_time()
        time.sleep(1)
        self.end_working_time()
        # time.sleep(1)
        self.get_submit_car_button().click()

    def fill_car_form_without_required_fields(self, phone_number, capacity, weight_limit, distance_limit, house_number,
                                              postal_code, street):
        self.send_keys_to_phone_number(phone_number)
        self.send_keys_to_capacity(capacity)
        self.send_keys_to_weight_limit(weight_limit)
        self.send_keys_to_distance_limit(distance_limit)
        self.send_keys_to_house_number(house_number)
        self.send_keys_to_postal_code(postal_code)
        self.send_keys_to_street(street)
        self.choose_car_colour()

    def fill_only_required_fields(self, caption, city):
        self.send_keys_to_caption(caption)
        self.send_keys_to_city(city)
        self.start_working_time()
        self.end_working_time()
        self.get_submit_car_button().click()
