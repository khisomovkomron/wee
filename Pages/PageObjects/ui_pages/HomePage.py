from Common.CommonFuncs.waitings import Waiting
from Common.CommonFuncs.webcommon import WebDriverFactory
from Common.CommonFuncs.assertions import Assertions
from Configs.Locators.home_page import HOME_PAGE



class HomePage(WebDriverFactory):

    PROFILE_NAME = HOME_PAGE['profile_name']['locator']


    def assert_table_titles(self):
        assertion = Assertions(self.browser)
        assertion.assert_element_contains_text('Komron', locator=self.PROFILE_NAME)


