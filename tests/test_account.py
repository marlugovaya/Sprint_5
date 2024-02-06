
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Sprint_5.locators import TestLocators
from Sprint_5.data import TestData, login

class TestAccount:

    # Переход по клику на «Личный кабинет»
    def test_move_to_account(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert (driver.current_url == "https://stellarburgers.nomoreparties.site/login")

    # Переход из Личного кабинета в Конструктор
    def test_move_to_constructor(self,driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        login(driver, TestData.GOOD_LOGIN_PASSWORD[0], TestData.GOOD_LOGIN_PASSWORD[1])

        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        assert (driver.current_url == "https://stellarburgers.nomoreparties.site/")

    # Переход из Личного кабинета по логотипу
    def test_move_to_logo(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        login(driver, TestData.GOOD_LOGIN_PASSWORD[0], TestData.GOOD_LOGIN_PASSWORD[1])

        driver.find_element(*TestLocators.STELLAR_BURGERS_LOGO).click()
        assert (driver.current_url == "https://stellarburgers.nomoreparties.site/")

    # Выход по кнопке «Выйти» в личном кабинете
    def test_logout(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        login(driver, TestData.GOOD_LOGIN_PASSWORD[0], TestData.GOOD_LOGIN_PASSWORD[1])
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert (driver.current_url == 'https://stellarburgers.nomoreparties.site/login')
