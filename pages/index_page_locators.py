from selenium.webdriver.common.by import By


class IndexPageLocators:
    REGISTER_LINK = (By.XPATH, "//a[@class='ico-register']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Log in']")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Log out']")
    ITEM_BOOKS = (By.XPATH, "//a[@href='/books']")
    WELCOME_LINK = (By.XPATH, "//div[@class='topic-block-title']")
