from selenium.webdriver.common.by import By


class RegisterSuccessPageLocators:
    REGISTER_SUCCESS_LBL = (By.XPATH, "//div[@class='result']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@class='button-1 register-continue-button']")
