from selenium.webdriver.common.by import By


class RegisterPageLocators:
    USER_NAME_FIRST_NAME_BOX = (By.ID, "FirstName")
    USER_NAME_LAST_NAME_BOX = (By.ID, "LastName")
    USER_EMAIL_TEXT_BOX = (By.ID, "Email")
    USER_NAME_PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD_TEXT_BOX = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
