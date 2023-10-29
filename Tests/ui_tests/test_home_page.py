from Pages.PageObjects.ui_pages.HomePage import HomePage
from Common.CommonFuncs.assertions import Assertions
from Common.CommonFuncs.waitings import Waiting
import allure


class TestTable:

    def test_1(self, browser):
        page = HomePage(browser)
        assertion = Assertions(browser)
        page.open()
        # page.click(locator=page.ACTION_LOG_MENU)
        # assertion.assert_url_contains('action_log')
        # page.assert_filter_btns()
        # page.assert_table_titles()
        # page.assert_table_cells()

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

