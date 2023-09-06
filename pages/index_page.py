from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class IndexPage(BasePage):

    def wait_and_click_register_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.REGISTER_LINK).click()

    def wait_and_click_login_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.LOGIN_LINK).click()

    def wait_and_click_logout_button(self):
        self.explicitly_wait_and_find_element(5, IndexPageLocators.LOGOUT_LINK).click()

    def wait_and_click_item_books(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.ITEM_BOOKS).click()

    def get_welcome_page_label(self):
        welcome_page_lbl = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, IndexPageLocators.WELCOME_LINK).text
        return welcome_page_lbl

    def click_logout_link(self):
        self.find_element(IndexPageLocators.LOGOUT_LINK).click()
