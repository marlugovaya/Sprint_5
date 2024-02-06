import random
from Sprint_5.locators import TestLocators


def login(driver, email, password):
    inputs = driver.find_elements(*TestLocators.INPUTS_FOR_LOGIN)
    inputs[0].send_keys(email)
    inputs[1].send_keys(password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()


def generate_email():
    email = "margatitalugovaya5" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + "@yandex.ru"
    return email


class TestData:

    GOOD_LOGIN_PASSWORD = "margatitalugovaya5222@yandex.ru","coolpassword123"
    BAD_LOGIN_PASSWORD = "margatitalugovaya5222@yandex.ru","1234"

