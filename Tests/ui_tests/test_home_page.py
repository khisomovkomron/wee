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
        Waiting(browser).explicit_wait(locator_text=page.PROFILE)
        page.click(locator=page.PROFILE)
        page.click(locator=page.CODE_BUTTON)
        page.click(locator=page.RUS_CODE)
        page.send_keys('9771858108', locator=page.CODE_INPUT)
        page.click(locator=page.LOG_IN_BUTTON)
        browser.implicitly_wait(time_to_wait=10)
        time.sleep(5)
        yield page

    def test_profile_name(self, browser, setup):
        page = HomePage(browser)
        page.assert_profile_name()



