from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import urllib.parse
from loguru import logger
import allure


class Waiting:

    def __init__(self, browser):
        self.browser = browser

    @staticmethod
    def get_by_type(locator_type):
        """Returns locator type in right form """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        if locator_type == "name":
            return By.NAME
        if locator_type == "xpath":
            return By.XPATH
        if locator_type == "css":
            return By.CSS_SELECTOR
        if locator_type == "class":
            return By.CLASS_NAME
        if locator_type == "link":
            return By.LINK_TEXT
        else:
            logger.info(f"Locator type {locator_type}  not correct/supported")
        return False

    def implicit_wait(self, timeout=10):
        wait = WebDriverWait(self.browser, timeout=timeout)

    def explicit_wait(self, locator_type='xpath', locator_text='', timeout=10, element: WebElement = None):
        try:
            if element:
                WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable(element))
                logger.info(f"Element is clickable")
            else:
                wait = WebDriverWait(self.browser, timeout=timeout)
                element = wait.until(EC.element_to_be_clickable((self.get_by_type(locator_type), locator_text)))
                #logger.info(f"Element {locator_text} is clickable")
            return element
        except:
            logger.info(f"Element is not clickable")

    def wait_until_invisibility_of_element(self, locator_type='xpath', locator='', timeout=5, poll_frequency=0.5):
        try:
            wait = WebDriverWait(self.browser, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = self.browser.find_element(self.get_by_type(locator_type), locator)
            wait.until(EC.invisibility_of_element(element))
            with allure.step(f"Element: {locator} invisible on the web page"):
                pass
        except:
            with allure.step(f"ERROR: Element: {locator} not invisible on the web page"):
                pass
            logger.info(f"Element: {locator} not invisible on the web page")

    def wait_until_visibility_of_element(self, locator_text, locator_type='xpath', timeout=5, poll_frequency=1):
        element = None
        try:
            locator_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.browser, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((locator_type, locator_text)))
            with allure.step(f"Element: {locator_text} visible on the web page"):
                pass
        except:
            logger.info(f"Element: {locator_text} not visible on the web page")
            with allure.step(f"ERROR: Element: {locator_text} invisible on the web page"):
                pass
        return element

    def wait_until_text_to_be_present_in_element(self, text, locator_text, locator_type='xpath', timeout=5,
                                                 poll_frequency=0.5, is_input=False):
        element = None
        try:
            locator_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.browser, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            if is_input:
                element = wait.until(EC.text_to_be_present_in_element_value((locator_type, locator_text), text))
            else:
                element = wait.until(EC.text_to_be_present_in_element((locator_type, locator_text), text))
            with allure.step(f"Text of element {locator_text} is visible on the web page"):
                pass
        except:
            logger.info(f"Text of element {locator_text} is not visible on the web page")
            with allure.step(f"ERROR: Text of element {locator_text} is not visible on the web page"):
                pass
        return element

    def wait_until_url_changes(self, expected_url, timeout=5, poll_frequency=0.5):
        try:
            wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=poll_frequency)
            wait.until(EC.url_changes(urllib.parse.quote_plus(expected_url, safe=',=')))
            with allure.step(f"URL was changed to {expected_url}"):
                pass
        except:
            logger.info(f"URL wasn't changed to {expected_url}")
            with allure.step(f"URL wasn't changed to {expected_url}"):
                pass

