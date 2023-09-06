from selenium.webdriver.common.by import By


class WelcomeSignInPageLocators:
    USER_EMAIL_TXT_BOX = (By.XPATH, "//input[@class='email']")
    PASSWORD_BOX = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='button-1 login-button']")
