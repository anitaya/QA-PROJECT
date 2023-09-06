import random

# Generate a random integer with 4 digits
random_number = random.randint(1000, 9999)
import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope="module")
def register_feature():
    firstname = "charles"
    lastname = "david"

    password = "charles"
    # Generate a random integer with 4 digits
    random_number = random.randint(1000, 9999)
    user_email = str(random_number) + "charles100@gmail.com"

    return [firstname, lastname, user_email, password]
