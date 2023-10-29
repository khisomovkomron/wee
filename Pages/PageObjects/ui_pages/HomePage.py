from Common.CommonFuncs.waitings import Waiting
from Common.CommonFuncs.webcommon import WebDriverFactory
from Common.CommonFuncs.assertions import Assertions
from Configs.Locators.home_page import ACTION_LOG
from Configs.Locators.Menu import MENU
from Configs.Locators.FilterComponent import FILTER
from Configs.Locators.SidePanelBtns import SIDE_PANEL


class ActionLogPage(WebDriverFactory):

    ACTION_LOG_MENU = MENU['action_log']['locator']
    SEARCH_INP = FILTER['search_inp']['locator']
    CHAPTER_HEADER = ACTION_LOG['chapter_header']['locator']
    CHAPTER_CELL = ACTION_LOG['chapter_cell']['locator']
    ACTION_HEADER = ACTION_LOG['action_header']['locator']
    ACTION_CELL = ACTION_LOG['action_cell']['locator']
    PARENT_HEADER = ACTION_LOG['parent_header']['locator']
    PARENT_CELL = ACTION_LOG['parent_cell']['locator']
    OBJECT_HEADER = ACTION_LOG['object_header']['locator']
    OBJECT_CELL = ACTION_LOG['object_cell']['locator']
    NAME_HEADER = ACTION_LOG['name_header']['locator']
    NAME_CELL = ACTION_LOG['name_cell']['locator']
    OLD_VALUE_HEADER = ACTION_LOG['old_value_header']['locator']
    OLD_VALUE_CELL = ACTION_LOG['old_value_cell']['locator']
    NEW_VALUE_HEADER = ACTION_LOG['new_value_header']['locator']
    NEW_VALUE_CELL = ACTION_LOG['new_value_cell']['locator']
    UPDATES_HEADER = ACTION_LOG['updates_header']['locator']
    UPDATES_CELL = ACTION_LOG['updates_cell']['locator']
    FIRST_ROW = ACTION_LOG['first_row']['locator']
    DETAIL_INFO_HEADER = ACTION_LOG['detail_info_header']['locator']
    DETAIL_INFO_ID = ACTION_LOG['detail_info_id']['locator']
    CHAPTER_LABEL = ACTION_LOG['chapter_label']['locator']
    CHAPTER_INPUT = ACTION_LOG['chapter_input']['locator']
    ACTION_LABEL = ACTION_LOG['action_label']['locator']
    ACTION_INPUT = ACTION_LOG['action_input']['locator']
    PARENT_OBJECT_LABEL = ACTION_LOG['parent_object_label']['locator']
    PARENT_OBJECT_INPUT = ACTION_LOG['parent_object_input']['locator']
    OBJECT_ID_LABEL = ACTION_LOG['object_id_label']['locator']
    OBJECT_ID_INPUT = ACTION_LOG['object_id_input']['locator']
    OBJECT_LABEL = ACTION_LOG['object_label']['locator']
    OBJECT_INPUT = ACTION_LOG['object_input']['locator']
    NAME_LABEL = ACTION_LOG['name_label']['locator']
    NAME_INPUT = ACTION_LOG['name_input']['locator']
    OLD_VALUE_LABEL = ACTION_LOG['old_value_label']['locator']
    OLD_VALUE_INPUT = ACTION_LOG['old_value_input']['locator']
    NEW_VALUE_LABEL = ACTION_LOG['new_value_label']['locator']
    NEW_VALUE_INPUT = ACTION_LOG['new_value_input']['locator']
    UPDATED_BY_LABEL = ACTION_LOG['updated_by_label']['locator']
    UPDATED_BY_INPUT = ACTION_LOG['updated_by_input']['locator']
    UPDATED_LABEL = ACTION_LOG['updated_label']['locator']
    UPDATED_INPUT = ACTION_LOG['updated_input']['locator']
    CLOSE_BTN = ACTION_LOG['close_btn']['locator']
    SIDE_PANEL_TITLE = SIDE_PANEL['title']['locator']
    SIDE_PANEL_DESCRIPTION = SIDE_PANEL['description']['locator']
    SIDE_PANEL_CLOSE_BTN = SIDE_PANEL['close_btn']['locator']
    OUTSIDE_SIDE_PANEL = SIDE_PANEL['outside_side_panel']['locator']

    def assert_table_titles(self):
        assertion = Assertions(self.browser, self.stand)
        assertion.assert_element_contains_text('Раздел', locator=self.CHAPTER_HEADER)
        assertion.assert_element_contains_text('Действие', locator=self.ACTION_HEADER)
        assertion.assert_element_contains_text('Родительский объект', locator=self.PARENT_HEADER)
        assertion.assert_element_contains_text('Объект', locator=self.OBJECT_HEADER)
        assertion.assert_element_contains_text('Наименование', locator=self.NAME_HEADER)
        assertion.assert_element_contains_text('Старое значение', locator=self.OLD_VALUE_HEADER)
        assertion.assert_element_contains_text('Новое значение', locator=self.NEW_VALUE_HEADER)
        assertion.assert_element_contains_text('Изменения', locator=self.UPDATES_HEADER)

    def assert_table_cells(self):
        assertion = Assertions(self.browser, self.stand)
        assertion.assert_element_contains_any_text(locator=self.CHAPTER_CELL)
        assertion.assert_element_contains_any_text(locator=self.ACTION_CELL)
        assertion.assert_element_contains_any_text(locator=self.PARENT_CELL)
        assertion.assert_element_contains_any_text(locator=self.OBJECT_CELL)
        assertion.assert_element_contains_any_text(locator=self.NAME_CELL)
        assertion.assert_element_contains_any_text(locator=self.OLD_VALUE_CELL)
        assertion.assert_element_contains_any_text(locator=self.NEW_VALUE_CELL)
        assertion.assert_element_contains_any_text(locator=self.UPDATES_CELL)

    def assert_filter_btns(self):
        assertion = Assertions(self.browser, self.stand)
        assertion.assert_element_is_visible(locator=FILTER['search_inp']['locator'])
        Waiting(self.browser).wait_until_visibility_of_element(locator_text=FILTER['open_filter_btn']['locator'])
        assertion.assert_element_displayed(locator=FILTER['open_filter_btn']['locator'])
        assertion.assert_element_displayed(locator=FILTER['items_counter']['locator'])

    def assert_filter_btns_hidden(self):
        assertion = Assertions(self.browser, self.stand)
        Waiting(self.browser).wait_until_invisibility_of_element(locator=FILTER['open_filter_btn']['locator'])
        assertion.assert_element_is_not_displayed(locator=FILTER['search_inp']['locator'])
        assertion.assert_element_is_not_displayed(locator=FILTER['open_filter_btn']['locator'])
        assertion.assert_element_is_not_displayed(locator=FILTER['items_counter']['locator'])

    def wait_for_table(self, timeout=10):
        Waiting(self.browser).wait_until_visibility_of_element(locator_text=self.FIRST_ROW, timeout=timeout)

    def assert_sidepanel(self):
        assertion = Assertions(self.browser, self.stand)
        assertion.assert_element_contains_text('Детальная информация', locator=self.SIDE_PANEL_TITLE)
        assertion.assert_element_contains_text('ID:', locator=self.SIDE_PANEL_DESCRIPTION)
        assertion.assert_element_contains_text('Раздел', locator=self.CHAPTER_LABEL)
        assertion.assert_element_contains_text('Действие', locator=self.ACTION_LABEL)
        assertion.assert_element_contains_text('Родительский объект', locator=self.PARENT_OBJECT_LABEL)
        assertion.assert_element_contains_text('ID Объекта', locator=self.OBJECT_ID_LABEL)
        assertion.assert_element_contains_text('Объект', locator=self.OBJECT_LABEL)
        assertion.assert_element_contains_text('Наименование', locator=self.NAME_LABEL)
        assertion.assert_element_contains_text('Старое значение', locator=self.OLD_VALUE_LABEL)
        assertion.assert_element_contains_text('Новое значение', locator=self.NEW_VALUE_LABEL)
        assertion.assert_element_contains_text('Пользователь', locator=self.UPDATED_BY_LABEL)
        assertion.assert_element_contains_text('Изменения', locator=self.UPDATED_LABEL)
        assertion.assert_element_is_visible(locator=self.CHAPTER_INPUT)
        assertion.assert_element_is_visible(locator=self.ACTION_INPUT)
        assertion.assert_element_is_visible(locator=self.PARENT_OBJECT_INPUT)
        assertion.assert_element_is_visible(locator=self.OBJECT_ID_INPUT)
        assertion.assert_element_is_visible(locator=self.OBJECT_INPUT)
        assertion.assert_element_is_visible(locator=self.NAME_INPUT)
        assertion.assert_element_is_visible(locator=self.OLD_VALUE_INPUT)
        assertion.assert_element_is_visible(locator=self.NEW_VALUE_INPUT)
        assertion.assert_element_is_visible(locator=self.UPDATED_BY_INPUT)
        assertion.assert_element_is_visible(locator=self.UPDATED_INPUT)
        assertion.assert_element_is_visible(locator=self.SIDE_PANEL_CLOSE_BTN)
