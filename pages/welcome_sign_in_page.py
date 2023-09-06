from pages.base_page import BasePage
from pages.welcome_sign_in_page_locators import WelcomeSignInPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class WelcomeSignInPage(BasePage):

    def wait_and_type_user_email(self, registeredFeature):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, WelcomeSignInPageLocators.USER_EMAIL_TXT_BOX).send_keys(
            registeredFeature[2])

    def type_user_password(self, registeredFeature):
        self.find_element(WelcomeSignInPageLocators.PASSWORD_BOX).send_keys(
           registeredFeature[3])

    def click_login_btn(self):
        self.find_element(WelcomeSignInPageLocators.LOGIN_BUTTON).click()
