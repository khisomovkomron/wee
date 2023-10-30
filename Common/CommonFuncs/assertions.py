import time
import re
from Common.CommonFuncs.webcommon import WebDriverFactory
from Common.CommonFuncs.waitings import Waiting
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementClickInterceptedException
from loguru import logger
import allure
import urllib.parse
from allure_commons.types import AttachmentType


class Assertions(WebDriverFactory):

    def asserting(self, expected, actual):
        logger.info(f'Asserting two variables: "{expected}" and "{actual}"')
        try:
            assert expected == actual, f"Incorrect information, Expected: {expected}, Actual: {actual}"
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def verify_page_title(self, page_title):
        """
        Verify page title
        @type page_title: str
        @param page_title: Expected title of the page
        """
        try:
            actual_title = self.get_page_title()
            assert actual_title == page_title, f'Page title is incorrect. Expected: {page_title}, Actual: {actual_title}'
            logger.success('Page title is correct')
            with allure.step('Page title is correct'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_displayed(self, **kwargs):
        """
        Check what element is displayed on page
        @param kwargs: WebElement or locator text & type
        """
        try:
            assert self.is_element_displayed(**kwargs), 'Element is not displayed'
            logger.success('Element is displayed')
            with allure.step('SUCCESS: Element is displayed'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_current_url(self, expected_url: str):
        """
        Function to get the current url and assert it is same as the expected url.
        """
        current_url = self.browser.current_url

        try:
            if not expected_url.startswith('http') or not expected_url.startswith('https'):
                expected_url = 'https://' + expected_url + '/'

            assert current_url == expected_url, f"The current url is not as expected. " \
                                                f"Actual: {current_url}, Expected: {expected_url}"

            logger.success("The page url is as expected.")
            with allure.step('SUCCESS: The page url is as expected.'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_url_contains(self, text: str):
        """
        Check that URL contains text
        """
        try:
            text = urllib.parse.quote_plus(text, safe=',=')
            Waiting(self.browser).wait_until_url_changes(text)
            WebDriverWait(self.browser, 10).until(EC.url_contains(text))
            current_url = self.browser.current_url
            assert text in current_url, f'Current url "{current_url}" does not contain text "{text}".'
            logger.success(f'Current url "{current_url}" contains expected text "{text}".')
            with allure.step(f'SUCCESS: Current url "{current_url}" contains expected text "{text}".'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_url_doesnt_contains(self, text):
        """
        Check that URL does not contain text
        """
        try:
            text = urllib.parse.quote_plus(text, safe=',=')
            current_url = self.browser.current_url
            assert text not in current_url, f'Current url "{current_url}" contains text "{text}".'
            logger.success(f'Current url "{current_url}" does not contains text "{text}".')
            with allure.step(f'SUCCESS: Current url "{current_url}" does not contains text "{text}".'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_url_ends_with(self, text):
        """
        Check that URL does not contain text
        """
        try:
            text = urllib.parse.quote_plus(text, safe=',=')
            current_url = self.browser.current_url
            assert current_url.endswith(text), f'Current url does not "{current_url}" ends with text "{text}".'
            logger.success(f'Assertion PASSED')
            with allure.step(f'SUCCESS: Assertion PASSED.'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_url_doesnt_contains_any_of(self, *text):
        """
        Check that URL does not contain text
        """
        try:
            current_url = self.browser.current_url
            for i in text:
                parsed_text = urllib.parse.quote_plus(i, safe=',=')
                assert parsed_text not in current_url, f'Current url "{current_url}" does not contain text "{text}".'
            logger.success(f'Current url "{current_url}" does not contains any of: {text}.')
            with allure.step(f'SUCCESS: Current url "{current_url}" does not contains any of:{text}.'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_visible(self, locator='', locator_type='css', element: WebElement = None):
        """
        Function to check if the passed in element is visible.
        Raises and exception if it is not exception.
        """
        if element:
            element = element
        else:
            element = self.browser.find_element(self.get_by_type(locator_type), locator)

        if not element.is_displayed():
            raise AssertionError('The element is not displayed')
        else:
            logger.success('Expected element is displayed')
            with allure.step('Expected element is displayed'):
                pass

    def assert_element_contains_text(self, expected_text, locator='', locator_type='xpath', case_sensitive=False,
                                     element: WebElement = None, is_input=False, element_name=None):

        if is_input:
            element_text = self.get_input_value(locator=locator, locator_type=locator_type, element=element)
        else:
            Waiting(self.browser).wait_until_visibility_of_element(locator_text=locator, locator_type=locator_type)
            element_text = self.get_element_text(locator=locator, locator_type=locator_type, element=element)

        try:
            if not case_sensitive:
                assert expected_text.lower() in element_text.lower(), f'Element does not contain text "{expected_text}".' \
                                                                      f'Current text is: "{element_text}"'
            else:
                assert expected_text in element_text, f'Element does not contain text "{expected_text}". Current text ' \
                                                      f'is: "{element_text}"'

            if element_name:
                locator = f'"{element_name}"'
            logger.success(f'Element {locator} contains text "{expected_text}".')
            with allure.step(f'Element {locator} contains text "{expected_text}".'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_text_length_is(self, length, locator='', locator_type='css', element: WebElement = None, is_input=False):

        if is_input:
            element_text = self.get_input_value(locator=locator, locator_type=locator_type, element=element)
        else:
            element_text = self.get_element_text(locator=locator, locator_type=locator_type, element=element)

        try:
            assert len(element_text) == length, f'Length of text in element is {len(element_text)}, ' \
                                                f'but {length} expected'
            logger.success(f'Length of element is {length}.')
            with allure.step(f'Length of element is {length}.'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_not_contains_any_text(self, locator='', locator_type='css', element: WebElement = None,
                                             is_input=False):

        if is_input:
            element_text = self.get_input_value(locator=locator, locator_type=locator_type, element=element)
        else:
            element_text = self.get_element_text(locator=locator, locator_type=locator_type, element=element)

        try:
            assert len(element_text) == 0, f'Element {locator} contains text "{element.text}"'
            logger.success(f'Element {locator} does not contain any text')
            with allure.step(f'Element {locator} does not contain any text'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_not_contains_text(self, expected_text, locator='', locator_type='css',
                                         element: WebElement = None, is_input=False):

        if is_input:
            element_text = self.get_input_value(locator=locator, locator_type=locator_type, element=element)
        else:
            element_text = self.get_element_text(locator=locator, locator_type=locator_type, element=element)

        try:
            assert expected_text not in element_text, f'Element {locator} contains text "{element.text}"'
            logger.success(f'Element {locator} does not contain text "{expected_text}"')
            with allure.step(f'Element {locator} does not contain text "{expected_text}"'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_contains_any_text(self, locator='', locator_type='css',  element: WebElement = None,
                                         is_input=False):
        try:
            if is_input:
                element_text = self.get_input_value(locator=locator, locator_type=locator_type, element=element)
            else:
                element_text = self.get_element_text(locator=locator, locator_type=locator_type, element=element)

            assert len(element_text) >= 1, f"Element does not contain any text"
            logger.success('Element is visible and contains some text')
            with allure.step('Element is visible and contains some text'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_not_exists(self, locator='', locator_type='css', element: WebElement = None):
        try:
            if isinstance(self, WebElement):
                element = element
            else:
                element = self.get_element(locator, locator_type)
            if element:
                raise Exception("Element should not be found")
            else:
                logger.success('Element does not exist on current page')
                with allure.step('Element does not exist on current page'):
                    pass
        except:
            raise AssertionError

    def assert_element_exists(self, locator='', locator_type='css', element: WebElement = None):
        try:
            if element:
                element = [].append(element)
            else:
                element = self.get_elements(locator, locator_type)
            if len(element) < 1 or not element:
                raise Exception("Element not found")
            else:
                logger.success('Element is exists on current page')
                with allure.step('Element is exists on current page'):
                    pass
            return True
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_is_not_visible(self, locator='', locator_type='css'):
        by_type = self.get_by_type(locator_type)
        try:
            Waiting(self.browser).wait_until_invisibility_of_element(locator_type=locator_type, locator=locator)
            assert len(self.browser.find_elements(by_type, locator)) < 1, \
                "Element is present on page"
            logger.success(f'Element "{locator}" is not present on page')
            with allure.step(f'Element "{locator}" is not present on page'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_is_visible(self, locator='', locator_type='css'):
        by_type = self.get_by_type(locator_type)
        try:
            assert WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((by_type, locator))), \
                "Element is not present on page"
            logger.success(f'Element "{locator}" is present on page')
            with allure.step(f'Element "{locator}" is present on page'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_is_not_clickable(self, locator='', locator_type='css', element: WebElement = None):
        if element:
            element = element
        else:
            element = self.get_element(locator, locator_type)
        try:
            element.click()
        except ElementClickInterceptedException:
            logger.success(f'Element "{locator}" is not clickable')
            with allure.step(f'Element "{locator}" is not clickable'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_is_clickable(self, locator='', locator_type='css', element: WebElement = None):
        if element:
            element = element
        else:
            element = self.get_element(locator, locator_type)
        try:
            assert element.is_enabled(), "Element is not clickable"
            logger.success(f'Element "{locator}" is clickable')
            with allure.step(f'Element "{locator}" is clickable'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_is_not_displayed(self, locator='', locator_type='css', element: WebElement = None):
        if element:
            element = element
        else:
            element = self.get_element(locator, locator_type)
        try:
            Waiting(self.browser).wait_until_invisibility_of_element(locator_type=locator_type, locator=locator)
            assert not element.is_displayed(), "Element is displayed on page"
            logger.success(f"Element {locator} is not displayed on page")
            with allure.step(f'Element "{locator}" is not displayed on page'):
                pass
        except AttributeError:
            logger.success(f"Element {locator} is not displayed on page")
            with allure.step(f'Element "{locator}" is not displayed on page'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_is_selected(self, locator='', locator_type='css', element: WebElement = None):
        if isinstance(self, WebElement):
            element = element
        else:
            element = self.get_element(locator, locator_type)
        try:
            Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
            assert element.is_selected(), "Element is not selected"
            logger.success(f"Element {locator} is selected")
            with allure.step(f'Element "{locator}" is selected'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_element_is_not_selected(self, locator='', locator_type='css', element: WebElement = None):
        if element:
            element = element
        else:
            element = self.get_element(locator, locator_type)
        try:
            Waiting(self.browser).wait_until_visibility_of_element(locator_type=locator_type, locator_text=locator)
            assert not element.is_selected(), "Element is selected"
            logger.success(f"Element {locator} is not selected")
            with allure.step(f'Element "{locator}" is not selected'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_attribute_has_value(self, property_name, value, locator='', locator_type='css',
                                   element: WebElement = None):
        if element:
            element = element
        else:
            element = self.get_element(locator, locator_type)
        try:
            val = element.get_attribute(property_name.lower())
            assert val == value, f"Property of element with name {property_name} has value {val}"
            logger.success(f'Property of element with name "{property_name}" has correct value: {val}')
            with allure.step(f'Property of element with name "{property_name}" has correct value: {val}'):
                pass
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def assert_attribute_has_css_property(self, property_name, value, locator='', locator_type='css',
                                          element: WebElement = None, is_message=True):
        if element:
            element = element
        else:
            element = self.get_element(locator, locator_type)
        try:
            val = element.value_of_css_property(property_name.lower())
            assert val == value, f"Property of element with name {property_name} has value {val}"
            with allure.step(f'Property of element with name "{property_name}" has correct value: {val}'):
                pass
        except AssertionError as e:
            logger.error(e)
            raise Exception(e)
        if is_message:
            logger.success(f'Property of element with name {property_name} has correct value')


class ApiAssertions:
    def __init__(self, json):
        self.json = json

    def assert_value_of_attribute_equals(self, attribute, value, path=None):
        if path:
            self.json = self.json[path]
        assert self.json[attribute] == value, f'Value does not equal "{value}". Actual result: "{self.json[attribute]}"'
        logger.success(f'Assertion PASSED. Value of attribute "{attribute}" is "{value}"')
        with allure.step(f'Assertion PASSED. Value of attribute "{attribute}" is "{value}"'):
            pass

    @staticmethod
    def assert_value_equals(value, exp_value, check_message=None):
        assert exp_value == value, f'Value does not equal "{exp_value}". Actual result: "{value}"'
        if not check_message:
            logger.success(f'Assertion PASSED. Response contains expected value: "{exp_value}"')
        else:
            logger.success(check_message)
        with allure.step(f'Assertion PASSED. Response contains expected value: "{exp_value}"'):
            pass

    @staticmethod
    def assert_values_are_not_equal(value, exp_value, check_message=None):
        assert exp_value != value, 'Values are equal.'
        if not check_message:
            logger.success(f'Assertion PASSED. Values are not equal.')
        else:
            logger.success(check_message)
        with allure.step(f'Assertion PASSED. Values are not equal.'):
            pass

    def assert_value_of_attribute_contains_text(self, attribute, text):
        self.assert_attribute_exists_in_response(attribute)
        assert text in self.json[
            attribute], f'Value does not contains "{text}". Actual result: "{self.json[attribute]}"'
        logger.success(f'Assertion PASSED. Attribute "{attribute}" contains text "{text}"')
        with allure.step(f'Assertion PASSED. Attribute "{attribute}" contains text "{text}"'):
            pass

    def assert_attribute_exists_in_response(self, *attribute, path=None):
        if path:
            for i in range(len(attribute)):
                assert path[attribute[i]], f"There is no attribute named \"{attribute}\" in response. " \
                                           f"{logger.error('Assertion FAILED')}"
                logger.success(f'Assertion PASSED. Attribute named "{attribute[i]}" exists in response')
        else:
            try:
                for i in range(len(attribute)):
                    if self.json[attribute[i]] is None:
                        assert self.json[attribute[i]] is None, f"There is no attribute named \"{attribute}\" in response. " \
                                                    f"{logger.error('Assertion FAILED')}"
                        logger.success(f'Assertion PASSED. Attribute named "{attribute[i]}" exists in response')

                    else:
                        assert self.json[attribute[i]], f"There is no attribute named \"{attribute}\" in response. " \
                                                    f"{logger.error('Assertion FAILED')}"
                        logger.success(f'Assertion PASSED. Attribute named "{attribute[i]}" exists in response')
            except KeyError as e:
                logger.error(e)
                raise AssertionError(f"There is no attribute named \"{attribute}\" in response")

    def assert_attribute_does_exists_in_response(self, attribute):
        try:
            assert not self.json[attribute], f"There is attribute named \"{attribute}\" in response"
            logger.success('Assertion PASSED')
        except KeyError:
            raise AssertionError(f"There is attribute named \"{attribute}\" in response")

    def assert_value_type_is(self, *attribute, value_type, path=None):
        for i in range(len(attribute)):
            if path:
                val = path[attribute[i]]
                self.assert_attribute_exists_in_response(attribute[i], path=path)
            else:
                val = self.json[attribute[i]]
                self.assert_attribute_exists_in_response(attribute[i])
            assert isinstance(val, value_type), f'Type of "{val}" is {type(val)}'
            logger.success(f'Assertion PASSED. Type of {attribute[i]} is {value_type}')

    def assert_attribute_contains_child_elements(self, attribute):
        self.assert_attribute_exists_in_response(attribute)
        assert len(self.json[attribute]) > 0, f'Element "{attribute}" does not contains child elements. ' \
                                              f'{logger.error("Assertion FAILED")}'
        logger.success('Assertion PASSED')

    def assert_response_does_not_contains(self, keyword):
        clean_json = re.sub(r'[{}\[\]:]', '', str(self.json))
        assert keyword not in clean_json, f'JSON contains "{keyword}". {logger.error("Assertion FAILED")}'
        logger.success('Assertion PASSED')

    @staticmethod
    def assert_value_contains_in_response(expected_value, response):
        assert expected_value in response, f'There is no these value: "{expected_value}" in response'
        logger.success(f'Assertion PASSED. "{expected_value}" contains in response')

    @staticmethod
    def assert_value_not_contains_in_response(expected_value, response):
        assert expected_value not in response, f'There is no logistic margin with id {expected_value} in response'
        logger.success('Assertion PASSED')

    @staticmethod
    def assert_length_of_param_is_equals(length, param):
        assert len(param) == int(length), f'Length of parameter = {len(param)} but {length} expected'
        logger.success('Assertion PASSED')
