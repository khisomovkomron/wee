from Common.CommonFuncs.waitings import Waiting
from Common.CommonFuncs.webcommon import WebDriverFactory
from Common.CommonFuncs.assertions import Assertions
from Configs.Locators.home_page import HOME_PAGE



class HomePage(WebDriverFactory):

    PROFILE = HOME_PAGE['profile']['locator']
    CODE_BUTTON = HOME_PAGE['code_button']['locator']
    RUS_CODE = HOME_PAGE['rus_code']['locator']
    CODE_INPUT = HOME_PAGE['code_input']['locator']
    LOG_IN_BUTTON = HOME_PAGE['log_in_button']['locator']
    PROFILE_NAME = HOME_PAGE['profile_name']['locator']

    def assert_profile_name(self):
        assertion = Assertions(self.browser)
        assertion.assert_element_contains_text('Komron', locator_type='xpath', locator=self.PROFILE_NAME)


