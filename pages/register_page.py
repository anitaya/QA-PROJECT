from pages.base_page import BasePage
from pages.register_page_locators import RegisterPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class RegisterPage(BasePage):

    def wait_and_type_user_first_name(self, registerFeature):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                              RegisterPageLocators.USER_NAME_FIRST_NAME_BOX).send_keys(
            registerFeature[0])

    def type_user_last_name(self, registerFeature):
        self.find_element(RegisterPageLocators.USER_NAME_LAST_NAME_BOX).send_keys(
            registerFeature[1])

    def type_user_email(self, registerFeature):
        self.find_element(RegisterPageLocators.USER_EMAIL_TEXT_BOX).send_keys(
            registerFeature[2])

    def type_user_email_password(self, registerFeature):
        self.find_element(RegisterPageLocators.USER_NAME_PASSWORD).send_keys(
            registerFeature[3])

    def type_user_email_confirm_password(self, registerFeature):
        self.find_element(RegisterPageLocators. CONFIRM_PASSWORD_TEXT_BOX).send_keys(
            registerFeature[3])

    def click_register_btn(self):
        self.find_element(RegisterPageLocators.REGISTER_BUTTON).click()
