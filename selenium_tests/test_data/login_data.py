from faker import Faker
from faker.providers import DynamicProvider
import csv
import codecs


def get_csv_data(filename):
    rows = []
    data_file = codecs.open(filename, "r", "utf-8")
    reader = csv.reader(data_file)

    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows


class FakeData():
    def __init__(self):
        fake = Faker("pl_PL")
        self.email = fake.email()
        self.password = fake.password()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        # self.registration_gender = random.choice([Gender.FEMALE, Gender.MALE])
        data = fake.date_of_birth()
        self.day_of_birth = str(data.day)
        self.month_of_birth = str(data.month)
        self.year_of_birth = str(data.year)
        self.caption = fake.license_plate()
        self.phone_number = fake.phone_number()
        self.house_number = fake.building_number()
        self.postal_code = fake.postalcode()
        self.street = fake.street_name()
        self.city = fake.city()
        self.capacity = fake.port_number()
        self.weight_limit = fake.port_number()
        self.distance_limit = fake.port_number()


class AddDynamicProvider():
    def __init__(self):
        fake = Faker()

    @staticmethod
    def car_type():
        car_names = DynamicProvider("car_name", ["AUDI", "AlfaRomeo", "BMW", "Citroen", "Doge", "Fiat", "Ford", "Honda",
                                                 "Kia", "Łada", "Mustang", "Nissan", "Opel", "Porsche", "RangeRover",
                                                 "Skoda", "Toyota", "VW"])
