import time

from Pages.PageObjects.ui_pages.HomePage import HomePage
from Common.CommonFuncs.waitings import Waiting
import allure
import pytest


class TestHomePage:

    @pytest.fixture()
    def setup(self, browser):
        page = HomePage(browser)
        page.open()
        time.sleep(5)

        Waiting(browser).wait_until_button_clickable(locator_text=page.PROFILE)
        page.click(locator=page.PROFILE)
        page.click(locator=page.CODE_BUTTON)
        page.click(locator=page.RUS_CODE)
        page.send_keys('9771858108', locator=page.CODE_INPUT)
        page.click(locator=page.LOG_IN_BUTTON)
        browser.implicitly_wait(time_to_wait=10)

        yield page

    def test_profile_name(self, browser, setup):
        page = HomePage(browser)

        Waiting(browser).wait_until_text_to_be_present_in_element(text='Komron', locator_text=page.PROFILE_NAME)
        page.assert_profile_name()



