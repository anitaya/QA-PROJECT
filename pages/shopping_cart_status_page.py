from pages.base_page import BasePage
from pages.shopping_cart_status_page_locators import ShoppingCartStatusPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ShoppingCartStatusPage(BasePage):
    def get_shopping_cart_status_success_lbl(self):
        shopping_cart_status_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, ShoppingCartStatusPageLocators.SHOPPING_CART_STATUS_SUCCESS_MSG).text
        return shopping_cart_status_success_txt


