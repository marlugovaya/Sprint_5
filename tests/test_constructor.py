
from Sprint_5.locators import TestLocators
from Sprint_5.data import TestData


class TestConstructor:

    # Переход на вкладку Соусы
    def test_switch_to_souces(self, driver, login):
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_elements(*TestLocators.CONSTRUCTOR_TABS)[1].click()
        assert (driver.find_element(*TestLocators.CONSTRUCTOR_SELECTED_TAB).text == 'Соусы')

    # Переход на вкладку Начинки
    def test_switch_to_fillings(self, driver, login):
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_elements(*TestLocators.CONSTRUCTOR_TABS)[2].click()
        assert (driver.find_element(*TestLocators.CONSTRUCTOR_SELECTED_TAB).text == 'Начинки')

    # Переход на вкладку Булки
    def test_switch_to_buns(self, driver, login):
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_elements(*TestLocators.CONSTRUCTOR_TABS)[1].click()
        driver.find_elements(*TestLocators.CONSTRUCTOR_TABS)[0].click()
        assert (driver.find_element(*TestLocators.CONSTRUCTOR_SELECTED_TAB).text == 'Булки')
