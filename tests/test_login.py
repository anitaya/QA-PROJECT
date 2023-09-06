from test_utils import *
from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from pages.welcome_sign_in_page import WelcomeSignInPage
from resources.constants import TEST_SITE_URL


class TestLogin:

    # Test Case 1 ( Registering the user)
    def test_register_new_user(self, driver, register_feature):
        index_page = IndexPage(driver)

        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()

        register_page = RegisterPage(driver)
        register_page.wait_and_type_user_first_name(register_feature)
        register_page.type_user_last_name(register_feature)
        register_page.type_user_email(register_feature)
        register_page.type_user_email_password(register_feature)
        register_page.type_user_email_confirm_password(register_feature)
        register_page.click_register_btn()

        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()

        assert register_success_lbl == "Your registration completed", "User registration failed!"
        continue_btn = RegisterSuccessPage(driver)
        continue_btn.click_continue_btn()

    # Test Case  2 (login page)

    def test_log_in(self, driver, register_feature):
        index_page = IndexPage(driver)
        # index_page.navigate_to(TEST_SITE_URL)
        # try:
        #     index_page.wait_and_click_logout_button()
        # except Exception as e:
        #     print(e)
        index_page.wait_and_click_login_button()

        welcome_sign_in_page = WelcomeSignInPage(driver)
        welcome_sign_in_page.wait_and_type_user_email(register_feature)
        welcome_sign_in_page.type_user_password(register_feature)
        welcome_sign_in_page.click_login_btn()
        welcome_page_lbl = index_page.get_welcome_page_label()

        assert welcome_page_lbl == "Welcome to our store", "Error! Login Failed!"

    def test_log_out(self, driver):

        logout_page = IndexPage(driver)
        logout_page.navigate_to(TEST_SITE_URL)

        logout_page.click_logout_link()
        assert "https://demo.nopcommerce.com/" == TEST_SITE_URL, "Logout not successfully"
