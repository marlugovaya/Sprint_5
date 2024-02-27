import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Sprint_5.locators import TestLocators
from Sprint_5.data import TestData
from Sprint_5.helpers import generate_email

class TestRegistration:

    # Успешная регистрация
    def test_registration_success(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()

        inputs_reg = driver.find_elements(*TestLocators.INPUTS_FOR_LOGIN)
        inputs_reg[0].send_keys('Совсем новое имя пользователя')
        new_login = generate_email()
        new_password = TestData.GOOD_LOGIN_PASSWORD[1]
        inputs_reg[1].send_keys(new_login)
        inputs_reg[2].send_keys(new_password)

        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        inputs = driver.find_elements(*TestLocators.INPUTS_FOR_LOGIN)
        inputs[0].send_keys(new_login)
        inputs[1].send_keys(new_password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BUTTON))
        assert (driver.find_element(*TestLocators.PROFILE_BUTTON).is_displayed())

    # Ошибка для некорректного пароля
    def test_registration_incorrect_password(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()

        inputs_reg = driver.find_elements(*TestLocators.INPUTS_FOR_LOGIN)
        inputs_reg[0].send_keys('Совсем новое имя пользователя')
        new_login = generate_email()
        new_password = TestData.BAD_LOGIN_PASSWORD[1]
        inputs_reg[1].send_keys(new_login)
        inputs_reg[2].send_keys(new_password)

        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        error = driver.find_element(*TestLocators.INCORRECT_PASSWORD_ERROR)
        assert (error.is_displayed())
