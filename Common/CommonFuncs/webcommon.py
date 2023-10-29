from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from Common.urls import URL_CONFIG
from Common.CommonFuncs.waitings import Waiting
from Common.utils import Util
from loguru import logger
import allure
import os
import random
import os.path
from selenium.webdriver.common.action_chains import ActionChains


class WebDriverFactory:

    RANDOM_NAME = Util.generate_random_string()
    RANDOM_PRIORITY = f'{random.randint(0, 100)}'
    RANDOM_COMMENT = f'auto_comment_{random.randint(100, 10000)}'

    @classmethod
    def set_random_name(cls, length=10):
        cls.RANDOM_NAME = Util().generate_random_string(length)
        return cls.RANDOM_NAME

    @classmethod
    def set_random_priority(cls):
        cls.RANDOM_PRIORITY = f'{random.randint(0, 100)}'
        return cls.RANDOM_PRIORITY

    @classmethod
    def set_random_comment(cls):
        cls.RANDOM_COMMENT = f'auto_comment_{random.randint(100, 10000)}'
        return cls.RANDOM_COMMENT

    def __init__(self, browser, stand, timeout=10):
        self.browser = browser
        self.stand = stand
        self.browser.implicitly_wait(timeout)

    def open(self, page):
        base_url = URL_CONFIG.get('base_url')
        if URL_CONFIG.get(page):
            page = URL_CONFIG.get(page)
        else:
            page = page
        try:
            if self.stand == 'dev_wee':
                self.browser.get(f'{base_url}{page}')
                logger.info(f'Opened page with URL: {base_url}{page}')
            elif self.stand == 'prod_wee':
                self.browser.get(f'{URL_CONFIG.get("base_wee_url")}{page}')
                logger.info(f'Opened page with URL: {URL_CONFIG.get("base_wee_url")}{page}')
            else:
                self.browser.get(f'{base_url}{page}')



        except Exception as e:
            logger.error(f'ERROR: {e}. Can\'t initiate browser instance')
            raise Exception

    @staticmethod
    def locator_by_name(source, name):
        return source[name]['locator']

    @staticmethod
    def locators_by_names(source, *name):
        if len(name) > 1:
            return [WebDriverFactory.locator_by_name(source=source, name=i) for i in name]
        else:
            for i in name:
                return WebDriverFactory.locator_by_name(source=source, name=i)

    def get_url(self):
        return self.browser.current_url

    def quit(self):
        self.browser.quit()

    def is_element_displayed(self, locator='', locator_type='css', element: WebElement = None):
        """Checks if element is visible and returns True or False
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        if element:
            Waiting(self.browser).wait_until_visibility_of_element(locator_text=locator, locator_type=locator_type,
                                                                   timeout=10)
            element = element
        else:
            Waiting(self.browser).wait_until_visibility_of_element(locator_text=locator, locator_type=locator_type,
                                                                   timeout=10)
            element = self.get_element(locator, locator_type)

        if element.is_displayed():
            return True
        else:
            return False

    def send_file(self, path, locator='', locator_type='css', element: WebElement = None):
        """ Sending file by file PATH
        @param path: PATH of file to sending
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        if element:
            input_filed = element
        else:
            Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
            input_filed = self.get_element(locator, locator_type)

        input_filed.send_keys(f'{os.path.normpath(os.getcwd()+path)}')

    def click(self, locator='', locator_type='css', element: WebElement = None):
        """ Can click by locator & type or by WebElement
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - CSS)
        @param element: WebElement
        """
        if element:
            Waiting(self.browser).explicit_wait(element=element)
            element = element
        else:
            Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
            Waiting(self.browser).explicit_wait(locator_type=locator_type, locator_text=locator)
            element = self.get_element(locator, locator_type)

        element.click()
        logger.info(f'Clicked at element {locator}')
        with allure.step(f'Clicked at element {locator}'):
            pass

    def get_element_text(self, locator='', locator_type='css', element: WebElement = None):
        """ Returns element's text by locator & type or by WebElement
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        if element:
            element = element
        else:
            Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
            element = self.get_element(locator, locator_type)
        element_text = element.text

        return element_text

    def get_input_value(self, locator='', locator_type='css', element: WebElement = None):
        """ Returns input's value by locator & type or by WebElement
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        if element:
            element = element
        else:
            Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
            element = self.get_element(locator, locator_type)
        element_text = element.get_attribute('value')

        return element_text

    def is_element_present(self, locator, locator_type='css'):
        """This method checks that element is exists in DOM
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - css)"""
        try:
            element = self.get_element(locator, locator_type)
        except NoSuchElementException:
            return False
        return True if element else False

    def get_element_href(self, locator='', locator_type='css', element: WebElement = None):
        """ Returns element's attribute href by locator & type or by WebElement
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        if element:
            element = element
        else:
            element = self.get_element(locator, locator_type)

        element_href = element.get_attribute('href')

        return element_href

    def move_to_element(self, locator='', locator_type='css', element: WebElement = None):
        """ Move to element method
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - CSS)
        @param element: WebElement
        """
        actions = ActionChains(self.browser)
        if element:
            element = element
        else:
            element = self.get_element(locator=locator, locator_type=locator_type)

        actions.move_to_element(element).perform()

    def execute_script_click(self, locator='', locator_type='css', element: WebElement = None):
        """This method is executed JS-script that clicked on element
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        if element:
            element = element
        else:
            Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
            element = self.get_element(locator, locator_type)

        self.browser.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, locator='', locator_type='css', element: WebElement = None):
        """This method is executed JS-script that scrolls page into view of element
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        if element:
            element = element
        else:
            Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
            element = self.get_element(locator, locator_type)

        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def close_alert(self):
        alert = self.browser.switch_to.alert
        alert.dismiss()

    def get_element_attribute(self, attr_name: str, locator='', locator_type='css', element: WebElement = None):
        """This method is executed JS-script that scrolls page into view of element
        @param attr_name: Name of attribute that you want to know (e.g. name, value, color, etc.)
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        if element:
            element = element
        else:
            Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
            element = self.get_element(locator, locator_type)

        element_attr = element.get_attribute(attr_name)

        return element_attr

    def get_title(self):
        """ Returns title of page """
        return self.browser.title

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
            logger.info(f"Locator type {locator_type} not correct/supported")
        return False

    def get_element(self, locator: str, locator_type="css"):
        """Returns WebElement by locator text & locator type
        @param locator: text of locator
        @param locator_type: id/name/xpath/css/class/link"""
        element = None
        try:
            Waiting(self.browser).wait_until_visibility_of_element(locator_text=locator, locator_type=locator_type)
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.browser.find_element(by_type, locator)
            logger.info(f"Element found with locator: {locator} and locator_type: {locator_type}")
            with allure.step(f"Element found with locator: {locator} and locator_type: {locator_type}"):
                pass
        except:
            logger.info(f"Element not found. Locator {locator}. Type:{locator_type}")
        return element

    def get_elements(self, locator: str, locator_type="css"):
        """Returns WebElement by locator text & locator type
        @param locator: text of locator
        @param locator_type: id/name/xpath/css/class/link"""
        element = None
        try:
            Waiting(self.browser).wait_until_visibility_of_element(locator_text=locator, locator_type=locator_type)
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.browser.find_elements(by_type, locator)
            logger.info(f"Elements found with locator: {locator} and locator_type: {locator_type}")
            with allure.step(f"Elements found with locator: {locator} and locator_type: {locator_type}"):
                pass
        except:
            logger.info(f"Elements not found. Locator {locator}. Type:{locator_type}")
        return element

    def send_keys(self, data: str, locator='', locator_type='css', element: WebElement = None):
        """ You can send text to founded element or send it by locator data (e.g. locator + locator type)
        @param data: Text you want to send in element
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        try:
            if element:
                element = element
            else:
                Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
                element = self.get_element(locator, locator_type)
                logger.info(f"Sending data to element with locator: {locator} locator_type: {locator_type}")

            element.clear()
            element.send_keys(data)
            logger.info(f"Sent data on element with locator: {locator} and locator_type: {locator_type}")
            with allure.step(f"Sent data on element with locator: {locator} and locator_type: {locator_type}"):
                pass
        except Exception as e:
            logger.error(f"ERROR: {e}. Can\'t send data on element with locator: {locator} and "
                         f"locator_type: {locator_type}")
            raise Exception

    def clear_field(self, locator='', locator_type='css', element: WebElement = None):
        """ Cleaning field founded by locator text &
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        try:
            if element:
                element = element
            else:
                Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
                element = self.get_element(locator, locator_type)
            element.clear()
            logger.info(f"Clear field with locator: {locator} & locator_type {locator_type}")
            with allure.step(f"Clear field with locator: {locator} & locator_type {locator_type}"):
                pass
        except Exception as e:
            logger.error(f"ERROR: {e}. Can\'t clear field with locator: {locator} and locator_type: {locator_type}")
            raise Exception

    def get_text(self, locator='', locator_type='css', element: WebElement = None):
        """ Returns text of element
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - XPATH)
        @param element: WebElement
        """
        try:
            if element:
                element = element
            else:
                Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
                element = self.get_element(locator, locator_type)
            text = element.text
            return text
        except Exception as e:
            logger.error(f"ERROR: {e}. Can\'t get text from field with locator: {locator} and "
                         f"locator_type: {locator_type}")
            raise Exception

    def element_presence_check(self, locator, locator_type='css'):
        Waiting(self.browser).wait_until_visibility_of_element(locator, locator_type)
        element_list = self.get_elements(locator, locator_type)
        if len(element_list) > 0:
            logger.info("Element present with locator:" + locator
                        + " locator_Type" + str(locator_type))
            return True
        else:
            logger.info("Element not present with locator:" + locator +
                        " locator_Type: " + str(locator_type))
            return False

    def web_scroll(self, direction="up", scroll_by=None):
        """ Page scrolls by direction
        @type direction: str - up or down
        @type scroll_by: int - value of pixels to scroll """

        if scroll_by and direction == 'up':
            self.browser.execute_script(f'window.scrollTo(0, -{scroll_by})')
        elif scroll_by and direction == 'down':
            self.browser.execute_script(f'window.scrollTo(0, {scroll_by})')
        elif direction == 'up' and not scroll_by:
            self.browser.execute_script('window.scrollTo(0, -1000);')
        else:
            self.browser.execute_script('window.scrollTo(0, 1000);')

    def switch_to_alert(self):
        """Switching to alert"""
        return self.browser.switch_to.alert

    def switch_to_active_element(self):
        """Switching to alert"""
        return self.browser.switch_to.active_element

    def switch_to_iframe(self, locator='', locator_type='css', element: WebElement = None):
        """ Switching to iframe
        @param locator: Locator of element in the page
        @param locator_type: Type of the locator on page (by default - css)
        @param element: WebElement
        """
        try:
            if isinstance(self, WebElement):
                element = element
            else:
                element = self.get_element(locator, locator_type)

            return self.browser.switch_to.frame(element)
        except Exception as e:
            logger.error(f'Error message: {e}')
            raise Exception

    def get_page_title(self):
        """Getting the page title"""
        return self.browser.title

    def refresh(self):
        """Getting the page title"""
        return self.browser.refresh()
