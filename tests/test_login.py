from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


from Sprint_5.locators import TestLocators
from Sprint_5.data import TestData, login

import time

class TestLogin:

    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_main(self, driver):
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        login(driver, TestData.GOOD_LOGIN_PASSWORD[0], TestData.GOOD_LOGIN_PASSWORD[1])

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BUTTON))
        assert (driver.find_element(*TestLocators.PROFILE_BUTTON).is_displayed())

    # Вход через кнопку «Личный кабинет»
    def test_login_account(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        login(driver, TestData.GOOD_LOGIN_PASSWORD[0], TestData.GOOD_LOGIN_PASSWORD[1])

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BUTTON))
        assert (driver.find_element(*TestLocators.PROFILE_BUTTON).is_displayed())

    # Вход через кнопку в форме регистрации
    def test_login_registration(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()
        driver.find_element(*TestLocators.LOGIN_LINK).click()

        login(driver, TestData.GOOD_LOGIN_PASSWORD[0], TestData.GOOD_LOGIN_PASSWORD[1])

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BUTTON))
        assert (driver.find_element(*TestLocators.PROFILE_BUTTON).is_displayed())

    # Вход через кнопку в форме восстановления пароля
    def test_login_password_recovery(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.PASSWORD_RECOVERY_LINK).click()
        driver.find_element(*TestLocators.LOGIN_LINK).click()

        login(driver, TestData.GOOD_LOGIN_PASSWORD[0], TestData.GOOD_LOGIN_PASSWORD[1])

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BUTTON))
        assert (driver.find_element(*TestLocators.PROFILE_BUTTON).is_displayed())
