from selenium.webdriver.common.by import By


class BooksPageLocators:
    ADD_TO_CART = (By.XPATH, "/html/body/div[6]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/button[1]")
    SUCCESS_MSG_ADD_TO_CART = (By.XPATH, "//p")
    CLOSE_THE_CROSS = (By.XPATH, "//span[@class='close']")
    CLICK_SHOPPING_CART = (By.XPATH, "//span[@class='cart-label']")
