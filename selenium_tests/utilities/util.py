import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging


class Util(object):
    log = cl.custom_logger(logging.INFO)

    def get_alpha_numeric(self, length, type='letters'):
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, charCount=10):
        return self.get_alpha_numeric(charCount, 'lower')

    def get_unique_name_list(self, list_size=5, item_length=None):
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_inique_name(item_length[i]))
        return name_list

    def verify_text_contains(self, actual_text, expected_text):
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verify_text_match(self, actual_text, expected_text):
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verify_list_match(self, expected_list, actual_list):
        return set(expected_list) == set(actual_list)

    def verify_list_contains(self, expected_list, actual_list):
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
        else:
            return True

