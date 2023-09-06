from test_utils import *
from pages.index_page import IndexPage
from pages.books_page import BooksStorePage
from pages.shopping_cart_status_page import ShoppingCartStatusPage
from resources.constants import TEST_SITE_URL


class TestLogin:
    # Test scenario (item add to cart)
    def test_add_books_to_cart(self, driver):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_item_books()
        books_page = BooksStorePage(driver)
        books_page.click_add_to_cart()
        books_page = BooksStorePage(driver)
        add_to_cart_success_label = books_page.get_add_to_cart_success_label()
        assert add_to_cart_success_label == "The product has been added to your shopping cart", "User success message failed!"
        close_cross = BooksStorePage(driver)
        close_cross.click_on_cross()
        check_in_shopping_cart = BooksStorePage(driver)
        check_in_shopping_cart.click_on_shopping_cart()

        shopping_cart_status_page = ShoppingCartStatusPage(driver)

        shopping_cart_status_success_lbl = shopping_cart_status_page.get_shopping_cart_status_success_lbl()
        assert shopping_cart_status_success_lbl == "Fahrenheit 451 by Ray Bradbury", "Error! Msg Failed!"
