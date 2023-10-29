from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class Actions(ActionChains):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def copy(self):
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).perform()
        actions.send_keys("c").perform()
        actions.key_up(Keys.CONTROL).perform()

    def delete(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DELETE).perform()

    def backspace(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.BACKSPACE).perform()

    def enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def hover_over(self, element):
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

    def escape(self):
        action_chains = ActionChains(self.driver)
        action_chains.send_keys(Keys.ESCAPE).perform()

    def select_all(self):
        action_chains = ActionChains(self.driver)
        action_chains.key_down(Keys.CONTROL).perform()
        action_chains.send_keys(Keys.SHIFT + "a").perform()
        action_chains.key_up(Keys.CONTROL).perform()

    def right_click(self, element):
        action_chains = ActionChains(self.driver)
        action_chains.context_click(element).perform()

    def move_to_element_and_click(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
