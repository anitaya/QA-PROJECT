from pages.base_page import BasePage
from pages.books_page_locators import BooksPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class BooksStorePage(BasePage):

    def click_add_to_cart(self):
        self.find_element(BooksPageLocators.ADD_TO_CART).click()

    def get_add_to_cart_success_label(self):
        lbl_add_to_cart_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, BooksPageLocators.SUCCESS_MSG_ADD_TO_CART).text
        return lbl_add_to_cart_success_txt

    def click_on_cross(self):
        self.find_element(BooksPageLocators.CLOSE_THE_CROSS).click()

    def click_on_shopping_cart(self):
        self.find_element(BooksPageLocators.CLICK_SHOPPING_CART).click()
