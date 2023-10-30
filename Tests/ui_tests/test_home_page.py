import time

from Pages.PageObjects.ui_pages.HomePage import HomePage
from Common.CommonFuncs.assertions import Assertions
from Common.CommonFuncs.waitings import Waiting
import allure


class TestTable:

    def test_1(self, browser):
        page = HomePage(browser)
        assertion = Assertions(browser)
        page.open()
        Waiting(browser).explicit_wait(locator_text=page.PROFILE)
        page.click(locator=page.PROFILE)
        page.click(locator=page.CODE_BUTTON)
        page.click(locator=page.RUS_CODE)
        page.send_keys('9771858108',locator=page.CODE_INPUT)
        page.click(locator=page.LOG_IN_BUTTON)
        browser.implicitly_wait(time_to_wait=10)
        time.sleep(5)
        page.assert_profile_name()


    # def test_2(self, browser, stand):
    #     page = HomePage(browser, stand)
    #     assertion = Assertions(browser, stand)
    #     page.open(page='action_log')
    #     page.move_to_element(locator=page.FIRST_ROW)
    #     assertion.assert_attribute_has_css_property('background-color', 'rgba(244, 248, 255, 1)',
    #                                                 locator=page.FIRST_ROW)
    #
    # def test_3(self, browser, stand):
    #     page = HomePage(browser, stand)
    #     page.open(page='action_log')
    #     Waiting(browser).wait_until_visibility_of_element(locator_text=page.FIRST_ROW)
    #     page.web_scroll(direction='down')
    #     page.assert_table_titles()
    #     page.assert_filter_btns_hidden()

