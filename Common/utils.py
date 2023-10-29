import logging as logger
import random
import string
import time
import traceback
from datetime import date, timedelta


class Util(object):

    def sleep(self, sec, info=""):

        if info is not None:
            logger.info("Wain :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type_let='letters'):

        alpha_num = ''
        if type_let == 'lower':
            case = string.ascii_lowercase
        elif type_let == 'upper':
            case = string.ascii_uppercase
        elif type_let == 'digits':
            case = string.digits
        elif type_let == 'mix':
            case = string.ascii_lowercase + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, itemLength=10):
        namelist = []
        for i in range(0, itemLength):
            namelist.append(self.getUniqueName(itemLength[i]))
        return namelist

    def verify_text_contains(self, actualText, expectedText):

        logger.info("Actual Text from application Web UI --> :: " + actualText)
        logger.info("Expected  Text from application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            logger.info("$$$ VERIFICATION CONTAIN !!!")
            return True
        else:
            logger.info('$$$ VERIFICATION DOES NOT CONTAIN!!!')
            return False

    def verifyTextMatch(self, actualText, expectedText):

        logger.info("Actual Text from application Web UI --> :: " + actualText)
        logger.info("Expected  Text from application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            logger.info("$$$ VERIFICATION MATCHED !!!")
            return True
        else:
            logger.info("$$$ VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):

        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True

    def generate_random_email_and_password(self, domain=None, email_prefix=None, ):
        logger.debug("Generating random email and password")

        if not domain:
            domain = 'threek.com'
        if not email_prefix:
            email_prefix = 'testuser'

        random_email_string_length = 10
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
        email = email_prefix + '_' + random_string + '@' + domain

        password_length = 20
        password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

        random_info = {'email': email, 'password': password_string}
        logger.debug(f"Randomly generated email and password: {random_info}")

        return random_info

    @staticmethod
    def generate_random_string(length=10, prefix=None, suffix=None):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
        if prefix:
            random_string = prefix + random_string
        if suffix:
            random_string = random_string + suffix

        return random_string

    @staticmethod
    def generate_random_coupon_code(sufix=None, lenght=10):
        code = ''.join(random.choices(string.ascii_uppercase, k=lenght))
        if sufix:
            code = code + sufix
        return code

    @staticmethod
    def generate_random_margin():
        return round(random.randint(1, 100) + random.random(), 2)

    @staticmethod
    def today_iso_format():
        return date.today().isoformat()

    @staticmethod
    def after_one_month_iso_format():
        return (date.today() + timedelta(days=30)).isoformat()

    def generate_random_number_from_given_data(self, data):
        return round(random.randint(1, len(data)-1))


